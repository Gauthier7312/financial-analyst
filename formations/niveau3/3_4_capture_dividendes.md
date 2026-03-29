# Module 3.4 — Capture de Dividendes BRVM 2026

> **Durée estimée :** 45 min | **Niveau :** Avancé | **Statut :** `python tracker.py start 3.4`

---

## Le calendrier dividendes 2026 — Données live BRVM

| Valeur | Ticker | Dividende | Yield | Détachement | Acheter avant | RSI actuel |
|---|---|---|---|---|---|---|
| BOA BF | BOABF.bf | 397 FCFA | 7.21% | 21/04/2026 | **15/04/2026** | 75.44 🔴 |
| BOA SN | BOAS.sn | 450 FCFA | 6.83% | 28/05/2026 | **20/05/2026** | À vérifier |
| SONATEL | SNTS.sn | 1 740 FCFA | 6.13% | 22/05/2026 | **15/05/2026** | 49.55 🟢 |
| BOA ML | BOAM.ml | 305 FCFA | 6.50% | 01/06/2026 | **24/05/2026** | À vérifier |
| SAPH CI | CAPH.ci | 430 FCFA | 5.91% | TBD | TBD | À vérifier |
| PALMCI | PALC.ci | 441 FCFA | 5.39% | TBD | TBD | À vérifier |
| ORANGE CI | ORAC.ci | 704 FCFA | 4.60% | TBD | TBD | 56.24 🟡 |

---

## Mécanique de la capture de dividende

### Ce qui se passe autour de la date de détachement

```
J-5  : Tu achètes les actions (avant la date limite)
J=0  : Date de détachement — le dividende est "détaché" du cours
       → Le cours baisse mécaniquement du montant du dividende

J+10 à J+30 : CREPMF enregistre, ta SGI verse le dividende sur ton compte
```

### Exemple SONATEL 2026

```
Avant détachement (21/05) : cours ~28 400 FCFA
Après détachement (22/05) : cours théorique ~26 660 FCFA (baisse de 1 740)

Ton dividende reçu = 1 740 FCFA/action
Ta moins-value latente = -1 740 FCFA/action
Bilan brut = 0 FCFA (avant frais)
```

**Alors pourquoi faire cette stratégie ?**

Parce que dans la pratique, le cours ne baisse pas exactement du montant
du dividende — et sur des valeurs haussières, le cours peut récupérer rapidement.

---

## Les 3 scénarios post-détachement

### Scénario 1 — Valeur haussière (meilleur cas)
```
Cours avant : 28 400 | Dividende : 1 740 | Cours après détachement : 27 500
(baisse de seulement 900 au lieu de 1 740)

Gain total = Dividende - Perte de cours = 1 740 - 900 = +840 FCFA/action ✅
```

### Scénario 2 — Marché neutre
```
Cours avant : 28 400 | Cours après : 26 700
Perte de cours ≈ dividende → Bilan ≈ 0 (juste les frais à payer)
```

### Scénario 3 — Valeur en baisse (pire cas)
```
Cours avant : 28 400 | Cours après : 25 800
Perte de cours > dividende → Bilan négatif ❌
```

**Conclusion :** La capture de dividende fonctionne vraiment bien sur des valeurs
avec une tendance haussière de fond. Ne pas faire cette stratégie sur une valeur
dont le RSI est suracheté (comme BOA BF à 75.44 actuellement).

---

## Analyse décision : Que faire avec BOA BF aujourd'hui ?

```
Dividende : 397 FCFA (7.21%)
Cours actuel : 5 510 FCFA
RSI : 75.44 (suracheté 🔴)
YTD : +46.93% (!)
Date limite achat pour dividende : 15/04/2026 (dans ~18 jours)

Scénario A — J'achète maintenant pour le dividende
  + Je touche 397 FCFA de dividende
  - J'achète au RSI 75 = risque de correction de -10 à -15%
  - Perte potentielle : -5 510 × 12% = -661 FCFA/action
  Bilan : 397 - 661 = -264 FCFA/action → Négatif 🔴

Scénario B — J'attends une correction
  Si cours revient à 5 000 FCFA (RSI ~50) avant le 15/04 → ACHAT
  Dividende 397 FCFA = 7.94% de rendement au nouveau cours
  Bilan potentiel : positif si tendance se maintient ✅

Scénario C — Je passe
  Trop risqué sans correction. Je surveille SONATEL à la place.
```

**Recommandation pour profil débutant : Scénario C (passer sur BOA BF) + Scénario SONATEL.**

---

## Plan d'action dividendes Avril-Mai 2026

```
Priorité 1 (MAINTENANT) — SONATEL
  → Acheter avant le 15/05
  → RSI 49.55 ✅ | Fondamentaux excellents (9/10)
  → Dividende : 1 740 FCFA/action (6.13%)

Priorité 2 (SURVEILLER) — BOA BF
  → Attendre RSI < 60 avant d'agir
  → Si cours revient à 4 900–5 100, reconsidérer

Priorité 3 (PLUS TARD) — BOA SN
  → Date limite : 20/05
  → Vérifier RSI et cours dans 3–4 semaines
```

---

## Exercice pratique

Simule une stratégie de capture de dividende sur SONATEL :

1. Prix d'achat simulé : 28 400 FCFA (7 actions = ~200 000 FCFA)
2. Dividende attendu : 1 740 FCFA × 7 = 12 180 FCFA
3. Définis un scénario optimiste et un scénario pessimiste post-détachement
4. Calcule ton rendement net (dividende - frais de courtage)

```bash
python tracker.py note 3.4 "Plan dividende SONATEL: 7 actions × 28400 = 198800 FCFA + frais. Dividende attendu: 12180 FCFA. Achat avant 15/05."
```

---

## Quiz de vérification

1. Qu'est-ce qu'un "détachement de dividende" ? Que se passe-t-il sur le cours ?
2. Calcule le rendement net d'une capture dividende SONATEL : achat à 28 400, dividende 1 740, cours après 27 200.
3. Pourquoi déconseille-t-on la capture dividende sur BOA BF aujourd'hui (RSI 75.44) ?
4. Quelle est la règle de timing minimum pour la capture de dividende ?
5. Dans quelles conditions la capture de dividende est-elle vraiment profitable ?

```bash
python tracker.py quiz 3.4 <ton_score>
python tracker.py done 3.4
python tracker.py start 3.5
```
