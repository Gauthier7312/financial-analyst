---
description: >
  Affiche l'état du portefeuille BRVM avec cours live, P&L latent, alertes
  de stop-loss actives, et dividendes imminents sur les positions. Permet aussi
  d'ajouter/modifier/supprimer des positions et d'ajuster les stop-loss.
  Usage : /portefeuille | /portefeuille ajouter | /portefeuille alerte
---

# Commande : /portefeuille

## Comportement par défaut — `/portefeuille`

1. **Déléguer à l'agent `brvm-portefeuille`** pour lire `watch_list.md`

2. Pour chaque position active, **déléguer à l'agent `brvm-marche`** pour fetcher le cours live

3. **Afficher le rapport complet** (format défini dans `agents/portefeuille.md`)

4. **Afficher les alertes actives** si stop-loss proche ou dividendes dans ≤ 15 jours

## Comportement avec sous-commandes

### `/portefeuille ajouter`
```
Quelle valeur as-tu achetée ?
→ Répondre : "SONATEL — 5 actions à 28 400 FCFA"
→ L'agent ajoute la position avec stop-loss auto (-15%) et objectifs calculés
```

### `/portefeuille stop [VALEUR] [PRIX]`
```
/portefeuille stop SONATEL 26000
→ Met à jour le stop-loss de SONATEL à 26 000 FCFA
```

### `/portefeuille vendre [VALEUR]`
```
/portefeuille vendre BOA CI
→ Archive la position dans le journal avec P&L réalisé
→ Libère l'allocation de capital
```

### `/portefeuille alerte`
```
→ Affiche uniquement les alertes actives (stop-loss proches, dividendes imminents)
→ Utile pour un check rapide sans afficher tout le portefeuille
```

## Exemples d'utilisation

```
/portefeuille             ← état complet avec cours live
/portefeuille ajouter     ← ajouter une nouvelle position
/portefeuille alerte      ← voir uniquement les alertes
/portefeuille stop SONATEL 25000   ← modifier stop-loss
/portefeuille vendre TOTAL CI      ← clôturer une position
```
