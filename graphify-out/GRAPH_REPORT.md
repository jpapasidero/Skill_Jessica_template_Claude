# Graph Report - Skill_Jessica_template_Claude  (2026-05-13)

## Corpus Check
- 11 files · ~43,021 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 120 nodes · 349 edges · 13 communities detected
- Extraction: 76% EXTRACTED · 24% INFERRED · 0% AMBIGUOUS · INFERRED: 85 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]

## God Nodes (most connected - your core abstractions)
1. `add_textbox()` - 29 edges
2. `add_master_chrome()` - 24 edges
3. `add_rect()` - 22 edges
4. `set_white_background()` - 19 edges
5. `add_takeaway_band()` - 18 edges
6. `cm()` - 14 edges
7. `add_oval()` - 14 edges
8. `add_line()` - 13 edges
9. `build_slide_4()` - 11 edges
10. `remove_theme_style()` - 11 edges

## Surprising Connections (you probably didn't know these)
- `build_slide_1()` --calls--> `add_rect()`  [INFERRED]
  scripts\builders.py → scripts\helpers.py
- `build_slide_1()` --calls--> `add_textbox()`  [INFERRED]
  scripts\builders.py → scripts\helpers.py
- `build_slide_1()` --calls--> `add_takeaway_band()`  [INFERRED]
  scripts\builders.py → scripts\helpers.py
- `build_slide_2()` --calls--> `set_white_background()`  [INFERRED]
  scripts\builders.py → scripts\helpers.py
- `build_slide_2()` --calls--> `add_master_chrome()`  [INFERRED]
  scripts\builders.py → scripts\helpers.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.16
Nodes (21): build_layout15_slides(), _classify_omoc_bullet(), _extract_raw_levers(), _fallback_summarize_levers(), _first_sentence(), generate_impact_content(), parse_impact_file(), _parse_title() (+13 more)

### Community 1 - "Community 1"
Cohesion: 0.18
Nodes (14): build_slide(), Dispatcher : appelle le bon builder selon layout_n (1..11)., Dispatcher : appelle le bon builder selon layout_n (1..11)., Dispatcher : appelle le bon builder selon layout_n (1..11)., Dispatcher : appelle le bon builder selon layout_n (1..11)., generate(), init_presentation(), main() (+6 more)

### Community 2 - "Community 2"
Cohesion: 0.4
Nodes (10): build_slide_11(), build_slide_12(), build_slide_14(), build_slide_15(), build_slide_2(), build_slide_4(), plain_text(), Constructeurs par layout (slide 1 à 11) du template Palette Jessica. Chaque fon (+2 more)

### Community 3 - "Community 3"
Cohesion: 0.56
Nodes (8): add_line(), add_oval(), add_transparent_text_image(), cm(), hex_to_rgb(), hex_to_rgba(), _load_pil_font(), Helpers bas-niveau pour le template Palette Jessica. Manipule directement le XML

### Community 4 - "Community 4"
Cohesion: 0.29
Nodes (10): build_slide_1(), build_slide_10(), build_slide_13(), build_slide_3(), build_slide_5(), add_master_chrome(), Ajoute le 'chrome' commun à toutes les slides : titre, barre signature, footer,, Ajoute le 'chrome' commun à toutes les slides : titre, barre signature, footer, (+2 more)

### Community 5 - "Community 5"
Cohesion: 0.29
Nodes (7): add_teardrop(), Larme (teardrop). En python-pptx : MSO_SHAPE.TEAR (rotation à appliquer pour poi, Larme (teardrop). En python-pptx : MSO_SHAPE.TEAR (rotation à appliquer pour poi, Remove PowerPoint theme effects that can add shadows by default., Larme (teardrop). En python-pptx : MSO_SHAPE.TEAR., Remove PowerPoint theme effects that can add shadows by default., remove_theme_style()

### Community 6 - "Community 6"
Cohesion: 0.29
Nodes (7): add_rect(), emphasis_spans(), Retourne des segments (texte, style) en appliquant les emphases non chevauchante, Fusionne le style du placeholder avec une emphase locale., Fusionne le style du placeholder avec une emphase locale., Retourne des segments (texte, style) en appliquant les emphases non chevauchante, run_style()

### Community 7 - "Community 7"
Cohesion: 0.33
Nodes (6): build_slide_8(), build_slide_9(), add_textbox(), Crée un textbox avec texte simple ou spec enrichie (interligne + emphases)., Crée un textbox avec texte simple ou spec enrichie (interligne + emphases)., Crée un textbox avec un run unique aux propriétés spécifiées.

### Community 8 - "Community 8"
Cohesion: 0.33
Nodes (6): build_slide_6(), build_slide_7(), add_takeaway_band(), Bandeau bordeaux avec gradient vertical 3-stops + texte centré blanc., Bandeau bordeaux avec gradient vertical 3-stops + texte centré blanc., Bandeau bordeaux avec gradient vertical 3-stops + texte centré blanc.

### Community 9 - "Community 9"
Cohesion: 0.33
Nodes (5): is_omoc_bullet(), is_title_block(), Exploration approfondie des drawings OMOC dans le PDF. On cherche les 4 bullets, Bloc titre : en haut de page, texte non vide, pas trop petit., Bullet OMOC = rectangle dans la zone gauche (x < 350),     couleur bleue (0.23,

### Community 10 - "Community 10"
Cohesion: 0.5
Nodes (4): Applique les propriétés à un run et patche le XML pour cap / alpha si demandé., Applique les propriétés à un run et patche le XML pour cap / alpha si demandé., Applique les propriétés à un run et patche le XML pour cap / alpha si demandé., set_run_props()

### Community 11 - "Community 11"
Cohesion: 0.67
Nodes (3): normalize_line_spacing(), Convertit l'interligne JSON en valeur python-pptx (ratio ou points)., Convertit l'interligne JSON en valeur python-pptx (ratio ou points).

### Community 12 - "Community 12"
Cohesion: 0.67
Nodes (3): normalize_text_spec(), Accepte une chaine simple ou une spec enrichie de type {"text": ..., ...}., Accepte une chaine simple ou une spec enrichie de type {"text": ..., ...}.

## Knowledge Gaps
- **49 isolated node(s):** `Retourne le texte brut d'un champ enrichi, sans emphases inline.`, `Dispatcher : appelle le bon builder selon layout_n (1..11).`, `Crée une présentation vierge au bon format.`, `Trouve le logo depuis un chemin explicite ou les dossiers d'assets locaux.`, `Remove PowerPoint theme effects that can add shadows by default.` (+44 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `add_textbox()` connect `Community 7` to `Community 2`, `Community 3`, `Community 4`, `Community 6`, `Community 8`, `Community 10`, `Community 11`, `Community 12`?**
  _High betweenness centrality (0.090) - this node is a cross-community bridge._
- **Why does `init_presentation()` connect `Community 1` to `Community 3`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **Why does `cm()` connect `Community 3` to `Community 1`, `Community 2`, `Community 4`, `Community 5`, `Community 6`, `Community 7`, `Community 8`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Are the 15 inferred relationships involving `add_textbox()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`add_textbox()` has 15 INFERRED edges - model-reasoned connections that need verification._
- **Are the 15 inferred relationships involving `add_master_chrome()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`add_master_chrome()` has 15 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `add_rect()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`add_rect()` has 10 INFERRED edges - model-reasoned connections that need verification._
- **Are the 15 inferred relationships involving `set_white_background()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`set_white_background()` has 15 INFERRED edges - model-reasoned connections that need verification._