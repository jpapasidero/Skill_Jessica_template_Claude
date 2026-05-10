"""
Constructeurs par layout (slide 1 à 11) du template Palette Jessica.
Chaque fonction reçoit (prs, slide, content_dict) et remplit la slide.
content_dict contient les valeurs textuelles fournies par l'utilisateur.
"""
from pathlib import Path

try:
    from .helpers import (add_textbox, add_rect, add_oval, add_teardrop, add_line,
                          add_takeaway_band, add_master_chrome, set_white_background, cm)
except ImportError:
    from helpers import (add_textbox, add_rect, add_oval, add_teardrop, add_line,
                         add_takeaway_band, add_master_chrome, set_white_background, cm)


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def resolve_background_asset(filename):
    for asset_dir in ("assets", "asset"):
        path = PROJECT_ROOT / asset_dir / "backgrounds" / filename
        if path.exists():
            return path
    return None


# ============================================================
# LAYOUT 1 — Hook sens + factuel
# ============================================================
def build_slide_1(slide, c, page_num=1, total=11, logo_path=None):
    set_white_background(slide)
    add_master_chrome(slide, c.get("title", "Hook sens + factuel"),
                       page_num=page_num, total=total, logo_path=logo_path)

    # LeftAccentBar bordeaux
    add_rect(slide, 2, 3.5, 0.11, 6.3, "#A25871", name="LeftAccentBar")

    # Manifesto
    add_textbox(slide, 2.33, 3.44, 21.16, 2.86, c.get("manifesto", ""),
                font="Segoe UI Light", size_pt=24, color_hex="#474E67",
                anchor="t", name="S01_MANIFESTO", line_spacing=1.15,
                emphasis_style={"font": "Segoe UI", "bold": True, "color_hex": "#A25871"})
    # Body
    add_textbox(slide, 2.33, 7.96, 20.46, 2.82, c.get("body", ""),
                font="Segoe UI", size_pt=13, color_hex="#474E67",
                name="S01_BODY", line_spacing=1.3,
                emphasis_style={"font": "Segoe UI", "bold": True, "color_hex":"#070E1D"})

    # 3 KPI verticaux
    stats = c.get("stats", [])
    colors = ["#6A5D79", "#A25871", "#FDA85B"]
    accents = ["#484C6A", "#A25871", "#FDA85B"]
    ys_value = [3.18, 7.76, 12.35]
    ys_label = [5.29, 9.88, 14.46]
    ys_sub = [6.07, 10.65, 15.24]
    ys_accent = [2.89, 7.48, 12.05]

    for i in range(3):
        s = stats[i] if i < len(stats) else {}
        # mini accent
        add_rect(slide, 24.20, ys_accent[i], 1.13, 0.07, accents[i], name=f"KpiAccent_{i+1}")
        # value
        add_textbox(slide, 24.20, ys_value[i], 9.45, 2.12, s.get("value", ""),
                    font="Segoe UI Black", size_pt=44, bold=True, color_hex=colors[i],
                    name=f"S01_STAT_{i+1}_VALUE")
        # label
        add_textbox(slide, 24.20, ys_label[i], 9.45, 0.78, s.get("label", ""),
                    font="Segoe UI", size_pt=13, bold=True, color_hex="#070E1D",
                    name=f"S01_STAT_{i+1}_LABEL")
        # sublabel
        add_textbox(slide, 24.20, ys_sub[i], 9.45, 0.71, s.get("sublabel", ""),
                    font="Segoe UI", size_pt=10, color_hex="#474E67",
                    name=f"S01_STAT_{i+1}_SUBLABEL")

    add_takeaway_band(slide, c.get("takeaway", "Take away"))


# ============================================================
# LAYOUT 2 — Hook sens + vision (3 colonnes small caps)
# ============================================================
def build_slide_2(slide, c, page_num=2, total=11, logo_path=None):
    set_white_background(slide)
    add_master_chrome(slide, c.get("title", "Hook sens + vision"),
                       page_num=page_num, total=total, logo_path=logo_path)

    cols = c.get("columns", [])
    xs = [2.36, 12.77, 23.19]
    title_colors = ["#6A5D79", "#A25871", "#FDA85B"]
    sep_xs = [1.69, 12.11, 22.53]

    for i in range(3):
        col = cols[i] if i < len(cols) else {}
        # séparateur vertical
        add_rect(slide, sep_xs[i], 4.71, 0.10, 9.9, title_colors[i],
                 name=f"S02_SEP_{i+1}")
        # titre small caps
        add_textbox(slide, xs[i], 7.07, 9.0, 2.66, col.get("title", ""),
                    font="Segoe UI", size_pt=20, bold=True,
                    color_hex=title_colors[i], cap="small",
                    name=f"S02_COL_{i+1}_TITLE")
        # body
        add_textbox(slide, xs[i], 11.35, 9.0, 3.13, col.get("body", ""),
                    font="Segoe UI Light", size_pt=14, color_hex="#474E67",
                    name=f"S02_COL_{i+1}_BODY", line_spacing=1.3)


# ============================================================
# LAYOUT 3 — Liste 6 points (larmes)
# ============================================================
def build_slide_3(slide, c, page_num=3, total=11, logo_path=None):
    set_white_background(slide)
    add_master_chrome(slide, c.get("title", "Liste en 6 points"),
                       page_num=page_num, total=total, logo_path=logo_path)

    factors = c.get("factors", [])
    teardrop_colors = ["#D8DBE8", "#BBB4C4", "#D5B3BE", "#F1D3D5", "#FEE3CA", "#FEF4DA"]
    # 3x2 grille
    positions = [
        (1.43, 6.89, 3.42, 3.59),  # F1 label x,y et larme x,y (centrée au-dessus)
        (13.36, 6.95, 15.36, 3.65),
        (24.86, 6.95, 26.86, 3.65),
        (1.47, 14.21, 3.46, 10.91),
        (13.20, 14.21, 15.20, 10.91),
        (24.56, 14.21, 26.56, 10.91),
    ]

    for i in range(6):
        f = factors[i] if i < len(factors) else {}
        lx, ly, tx, ty = positions[i]
        label_h = 0.86
        label_w = 6.94
        lx = tx + 1.5 - label_w / 2
        # larme
        add_teardrop(slide, tx, ty, 3.0, 3.0, teardrop_colors[i],
                     name=f"S03_TEARDROP_{i+1}")
        # label
        add_textbox(slide, lx, ly, label_w, label_h, f.get("label", ""),
                    font="Segoe UI", size_pt=14, bold=True,
                    color_hex="#070E1D", cap="small", align="center", anchor="m",
                    name=f"S03_FACTOR_{i+1}_LABEL")

    add_takeaway_band(slide, c.get("takeaway", "Take away"))


# ============================================================
# LAYOUT 4 — Triptyque (3 cercles)
# ============================================================
def build_slide_4(slide, c, page_num=4, total=11, logo_path=None):
    set_white_background(slide)
    triangle_bg = resolve_background_asset("triangle_bg.png")
    if triangle_bg:
        triangle = slide.shapes.add_picture(str(triangle_bg), cm(0), cm(3),
                                            width=cm(14.8), height=cm(12.9))
        triangle.left = int((cm(33.867) - triangle.width) / 2)

    add_master_chrome(slide, c.get("title", "Triptyque"),
                       page_num=page_num, total=total, logo_path=logo_path)

    nodes = c.get("nodes", {})

    # Labels aux 3 sommets
    label_positions = [
        ("top", 19.61, 1.78, 19.61, 2.55),
        ("left", 2.81, 11.84, 2.81, 12.61),
        ("right", 24.80, 11.84, 24.80, 12.61),
    ]
    for key, lx, ly, sx, sy in label_positions:
        n = nodes.get(key, {})
        add_textbox(slide, lx, ly, 6.08, 1.03, n.get("label", ""),
                    font="Segoe UI", size_pt=18, bold=True, color_hex="#070E1D",
                    name=f"S04_{key.upper()}_LABEL")
        add_textbox(slide, sx, sy, 6.08, 0.86, n.get("sublabel", ""),
                    font="Segoe UI Light", size_pt=14, color_hex="#474E67",
                    name=f"S04_{key.upper()}_SUBLABEL")

    add_takeaway_band(slide, c.get("takeaway", "Take away"))


# ============================================================
# LAYOUT 5 — Timeline 4 étapes
# ============================================================
def build_slide_5(slide, c, page_num=5, total=11, logo_path=None):
    set_white_background(slide)
    add_master_chrome(slide, c.get("title", "Timeline"),
                       page_num=page_num, total=total, logo_path=logo_path)

    steps = c.get("steps", [])
    xs = [1.69, 9.44, 17.18, 24.92]
    period_colors = ["#6A5D79", "#A25871", "#D4737A", "#FDA85B"]
    bullet_colors = period_colors
    line_colors = ["#BBB4C4", "#D5B3BE", "#F1D3D5"]

    # ligne reliant les puces (à hauteur du centre des puces)
    bullet_cy = 7.64 + 0.46
    for i in range(3):
        x1 = xs[i] + 0.92
        x2 = xs[i+1]
        add_line(slide, x1, bullet_cy, x2, bullet_cy, line_colors[i], width_pt=1.5)

    for i in range(4):
        s = steps[i] if i < len(steps) else {}
        # puce numérotée (cercle plein avec chiffre blanc centré)
        add_oval(slide, xs[i], 7.64, 0.92, 0.92, bullet_colors[i],
                 name=f"S05_STEP_{i+1}_BULLET")
        add_textbox(slide, xs[i], 7.64, 0.92, 0.92, str(i+1),
                    font="Segoe UI Black", size_pt=12, bold=True, color_hex="#FFFFFF",
                    align="center", anchor="m", name=f"S05_STEP_{i+1}_NUMBER")
        # period (small caps colorée)
        add_textbox(slide, xs[i], 8.87, 7.47, 0.62, s.get("period", ""),
                    font="Segoe UI", size_pt=12, bold=True,
                    color_hex=period_colors[i], cap="small",
                    name=f"S05_STEP_{i+1}_PERIOD")
        # title
        add_textbox(slide, xs[i], 9.60, 7.47, 0.80, s.get("step_title", ""),
                    font="Segoe UI", size_pt=16, bold=True, color_hex="#070E1D",
                    name=f"S05_STEP_{i+1}_TITLE")
        # body
        add_textbox(slide, xs[i], 10.54, 7.47, 1.93, s.get("body", ""),
                    font="Segoe UI Light", size_pt=12, color_hex="#474E67",
                    name=f"S05_STEP_{i+1}_BODY", line_spacing=1.3)


# ============================================================
# LAYOUT 6 — Tableau 5x4
# ============================================================
def build_slide_6(slide, c, page_num=6, total=11, logo_path=None):
    set_white_background(slide)
    add_master_chrome(slide, c.get("title", "Tableau"),
                       page_num=page_num, total=total, logo_path=logo_path)

    headers = c.get("headers", ["", "", "", "", ""])
    rows = c.get("rows", [])

    col_x = [1.52, 11.59, 17.38, 22.26, 28.70]
    col_w = [10.07, 5.82, 4.9, 6.47, 4.52]
    row_y = [6.56, 7.97, 9.38, 10.79]
    row_h = 1.4
    tab_w = 31.62
    header_y = 5.27
    header_h = 1.27

    # En-tête (rectangles violet sourd)
    for i in range(5):
        add_rect(slide, col_x[i], header_y, col_w[i], header_h, "#6A5D79",
                 name=f"S06_HEADER_{i+1}_BG")
        add_textbox(slide, col_x[i], header_y, col_w[i], header_h,
                    headers[i] if i < len(headers) else "",
                    font="Segoe UI", size_pt=16, bold=True, color_hex="#FFFFFF",
                    align="left", anchor="m", name=f"S06_HEADER_C{i+1}")

    # Lignes (zébrage)
    for r in range(4):
        is_even = (r % 2 == 1)
        bg = "#F4F5F9" if is_even else "#FFFFFF"
        # bande de fond pour la ligne
        add_rect(slide, col_x[0], row_y[r], tab_w, row_h, bg, name=f"S06_R{r+1}_BG")

        row_data = rows[r] if r < len(rows) else [""]*5
        for ci in range(5):
            cell_text = row_data[ci] if ci < len(row_data) else ""
            # mise en forme par colonne
            if ci == 0:
                font, size, bold, col = "Segoe UI", 14, True, "#070E1D"
            elif ci == 3:
                font, size, bold, col = "Segoe UI", 14, True, "#6A5D79"
            elif ci == 4:
                font, size, bold, col = "Segoe UI", 14, True, "#474E67"
            else:
                font, size, bold, col = "Segoe UI", 14, False, "#474E67"

            add_textbox(slide, col_x[ci], row_y[r], col_w[ci], row_h, cell_text,
                        font=font, size_pt=size, bold=bold, color_hex=col,
                        align="left", anchor="m", name=f"S06_R{r+1}C{ci+1}")
            add_line(slide, col_x[0], row_y[r]+row_h, col_x[0]+tab_w, row_y[r]+row_h, "#D8DBE8", width_pt=0.75, dash=False)

    add_takeaway_band(slide, c.get("takeaway", "Take away"))


# ============================================================
# LAYOUT 7 — Dashboard (6 KPI + 5 barres)
# ============================================================
def build_slide_7(slide, c, page_num=7, total=11, logo_path=None):
    set_white_background(slide)
    add_master_chrome(slide, c.get("title", "Dashboard"),
                       page_num=page_num, total=total, logo_path=logo_path)

    kpis = c.get("kpis", [])
    bars = c.get("bars", [])
    section_label = c.get("section_label", "")

    pastels = ["#D8DBE8", "#BBB4C4", "#D5B3BE", "#F1D3D5", "#FEE3CA", "#FEF4DA"]
    strongs = ["#484C6A", "#6A5D79", "#A25871", "#D4737A", "#FDA85B", "#FBCC58"]
    xs = [1.06, 6.29, 11.51, 16.73, 21.95, 27.18]

    # 6 cartes KPI
    for i in range(6):
        k = kpis[i] if i < len(kpis) else {}
        add_rect(slide, xs[i], 3.71, 5.0, 4.44, pastels[i], rounded=True,
                 name=f"S07_KPI_{i+1}_CARD")
        add_textbox(slide, xs[i] + 0.11, 4.78, 4.8, 1.80, k.get("value", ""),
                    font="Segoe UI Black", size_pt=36, bold=True,
                    color_hex=strongs[i], align="center", anchor="m",
                    name=f"S07_KPI_{i+1}_LABEL")
        add_textbox(slide, xs[i] + 0.11, 6.65, 4.8, 0.73, k.get("sublabel", ""),
                    font="Segoe UI", size_pt=11, color_hex="#474E67",
                    align="center", name=f"S07_KPI_{i+1}_SUBLABEL")

    # Section label
    add_rect(slide, 1.09, 8.50, 31.08, 1.17, "#F2F2F2", line_hex=None, line_w_pt=0,
             rounded=False, radius_adjust=0.1, name=None)    
    add_textbox(slide, 1.09, 8.50, 31.08, 1.17, section_label,
                font="Segoe UI", size_pt=12, bold=True, italic=True,
                color_hex="#070E1D", align="center", anchor="m",name="S07_SECTION_LABEL")

    # 5 barres horizontales
    bar_ys = [10.09, 11.40, 12.68, 13.96, 15.18]
    bar_colors = ["#6A5D79", "#A25871", "#D4737A", "#FDA85B", "#FBCC58"]
    for i in range(5):
        b = bars[i] if i < len(bars) else {}
        # label
        add_textbox(slide, 1.06, bar_ys[i], 6.94, 0.97, b.get("label", ""),
                    font="Segoe UI", size_pt=11, bold=True, color_hex="#070E1D",
                    anchor="m", name=f"S07_BAR_{i+1}_LABEL")
        # barre (longueur proportionnelle à value 0..100)
        val = float(b.get("value", 50))
        max_w = 24.0
        bar_w = max_w * (val / 100.0)
        add_rect(slide, 8.20, bar_ys[i] + 0.20, bar_w, 0.55, bar_colors[i],
                 rounded=True, radius_adjust=0.5, name=f"S07_BAR_{i+1}_BAR")
        # valeur affichée à droite
        add_textbox(slide, 8.20 + bar_w + 0.10, bar_ys[i] + 0.10, 1.6, 0.75,
                    f"{int(val)}%", font="Segoe UI", size_pt=11, bold=True,
                    color_hex="#070E1D", anchor="m", name=f"S07_BAR_{i+1}_VALUE")

    add_takeaway_band(slide, c.get("takeaway", "Take away"))


# ============================================================
# LAYOUT 8 — Comparatif (5 lignes barres horizontales)
# ============================================================
def build_slide_8(slide, c, page_num=8, total=11, logo_path=None):
    set_white_background(slide)
    add_master_chrome(slide, c.get("title", "Comparatif"),
                       page_num=page_num, total=total, logo_path=logo_path)

    add_textbox(slide, 1.08, 4.04, 31.70, 0.97, c.get("subtitle", ""),
                font="Segoe UI Black", size_pt=21, bold=True,
                color_hex="#6A5D79", name="S08_SUBTITLE")

    legends = c.get("legends", ["Série 1", "Série 2"])
    add_textbox(slide, 21.81, 6.14, 5.56, 0.89, legends[0],
                font="Segoe UI", size_pt=10, color_hex="#474E67",
                align="left", anchor="m",name="S08_LEGEND_1")
    add_textbox(slide, 28.47, 6.14, 5.56, 0.89, legends[1],
                font="Segoe UI", size_pt=10, color_hex="#474E67",
                align="left", anchor="m",name="S08_LEGEND_2")

    # petits carrés couleurs des légendes
    add_rect(slide, 21.30, 6.30, 0.45, 0.45, "#D5B3BE", name="S08_LEGEND_1_SQ")
    add_rect(slide, 27.96, 6.30, 0.45, 0.45, "#FEE3CA", name="S08_LEGEND_2_SQ")

    rows = c.get("rows", [])
    row_ys = [8.05, 9.35, 10.66, 11.97, 13.27]

    for i in range(5):
        r = rows[i] if i < len(rows) else {}
        # label
        add_textbox(slide, 1.08, row_ys[i], 10.56, 0.97, r.get("label", ""),
                    font="Segoe UI", size_pt=12, bold=True, color_hex="#070E1D",
                    anchor="m", name=f"S08_ROW_{i+1}_LABEL")
        # barres : normalisation par ligne (la plus grande des deux = barre pleine)
        v1 = float(r.get("value_1", 0))
        v2 = float(r.get("value_2", 0))
        v_max = max(abs(v1), abs(v2), 1)
        max_w_1 = 12.22
        max_w_2 = 7.33
        # ratio relatif : la plus grande prend ~80% de l'espace dispo
        w1 = max_w_1 * (abs(v1) / v_max) * 0.85
        w2 = max_w_2 * (abs(v2) / v_max) * 0.85
        add_rect(slide, 11.94, row_ys[i] + 0.10, max(w1, 0.5), 0.83, "#D5B3BE",
                 rounded=True, radius_adjust=0.3, name=f"S08_ROW_{i+1}_BAR_1")
        add_rect(slide, 24.44, row_ys[i] + 0.10, max(w2, 0.5), 0.83, "#FEE3CA",
                 rounded=True, radius_adjust=0.3, name=f"S08_ROW_{i+1}_BAR_2")
        # valeurs (format display si fourni, sinon valeur brute)
        d1 = str(r.get("display_1", v1))
        d2 = str(r.get("display_2", v2))
        add_textbox(slide, 11.94 + max(w1, 0.5) + 0.10, row_ys[i] + 0.10,
                    2.0, 0.83, d1,
                    font="Segoe UI", size_pt=12, bold=True, color_hex="#474E67",
                    anchor="m", name=f"S08_ROW_{i+1}_VALUE_1")
        add_textbox(slide, 24.44 + max(w2, 0.5) + 0.10, row_ys[i] + 0.10,
                    2.0, 0.83, d2,
                    font="Segoe UI", size_pt=12, bold=True, color_hex="#474E67",
                    anchor="m", name=f"S08_ROW_{i+1}_VALUE_2")

    add_takeaway_band(slide, c.get("takeaway", "Take away"))


# ============================================================
# LAYOUT 9 — Risques & Opportunités (grille 2x3)
# ============================================================
def build_slide_9(slide, c, page_num=9, total=11, logo_path=None):
    set_white_background(slide, "#EFF1F6")
    add_master_chrome(slide, c.get("title", "Risques & Opportunités"),
                       page_num=page_num, total=total, logo_path=logo_path)

    risks = c.get("risks", [])
    opps = c.get("opportunities", [])
    card_w, card_h = 10.89, 6.40
    card_gap = 0.26
    group_w = card_w * 3 + card_gap * 2
    group_x = (33.867 - group_w) / 2
    card_xs = [group_x + i * (card_w + card_gap) for i in range(3)]

    LEVEL_COLORS = {
        "high_risk": "#C00000",
        "medium_risk": "#FDA85B",
        "high_opp": "#00B050",
        "medium_opp": "#A8A400",
    }
    LEVEL_BACKGROUNDS = {
        "high_risk": "#FF97973",
        "medium_risk": "#FEE3CA",
        "high_opp": "#69FFAD",
        "medium_opp": "#FFFF85",
    }
    LEVEL_TEXTS = {
        "high_risk": "Risque élevé",
        "medium_risk": "Risque moyen",
        "high_opp": "Gain élevé",
        "medium_opp": "Gain moyen",
    }

    # Ligne 1 : Risques
    for i in range(3):
        x = card_xs[i]
        r = risks[i] if i < len(risks) else {}
        # carte
        add_rect(slide, x, 3.50, card_w, card_h, "#FFFFFF",
                 line_hex="#AFB5C8", line_w_pt=0.25, rounded=True,
                 name=f"S09_RISK_{i+1}_CARD")
        # icône violette (cercle simulant Wingdings)
        add_rect(slide, x + 0.13, 4.00, 0.85, 0.85, "#BBB4C4",text="L",
                rounded=True,radius_adjust=0.15,
                font="Wingdings", size_pt=18, bold=True, color_hex="#6A5D79",
                align="center", anchor="m", name=f"S09_RISK_{i+1}_ICON")
        # title
        add_textbox(slide, x + 1.20, 3.85, 9.0, 0.77, r.get("title", ""),
                    font="Segoe UI", size_pt=12, bold=True, color_hex="#070E1D", margin_left=0,
                    name=f"S09_RISK_{i+1}_TITLE")
        # level (small caps colorée)
        level = r.get("level", "high_risk")
        add_rect(slide, x + 1.20, 4.62, 2.48, 0.53, LEVEL_BACKGROUNDS.get(level,"#FF97973"),
                    rounded=True,radius_adjust=0.15,
                    text=LEVEL_TEXTS.get(level, ""),font="Segoe UI", size_pt=10,
                    color_hex=LEVEL_COLORS.get(level, "#C00000"), cap="small",
                    align="center",anchor="m",name=f"S09_RISK_{i+1}_LEVEL")
        # body
        add_textbox(slide, x + 0.13, 5.30, card_w - 0.40, 1.20, r.get("body", ""),
                    font="Segoe UI", size_pt=10, color_hex="#070E1D", margin_left=0,
                    name=f"S09_RISK_{i+1}_BODY")
        # séparateur pointillé
        add_line(slide, x + 0.20, 6.80, x + card_w - 0.20, 6.80, "#AFB5C8",
                 width_pt=0.75, dash=True)
        # action tag (PARADE)
        add_rect(slide, x + 0.20, 7.10, 1.71, 0.53, "#DDE7CF",text="Parade",
                    rounded=True,radius_adjust=0.15,
                    font="Segoe UI", size_pt=10, 
                    color_hex="#8DAC95", cap="small", align="center",anchor="m",
                    name=f"S09_RISK_{i+1}_ACTION_TAG")
        # action body
        add_textbox(slide, x + 2.10, 7.10, card_w - 2.30, 1.0, r.get("action", ""),
                    font="Segoe UI Light", size_pt=10, color_hex="#070E1D",
                    margin_top=0, name=f"S09_RISK_{i+1}_ACTION_BODY")

    # Ligne 2 : Opportunités
    for i in range(3):
        x = card_xs[i]
        o = opps[i] if i < len(opps) else {}
        add_rect(slide, x, 10.30, card_w, card_h, "#FFFFFF",
                 line_hex="#AFB5C8", line_w_pt=0.25, rounded=True,
                 name=f"S09_OPP_{i+1}_CARD")
        add_rect(slide, x + 0.13, 10.80, 0.85, 0.85, "#FEF4da",text="J",
                rounded=True,radius_adjust=0.15,
                font="Wingdings", size_pt=18, bold=True, color_hex="#FBCC58",
                align="center",anchor="m", name=f"S09_OPP_{i+1}_ICON")
        add_textbox(slide, x + 1.20, 10.65, 9.0, 0.77, o.get("title", ""),
                    font="Segoe UI", size_pt=12, bold=True, color_hex="#070E1D", margin_left=0,
                    name=f"S09_OPP_{i+1}_TITLE")
        level = o.get("level", "high_opp")
        add_rect(slide, x + 1.20, 11.42, 2.48, 0.53, LEVEL_BACKGROUNDS.get(level,"#69FFAD"),
                    rounded=True,radius_adjust=0.15,
                    text=LEVEL_TEXTS.get(level, ""),font="Segoe UI", size_pt=10,
                    color_hex=LEVEL_COLORS.get(level, "#00B050"), cap="small",
                    align="center",anchor="m", name=f"S09_OPP_{i+1}_LEVEL")
        add_textbox(slide, x + 0.13, 12.10, card_w - 0.40, 1.20, o.get("body", ""),
                    font="Segoe UI", size_pt=10, color_hex="#070E1D", margin_left=0,
                    name=f"S09_OPP_{i+1}_BODY")
        add_line(slide, x + 0.20, 13.60, x + card_w - 0.20, 13.60, "#AFB5C8",
                 width_pt=0.75, dash=True)
        add_rect(slide, x + 0.20, 13.90, 1.71, 0.53, "#DDE7CF",text="Levier",
                    rounded=True,radius_adjust=0.15,
                    font="Segoe UI", size_pt=10,
                    color_hex="#8DAC95", cap="small", align="center",anchor="m",
                    name=f"S09_OPP_{i+1}_ACTION_TAG")
        add_textbox(slide, x + 2.10, 13.90, card_w - 2.30, 1.0, o.get("action", ""),
                    font="Segoe UI Light", size_pt=10, color_hex="#070E1D",
                    margin_top=0, name=f"S09_OPP_{i+1}_ACTION_BODY")


# ============================================================
# LAYOUT 10 — Plan d'action 3 phases
# ============================================================
def build_slide_10(slide, c, page_num=10, total=11, logo_path=None):
    set_white_background(slide)
    add_master_chrome(slide, c.get("title", "Plan d'action"),
                       page_num=page_num, total=total, logo_path=logo_path)

    # Date
    add_textbox(slide, 28.11, 0.75, 5.08, 1.29, c.get("date", ""),
                font="Calibri", size_pt=12, color_hex="#FFFFFF",
                align="right", anchor="m", name="S10_DATE")

    phases = c.get("phases", [])
    slide_w = 33.867
    card_w = 10.50
    card_gap = 0.62
    group_w = card_w * 3 + card_gap * 2
    group_x = (slide_w - group_w) / 2
    card_xs = [group_x + i * (card_w + card_gap) for i in range(3)]
    title_x_offset = 1.76
    item_x_offset = 1.02
    band_colors = ["#6A5D79", "#A25871", "#FDA85B"]
    card_y = 4.10
    band_h = 2.10
    content_top = card_y + band_h
    content_h = 11.49 - band_h
    item_section_h = content_h / 3
    item_title_h = 1.02
    item_body_h = 0.85
    item_titles_y = [content_top + j * item_section_h + 0.10 for j in range(3)]
    item_bodies_y = [y + 0.96 for y in item_titles_y]
    separator_ys = [content_top + item_section_h * j for j in range(1, 3)]

    for i in range(3):
        p = phases[i] if i < len(phases) else {}
        # carte (rectangle blanc avec bordure légère)
        add_rect(slide, card_xs[i], card_y, card_w, 11.49, "#FFFFFF",
                 line_hex="#E0E2EA", line_w_pt=0.25, name=f"S10_PHASE_{i+1}_CARD")
        # bandeau coloré supérieur
        add_rect(slide, card_xs[i], card_y, card_w, band_h, band_colors[i],
                 name=f"S10_PHASE_{i+1}_BAND")
        # numéro (gros chiffre blanc)
        add_oval(slide, card_xs[i]+0.2, card_y+band_h/4, 1.14, 1.14, band_colors[i],
                 line_hex="#FFFFFF", line_w_pt=2.25, text=str(i+1),
                 font="Segoe UI", size_pt=24, bold=True, color_hex="#FFFFFF",
                 align="center", anchor="m", name=f"S10_PHASE_{i+1}_NUMBER")
        # titre phase
        add_textbox(slide, card_xs[i] + title_x_offset, 4.33, 8.40, 0.95, p.get("phase_title", ""),
                    font="Segoe UI", size_pt=16, bold=True, color_hex="#FFFFFF",
                    anchor="m", name=f"S10_PHASE_{i+1}_TITLE")
        # sous-titre phase
        add_textbox(slide, card_xs[i] + title_x_offset, 5.25, 8.40, 0.81, p.get("phase_subtitle", ""),
                    font="Segoe UI", size_pt=12, italic=True, color_hex="#FFFFFF",
                    name=f"S10_PHASE_{i+1}_SUBTITLE")

        # 3 items
        items = p.get("items", [])
        for j in range(3):
            it = items[j] if j < len(items) else {}
            # puce
            bullet_y = item_titles_y[j] + item_title_h / 2 - 0.15
            add_oval(slide, card_xs[i] + 0.5, bullet_y, 0.30, 0.30,
                     band_colors[i], name=f"S10_PHASE_{i+1}_ITEM_{j+1}_BULLET")
            # title
            add_textbox(slide, card_xs[i] + item_x_offset, item_titles_y[j], 9.08, item_title_h,
                        it.get("title", ""),
                        font="Segoe UI", size_pt=11, bold=True, color_hex="#070E1D",
                        anchor="m", name=f"S10_PHASE_{i+1}_ITEM_{j+1}_TITLE")
            # body
            add_textbox(slide, card_xs[i] + item_x_offset, item_bodies_y[j], 9.08, item_body_h,
                        it.get("body", ""),
                        font="Segoe UI Light", size_pt=10.5, color_hex="#474E67",
                        name=f"S10_PHASE_{i+1}_ITEM_{j+1}_BODY")
            # séparateur fin entre items
            if j < 2:
                add_line(slide, card_xs[i] + 0.40, separator_ys[j],
                         card_xs[i] + 10.10, separator_ys[j],
                         "#E8E9EE", width_pt=0.5)

    add_takeaway_band(slide, c.get("takeaway", "Take away"))


# ============================================================
# LAYOUT 11 — Arc narratif et CTA
# ============================================================
def build_slide_11(slide, c, page_num=11, total=11, logo_path=None):
    set_white_background(slide)
    add_master_chrome(slide, c.get("title", "Arc narratif"),
                       page_num=page_num, total=total, logo_path=logo_path)

    blocks = c.get("blocks", [])
    bar_ys = [3.05, 7.55, 12.05]
    # Filigranes positionnés un peu au-dessus du titre, pour effet "chiffre derrière le texte"
    number_ys = [2.50, 7.00, 11.50]
    title_ys = [3.30, 7.83, 12.30]
    body_ys = [4.50, 9.03, 13.50]
    bar_colors = ["#6A5D79", "#A25871", "#FDA85B"]
    title_colors = ["#6A5D79", "#A25871", "#FDA85B"]
    number_colors = ["#BBB4C4", "#D5B3BE", "#FEE3CA"]

    for i in range(3):
        b = blocks[i] if i < len(blocks) else {}
        # barre verticale colorée à gauche
        add_rect(slide, 1.09, bar_ys[i], 0.10, 4.20, bar_colors[i],
                 name=f"S11_BLOCK_{i+1}_ACCENT_BAR")
        # filigrane chiffre (sz 72pt, alpha 40%, 2.5cm de haut suffit)
        add_textbox(slide, 1.80, number_ys[i], 4.0, 2.20, f"0{i+1}",
                    font="Segoe UI Black", size_pt=72, bold=True,
                    color_hex=number_colors[i], alpha_pct=40,
                    anchor="t", name=f"S11_BLOCK_{i+1}_NUMBER")
        # titre coloré
        add_textbox(slide, 2.00, title_ys[i], 29.50, 1.10, b.get("block_title", ""),
                    font="Segoe UI", size_pt=18, bold=True,
                    color_hex=title_colors[i], name=f"S11_BLOCK_{i+1}_TITLE")
        # body
        add_textbox(slide, 2.00, body_ys[i], 29.50, 2.40, b.get("body", ""),
                    font="Segoe UI Light", size_pt=14, color_hex="#474E67",
                    name=f"S11_BLOCK_{i+1}_BODY", line_spacing=1.3,
                    emphasis_style={"font": "Segoe UI", "bold": True})

    # CTA en bas (gradient bandeau)
    add_takeaway_band(slide, c.get("cta", "Êtes-vous prêts ?"))


# ============================================================
# Dispatcher
# ============================================================
BUILDERS = {
    1: build_slide_1, 2: build_slide_2, 3: build_slide_3, 4: build_slide_4,
    5: build_slide_5, 6: build_slide_6, 7: build_slide_7, 8: build_slide_8,
    9: build_slide_9, 10: build_slide_10, 11: build_slide_11,
}


def build_slide(layout_n, slide, content, page_num=None, total=11, logo_path=None):
    """Dispatcher : appelle le bon builder selon layout_n (1..11)."""
    if layout_n not in BUILDERS:
        raise ValueError(f"Layout inconnu : {layout_n}. Doit être entre 1 et 11.")
    return BUILDERS[layout_n](slide, content, page_num=page_num or layout_n,
                              total=total, logo_path=logo_path)
