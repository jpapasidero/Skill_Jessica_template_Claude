#!/usr/bin/env python3
"""
Générateur de présentation au template "Palette Jessica" (Safran).

Usage :
    python generate_pptx.py --content content.json --output out.pptx [--logo logo.png]

Le fichier content.json contient une liste de slides, chacune décrivant son
layout (1..11) et le contenu textuel à injecter dans les placeholders nommés.

Voir references/content_schema.md pour le contrat d'entrée détaillé.
"""
import argparse
import json
import sys
from pathlib import Path
from pptx import Presentation
from pptx.util import Cm

# Permettre l'exécution directe ET en module
try:
    from .builders import build_slide
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from builders import build_slide


# Format slide : 33.87 × 19.05 cm (16:9 widescreen)
SLIDE_W_CM = 33.867
SLIDE_H_CM = 19.05


def init_presentation():
    """Crée une présentation vierge au bon format."""
    prs = Presentation()
    prs.slide_width = Cm(SLIDE_W_CM)
    prs.slide_height = Cm(SLIDE_H_CM)
    return prs


def generate(content_path, output_path, logo_path=None):
    with open(content_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    prs = init_presentation()
    slides_data = data.get("slides", [])
    total = len(slides_data)

    # layout vide ("blank") pour chaque slide
    blank_layout = prs.slide_layouts[6]  # généralement "Blank" en index 6

    for i, sd in enumerate(slides_data, start=1):
        layout_n = sd.get("layout")
        if layout_n is None:
            print(f"[WARN] slide {i} : champ 'layout' manquant, skip", file=sys.stderr)
            continue
        slide = prs.slides.add_slide(blank_layout)
        # nettoyer les placeholders éventuels du layout blank (pour partir vraiment de zéro)
        for shp in list(slide.placeholders):
            sp = shp._element
            sp.getparent().remove(sp)

        try:
            build_slide(layout_n, slide, sd.get("content", {}),
                        page_num=i, total=total, logo_path=logo_path)
        except Exception as e:
            print(f"[ERROR] slide {i} layout {layout_n} : {e}", file=sys.stderr)
            raise

    prs.save(output_path)
    print(f"[OK] Présentation générée : {output_path} ({total} slides)")


def main():
    ap = argparse.ArgumentParser(description="Générateur PPTX Palette Jessica")
    ap.add_argument("--content", required=True, help="Fichier JSON de contenu")
    ap.add_argument("--output", required=True, help="Fichier .pptx de sortie")
    ap.add_argument("--logo", default=None, help="Chemin vers le logo Safran (PNG)")
    args = ap.parse_args()
    generate(args.content, args.output, logo_path=args.logo)


if __name__ == "__main__":
    main()