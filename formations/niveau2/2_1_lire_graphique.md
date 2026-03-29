# Module 2.1 — Lire un graphique boursier

> **Durée estimée :** 1h | **Niveau :** Intermédiaire | **Statut :** `python tracker.py start 2.1`

---

## Anatomie d'un graphique boursier

Sur sikafinance.com, chaque valeur a un graphique. Voici comment le lire.

### Les types de graphiques

**Graphique en ligne** — Le plus simple
Relie les prix de clôture. Bonne vue d'ensemble de la tendance.

**Graphique en chandeliers japonais (Candlesticks)** — Le plus utilisé
Chaque bougie représente une période (jour, semaine, mois).

```
     │  ← Mèche haute (plus haut de la période)
    ┌┴┐
    │ │ ← Corps (entre ouverture et clôture)
    └┬┘
     │  ← Mèche basse (plus bas de la période)

Bougie verte/blanche = hausse (clôture > ouverture)
Bougie rouge/noire   = baisse (clôture < ouverture)
```

---

## Les 3 tendances

```
HAUSSIÈRE  : Série de sommets et creux croissants
             Chaque rebond dépasse le précédent      ↗↗↗

BAISSIÈRE  : Série de sommets et creux décroissants
             Chaque rebond échoue plus bas            ↘↘↘

LATÉRALE   : Oscillations dans un range horizontal
             Ni haussier ni baissier                  ↔↔↔
```

**Règle d'or :** Ne jamais acheter contre la tendance dominante.

---

## Supports et Résistances — La base de l'analyse graphique

Un **support** est un niveau de prix où la demande est forte — les acheteurs
reviennent systématiquement à ce niveau, empêchant le cours de descendre plus bas.

Une **résistance** est un niveau où l'offre est forte — les vendeurs bloquent
la hausse à ce niveau.

### Exemple SONATEL (données réelles 28/03/2026)

```
Cours actuel : 28 400 FCFA
Plus haut 52 sem : 29 300 → RÉSISTANCE
Plus bas 52 sem  : 24 000 → SUPPORT FORT

Si SONATEL franchit 29 300 avec volume
  → Signal haussier vers 32 000–33 000 FCFA

Si SONATEL casse 24 000 à la baisse
  → Signal baissier vers 21 000–22 000 FCFA
```

### Comment identifier un support/résistance valide ?

- Le cours a rebondi sur ce niveau **au moins 2 fois** dans le passé
- Le rebond s'est accompagné d'un volume élevé
- Plus un niveau a été testé souvent, plus il est solide

---

## Le Volume — Le juge de paix

Le volume confirme ou invalide chaque mouvement de cours.

| Signal cours | Volume | Interprétation |
|---|---|---|
| Hausse | Élevé | Mouvement fiable ✅ |
| Hausse | Faible | Mouvement suspect ⚠️ |
| Baisse | Élevé | Vente de conviction 🔴 |
| Baisse | Faible | Correction temporaire possible 🟡 |
| Stagnation | Élevé | Accumulation/distribution en cours |

---

## Les figures chartistes classiques

### Double Fond (signal d'achat)
```
      ──────
     /      \         /
    /        \       /
   /          \_____/
```
Le cours touche le même support 2 fois puis repart à la hausse.
**Signal :** Achat au franchissement du col (ligne médiane).

### Double Sommet (signal de vente)
```
   \_____/
         \       /
          \     /
           \___/
```
Le cours bute 2 fois sur la même résistance. **Signal :** Vente.

### Triangle (consolidation avant cassure)
```
   \         /
    \       /
     \─────/
```
Compression du cours = énergie accumulée. Cassure violente à venir.
La direction de la cassure détermine le sens du trade.

---

## Exercice pratique sur sikafinance.com

1. Va sur `sikafinance.com/marches/cotation_BOAC.ci` (BOA CI)
2. Observe le graphique sur **6 mois**
3. Identifie :
   - La tendance principale (haussière / baissière / latérale)
   - Le niveau de support le plus proche
   - Le niveau de résistance le plus proche
   - Un moment où le volume a été élevé — que s'est-il passé sur le cours ?

```bash
python tracker.py note 2.1 "BOA CI tendance: [ta réponse] — Support: [X] — Résistance: [Y]"
```

---

## Quiz de vérification

1. Qu'est-ce qu'un support ? Comment l'identifier ?
2. Que signifie une hausse avec un faible volume ?
3. TOTAL CI est à 2 975 FCFA. Son plus bas 52 sem est 2 100. C'est quoi le support ?
4. Décris la figure "double fond" et ce qu'elle signifie.
5. Pourquoi la tendance est-elle plus importante que le cours actuel ?

```bash
python tracker.py quiz 2.1 <ton_score>
```
