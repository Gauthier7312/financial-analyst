---
description: >
  Résumé du marché BRVM du jour : indices, palmarès des hausses et baisses,
  top volumes, et actualités marquantes. Fetche en temps réel depuis sikafinance.com.
  Usage : /marche
---

# Commande : /marche

## Comportement

1. **Déléguer à l'agent `brvm-marche`** pour fetcher en parallèle :
   - `sikafinance.com/marches/palmares` — palmarès du jour
   - `sikafinance.com/marches/actualites_bourse_brvm` — actualités récentes

2. **Afficher le résumé structuré** :

```
📈 MARCHÉ BRVM — [JOUR] [DATE]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INDICES
  BRVM Composite : [X] pts   [±X]% jour  [±X]% YTD
  BRVM 30        : [X] pts   [±X]% jour  [±X]% YTD

TOP 5 HAUSSES              TOP 5 BAISSES
  1. [Valeur] +[X]%    │   1. [Valeur] -[X]%
  2. [Valeur] +[X]%    │   2. [Valeur] -[X]%
  3. [Valeur] +[X]%    │   3. [Valeur] -[X]%
  4. [Valeur] +[X]%    │   4. [Valeur] -[X]%
  5. [Valeur] +[X]%    │   5. [Valeur] -[X]%

TOP VOLUMES (signaux de momentum)
  1. [Valeur] — [X] titres échangés
  2. [Valeur] — [X] titres échangés
  3. [Valeur] — [X] titres échangés

📰 ACTUALITÉS
  → [actu 1]
  → [actu 2]
  → [actu 3]

💡 SIGNAL DU JOUR
  [1 phrase sur le momentum général du marché]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Analyser une valeur → /analyse [nom]
Dividendes imminents → /dividendes
```

3. **Si une valeur du palmarès est dans le portefeuille de l'utilisateur**, signaler :
   ```
   ⚡ [VALEUR] est dans ton portefeuille — cours actuel [X] FCFA ([±X]% depuis ton entrée)
   ```
