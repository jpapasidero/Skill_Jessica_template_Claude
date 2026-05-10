# Graph Report - Skill_Jessica_template_Claude  (2026-05-10)

## Corpus Check
- 4 files · ~15,099 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 56 nodes · 151 edges · 12 communities detected
- Extraction: 58% EXTRACTED · 42% INFERRED · 0% AMBIGUOUS · INFERRED: 63 edges (avg confidence: 0.8)
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

## God Nodes (most connected - your core abstractions)
1. `add_textbox()` - 22 edges
2. `add_rect()` - 18 edges
3. `add_master_chrome()` - 17 edges
4. `add_takeaway_band()` - 14 edges
5. `set_white_background()` - 13 edges
6. `cm()` - 10 edges
7. `build_slide_4()` - 9 edges
8. `add_oval()` - 9 edges
9. `add_line()` - 9 edges
10. `build_slide_10()` - 8 edges

## Surprising Connections (you probably didn't know these)
- `build_slide_1()` --calls--> `add_master_chrome()`  [INFERRED]
  builders.py → helpers.py
- `build_slide_1()` --calls--> `add_rect()`  [INFERRED]
  builders.py → helpers.py
- `build_slide_1()` --calls--> `add_textbox()`  [INFERRED]
  builders.py → helpers.py
- `build_slide_2()` --calls--> `set_white_background()`  [INFERRED]
  builders.py → helpers.py
- `build_slide_2()` --calls--> `add_rect()`  [INFERRED]
  builders.py → helpers.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.33
Nodes (9): build_slide_1(), build_slide_11(), build_slide_7(), build_slide_8(), Constructeurs par layout (slide 1 à 11) du template Palette Jessica. Chaque fonc, add_takeaway_band(), Bandeau bordeaux avec gradient vertical 3-stops + texte centré blanc., Bandeau bordeaux avec gradient vertical 3-stops + texte centré blanc. (+1 more)

### Community 1 - "Community 1"
Cohesion: 0.32
Nodes (7): build_slide(), Dispatcher : appelle le bon builder selon layout_n (1..11)., Dispatcher : appelle le bon builder selon layout_n (1..11)., generate(), init_presentation(), main(), Crée une présentation vierge au bon format.

### Community 2 - "Community 2"
Cohesion: 0.33
Nodes (6): build_slide_3(), add_teardrop(), Larme (teardrop). En python-pptx : MSO_SHAPE.TEAR (rotation à appliquer pour poi, Larme (teardrop). En python-pptx : MSO_SHAPE.TEAR (rotation à appliquer pour poi, Remove PowerPoint theme effects that can add shadows by default., remove_theme_style()

### Community 3 - "Community 3"
Cohesion: 0.5
Nodes (5): add_rect(), hex_to_rgb(), Applique les propriétés à un run et patche le XML pour cap / alpha si demandé., Applique les propriétés à un run et patche le XML pour cap / alpha si demandé., set_run_props()

### Community 4 - "Community 4"
Cohesion: 0.5
Nodes (4): build_slide_2(), add_master_chrome(), Ajoute le 'chrome' commun à toutes les slides : titre, barre signature, footer,, Ajoute le 'chrome' commun à toutes les slides : titre, barre signature, footer,

### Community 5 - "Community 5"
Cohesion: 0.67
Nodes (4): build_slide_4(), resolve_background_asset(), add_oval(), cm()

### Community 6 - "Community 6"
Cohesion: 0.5
Nodes (4): build_slide_5(), add_textbox(), Crée un textbox avec texte simple ou spec enrichie (interligne + emphases)., Crée un textbox avec un run unique aux propriétés spécifiées.

### Community 7 - "Community 7"
Cohesion: 0.5
Nodes (4): build_slide_10(), build_slide_6(), build_slide_9(), add_line()

### Community 8 - "Community 8"
Cohesion: 0.5
Nodes (3): normalize_line_spacing(), Helpers bas-niveau pour le template Palette Jessica. Manipule directement le XML, Convertit l'interligne JSON en valeur python-pptx (ratio ou points).

### Community 9 - "Community 9"
Cohesion: 1.0
Nodes (2): normalize_text_spec(), Accepte une chaine simple ou une spec enrichie de type {"text": ..., ...}.

### Community 10 - "Community 10"
Cohesion: 1.0
Nodes (2): emphasis_spans(), Retourne des segments (texte, style) en appliquant les emphases non chevauchante

### Community 11 - "Community 11"
Cohesion: 1.0
Nodes (2): Fusionne le style du placeholder avec une emphase locale., run_style()

## Knowledge Gaps
- **20 isolated node(s):** `Constructeurs par layout (slide 1 à 11) du template Palette Jessica. Chaque fonc`, `Dispatcher : appelle le bon builder selon layout_n (1..11).`, `Crée une présentation vierge au bon format.`, `Helpers bas-niveau pour le template Palette Jessica. Manipule directement le XML`, `Remove PowerPoint theme effects that can add shadows by default.` (+15 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 9`** (2 nodes): `normalize_text_spec()`, `Accepte une chaine simple ou une spec enrichie de type {"text": ..., ...}.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 10`** (2 nodes): `emphasis_spans()`, `Retourne des segments (texte, style) en appliquant les emphases non chevauchante`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 11`** (2 nodes): `Fusionne le style du placeholder avec une emphase locale.`, `run_style()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `add_textbox()` connect `Community 6` to `Community 0`, `Community 2`, `Community 3`, `Community 4`, `Community 5`, `Community 7`, `Community 8`, `Community 9`, `Community 10`, `Community 11`?**
  _High betweenness centrality (0.189) - this node is a cross-community bridge._
- **Why does `cm()` connect `Community 5` to `Community 0`, `Community 1`, `Community 2`, `Community 3`, `Community 4`, `Community 6`, `Community 7`, `Community 8`?**
  _High betweenness centrality (0.095) - this node is a cross-community bridge._
- **Why does `add_rect()` connect `Community 3` to `Community 0`, `Community 2`, `Community 4`, `Community 5`, `Community 7`, `Community 8`, `Community 9`, `Community 10`, `Community 11`?**
  _High betweenness centrality (0.091) - this node is a cross-community bridge._
- **Are the 11 inferred relationships involving `add_textbox()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`add_textbox()` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `add_rect()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`add_rect()` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 11 inferred relationships involving `add_master_chrome()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`add_master_chrome()` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `add_takeaway_band()` (e.g. with `build_slide_1()` and `build_slide_3()`) actually correct?**
  _`add_takeaway_band()` has 8 INFERRED edges - model-reasoned connections that need verification._