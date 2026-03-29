---
description: >
  Affiche le calendrier des dividendes BRVM 2026 avec yields, dates de détachement,
  deadlines d'achat, et analyse RSI pour identifier les opportunités de capture.
  Usage : /dividendes | /dividendes SONATEL
---

# Commande : /dividendes

## Comportement par défaut — `/dividendes`

1. **Déléguer à l'agent `brvm-marche`** pour fetcher :
   - `sikafinance.com/marches/dividendes` — calendrier officiel
   - Cotations des valeurs avec dividendes imminents (RSI, cours actuel)

2. **Déléguer à l'agent `brvm-stratege`** pour filtrer selon la stratégie D (Capture Dividende) :
   - Yield > 5%
   - RSI < 65 (pas suracheté)
   - Date de détachement dans les 60 prochains jours

3. **Afficher le calendrier structuré** :

```
📅 CALENDRIER DIVIDENDES BRVM 2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

OPPORTUNITÉS ACTIVES (Yield > 5% + RSI < 65)
┌─────────────┬──────────┬───────────┬─────────────┬──────────────┬──────────┐
│ Valeur      │ Dividende│ Yield     │ Détachement │ Acheter avant│ RSI      │
├─────────────┼──────────┼───────────┼─────────────┼──────────────┼──────────┤
│ [Valeur]    │ [X] FCFA │ [X]%  ✅  │ [date]      │ [date] ⚡    │ [X] ✅   │
└─────────────┴──────────┴───────────┴─────────────┴──────────────┴──────────┘

SURVEILLER (RSI élevé — attendre repli)
  [Valeur] — [X]% — RSI [X] 🔴 — attendre RSI < 60

CALENDRIER COMPLET 2026
  [Valeur] : [X] FCFA ([X]%) → [date détachement]
  [...]

⚠️ RAPPEL MÉCANIQUE
La capture de dividende n'est rentable que si la valeur est en tendance
haussière. Le cours baisse du montant du dividende le jour du détachement.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Analyser une opportunité → /analyse [valeur]
Module dédié → /formation 3.4
```

## Comportement avec argument — `/dividendes [VALEUR]`

Analyse spécifique de la stratégie Capture Dividende pour cette valeur :
1. Fetche le cours et RSI live
2. Calcule le rendement total estimé (plus-value + dividende) selon 3 scénarios
3. Recommande d'acheter maintenant, d'attendre, ou d'éviter avec justification

## Exemple d'utilisation

```
/dividendes              ← calendrier complet + opportunités filtrées
/dividendes SONATEL      ← analyse capture dividende SONATEL
/dividendes BOA BF       ← analyse capture dividende BOA BF
```
