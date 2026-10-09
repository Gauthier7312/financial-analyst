---
description: >
  Point d'entrée principal du plugin BRVM Trader. Initialise le parcours de
  formation au premier lancement, affiche l'état de la progression et oriente
  vers l'analyse de marché, la formation, les dividendes ou le portefeuille.
  Usage : /brvm-trader
---

# Commande : /brvm-trader

Point d'entrée du plugin. Ne fait aucun fetch de données : c'est un aiguillage.

## Séquence

1. **Lire `.claude/courses/progress.md`**
   - Si le fichier est absent : déléguer à l'agent `brvm-formateur` pour le créer
     avec le template des 9 niveaux (voir `agents/formateur.md` → « Initialisation
     de progress.md »), puis signaler `🆕 Parcours initialisé — tu démarres au module 1.0`
   - Si présent : en extraire la progression globale, les badges et le module suivant

2. **Afficher le message d'accueil** ci-dessous, en remplaçant les champs entre
   crochets par les valeurs réelles lues dans `progress.md`

3. **Attendre le choix** de l'apprenant et router vers la commande correspondante

## Message d'accueil

```
# Bonjour — Je suis ton Expert BRVM 👋

📊 ANALYSER LE MARCHÉ          → /analyse [VALEUR] ou /marche
   Données live sikafinance.com · Score /10 · Verdict ACHAT/ATTENDRE/ÉVITER

📚 TE FORMER À LA BOURSE       → /formation
   Progression : [████░░░░░░░░░░░░░░░░] [X]%  ([n]/37 modules)
   Badges      : [liste ou "aucun pour l'instant"]
   Prochain    : [X.X] — [titre] ([durée])

🎯 STRATÉGIES & DIVIDENDES     → /dividendes · /portefeuille
   Calendrier dividendes 2026 · DCA · Buy & Hold · Momentum · Capture dividende

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Que veux-tu faire ?
  1️⃣  Continuer ma formation → [X.X] [titre]
  2️⃣  Analyser une action BRVM
  3️⃣  Voir le marché du jour
  4️⃣  Consulter mon portefeuille
```

## Routage des réponses

| Réponse | Action |
|---------|--------|
| `1` / « formation » / « continuer » | `/formation` — agent `brvm-formateur` |
| `2` / « analyse » / un ticker (ex. `SONATEL`) | `/analyse [TICKER]` — agents `brvm-marche` + `brvm-stratege` |
| `3` / « marché » / « palmarès » | `/marche` — agent `brvm-marche` |
| `4` / « portefeuille » / « positions » | `/portefeuille` — agent `brvm-portefeuille` |
| « dividendes » | `/dividendes` |
| Question libre sur la bourse | Répondre directement, puis lier au module de formation pertinent |

## Rappel obligatoire

Au premier lancement d'une session, afficher une fois :

> ⚠️ Les analyses de ce plugin sont des **exemples pédagogiques**, pas des conseils
> d'investissement. Aucun ordre ne peut être passé depuis Claude Code — il faut
> une SGI agréée par le CREPMF.
