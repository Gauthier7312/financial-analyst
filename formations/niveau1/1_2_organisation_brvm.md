# Module 1.2 — Organisation du marché BRVM

> **Durée estimée :** 45 min | **Niveau :** Débutant | **Statut :** `python tracker.py start 1.2`

---

## Qu'est-ce que la BRVM ?

La **Bourse Régionale des Valeurs Mobilières** est la bourse commune des 8 pays
de l'UEMOA (Union Économique et Monétaire Ouest Africaine).

```
Pays membres : Côte d'Ivoire, Sénégal, Burkina Faso, Mali,
               Bénin, Niger, Togo, Guinée-Bissau
Siège : Abidjan, Côte d'Ivoire
Fondée : 1998
Valeurs cotées : 80+
Volume quotidien : 3 à 10 milliards FCFA/jour
```

---

## Les horaires et règles du marché

| Règle | Détail |
|---|---|
| Horaires | 9h00 – 15h30 GMT (heure Abidjan) |
| Jours de cotation | Lundi au vendredi (hors jours fériés) |
| Variation max/séance | ±7,5% (coupe-circuit automatique) |
| Règlement des ordres | T+3 (3 jours ouvrables après l'ordre) |
| Devise | FCFA (arrimé Euro à 655,957) |

**T+3 signifie :** Si tu achètes une action un lundi, les titres arrivent dans
ton compte le jeudi. Il faut en tenir compte pour les dividendes.

---

## Les 3 grands acteurs du marché

### 1. Le CREPMF — Le gendarme
Le **Conseil Régional de l'Épargne Publique et des Marchés Financiers** régule
tout le marché. Il autorise les SGI, valide les émissions, protège les
investisseurs. Pense à lui comme à l'AMF en France ou la SEC aux USA.

### 2. La BRVM — La place de marché
Elle gère l'infrastructure : les cotations, les indices, la diffusion des
informations. Elle ne vend rien elle-même — elle est l'intermédiaire neutre.

### 3. Les SGI — Ton intermédiaire obligatoire
Les **Sociétés de Gestion et d'Intermédiation** sont les seules habilitées à
passer des ordres sur la BRVM. Tu ne peux pas acheter directement.

Exemples de SGI :
- SG Capital Securities WA (Société Générale)
- BICI Bourse
- CGF Bourse
- Coris Bourse
- ARM Securities

---

## Les 2 marchés de la BRVM

### Marché Principal
Pour les grandes capitalisations (SONATEL, BOA CI, ORANGE CI, etc.).
Conditions d'admission strictes. Liquidité meilleure.

### Marché Alternatif (depuis 2017)
Pour les PME. Conditions allégées. Moins liquide mais rendements potentiels
plus élevés. Exemple : BERNABE CI, SICOR CI.

---

## Les indices BRVM

Un **indice** est un panier de valeurs qui sert de baromètre du marché.

| Indice | Composition | Rôle |
|---|---|---|
| **BRVM Composite** | Toutes les valeurs cotées | Baromètre général |
| **BRVM 30** | 30 premières capitalisations | Valeurs de référence |
| **BRVM Prestige** | Top 15 liquides | Valeurs premiums |

**Performance au 28/03/2026 :**
- BRVM Composite : **+17.48% YTD** | **+42% sur 1 an**

---

## Le circuit d'un ordre d'achat

```
Toi
  ↓ (ordre passé via app/téléphone/mail)
SGI (vérifie ton solde, envoie l'ordre)
  ↓
BRVM (confronte ton ordre d'achat avec un ordre de vente)
  ↓
Match trouvé → Transaction exécutée
  ↓
DC/BR (Dépositaire Central) enregistre le transfert de titres
  ↓
J+3 → Titres dans ton compte, argent débité
```

---

## Concepts à retenir

| Terme | Définition simple |
|---|---|
| **UEMOA** | Union des 8 pays d'Afrique de l'Ouest partageant le FCFA |
| **SGI** | Seul intermédiaire autorisé à acheter/vendre sur la BRVM |
| **CREPMF** | Régulateur du marché financier UEMOA |
| **T+3** | Délai de 3 jours entre l'ordre et le règlement-livraison |
| **Indice** | Panier de valeurs mesurant la santé globale du marché |

---

## Quiz de vérification

1. Combien de pays composent la zone UEMOA ?
2. Que signifie T+3 concrètement pour un investisseur ?
3. Quelle est la variation maximale autorisée par séance sur la BRVM ?
4. Pourquoi ne peut-on pas acheter des actions directement sans passer par une SGI ?
5. Quelle est la différence entre le BRVM Composite et le BRVM 30 ?

```bash
python tracker.py quiz 1.2 <ton_score>
```

---

## Prochaine étape

➡️ Module 1.3 — Les acteurs : SGI, CREPMF, BRVM
```bash
python tracker.py done 1.2
python tracker.py start 1.3
```
