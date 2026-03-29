# 📈 BRVM Trader — Plugin Claude Code

> **Expert financier IA spécialisé sur la BRVM** (Bourse Régionale des Valeurs Mobilières, Zone UEMOA).
> 4 agents spécialisés · 5 commandes slash · 13 modules de formation · Données live sikafinance.com

![Claude Code](https://img.shields.io/badge/Claude%20Code-Plugin-orange?logo=anthropic)
![Version](https://img.shields.io/badge/version-2.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Zone](https://img.shields.io/badge/zone-UEMOA%20%2F%20FCFA-yellow)

---

## ⚡ Installation

**1. Ajouter le marketplace dans Claude Code (`~/.claude/settings.json`) :**

```json
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

**3. Lancer :**

```
/brvm-trader
```

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
├── commands/                       ← 5 commandes slash
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
│       │   └── niveau3/            ← 4 modules .mdc (stratégies)
│       └── data/
│           ├── valeurs_brvm.md     ← Tickers + profils fondamentaux
│           ├── strategies_avancees.md ← Patterns trading avancés
│           ├── news_et_communiques.md ← Actualités et alertes
│           ├── watch_list.md       ← Template positions (ignoré git)
│           └── data_freshness.json ← Cache timestamp fetch
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
- Enseigne 13 modules (concept par concept, avec exemples BRVM réels)
- Quiz interactif oral avec correction détaillée
- Système de déblocage par niveau (score ≥ 7/10)
- Sauvegarde progression dans `progress.md` après chaque quiz
- Badges : 🏅 Initié → 🥈 Analyste → 🏆 Stratège BRVM

### `brvm-portefeuille` — Suivi de Portefeuille

Tracker personnel des positions avec alertes automatiques.

- P&L latent en temps réel (cours live via brvm-marche)
- Alertes stop-loss (critique si cours ≤ stop, avertissement si à -3%)
- Calendrier dividendes filtré sur les positions actives
- Gestion de la watch list : ajouter, modifier, clôturer des positions
- Règles de concentration automatiquement vérifiées

---

## ⌨️ Les 5 commandes

| Commande | Description | Exemple |
|----------|-------------|---------|
| `/analyse [valeur]` | Analyse complète + score /10 | `/analyse SONATEL` |
| `/marche` | Palmarès + indices du jour | `/marche` |
| `/formation [module]` | Formation interactive | `/formation 2.2` |
| `/portefeuille` | État positions + alertes | `/portefeuille` |
| `/dividendes` | Calendrier dividendes 2026 | `/dividendes SONATEL` |

---

## 📚 Formation — 3 niveaux, 13 modules, ~15h

| Niveau | Modules | Durée | Déblocage |
|--------|---------|-------|-----------|
| **1 — Initiation** | Vocabulaire · Pourquoi investir · Organisation BRVM · Acteurs · Premier ordre | 4h30 | Dès l'installation |
| **2 — Analyser** | Graphiques · RSI & supports · PER & dividendes · Timing achat/vente | 5h | Score N1 ≥ 7/10 |
| **3 — Stratégies** | Portefeuille · Gestion risque · DCA/Momentum · Capture dividendes | 4h45 | Score N2 ≥ 7/10 |

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
