# Graph Report - Skill_Jessica_template_Claude  (2026-05-12)

## Corpus Check
- 4 files · ~15,994 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 73 nodes · 175 edges · 9 communities detected
- Extraction: 63% EXTRACTED · 37% INFERRED · 0% AMBIGUOUS · INFERRED: 64 edges (avg confidence: 0.8)
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

## God Nodes (most connected - your core abstractions)
1. `add_textbox()` - 23 edges
2. `add_rect()` - 18 edges
3. `add_master_chrome()` - 18 edges
4. `add_takeaway_band()` - 15 edges
5. `set_white_background()` - 13 edges
6. `cm()` - 11 edges
7. `add_oval()` - 10 edges
8. `build_slide_4()` - 9 edges
9. `remove_theme_style()` - 9 edges
10. `add_line()` - 9 edges

## Surprising Connections (you probably didn't know these)
- `build_slide_1()` --calls--> `set_white_background()`  [INFERRED]
  builders.py → helpers.py
- `build_slide_1()` --calls--> `add_master_chrome()`  [INFERRED]
  builders.py → helpers.py
- `build_slide_1()` --calls--> `add_rect()`  [INFERRED]
  builders.py → helpers.py
- `build_slide_2()` --calls--> `set_white_background()`  [INFERRED]
  builders.py → helpers.py
- `build_slide_2()` --calls--> `add_master_chrome()`  [INFERRED]
  builders.py → helpers.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.18
Nodes (14): build_slide_1(), build_slide_11(), build_slide_7(), add_takeaway_band(), add_textbox(), emphasis_spans(), Retourne des segments (texte, style) en appliquant les emphases non chevauchante, Bandeau bordeaux avec gradient vertical 3-stops + texte centré blanc. (+6 more)

### Community 1 - "Community 1"
Cohesion: 0.21
Nodes (13): build_slide_3(), add_teardrop(), add_transparent_text_image(), cm(), hex_to_rgba(), _load_pil_font(), Helpers bas-niveau pour le template Palette Jessica. Manipule directement le XML, Larme (teardrop). En python-pptx : MSO_SHAPE.TEAR (rotation à appliquer pour poi (+5 more)

### Community 2 - "Community 2"
Cohesion: 0.21
Nodes (11): build_slide(), Dispatcher : appelle le bon builder selon layout_n (1..11)., Dispatcher : appelle le bon builder selon layout_n (1..11)., Dispatcher : appelle le bon builder selon layout_n (1..11)., generate(), init_presentation(), main(), Crée une présentation vierge au bon format. (+3 more)

### Community 3 - "Community 3"
Cohesion: 0.57
Nodes (7): build_slide_10(), build_slide_5(), build_slide_9(), add_line(), add_oval(), hex_to_rgb(), set_white_background()

### Community 4 - "Community 4"
Cohesion: 0.38
Nodes (7): build_slide_6(), build_slide_8(), add_master_chrome(), add_rect(), Ajoute le 'chrome' commun à toutes les slides : titre, barre signature, footer,, Ajoute le 'chrome' commun à toutes les slides : titre, barre signature, footer,, Ajoute le 'chrome' commun à toutes les slides : titre, barre signature, footer,

### Community 5 - "Community 5"
Cohesion: 0.27
Nodes (6): normalize_line_spacing(), normalize_text_spec(), Accepte une chaine simple ou une spec enrichie de type {"text": ..., ...}., Accepte une chaine simple ou une spec enrichie de type {"text": ..., ...}., Convertit l'interligne JSON en valeur python-pptx (ratio ou points)., Convertit l'interligne JSON en valeur python-pptx (ratio ou points).

### Community 6 - "Community 6"
Cohesion: 0.5
Nodes (4): build_slide_2(), build_slide_4(), Constructeurs par layout (slide 1 à 11) du template Palette Jessica. Chaque fonc, resolve_background_asset()

### Community 7 - "Community 7"
Cohesion: 0.5
Nodes (4): Applique les propriétés à un run et patche le XML pour cap / alpha si demandé., Applique les propriétés à un run et patche le XML pour cap / alpha si demandé., Applique les propriétés à un run et patche le XML pour cap / alpha si demandé., set_run_props()

### Community 8 - "Community 8"
Cohesion: 0.67
Nodes (3): Fusionne le style du placeholder avec une emphase locale., Fusionne le style du placeholder avec une emphase locale., run_style()

## Knowledge Gaps
- **33 isolated node(s):** `Constructeurs par layout (slide 1 à 11) du template Palette Jessica. Chaque fonc`, `Dispatcher : appelle le bon builder selon layout_n (1..11).`, `Crée une présentation vierge au bon format.`, `Trouve le logo depuis un chemin explicite ou les dossiers d'assets locaux.`, `Helpers bas-niveau pour le template Palette Jessica. Manipule directement le XML` (+28 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `add_textbox()` connect `Community 0` to `Community 1`, `Community 3`, `Community 4`, `Community 5`, `Community 6`, `Community 7`, `Community 8`?**
  _High betweenness centrality (0.187) - this node is a cross-community bridge._
- **Why does `cm()` connect `Community 1` to `Community 0`, `Community 2`, `Community 3`, `Community 4`, `Community 6`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._
- **Why does `add_takeaway_band()` connect `Community 0` to `Community 1`, `Community 3`, `Community 4`, `Community 6`?**
  _High betweenness centrality (0.097) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `add_textbox()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`add_textbox()` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `add_rect()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`add_rect()` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 11 inferred relationships involving `add_master_chrome()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`add_master_chrome()` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `add_takeaway_band()` (e.g. with `build_slide_1()` and `build_slide_3()`) actually correct?**
  _`add_takeaway_band()` has 8 INFERRED edges - model-reasoned connections that need verification._