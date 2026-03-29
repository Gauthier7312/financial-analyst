#!/usr/bin/env python3
"""
BRVM Formation Tracker — Suivi interactif du parcours apprenant
Usage:
  python tracker.py status              → Affiche le tableau de bord
  python tracker.py start <module>      → Démarre un module (ex: 1.1)
  python tracker.py done <module>       → Marque un module comme complété
  python tracker.py quiz <module> <score> → Enregistre le score d'un quiz
  python tracker.py note <module> "texte" → Ajoute une note sur un module
  python tracker.py log "texte"         → Ajoute une entrée dans le journal
  python tracker.py unlock <niveau>     → Déverrouille un niveau (2 ou 3)
"""

import json
import sys
from datetime import date
from pathlib import Path

PARCOURS_FILE = Path(__file__).parent / "parcours.json"

STATUTS = {
    "non_commence": "⬜",
    "en_cours":     "🟡",
    "complete":     "✅",
    "verrouille":   "🔒"
}

BADGES = {
    "niveau1_complete": "🏅 Initié BRVM",
    "niveau2_complete": "🥈 Analyste Junior",
    "niveau3_complete": "🏆 Stratège BRVM",
    "premier_quiz":     "🎯 Premier Quiz",
    "note_assidu":      "📝 Apprenant Assidu",
}


def load():
    with open(PARCOURS_FILE) as f:
        return json.load(f)


def save(data):
    data["derniere_activite"] = str(date.today())
    _recalc(data)
    with open(PARCOURS_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("✓ Parcours sauvegardé.")


def _recalc(data):
    total, done = 0, 0
    for nk, nv in data["niveaux"].items():
        mods = nv["modules"]
        n_done = sum(1 for m in mods.values() if m["statut"] == "complete")
        n_total = len(mods)
        pct = round(n_done / n_total * 100) if n_total else 0
        nv["progression_pct"] = pct
        total += n_total
        done += n_done
        if pct == 100 and nv["statut"] != "verrouille":
            nv["statut"] = "complete"
            badge_key = f"{nk}_complete"
            if badge_key in BADGES and BADGES[badge_key] not in data["badges"]:
                data["badges"].append(BADGES[badge_key])
                print(f"\n🎉 Nouveau badge débloqué : {BADGES[badge_key]}")
    data["progression_globale_pct"] = round(done / total * 100) if total else 0


def _find_module(data, mid):
    for nk, nv in data["niveaux"].items():
        if mid in nv["modules"]:
            return nv["modules"][mid], nv
    return None, None


def cmd_status(data):
    print(f"\n{'═'*52}")
    print(f"  📚 BRVM Formation — Tableau de Bord")
    print(f"  Apprenant : {data['apprenant']}  |  Depuis : {data['debut_formation']}")
    print(f"  Dernière activité : {data['derniere_activite']}")
    print(f"{'═'*52}")

    bar_filled = int(data["progression_globale_pct"] / 5)
    bar = "█" * bar_filled + "░" * (20 - bar_filled)
    print(f"\n  Progression globale : [{bar}] {data['progression_globale_pct']}%\n")

    for nk, nv in data["niveaux"].items():
        lock = "🔒 " if nv["statut"] == "verrouille" else ""
        print(f"  {lock}{nv['titre']} — {nv['progression_pct']}%")
        for mid, mod in nv["modules"].items():
            icon = STATUTS.get(mod["statut"], "?")
            score = f" [{mod['score_quiz']}/10]" if mod["score_quiz"] is not None else ""
            print(f"    {icon} {mid}. {mod['titre']}{score}")
        print()

    if data["badges"]:
        print(f"  Badges : {' '.join(data['badges'])}")
    print(f"{'═'*52}\n")


def cmd_start(data, mid):
    mod, nv = _find_module(data, mid)
    if mod is None:
        print(f"❌ Module {mid} introuvable.")
        return
    if mod["statut"] == "verrouille":
        print(f"🔒 Ce module est verrouillé. Complète le niveau précédent d'abord.")
        return
    if mod["statut"] == "complete":
        print(f"✅ Module {mid} déjà complété.")
        return
    mod["statut"] = "en_cours"
    nv["statut"] = "en_cours"
    data["journal"].append({"date": str(date.today()), "event": f"Démarrage module {mid} : {mod['titre']}"})
    save(data)
    print(f"\n🟡 Module {mid} démarré : {mod['titre']}")
    print(f"   Ouvre le fichier : formations/niveau{mid[0]}/{mid.replace('.','_')}_*.md\n")


def cmd_done(data, mid):
    mod, nv = _find_module(data, mid)
    if mod is None:
        print(f"❌ Module {mid} introuvable.")
        return
    if mod["statut"] == "verrouille":
        print(f"🔒 Ce module est verrouillé.")
        return
    mod["statut"] = "complete"
    mod["date_completion"] = str(date.today())
    data["journal"].append({"date": str(date.today()), "event": f"Module {mid} complété : {mod['titre']}"})

    # Premier quiz badge
    if "quiz" in mod["titre"].lower() and "premier_quiz" not in [b for b in data["badges"]]:
        if BADGES["premier_quiz"] not in data["badges"]:
            data["badges"].append(BADGES["premier_quiz"])
            print(f"\n🎉 Badge débloqué : {BADGES['premier_quiz']}")

    save(data)
    print(f"\n✅ Module {mid} marqué comme complété !")
    _check_unlock(data, mid)


def _check_unlock(data, mid):
    niveau = int(mid[0])
    nv_key = f"niveau{niveau}"
    nv = data["niveaux"][nv_key]
    all_done = all(m["statut"] == "complete" for m in nv["modules"].values())
    if all_done:
        next_key = f"niveau{niveau + 1}"
        if next_key in data["niveaux"] and data["niveaux"][next_key]["statut"] == "verrouille":
            data["niveaux"][next_key]["statut"] = "non_commence"
            for m in data["niveaux"][next_key]["modules"].values():
                m["statut"] = "non_commence"
            save(data)
            print(f"\n🔓 Niveau {niveau + 1} déverrouillé ! Tu peux commencer {data['niveaux'][next_key]['titre']}.")


def cmd_quiz(data, mid, score_str):
    try:
        score = int(score_str)
        assert 0 <= score <= 10
    except:
        print("❌ Score invalide. Utilise un entier entre 0 et 10.")
        return
    mod, _ = _find_module(data, mid)
    if mod is None:
        print(f"❌ Module {mid} introuvable.")
        return
    mod["score_quiz"] = score
    data["journal"].append({"date": str(date.today()), "event": f"Quiz {mid} : {score}/10"})
    save(data)
    if score >= 7:
        print(f"\n✅ Score {score}/10 — Bien joué ! Tu peux valider ce module.")
        cmd_done(data, mid)
    else:
        print(f"\n⚠️  Score {score}/10 — Relis le module avant de continuer.")


def cmd_note(data, mid, texte):
    mod, _ = _find_module(data, mid)
    if mod is None:
        print(f"❌ Module {mid} introuvable.")
        return
    mod["notes"] = (mod["notes"] + "\n" + texte).strip()
    if BADGES["note_assidu"] not in data["badges"] and len(data["journal"]) >= 3:
        data["badges"].append(BADGES["note_assidu"])
        print(f"\n🎉 Badge débloqué : {BADGES['note_assidu']}")
    save(data)
    print(f"\n📝 Note ajoutée sur le module {mid}.")


def cmd_log(data, texte):
    data["journal"].append({"date": str(date.today()), "event": texte})
    save(data)
    print(f"\n📖 Journal mis à jour.")


def main():
    data = load()
    args = sys.argv[1:]

    if not args or args[0] == "status":
        cmd_status(data)
    elif args[0] == "start" and len(args) >= 2:
        cmd_start(data, args[1])
    elif args[0] == "done" and len(args) >= 2:
        cmd_done(data, args[1])
    elif args[0] == "quiz" and len(args) >= 3:
        cmd_quiz(data, args[1], args[2])
    elif args[0] == "note" and len(args) >= 3:
        cmd_note(data, args[1], " ".join(args[2:]))
    elif args[0] == "log" and len(args) >= 2:
        cmd_log(data, " ".join(args[1:]))
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
