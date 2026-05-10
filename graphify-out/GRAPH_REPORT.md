# Graph Report - Skill_Jessica_template_Claude  (2026-05-10)

## Corpus Check
- 4 files · ~6,691 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 39 nodes · 117 edges · 8 communities detected
- Extraction: 48% EXTRACTED · 52% INFERRED · 0% AMBIGUOUS · INFERRED: 61 edges (avg confidence: 0.8)
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

## God Nodes (most connected - your core abstractions)
1. `add_textbox()` - 17 edges
2. `add_master_chrome()` - 16 edges
3. `set_white_background()` - 13 edges
4. `add_rect()` - 12 edges
5. `add_takeaway_band()` - 12 edges
6. `cm()` - 9 edges
7. `build_slide_10()` - 8 edges
8. `add_oval()` - 8 edges
9. `build_slide_4()` - 7 edges
10. `build_slide_9()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `build_slide_1()` --calls--> `set_white_background()`  [INFERRED]
  builders.py → helpers.py
- `build_slide_1()` --calls--> `add_textbox()`  [INFERRED]
  builders.py → helpers.py
- `build_slide_1()` --calls--> `add_takeaway_band()`  [INFERRED]
  builders.py → helpers.py
- `build_slide_2()` --calls--> `add_master_chrome()`  [INFERRED]
  builders.py → helpers.py
- `build_slide_2()` --calls--> `add_rect()`  [INFERRED]
  builders.py → helpers.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.5
Nodes (8): build_slide_10(), build_slide_2(), build_slide_4(), build_slide_5(), build_slide_9(), add_line(), add_oval(), set_white_background()

### Community 1 - "Community 1"
Cohesion: 0.38
Nodes (6): build_slide(), Dispatcher : appelle le bon builder selon layout_n (1..11)., generate(), init_presentation(), main(), Crée une présentation vierge au bon format.

### Community 2 - "Community 2"
Cohesion: 0.53
Nodes (6): build_slide_1(), build_slide_11(), build_slide_6(), add_master_chrome(), add_rect(), Ajoute le 'chrome' commun à toutes les slides : titre, barre signature, footer,

### Community 3 - "Community 3"
Cohesion: 0.5
Nodes (4): hex_to_rgb(), Helpers bas-niveau pour le template Palette Jessica. Manipule directement le XML, Applique les propriétés à un run et patche le XML pour cap / alpha si demandé., set_run_props()

### Community 4 - "Community 4"
Cohesion: 0.67
Nodes (3): build_slide_7(), add_takeaway_band(), Bandeau bordeaux avec gradient vertical 3-stops + texte centré blanc.

### Community 5 - "Community 5"
Cohesion: 0.67
Nodes (2): build_slide_8(), Constructeurs par layout (slide 1 à 11) du template Palette Jessica. Chaque fonc

### Community 6 - "Community 6"
Cohesion: 0.67
Nodes (3): build_slide_3(), add_textbox(), Crée un textbox avec un run unique aux propriétés spécifiées.

### Community 7 - "Community 7"
Cohesion: 0.67
Nodes (3): add_teardrop(), cm(), Larme (teardrop). En python-pptx : MSO_SHAPE.TEAR (rotation à appliquer pour poi

## Knowledge Gaps
- **9 isolated node(s):** `Constructeurs par layout (slide 1 à 11) du template Palette Jessica. Chaque fonc`, `Dispatcher : appelle le bon builder selon layout_n (1..11).`, `Crée une présentation vierge au bon format.`, `Helpers bas-niveau pour le template Palette Jessica. Manipule directement le XML`, `Applique les propriétés à un run et patche le XML pour cap / alpha si demandé.` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 5`** (3 nodes): `builders.py`, `build_slide_8()`, `Constructeurs par layout (slide 1 à 11) du template Palette Jessica. Chaque fonc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `add_textbox()` connect `Community 6` to `Community 0`, `Community 2`, `Community 3`, `Community 4`, `Community 5`, `Community 7`?**
  _High betweenness centrality (0.140) - this node is a cross-community bridge._
- **Why does `cm()` connect `Community 7` to `Community 0`, `Community 1`, `Community 2`, `Community 3`, `Community 4`, `Community 6`?**
  _High betweenness centrality (0.121) - this node is a cross-community bridge._
- **Why does `add_master_chrome()` connect `Community 2` to `Community 0`, `Community 3`, `Community 4`, `Community 5`, `Community 6`, `Community 7`?**
  _High betweenness centrality (0.094) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `add_textbox()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`add_textbox()` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 11 inferred relationships involving `add_master_chrome()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`add_master_chrome()` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 11 inferred relationships involving `set_white_background()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`set_white_background()` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `add_rect()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`add_rect()` has 8 INFERRED edges - model-reasoned connections that need verification._