# Catalogue des 15 layouts — Palette Jessica

| # | Nom | Quand l'utiliser | Champs clés |
|---|---|---|---|
| 1 | **Hook sens + factuel** | Slide d'ouverture forte. Manifeste + 3 KPI signature. | `manifesto`, `body`, `stats[3]`, `takeaway` |
| 2 | **Hook sens + vision** | Présenter 3 piliers / 3 partis-pris en parallèle. Pas de hiérarchie entre les 3. | `columns[3]` (title small caps + body) |
| 3 | **Liste 6 points** | Énumérer 6 facteurs / leviers / éléments d'égale importance. | `factors[6]` (label small caps), `takeaway` |
| 4 | **Triptyque** | 3 dimensions interdépendantes (people-process-tech, sens-impact-coût, etc.). Visuel cercles connectés. | `nodes.{top,left,right}`, `takeaway` |
| 5 | **Timeline** | Roadmap 4 étapes temporelles. Chaque étape = période + titre + body. | `steps[4]` (period small caps), pas de takeaway |
| 6 | **Tableau** | Comparatif structuré multi-critères. 5 colonnes x 4 lignes (entête + 4 données). | `headers[5]`, `rows[4][5]`, `takeaway` |
| 7 | **Dashboard** | Vue d'ensemble : 6 KPI + 5 indicateurs barres horizontales. | `kpis[6]`, `bars[5]`, `section_label`, `takeaway` |
| 8 | **Comparatif** | Comparaison 2 séries sur 5 lignes (avant/après, scénario A/B...). | `subtitle`, `legends[2]`, `rows[5]`, `takeaway` |
| 9 | **Risques & Opportunités** | Bilan typique d'un projet : 3 risques (haut) + 3 opportunités (bas). | `risks[3]`, `opportunities[3]`, level codifié |
| 10 | **Plan d'action 3 phases** | Roadmap détaillée : 3 phases x 3 items chacune. Bandeaux colorés. | `phases[3]`, chaque phase `items[3]`, `takeaway` |
| 11 | **Arc narratif / CTA** | Slide de clôture. 3 blocs narratifs empilés (appris-proposé-attendu) + CTA. | `blocks[3]`, `cta` |
| 12 | **Process vertical** | Décrire une méthode ou un protocole en 6 étapes lisibles. | `steps[6]` avec `label`, `sublabel` |
| 13 | **Opposition qualitative** | Contraster bonnes pratiques et pièges à éviter. | `left_title`, `right_title`, `left_items[5]`, `right_items[5]` |
| 14 | **Comparatif qualitatif** | Comparer deux approches, méthodes ou scénarios sans tableau chiffré. | `left_title`, `right_title`, `left_items[5]`, `right_items[5]`, `takeaway` |
| 15 | **Impact par population** | Cartographier l'intensité d'impact par groupe et levier d'accompagnement. | `headers[5]`, `rows[6]`, `impacts[4]`, `levers` |

## Storylines recommandées

### Storyline "Convaincre un comité de décision" (8 slides)
1. Layout 1 — Hook factuel (chiffres qui font mal du statu quo)
2. Layout 2 — Vision en 3 piliers
3. Layout 4 — Triptyque (les 3 dimensions à articuler)
4. Layout 5 — Timeline (la trajectoire)
5. Layout 7 — Dashboard (les KPI à suivre)
6. Layout 9 — Risques & Opportunités
7. Layout 10 — Plan d'action 3 phases
8. Layout 11 — Arc narratif + CTA "validez-vous la phase 1 ?"

### Storyline "Retour d'expérience post-pilote" (6 slides)
1. Layout 1 — Hook factuel (3 chiffres résultats du pilote)
2. Layout 5 — Timeline (ce qu'on a fait)
3. Layout 8 — Comparatif avant/après
4. Layout 3 — 6 facteurs de succès identifiés
5. Layout 9 — Risques & Opportunités pour le scale-up
6. Layout 11 — CTA "généralisons-nous ?"

### Storyline "Présentation projet à un sponsor" (5 slides)
1. Layout 1 — Hook
2. Layout 6 — Tableau scénarios (A/B/C/D + recommandation)
3. Layout 7 — Dashboard cible
4. Layout 10 — Plan d'action 3 phases
5. Layout 11 — CTA

### Storyline "Conduite du changement opérationnelle" (7 slides)
1. Layout 1 — Hook factuel sur l'urgence du changement
2. Layout 15 — Impact par population pour objectiver l'effort
3. Layout 13 — Bonnes pratiques / pièges à éviter
4. Layout 12 — Process de déploiement en 6 étapes
5. Layout 14 — Comparatif qualitatif des approches possibles
6. Layout 9 — Risques & Opportunités
7. Layout 11 — Décision et engagement sponsor

## Mapping DISC x layout

| Profil dominant audience | Layouts à privilégier | Layouts à éviter |
|---|---|---|
| **D** (Dominant) | 1, 6, 8, 11, 13 (chiffres, choix tranchés, CTA direct) | 3, 4 (trop conceptuels) |
| **I** (Influent) | 2, 4, 11, 13 (vision, narration, émotion, contrastes simples) | 6, 8 (trop arides) |
| **S** (Stable) | 5, 10, 12 (étapes claires, prévisibilité) | 11 sans CTA progressif |
| **C** (Consciencieux) | 6, 7, 8, 9, 14, 15 (data, structure, risques) | 4 (manque de précision) |

Pour un comité mixte : ouvrir en mode I (slide 1 manifeste émotionnel + chiffres D), corps en mode C (data slides 6-8 ou 15), conclure en mode D (slide 11 CTA).
