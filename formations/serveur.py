#!/usr/bin/env python3
"""
Serveur local de la formation BRVM.
Double-clique sur BRVM_Formation.command pour démarrer.
"""
import json, os, webbrowser, threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from datetime import date

BASE = Path(__file__).parent

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a): pass  # silencieux

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self._send_file(BASE / "app.html", "text/html")
        elif self.path == "/parcours":
            self._send_json(BASE / "parcours.json")
        elif self.path.startswith("/module/"):
            mid = self.path.replace("/module/", "")  # ex: "1.1"
            n = mid[0]
            slug = mid.replace(".", "_")
            folder = BASE / f"niveau{n}"
            matches = list(folder.glob(f"{slug}_*.md")) if folder.exists() else []
            if matches:
                self._send_text(matches[0])
            else:
                self._send(404, "text/plain", b"Module introuvable")
        else:
            self._send(404, "text/plain", b"Not found")

    def do_POST(self):
        if self.path == "/parcours":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            try:
                data = json.loads(body)
                data["derniere_activite"] = str(date.today())
                self._recalc(data)
                with open(BASE / "parcours.json", "w") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                self._send(200, "application/json", b'{"ok":true}')
            except Exception as e:
                self._send(500, "application/json", json.dumps({"error": str(e)}).encode())
        else:
            self._send(404, "text/plain", b"Not found")

    def _recalc(self, data):
        BADGES = {
            "niveau1_complete": "🏅 Initié BRVM",
            "niveau2_complete": "🥈 Analyste Junior",
            "niveau3_complete": "🏆 Stratège BRVM",
        }
        total, done = 0, 0
        for nk, nv in data["niveaux"].items():
            mods = nv["modules"]
            n_done = sum(1 for m in mods.values() if m["statut"] == "complete")
            n_total = len(mods)
            pct = round(n_done / n_total * 100) if n_total else 0
            nv["progression_pct"] = pct
            total += n_total
            done += n_done
            if pct == 100 and nv["statut"] not in ("verrouille",):
                nv["statut"] = "complete"
                badge = BADGES.get(f"{nk}_complete")
                if badge and badge not in data.get("badges", []):
                    data.setdefault("badges", []).append(badge)
            # Débloquer niveau suivant
            niveau_num = int(nk[-1])
            next_key = f"niveau{niveau_num + 1}"
            if pct == 100 and next_key in data["niveaux"] and data["niveaux"][next_key]["statut"] == "verrouille":
                data["niveaux"][next_key]["statut"] = "non_commence"
                for m in data["niveaux"][next_key]["modules"].values():
                    if m["statut"] == "verrouille":
                        m["statut"] = "non_commence"
        data["progression_globale_pct"] = round(done / total * 100) if total else 0

    def _send_file(self, path, ctype):
        try:
            content = Path(path).read_bytes()
            self._send(200, ctype, content)
        except FileNotFoundError:
            self._send(404, "text/plain", b"Fichier introuvable")

    def _send_json(self, path):
        self._send_file(path, "application/json")

    def _send_text(self, path):
        self._send_file(path, "text/plain; charset=utf-8")

    def _send(self, code, ctype, body):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)

def open_browser():
    import time; time.sleep(0.8)
    webbrowser.open("http://localhost:7777")

if __name__ == "__main__":
    threading.Thread(target=open_browser, daemon=True).start()
    print("Formation BRVM démarrée → http://localhost:7777")
    print("Ferme cette fenêtre pour arrêter le serveur.")
    HTTPServer(("localhost", 7777), Handler).serve_forever()
