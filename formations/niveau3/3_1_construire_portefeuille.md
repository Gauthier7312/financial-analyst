# Module 3.1 — Construire son portefeuille BRVM

> **Durée estimée :** 1h | **Niveau :** Avancé | **Statut :** `python tracker.py start 3.1`

---

## Les principes de base d'un portefeuille

Un **portefeuille** est l'ensemble de tes positions en bourse.
L'objectif est de combiner des valeurs qui :
- Maximisent le rendement attendu
- Minimisent le risque global par la **diversification**

---

## La Pyramide du capital BRVM

| Capital | Nb de valeurs recommandé | Raison |
|---|---|---|
| < 200 000 FCFA | 1 blue chip | Frais trop élevés si on divise plus |
| 200–500 000 FCFA | 2–3 valeurs | Diversification minimale |
| 500 000 – 1M FCFA | 3–4 valeurs | Bon équilibre |
| > 1M FCFA | 4–6 valeurs | Diversification complète |

**Règle :** Mieux vaut 2 valeurs bien choisies que 8 valeurs mal comprises.

---

## Règles de concentration

```
Une seule valeur    : max 40% du portefeuille
Un seul secteur     : max 60% du portefeuille
Liquidités réservées: min 10–15% (pour saisir les opportunités)
```

### Pourquoi ces règles ?
Si tu mets 80% sur une seule valeur et qu'elle perd -30%, ton portefeuille
perd -24%. Inacceptable pour un débutant.

---

## Les 4 types de valeurs à combiner

### 1. Valeurs défensives (socle du portefeuille, 50–60%)
- Beta < 0.8 | Dividende régulier | Grande capitalisation
- Exemples BRVM : SONATEL, TOTAL CI, PALMCI, SAPH

### 2. Valeurs de croissance (15–25%)
- Croissance du CA et bénéfices > 15%/an | PER acceptable
- Exemples BRVM : BOA CI (en forte croissance), ORANGE CI

### 3. Valeurs de dividende (20–30%)
- Yield > 6% | Payout ratio < 75%
- Exemples BRVM : BOA BF (7.21%), BOA SN (6.83%), SONATEL (6.13%)

### 4. Cash et obligations (10–15%)
- Garder des liquidités pour les opportunités
- Obligations d'État si tu veux un rendement fixe sur cette part

---

## Construction d'un portefeuille simulé à 500 000 FCFA

```
Allocation proposée :

SONATEL (SNTS.sn)   → 40% → 200 000 FCFA
  Défensif + dividende 6.13% + fondamentaux excellents

BOA CI (BOAC.ci)    → 30% → 150 000 FCFA
  Croissance (+42% sur 1 an) + secteur bancaire solide

TOTAL CI (TTLC.ci)  → 20% → 100 000 FCFA
  Ultra-défensif (beta 0.29) + rebond en cours

Liquidités          → 10% → 50 000 FCFA
  Réservées pour renforcer sur baisse ou opportunité
```

**Rendement attendu (dividendes seuls) :**
- SONATEL : 200 000 × 6.13% = 12 260 FCFA
- BOA CI : 150 000 × ~4% (estimé) = 6 000 FCFA
- Total dividendes : ~18 000 FCFA/an → 3.6% sur 500K

Plus la plus-value potentielle si les cours montent.

---

## La corrélation — Pourquoi diversifier

Deux actions **corrélées** montent et baissent ensemble → pas de vraie diversification.
Deux actions **décorrélées** évoluent indépendamment → vraie protection.

```
SONATEL + ORANGE CI → Corrélées (toutes deux dans les télécoms)
SONATEL + PALMCI    → Décorrélées (télécom vs agroalimentaire)
```

**Bonne diversification BRVM :**
- 1 valeur télécoms (SONATEL ou ORANGE CI)
- 1 valeur bancaire (BOA CI, SG CI, CORIS BANK)
- 1 valeur industrie/énergie (TOTAL CI, BERNABE)
- 1 valeur agroalimentaire optionnelle (PALMCI, SAPH, NESTLE)

---

## Le rebalancement

Ton portefeuille dérive dans le temps. Si SONATEL monte fort, son poids
peut passer de 40% à 55%. Il faut **rééquilibrer**.

**Fréquence recommandée :** 1 fois par an minimum, 2 fois si marché volatile.

**Comment :**
1. Calcule le poids actuel de chaque valeur
2. Compare à ton allocation cible
3. Vends ce qui dépasse la limite, rachète ce qui est sous-pondéré

---

## Exercice pratique

Construis ton portefeuille idéal simulé :

1. Choisis 2–3 valeurs BRVM qui t'intéressent
2. Définis une allocation (% pour chacune)
3. Justifie chaque choix (fondamentaux + technique)
4. Identifie ta valeur défensive, ta valeur de croissance, ta valeur de dividende

```bash
python tracker.py note 3.1 "Portefeuille simulé: [valeur1] [X%], [valeur2] [Y%], [valeur3] [Z%] — liquidités [W%]"
```

---

## Quiz de vérification

1. Avec 350 000 FCFA, combien de valeurs recommandes-tu ? Pourquoi ?
2. Quelle est la différence entre une valeur défensive et une valeur de croissance ?
3. Pourquoi ne faut-il pas mettre plus de 60% dans un seul secteur ?
4. C'est quoi la corrélation entre deux actions ? Donne un exemple BRVM.
5. Qu'est-ce que le rebalancement et à quelle fréquence le faire ?

```bash
python tracker.py quiz 3.1 <ton_score>
```
