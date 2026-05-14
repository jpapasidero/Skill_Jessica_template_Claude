# Caractérisation des zones de la page "Garants de fabricabilité – 5 personnes"

Les coordonnées sont exprimées en **pourcentage de la largeur et de la hauteur de la page**.  
Référence :  
- **0 %** = bord gauche / haut  
- **100 %** = bord droit / bas  

---

## Zone 1 — Titre

**Description :**  
Titre principal de la page, juste sous la bande « C2 – Confidential ».

**Contenu :**  
- Avant le `-` ou le `_` : population
- Après le `-` ou le `_` : effectif

**Coordonnées relatives :**
- `x_min = 5`  
- `x_max = 60`  
- `y_min = 3`  
- `y_max = 12`

---

## Zone 2 — Radar (affiné : radar + labels + 4 bullets internes)

**Description :**  
Zone contenant le radar, ses 4 labels et les 4 bullets rouges internes,  
en excluant le bullet rouge externe à gauche et les encadrés textuels éloignés.

**Contenu :**  
- Polygone du radar  
- 4 axes  
- 4 bullets rouges internes  
- Labels proches : `Organization`, `Culture`, `Business`, `Tool`

**Coordonnées relatives de la zone :**
- `x_min = 15`  
- `x_max = 38`  
- `y_min = 24`  
- `y_max = 55`

**Repères internes (indicatifs) :**
- Centre du radar :  
  - `x_center ≈ 26`  
  - `y_center ≈ 38`
- Bullets internes :  
  - Haut : `x ≈ 26`, `y ≈ 27`  
  - Droite : `x ≈ 35`, `y ≈ 38`  
  - Bas : `x ≈ 26`, `y ≈ 49`  
  - Gauche interne : `x ≈ 17`, `y ≈ 38`

---

## Zone 3 — Tableau « Ressorts du changement / Actions »

**Description :**  
Tableau en bas à droite, section 3.

**Contenu :**  
- Colonne `Ressorts du changement`  
- Colonne `Actions`  
- Lignes : `Sens`, `Preuve`, `Accompagnement technique`, `Accompagnement de proximité`

**Coordonnées relatives :**
- `x_min = 55`  
- `x_max = 95`  
- `y_min = 60`  
- `y_max = 95`
