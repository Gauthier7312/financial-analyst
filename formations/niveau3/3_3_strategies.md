# Module 3.3 — Stratégies : DCA, Buy & Hold, Momentum, Contrarian

> **Durée estimée :** 1h | **Niveau :** Avancé | **Statut :** `python tracker.py start 3.3`

---

## Les 5 stratégies du skill BRVM Trader

### Stratégie A — DCA (Dollar Cost Averaging)
**Pour qui :** Tous les profils, débutants en priorité.

Investir en tranches régulières plutôt qu'en une seule fois.

```
Exemple : 300 000 FCFA à investir sur SONATEL

Plan DCA sur 3 mois :
  Avril    : 150 000 FCFA à 28 400 FCFA → ~5.28 actions
  Mai      : 100 000 FCFA à 27 200 FCFA → ~3.68 actions (si baisse)
  Juin     : 50 000 FCFA  à 29 000 FCFA → ~1.72 actions (si hausse)

Prix moyen = (150K×28400 + 100K×27200 + 50K×29000) / 300K
           = (4 260K + 2 720K + 1 450K) / 300K = 27 967 FCFA/action
```

**Avantage :** Tu achètes plus quand c'est bas, moins quand c'est cher.
**Idéal pour :** Construire une position longue sur une blue chip.

---

### Stratégie B — Buy & Hold Dividendes
**Pour qui :** Investisseur conservateur, horizon 3–5 ans.

**Critères d'entrée :**
- Rendement dividende > 5%
- RSI entre 35 et 55
- Beta < 0.9
- Bénéfices en croissance 3 ans consécutifs

**Valeurs BRVM 2026 :** SONATEL (6.13%), BOA SN (6.83%), BOA BF (7.21%)

**Logique :** Tu achètes pour les dividendes et tu laisses la plus-value venir naturellement.

```
100 000 FCFA sur SONATEL :
  Dividende 2026 : 6 130 FCFA
  Dividende 2027 : ~6 500 FCFA (si croissance bénéfices)
  Plus-value estimée sur 3 ans : +15 à +25%

Rendement total estimé sur 3 ans : 35–45%
```

---

### Stratégie C — Momentum
**Pour qui :** Investisseur actif, tolérance au risque modérée.

**Critères d'entrée :**
- RSI entre 50 et 65
- Perf 1 mois > +5%
- Volume supérieur à la moyenne

**Sortie :** +15 à +25% de gain OU RSI > 72
**Stop-loss :** -10 à -12%

**Logique :** "Les tendances persistent." Une action qui monte avec volume
a tendance à continuer de monter.

```
Exemple : ORANGE CI au 28/03
  RSI : 56.24 ✅ (50-65)
  Perf 1 sem : +5.15% ✅
  Volume : faible ❌

  → Le volume faible invalide le signal. Attendre.
```

---

### Stratégie D — Capture de Dividende
**Pour qui :** Investisseur cherchant un gain court terme défini.

**Principe :** Acheter une valeur avant le détachement de dividende,
percevoir le dividende, puis vendre.

**Règle :** Acheter au minimum 5 jours ouvrables avant la date de détachement.

**Attention :** Le cours baisse généralement du montant du dividende après le détachement.
Le gain réel n'est pas garanti. La stratégie fonctionne mieux sur des valeurs
avec tendance haussière de fond.

```
Calendrier 2026 :
BOA BF   : 7.21% → Acheter avant 15/04
SONATEL  : 6.13% → Acheter avant 15/05
BOA SN   : 6.83% → Acheter avant 20/05
```

---

### Stratégie E — Contrarian (Rebond)
**Pour qui :** Investisseur patient, bonne tolérance au risque.

**Critères d'entrée :**
- Correction > -20% depuis le sommet récent
- RSI < 35 (survendu)
- Dividende maintenu (l'entreprise est solide)
- La baisse est conjoncturelle, pas structurelle

```
Exemple : TOTAL CI
  Baisse 1 an : -14.88%
  YTD : +27.41% (rebond engagé)
  Beta : 0.29 (très défensif)
  RSI : 60.50 (momentum en cours)

  → Stratégie E réussie sur TOTAL CI depuis le début 2026
```

---

## Comment choisir sa stratégie

| Profil | Temps disponible | Stratégie recommandée |
|---|---|---|
| Débutant | Minimal | B (dividendes) + A (DCA) |
| Intermédiaire | 1h/semaine | B + D (capture dividende) |
| Actif | Plusieurs heures/semaine | C (momentum) + E (contrarian) |

**Pour ton profil actuel :** Stratégies A et B. La D pour les dividendes imminents.

---

## Combiner les stratégies — Exemple pratique

```
Capital 500 000 FCFA :

Socle Buy & Hold (Stratégie B)    → 300 000 FCFA
  → SONATEL (avant 15/05 pour dividende)

DCA sur valeur de croissance (A)   → 150 000 FCFA
  → BOA CI en 2 tranches : 75K maintenant + 75K à J+30

Liquidités + opportunité (D/E)     → 50 000 FCFA
  → Prête à saisir un rebond ou une capture de dividende
```

---

## Quiz de vérification

1. Explique la différence entre les stratégies B (Buy & Hold) et C (Momentum).
2. Quels sont les critères pour valider un signal Momentum ?
3. Un ami te dit "j'achète TOTAL CI parce qu'il a beaucoup baissé" — est-ce de la stratégie E ? Justifie.
4. Quel est le risque principal de la stratégie de capture de dividende ?
5. Avec un capital de 200 000 FCFA et un profil débutant, propose une allocation avec 2 valeurs et une stratégie.

```bash
python tracker.py quiz 3.3 <ton_score>
```
