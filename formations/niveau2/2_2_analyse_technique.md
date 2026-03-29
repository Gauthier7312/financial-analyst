# Module 2.2 — Analyse Technique : RSI, Moyennes Mobiles, MACD

> **Durée estimée :** 1h15 | **Niveau :** Intermédiaire | **Statut :** `python tracker.py start 2.2`

---

## Le RSI — Relative Strength Index

### Comment ça marche ?
Le RSI mesure la **vitesse et l'amplitude** des mouvements de cours sur les 14 dernières séances.
Il donne un chiffre entre 0 et 100.

```
RSI < 30  → L'action a trop baissé → SURVENDU   → Signal d'achat potentiel 🟢
RSI 30–45 → Zone d'opportunité                  → Intéressant 🟡
RSI 45–60 → Zone neutre / saine                 → Neutre ✅
RSI 60–70 → Début de surchauffe                 → Prudence ⚠️
RSI > 70  → L'action a trop monté → SURACHETÉ   → NE PAS ACHETER 🔴
```

### Valeurs BRVM au 28/03/2026

| Valeur | RSI | Signal |
|---|---|---|
| SONATEL | 49.55 | ✅ Zone saine — bon point d'entrée |
| BOA CI | 60.54 | ⚠️ Limite — attendre |
| TOTAL CI | 60.50 | ⚠️ Limite — attendre |
| ORANGE CI | 56.24 | ✅ Zone saine |
| BOA BF | 75.44 | 🔴 Suracheté — ne pas acheter |

### Les pièges du RSI seul

**Divergence haussière :** Le cours fait de nouveaux plus bas, mais le RSI remonte.
→ Signal de retournement haussier probable.

**Divergence baissière :** Le cours fait de nouveaux plus hauts, mais le RSI baisse.
→ Signal de retournement baissier probable.

**Règle :** Ne jamais utiliser le RSI seul. Le confirmer avec le volume et la tendance.

---

## Les Moyennes Mobiles (MM)

Une moyenne mobile lisse le cours pour éliminer le "bruit" quotidien.

```
MM20 = Moyenne des 20 derniers cours de clôture
MM50 = Moyenne des 50 derniers cours de clôture
MM200 = Moyenne des 200 derniers cours (tendance longue)
```

### Signaux des croisements

```
MM20 croise MM50 à la HAUSSE → "Golden Cross" → Signal d'ACHAT 🟢
MM20 croise MM50 à la BAISSE → "Death Cross"  → Signal de VENTE 🔴
```

### Lecture rapide

| Position | Signal |
|---|---|
| Cours > MM20 > MM50 | Tendance haussière forte ✅ |
| MM20 > Cours > MM50 | Correction dans une tendance haussière — attendre |
| Cours < MM20 < MM50 | Tendance baissière — éviter |
| Cours < MM50 < MM20 | Baisse confirmée — ne pas acheter |

---

## Le MACD

Le MACD (Moving Average Convergence Divergence) mesure l'**élan** du cours.

Il se lit comme :
- **Ligne MACD** (bleue) — différence entre MM12 et MM26
- **Ligne Signal** (rouge) — MM9 du MACD
- **Histogramme** — écart entre les deux lignes

```
MACD croise Signal à la HAUSSE et histogramme passe positif → ACHAT 🟢
MACD croise Signal à la BAISSE et histogramme passe négatif → VENTE 🔴
```

**Sur la BRVM :** Le MACD est moins fiable sur les petites valeurs peu liquides.
L'utiliser principalement sur SONATEL, BOA CI, ORANGE CI, TOTAL CI.

---

## Le Beta — Mesurer la volatilité

Le Beta compare le mouvement d'une action à celui du marché global.

```
Beta = 1    → L'action bouge exactement comme le marché
Beta > 1    → Plus volatile que le marché (risque ET potentiel élevés)
Beta < 1    → Moins volatile que le marché (défensif)
Beta < 0    → Évolue en sens inverse du marché (rare)
```

### Valeurs BRVM au 28/03/2026

| Valeur | Beta | Profil |
|---|---|---|
| TOTAL CI | 0.29 | Ultra-défensif — peu de mouvement |
| BOA CI | 0.34 | Très défensif |
| SONATEL | 0.83 | Défensif |
| ORANGE CI | 1.08 | Légèrement risqué |
| BOA BF | 0.56 | Défensif |

**Pour un débutant :** Privilégier les valeurs avec Beta < 0.9.

---

## Combiner les indicateurs — La méthode

Ne jamais baser une décision sur un seul indicateur.
Voici comment les combiner :

```
ÉTAPE 1 : Tendance (graphique 3–6 mois)
  → Haussière ? Sinon, passer.

ÉTAPE 2 : RSI
  → Entre 30 et 60 ? Sinon, attendre.

ÉTAPE 3 : Volume
  → Les mouvements récents ont-ils du volume ? Sinon, méfiance.

ÉTAPE 4 : Support
  → Suis-je près d'un support ? Meilleur point d'entrée.

ÉTAPE 5 : Beta
  → Mon profil supporte-t-il ce niveau de volatilité ?
```

---

## Exercice pratique

Sur sikafinance.com, analyse ORANGE CI (ORAC.ci) :
- RSI actuel : 56.24 — Dans quelle zone ?
- Beta : 1.08 — Quel profil d'investisseur ?
- Perf 1 mois : -1.64% — Tendance court terme ?
- Conclusion : acheter maintenant ou attendre ?

```bash
python tracker.py note 2.2 "Analyse ORANGE CI: RSI [X] = [signal], Beta [Y] = [profil], conclusion: [ta décision]"
```

---

## Quiz de vérification

1. Un RSI à 72 signifie quoi ? Que faire ?
2. Qu'est-ce qu'un "Golden Cross" ?
3. SONATEL a un Beta de 0.83. Que signifie-t-il pour un investisseur débutant ?
4. Pourquoi ne faut-il pas utiliser le RSI seul pour prendre une décision ?
5. Décris les 5 étapes pour analyser une valeur techniquement.

```bash
python tracker.py quiz 2.2 <ton_score>
```
