# 📈 BRVM Trader — Plugin Claude Code

> **Expert financier IA spécialisé sur la BRVM** (Bourse Régionale des Valeurs Mobilières, Zone UEMOA).
> Analyse technique & fondamentale en temps réel + formation interactive 3 niveaux pour débutants.

![Claude Code](https://img.shields.io/badge/Claude%20Code-Plugin-orange?logo=anthropic)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Zone](https://img.shields.io/badge/zone-UEMOA%20%2F%20FCFA-yellow)

---

## ⚡ Installation rapide

**1. Ajouter le marketplace dans Claude Code :**

```json
// ~/.claude/settings.json
{
  "extraKnownMarketplaces": {
    "brvm-trader": {
      "source": { "source": "github", "repo": "elysee15/financial-analyst" }
    }
  }
}
```

**2. Installer le plugin :**

```bash
claude plugin marketplace add brvm-trader@brvm-trader
```

**3. Lancer le skill :**

```
/brvm-trader
```

---

## 🎯 Ce que fait ce plugin

### 📊 Analyser le marché en temps réel

Le skill fetch automatiquement les données live depuis **sikafinance.com** et produit une analyse structurée :

```
SONATEL (SNTS.sn) — Analyse au 29/03/2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cours          : 28 400 FCFA   Variation : -0.09%
RSI            : 49.55 ✅      Beta      : 0.83 (défensif)
Volume         : 7 988 titres  Cap       : 2 840 Mds FCFA
Dividende      : 1 740 FCFA    Yield     : 6.13%
PER            : 6.9x          Plus haut : 29 300 FCFA

Score Technique  : 4/5
Score Fondamental: 5/5
━━━━━━━━━━━━━━━━━━
VERDICT : ACHAT FORT 🟢 (9/10)
Entrée : 27 800–28 400 FCFA | Stop : 24 200 FCFA | Objectif 12m : 32 000 FCFA
```

### 📚 Formation interactive à la BRVM

**3 niveaux progressifs, 13 modules, ~15h de contenu conversationnel** — sans vidéos, sans liens externes, tout se passe dans le chat.

| Niveau | Thème | Modules | Durée |
|--------|-------|---------|-------|
| **1 — Initiation** | Vocabulaire, Pourquoi investir, Organisation BRVM, Acteurs du marché, Premier ordre | 5 modules | 4h30 |
| **2 — Analyser** | Lire un graphique, Analyse technique (RSI/supports), Analyse fondamentale (PER/dividendes), Timing achat/vente | 4 modules | 5h |
| **3 — Stratégies** | Construire un portefeuille, Gestion du risque, DCA / Buy&Hold / Momentum, Capture de dividendes | 4 modules | 4h45 |

**Fonctionnement :**
- Claude enseigne les concepts à l'oral, avec des exemples sur des valeurs BRVM réelles
- Questions de compréhension après chaque concept
- **Quiz de fin de module** avec score /10 et correction détaillée
- Score ≥ 7/10 → module suivant débloqué
- **Progression sauvegardée automatiquement** dans `.claude/courses/progress.md`

### 🎯 Accompagnement stratégique

| Stratégie | Profil | Critères |
|-----------|--------|----------|
| **DCA** | Tous | Investir en 2 tranches (immédiat + J+45) |
| **Buy & Hold Dividendes** | Conservateur | Yield >5% + RSI 35–55 + Beta <0.9 |
| **Momentum** | Actif | RSI 50–65 + Perf 1 mois >+5% + Volume fort |
| **Capture Dividende** | Opportuniste | Acheter ≥5 jours avant détachement |
| **Contrarian** | Expérimenté | Correction >-20% + RSI <35 + dividende maintenu |

---

## 📐 Système de scoring (/10)

Chaque analyse produit un score objectif avant toute décision :

| Critère Technique | | Critère Fondamental | |
|---|-|----|---|
| RSI 30–60 | +1 | Dividend Yield >5% | +1 |
| Beta <0.9 | +1 | Bénéfices croissants 3 ans | +1 |
| Momentum 1 mois positif | +1 | Capitalisation >200 Mds | +1 |
| Volume > moyenne | +1 | Backing groupe international | +1 |
| Trend YTD positif | +1 | PER <15 | +1 |

**≥ 8/10 → ACHAT FORT 🟢 · 6–7/10 → ACHAT PARTIEL 🟡 · ≤ 5/10 → PASSER 🔴**

---

## 🏦 Valeurs BRVM couvertes

| Ticker | Société | Pays |
|--------|---------|------|
| SNTS.sn | SONATEL | Sénégal |
| BOAC.ci | BOA Côte d'Ivoire | Côte d'Ivoire |
| ORAC.ci | Orange CI | Côte d'Ivoire |
| ECOC.ci | Ecobank CI | Côte d'Ivoire |
| SGBC.ci | SG CI | Côte d'Ivoire |
| TTLC.ci | Total CI | Côte d'Ivoire |
| SIBC.ci | SIB CI | Côte d'Ivoire |
| CBIBF.bf | Coris Bank | Burkina Faso |
| NSBC.ci | NSIA | Côte d'Ivoire |
| BOABF.bf | BOA Burkina Faso | Burkina Faso |
| BOAS.sn | BOA Sénégal | Sénégal |
| BOAB.bj | BOA Bénin | Bénin |

Et toutes les valeurs BRVM via **sikafinance.com**.

---

## 🗂 Structure du repo

```
financial-analyst/
├── .claude-plugin/
│   ├── marketplace.json    ← Listing marketplace (schema Anthropic)
│   └── plugin.json         ← Définition du plugin
├── skills/
│   └── brvm-trader/
│       ├── SKILL.md        ← Cerveau du skill (analyse + formation)
│       └── courses/
│           ├── niveau1/    ← 5 modules .mdc (initiation)
│           ├── niveau2/    ← 4 modules .mdc (analyse)
│           └── niveau3/    ← 4 modules .mdc (stratégies)
├── formations/             ← Contenu pédagogique détaillé (.md)
│   ├── niveau1/
│   ├── niveau2/
│   ├── niveau3/
│   └── parcours.json       ← Suivi de progression JSON
└── CLAUDE.md               ← Instructions contextuelles du projet
```

---

## 🔎 Prérequis

- [Claude Code](https://claude.ai/download) installé
- Aucun compte boursier requis pour la formation
- Connexion internet (pour les données live sikafinance.com)

---

## ⚠️ Avertissement

Ce plugin est un **outil éducatif**. Les analyses sont des exemples pédagogiques et **ne constituent pas des conseils en investissement**. Tout investissement en bourse comporte des risques de perte en capital. Consultez un professionnel agréé avant toute décision réelle.

---

## 📄 Licence

MIT — libre d'utilisation, de modification et de redistribution.

---

*Données de marché : [sikafinance.com](https://www.sikafinance.com) · Zone UEMOA / FCFA · Plugin Claude Code*
