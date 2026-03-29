# Module 1.3 — Les acteurs : SGI, CREPMF, BRVM

> **Durée estimée :** 30 min | **Niveau :** Débutant | **Statut :** `python tracker.py start 1.3`

---

## Choisir sa SGI — Les critères

Toutes les SGI sont régulées par le CREPMF, mais elles diffèrent sur :

| Critère | Questions à poser |
|---|---|
| **Frais de courtage** | Quel % par transaction ? (standard : 0.6–1.2%) |
| **Frais de conservation** | Quel % par an sur tes titres ? (standard : 0.25%) |
| **Dépôt minimum** | Combien pour ouvrir un compte ? |
| **Interface** | App mobile ? Web ? Ou uniquement par téléphone ? |
| **Solidité** | Groupe bancaire international derrière ? |
| **Conseil** | Est-ce qu'ils t'accompagnent ou juste exécutent ? |

### Comparatif indicatif

| SGI | Courtage | Conservation | App mobile | Backing |
|---|---|---|---|---|
| SG Capital Securities | 0.8% | 0.25%/an | Oui | Société Générale France |
| BICI Bourse | 0.9% | 0.25%/an | Partiel | BNP Paribas |
| CGF Bourse | 0.7% | 0.25%/an | Non | Local CI |
| Coris Bourse | 0.8% | 0.25%/an | Oui | Coris Bank BF |

---

## Comprendre les frais réels d'un investissement

Exemple : Tu achètes 10 actions SONATEL à 28 400 FCFA via SG Capital.

```
Montant brut         : 284 000 FCFA
Courtage (0.8%)      :   2 272 FCFA
TVA sur courtage (18%):    409 FCFA
─────────────────────────────────────
Coût total réel      : 286 681 FCFA

Conservation annuelle (0.25%) : 710 FCFA/an
```

**Le prix de revient unitaire de tes actions = 28 668 FCFA** (pas 28 400).
Pour être à l'équilibre, SONATEL doit monter au-delà de 28 668 FCFA.

---

## Le CREPMF — Ce qu'il fait concrètement

- Autorise et surveille les SGI (peut retirer la licence)
- Approuve les introductions en bourse (IPO)
- Valide les émissions obligataires des États
- Sanctionne les délits d'initiés
- Publie des alertes sur les sociétés en difficulté

**Ce qu'il ne fait pas :** Il ne garantit pas que tes investissements
seront rentables. Il garantit que les règles du jeu sont respectées.

---

## Le rôle du Dépositaire Central (DC/BR)

Quand tu achètes une action, tu n'as pas un bout de papier entre les mains.
Les titres sont **dématérialisés** et conservés chez le DC/BR.

Ton relevé de portefeuille chez ta SGI est la preuve de ta propriété.

---

## Les émetteurs — Qui lève de l'argent sur la BRVM ?

### Actions (capital)
Les entreprises lèvent des fonds en émettant des actions (IPO ou augmentation de capital).
Exemples : SONATEL, BOA CI, ORANGE CI, TOTAL CI, PALMCI, SAPH...

### Obligations (dette)
Les États et entreprises empruntent en émettant des obligations.
Exemples : OAT Côte d'Ivoire, Obligations SONATEL, BOAD...

---

## Concepts à retenir

| Terme | Définition simple |
|---|---|
| **Courtage** | Commission prélevée par la SGI à chaque transaction |
| **Conservation** | Frais annuels pour garder tes titres en portefeuille |
| **DC/BR** | Dépositaire Central — conserve électroniquement les titres |
| **IPO** | Introduction en Bourse — première fois qu'une action est cotée |
| **Délit d'initié** | Utiliser une info confidentielle pour trader — illégal |

---

## Quiz de vérification

1. Si tu achètes pour 500 000 FCFA d'actions avec un courtage à 0.8%, combien paies-tu de frais ?
2. Cite 3 critères pour choisir une SGI.
3. Quel est le rôle du DC/BR ?
4. Quelle est la différence entre une action et une obligation ?
5. Le CREPMF garantit-il la rentabilité des investissements ? Justifie.

```bash
python tracker.py quiz 1.3 <ton_score>
```

---

## Prochaine étape

➡️ Module 1.4 — Comment passer son premier ordre ?
```bash
python tracker.py done 1.3
python tracker.py start 1.4
```
