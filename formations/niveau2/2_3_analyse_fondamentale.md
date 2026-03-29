# Module 2.3 — Analyse Fondamentale : PER, Dividendes, ROE

> **Durée estimée :** 1h15 | **Niveau :** Intermédiaire | **Statut :** `python tracker.py start 2.3`

---

## L'analyse fondamentale en une phrase

> "Acheter une action, c'est acheter une part d'une entreprise réelle.
> L'analyse fondamentale vérifie que cette entreprise vaut le prix qu'on paie."

---

## Le PER — Price Earnings Ratio

### Formule
```
PER = Prix de l'action / Bénéfice par action (BPA)
```

### Interprétation
```
PER < 8    → Très bon marché 🟢 (soldes !)
PER 8–12   → Juste valorisation pour la BRVM
PER 12–20  → Cher mais possible si forte croissance
PER > 20   → Très cher — prudence 🔴
```

### Exemple SONATEL
```
Cours : 28 400 FCFA
Bénéfice 2025 : 413 milliards FCFA
Nombre d'actions : ~100 millions
BPA = 413 000 000 000 / 100 000 000 = 4 130 FCFA/action
PER = 28 400 / 4 130 = 6.9x

→ SONATEL se paye 6.9 fois ses bénéfices annuels.
→ C'est bon marché. La moyenne mondiale est 15–20x.
```

---

## Le Dividende et le Rendement

### Rendement dividende
```
Rendement = Dividende par action / Prix de l'action × 100
```

### Calendrier dividendes BRVM 2026

| Valeur | Dividende | Rendement | Détachement | Acheter avant |
|---|---|---|---|---|
| BOA BF | 397 FCFA | 7.21% | 21/04/2026 | 15/04/2026 |
| SONATEL | 1 740 FCFA | 6.13% | 22/05/2026 | 15/05/2026 |
| BOA SN | 450 FCFA | 6.83% | 28/05/2026 | 20/05/2026 |
| PALMCI | 441 FCFA | 5.39% | TBD | TBD |
| SAPH CI | 430 FCFA | 5.91% | TBD | TBD |
| ORANGE CI | 704 FCFA | 4.60% | TBD | TBD |

### Le payout ratio — Le dividende est-il soutenable ?
```
Payout ratio = Dividende total / Bénéfice net

< 60% → Dividende soutenable et marge pour le réinvestir ✅
60–80% → Acceptable
> 85% → L'entreprise distribue presque tout — peu de marge 🔴
> 100% → Distribue plus qu'elle ne gagne — insoutenable 🚨
```

---

## Le ROE — Return on Equity

Le ROE mesure l'efficacité de l'entreprise à générer des profits avec l'argent
des actionnaires.

```
ROE = Bénéfice net / Capitaux propres × 100
```

| ROE | Interprétation |
|---|---|
| > 15% | Excellente rentabilité 🟢 |
| 10–15% | Bonne |
| 5–10% | Correcte |
| < 5% | Faible — l'entreprise peine à rentabiliser |

---

## Le Bilan — Solidité financière

### Ratio Dette/Fonds propres (D/E)
```
D/E < 1   → Bilan sain ✅
D/E 1–2   → Acceptable
D/E > 2   → Entreprise trop endettée 🔴
```

*Exception : Les banques ont un D/E naturellement élevé — utiliser
le ratio Tier 1 Capital à la place (> 10% = solide).*

---

## La Capitalisation boursière

```
Capitalisation = Prix × Nombre d'actions en circulation
```

| Taille | Capitalisation BRVM | Exemple | Profil |
|---|---|---|---|
| Grande cap | > 500 Mds FCFA | SONATEL (2 840 Mds) | Sûr, liquide |
| Moyenne cap | 100–500 Mds | BOA CI (348 Mds) | Équilibré |
| Petite cap | < 100 Mds | Petites valeurs | Risqué, peu liquide |

**Pour un débutant :** Rester sur les grandes et moyennes capitalisations.

---

## Le Score Fondamental /5 (du skill BRVM)

| Critère | Condition | Points |
|---|---|---|
| Dividende | Yield > 5% | +1 |
| Croissance | Bénéfices croissants 3 ans | +1 |
| Taille | Cap > 200 Mds FCFA | +1 |
| Backing | Groupe international | +1 |
| Valorisation | PER < 15x | +1 |

**Application SONATEL :** 5/5 → Fondamentaux excellents.

---

## Exercice pratique

Analyse BOA CI (BOAC.ci) avec les données disponibles sur sikafinance :
1. Note la capitalisation — grande, moyenne ou petite cap ?
2. Le groupe BOA est-il international ?
3. Comment estimer le PER si tu as le cours et une estimation du bénéfice ?
4. Donne ton score fondamental /5 pour BOA CI.

```bash
python tracker.py note 2.3 "BOA CI fondamentaux: Cap=[X] Mds, Backing=[oui/non], PER estimé=[X], Score=[Y/5]"
```

---

## Quiz de vérification

1. Calcule le rendement dividende de SONATEL (dividende 1 740 FCFA, cours 28 400 FCFA).
2. Un PER de 22x pour une valeur BRVM, qu'est-ce que ça signifie ?
3. Qu'est-ce que le payout ratio et pourquoi est-il important ?
4. Pourquoi les grandes capitalisations sont-elles recommandées pour les débutants ?
5. Une entreprise avec ROE de 4% et D/E de 3.5 — est-ce un bon investissement ? Justifie.

```bash
python tracker.py quiz 2.3 <ton_score>
```
