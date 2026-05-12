# Graph Report - Skill_Jessica_template_Claude  (2026-05-12)

## Corpus Check
- 5 files · ~21,154 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 104 nodes · 238 edges · 7 communities detected
- Extraction: 64% EXTRACTED · 36% INFERRED · 0% AMBIGUOUS · INFERRED: 85 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]

## God Nodes (most connected - your core abstractions)
1. `add_textbox()` - 27 edges
2. `add_master_chrome()` - 22 edges
3. `add_rect()` - 20 edges
4. `set_white_background()` - 17 edges
5. `add_takeaway_band()` - 16 edges
6. `cm()` - 12 edges
7. `add_oval()` - 12 edges
8. `add_line()` - 11 edges
9. `build_slide_4()` - 9 edges
10. `remove_theme_style()` - 9 edges

## Surprising Connections (you probably didn't know these)
- `build_slide_1()` --calls--> `set_white_background()`  [INFERRED]
  builders.py → helpers.py
- `build_slide_1()` --calls--> `add_master_chrome()`  [INFERRED]
  builders.py → helpers.py
- `build_slide_1()` --calls--> `add_rect()`  [INFERRED]
  builders.py → helpers.py
- `build_slide_2()` --calls--> `add_textbox()`  [INFERRED]
  builders.py → helpers.py
- `build_slide_3()` --calls--> `set_white_background()`  [INFERRED]
  builders.py → helpers.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.23
Nodes (24): build_slide_10(), build_slide_11(), build_slide_12(), build_slide_13(), build_slide_14(), build_slide_15(), build_slide_2(), build_slide_4() (+16 more)

### Community 1 - "Community 1"
Cohesion: 0.13
Nodes (21): build_layout15_slides(), _classify_omoc_bullet(), _extract_raw_levers(), _fallback_summarize_levers(), _first_sentence(), generate_impact_content(), parse_impact_file(), _parse_title() (+13 more)

### Community 2 - "Community 2"
Cohesion: 0.14
Nodes (17): build_slide_1(), build_slide_7(), build_slide_8(), add_takeaway_band(), add_textbox(), normalize_text_spec(), Fusionne le style du placeholder avec une emphase locale., Fusionne le style du placeholder avec une emphase locale. (+9 more)

### Community 3 - "Community 3"
Cohesion: 0.16
Nodes (16): build_slide_3(), add_teardrop(), add_transparent_text_image(), cm(), hex_to_rgba(), _load_pil_font(), normalize_line_spacing(), Helpers bas-niveau pour le template Palette Jessica. Manipule directement le XML (+8 more)

### Community 4 - "Community 4"
Cohesion: 0.16
Nodes (14): build_slide(), Dispatcher : appelle le bon builder selon layout_n (1..11)., Dispatcher : appelle le bon builder selon layout_n (1..11)., Dispatcher : appelle le bon builder selon layout_n (1..11)., Dispatcher : appelle le bon builder selon layout_n (1..11)., generate(), init_presentation(), main() (+6 more)

### Community 5 - "Community 5"
Cohesion: 0.5
Nodes (4): Applique les propriétés à un run et patche le XML pour cap / alpha si demandé., Applique les propriétés à un run et patche le XML pour cap / alpha si demandé., Applique les propriétés à un run et patche le XML pour cap / alpha si demandé., set_run_props()

### Community 6 - "Community 6"
Cohesion: 0.67
Nodes (3): emphasis_spans(), Retourne des segments (texte, style) en appliquant les emphases non chevauchante, Retourne des segments (texte, style) en appliquant les emphases non chevauchante

## Knowledge Gaps
- **48 isolated node(s):** `Constructeurs par layout (slide 1 à 11) du template Palette Jessica. Chaque fon`, `Retourne le texte brut d'un champ enrichi, sans emphases inline.`, `Dispatcher : appelle le bon builder selon layout_n (1..11).`, `Crée une présentation vierge au bon format.`, `Trouve le logo depuis un chemin explicite ou les dossiers d'assets locaux.` (+43 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `add_textbox()` connect `Community 2` to `Community 0`, `Community 3`, `Community 5`, `Community 6`?**
  _High betweenness centrality (0.129) - this node is a cross-community bridge._
- **Why does `init_presentation()` connect `Community 4` to `Community 3`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._
- **Why does `cm()` connect `Community 3` to `Community 0`, `Community 2`, `Community 4`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._
- **Are the 15 inferred relationships involving `add_textbox()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`add_textbox()` has 15 INFERRED edges - model-reasoned connections that need verification._
- **Are the 15 inferred relationships involving `add_master_chrome()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`add_master_chrome()` has 15 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `add_rect()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`add_rect()` has 10 INFERRED edges - model-reasoned connections that need verification._
- **Are the 15 inferred relationships involving `set_white_background()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`set_white_background()` has 15 INFERRED edges - model-reasoned connections that need verification._