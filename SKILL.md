---
name: gen-pptx-jessica
description: Génère des présentations PowerPoint au style Safran en utilisant le modèle 16:9 « Palette Jessica ». À utiliser pour les diaporamas, présentations ou fichiers .pptx au style Safran (#A25871/#6A5D79/#FDA85B). Prend en charge 14 mises en page standard (Hook, Liste, Timeline, Dashboard, Plan, Process, etc.) ainsi que les briefs de contenu pour les projets de transformation et de conduite du changement. À utiliser également pour les demandes de type « présentation Safran », « support comité » ou « deck conduite du changement ». REMARQUE : La mise en page 15 (Impact par population) n’est JAMAIS incluse par défaut. Elle est générée uniquement sur demande explicite d’une « analyse d’impact » accompagnée d’un fichier PPTX contenant les zones nommées TITLE, ZONE_OMOC et RESSORTS_CHANGE.
---

## Skill: gen-pptx-jessica — Générateur de présentations Safran

Ce skill produit des présentations PowerPoint conformes au template **Palette Jessica** (Safran), en s'appuyant sur 15 layouts métier prédéfinis et la palette signature **bordeaux #A25871 / violet #6A5D79 / orange #FDA85B**.

# Quand utiliser ce skill

Déclenche-le dès que l'utilisateur :
- demande une présentation, deck, slides, pitch, support — au format `.pptx`
- mentionne le template "Palette Jessica", Safran, ou la palette bordeaux/violet/orange
- a besoin d'un livrable visuel pour un projet de transformation, change management, comité, retour d'expérience
- fournit un brief texte qu'il faut transformer en deck

Ne pas l'utiliser pour : un seul slide isolé qu'on peut juste décrire en chat, ou une demande qui n'est pas un livrable PPTX.

# Référence rapide des 15 layouts

| # | Nom | Usage type | Take-away |
|---|---|---|---|
| 1 | Hook sens + factuel | Ouverture forte avec 3 KPI signature | Oui |
| 2 | Hook sens + vision | 3 piliers / 3 partis-pris | Non |
| 3 | Liste 6 points | Facteurs, leviers, étapes | Oui |
| 4 | Triptyque | 3 dimensions liées (people-process-technology...) | Oui |
| 5 | Timeline | 4 étapes / phases temporelles | Non |
| 6 | Tableau | Comparatif structuré 5 colonnes × 4 lignes | Oui |
| 7 | Dashboard | 6 KPI + 5 indicateurs barres | Oui |
| 8 | Comparatif quantitatif | 5 lignes × 2 valeurs comparées | Oui |
| 9 | Risques & Opportunités | Grille 2×3 (3 risques / 3 opps) | Non |
| 10 | Plan d'action 3 phases | Roadmap avec 3 phases × 3 items | Oui |
| 11 | Arc narratif / CTA | Conclusion 3 blocs + appel à l'action | Oui (CTA) |
| 12 | Process vertical | 6 étapes avec label + sublabel | Non |
| 13 | Opposition qualitative | À faire / À éviter en 2 colonnes | Non |
| 14 | Comparatif qualitatif | Deux approches en miroir | Oui |
| 15 | Impact par population | Matrice d'intensité + leviers | Non |

# Structure du contenu (content.json)

```json
{
  "slides": [
    {
      "layout": 1,
      "content": {
        "title": "Pourquoi transformer maintenant",
        "manifesto": "Le statu quo nous coûte plus cher que le changement.",
        "body": "...",
        "stats": [
          {"value": "+38%", "label": "Engagement", "sublabel": "vs N-1"},
          {"value": "12 j", "label": "Cycle réduit", "sublabel": "moyenne projet"},
          {"value": "2,4 M€", "label": "Gains", "sublabel": "annualisés"}
        ],
        "takeaway": "Le moment est venu d'agir."
      }
    },
    { "layout": 5, "content": { "...": "..." } }
  ]
}
```

# Workflow de génération

1. **Comprendre l'intention** : combien de slides, quel objectif (informer / convaincre / décider), quelle audience (DISC : Dominant, Influent, Stable, Consciencieux). En l'absence de précisions, propose une structure narrative (storyline) avant de générer.

2. **Choisir les layouts** parmi les **14 layouts standard** (voir `references/layouts_catalog.md`). Il s'agit d'adapter le choix au message :
   - Layout 1 (Hook factuel) ou 2 (Hook Vision) en ouverture
   - Layout 5 (Timeline) ou 10 (Plan 3 phases) pour le quand/comment
   - Layout 9 (Risques & Opportunités) avant la décision
   - Layout 11 (CTA) pour la clôture
   - Layout 12 pour un protocole/process en 6 étapes
   - Layout 13 pour opposer bonnes pratiques et erreurs à éviter
   - Layout 14 pour comparer qualitativement deux méthodes

   > [!IMPORTANT]
   > **Le Layout 15 (Impact par population) n'est JAMAIS inclus par défaut.**
   > Il est réservé à un workflow spécifique d'analyse d'impact — voir la section dédiée ci-dessous.

3. **Construire le `content.json`** au format décrit dans `references/content_schema.md`. 
   > [!IMPORTANT]
   > **CONSIGNE CRITIQUE : EMPHASES OBLIGATOIRES**
   # > Pour les **Layouts 1, 11 et 14**, il est obligatoire d'utiliser la structure enrichie `{ "text": "...", "emphasis": [...] }` pour mettre en gras les mots-clés stratégiques. Ne jamais fournir du texte brut pour ces champs.

4. **Générer la présentation** :
   ```bash
   cd <skill-path>
   python scripts/generate_pptx.py \
       --content /path/to/content.json \
       --output /path/to/output.pptx \
       [--logo /path/to/safran_logo.png]
   ```
 
5. **Remise du fichier généré** : il s'agit de remettre le fichier à l'utilisateur en indiquant clairement le chemin du `.pptx` produit.

Le détail exact des champs attendus pour chaque layout est dans `references/content_schema.md` — **il est nécessaire de lire ce fichier avant de construire le JSON**, particulièrement pour les layouts 6 (tableau), 7 (dashboard), 9 (risques/opps) et 10 (phases) qui ont des structures imbriquées.

# Contraintes techniques

- **Format slide** : 16:9 widescreen (33.87 × 19.05 cm) — fixé par le générateur
- **Polices** : Segoe UI Black (titres), Segoe UI (corps), Segoe UI Light (secondaire). Si la machine ne les a pas, PowerPoint substituera automatiquement (Arial Black / Arial / Arial Light)
- **Logo Safran** : le générateur cherche automatiquement un PNG/JPG dans `assets/logo`, `assets/logos`, `asset/logo` ou `asset/logos`. `--logo path/to/logo.png` reste possible pour forcer un fichier précis.
- **Le fichier produit ne contient pas de slide master Safran personnalisé** — les éléments « chrome » (titre, barre signature, footer confidentiel, n° page) sont reproduits sur chaque slide via shapes nommées. Ce choix garantit la fidélité visuelle sans dépendre d'un fichier source `.pptx` propriétaire.
- **Layout 3** : le décor comparatif est inséré depuis `assets/backgrounds/triangle.png`. Ne pas recréer cette forme en shapes ; seuls les placeholders texte nommés sont modifiés.
- **Layout 14** : le décor comparatif est inséré depuis `assets/backgrounds/Comp_quali_bg.png`, exporté depuis la forme `Comp_quali_bg` du template. Ne pas recréer cette forme en shapes ; seuls les placeholders texte nommés sont modifiés.
- **Layout 15** : les cellules `S15_TABLE_R*_C*` ont un léger arrondi et les emphases inline sont ignorées sur ce slide.
- **Tolérance JSON** : les listes trop courtes sont complétées visuellement par des emplacements vides ; les entrées au-delà du nombre rendu par le layout sont ignorées. Le générateur ne valide pas strictement le schéma avant rendu.
- **Texte enrichi** : tout champ texte peut être une chaîne ou un objet `{ "text": "...", "line_spacing": ..., "emphasis": [...] }`. Les emphases sont appliquées aux occurrences textuelles non chevauchantes, insensibles à la casse par défaut.

# Vérification post-génération

Après génération, vérifier :
- [ ] Le bandeau Take-away (gradient vertical bordeaux) apparaît sur les slides 1, 3, 4, 6, 7, 8, 10, 11, 14
- [ ] Le bandeau **n'apparaît pas** sur les slides 2, 5, 9, 12, 13, 15
- [ ] Les couleurs signature sont présentes : `#A25871`, `#6A5D79`, `#FDA85B`
- [ ] Le titre est en `#484C6A` Segoe UI Black 29.32pt
- [ ] La barre de signature (rectangle bleu nuit + trait fin) apparaît sous chaque titre
- [ ] Le filigrane "01"/"02"/"03" (slide 11) est translucide à 40%
- [ ] Les small caps fonctionnent sur slides 2 (titres colonnes), 3 (factor labels), 5 (periods), 9 (level + action tags), 14 (titres comparatifs)
- [ ] **VÉRIFICATION EMPHASES** : Les mots-clés sont-ils bien en gras/couleur sur les Layouts 1, 11 et 14 ? (Vérifier la présence du champ `emphasis` dans le JSON généré).

# Extension / personnalisation

- Pour ajouter un layout :  créer un `build_slide_N` dans `scripts/builders.py` et de l'enregistrer dans le dict `BUILDERS`
- Pour modifier la palette : éditer les hex codes en haut des builders concernés (recommandation : extraire dans une constante en début de `builders.py` pour future v2)
- La spec complète du template original est dans `references/spec.json` — pour audit / régénération XML directe

# Cas particulier de l'analyse d'impact - layout 15

> [!CAUTION]
> **Le Layout 15 ne doit JAMAIS être inclus dans une présentation standard.**
> Il n'est activé que lorsque les **deux conditions suivantes sont simultanément réunies** :
> 1. L'utilisateur indique **explicitement** qu'il souhaite formaliser une **analyse d'impact** (ex. : « génère le slide d'impact par population », « fais le Layout 15 à partir de mon fichier d'analyse », « je veux formaliser mon analyse d'impact »)
> 2. L'utilisateur **joint un fichier source** (`.pptx` ou `.pdf`) contenant les données d'analyse d'impact par population
>
> Si l'une de ces conditions manque, ne pas utiliser le Layout 15. Si le fichier PPTX joint ne contient pas les zones sus-nommées, en informer l'utilisateur.

# Workflow de génération du layout 15 - analyse d'impact

1. **Identifier le format du fichier joint, puis lancer le parseur** :

   - Si le fichier est un **PDF** (extension `.pdf`) :
```bash
     python scripts/impact_parser.py <fichier_impact.pdf> --raw
```
     Le parseur appelle `_parse_impact_pdf()` qui extrait titre, bullets OMOC par couleur/position géométrique, et la table RESSORTS_CHANGE.
     Il utilise automatiquement **PyMuPDF** si disponible, sinon **pdfplumber** (fallback, disponible dans Claude.ai).
     > Si aucune des deux librairies n'est disponible, il est nécessaire d'extraire les données manuellement depuis le contenu du PDF déjà visible dans le contexte, en appliquant les mêmes règles de mapping.

   - Si le fichier est un **PPTX** (extension `.pptx`) :
```bash
     python scripts/impact_parser.py <fichier_impact.pptx> --raw
```
     Le parseur appelle `parse_impact_pptx()` qui extrait titre, bullets OMOC par couleur/position géométrique, et la table RESSORTS_CHANGE.

   Dans les deux cas, la sortie `--raw` retourne un JSON avec, pour chaque slide/page :
   - `population` : nom de la population impactée (ou `"Population à nommer"` si absent du titre)
   - `effectif` : effectif (ou `"TBD"` si absent du titre)
   - `omoc` : cotations d'impact `{Tool, Business, Organization, Culture}` de 1 à 4 (ou `"0"` si illisible)
   - `raw_levers` : liste des actions de changement brutes (ressort, type, détail)

2. **Synthèse sémantique**
	Pour chaque population, lire **exclusivement** le champ `détail` de chaque entrée `raw_levers` et rédiger un résumé synthétique (max 135 caractères).
	- Style télégraphique professionnel (pas de verbes conjugués).
	- Extraire les actions concrètes nommées dans `détail` : noms d'outils, livrables, acteurs, moments-clés.
	- **INTERDIT** : utiliser le champ `type` (Communication, Support, Mobilisation...) comme contenu ou comme préfixe de la synthèse. Le `type` est une métadonnée de catégorie, pas un levier actionnable.
	- **INTERDIT** : utiliser le champ `ressort` (Sens, Preuve...) comme contenu de la synthèse.
	- Si plusieurs `détail` concernent la même action, fusionner en une formulation unique.
	- Exemple attendu pour une population outillage : *"Planification 3 mois ; pairs VP1 en témoin RGM ; templates oSmoz outillages ; retex coord. IB + mesure appropriation"*

3. **Construction et génération**
	- Il s'agit de construire le `content.json` pour le Layout 15 en injectant les résumés rédigés dans le champ `levers` de chaque population.
	- Il s'agit ensuite de générer la présentation :
	```bash
	python scripts/generate_pptx.py \
		--content /path/to/content.json \
		--output /path/to/output.pptx \
	```
	
# Contraintes spécifiques au layout 15

> [!WARNING]
> **INTERDICTION STRICTE d'inventer ou d'extrapoler des données manquantes à partir de la synthèse d'autres populations, même si le contenu te semble bizarre**
> Toutes les informations du Layout 15 doivent provenir **exclusivement** du fichier fourni. En cas de donnée manquante :
> - **Population introuvable dans TITLE** → créer une ligne pour cette slide et indiquer `Population à nommer` dans le LABEL
> - **Effectif absent du TITLE** → inscrire `TBD` dans le SUBLABEL (ne pas deviner l'effectif)
> - **Cotation OMOC manquante** (bullet absent ou non identifiable) → laisser la valeur à `0` (ne pas interpoler)
> - **RESSORTS_CHANGE vide, illisible ou ressemblant à un placeholder en cours de rédaction** → laisser la cellule vide, le signaler à l'utilisateur (ne pas rédiger un résumé fictif)
> - **Analyse d'impact (depuis PPTX ou PDF)** → Il est strictement **interdit de regrouper des populations**. Il faut générer 1 ligne par planche source (slide), même si les planches concernent des populations identiques. Ce sont les mêmes contraintes de restitution quelle que soit la source.
>
> En cas de doute sur l'interprétation d'une donnée, signaler l'ambiguïté à l'utilisateur **avant** de générer, plutôt que de faire une hypothèse silencieuse.

-  **Maximum 6 populations par slide Layout 15.** Si le fichier d'impact contient plus de 6 populations, créer des slides Layout 15 supplémentaires.
- **Ordre chronologique obligatoire** : les populations doivent apparaître dans le Layout 15 **dans l'ordre des slides du fichier source** (champ `slide_index` dans la sortie `--raw`). Ne pas réordonner, regrouper ni trier autrement.

# Bonnes pratiques de contenu

- **Titres courts** (5-7 mots max) pour ne pas casser la mise en page
- **Manifesto / titres de section en small caps** : écrire en minuscules normales — l'effet `cap="small"` est appliqué automatiquement par le rendu OOXML
- **3 KPI verticaux (slide 1)** : 1 chiffre signature par couleur (violet, bordeaux, orange). Le script accepte du texte plus long, mais vise 4-6 caractères pour préserver le rendu en 44 pt.
- **Take-away** : 1 phrase d'action, max 12 mots, formulation impérative ou affirmative forte
- **Layout 11 (CTA)** : la phrase CTA doit poser une question ou appeler à un engagement explicite (registre Influent en DISC)
- **Mots en emphase (Layouts 1, 11, 14) — RÈGLE D'OR** :
  L'IA **DOIT** identifier proactivement les mots-clés et utiliser **OBLIGATOIREMENT** la structure enrichie :
  `{ "text": "...", "emphasis": ["mot1", "mot2"] }`
  Ceci s'applique aux champs suivants :
  - **Layout 1** : `manifesto` et `body`
  - **Layout 11** : `body` (dans `blocks`)
  - **Layout 14** : `left_items` et `right_items`
  *L'emphase est strictement interdite sur tous les autres éléments.*


# Limites connues

- python-pptx ne reproduit pas le `cap="small"` à 100 % : injecté en XML mais certains visualiseurs (LibreOffice headless, aperçus thumbnails) peuvent le rendre en majuscules pleines
- Le logo Safran est chargé depuis les assets locaux du skill quand il est présent. Garder `--logo` seulement pour surcharger ce choix.

