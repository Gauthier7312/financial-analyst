from openpyxl import Workbook
from openpyxl.styles import (Font, PatternFill, Alignment, Border, Side,
                              GradientFill)
from openpyxl.utils import get_column_letter
from openpyxl.styles.numbers import FORMAT_PERCENTAGE_00
import datetime

wb = Workbook()

# ── Palette ──────────────────────────────────────────────────────────────────
DARK_GREEN   = "1A5276"
MID_GREEN    = "1E8449"
LIGHT_GREEN  = "D5F5E3"
GOLD         = "F1C40F"
DARK_GOLD    = "9A7D0A"
ORANGE_BG    = "FDEBD0"
BLUE_INPUT   = "0000FF"
BLACK        = "000000"
WHITE        = "FFFFFF"
GREY_BG      = "F2F3F4"
RED_ALERT    = "E74C3C"
LIGHT_BLUE   = "D6EAF8"
HEADER_BLUE  = "1A3A5C"

def thin_border():
    s = Side(style="thin", color="AAAAAA")
    return Border(left=s, right=s, top=s, bottom=s)

def header_font(sz=11, bold=True, color=WHITE):
    return Font(name="Arial", size=sz, bold=bold, color=color)

def body_font(sz=10, bold=False, color=BLACK):
    return Font(name="Arial", size=sz, bold=bold, color=color)

def fill(hex_color):
    return PatternFill("solid", fgColor=hex_color)

def center():
    return Alignment(horizontal="center", vertical="center", wrap_text=True)

def left():
    return Alignment(horizontal="left", vertical="center", wrap_text=True)

def style_header_row(ws, row, cols, bg=DARK_GREEN, fg=WHITE, sz=11):
    for c in cols:
        cell = ws.cell(row=row, column=c)
        cell.font = header_font(sz=sz, color=fg)
        cell.fill = fill(bg)
        cell.alignment = center()
        cell.border = thin_border()

def style_data_row(ws, row, cols, bg=WHITE, bold=False, color=BLACK):
    for c in cols:
        cell = ws.cell(row=row, column=c)
        cell.font = body_font(bold=bold, color=color)
        cell.fill = fill(bg)
        cell.alignment = center()
        cell.border = thin_border()

def set_col_widths(ws, widths):
    for col_letter, width in widths.items():
        ws.column_dimensions[col_letter].width = width

def merge_title(ws, cell_range, text, bg=DARK_GREEN, fg=WHITE, sz=14):
    ws.merge_cells(cell_range)
    top_cell = ws[cell_range.split(":")[0]]
    top_cell.value = text
    top_cell.font = Font(name="Arial", size=sz, bold=True, color=fg)
    top_cell.fill = fill(bg)
    top_cell.alignment = center()


# ══════════════════════════════════════════════════════════════════════════════
# SHEET 1 — PROFIL INVESTISSEUR
# ══════════════════════════════════════════════════════════════════════════════
ws1 = wb.active
ws1.title = "🧑 Profil Investisseur"
ws1.row_dimensions[1].height = 40
ws1.row_dimensions[2].height = 20

merge_title(ws1, "A1:F1", "PROFIL INVESTISSEUR — SESSION DU 28 MARS 2026", sz=14)
merge_title(ws1, "A2:F2", "BRVM · Bourse Régionale des Valeurs Mobilières · Zone UEMOA", bg=MID_GREEN, sz=11)

# Section identité
headers = ["Paramètre", "Valeur", "Commentaire"]
row = 4
ws1.cell(row=row, column=1).value = "INFORMATIONS GÉNÉRALES"
ws1.merge_cells(f"A{row}:F{row}")
ws1.cell(row=row, column=1).font = Font(name="Arial", size=11, bold=True, color=WHITE)
ws1.cell(row=row, column=1).fill = fill(HEADER_BLUE)
ws1.cell(row=row, column=1).alignment = center()

data_profil = [
    ("Date de la session",      "28 mars 2026",                   "Données live récupérées sur sikafinance.com"),
    ("Profil investisseur",     "Débutant",                       "Première expérience boursière"),
    ("Capital disponible",      "500 000 FCFA",                   "Montant confirmé pour investissement"),
    ("Horizon minimum",         "2 à 3 ans",                      "Ne pas toucher l'argent avant cette échéance"),
    ("Stratégie retenue",       "DCA (Achat progressif)",         "2 tranches : 300K maintenant + 200K dans 6 semaines"),
    ("Marché cible",            "BRVM (Zone UEMOA)",              "Bourse Régionale des Valeurs Mobilières"),
    ("SGI choisie",             "SG Capital Securities WA",       "Meilleur rapport coût/sécurité pour un débutant"),
    ("Dépôt minimum SGI",       "0 FCFA",                         "Aucune barrière d'entrée"),
    ("Courtage SGI",            "0,80%",                          "Moins cher que Bridge (1%) et BOA (1%)"),
    ("Conservation SGI",        "0,25%/an",                       "Frais de détention annuels"),
    ("Tenue de compte SGI",     "2 500 FCFA/trimestre",           "= 10 000 FCFA/an"),
    ("Backing SGI",             "Société Générale France",        "Top 10 banques européennes — risque dépositaire quasi nul"),
]

for i, (param, val, comment) in enumerate(data_profil):
    r = i + 5
    ws1.row_dimensions[r].height = 22
    ws1.cell(row=r, column=1).value = param
    ws1.cell(row=r, column=2).value = val
    ws1.merge_cells(f"C{r}:F{r}")
    ws1.cell(row=r, column=3).value = comment
    bg = GREY_BG if i % 2 == 0 else WHITE
    style_data_row(ws1, r, [1], bg=bg, bold=True, color=HEADER_BLUE)
    style_data_row(ws1, r, [2], bg=bg, bold=False, color=BLUE_INPUT)
    ws1.cell(row=r, column=3).font = body_font(color="555555")
    ws1.cell(row=r, column=3).fill = fill(bg)
    ws1.cell(row=r, column=3).alignment = left()
    ws1.cell(row=r, column=3).border = thin_border()

# Section règles d'or
r_rules = len(data_profil) + 6
ws1.row_dimensions[r_rules].height = 25
ws1.cell(row=r_rules, column=1).value = "RÈGLES D'OR À NE JAMAIS OUBLIER"
ws1.merge_cells(f"A{r_rules}:F{r_rules}")
ws1.cell(row=r_rules, column=1).font = Font(name="Arial", size=11, bold=True, color=WHITE)
ws1.cell(row=r_rules, column=1).fill = fill(DARK_GOLD)
ws1.cell(row=r_rules, column=1).alignment = center()

regles = [
    ("✅ Règle 1", "Ne jamais investir l'argent dont tu as besoin à court terme"),
    ("✅ Règle 2", "Toujours garder 3 à 6 mois de dépenses en cash liquide (fonds d'urgence)"),
    ("✅ Règle 3", "Ne pas regarder le portefeuille plus d'1 fois par mois"),
    ("✅ Règle 4", "Ne jamais paniquer et vendre lors d'une correction de -10 à -15%"),
    ("✅ Règle 5", "Réinvestir systématiquement les dividendes reçus"),
    ("❌ Règle 6", "Ne jamais mettre plus de 500K FCFA avant 6 mois d'expérience"),
    ("❌ Règle 7", "Ne jamais écouter les tuyaux de valeurs inconnues sans analyse"),
    ("❌ Règle 8", "Ne jamais activer la gestion sous mandat (trop cher pour un débutant)"),
]

for i, (code, regle) in enumerate(regles):
    r = r_rules + 1 + i
    ws1.row_dimensions[r].height = 20
    ws1.cell(row=r, column=1).value = code
    ws1.merge_cells(f"B{r}:F{r}")
    ws1.cell(row=r, column=2).value = regle
    bg = LIGHT_GREEN if "✅" in code else "FADBD8"
    style_data_row(ws1, r, [1], bg=bg, bold=True)
    ws1.cell(row=r, column=2).font = body_font()
    ws1.cell(row=r, column=2).fill = fill(bg)
    ws1.cell(row=r, column=2).alignment = left()
    ws1.cell(row=r, column=2).border = thin_border()

set_col_widths(ws1, {"A": 28, "B": 32, "C": 20, "D": 20, "E": 20, "F": 20})


# ══════════════════════════════════════════════════════════════════════════════
# SHEET 2 — COMPARATIF SGI
# ══════════════════════════════════════════════════════════════════════════════
ws2 = wb.create_sheet("🏦 Comparatif SGI")
ws2.row_dimensions[1].height = 40

merge_title(ws2, "A1:G1", "COMPARATIF DES 3 SGI — SOURCE: SIKAFINANCE.COM (28/03/2026)")

headers_sgi = ["Critère", "Bridge Securities", "BOA Capital Securities", "SG Capital Securities WA", "Meilleur", "Note"]
for c, h in enumerate(headers_sgi, 1):
    ws2.cell(row=2, column=c).value = h
style_header_row(ws2, 2, range(1, 7), bg=HEADER_BLUE)
ws2.merge_cells("F2:G2")

sgi_data = [
    ("Dépôt minimum",       "250 000 FCFA",   "1 000 000 FCFA",  "0 FCFA",          "SG Capital ✅",  "BOA éliminé d'office avec 500K FCFA"),
    ("Frais de courtage",   "1,00%",           "1,00%",           "0,80%",           "SG Capital ✅",  "Économie de 1 000 FCFA par 500K investi"),
    ("Conservation / an",  "0,50%",           "0,22 – 0,27%",    "0,25 – 0,50%",    "BOA Capital ✅", "BOA le meilleur mais inaccessible"),
    ("Tenue de compte",     "2 500/trimestre", "0 FCFA",          "2 500/trimestre", "BOA Capital ✅", "BOA gratuit mais min. 1 million requis"),
    ("Gestion sous mandat", "2,00%/an",        "0%",              "0%",              "BOA / SG ✅",    "Bridge : piège à éviter absolument"),
    ("Groupe bancaire",     "Oragroup",        "BMCE Bank Africa","Société Générale","SG Capital ✅",  "SG France = top 10 banques mondiales"),
    ("Risque dépositaire",  "Modéré",          "Faible",          "Très faible",     "SG Capital ✅",  "Priorité absolue pour un débutant"),
    ("Coût annuel réel*",   "17 500 FCFA",     "N/A (éliminé)",   "15 250 FCFA",     "SG Capital ✅",  "*Sur 500K, 1 A/R par an, hors plus-values"),
    ("% du capital mangé",  "3,50%",           "N/A",             "3,05%",           "SG Capital ✅",  "Économie nette de 2 250 FCFA/an"),
    ("VERDICT FINAL",       "❌ À éviter",      "❌ Inaccessible",  "✅ CHOIX N°1",    "SG Capital ✅",  "Ouvrir compte chez SG Capital Securities"),
]

colors_sgi = {
    "Bridge Securities":        "FADBD8",
    "BOA Capital Securities":   "FDEBD0",
    "SG Capital Securities WA": LIGHT_GREEN,
}

for i, row_data in enumerate(sgi_data):
    r = i + 3
    ws2.row_dimensions[r].height = 22
    for c, val in enumerate(row_data, 1):
        cell = ws2.cell(row=r, column=c)
        cell.value = val
        cell.border = thin_border()
        cell.alignment = center()
        if c == 1:
            cell.font = body_font(bold=True, color=HEADER_BLUE)
            cell.fill = fill(GREY_BG if i % 2 == 0 else "EAECEE")
        elif c == 2:
            cell.font = body_font(color=RED_ALERT if "❌" not in val else RED_ALERT)
            cell.fill = fill("FADBD8")
        elif c == 3:
            cell.font = body_font(color=RED_ALERT)
            cell.fill = fill("FDEBD0")
        elif c == 4:
            cell.font = body_font(color=MID_GREEN if "✅" in val else BLACK, bold="✅" in val)
            cell.fill = fill(LIGHT_GREEN)
        elif c == 5:
            cell.font = body_font(bold=True, color=MID_GREEN)
            cell.fill = fill("D5F5E3")
        else:
            ws2.merge_cells(f"F{r}:G{r}")
            cell.font = body_font(color="555555")
            cell.fill = fill(GREY_BG if i % 2 == 0 else WHITE)
            cell.alignment = left()

    if row_data[0] == "VERDICT FINAL":
        for c in range(1, 8):
            ws2.cell(row=r, column=c).font = Font(name="Arial", size=10, bold=True)
            ws2.cell(row=r, column=c).fill = fill(LIGHT_GREEN)

set_col_widths(ws2, {"A": 24, "B": 22, "C": 22, "D": 26, "E": 18, "F": 20, "G": 10})


# ══════════════════════════════════════════════════════════════════════════════
# SHEET 3 — PORTEFEUILLE RECOMMANDÉ
# ══════════════════════════════════════════════════════════════════════════════
ws3 = wb.create_sheet("📊 Portefeuille")
ws3.row_dimensions[1].height = 40
ws3.row_dimensions[2].height = 20

merge_title(ws3, "A1:I1", "PORTEFEUILLE RECOMMANDÉ — CAPITAL : 500 000 FCFA")
merge_title(ws3, "A2:I2", "Stratégie DCA · Horizon 2-3 ans minimum · SGI : SG Capital Securities WA", bg=MID_GREEN, sz=10)

# Allocation table
alloc_headers = ["Valeur", "Ticker", "Secteur", "Allocation %", "Montant FCFA",
                 "Cours (28/03)", "Nb Actions", "Objectif 1 an", "Rendement cible"]
for c, h in enumerate(alloc_headers, 1):
    ws3.cell(row=4, column=c).value = h
style_header_row(ws3, 4, range(1, 10), bg=DARK_GREEN)

portefeuille = [
    ("SONATEL",   "SNTS.sn", "Télécom / Défensif",  0.40, 200000, 28400),
    ("BOA CI",    "BOAC.ci", "Banque / Croissance",  0.35, 175000,  8700),
    ("TOTAL CI",  "TTLC.ci", "Énergie / Rebond",     0.25, 125000,  2975),
]

for i, (name, ticker, sector, alloc, montant, cours) in enumerate(portefeuille):
    r = i + 5
    ws3.row_dimensions[r].height = 24
    nb_actions = montant // cours
    objectif = round(cours * 1.12, 0)  # +12% target
    rendement = 0.09 + (0.03 * i)

    colors_port = [LIGHT_GREEN, LIGHT_BLUE, ORANGE_BG]
    bg = colors_port[i]

    data = [name, ticker, sector, f"{alloc*100:.0f}%", f"{montant:,.0f}",
            f"{cours:,.0f}", f"~{nb_actions} titres", f"~{objectif:,.0f}", f"+{rendement*100:.0f}%"]
    for c, val in enumerate(data, 1):
        cell = ws3.cell(row=r, column=c)
        cell.value = val
        cell.fill = fill(bg)
        cell.border = thin_border()
        cell.alignment = center()
        if c == 1:
            cell.font = body_font(bold=True, color=DARK_GREEN)
        elif c in [4, 9]:
            cell.font = body_font(bold=True, color=MID_GREEN)
        elif c == 5:
            cell.font = Font(name="Arial", size=10, bold=True, color=BLUE_INPUT)
        else:
            cell.font = body_font()

# Total row
r_total = 8
ws3.row_dimensions[r_total].height = 26
totals = ["TOTAL", "", "", "100%", "500 000", "", "", "", ""]
for c, val in enumerate(totals, 1):
    cell = ws3.cell(row=r_total, column=c)
    cell.value = val
    cell.fill = fill(DARK_GREEN)
    cell.font = Font(name="Arial", size=11, bold=True, color=WHITE)
    cell.border = thin_border()
    cell.alignment = center()

# DCA Schedule
r_dca = 10
merge_title(ws3, f"A{r_dca}:I{r_dca}", "CALENDRIER DCA — PLAN D'EXÉCUTION", bg=HEADER_BLUE, sz=11)

dca_headers = ["Tranche", "Date cible", "Montant", "Valeurs à acheter", "Montant par valeur", "Statut", "Notes"]
for c, h in enumerate(dca_headers, 1):
    ws3.cell(row=r_dca+1, column=c).value = h
style_header_row(ws3, r_dca+1, range(1, 8), bg=HEADER_BLUE)

dca_data = [
    ("Tranche 1", "Semaine 1-2 (Avr. 2026)", "300 000 FCFA", "SONATEL + BOA CI", "200K + 100K", "⏳ À EXÉCUTER", "Ouvrir compte SG Capital en priorité"),
    ("Tranche 2", "Semaine 6-8 (Mai 2026)",  "200 000 FCFA", "TOTAL CI + complément BOA", "125K + 75K", "⏳ EN ATTENTE", "Après validation tranche 1"),
]

for i, row_d in enumerate(dca_data):
    r = r_dca + 2 + i
    ws3.row_dimensions[r].height = 22
    bg = LIGHT_GREEN if i == 0 else ORANGE_BG
    for c, val in enumerate(row_d, 1):
        cell = ws3.cell(row=r, column=c)
        cell.value = val
        cell.fill = fill(bg)
        cell.border = thin_border()
        cell.alignment = center()
        cell.font = body_font(bold=(c in [1, 3, 6]))
        if c > 7:
            ws3.merge_cells(f"H{r}:I{r}")

# Projection table
r_proj = r_dca + 6
merge_title(ws3, f"A{r_proj}:I{r_proj}", "PROJECTION DE VALEUR — 500 000 FCFA INVESTI", bg=DARK_GOLD, fg=WHITE, sz=11)
proj_headers = ["Scénario", "Rend./an", "Fin 2026 (9 mois)", "An 1", "An 2", "An 3", "An 5", "Gain total", "x Capital"]
for c, h in enumerate(proj_headers, 1):
    ws3.cell(row=r_proj+1, column=c).value = h
style_header_row(ws3, r_proj+1, range(1, 10), bg=DARK_GOLD, fg=WHITE)

scenarios = [
    ("Pessimiste",  "3%",  "511 250", "515 000", "530 450", "546 364", "579 637",   "+79 637",  "1,16x"),
    ("Réaliste",    "9%",  "533 750", "545 000", "594 050", "647 515", "769 312",  "+269 312",  "1,54x"),
    ("Optimiste",   "14%", "553 750", "570 000", "649 800", "740 772", "963 000",  "+463 000",  "1,93x"),
]
scen_colors = ["FADBD8", LIGHT_GREEN, "D6EAF8"]
for i, row_s in enumerate(scenarios):
    r = r_proj + 2 + i
    ws3.row_dimensions[r].height = 22
    for c, val in enumerate(row_s, 1):
        cell = ws3.cell(row=r, column=c)
        cell.value = val
        cell.fill = fill(scen_colors[i])
        cell.border = thin_border()
        cell.alignment = center()
        cell.font = body_font(bold=(c in [1, 8, 9]))

set_col_widths(ws3, {"A": 18, "B": 12, "C": 22, "D": 12, "E": 14, "F": 14, "G": 14, "H": 16, "I": 14})


# ══════════════════════════════════════════════════════════════════════════════
# SHEET 4 — DONNÉES MARCHÉ LIVE
# ══════════════════════════════════════════════════════════════════════════════
ws4 = wb.create_sheet("📈 Données Marché Live")
ws4.row_dimensions[1].height = 40

merge_title(ws4, "A1:K1", "DONNÉES MARCHÉ BRVM — LIVE AU 28 MARS 2026 · Source : sikafinance.com")

mkt_headers = ["Valeur", "Ticker", "Cours (FCFA)", "Beta 1 an", "RSI", "Var. 1 mois",
               "Var. YTD", "Var. 1 an", "Var. 5 ans", "Cap. (Mds FCFA)", "Signal"]
for c, h in enumerate(mkt_headers, 1):
    ws4.cell(row=2, column=c).value = h
style_header_row(ws4, 2, range(1, 12), bg=DARK_GREEN)

marche_data = [
    ("SONATEL",    "SNTS.sn", 28400,  0.83, 49.6,  -3.07,  8.73,  13.15,  128.11, 2840,  "🟡 ACCUMULER"),
    ("ORANGE CI",  "ORAC.ci", 15300,  1.08, 56.2,  -1.64,  7.37,   9.52,      None, 2305,  "🟢 ACHAT (signal jour)"),
    ("ECOBANK CI", "ECOC.ci", 16500,  0.54, 49.0,  -2.94,  3.13,  66.67,  396.24,  908,  "🟡 ATTENDRE"),
    ("BOA CI",     "BOAC.ci",  8700,  0.34, 60.5, +10.13, 21.17,  42.39,  390.14,  348,  "🟢 ACHAT PRIORITÉ 1"),
    ("SIB CI",     "SIBC.ci",  7050,  0.69, 59.1,  +1.81, 22.61,  57.72,  405.38,  705,  "🟢 ACHAT FORT"),
    ("CORIS BANK", "CBIBF.bf",13790,  0.81, 62.4,  -1.85, 27.92,  28.28,   81.93,  441,  "🟡 RSI ÉLEVÉ – PRUDENCE"),
    ("SG CI",      "SGBC.ci", 35000,  1.36, 53.9,  -6.54, 17.08,  60.18,  343.04, 1089,  "🔴 ATTENDRE REBOND"),
    ("TOTAL CI",   "TTLC.ci",  2975,  0.29, 60.5,  +6.25, 27.41, -14.88,  138.00,  187,  "🟢 REBOND EN COURS"),
    ("NSIA BANQUE","NSBC.ci", 14145,  0.86, 55.9,  -3.78, 23.59,  67.40,  292.92,  350,  "🟡 SURVEILLER"),
]

signal_colors = {
    "🟢": LIGHT_GREEN,
    "🟡": "FEF9E7",
    "🔴": "FADBD8",
}

for i, row_m in enumerate(marche_data):
    r = i + 3
    ws4.row_dimensions[r].height = 22
    name, ticker, cours, beta, rsi, m1, ytd, y1, y5, cap, signal = row_m
    sig_bg = signal_colors.get(signal[0], WHITE)

    vals = [name, ticker, f"{cours:,.0f}", f"{beta:.2f}", f"{rsi:.1f}",
            f"{m1:+.2f}%" if m1 is not None else "N/D",
            f"{ytd:+.2f}%", f"{y1:+.2f}%",
            f"{y5:+.2f}%" if y5 else "N/D",
            f"{cap:,.0f}", signal]

    for c, val in enumerate(vals, 1):
        cell = ws4.cell(row=r, column=c)
        cell.value = val
        cell.border = thin_border()
        cell.alignment = center()

        if c == 1:
            cell.font = body_font(bold=True, color=HEADER_BLUE)
            cell.fill = fill(GREY_BG if i % 2 == 0 else WHITE)
        elif c == 11:
            cell.fill = fill(sig_bg)
            cell.font = body_font(bold=True)
        elif c in [6, 7, 8, 9]:
            # Color positive/negative
            try:
                num_val = float(val.replace("%", "").replace("+", "").replace(",", ""))
                cell.font = body_font(bold=False,
                                      color=MID_GREEN if num_val >= 0 else RED_ALERT)
            except:
                cell.font = body_font()
            cell.fill = fill(GREY_BG if i % 2 == 0 else WHITE)
        else:
            cell.fill = fill(GREY_BG if i % 2 == 0 else WHITE)
            cell.font = body_font()

# Legend
r_leg = len(marche_data) + 5
ws4.cell(row=r_leg, column=1).value = "LÉGENDE SIGNAUX :"
ws4.cell(row=r_leg, column=1).font = body_font(bold=True)
legends = [("🟢 ACHAT", "Signal positif — Momentum favorable, bon point d'entrée"),
           ("🟡 SURVEILLER", "Neutre — Attendre confirmation avant d'acheter"),
           ("🔴 ATTENDRE", "Signal négatif — Risque de correction, ne pas acheter maintenant")]
for i, (sig, desc) in enumerate(legends):
    r = r_leg + 1 + i
    ws4.cell(row=r, column=1).value = sig
    ws4.merge_cells(f"B{r}:K{r}")
    ws4.cell(row=r, column=2).value = desc
    col = signal_colors.get(sig[0], WHITE)
    for c in [1, 2]:
        ws4.cell(row=r, column=c).fill = fill(col)
        ws4.cell(row=r, column=c).font = body_font(bold=(c==1))
        ws4.cell(row=r, column=c).border = thin_border()
        ws4.cell(row=r, column=c).alignment = left()

set_col_widths(ws4, {"A": 16, "B": 12, "C": 14, "D": 10, "E": 8,
                     "F": 14, "G": 12, "H": 12, "I": 12, "J": 18, "K": 26})


# ══════════════════════════════════════════════════════════════════════════════
# SHEET 5 — SUIVI & SPÉCULATION
# ══════════════════════════════════════════════════════════════════════════════
ws5 = wb.create_sheet("🔭 Suivi & Spéculation")
ws5.row_dimensions[1].height = 40

merge_title(ws5, "A1:J1", "SUIVI MENSUEL & SPÉCULATION — MISE À JOUR REQUISE CHAQUE MOIS")

# Prix d'entrée & cibles
merge_title(ws5, "A3:J3", "PRIX D'ENTRÉE, CIBLES ET STOP-LOSS", bg=HEADER_BLUE, sz=11)
spec_headers = ["Valeur", "Prix entrée", "Stop-Loss (-15%)", "Cible CT (3 mois)", "Cible MT (12 mois)",
                "Dividende att.", "Catalyseurs", "Risques", "Statut", "Date MàJ"]
for c, h in enumerate(spec_headers, 1):
    ws5.cell(row=4, column=c).value = h
style_header_row(ws5, 4, range(1, 11), bg=HEADER_BLUE)

spec_data = [
    ("SONATEL",  28400, f"~{int(28400*0.85):,}", f"~{int(28400*1.08):,}", f"~{int(28400*1.15):,}",
     "~7%/an", "Résultats annuels, expansion fibre", "Concurrence Expresso, régulation", "⏳ À acheter", "28/03/2026"),
    ("BOA CI",    8700, f"~{int(8700*0.85):,}",  f"~{int(8700*1.12):,}",  f"~{int(8700*1.25):,}",
     "~4-5%/an", "Momentum fort +10% mois, bénéfice record 2024", "Exposition créances douteuses", "⏳ À acheter", "28/03/2026"),
    ("TOTAL CI",  2975, f"~{int(2975*0.85):,}",  f"~{int(2975*1.10):,}",  f"~{int(2975*1.20):,}",
     "~5-6%/an", "Rebond -14% sur 1 an, beta 0.29", "Prix pétrole, tension géopolitique", "⏳ À acheter", "28/03/2026"),
]

spec_colors = [LIGHT_GREEN, LIGHT_BLUE, ORANGE_BG]
for i, row_s in enumerate(spec_data):
    r = i + 5
    ws5.row_dimensions[r].height = 35
    for c, val in enumerate(row_s, 1):
        cell = ws5.cell(row=r, column=c)
        cell.value = val
        cell.fill = fill(spec_colors[i])
        cell.border = thin_border()
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.font = body_font(bold=(c == 1))

# Suivi mensuel
r_suivi = 10
merge_title(ws5, f"A{r_suivi}:J{r_suivi}", "TABLEAU DE SUIVI MENSUEL — À REMPLIR CHAQUE MOIS", bg=MID_GREEN, sz=11)
suivi_headers = ["Mois", "Valeur", "Cours début", "Cours fin", "Variation %",
                 "Dividende reçu", "Valeur portef.", "Gain/Perte", "Action prise", "Commentaire"]
for c, h in enumerate(suivi_headers, 1):
    ws5.cell(row=r_suivi+1, column=c).value = h
style_header_row(ws5, r_suivi+1, range(1, 11), bg=MID_GREEN)

mois_labels = ["Avril 2026", "Mai 2026", "Juin 2026", "Juillet 2026",
               "Août 2026", "Septembre 2026", "Oct. 2026", "Nov. 2026", "Déc. 2026"]
valeurs_suivi = ["SONATEL", "BOA CI", "TOTAL CI"]

row_idx = r_suivi + 2
for mois in mois_labels:
    for j, val in enumerate(valeurs_suivi):
        ws5.row_dimensions[row_idx].height = 20
        ws5.cell(row=row_idx, column=1).value = mois if j == 0 else ""
        ws5.cell(row=row_idx, column=2).value = val
        for c in range(1, 11):
            cell = ws5.cell(row=row_idx, column=c)
            cell.border = thin_border()
            cell.alignment = center()
            bg = GREY_BG if (mois_labels.index(mois)) % 2 == 0 else WHITE
            cell.fill = fill(bg)
            if c == 1:
                cell.font = body_font(bold=True, color=HEADER_BLUE)
            elif c == 5:
                # Formula placeholder note
                cell.value = "=SI(D{0}<>0,(D{0}-C{0})/C{0},\"\")".format(row_idx) if j == 0 else ""
                cell.font = body_font(color=BLACK)
            else:
                cell.font = body_font()
        row_idx += 1

# Alertes & signaux à surveiller
r_alert = row_idx + 2
merge_title(ws5, f"A{r_alert}:J{r_alert}", "🚨 ALERTES & SIGNAUX À SURVEILLER", bg=RED_ALERT, sz=11)
alert_headers = ["Signal", "Valeur", "Condition déclenchante", "Action recommandée", "Priorité"]
for c, h in enumerate(alert_headers, 1):
    ws5.cell(row=r_alert+1, column=c).value = h
style_header_row(ws5, r_alert+1, range(1, 6), bg=RED_ALERT)

alertes = [
    ("🟢 ACHAT RENFORCÉ", "BOA CI",    "Si cours < 8 000 FCFA (correction -8%)",     "Acheter 50 000 FCFA supplémentaires",      "HAUTE"),
    ("🟢 ACHAT RENFORCÉ", "TOTAL CI",  "Si cours < 2 700 FCFA (correction -9%)",     "Ajouter position de 50 000 FCFA",          "HAUTE"),
    ("🟡 SURVEILLER",     "SONATEL",   "Si RSI > 70 (surachat)",                      "Ne pas acheter, attendre repli",           "MOYENNE"),
    ("🟡 SURVEILLER",     "CORIS BANK","RSI déjà à 62, si > 70",                     "Éviter, zone de surachat proche",          "MOYENNE"),
    ("🔴 STOP-LOSS",      "SONATEL",   "Si cours < 24 140 FCFA (-15%)",              "Vendre 50% de la position",                "CRITIQUE"),
    ("🔴 STOP-LOSS",      "BOA CI",    "Si cours < 7 395 FCFA (-15%)",               "Vendre 50% de la position",                "CRITIQUE"),
    ("🔴 STOP-LOSS",      "TOTAL CI",  "Si cours < 2 529 FCFA (-15%)",               "Vendre 50% de la position",                "CRITIQUE"),
    ("🔵 DIVIDENDES",     "SONATEL",   "Publication résultats annuels (avr-mai)",     "Encaisser et réinvestir immédiatement",    "NORMALE"),
    ("🔵 DIVIDENDES",     "TOTAL CI",  "AG annuelle prévisible T2 2026",             "Vérifier date détachement coupon",         "NORMALE"),
]

alert_colors = {"🟢": LIGHT_GREEN, "🟡": "FEF9E7", "🔴": "FADBD8", "🔵": LIGHT_BLUE}
prio_colors = {"HAUTE": "F1948A", "MOYENNE": "FAD7A0", "CRITIQUE": RED_ALERT, "NORMALE": "AED6F1"}

for i, row_a in enumerate(alertes):
    r = r_alert + 2 + i
    ws5.row_dimensions[r].height = 22
    for c, val in enumerate(row_a, 1):
        cell = ws5.cell(row=r, column=c)
        cell.value = val
        bg = alert_colors.get(row_a[0][0], WHITE)
        cell.fill = fill(bg)
        cell.border = thin_border()
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        if c == 5:
            cell.fill = fill(prio_colors.get(val, WHITE))
            cell.font = body_font(bold=True)
        elif c == 1:
            cell.font = body_font(bold=True)
        else:
            cell.font = body_font()

set_col_widths(ws5, {"A": 18, "B": 14, "C": 20, "D": 22, "E": 20,
                     "F": 16, "G": 16, "H": 14, "I": 18, "J": 20})


# ══════════════════════════════════════════════════════════════════════════════
# SHEET 6 — LEXIQUE & MÉMO
# ══════════════════════════════════════════════════════════════════════════════
ws6 = wb.create_sheet("📚 Lexique & Mémo")
merge_title(ws6, "A1:D1", "LEXIQUE DES TERMES FINANCIERS — MÉMO DÉBUTANT BRVM")

lexique = [
    ("TERME", "DÉFINITION", "EXEMPLE", "À RETENIR"),
    ("SGI", "Société de Gestion et d'Intermédiation — ton courtier en bourse",
     "SG Capital Securities", "Ouvre ton compte ici avant tout"),
    ("BRVM", "Bourse Régionale des Valeurs Mobilières — la bourse de l'Afrique de l'Ouest (8 pays UEMOA)",
     "Abidjan, CI", "Seule bourse de la zone franc"),
    ("FCFA", "Franc CFA — monnaie arrimée à l'Euro. 1€ = 655,957 FCFA",
     "500 000 FCFA = ~762 €", "Stable, peu de risque de change"),
    ("Courtage", "Commission prélevée par la SGI à chaque achat/vente",
     "1% = 5 000 FCFA sur 500K", "Minimise tes transactions"),
    ("Conservation", "Frais annuels pour garder tes actions dans ton compte-titres",
     "0,25%/an = 1 250 FCFA/an", "Frais automatiques, inévitables"),
    ("Beta", "Mesure la volatilité d'une action par rapport au marché. Beta < 1 = moins volatile",
     "BOA CI : beta 0,34", "Préfère beta < 1 pour commencer"),
    ("RSI", "Relative Strength Index — indicateur 0-100. >70 = suracheté, <30 = survendu",
     "BOA CI RSI = 60,5", "N'achète pas si RSI > 70"),
    ("Dividende", "Part du bénéfice versée aux actionnaires, généralement 1x/an",
     "SONATEL ~7%/an", "Revenu passif = réinvestir"),
    ("DCA", "Dollar Cost Averaging — investir en plusieurs fois pour lisser le prix d'entrée",
     "300K maintenant + 200K dans 6 sem.", "Stratégie recommandée pour débutant"),
    ("Stop-Loss", "Seuil de perte déclencher une vente automatique pour limiter les pertes",
     "-15% du prix d'achat", "Discipline de fer à respecter"),
    ("PER", "Price-to-Earnings Ratio — cours divisé par bénéfice. Mesure la cherté d'une action",
     "PER 10 = action à 10x ses bénéfices", "Plus c'est bas, plus c'est bon marché"),
    ("Blue Chip", "Valeur de premier plan, grande capitalisation, stable et reconnue",
     "SONATEL, ECOBANK CI", "Idéal pour portefeuille débutant"),
    ("Capitalisation", "Valeur totale d'une entreprise en bourse = cours × nb d'actions",
     "SONATEL : 2 840 Mds FCFA", "Grande cap = plus de sécurité"),
    ("YTD", "Year-To-Date — performance depuis le 1er janvier de l'année en cours",
     "BOA CI YTD = +21,17%", "Compare les perfs depuis janvier"),
]

for i, (terme, defi, ex, note) in enumerate(lexique):
    r = i + 2
    ws6.row_dimensions[r].height = 30
    data = [terme, defi, ex, note]
    for c, val in enumerate(data, 1):
        cell = ws6.cell(row=r, column=c)
        cell.value = val
        cell.border = thin_border()
        cell.alignment = Alignment(horizontal="left" if c > 1 else "center",
                                   vertical="center", wrap_text=True)
        if r == 2:
            cell.font = header_font(color=WHITE)
            cell.fill = fill(DARK_GREEN)
        else:
            bg = GREY_BG if i % 2 == 0 else WHITE
            cell.fill = fill(bg)
            cell.font = body_font(bold=(c == 1), color=HEADER_BLUE if c == 1 else BLACK)

set_col_widths(ws6, {"A": 18, "B": 50, "C": 30, "D": 35})

# ── Final save ────────────────────────────────────────────────────────────────
output_path = "/Users/elyseebleu/Documents/financial-analyst/BRVM_Portefeuille_2026.xlsx"
wb.save(output_path)
print(f"✅ Fichier créé : {output_path}")
