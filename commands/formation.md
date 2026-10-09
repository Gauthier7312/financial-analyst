---
description: >
  Lance ou reprend la formation interactive à la bourse BRVM. Sans argument,
  affiche le tableau de bord de progression et propose de continuer le module
  suivant. Avec un numéro de module, lance directement ce module si débloqué.
  Usage : /formation | /formation 1.0 | /formation 2.2 | /formation quiz
---

# Commande : /formation [module optionnel]

## Comportement sans argument — `/formation`

1. **Déléguer à l'agent `brvm-formateur`** pour lire `progress.md`
   - Si `progress.md` absent : le créer et afficher le message de bienvenue

2. **Afficher le tableau de bord** — vue compacte des 9 niveaux, puis le détail
   du seul niveau en cours (ne jamais dérouler les 37 modules d'un coup) :

```
📚 TON PARCOURS BRVM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Progression : [████░░░░░░░░░░░░░░░░] [X]%  ([n]/37 modules)
Badges      : [liste ou "aucun pour l'instant"]

  [✅/🟡/🔒] N1 — Initiation                 [n]/5  · 3h15
  [✅/🟡/🔒] N2 — Analyser                   [n]/4  · 4h30
  [✅/🟡/🔒] N3 — Stratégies                 [n]/4  · 3h30
  [✅/🟡/🔒] N4 — Technique approfondie      [n]/5  · 6h30
  [✅/🟡/🔒] N5 — Fondamentale avancée       [n]/5  · 5h45
  [✅/🟡/🔒] N6 — Macro UEMOA                [n]/4  · 4h00
  [✅/🟡/🔒] N7 — Psychologie & discipline   [n]/3  · 2h45
  [✅/🟡/🔒] N8 — Fiscalité & régulation     [n]/3  · 2h15
  [✅/🟡/🔒] N9 — Portefeuille avancé        [n]/4  · 3h45

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NIVEAU [X] EN COURS — [titre du niveau]

  [✅/🟡/⬜/🔒] [X.X] [titre du module]       [score ou —]
  [... une ligne par module du niveau en cours ...]
  [✅/🟡/⬜/🔒] Quiz N[X] — Validation        [score ou —]

📌 PROCHAIN MODULE : [X.X] — [titre]
   Durée estimée : [X] min
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Continuer → réponds "go" ou "1" | Autre module → /formation [numéro]
Voir un niveau entier → /formation N[X]
```

Légende : ✅ validé · 🟡 en cours · ⬜ disponible non commencé · 🔒 verrouillé

## Comportement avec argument — `/formation [X.X]`

1. Vérifier que le module existe (1.0 → 9.4 — voir la table des 37 modules ci-dessous)
2. Vérifier que le module est débloqué
   - Si verrouillé : indiquer la condition de déblocage et proposer le module actuel
3. Déléguer à l'agent `brvm-formateur` pour enseigner le module
4. Suivre le protocole en 7 étapes (voir `agents/formateur.md`)

## Comportement spécial — `/formation quiz`

Lance le quiz du module en cours (sans re-enseigner les concepts).
Utile pour retenter un quiz après révision.

## Exemples d'utilisation

```
/formation           ← tableau de bord + module suivant
/formation 1.0       ← commencer le vocabulaire
/formation 2.2       ← cours analyse technique RSI
/formation 4.4       ← figures chartistes avancées
/formation 5.3       ← valorisation DCF
/formation 9.4       ← suivi de performance (TRI, benchmark)
/formation N6        ← détail du niveau 6 (macro UEMOA)
/formation quiz      ← passer le quiz du module en cours
```

---

## Les 37 modules

| Niveau | Modules | Durée |
|--------|---------|-------|
| **N1 — Initiation** | 1.0 Vocabulaire · 1.1 Pourquoi investir · 1.2 Organisation BRVM · 1.3 Les acteurs · 1.4 Premier ordre | 3h15 |
| **N2 — Analyser** | 2.1 Lire un graphique · 2.2 Technique (RSI, MM, MACD) · 2.3 Fondamentale (PER, ROE) · 2.4 Timing achat/vente | 4h30 |
| **N3 — Stratégies** | 3.1 Portefeuille · 3.2 Risque & stop-loss · 3.3 DCA/Buy&Hold/Momentum · 3.4 Capture dividendes | 3h30 |
| **N4 — Technique approfondie** | 4.1 Bases absolues · 4.2 Tendance (Bollinger) · 4.3 Momentum avancé · 4.4 Figures chartistes · 4.5 Multi-timeframe | 6h30 |
| **N5 — Fondamentale avancée** | 5.1 Bilan & compte de résultat · 5.2 Ratios clés · 5.3 Valorisation DCF · 5.4 Analyse sectorielle · 5.5 Rapport annuel | 5h45 |
| **N6 — Macro UEMOA** | 6.1 Franc CFA · 6.2 BCEAO & taux · 6.3 Cycles économiques · 6.4 Indicateurs macro | 4h00 |
| **N7 — Psychologie** | 7.1 Biais cognitifs · 7.2 Gestion des émotions · 7.3 Journal de trading | 2h45 |
| **N8 — Fiscalité & régulation** | 8.1 Fiscalité UEMOA · 8.2 CREPMF · 8.3 Droits actionnaires | 2h15 |
| **N9 — Portefeuille avancé** | 9.1 Diversification · 9.2 Rebalancement · 9.3 Opérations sur titres · 9.4 Suivi de performance | 3h45 |

**Total : 9 niveaux · 37 modules · ~36h15**

## Comportement avec un niveau — `/formation N[X]`

Affiche le détail des modules du niveau demandé (statuts, scores, durées) sans
lancer de module. Si le niveau est verrouillé, indiquer la condition de déblocage.
