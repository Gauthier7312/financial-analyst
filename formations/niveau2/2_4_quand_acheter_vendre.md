# Module 2.4 — Quand acheter et quand vendre ?

> **Durée estimée :** 1h | **Niveau :** Intermédiaire | **Statut :** `python tracker.py start 2.4`

---

## La question à 1 million de FCFA

Il n'existe pas de signal parfait. Mais en combinant analyse technique
+ fondamentale + timing de marché, on peut identifier des **zones d'achat
à probabilité élevée**.

---

## Le Score Global /10 — La règle de décision

Applique ce scoring avant tout achat (du skill BRVM Trader) :

### Score Technique /5
| Condition | Points |
|---|---|
| RSI entre 30 et 60 | +1 |
| Beta < 0.9 | +1 |
| Momentum 1 mois positif | +1 |
| Volume > moyenne récente | +1 |
| YTD positif | +1 |

### Score Fondamental /5
| Condition | Points |
|---|---|
| Rendement dividende > 5% | +1 |
| Bénéfices croissants 3 ans | +1 |
| Capitalisation > 200 Mds | +1 |
| Groupe international | +1 |
| PER < 15x | +1 |

### Décision
```
≥ 8/10 → ACHAT FORT 🟢
6–7/10 → ACHAT PARTIEL (DCA) 🟡
≤ 5/10 → PASSER 🔴
```

---

## Les 5 situations qui crient "ACHAT"

### 1. RSI sous 35 + Support solide
L'action est survendue et rebondit sur un niveau historique.
```
Exemple : TOTAL CI à 2 100 FCFA (plus bas 52 sem) avec RSI à 28
→ Signal d'achat fort — le marché a trop vendu
```

### 2. Avant un détachement de dividende (>5% de yield)
Acheter au moins 5 jours ouvrables avant la date de détachement.
```
Exemple : Acheter BOA BF avant le 15/04 pour toucher 397 FCFA/action
→ Stratégie "Capture de dividende"
```

### 3. Correction sur une tendance haussière longue
Le cours corrige de -10 à -20% dans une tendance haussière.
```
SONATEL perd -3% sur 1 mois mais +13% sur 1 an
→ Correction normale = fenêtre d'achat
```

### 4. Golden Cross (MM20 croise MM50 à la hausse)
Signal technique fort de reprise de tendance.

### 5. Publication de bons résultats + cours encore bas
Les résultats annuels sont publiés (Jan–Avr sur la BRVM).
Si les bénéfices dépassent les attentes mais le cours n'a pas encore réagi.

---

## Les 5 situations qui crient "VENDRE"

### 1. Atteinte de l'objectif de cours
Tu as fixé +15% à l'entrée. L'action a fait +15%. Tu prends tes profits.
Discipline absolue — ne pas être trop gourmand.

### 2. RSI > 72 + Résistance clé
L'action est suracheté et bute sur un plafond historique.
```
BOA BF : RSI 75.44 + cours au plus haut 52 sem → Ne pas acheter / Alléger
```

### 3. Le stop-loss est touché
Tu as défini -15%. Le cours atteint ce niveau. Tu vends. Sans hésiter.
C'est la règle la plus importante — elle protège ton capital.

### 4. Les fondamentaux se dégradent
Profit warning émis (comme BOA Niger le 16/03/2026).
Dividende coupé ou suspendu.
Changement de dirigeant suspect.

### 5. Tu as besoin de l'argent
Investir en bourse c'est pour de l'argent dont tu n'as PAS besoin dans les 2–3 ans.
Si tu as besoin de l'argent, vendre n'est pas une honte.

---

## La stratégie DCA — L'ami du débutant

DCA = Dollar Cost Averaging = investir en plusieurs tranches.

```
Capital disponible : 300 000 FCFA sur SONATEL

Au lieu de tout investir d'un coup :
  Tranche 1 (maintenant) : 150 000 FCFA à 28 400 FCFA
  Tranche 2 (J+30)       : 100 000 FCFA à 27 500 FCFA (si baisse)
  Tranche 3 (J+60)       : 50 000 FCFA  à 28 000 FCFA

Prix moyen = (150K×28400 + 100K×27500 + 50K×28000) / 300K = 28 083 FCFA
```

**Avantage :** Tu lisses ton prix d'entrée. Tu profites des baisses intermédiaires.
**Inconvénient :** Si le cours monte fort dès le départ, tu aurais gagné à tout mettre d'un coup.

---

## Timing spécifique à la BRVM

### Saisonnalité des dividendes (Jan–Juin)
La BRVM monte souvent en début d'année, anticipant les dividendes.
Meilleure période pour les stratégies de capture de dividende : **Janvier–Avril**.

### Publications de résultats
La plupart des sociétés BRVM publient leurs résultats annuels entre **Février et Avril**.
C'est une période de volatilité et d'opportunités.

### Fin d'année
Décembre = dégagement fiscal de certains fonds. Peut créer des baisses temporaires
→ opportunités d'achat sur des valeurs solides.

---

## Exercice pratique

Applique le Score /10 à ORANGE CI avec les données du 28/03/2026 :

**Données :**
- RSI 56.24 | Beta 1.08 | Momentum 1 mois : -1.64% | YTD : +7.37%
- Yield dividende : 4.60% | Backing Orange France : oui | Cap : 2 305 Mds

Score technique : ?/5
Score fondamental : ?/5
Total : ?/10 → Décision : ?

```bash
python tracker.py note 2.4 "ORANGE CI score: technique=[X/5] fondamental=[Y/5] total=[Z/10] décision=[ACHAT/ATTENDRE/PASSER]"
```

---

## Quiz de vérification

1. Tu achètes une action à 5 000 FCFA avec un stop à -12%. À quel prix vends-tu en stop-loss ?
2. Explique pourquoi le DCA réduit le risque par rapport à un achat unique.
3. Un Golden Cross vient d'apparaître sur TOTAL CI. Que vérifies-tu avant d'acheter ?
4. Que fais-tu si une société émet un profit warning sur une action que tu détiens ?
5. Quel est le meilleur moment de l'année pour acheter des valeurs à dividende sur la BRVM ?

```bash
python tracker.py quiz 2.4 <ton_score>
python tracker.py done 2.4
python tracker.py start 2.5
```
