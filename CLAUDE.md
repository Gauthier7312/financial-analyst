# Contexte Projet — Formation BRVM

## Qui je suis
- **Apprenant** — je me forme au fonctionnement du marché boursier et de la BRVM
- Aucun compte boursier ouvert pour l'instant, aucun capital investi
- Objectif : comprendre les mécanismes de la bourse avant d'investir réellement

## Mon niveau actuel
- Débutant complet en bourse
- En phase de formation et d'apprentissage
- Pas encore de SGI, pas de portefeuille réel

## Module de formation
- `formations/parcours.json` — Suivi du parcours apprenant (progression, scores, journal)
- `formations/tracker.py` — Script CLI de gestion du parcours
- `formations/niveau1/` — Initiation à la Bourse & BRVM (4 modules + quiz)
- `formations/niveau2/` — Analyser et choisir ses actions (4 modules + quiz)
- `formations/niveau3/` — Stratégies d'investissement (4 modules + quiz)

## Fichiers du projet
- `brvm-trader/SKILL.md` — Skill expert BRVM (analyse technique + fondamentale + stratégies)
- `brvm-trader/references/valeurs_brvm.md` — Tickers et snapshot marché
- `brvm-trader/references/news_et_communiques.md` — Actualités et communiqués live
- `brvm-trader/references/strategies_avancees.md` — Patterns de trading avancés
- `brvm-trader/references/watch_list.md` — Liste de surveillance avec alertes prix

## Instructions pour Claude
- Toujours activer le skill `brvm-trader` pour toute question BRVM
- Toujours fetcher les données live sur sikafinance.com avant toute analyse
- Adapter les explications à un profil débutant : vulgariser, expliquer les concepts, donner des exemples concrets
- Quand on parle d'actions ou de stratégies, préciser qu'il s'agit d'exemples pédagogiques, pas de conseils d'investissement réels
- Parler franchement, avec des chiffres précis, mais sans présupposer qu'un achat ou vente va avoir lieu
- Après chaque session de formation, proposer de mettre à jour `formations/parcours.json` via `python formations/tracker.py`
- Si l'apprenant répond à un quiz, l'aider à s'auto-évaluer et lui suggérer d'enregistrer son score
