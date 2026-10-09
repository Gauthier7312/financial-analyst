# 📈 BRVM Trader — Plugin Claude Code

> **Expert financier IA spécialisé sur la BRVM** (Bourse Régionale des Valeurs Mobilières, Zone UEMOA).
> 4 agents spécialisés · 6 commandes slash · 37 modules de formation · Données live sikafinance.com

![Claude Code](https://img.shields.io/badge/Claude%20Code-Plugin-orange?logo=anthropic)
![Version](https://img.shields.io/badge/version-2.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Zone](https://img.shields.io/badge/zone-UEMOA%20%2F%20FCFA-yellow)

---

## ⚡ Installation

Le plugin s'installe via le système de marketplace de Claude Code. Deux voies,
au choix — tout se tape **dans Claude Code**, pas dans un terminal.

**Depuis GitHub :**

```
/plugin marketplace add Gauthier7312/financial-analyst
/plugin install brvm-trader@brvm-trader
```

**Depuis une copie locale du dépôt** (recommandé si tu modifies le plugin : tes
changements sont pris en compte sans passer par un `git push`) :

```
/plugin marketplace add /chemin/vers/financial-analyst
/plugin install brvm-trader@brvm-trader
```

La syntaxe est `<plugin>@<marketplace>` — ici les deux s'appellent `brvm-trader`.

**Vérifier :** tape `/plugin` → `brvm-trader` doit apparaître dans « Installed
plugins » avec 4 agents, 6 commandes et 2 skills. Puis tape `/` : `/brvm-trader`,
`/formation`, `/analyse`, `/marche`, `/portefeuille`, `/dividendes` sont disponibles.

**Lancer :**

```
/brvm-trader
```

Au premier lancement, ton fichier de progression est créé dans
`.claude/courses/progress.md` et tu démarres au module 1.0.

> Les équivalents en ligne de commande existent aussi :
> `claude plugin marketplace add <dépôt-ou-chemin>` puis
> `claude plugin install brvm-trader@brvm-trader`.

### Hooks recommandés (optionnels, dans `~/.claude/settings.json`)

Ces hooks améliorent l'expérience mais ne sont pas obligatoires :

```json
{
  "hooks": {
    "SessionStart": [{
      "hooks": [{
        "type": "command",
        "command": "test -f \"$HOME/.claude/courses/progress.md\" && echo '{\"systemMessage\": \"📊 Progression BRVM chargée\"}' || echo '{\"systemMessage\": \"👋 Lance /brvm-trader pour démarrer ta formation BRVM\"}'",
        "timeout": 5
      }]
    }],
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_input.file_path // empty' | grep -q 'progress\\.md' && echo '{\"systemMessage\": \"✅ Progression sauvegardée\"}' || true",
        "timeout": 5
      }]
    }]
  }
}
```

---

## 🗺️ Architecture

```
financial-analyst/
│
├── agents/                         ← 4 agents spécialisés
│   ├── marche.md                   ← Données live sikafinance.com
│   ├── stratege.md                 ← Score /10 + verdict + stratégie
│   ├── formateur.md                ← Formation interactive + progression
│   └── portefeuille.md             ← Positions + stop-loss + alertes
│
├── commands/                       ← 6 commandes slash
│   ├── brvm-trader.md              ← /brvm-trader (point d'entrée)
│   ├── analyse.md                  ← /analyse [TICKER]
│   ├── marche.md                   ← /marche
│   ├── formation.md                ← /formation [module]
│   ├── portefeuille.md             ← /portefeuille
│   └── dividendes.md               ← /dividendes
│
├── skills/
│   └── brvm-trader/
│       ├── SKILL.md                ← Orchestrateur principal
│       ├── courses/
│       │   ├── niveau1/            ← 5 modules .mdc (initiation)
│       │   ├── niveau2/            ← 4 modules .mdc (analyse)
│       │   ├── niveau3/            ← 4 modules .mdc (stratégies)
│       │   ├── niveau4/            ← 5 modules .mdc (technique approfondie)
│       │   ├── niveau5/            ← 5 modules .mdc (fondamentale avancée)
│       │   ├── niveau6/            ← 4 modules .mdc (macro UEMOA)
│       │   ├── niveau7/            ← 3 modules .mdc (psychologie)
│       │   ├── niveau8/            ← 3 modules .mdc (fiscalité)
│       │   └── niveau9/            ← 4 modules .mdc (portefeuille avancé)
│       └── data/
│           ├── valeurs_brvm.md     ← Tickers + profils fondamentaux
│           ├── strategies_avancees.md ← Patterns trading avancés
│           ├── news_et_communiques.md ← Actualités et alertes
│           ├── watch_list.md       ← Template positions (ignoré git)
│           ├── market_snapshot.md  ← Dernière valeur connue entre sessions
│           ├── data_freshness.json ← Timestamps des derniers fetches
│           └── cache/              ← Cache daté YYYY-MM-DD_[source].md
│
├── .claude/
│   └── settings.json               ← Hooks SessionStart + PostToolUse
│
├── .claude-plugin/
│   ├── marketplace.json            ← Listing marketplace
│   └── plugin.json                 ← Agents + Skills + Commands
│
└── README.md
```

---

## 🤖 Les 4 agents

### `brvm-marche` — Données Live

Source unique de données de marché. Fetche sikafinance.com et retourne des
structures normalisées consommables par les autres agents.

- Cotation individuelle : cours, RSI, Beta, volumes, perfs, dividende, PER
- Palmarès du jour : top hausses/baisses/volumes + indices
- Dividendes : calendrier complet avec yields
- Actualités : news et alertes CREPMF
- **Cache daté** : vérifie `skills/brvm-trader/data/cache/YYYY-MM-DD_[source].md` avant tout fetch — réutilise si disponible, sauvegarde après fetch réussi

### `brvm-stratege` — Analyse Stratégique

Transforme les données brutes en décisions d'investissement structurées.

- Score technique /5 (RSI, Beta, momentum, volume, trend YTD)
- Score fondamental /5 (yield, bénéfices, capitalisation, backing, PER)
- Verdict ACHAT FORT 🟢 / ACHAT PARTIEL 🟡 / PASSER 🔴
- Sélection de stratégie adaptée (DCA, Buy&Hold, Momentum, Capture dividende, Contrarian)
- Niveaux opérationnels : entrée, stop-loss -15%, objectifs 3m et 12m
- Checklist pré-achat 15 critères

### `brvm-formateur` — Formation Interactive

Gère intégralement le parcours pédagogique sans aucune ligne de commande.

- Crée `progress.md` automatiquement si absent
- Enseigne 37 modules sur 9 niveaux (concept par concept, exemples BRVM réels)
- Quiz interactif oral avec correction détaillée
- Système de déblocage par niveau (score ≥ 7/10)
- Sauvegarde progression dans `progress.md` après chaque quiz
- Badges : 🏅 Initié → 🥈 Analyste → 🏆 Stratège → 📊 Chartiste → 🔍 Fondamentaliste →
  🌍 Macro-Économiste → 🧠 Mental d'Acier → ⚖️ Averti → 👑 Gestionnaire de Portefeuille

### `brvm-portefeuille` — Suivi de Portefeuille

Tracker personnel des positions avec alertes automatiques.

- P&L latent en temps réel (cours live via brvm-marche)
- Alertes stop-loss (critique si cours ≤ stop, avertissement si à -3%)
- Calendrier dividendes filtré sur les positions actives
- Gestion de la watch list : ajouter, modifier, clôturer des positions
- Règles de concentration automatiquement vérifiées

---

## ⌨️ Les 6 commandes

| Commande | Description | Exemple |
|----------|-------------|---------|
| `/brvm-trader` | Point d'entrée — accueil + progression | `/brvm-trader` |
| `/analyse [valeur]` | Analyse complète + score /10 | `/analyse SONATEL` |
| `/marche` | Palmarès + indices du jour | `/marche` |
| `/formation [module]` | Formation interactive | `/formation 2.2` |
| `/portefeuille` | État positions + alertes | `/portefeuille` |
| `/dividendes` | Calendrier dividendes 2026 | `/dividendes SONATEL` |

---

## 📚 Formation — 9 niveaux, 37 modules, ~36h

| Niveau | Modules | Durée | Déblocage |
|--------|---------|-------|-----------|
| **1 — Initiation** | Vocabulaire · Pourquoi investir · Organisation BRVM · Acteurs · Premier ordre | 3h15 | Dès l'installation |
| **2 — Analyser** | Graphiques · RSI, MM, MACD · PER, ROE, dividendes · Timing achat/vente | 4h30 | Quiz N1 ≥ 7/10 |
| **3 — Stratégies** | Portefeuille · Gestion risque · DCA/Momentum · Capture dividendes | 3h30 | Quiz N2 ≥ 7/10 |
| **4 — Technique approfondie** | Bases · Bollinger · Momentum avancé · Figures chartistes · Multi-timeframe | 6h30 | Quiz N3 ≥ 7/10 |
| **5 — Fondamentale avancée** | Bilan · Ratios · Valorisation DCF · Sectorielle · Rapport annuel | 5h45 | Quiz N4 ≥ 7/10 |
| **6 — Macro UEMOA** | Franc CFA · BCEAO & taux · Cycles économiques · Indicateurs macro | 4h00 | Quiz N5 ≥ 7/10 |
| **7 — Psychologie** | Biais cognitifs · Gestion des émotions · Journal de trading | 2h45 | Quiz N6 ≥ 7/10 |
| **8 — Fiscalité & régulation** | Fiscalité UEMOA · CREPMF · Droits des actionnaires | 2h15 | Quiz N7 ≥ 7/10 |
| **9 — Portefeuille avancé** | Diversification · Rebalancement · Opérations sur titres · Performance | 3h45 | Quiz N8 ≥ 7/10 |

Chaque module se termine par un quiz oral de 5 questions noté /10. Il faut **7/10**
pour débloquer la suite. La progression est sauvegardée dans `.claude/courses/progress.md`
(fichier personnel, exclu du dépôt).

---

## 📐 Système de scoring /10

| Technique /5 | Fondamental /5 |
|---|---|
| RSI 30–60 → +1 | Dividend Yield > 5% → +1 |
| Beta < 0.9 → +1 | Bénéfices croissants 3 ans → +1 |
| Momentum 1 mois + → +1 | Capitalisation > 200 Mds → +1 |
| Volume > moyenne → +1 | Backing groupe international → +1 |
| Trend YTD + → +1 | PER < 15x → +1 |

**≥ 8/10 → ACHAT FORT 🟢 · 6–7/10 → ACHAT PARTIEL 🟡 · ≤ 5/10 → PASSER 🔴**

---

## 🏦 Valeurs BRVM couvertes

SONATEL · BOA CI · Orange CI · Ecobank CI · SG CI · Total CI · SIB CI · Coris Bank · NSIA · BOA BF · BOA SN · BOA BJ · PALMCI · SAPH CI · et toutes les valeurs BRVM via sikafinance.com

---

## ⚠️ Avertissement

Ce plugin est un **outil éducatif**. Les analyses sont des exemples pédagogiques et **ne constituent pas des conseils en investissement**. Tout investissement comporte des risques de perte en capital.

---

*Plugin Claude Code v2.0 · Zone UEMOA / FCFA · Données : [sikafinance.com](https://www.sikafinance.com)*
