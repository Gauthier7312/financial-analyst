# Contexte Projet — Formation & Trading BRVM

## Qui je suis
- **Apprenant** — je me forme au fonctionnement du marché boursier et de la BRVM
- Aucun compte boursier ouvert pour l'instant, aucun capital investi
- Objectif : comprendre les mécanismes de la bourse avant d'investir réellement

## Mon niveau actuel
- Débutant complet en bourse
- En phase de formation et d'apprentissage
- Pas encore de SGI, pas de portefeuille réel

## Architecture du plugin

Ce projet est un **plugin Claude Code** installable et distribuable.

### Agents spécialisés (`agents/`)
| Agent | Rôle |
|-------|------|
| `brvm-marche` | Données live sikafinance.com (cours, palmarès, dividendes) |
| `brvm-stratege` | Score /10, verdict ACHAT/ATTENDRE/ÉVITER, stratégies |
| `brvm-formateur` | Formation interactive, quiz, progression |
| `brvm-portefeuille` | Positions, stop-loss, alertes, watch list |

### Commandes disponibles (`commands/`)
| Commande | Usage |
|----------|-------|
| `/analyse [VALEUR]` | Analyse complète d'une action BRVM |
| `/marche` | Palmarès et indices du jour |
| `/formation [module]` | Formation interactive + tableau de bord |
| `/portefeuille` | État des positions et alertes |
| `/dividendes` | Calendrier dividendes 2026 |
| `/brvm-trader` | Point d'entrée principal |

### Données de référence (`skills/brvm-trader/data/`)
- `valeurs_brvm.md` — tickers et profils fondamentaux
- `strategies_avancees.md` — patterns de trading avancés
- `news_et_communiques.md` — actualités et alertes
- `watch_list.md` — positions personnelles (ignoré par git)
- `data_freshness.json` — timestamp du dernier fetch

### Formation (`skills/brvm-trader/courses/`)
- `niveau1/` — 5 modules initiation (vocabulaire, BRVM, acteurs, ordres)
- `niveau2/` — 4 modules analyse (graphiques, RSI, fondamentale, timing)
- `niveau3/` — 4 modules stratégies (portefeuille, risque, DCA, dividendes)
- `niveau4/` — 5 modules analyse technique débutant → avancé (MM, MACD, figures, multi-timeframe)
- `niveau5/` — 5 modules analyse fondamentale avancée (bilan, ratios, DCF, sectorielle, rapport annuel)
- `niveau6/` — 4 modules macro-économie UEMOA (CFA, BCEAO, cycles, indicateurs)
- `niveau7/` — 3 modules psychologie & discipline (biais cognitifs, émotions, journal de trading)
- `niveau8/` — 3 modules fiscalité & régulation (impôts UEMOA, CREPMF, droits actionnaire)
- `niveau9/` — 4 modules gestion de portefeuille avancée (diversification, rebalancement, opérations sur titres, performance)

### Progression
- `.claude/courses/progress.md` — créé automatiquement au premier `/brvm-trader`

## Instructions pour Claude
- Utiliser `/brvm-trader` comme point d'entrée principal
- Déléguer systématiquement aux agents spécialisés selon l'intention
- Toujours fetcher les données live sur sikafinance.com avant toute analyse
- Adapter les explications au profil débutant : vulgariser, exemples concrets
- Mentionner que les analyses sont des exemples pédagogiques, pas des conseils d'investissement
- Lier chaque analyse à un module de formation pertinent
