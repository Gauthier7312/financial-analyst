# Formation BRVM — Parcours Complet

Basé sur le programme sikafinance.com/formations — enrichi avec données live et skill BRVM Trader.

## Démarrage rapide

```bash
# Voir ton tableau de bord
python formations/tracker.py status

# Démarrer le premier module
python formations/tracker.py start 1.1

# Après avoir lu le module, enregistrer ton score
python formations/tracker.py quiz 1.1 8

# Valider et passer au suivant
python formations/tracker.py done 1.1
python formations/tracker.py start 1.2
```

## Structure des 3 niveaux

| Niveau | Titre | Durée | Déblocage |
|---|---|---|---|
| 1 | Initiation à la Bourse & BRVM | 4h | Disponible |
| 2 | Analyser et choisir ses actions | 5h | Quiz N1 ≥ 7/10 |
| 3 | Stratégies d'investissement | 5h | Quiz N2 ≥ 7/10 |

## Commandes disponibles

| Commande | Effet |
|---|---|
| `tracker.py status` | Tableau de bord complet |
| `tracker.py start 1.1` | Démarre le module 1.1 |
| `tracker.py done 1.1` | Valide le module 1.1 |
| `tracker.py quiz 1.1 8` | Enregistre score 8/10 au quiz du module 1.1 |
| `tracker.py note 1.1 "texte"` | Ajoute une note personnelle |
| `tracker.py log "texte"` | Entrée dans le journal de formation |
