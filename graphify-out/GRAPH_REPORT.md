# Graph Report - Skill_Jessica_template_Claude  (2026-05-14)

## Corpus Check
- 12 files · ~47,693 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 150 nodes · 393 edges · 10 communities detected
- Extraction: 78% EXTRACTED · 22% INFERRED · 0% AMBIGUOUS · INFERRED: 85 edges (avg confidence: 0.8)
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

## God Nodes (most connected - your core abstractions)
1. `add_textbox()` - 29 edges
2. `add_master_chrome()` - 25 edges
3. `add_rect()` - 22 edges
4. `add_takeaway_band()` - 19 edges
5. `set_white_background()` - 19 edges
6. `cm()` - 14 edges
7. `add_oval()` - 14 edges
8. `add_line()` - 13 edges
9. `parse_impact_file()` - 13 edges
10. `generate_impact_content()` - 12 edges

## Surprising Connections (you probably didn't know these)
- `build_slide_1()` --calls--> `add_rect()`  [INFERRED]
  scripts\builders.py → scripts\helpers.py
- `build_slide_2()` --calls--> `add_rect()`  [INFERRED]
  scripts\builders.py → scripts\helpers.py
- `build_slide_2()` --calls--> `add_oval()`  [INFERRED]
  scripts\builders.py → scripts\helpers.py
- `build_slide_3()` --calls--> `add_teardrop()`  [INFERRED]
  scripts\builders.py → scripts\helpers.py
- `build_slide_4()` --calls--> `cm()`  [INFERRED]
  scripts\builders.py → scripts\helpers.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.19
Nodes (34): build_slide_1(), build_slide_10(), build_slide_11(), build_slide_12(), build_slide_13(), build_slide_14(), build_slide_15(), build_slide_2() (+26 more)

### Community 1 - "Community 1"
Cohesion: 0.14
Nodes (33): add_line(), add_oval(), add_rect(), add_teardrop(), add_transparent_text_image(), cm(), emphasis_spans(), hex_to_rgb() (+25 more)

### Community 2 - "Community 2"
Cohesion: 0.17
Nodes (15): build_slide(), Dispatcher : appelle le bon builder selon layout_n (1..11)., Dispatcher : appelle le bon builder selon layout_n (1..11)., Dispatcher : appelle le bon builder selon layout_n (1..11)., Dispatcher : appelle le bon builder selon layout_n (1..11)., Dispatcher : appelle le bon builder selon layout_n (1..11)., generate(), init_presentation() (+7 more)

### Community 3 - "Community 3"
Cohesion: 0.21
Nodes (13): _fallback_summarize_levers(), parse_impact_pdf(), _parse_impact_pdf_fitz(), _parse_impact_pdf_pdfplumber(), Résumé mécanique de secours (≤ max_len caractères) utilisé quand     l'IA ne fou, Résumé mécanique de secours (≤ max_len caractères) utilisé quand     l'IA ne fou, Résumé mécanique de secours (≤ max_len caractères) utilisé quand     l'IA ne fou, Parse un fichier d'analyse d'impact PDF et retourne la même structure. (+5 more)

### Community 4 - "Community 4"
Cohesion: 0.21
Nodes (12): _extract_raw_levers(), _first_sentence(), parse_impact_file(), Parse un fichier d'analyse d'impact PPTX et retourne une liste de     dictionnai, Parse un fichier d'analyse d'impact PPTX et retourne une liste de     dictionnai, Parse un fichier d'analyse d'impact PPTX et retourne une liste de     dictionnai, Parse un fichier d'analyse d'impact PPTX et retourne une liste de     dictionnai, Extrait les données brutes de la table RESSORTS_CHANGE.      Retourne une liste (+4 more)

### Community 5 - "Community 5"
Cohesion: 0.38
Nodes (5): is_omoc_bullet(), is_title_block(), Exploration approfondie des drawings OMOC dans le PDF. On cherche les 4 bullets, Bloc titre : en haut de page, texte non vide, pas trop petit., Bullet OMOC = rectangle dans la zone gauche (x < 350),     couleur bleue (0.23,

### Community 6 - "Community 6"
Cohesion: 0.33
Nodes (6): build_layout15_slides(), Convertit la liste de populations en entrées content.json pour le Layout 15., Convertit la liste de populations en entrées content.json pour le Layout 15., Convertit la liste de populations en entrées content.json pour le Layout 15., Convertit la liste de populations en entrées content.json pour le Layout 15., Convertit la liste de populations en entrées content.json pour le Layout 15.

### Community 7 - "Community 7"
Cohesion: 0.33
Nodes (6): generate_impact_content(), Fonction principale : parse le fichier d'analyse d'impact et retourne     la lis, Fonction principale : parse le fichier d'analyse d'impact et retourne     la lis, Fonction principale : parse le fichier d'analyse d'impact et retourne     la lis, Fonction principale : parse le fichier d'analyse d'impact et retourne     la lis, Fonction principale : parse le fichier d'analyse d'impact et retourne     la lis

### Community 8 - "Community 8"
Cohesion: 0.4
Nodes (5): _parse_title(), Sépare le texte du TITLE en (population, effectif).      Formats attendus :, Sépare le texte du TITLE en (population, effectif).      Formats attendus :, Sépare le texte du TITLE en (population, effectif).      Formats attendus :, Sépare le texte du TITLE en (population, effectif).      Formats attendus :

### Community 9 - "Community 9"
Cohesion: 0.5
Nodes (4): _classify_omoc_bullet(), Détermine l'axe OMOC et le niveau (0-4) d'un bullet à partir de sa     position, Détermine l'axe OMOC et le niveau (0-4) d'un bullet à partir de sa     position, Détermine l'axe OMOC et le niveau (0-4) d'un bullet à partir de sa     position

## Knowledge Gaps
- **74 isolated node(s):** `Retourne le texte brut d'un champ enrichi, sans emphases inline.`, `Dispatcher : appelle le bon builder selon layout_n (1..11).`, `Crée une présentation vierge au bon format.`, `Trouve le logo depuis un chemin explicite ou les dossiers d'assets locaux.`, `Remove PowerPoint theme effects that can add shadows by default.` (+69 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `generate_impact_content()` connect `Community 7` to `Community 2`, `Community 3`, `Community 4`, `Community 6`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Why does `init_presentation()` connect `Community 2` to `Community 1`?**
  _High betweenness centrality (0.082) - this node is a cross-community bridge._
- **Why does `generate()` connect `Community 2` to `Community 7`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Are the 15 inferred relationships involving `add_textbox()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`add_textbox()` has 15 INFERRED edges - model-reasoned connections that need verification._
- **Are the 15 inferred relationships involving `add_master_chrome()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`add_master_chrome()` has 15 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `add_rect()` (e.g. with `build_slide_1()` and `build_slide_2()`) actually correct?**
  _`add_rect()` has 10 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `add_takeaway_band()` (e.g. with `build_slide_1()` and `build_slide_3()`) actually correct?**
  _`add_takeaway_band()` has 9 INFERRED edges - model-reasoned connections that need verification._