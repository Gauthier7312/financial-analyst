# Module 3.2 — Gestion du Risque & Stop-Loss

> **Durée estimée :** 45 min | **Niveau :** Avancé | **Statut :** `python tracker.py start 3.2`

---

## La règle numéro 1 en bourse

> "Ne jamais perdre d'argent." — Warren Buffett
> (Règle n°2 : Ne jamais oublier la règle n°1.)

La gestion du risque n'est pas une option — c'est **la compétence centrale** de tout investisseur.

---

## Le Stop-Loss — Ton filet de sécurité

Un stop-loss est un niveau de prix prédéfini auquel tu vends automatiquement
pour limiter tes pertes.

### Niveaux recommandés

| Profil | Stop-Loss |
|---|---|
| Débutant | -12% à -15% |
| Intermédiaire | -10% |
| Actif/Trader | -7% |

### Calcul concret

```
Achat BOA CI à 8 700 FCFA — Profil débutant
Stop-Loss = 8 700 × (1 - 0.15) = 7 395 FCFA

Si BOA CI tombe à 7 395 FCFA → Tu vends. Sans discussion.
Perte réalisée = (8 700 - 7 395) × nombre d'actions
```

### Le stop-loss mental vs le stop-loss réel

**Stop mental :** Tu te dis "je vendrai si ça tombe à X". Problème : dans le
stress, tu ne vends pas. Tu attends. Tu espères. La perte s'aggrave.

**Stop réel :** Tu passes un ordre de vente à seuil de déclenchement chez ta SGI.
Exécution automatique, sans émotion.

→ Toujours utiliser un stop réel si ta SGI le permet.

---

## La Règle des 2% (gestion de position)

Ne jamais risquer plus de 2% de ton capital total sur une seule position.

```
Capital : 500 000 FCFA
Risque max par trade : 500 000 × 2% = 10 000 FCFA

Si tu achètes TOTAL CI à 2 975 FCFA avec stop à 2 529 FCFA (-15%) :
  Risque par action = 2 975 - 2 529 = 446 FCFA
  Nombre max d'actions = 10 000 / 446 = 22 actions
  Montant de la position = 22 × 2 975 = 65 450 FCFA (13% du capital)
```

Cette règle garantit que même 5 pertes consécutives ne ruinent pas ton portefeuille.

---

## La Règle de Liquidité BRVM

La BRVM est un marché peu liquide. Avant d'entrer en position :

```
Montant de ta position / Volume quotidien moyen < 20%

Exemple : Volume quotidien TOTAL CI = 9 700 000 FCFA
Position max = 9 700 000 × 20% = 1 940 000 FCFA

Si tu veux mettre 2M+ sur TOTAL CI → risque de ne pas pouvoir vendre rapidement
```

**Pour un capital de 500 000 FCFA :** Ce problème ne se pose généralement pas
sur les grandes capitalisations (SONATEL, BOA CI, ORANGE CI).

---

## Les 5 risques spécifiques à la BRVM

### 1. Risque pays
Les événements politiques impactent les valeurs nationales.
```
Instabilité au Mali → Valeurs maliennes (BOA ML) sous pression
Coup d'État au Burkina → BOA BF impacté temporairement
```
**Mitigation :** Diversifier sur plusieurs pays de l'UEMOA.

### 2. Risque de liquidité
Sur les petites valeurs, tu peux ne pas trouver acheteur quand tu veux vendre.
**Mitigation :** Rester sur les grandes caps (SONATEL, BOA CI, ORANGE CI).

### 3. Risque de concentration sectorielle
Si tu mets tout dans les banques et que le secteur bancaire UEMOA traverse une crise...
**Mitigation :** Diversifier sur 2–3 secteurs différents.

### 4. Risque d'information
La BRVM a moins de transparence que les marchés développés.
Les résultats peuvent arriver tardivement ou être peu détaillés.
**Mitigation :** Lire les communiqués CREPMF et suivre sikafinance.com.

### 5. Risque émotionnel
Le plus sous-estimé. Panique lors d'une baisse → vente au pire moment.
Euphorie lors d'une hausse → achat au pire moment.
**Mitigation :** Respecter son plan, ne pas vérifier le cours chaque heure.

---

## Le Journal de Trading — Ton meilleur outil de progrès

Note chaque décision :
```
Date    : 28/03/2026
Action  : SONATEL SNTS.sn
Type    : Achat simulé
Prix    : 28 400 FCFA
Qté     : 7 actions
Montant : 200 628 FCFA (frais inclus)
Stop    : 24 140 FCFA
Objectif: 32 000 FCFA
Raison  : RSI 49.55 (zone saine) + dividende 6.13% avant 15/05 + PER 6.9x
```

```bash
python tracker.py log "Simulation achat SONATEL 28400 FCFA — stop 24140 — objectif 32000 — RSI 49.55 — dividende 22/05"
```

---

## Quiz de vérification

1. Tu achètes PALMCI à 8 200 FCFA avec un profil débutant. Quel est ton stop-loss ?
2. C'est quoi la règle des 2% ? Applique-la pour un capital de 300 000 FCFA.
3. Cite 3 risques spécifiques à la BRVM et comment les mitiger.
4. Pourquoi un stop mental est-il moins fiable qu'un stop réel ?
5. Pourquoi faut-il tenir un journal de trading ?

```bash
python tracker.py quiz 3.2 <ton_score>
```
