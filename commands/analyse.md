---
description: >
  Analyse complète d'une valeur BRVM en temps réel. Fetche les données live depuis
  sikafinance.com, calcule le score /10 (technique + fondamental), et produit un
  verdict ACHAT/ATTENDRE/ÉVITER avec niveaux d'entrée, stop-loss et objectifs.
  Usage : /analyse SONATEL | /analyse BOA CI | /analyse TTLC.ci
---

# Commande : /analyse [VALEUR]

## Comportement

1. **Identifier le ticker** depuis l'argument fourni
   - Accepter le nom court (SONATEL), le ticker (SNTS.sn), ou une description partielle
   - Si ambigu, afficher les 2–3 valeurs correspondantes et demander confirmation
   - Si aucun argument : afficher le palmarès du jour (déléguer à `/marche`)

2. **Déléguer à l'agent `brvm-marche`** pour fetcher la cotation live

3. **Déléguer à l'agent `brvm-stratege`** pour calculer le score /10 et produire le verdict

4. **Afficher le bloc d'analyse complet** (format défini dans `agents/stratege.md`)

5. **En fin de réponse**, si score ≥ 6/10 : proposer d'ajouter la valeur au portefeuille
   ```
   Ajouter [VALEUR] à ta watch list ? → réponds "oui, j'ai acheté [X] à [prix]"
   ```

## Exemples d'utilisation

```
/analyse SONATEL
/analyse BOA CI
/analyse orange
/analyse TTLC.ci
/analyse                  ← sans argument = palmarès du jour
```

## Raccourcis reconnus

L'agent reconnaît les noms courants sans ticker exact :

| Ce que tu tapes | Ticker résolu |
|-----------------|---------------|
| sonatel | SNTS.sn |
| boa ci / boa côte d'ivoire | BOAC.ci |
| orange ci | ORAC.ci |
| total ci | TTLC.ci |
| ecobank | ECOC.ci |
| sg ci / société générale | SGBC.ci |
| sib | SIBC.ci |
| coris | CBIBF.bf |
| nsia | NSBC.ci |
| boa bf / boa burkina | BOABF.bf |
| boa sn / boa sénégal | BOAS.sn |
| palmci | PALMC.ci |
| saph | SAPHC.ci |
