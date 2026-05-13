"""
Exploration approfondie des drawings OMOC dans le PDF.
On cherche les 4 bullets OMOC : rectangles colorés dans la zone gauche de la page.
"""
import fitz
import re

RESSORT_KEYWORDS = {'sens', 'preuve', 'accompagnement'}
ACTION_KEYWORDS = {'communication', 'support', 'mobilisation', 'formation'}

def is_title_block(x0, y0, x1, y1, text, page_h=540):
    """Bloc titre : en haut de page, texte non vide, pas trop petit."""
    return y0 < 70 and y1 < 75 and len(text.strip()) > 5

def is_omoc_bullet(d, page_h=540):
    """
    Bullet OMOC = rectangle dans la zone gauche (x < 350),
    couleur bleue (0.23, 0.53, 0.80), taille ~11-27 pts.
    """
    fill = d.get("fill")
    rect = d.get("rect")
    if fill is None or rect is None:
        return False
    r, g, b = fill[0], fill[1], fill[2]
    # Bleu Safran OMOC : (0.231, 0.529, 0.800)
    is_blue = (0.20 < r < 0.25) and (0.50 < g < 0.56) and (0.77 < b < 0.83)
    # Dans zone gauche (radar)
    in_left = rect.x0 < 350 and rect.x1 < 360
    # Taille raisonnable (bullet) : w et h entre 5 et 100 pts
    w = rect.x1 - rect.x0
    h = rect.y1 - rect.y0
    is_rect_sized = 5 < w < 120 and 5 < h < 120
    return is_blue and in_left and is_rect_sized

pdf = fitz.open("Exemple_analyse_impact.pdf")

for page_num in range(min(3, len(pdf))):
    page = pdf[page_num]
    print(f"\n{'='*70}")
    print(f"PAGE {page_num + 1}")

    # Title
    blocks = page.get_text("blocks")
    title = ""
    for b in blocks:
        x0, y0, x1, y1, text = b[0], b[1], b[2], b[3], b[4].strip()
        if is_title_block(x0, y0, x1, y1, text):
            title = text.replace('\n', ' ')
            print(f"  TITLE: {title!r}")

    # OMOC bullets
    drawings = page.get_drawings()
    bullets = []
    for d in drawings:
        if is_omoc_bullet(d):
            r = d["rect"]
            cx = (r.x0 + r.x1) / 2
            cy = (r.y0 + r.y1) / 2
            bullets.append((cx, cy, r))
            print(f"  BULLET OMOC: cx={cx:.1f} cy={cy:.1f} rect={r}")

    # RESSORTS_CHANGE — blocs avec keywords
    print("  RESSORTS:")
    for b in blocks:
        text = b[4].strip().replace('\n', ' ')
        first_word = text.split()[0].lower() if text.split() else ''
        if first_word in RESSORT_KEYWORDS or 'accompagnement' in text.lower()[:20]:
            print(f"    [{b[1]:.0f}] {text[:150]!r}")

pdf.close()
