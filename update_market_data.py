#!/usr/bin/env python3
"""
Script de mise à jour automatique des données marché BRVM
Lance via : python3 update_market_data.py
Fetche sikafinance.com et met à jour les fichiers de référence du skill brvm-trader
"""

import urllib.request
import urllib.error
import re
import json
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REFS_DIR = os.path.join(BASE_DIR, "brvm-trader", "references")
SKILL_REFS = os.path.expanduser("~/.claude/skills/brvm-trader/references")
TODAY = datetime.now().strftime("%d/%m/%Y")
NOW   = datetime.now().strftime("%d/%m/%Y à %H:%M")

TICKERS = {
    "SONATEL":    "SNTS.sn",
    "ORANGE CI":  "ORAC.ci",
    "BOA CI":     "BOAC.ci",
    "BOA BF":     "BOABF.bf",
    "BOA SN":     "BOAS.sn",
    "ECOBANK CI": "ECOC.ci",
    "SG CI":      "SGBC.ci",
    "TOTAL CI":   "TTLC.ci",
    "SIB CI":     "SIBC.ci",
    "CORIS BANK": "CBIBF.bf",
    "NSIA BANQUE":"NSBC.ci",
}

SOURCES = {
    "palmares":     "https://www.sikafinance.com/marches/palmares",
    "dividendes":   "https://www.sikafinance.com/marches/dividendes",
    "actualites":   "https://www.sikafinance.com/marches/actualites_bourse_brvm",
    "communiques":  "https://www.sikafinance.com/marches/communiques_brvm",
    "indices":      "https://www.sikafinance.com/marches/indices_afrique",
}

def fetch(url, timeout=15):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return f"[ERREUR FETCH: {e}]"

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✅ {os.path.basename(path)}")

def sync_to_claude_skills(filename):
    src = os.path.join(REFS_DIR, filename)
    dst = os.path.join(SKILL_REFS, filename)
    if os.path.exists(src):
        os.makedirs(SKILL_REFS, exist_ok=True)
        import shutil
        shutil.copy2(src, dst)

def run():
    print(f"\n🔄 MISE À JOUR DONNÉES BRVM — {NOW}\n")

    # ── 1. Fetch toutes les sources ──────────────────────────────────────────
    print("📡 Fetch des sources sikafinance.com...")
    raw = {}
    for name, url in SOURCES.items():
        print(f"   → {url}")
        raw[name] = fetch(url)

    cotations = {}
    for name, ticker in TICKERS.items():
        url = f"https://www.sikafinance.com/marches/cotation_{ticker}"
        print(f"   → {url}")
        cotations[name] = fetch(url)

    # ── 2. Mettre à jour market_snapshot.md ─────────────────────────────────
    print("\n📝 Mise à jour market_snapshot.md...")

    snapshot_lines = [
        f"# Snapshot Marché BRVM — Mis à jour le {NOW}",
        f"## Source : sikafinance.com (fetch automatique)\n",
        f"> ⚠️ Ces données ont été fetchées automatiquement. Toujours vérifier sur sikafinance.com avant toute décision.\n",
        "---\n",
        "## Cotations individuelles (données brutes fetchées)\n",
    ]

    for name, html in cotations.items():
        ticker = TICKERS[name]
        snapshot_lines.append(f"### {name} ({ticker})")
        # Extraire des patterns de cours depuis le HTML
        cours_match = re.findall(r'(\d[\d\s]{2,8})\s*(?:XOF|FCFA|xof)', html, re.IGNORECASE)
        rsi_match   = re.findall(r'RSI[^:]*:\s*([\d.]+)', html, re.IGNORECASE)
        beta_match  = re.findall(r'[Bb]eta[^:]*:\s*([\d.]+)', html, re.IGNORECASE)
        var_match   = re.findall(r'([+-][\d.]+)\s*%', html)

        if cours_match:
            snapshot_lines.append(f"- Cours trouvé : {cours_match[0].strip()} FCFA")
        if rsi_match:
            snapshot_lines.append(f"- RSI : {rsi_match[0]}")
        if beta_match:
            snapshot_lines.append(f"- Beta : {beta_match[0]}")
        if var_match:
            snapshot_lines.append(f"- Variations détectées : {', '.join(var_match[:5])}")

        fetch_status = "✅ Fetch OK" if "[ERREUR" not in html else f"❌ {html[:80]}"
        snapshot_lines.append(f"- Statut fetch : {fetch_status}")
        snapshot_lines.append(f"- URL source : https://www.sikafinance.com/marches/cotation_{ticker}\n")

    snapshot_lines += [
        "---\n",
        "## Sources complémentaires\n",
        f"- Palmarès : https://www.sikafinance.com/marches/palmares",
        f"- Dividendes : https://www.sikafinance.com/marches/dividendes",
        f"- Actualités : https://www.sikafinance.com/marches/actualites_bourse_brvm",
        f"- Communiqués : https://www.sikafinance.com/marches/communiques_brvm",
        f"- Indices africains : https://www.sikafinance.com/marches/indices_afrique\n",
        "---\n",
        "## Règle absolue pour l'analyse",
        "> **Ne jamais utiliser ce fichier seul pour une décision de trading.**",
        "> Toujours re-fetcher les URLs ci-dessus au moment de l'analyse pour avoir les données les plus récentes.",
        "> Ce fichier sert uniquement de cache de contexte entre les sessions.",
    ]

    snapshot_content = "\n".join(snapshot_lines)
    snap_path = os.path.join(REFS_DIR, "market_snapshot.md")
    write_file(snap_path, snapshot_content)
    sync_to_claude_skills("market_snapshot.md")

    # ── 3. Mettre à jour data_freshness.json ────────────────────────────────
    print("\n📝 Mise à jour data_freshness.json...")
    freshness = {
        "last_update": NOW,
        "last_update_iso": datetime.now().isoformat(),
        "sources_fetched": list(SOURCES.keys()) + [f"cotation_{t}" for t in TICKERS.values()],
        "tickers_fetched": list(TICKERS.keys()),
        "fetch_errors": [
            name for name, html in {**raw, **cotations}.items()
            if "[ERREUR" in html
        ],
        "warning": "Toujours re-fetcher sikafinance.com avant toute analyse. Ce fichier indique QUAND les données ont été mises à jour, pas leur valeur exacte.",
        "urls": {
            "palmares":    "https://www.sikafinance.com/marches/palmares",
            "dividendes":  "https://www.sikafinance.com/marches/dividendes",
            "actualites":  "https://www.sikafinance.com/marches/actualites_bourse_brvm",
            "communiques": "https://www.sikafinance.com/marches/communiques_brvm",
            "indices":     "https://www.sikafinance.com/marches/indices_afrique",
        }
    }
    fresh_path = os.path.join(REFS_DIR, "data_freshness.json")
    write_file(fresh_path, json.dumps(freshness, ensure_ascii=False, indent=2))
    sync_to_claude_skills("data_freshness.json")

    # ── 4. Git commit + push ─────────────────────────────────────────────────
    print("\n📤 Git commit et push...")
    os.chdir(BASE_DIR)
    os.system('git add brvm-trader/references/market_snapshot.md brvm-trader/references/data_freshness.json')
    os.system(f'git commit -m "chore: mise à jour données marché BRVM — {NOW}" --allow-empty')
    os.system('git push origin main')

    print(f"\n✅ Mise à jour terminée — {NOW}")
    print("📌 Rappel : re-fetcher sikafinance.com au moment de chaque analyse pour les cours en temps réel.\n")

if __name__ == "__main__":
    run()
