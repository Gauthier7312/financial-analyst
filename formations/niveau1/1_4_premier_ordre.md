# Module 1.4 — Comment passer son premier ordre ?

> **Durée estimée :** 45 min | **Niveau :** Débutant | **Statut :** `python tracker.py start 1.4`

---

## Les 3 types d'ordres sur la BRVM

### Ordre au Marché (ou "Au mieux")
Tu achètes ou vends **au prix disponible immédiatement**.
- ✅ Exécution quasi-certaine
- ❌ Tu ne maîtrises pas le prix exact

### Ordre à Cours Limité
Tu fixes le **prix maximum que tu acceptes de payer** (achat) ou le minimum
que tu acceptes de recevoir (vente).
- ✅ Tu maîtrises ton prix d'entrée/sortie
- ❌ L'ordre peut ne pas s'exécuter si le cours ne touche pas ta limite

### Ordre à Seuil de Déclenchement (Stop)
L'ordre ne s'active que quand le cours franchit un seuil.
Utilisé principalement pour les **stop-loss** (protection).

---

## Exemple concret : Acheter SONATEL

**Situation :** SONATEL cote 28 400 FCFA. Tu veux acheter 5 actions.

**Option A — Ordre au Marché**
```
Tu envoies à ta SGI : "Acheter 5 SONATEL au marché"
→ Exécution immédiate à ~28 400 FCFA
→ Coût total : 5 × 28 400 + frais = ~143 340 FCFA
```

**Option B — Ordre à Cours Limité**
```
Tu envoies : "Acheter 5 SONATEL limite 28 000 FCFA"
→ Si le cours baisse à 28 000, l'ordre s'exécute
→ Si ça ne baisse pas, ton argent reste disponible
```

**Recommandation débutant :** Toujours utiliser les ordres à cours limité.
Tu gardes le contrôle de ton prix d'entrée.

---

## Les étapes pour passer ton premier ordre

### Étape 1 — Ouvrir un compte SGI
Documents généralement requis :
- Pièce d'identité valide (CNI, passeport)
- Justificatif de domicile (moins de 3 mois)
- Formulaire de profil investisseur
- Dépôt initial (variable selon la SGI)

### Étape 2 — Alimenter ton compte espèces
Virement bancaire ou dépôt en agence sur ton compte de trading.
Le solde doit couvrir : montant de l'achat + frais de courtage.

### Étape 3 — Identifier la valeur
Chercher le **ticker** (code de la valeur) sur sikafinance.com.
Exemples : SNTS.sn (SONATEL), BOAC.ci (BOA CI), TTLC.ci (TOTAL CI)

### Étape 4 — Vérifier avant d'acheter (checklist)
```
☐ Le marché est ouvert ? (9h–15h30 GMT)
☐ J'ai vérifié le cours actuel sur sikafinance ?
☐ Mon solde couvre l'achat + frais ?
☐ J'ai fixé mon stop-loss (prix de sortie en cas de perte) ?
☐ Je ne mets pas plus de 40% de mon capital sur une seule valeur ?
```

### Étape 5 — Passer l'ordre
Via l'app SGI, le site web, ou par téléphone au chargé de compte.

### Étape 6 — Confirmer et archiver
Garde une trace de chaque ordre passé (date, valeur, quantité, prix, frais).

---

## La gestion du stop-loss dès le départ

Le stop-loss est ton filet de sécurité. **Le définir avant d'acheter**, jamais après.

```
Tu achètes SONATEL à 28 400 FCFA
→ Stop-loss débutant = -15% = 24 140 FCFA
→ Si SONATEL tombe à 24 140, tu vends automatiquement

Perte maximale sur 5 actions = 5 × (28 400 - 24 140) = 21 300 FCFA
```

Acceptes-tu cette perte potentielle avant d'acheter ? Si non → investis moins.

---

## Erreurs classiques du premier ordre

| Erreur | Comment l'éviter |
|---|---|
| Acheter sans avoir lu les résultats de la société | Lire au moins le dividende et la capitalisation |
| Passer un ordre au marché sans vérifier le carnet | Utiliser un ordre limité |
| Investir tout d'un coup | Stratégie DCA : 2 tranches minimum |
| Ne pas noter son prix de revient réel (avec frais) | Tenir un journal de trades |
| Vérifier le cours 10x par jour | Check hebdomadaire maximum |

---

## Exercice pratique (sans argent réel)

Simule ton premier achat :

1. Va sur `sikafinance.com/marches/cotation_SNTS.sn`
2. Note le cours actuel de SONATEL
3. Calcule : si tu achètes 3 actions avec un courtage à 0.8%, quel est ton coût total ?
4. Définis ton stop-loss à -15%
5. Note ta "transaction simulée" dans le journal :
   ```bash
   python tracker.py log "Simulation achat 3 SONATEL à 28400 — stop 24140 — coût 86 681 FCFA"
   ```

---

## Quiz de vérification

1. Quelle est la différence entre un ordre au marché et un ordre à cours limité ?
2. Tu veux acheter BOA CI à maximum 8 500 FCFA. Quel type d'ordre utilises-tu ?
3. Si BOA CI cote 8 700 FCFA et que tu poses un stop-loss à -12%, à quel prix fixes-tu ton stop ?
4. Cite 3 documents nécessaires pour ouvrir un compte SGI.
5. Pourquoi faut-il définir le stop-loss AVANT de passer l'ordre d'achat ?

```bash
python tracker.py quiz 1.4 <ton_score>
```

---

## Prochaine étape

➡️ Module 1.5 — Quiz de validation Niveau 1
```bash
python tracker.py done 1.4
python tracker.py start 1.5
```
