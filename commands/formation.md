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

2. **Afficher le tableau de bord** :

```
📚 TON PARCOURS BRVM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Progression : [████░░░░░░░░░░░░░░░░] [X]%
Badges      : [liste ou "aucun pour l'instant"]

NIVEAU 1 — Initiation [statut]
  ✅ 1.0 Introduction & Vocabulaire         [score]/10
  [✅/🟡/⬜/🔒] 1.1 Pourquoi investir ?      [score ou —]
  [✅/🟡/⬜/🔒] 1.2 Organisation BRVM        [score ou —]
  [✅/🟡/⬜/🔒] 1.3 Les acteurs              [score ou —]
  [✅/🟡/⬜/🔒] 1.4 Premier ordre            [score ou —]

NIVEAU 2 — Analyser [statut]
  [✅/🔒] 2.1  Lire un graphique
  [✅/🔒] 2.2  Analyse technique (RSI)
  [✅/🔒] 2.3  Analyse fondamentale
  [✅/🔒] 2.4  Quand acheter/vendre ?

NIVEAU 3 — Stratégies [statut]
  [✅/🔒] 3.1  Construire un portefeuille
  [✅/🔒] 3.2  Gestion du risque
  [✅/🔒] 3.3  Stratégies DCA, Momentum...
  [✅/🔒] 3.4  Capture de dividendes

📌 PROCHAIN MODULE : [X.X] — [titre]
   Durée estimée : [X] min
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Continuer → réponds "go" ou "1" | Changer de module → /formation [numéro]
```

## Comportement avec argument — `/formation [X.X]`

1. Vérifier que le module existe (1.0 à 3.4)
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
/formation 3.4       ← capture de dividendes
/formation quiz      ← passer le quiz du module en cours
```
