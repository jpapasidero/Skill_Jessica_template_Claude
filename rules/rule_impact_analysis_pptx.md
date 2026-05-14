# Règles métier : Génération d'une analyse d'impact depuis un fichier PPTX

Quand l'utilisateur demande de formaliser une analyse d'impact à partir d'un fichier `.pptx` (contenant les zones nommées TITLE, ZONE_OMOC et RESSORTS_CHANGE), suivez obligatoirement ce workflow :

## 1. Extraction des données brutes
Exécutez le script d'extraction :
```bash
cd <skill-path>
python scripts/impact_parser.py <fichier_impact.pptx> --raw
```
Cela retourne un JSON avec, pour chaque slide source :
- `population` : nom de la population
- `effectif` : effectif (ou "TBD")
- `omoc` : cotations d'impact `{Tool, Business, Organization, Culture}` de 0 à 4
- `raw_levers` : actions de changement brutes

## 2. **Synthèse sémantique**
	Pour chaque population, lis **exclusivement** le champ `détail` de chaque entrée `raw_levers` et rédige un résumé synthétique (max 135 caractères).
	- Style télégraphique professionnel (pas de verbes conjugués).
	- Extraire les actions concrètes nommées dans `détail` : noms d'outils, livrables, acteurs, moments-clés.
	- **INTERDIT** : utiliser le champ `type` (Communication, Support, Mobilisation...) comme contenu ou comme préfixe de la synthèse. Le `type` est une métadonnée de catégorie, pas un levier actionnable.
	- **INTERDIT** : utiliser le champ `ressort` (Sens, Preuve...) comme contenu de la synthèse.
	- Si plusieurs `détail` concernent la même action, fusionner en une formulation unique.
	- Exemple attendu pour une population outillage : *"Planification 3 mois ; pairs VP1 en témoin RGM ; templates oSmoz outillages ; retex coord. IB + mesure appropriation"*

## 3. Construction et génération
- Construisez le `content.json` pour le Layout 15 en injectant vos résumés rédigés dans le champ `levers` de chaque population.
- Générez la présentation :
```bash
python scripts/generate_pptx.py \
    --content /path/to/content.json \
    --output /path/to/output.pptx \
    --impact <fichier_impact.pptx>
```

> **Note technique** : Quand `--impact` est utilisé, le générateur remplace automatiquement les slides Layout 15 du content.json par celles extraites du fichier d'impact.

## Règles de mapping automatiques (gérées par le script)
- `TITLE` (gauche) → `S15_TABLE_LABEL_Ri`
- `TITLE` (droite) → `S15_TABLE_SUBLABEL_Ri`
- `ZONE_OMOC` (4 bullets) → `S15_TABLE_Ri_C2..C5`
- `RESSORTS_CHANGE` → `S15_TABLE_Ri_C6` (Votre résumé)
