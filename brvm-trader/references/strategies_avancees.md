# Stratégies Avancées — BRVM Trader
## Patterns, timing et techniques pour marché frontier

---

## 1. DIVERGENCES RSI — Signal le plus fiable sur la BRVM

Une divergence se produit quand le cours et le RSI vont dans des directions opposées.

### Divergence Haussière (signal d'achat)
```
Cours : fait un nouveau plus bas
RSI   : fait un plus bas MOINS profond que le précédent
→ Signal : la baisse s'essoufle → ACHAT imminent

Exemple visuel :
  Cours  :  ↘ ↘↘  (nouveau plus bas)
  RSI    :  ↘ ↗   (plus bas moins profond)
  Action :  🟢 ACHETER sur confirmation (bougie haussière)
```

### Divergence Baissière (signal de vente/prudence)
```
Cours : fait un nouveau plus haut
RSI   : fait un plus haut MOINS élevé que le précédent
→ Signal : la hausse s'essoufle → RÉDUIRE la position

Exemple visuel :
  Cours  :  ↗ ↗↗  (nouveau plus haut)
  RSI    :  ↗ ↘   (plus haut moins élevé)
  Action :  🔴 ALLÉGER ou PRENDRE des profits
```

---

## 2. GAPS DE COTATION — Spécificité BRVM

Sur un marché à faible liquidité comme la BRVM, les gaps sont fréquents et exploitables.

### Types de gaps
```
Gap haussier (ouverture > clôture veille) :
  - Avec fort volume  → Tendance forte, suivre 🟢
  - Sans volume       → Faux signal, attendre ⚠️

Gap baissier (ouverture < clôture veille) :
  - Souvent lié à news négative → vérifier communiqués
  - Peut être point d'entrée si fondamentaux intacts
```

### Règle du "gap fill"
Sur la BRVM, ~60% des gaps sont comblés dans les 5–10 séances suivantes.
Si un gap monte fort sans raison fondamentale → attendre le retour au niveau précédent pour acheter.

---

## 3. SAISONNALITÉ BRVM — Le calendrier du trader

### T1 (Janvier – Mars) : Saison des résultats annuels
```
✅ Moment favorable : publications des résultats 2025
✅ AG convoquées → annonces dividendes
✅ Historiquement haussier (+5 à +15% sur le BRVM Composite)
Action : Renforcer les positions en janvier, avant la publication des résultats
```

### T2 (Avril – Juin) : Saison des dividendes
```
✅ Détachements de dividendes (BOA BF avr, SONATEL mai, BOA SN mai)
⚠️ Baisses post-détachement fréquentes (cours - montant dividende)
Action : Encaisser le dividende, réinvestir immédiatement sur les baisses
```

### T3 (Juillet – Septembre) : Creux estival
```
⚠️ Volumes faibles, peu d'activité
⚠️ Marché souvent flat ou légèrement baissier
Action : Période idéale pour accumuler à bon prix, pas de ventes précipitées
```

### T4 (Octobre – Décembre) : Rebond de fin d'année
```
✅ "Rallye de fin d'année" souvent présent
✅ Anticipation des résultats T3 et publications annuelles
Action : Renforcer en octobre pour profiter du rallye novembre-décembre
```

---

## 4. TRADING AUTOUR DES DIVIDENDES — La stratégie complète

### Phase 1 : Accumulation (J-20 à J-5 avant détachement)
- Acheter progressivement en DCA
- Le cours monte souvent en anticipation du dividende

### Phase 2 : Détachement (Jour J)
- Le cours baisse d'un montant ≈ dividende (ex-dividende)
- C'est NORMAL — tu reçois le cash sur ton compte

### Phase 3 : Post-détachement (J+1 à J+15)
- Certains investisseurs vendent → pression baissière supplémentaire
- Opportunité d'achat supplémentaire si fondamentaux solides

### Phase 4 : Réinvestissement
- Réinvestir le dividende reçu dès réception sur les mêmes titres ou sur une valeur en correction

### Calcul du rendement total (Total Return)
```
Rendement total = (Prix de vente - Prix d'achat + Dividendes reçus) / Prix d'achat

Exemple SONATEL :
  Achat à 28 400 FCFA
  Dividende reçu : 1 740 FCFA
  Cours dans 1 an : 32 000 FCFA
  Rendement = (32 000 - 28 400 + 1 740) / 28 400 = +18.8%
```

---

## 5. ANALYSE DES VOLUMES — Confirmation des signaux

### Ratio Volume / Moyenne (calculé manuellement sur sikafinance)
```
Volume du jour / Volume moyen 20 jours = Ratio

Ratio > 2x  → Événement majeur (résultats, dividende, OPA) → Signal fort
Ratio 1–2x  → Signal normal, crédible
Ratio < 0.5x → Journée sans conviction, ignorer le mouvement
```

### Accumulation silencieuse
Signe que les "mains fortes" (institutionnels) accumulent :
```
✅ Cours stable ou légèrement haussier
✅ Volume progressivement croissant sur plusieurs semaines
✅ Pas d'actualité particulière
→ Anticiper un mouvement haussier → Accumuler avec eux
```

---

## 6. GESTION DE POSITION — PYRAMIDING (pour profils intermédiaires)

Technique pour renforcer une position gagnante sans sur-exposer.

```
Position initiale : 50% du montant prévu
  → Si +8%  : Ajouter 30% du montant prévu
  → Si +15% : Ajouter les 20% restants
  → Stop-loss global : -10% du prix moyen d'entrée

Exemple sur BOA CI :
  Entrée 1 : 87 500 FCFA à 8 700 FCFA
  Entrée 2 : 52 500 FCFA à 9 396 FCFA (+8%)
  Entrée 3 : 35 000 FCFA à 10 005 FCFA (+15%)
  Prix moyen : ~9 100 FCFA
  Stop-loss  : ~8 190 FCFA (-10%)
```

---

## 7. RISQUES SPÉCIFIQUES BRVM À TOUJOURS SURVEILLER

### Risque de liquidité (le plus dangereux sur la BRVM)
- Sur les petites caps, il peut ne pas y avoir d'acheteur quand tu veux vendre
- Règle : Ne jamais acheter une valeur dont le volume quotidien < 5 fois ta position

### Risque politique (zone UEMOA)
- Coups d'État au Burkina Faso, Mali, Niger → impact direct sur les BOA de ces pays
- Diversifier entre CI, SN et BF pour réduire l'exposition

### Risque de concentration sectorielle
- Le secteur bancaire = ~55% de la capitalisation BRVM
- Avoir au moins 1 valeur hors banque (SONATEL, TOTAL CI, PALMCI)

### Risque de change indirect
- Le FCFA est arrimé à l'Euro → risque faible
- Mais si l'arrimage venait à changer → impact majeur sur tous les actifs

### Risque règlementaire CREPMF
- Suspension de cotation possible (rare mais arrive)
- Toujours vérifier les communiqués officiels avant d'investir une grosse somme

---

## 8. CHECKLIST COMPLÈTE AVANT TOUT ACHAT

```
ANALYSE TECHNIQUE
□ RSI entre 30 et 65 ?
□ Beta < 1.0 (pour débutant) ?
□ Volume du jour ≥ moyenne ?
□ Tendance 1 mois positive ou neutre ?
□ Pas de divergence baissière en cours ?

ANALYSE FONDAMENTALE
□ Dividende régulier et yield > 4% ?
□ Bénéfices stables ou croissants sur 3 ans ?
□ Capitalisation > 150 Mds FCFA ?
□ Groupe actionnaire solide ?
□ Pas de profit warning récent ?

ACTUALITÉS
□ Pas d'AG extraordinaire suspecte ?
□ Pas de changement de direction récent ?
□ Pas de litige ou enquête CREPMF ?
□ Pas de dette problématique publiée ?

GESTION DU RISQUE
□ Stop-loss défini AVANT l'achat ?
□ Position < 40% du portefeuille total ?
□ Liquidités restantes > 10% après l'achat ?
□ Volume quotidien > 5x la taille de ma position ?
□ Pas de tranche DCA 2 avant 6 semaines si tranche 1 fraîche ?
```
