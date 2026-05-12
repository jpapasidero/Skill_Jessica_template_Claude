# Content Schema — Palette Jessica

Ce fichier décrit, layout par layout, la structure JSON attendue par `generate_pptx.py` pour chaque slide.

## Structure générale

```json
{
  "slides": [
    { "layout": <1..11>, "content": { ... } },
    { "layout": <1..11>, "content": { ... } }
  ]
}
```

Tous les `content` peuvent inclure un champ `"title"` (titre de la slide). S'il est omis, le titre par défaut du layout est utilisé.

Le générateur est tolérant : lorsqu'une liste contient moins d'entrées que le layout n'en affiche, les emplacements restants sont rendus vides ; lorsqu'elle en contient davantage, les entrées supplémentaires sont ignorées. Les nombres ci-dessous décrivent donc la capacité rendue par les scripts, pas une validation bloquante.

---

## Layout 1 — Hook sens + factuel

```json
{
  "layout": 1,
  "content": {
    "title": "Pourquoi transformer maintenant",
    "manifesto": "Phrase manifeste forte (1-2 lignes max)",
    "body": "Paragraphe explicatif (2-4 lignes)",
    "stats": [
      {"value": "+38%", "label": "Engagement", "sublabel": "vs N-1"},
      {"value": "12 j", "label": "Cycle réduit", "sublabel": "moyenne projet"},
      {"value": "2,4 M€", "label": "Gains", "sublabel": "annualisés"}
    ],
    "takeaway": "Le moment est venu d'agir"
  }
}
```

- **stats** : jusqu'à 3 entrées rendues. Couleurs imposées (violet, bordeaux, orange).
- **value** : max 4-6 caractères pour respecter le rendu 44 pt.
- **manifesto** : interligne par défaut `1.15`. Les emphases utilisent par défaut Segoe UI bold en `#A25871`.
- **body** : interligne par défaut `1.3`. Les emphases utilisent par défaut Segoe UI bold.

---

## Layout 2 — Hook sens + vision (3 colonnes)

```json
{
  "layout": 2,
  "content": {
    "title": "Notre vision en 3 piliers",
    "columns": [
      {"title": "Le plan d'action doit vivre sur le terrain", "body": "..."},
      {"title": "Les indicateurs guident, pas l'inverse", "body": "..."},
      {"title": "Chaque équipier devient acteur", "body": "..."}
    ]
  }
}
```

- **columns[*].title** : sera rendu en small caps (1ère lettre majuscule + reste en petites capitales). Écrire en minuscules normales.
- **columns[*].body** : interligne par défaut `1.3`.
- **Pas de takeaway** sur ce layout.

---

## Layout 3 — Liste 6 points

```json
{
  "layout": 3,
  "content": {
    "title": "Les 6 facteurs de succès",
    "factors": [
      {"label": "Sponsor exécutif"},
      {"label": "Vision partagée"},
      {"label": "Equipes dédiées"},
      {"label": "Indicateurs simples"},
      {"label": "Communication continue"},
      {"label": "Quick wins visibles"}
    ],
    "takeaway": "Aligner les 6 facteurs avant le go"
  }
}
```

- **factors** : jusqu'à 6 entrées rendues.
- Labels rendus en small caps.

---

## Layout 4 — Triptyque

```json
{
  "layout": 4,
  "content": {
    "title": "Trois dimensions interdépendantes",
    "nodes": {
      "top": {"label": "Personnes", "sublabel": "compétences et culture"},
      "left": {"label": "Processus", "sublabel": "méthodes et standards"},
      "right": {"label": "Outils", "sublabel": "technologie et data"}
    },
    "takeaway": "Aucune dimension ne progresse seule"
  }
}
```

- 3 sommets fixes : `top`, `left`, `right`.

---

## Layout 5 — Timeline 4 étapes

```json
{
  "layout": 5,
  "content": {
    "title": "Notre feuille de route",
    "steps": [
      {"period": "T1 2026", "step_title": "Cadrage", "body": "Diagnostic + sponsoring"},
      {"period": "T2 2026", "step_title": "Pilote", "body": "2 sites + KPI baseline"},
      {"period": "T3-T4 2026", "step_title": "Déploiement", "body": "Vague 1, 6 sites"},
      {"period": "2027", "step_title": "Pérennisation", "body": "BAU + amélioration continue"}
    ]
  }
}
```

- **steps** : jusqu'à 4 entrées rendues. Couleurs de période imposées (violet, bordeaux, rose, orange).
- **period** rendu en small caps.
- **steps[*].body** : interligne par défaut `1.3`.
- **Pas de takeaway**.

---

## Layout 6 — Tableau 5×4

```json
{
  "layout": 6,
  "content": {
    "title": "Comparatif des scénarios",
    "headers": ["Scénario", "Coût", "Délai", "Risque", "Score"],
    "rows": [
      ["A — Statu quo amélioré", "0,5 M€", "6 mois", "Faible", "★★"],
      ["B — Refonte ciblée", "1,8 M€", "12 mois", "Moyen", "★★★★"],
      ["C — Transformation totale", "4,2 M€", "24 mois", "Elevé", "★★★"],
      ["D — Externalisation", "2,5 M€", "9 mois", "Moyen", "★★"]
    ],
    "takeaway": "Scénario B = meilleur rapport valeur/risque"
  }
}
```

- **headers** : jusqu'à 5 entrées rendues (cellules en-tête sur fond violet sourd).
- **rows** : jusqu'à 4 listes de 5 cellules rendues.
- Colonne 4 (avant-dernière) automatiquement colorée en `#6A5D79` bold.

---

## Layout 7 — Dashboard

```json
{
  "layout": 7,
  "content": {
    "title": "Indicateurs clés Q3",
    "kpis": [
      {"value": "94%", "sublabel": "Adhésion"},
      {"value": "12 j", "sublabel": "Cycle moyen"},
      {"value": "+38%", "sublabel": "Engagement"},
      {"value": "0,8", "sublabel": "Sigma"},
      {"value": "2,4 M€", "sublabel": "Gains"},
      {"value": "98%", "sublabel": "Conformité"}
    ],
    "section_label": "Avancement par chantier",
    "bars": [
      {"label": "Chantier 1 — Process", "value": 85},
      {"label": "Chantier 2 — Outils", "value": 62},
      {"label": "Chantier 3 — Compétences", "value": 41},
      {"label": "Chantier 4 — Pilotage", "value": 78},
      {"label": "Chantier 5 — Communication", "value": 90}
    ],
    "takeaway": "3 chantiers à accélérer en Q4"
  }
}
```

- **kpis** : jusqu'à 6 entrées rendues (ordre = couleurs bleu nuit / violet / bordeaux / rose / orange / jaune).
- **bars** : jusqu'à 5 entrées rendues. **value** est convertie en nombre et utilisée comme pourcentage ; viser `[0, 100]`, car le script ne borne pas la valeur.

---

## Layout 8 — Comparatif

```json
{
  "layout": 8,
  "content": {
    "title": "Avant / Après transformation",
    "subtitle": "5 indicateurs mesurés sur le pilote",
    "legends": ["Avant", "Après"],
    "rows": [
      {"label": "Délai de cycle (jours)", "value_1": 18, "value_2": 11, "display_1": "18 j", "display_2": "11 j"},
      {"label": "Taux de défauts (ppm)", "value_1": 1200, "value_2": 380},
      {"label": "Engagement équipe (%)", "value_1": 56, "value_2": 78},
      {"label": "Coût unitaire (€)", "value_1": 240, "value_2": 195},
      {"label": "Satisfaction client", "value_1": 7.2, "value_2": 8.6}
    ],
    "takeaway": "Gains significatifs sur les 5 dimensions"
  }
}
```

- **rows** : jusqu'à 5 entrées rendues.
- **value_1** et **value_2** : nombres pour proportionner les barres.
- **display_1**, **display_2** (optionnels) : texte affiché à droite des barres (sinon valeur brute).

---

## Layout 9 — Risques & Opportunités

```json
{
  "layout": 9,
  "content": {
    "title": "Risques & Opportunités",
    "risks": [
      {
        "title": "Résistance management intermédiaire",
        "level": "high_risk",
        "body": "Crainte d'évincement, charge perçue.",
        "action": "Programme dédié N-1 (formation + ambassadeurs)."
      },
      {"title": "Dépendance fournisseur SI", "level": "medium_risk", "body": "...", "action": "..."},
      {"title": "Charge équipes en déploiement", "level": "high_risk", "body": "...", "action": "..."}
    ],
    "opportunities": [
      {
        "title": "Vague d'engagement post-pilote",
        "level": "high_opp",
        "body": "Témoignages spontanés.",
        "action": "Capitaliser via communication interne."
      },
      {"title": "Synergie autres BU", "level": "medium_opp", "body": "...", "action": "..."},
      {"title": "Ouverture nouveau marché", "level": "high_opp", "body": "...", "action": "..."}
    ]
  }
}
```

- **level** ∈ `high_risk` (rouge), `medium_risk` (orange), `high_opp` (vert), `medium_opp` (olive).
- Tags d'action figés : "Parade" pour risques, "Levier" pour opportunités (small caps vert pâle).
- **risks** et **opportunities** : jusqu'à 3 entrées rendues chacun.
- **Pas de takeaway**.

---

## Layout 10 — Plan d'action 3 phases

```json
{
  "layout": 10,
  "content": {
    "title": "Plan d'action 18 mois",
    "date": "Mai 2026",
    "phases": [
      {
        "phase_title": "Cadrage",
        "phase_subtitle": "T1-T2 2026",
        "items": [
          {"title": "Sponsor + gouvernance", "body": "COPIL hebdo, sponsor N-1"},
          {"title": "Diagnostic terrain", "body": "30 entretiens, 6 sites"},
          {"title": "Roadmap détaillée", "body": "Chantiers + KPI baseline"}
        ]
      },
      {
        "phase_title": "Pilote",
        "phase_subtitle": "T3 2026 - T1 2027",
        "items": [
          {"title": "2 sites pilotes", "body": "France + Espagne"},
          {"title": "Méthode validée", "body": "Itération hebdo, REX mensuel"},
          {"title": "Premiers gains", "body": "+15% engagement, -20% cycle"}
        ]
      },
      {
        "phase_title": "Déploiement",
        "phase_subtitle": "T2-T4 2027",
        "items": [
          {"title": "Vague 1 (6 sites)", "body": "Avec ambassadeurs internes"},
          {"title": "Vague 2 (12 sites)", "body": "Y compris BU adjacentes"},
          {"title": "Pérennisation", "body": "BAU + amélioration continue"}
        ]
      }
    ],
    "takeaway": "Une feuille de route en 3 temps, 3 livrables clairs"
  }
}
```

- **phases** : jusqu'à 3 entrées rendues. Couleurs des bandeaux imposées (violet, bordeaux, orange).
- **items** par phase : jusqu'à 3 entrées rendues.
- **date** : optionnelle (apparaît en haut à droite).

---

## Layout 11 — Arc narratif / CTA

```json
{
  "layout": 11,
  "content": {
    "title": "Synthèse et appel à l'action",
    "blocks": [
      {
        "block_title": "Ce que nous avons appris",
        "body": "..."
      },
      {
        "block_title": "Ce que nous proposons",
        "body": "..."
      },
      {
        "block_title": "Ce que nous attendons de vous",
        "body": "..."
      }
    ],
    "cta": "Etes-vous prêts à valider la phase 1 ?"
  }
}
```

- **blocks** : jusqu'à 3 entrées rendues (couleurs filigranes : violet pâle / rose pâle / pêche pâle).
- Filigranes "01"/"02"/"03" générés automatiquement (alpha 40%).
- **cta** : phrase d'engagement, registre direct.
- **blocks[*].body** : interligne par défaut `1.3`. Les emphases utilisent par défaut Segoe UI bold.

---

## Layout 12 — Process vertical 6 étapes

```json
{
  "layout": 12,
  "content": {
    "title": "Process de déploiement",
    "steps": [
      {"label": "Identifier les clients", "sublabel": "Cartographie des parties prenantes"},
      {"label": "Évaluer les attentes", "sublabel": "Échelle de priorisation commune"},
      {"label": "Construire le questionnaire", "sublabel": "Questions fonctionnelles / dysfonctionnelles"},
      {"label": "Tester le dispositif", "sublabel": "Échantillon restreint"},
      {"label": "Diffuser largement", "sublabel": "Canal, suivi, données"},
      {"label": "Analyser les résultats", "sublabel": "Priorités d'action"}
    ]
  }
}
```

- **steps** : jusqu'à 6 entrées rendues.
- **label** : titre court en 12 pt bold.
- **sublabel** : détail opérationnel en 10 pt.
- Pas de takeaway : ce layout est une séquence process compacte.

---

## Layout 13 — Opposition qualitative

```json
{
  "layout": 13,
  "content": {
    "title": "Bonnes pratiques terrain",
    "left_title": "À faire",
    "right_title": "À éviter",
    "left_items": ["Question précise", "Bénéfice utilisateur"],
    "right_items": ["Question trop générale", "Échelle inadaptée"]
  }
}
```

- **left_items** et **right_items** : jusqu'à 5 entrées rendues par colonne.
- La colonne gauche utilise le vert `#0F6E56`; la droite utilise le brun rouge `#993C1D`.
- Chaque item est placé dans une carte blanche avec contour fin `#E0DFDB`.
- Pas de takeaway : le contraste visuel suffit à la décision.

---

## Layout 14 — Comparatif qualitatif

```json
{
  "layout": 14,
  "content": {
    "title": "Comparatif qualitatif",
    "left_title": "DMAIC",
    "right_title": "DMADV",
    "left_items": ["Améliorer un processus existant"],
    "right_items": ["Concevoir une solution nouvelle"],
    "takeaway": "Choisir l'approche selon la maturité du problème"
  }
}
```

- **left_items** et **right_items** : jusqu'à 5 entrées rendues.
- Titres de colonnes en small caps, 22 pt, violet `#6A5D79` à gauche et orange `#FDA85B` à droite.
- Le grand cadre décoratif est un asset PNG figé, `assets/backgrounds/Comp_quali_bg.png`, exporté depuis la forme nommée `Comp_quali_bg` du template. Le générateur ne recrée pas cette forme ; il insère l'asset puis modifie uniquement les placeholders texte nommés.
- **takeaway** : bandeau bas standard, positionné à `y=16.87 cm`.

---

## Layout 15 — Matrice d'impact par population

```json
{
  "layout": 15,
  "content": {
    "title": "Impact par population",
    "headers": ["Outils", "Métier", "Organisation", "Culture", "Leviers"],
    "rows": [
      {
        "label": "Conseillers en agence",
        "sublabel": "~ 1 200 pers.",
        "impacts": [4, 3, 2, 4],
        "levers": "Formation | Accompagnement terrain"
      }
    ],
    "legend_title": "Intensité",
    "legend": ["Faible", "Modéré", "Fort", "Très fort"],
    "footnote": "Leviers = axes d'accompagnement prioritaires par population"
  }
}
```

- **rows** : jusqu'à 6 populations rendues.
- **impacts** : 4 niveaux numériques pour les colonnes Outils / Métier / Organisation / Culture. `1` = faible `#CEC9D5`, `2` = modéré `#9D93AB`, `3` = fort `#6A5D79`, `4` = très fort `#393242`. `0` ou valeur vide laisse la cellule blanche.
- **levers** : texte libre affiché dans la dernière colonne, sans emphase inline sur ce layout.
- Les cellules `S15_TABLE_R*_C*` sont rendues avec un léger arrondi.
- Pas de takeaway : la légende occupe le bas de slide.

---

## Conventions générales

- Tous les textes peuvent être des **chaînes UTF-8** simples. Les caractères français (é, à, ç, œ, etc.) sont supportés.
- Tout champ texte peut aussi recevoir une **spécification enrichie** pour piloter le placeholder nommé correspondant :

```json
{
  "text": "Le statu quo coûte 480 k€ par mois, mais le pilote réduit le cycle.",
  "line_spacing": 1.15,
  "emphasis": [
    {
      "text": "statu quo",
      "font": "Segoe UI Black",
      "color": "#A25871",
      "bold": true
    },
    {
      "text": "réduit le cycle",
      "font": "Segoe UI",
      "color": "#6A5D79",
      "bold": true
    }
  ]
}
```

- **line_spacing** : accepte un ratio (`1.15`), un pourcentage (`"115%"`) ou une valeur en points (`"16pt"`).
- **emphasis** : applique une police, une couleur et/ou un style aux occurrences de `text` dans le paragraphe. Par défaut, toutes les occurrences sont concernées ; ajouter `"first_only": true` pour ne cibler que la première, ou `"case_sensitive": true` pour une recherche sensible à la casse.
- **Apostrophes courbes** (' au lieu de ') : à privilégier (le générateur les conserve telles quelles).
- **Sauts de ligne** dans un body : utiliser `\n` (encodé `\\n` en JSON).
- **Pas de balises HTML / Markdown** dans les valeurs : le générateur prend les chaînes brutes.
- Le script accepte aussi `"emphases"` comme alias de `"emphasis"` dans une spécification enrichie.
