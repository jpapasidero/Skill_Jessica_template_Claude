---
name: palette-jessica
description: Generate Safran-styled PowerPoint presentations using the "Palette Jessica" 16:9 template at pixel-perfect fidelity. Trigger this skill ANY time the user asks for a slide deck, presentation, pitch deck, or .pptx file in the Safran "Palette Jessica" style, mentions the bordeaux/violet/orange palette (#A25871/#6A5D79/#FDA85B), refers to the 11 named layouts (Hook factuel, Hook vision, Liste 6 points, Triptyque, Timeline, Tableau, Dashboard, Comparatif, Risques & Opportunités, Plan d'action 3 phases, Arc narratif/CTA), or wants to convert a topic outline into a complete branded presentation. Also use when the user uploads a content brief and asks for a "presentation Safran", "deck conduite du changement", "support comité", "présentation projet de transformation", or similar — even if they don't explicitly name the template.
---

# Skill: Palette Jessica — Générateur de présentations Safran

Ce skill produit des présentations PowerPoint conformes au template **Palette Jessica** (Safran), en s'appuyant sur 11 layouts métier prédéfinis et la palette signature **bordeaux #A25871 / violet #6A5D79 / orange #FDA85B**.

## Quand utiliser ce skill

Déclenche-le dès que l'utilisateur :
- demande une présentation, deck, slides, pitch, support — au format `.pptx`
- mentionne le template "Palette Jessica", Safran, ou la palette bordeaux/violet/orange
- a besoin d'un livrable visuel pour un projet de transformation, change management, comité, retour d'expérience
- fournit un brief texte qu'il faut transformer en deck

Ne pas l'utiliser pour : un seul slide isolé qu'on peut juste décrire en chat, ou une demande qui n'est pas un livrable PPTX.

## Workflow

1. **Comprendre l'intention** : combien de slides, quel objectif (informer / convaincre / décider), quelle audience (DISC : Dominant, Influent, Stable, Consciencieux). Si l'utilisateur n'a pas précisé, propose une structure narrative (storyline) avant de générer.

2. **Choisir les layouts** parmi les 11 disponibles (voir `references/layouts_catalog.md`). Adapte le choix au message :
   - Layout 1 (Hook factuel) ou 11 (Arc narratif) en ouverture
   - Layout 5 (Timeline) ou 10 (Plan 3 phases) pour le quand/comment
   - Layout 9 (Risques & Opportunités) avant la décision
   - Layout 11 (CTA) pour la clôture

3. **Construire le `content.json`** au format décrit dans `references/content_schema.md`.

4. **Générer la présentation** :
   ```bash
   cd <skill-path>
   python scripts/generate_pptx.py \
       --content /path/to/content.json \
       --output /path/to/output.pptx \
       [--logo /path/to/safran_logo.png]
   ```

5. **Présenter le fichier** à l'utilisateur via `present_files`.

## Structure du contenu (content.json)

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

Le détail exact des champs attendus pour chaque layout est dans `references/content_schema.md` — **lis ce fichier avant de construire le JSON**, particulièrement pour les layouts 6 (tableau), 7 (dashboard), 9 (risques/opps) et 10 (phases) qui ont des structures imbriquées.

## Bonnes pratiques de contenu

- **Titres courts** (5-7 mots max) pour ne pas casser la mise en page
- **Manifesto / titres de section en small caps** : écris en minuscules normales — l'effet `cap="small"` est appliqué automatiquement par le rendu OOXML
- **3 KPI verticaux (slide 1)** : 1 chiffre signature par couleur (violet, bordeaux, orange) — ne pas dépasser 4 caractères pour la valeur
- **Take-away** : 1 phrase d'action, max 12 mots, formulation impérative ou affirmative forte
- **Layout 11 (CTA)** : la phrase CTA doit poser une question ou appeler à un engagement explicite (registre Influent en DISC)

## Contraintes techniques

- **Format slide** : 16:9 widescreen (33.87 × 19.05 cm) — fixé par le générateur
- **Polices** : Segoe UI Black (titres), Segoe UI (corps), Segoe UI Light (secondaire). Si la machine ne les a pas, PowerPoint substituera automatiquement (Arial Black / Arial / Arial Light)
- **Logo Safran** : fournir `--logo path/to/logo.png` pour qu'il apparaisse en bas à droite (sinon, espace réservé blanc)
- **Le fichier produit ne contient pas de slide master Safran personnalisé** — les éléments « chrome » (titre, barre signature, footer confidentiel, n° page) sont reproduits sur chaque slide via shapes nommées. Ce choix garantit la fidélité visuelle sans dépendre d'un fichier source `.pptx` propriétaire.

## Référence rapide des 11 layouts

| # | Nom | Usage type | Take-away |
|---|---|---|---|
| 1 | Hook sens + factuel | Ouverture forte avec 3 KPI signature | Oui |
| 2 | Hook sens + vision | 3 piliers / 3 partis-pris | Non |
| 3 | Liste 6 points | Facteurs, leviers, étapes | Oui |
| 4 | Triptyque | 3 dimensions liées (people-process-technology...) | Oui |
| 5 | Timeline | 4 étapes / phases temporelles | Non |
| 6 | Tableau | Comparatif structuré 5 colonnes × 4 lignes | Oui |
| 7 | Dashboard | 6 KPI + 5 indicateurs barres | Oui |
| 8 | Comparatif | 5 lignes × 2 valeurs comparées | Oui |
| 9 | Risques & Opportunités | Grille 2×3 (3 risques / 3 opps) | Non |
| 10 | Plan d'action 3 phases | Roadmap avec 3 phases × 3 items | Oui |
| 11 | Arc narratif / CTA | Conclusion 3 blocs + appel à l'action | Oui (CTA) |

## Vérification post-génération

Après génération, vérifie :
- [ ] Le bandeau Take-away (gradient vertical bordeaux) apparaît sur les slides 1, 3, 4, 6, 7, 8, 10, 11
- [ ] Le bandeau **n'apparaît pas** sur les slides 2, 5, 9
- [ ] Les couleurs signature sont présentes : `#A25871`, `#6A5D79`, `#FDA85B`
- [ ] Le titre est en `#484C6A` Segoe UI Black 29.32pt
- [ ] La barre de signature (rectangle bleu nuit + trait fin) apparaît sous chaque titre
- [ ] Le filigrane "01"/"02"/"03" (slide 11) est translucide à 40%
- [ ] Les small caps fonctionnent sur slides 2 (titres colonnes), 3 (factor labels), 5 (periods), 9 (level + action tags)

## Extension / personnalisation

- Pour ajouter un layout : créer un `build_slide_N` dans `scripts/builders.py` et l'enregistrer dans le dict `BUILDERS`
- Pour modifier la palette : éditer les hex codes en haut des builders concernés (recommandation : extraire dans une constante en début de `builders.py` pour future v2)
- La spec complète du template original est dans `references/spec.json` — pour audit / régénération XML directe

## Limites connues

- python-pptx ne reproduit pas le `cap="small"` à 100 % : injecté en XML mais certains visualiseurs (LibreOffice headless, aperçus thumbnails) peuvent le rendre en majuscules pleines
- Le logo Safran (`image1.png`) est confidentiel — le skill ne l'embarque pas. Fournir le fichier via `--logo`
- Les images icônes (image3-5 du template original) ne sont pas embarquées — les builders dessinent des cercles colorés à la place
- Slide 4 (triptyque) : le template original utilise Poppins/Lato — ce skill substitue par Segoe UI pour cohérence
