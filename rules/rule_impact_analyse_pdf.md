# Règles métier : Génération d'une analyse d'impact depuis un fichier PDF

Quand l'utilisateur demande de formaliser une analyse d'impact à partir d'un fichier `.pdf` (comme `Exemple_analyse_impact.pdf`), suivez obligatoirement ce workflow :

## 1. Extraction des données brutes
Exécutez le script d'extraction :
```bash
cd <skill-path>
python scripts/impact_parser.py <fichier_impact.pdf> --raw
```
Le parseur (via PyMuPDF si disponible, sinon pdfplumber) va automatiquement lire et retourner un JSON brut avec :
- Le titre en haut de page pour la `population` et l'`effectif`.
- La zone graphique (côté OMOC) pour l'intensité des 4 cotations (Outils, Métier, Organisation, Culture).
- Le tableau (côté RESSORTS) pour les actions de changement (`raw_levers`).

## 2. Synthèse sémantique
Pour chaque population, lisez les `raw_levers` et rédigez un résumé synthétique (max 135 caractères).
- Style télégraphique professionnel (pas de verbes conjugués).
- Listez les leviers concrets décidés (ex. formation terrain, templates oSmoz, mobilisation de relais).
- Être spécifique au contenu des actions (ne pas se limiter à lister les types comme Communication, Support...).

## 3. Construction et génération
- Construisez le `content.json` pour le Layout 15 en injectant vos résumés rédigés dans le champ `levers` de chaque population.
- Générez la présentation :
```bash
python scripts/generate_pptx.py \
    --content /path/to/content.json \
    --output /path/to/output.pptx \
    --impact <fichier_impact.pdf>
```

> **Note technique** : Quand `--impact` est utilisé, le générateur remplace automatiquement les slides Layout 15 du content.json par celles extraites du fichier d'impact.

## Règles de mapping automatiques (gérées par le script)
- Titre PDF → `S15_TABLE_LABEL_Ri` et `S15_TABLE_SUBLABEL_Ri`
- Radar OMOC PDF → `S15_TABLE_Ri_C2..C5`
- Tableau Ressorts PDF → `S15_TABLE_Ri_C6` (Votre résumé)
