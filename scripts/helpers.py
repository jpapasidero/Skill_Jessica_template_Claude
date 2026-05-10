"""
Helpers bas-niveau pour le template Palette Jessica.
Manipule directement le XML OOXML pour les effets non gérés nativement par python-pptx :
- cap="small" (petites majuscules)
- alpha (filigrane translucide)
- gradient vertical 3-stops sur le bandeau Take-away
"""
from pptx.util import Cm, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
from lxml import etree


# ---------- Conversions ----------

def cm(v):
    return Cm(v)


def hex_to_rgb(hexstr):
    h = hexstr.lstrip("#")
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


# ---------- Texte ----------

def set_run_props(run, *, font=None, size_pt=None, bold=None, italic=None, color_hex=None,
                  cap=None, alpha_pct=None):
    """Applique les propriétés à un run et patche le XML pour cap / alpha si demandé."""
    if font:
        run.font.name = font
    if size_pt is not None:
        run.font.size = Pt(size_pt)
    if bold is not None:
        run.font.bold = bold
    if italic is not None:
        run.font.italic = italic
    if color_hex:
        run.font.color.rgb = hex_to_rgb(color_hex)

    rPr = run._r.get_or_add_rPr()

    # cap="small" : petites majuscules avec 1ère lettre majuscule (rendu OOXML natif)
    if cap == "small":
        rPr.set("cap", "small")
    elif cap == "all":
        rPr.set("cap", "all")

    # alpha : injecter <a:alpha val="N"/> dans <a:solidFill><a:srgbClr>
    if alpha_pct is not None and color_hex:
        # on retire le solidFill existant pour le reconstruire avec alpha
        for sf in rPr.findall(qn("a:solidFill")):
            rPr.remove(sf)
        sf = etree.SubElement(rPr, qn("a:solidFill"))
        srgb = etree.SubElement(sf, qn("a:srgbClr"))
        srgb.set("val", color_hex.lstrip("#").upper())
        alpha = etree.SubElement(srgb, qn("a:alpha"))
        alpha.set("val", str(int(alpha_pct * 1000)))  # 40% -> 40000


def add_textbox(slide, x_cm, y_cm, w_cm, h_cm, text, *, font="Segoe UI", size_pt=12,
                bold=False, italic=False, color_hex="#070E1D", cap=None, alpha_pct=None,
                align="left", anchor="t", name=None):
    """Crée un textbox avec un run unique aux propriétés spécifiées."""
    tb = slide.shapes.add_textbox(cm(x_cm), cm(y_cm), cm(w_cm), cm(h_cm))
    if name:
        tb.name = name
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Emu(45720)
    tf.margin_right = Emu(45720)
    tf.margin_top = Emu(45720)
    tf.margin_bottom = Emu(45720)

    # ancrage vertical
    from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
    anchor_map = {"t": MSO_ANCHOR.TOP, "m": MSO_ANCHOR.MIDDLE, "b": MSO_ANCHOR.BOTTOM}
    tf.vertical_anchor = anchor_map.get(anchor, MSO_ANCHOR.TOP)

    p = tf.paragraphs[0]
    align_map = {"left": PP_ALIGN.LEFT, "center": PP_ALIGN.CENTER, "right": PP_ALIGN.RIGHT}
    p.alignment = align_map.get(align, PP_ALIGN.LEFT)

    run = p.add_run()
    run.text = text
    set_run_props(run, font=font, size_pt=size_pt, bold=bold, italic=italic,
                  color_hex=color_hex, cap=cap, alpha_pct=alpha_pct)
    return tb


# ---------- Formes ----------

def add_rect(slide, x_cm, y_cm, w_cm, h_cm, fill_hex, *, line_hex=None, line_w_pt=0,
             rounded=False, name=None):
    shape_type = MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE
    shp = slide.shapes.add_shape(shape_type, cm(x_cm), cm(y_cm), cm(w_cm), cm(h_cm))
    if name:
        shp.name = name
    if rounded:
        # arrondi modéré
        shp.adjustments[0] = 0.1
    shp.fill.solid()
    shp.fill.fore_color.rgb = hex_to_rgb(fill_hex)
    if line_hex:
        shp.line.color.rgb = hex_to_rgb(line_hex)
        shp.line.width = Pt(line_w_pt) if line_w_pt else Pt(0.25)
    else:
        shp.line.fill.background()
    return shp


def add_oval(slide, x_cm, y_cm, w_cm, h_cm, fill_hex, *, line_hex=None, name=None):
    shp = slide.shapes.add_shape(MSO_SHAPE.OVAL, cm(x_cm), cm(y_cm), cm(w_cm), cm(h_cm))
    if name:
        shp.name = name
    shp.fill.solid()
    shp.fill.fore_color.rgb = hex_to_rgb(fill_hex)
    if line_hex:
        shp.line.color.rgb = hex_to_rgb(line_hex)
    else:
        shp.line.fill.background()
    return shp


def add_teardrop(slide, x_cm, y_cm, w_cm, h_cm, fill_hex, *, name=None):
    """Larme (teardrop). En python-pptx : MSO_SHAPE.TEAR (rotation à appliquer pour pointe en haut)."""
    shp = slide.shapes.add_shape(MSO_SHAPE.TEAR, cm(x_cm), cm(y_cm), cm(w_cm), cm(h_cm))
    if name:
        shp.name = name
    # rotation pour pointe vers le bas (esthétique larme du template)
    shp.rotation = 180
    shp.fill.solid()
    shp.fill.fore_color.rgb = hex_to_rgb(fill_hex)
    shp.line.fill.background()
    return shp


def add_line(slide, x1_cm, y1_cm, x2_cm, y2_cm, color_hex, *, width_pt=1.0, dash=False):
    from pptx.enum.shapes import MSO_CONNECTOR
    conn = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, cm(x1_cm), cm(y1_cm),
                                       cm(x2_cm), cm(y2_cm))
    conn.line.color.rgb = hex_to_rgb(color_hex)
    conn.line.width = Pt(width_pt)
    if dash:
        # injection dash dans XML
        ln = conn.line._get_or_add_ln()
        prstDash = etree.SubElement(ln, qn("a:prstDash"))
        prstDash.set("val", "dash")
    return conn


# ---------- Bandeau Take-away avec gradient vertical 3-stops ----------

def add_takeaway_band(slide, text="Take away"):
    """Bandeau bordeaux avec gradient vertical 3-stops + texte centré blanc."""
    POS_X, POS_Y, W, H = 1.09, 16.87, 31.70, 1.10
    BASE = "A25871"

    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, cm(POS_X), cm(POS_Y), cm(W), cm(H))
    shp.name = "TakeawayBand"

    # spPr est directement le CT_ShapeProperties accessible sur shp._element.spPr
    sppr = shp._element.spPr
    # nettoyer fill/line existants pour garder l'ordre OOXML valide :
    # géométrie -> fill -> line. Sinon PowerPoint peut ignorer le gradient
    # et retomber sur la couleur accent du thème.
    for tag in ["a:solidFill", "a:gradFill", "a:noFill", "a:blipFill", "a:pattFill", "a:ln"]:
        for el in sppr.findall(qn(tag)):
            sppr.remove(el)

    gradFill = etree.SubElement(sppr, qn("a:gradFill"))
    gradFill.set("flip", "none")
    gradFill.set("rotWithShape", "1")
    gsLst = etree.SubElement(gradFill, qn("a:gsLst"))

    # 3 stops : 0% (haut, plus clair), 50%, 100% (bas, plus sombre)
    stops = [(0, 30000), (50000, 67500), (100000, 100000)]
    for pos, shade in stops:
        gs = etree.SubElement(gsLst, qn("a:gs"))
        gs.set("pos", str(pos))
        srgb = etree.SubElement(gs, qn("a:srgbClr"))
        srgb.set("val", BASE)
        sm = etree.SubElement(srgb, qn("a:satMod"))
        sm.set("val", "115000")
        sh = etree.SubElement(srgb, qn("a:shade"))
        sh.set("val", str(shade))

    # angle vertical (5400000 = 90°)
    lin = etree.SubElement(gradFill, qn("a:lin"))
    lin.set("ang", "5400000")
    lin.set("scaled", "1")

    ln = etree.SubElement(sppr, qn("a:ln"))
    etree.SubElement(ln, qn("a:noFill"))

    # Texte centré
    add_textbox(slide, POS_X, POS_Y, W, H, text,
                font="Segoe UI", size_pt=16, bold=True, color_hex="#FFFFFF",
                align="center", anchor="m", name="TakeawayBandText")
    return shp


# ---------- Master commun (titre, signature bar, footer, logo, page num) ----------

def add_master_chrome(slide, title_text, *, page_num=None, total=None, with_signature=True,
                       logo_path=None):
    """Ajoute le 'chrome' commun à toutes les slides : titre, barre signature, footer, logo, n° page."""
    # Titre
    add_textbox(slide, 1.09, 0.71, 31.70, 1.58, title_text,
                font="Segoe UI Black", size_pt=29.32, color_hex="#484C6A",
                align="left", anchor="m", name="SLIDE_TITLE")

    # Barre signature double
    if with_signature:
        # rectangle bleu nuit
        add_rect(slide, 1.09, 2.46, 1.87, 0.27, "#484C6A", name="SignatureRect")
        # trait long fin (simulé par un rectangle très plat)
        add_rect(slide, 1.09, 2.71, 3.69, 0.025, "#112753", name="SignatureLine")

    # Footer confidentiel
    footer_text = ("This document and the information therein are the property of Safran. "
                   "They must not be copied or communicated to a third party without the "
                   "prior written authorization of Safran")
    add_textbox(slide, 1.06, 18.51, 26.32, 0.40, footer_text,
                font="Segoe UI", size_pt=6.5, color_hex="#A8A8B5",
                align="left", anchor="t", name="FooterConfidential")

    # Numéro de page
    if page_num is not None:
        page_str = f"{page_num:02d}" if total is None else f"{page_num:02d}/{total:02d}"
        add_textbox(slide, 1.04, 18.03, 1.50, 0.46, page_str,
                    font="Segoe UI", size_pt=9, bold=True, color_hex="#7D7B8D",
                    align="left", anchor="m", name="PageNumber")

    # Logo Safran (si fourni)
    if logo_path:
        try:
            slide.shapes.add_picture(logo_path, cm(29.77), cm(17.91),
                                     width=cm(3.03), height=cm(0.64))
        except Exception:
            pass


# ---------- Fond blanc explicite ----------

def set_white_background(slide):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = hex_to_rgb("#FFFFFF")
