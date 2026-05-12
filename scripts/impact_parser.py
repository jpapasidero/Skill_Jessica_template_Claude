#!/usr/bin/env python3
"""
Parseur de fichiers d'analyse d'impact PPTX (format Safran).

Extrait les données des zones nommées TITLE, ZONE_OMOC et RESSORTS_CHANGE
de chaque slide pour générer des entrées Layout 15 (Matrice d'impact par population).

Usage standalone :
    python impact_parser.py <chemin_analyse_impact.pptx> [--json]
"""
import json
import re
import sys
from pathlib import Path

from pptx import Presentation
from pptx.util import Emu


# ---------------------------------------------------------------------------
# Constantes géométriques du radar OMOC (GAP MEASURE)
# ---------------------------------------------------------------------------
# Le radar est un diamant centré dans l'image ZONE_OMOC.
# Image : pos=(0.0, 3.25) cm, taille=(11.37, 9.57) cm
# Centre du diamant (en coordonnées slide) :
OMOC_CENTER_X = 5.685   # cm
OMOC_CENTER_Y = 8.035   # cm

# Pas unique (calibré empiriquement sur le template Safran).
# Distance en cm entre deux niveaux concentriques du radar.
OMOC_STEP = 0.93  # cm par niveau

# Noms des Ellipses portant les bullets OMOC (identiques sur chaque slide)
OMOC_BULLET_NAMES = {'5', '7', '10', '14'}

# Axes du radar :
#   Organisation = axe vertical vers le haut (y décroissant)
#   Métier       = axe horizontal vers la droite (x croissant)
#   Outils       = axe vertical vers le bas (y croissant)
#   Culture      = axe horizontal vers la gauche (x décroissant)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _classify_omoc_bullet(x_cm, y_cm, w_cm, h_cm):
    """
    Détermine l'axe OMOC et le niveau (0-4) d'un bullet à partir de sa
    position et taille sur le slide.

    Retourne (axis_name, level) où axis_name ∈ {Organization, Business, Tool, Culture}.
    """
    # Centre du bullet
    cx = x_cm + w_cm / 2
    cy = y_cm + h_cm / 2

    dx = cx - OMOC_CENTER_X
    dy = OMOC_CENTER_Y - cy  # inversé : y monte = dy positif

    # Déterminer l'axe le plus proche
    if abs(dx) > abs(dy):
        axis = 'Business' if dx > 0 else 'Culture'
        distance = abs(dx)
    else:
        axis = 'Organization' if dy > 0 else 'Tool'
        distance = abs(dy)

    level = round(distance / OMOC_STEP)
    level = max(0, min(4, level))
    return axis, level


def _summarize_levers(table):
    """
    Résume les actions de la table RESSORTS_CHANGE en une seule chaîne
    pour la colonne « Leviers retenus » du Layout 15.

    Chaque ligne d'action commence par son type (Communication, Support,
    Mobilisation, Formation). On extrait ces types uniques comme résumé.
    """
    action_types = []
    seen = set()

    for ri in range(1, len(table.rows)):
        action_cell = table.cell(ri, 1).text.strip()
        if not action_cell:
            continue
        # Le premier mot/ligne est souvent le type d'action
        first_line = action_cell.split('\n')[0].strip()
        # Nettoyer : souvent "Communication", "Support", "Mobilisation", "Formation"
        action_type = first_line.rstrip(':').strip()
        if action_type and action_type.lower() not in seen:
            seen.add(action_type.lower())
            action_types.append(action_type)

    return ' | '.join(action_types)


def _parse_title(title_text):
    """
    Sépare le texte du TITLE en (population, effectif).

    Formats attendus :
      - "Population – N personnes"
      - "Population - N personnes"
      - "Population" (sans effectif)

    Retourne (population, effectif) où effectif = "TBD" si absent.
    """
    # Essayer en-dash d'abord, puis tiret simple
    for sep in ['\u2013', '-']:
        if sep in title_text:
            parts = title_text.split(sep, 1)
            population = parts[0].strip()
            effectif_raw = parts[1].strip()
            if effectif_raw:
                return population, f"~ {effectif_raw}"
            break
    else:
        population = title_text.strip()

    return population, "TBD"


# ---------------------------------------------------------------------------
# Parsing principal
# ---------------------------------------------------------------------------

def parse_impact_file(pptx_path):
    """
    Parse un fichier d'analyse d'impact PPTX et retourne une liste de
    dictionnaires, un par slide/population :

    [
        {
            "population": "Garants de fabricabilité",
            "effectif": "~ 5 personnes",
            "omoc": {"Tool": 1, "Business": 1, "Organization": 2, "Culture": 2},
            "levers": "Communication | Support"
        },
        ...
    ]
    """
    prs = Presentation(str(pptx_path))
    populations = []

    for slide in prs.slides:
        entry = {
            "population": "",
            "effectif": "TBD",
            "omoc": {"Tool": 0, "Business": 0, "Organization": 0, "Culture": 0},
            "levers": ""
        }

        for shape in slide.shapes:
            name = shape.name.strip()

            # --- TITLE / TITRE ---
            if name in ('TITLE', 'TITRE'):
                title_text = shape.text_frame.text.strip()
                entry["population"], entry["effectif"] = _parse_title(title_text)

            # --- ZONE_OMOC bullets (Ellipse 5, 7, 10, 14) ---
            if 'Ellipse' in name:
                parts = name.split()
                if len(parts) >= 2 and parts[-1] in OMOC_BULLET_NAMES:
                    x = Emu(shape.left).cm
                    y = Emu(shape.top).cm
                    w = Emu(shape.width).cm
                    h = Emu(shape.height).cm
                    axis, level = _classify_omoc_bullet(x, y, w, h)
                    entry["omoc"][axis] = level

            # --- RESSORTS_CHANGE ---
            if name == 'RESSORTS_CHANGE':
                entry["levers"] = _summarize_levers(shape.table)

        # N'ajouter que les slides qui ont un titre exploitable
        if entry["population"]:
            populations.append(entry)

    return populations


# ---------------------------------------------------------------------------
# Génération du contenu Layout 15
# ---------------------------------------------------------------------------

def build_layout15_slides(populations):
    """
    Convertit la liste de populations en entrées content.json pour le Layout 15.

    Règles :
    - Maximum 6 populations par slide Layout 15
    - Si > 6 populations, créer des slides supplémentaires
    - Mapping :
        label    → nom de la population (S15_TABLE_LABEL_Ri)
        sublabel → effectif (S15_TABLE_SUBLABEL_Ri)
        impacts  → [Outils, Métier, Organisation, Culture] (S15_TABLE_Ri_Ci)
        levers   → résumé RESSORTS_CHANGE (S15_TABLE_Ri_C6)
    """
    slides = []

    # Chunking par paquets de 6
    for chunk_start in range(0, len(populations), 6):
        chunk = populations[chunk_start:chunk_start + 6]

        rows = []
        for pop in chunk:
            omoc = pop["omoc"]
            rows.append({
                "label": pop["population"],
                "sublabel": pop["effectif"],
                "impacts": [
                    omoc.get("Tool", 0),         # Outils
                    omoc.get("Business", 0),      # Métier
                    omoc.get("Organization", 0),  # Organisation
                    omoc.get("Culture", 0),       # Culture
                ],
                "levers": pop["levers"]
            })

        slide_entry = {
            "layout": 15,
            "content": {
                "title": "Impact par population",
                "headers": [
                    "Outils", "Métier", "Organisation", "Culture",
                    "Leviers retenus"
                ],
                "rows": rows,
                "legend_title": "Intensité",
                "legend": ["Faible", "Modéré", "Fort", "Très fort"],
                "footnote": "Leviers = axes d'accompagnement prioritaires par population"
            }
        }
        slides.append(slide_entry)

    return slides


def generate_impact_content(pptx_path):
    """
    Fonction principale : parse le fichier d'analyse d'impact et retourne
    la liste de slides Layout 15 prête à être insérée dans le content.json.
    """
    populations = parse_impact_file(pptx_path)
    return build_layout15_slides(populations)


# ---------------------------------------------------------------------------
# Mode standalone
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python impact_parser.py <fichier_analyse_impact.pptx> [--json]",
              file=sys.stderr)
        sys.exit(1)

    pptx_path = sys.argv[1]
    output_json = "--json" in sys.argv

    populations = parse_impact_file(pptx_path)

    if output_json:
        slides = build_layout15_slides(populations)
        print(json.dumps({"slides": slides}, ensure_ascii=False, indent=2))
    else:
        print(f"Populations extraites : {len(populations)}")
        print("=" * 70)
        for i, pop in enumerate(populations, 1):
            omoc = pop["omoc"]
            print(f"\n[{i}] {pop['population']}")
            print(f"    Effectif     : {pop['effectif']}")
            print(f"    Outils       : {omoc['Tool']}")
            print(f"    Métier       : {omoc['Business']}")
            print(f"    Organisation : {omoc['Organization']}")
            print(f"    Culture      : {omoc['Culture']}")
            print(f"    Leviers      : {pop['levers']}")

        print(f"\n=> {len(populations)} populations => "
              f"{(len(populations) + 5) // 6} slide(s) Layout 15")
