# Konzept: Kapitelfluss, Flammen, XP und Herzen

> Stand 17.11.2026 · entschieden von Andi im Projekt-Chat (Entscheidungen K1–K10) · Umsetzung in Tickets 025–031.
> Lernregeln (Bestehen, Testreife, Leben) gehören in den Reducer/`RulePolicy`; Flammen und XP sind reine Belohnung,
> gerätelokal und **nie** Bestehenskriterium (D8). Zahlen hier sind Startwerte; der Pilot (Phase 7) kalibriert.

## 1. Entscheidungen

| # | Entscheidung | berührt |
|---|---|---|
| K1 | **Lektion bestanden ab 51 %.** Darunter: rotes ✗, „Nicht bestanden – nochmal“, Lektion bleibt offen. | Reducer (`LESSON_COMPLETED` nur bei Bestehen) |
| K2 | **Sperre:** Übung und Testreife erst, wenn **alle** Lektionen bestanden sind. Bestehende Fortschritte bleiben gültig. | Reducer/Policy |
| K3 | **Übung: 20 Fragen** je Durchgang (Pool unverändert), **überspringbar** → direkt Testreife. | ChapterFlow, Konstante |
| K4 | **Testreife nicht bestanden → Ziel-Stapel** (Pflicht): 2 Aufgaben je schwachem Lernziel, max. 10, mit Fortschritt „Ziel-Training x/n“; danach **Testreife neu** (neuer Block). Liste der unsicheren Lernziele bleibt. Konkretisiert V2. | Reducer (neuer Zustand `TARGET`) |
| K5 | **Kapitelseite = Stepper:** Balken antippbar (Lektionen · Übung · Testreife · Test 🏆), gesperrte grau, immer **nur ein Schritt** sichtbar (kein Scrollen in andere Schritte). | UI |
| K6 | **Ergebnis-Schritt 🏆** (eigener 5. Schritt, gesperrt bis bestanden): Testergebnis (%, richtig/falsch), Fehlerquote des ganzen Kapitels, Gesamtbewertung (1–3 Sterne: 1 = bestanden, 2 ab 70 %, 3 ab 90 % Trefferquote im Kapitel – G-019 A), Flammen, XP inkl. Bonus. Abgeschlossenes Kapitel öffnet hier. | UI |
| K7 | **Herzen verdienen:** 10 Richtige in Folge in der Übung → +1 Herz für den nächsten Kapiteltest; max. 1 pro Kapitel; Obergrenze 5 Leben bleibt. Ergänzt Entscheidung 2; Wirkung auf D14 im Pilot prüfen. | Reducer/Policy |
| K8 | **Flammen v2** (Abschn. 2) inkl. **Flammenschutz**. | `core/flames.ts` |
| K9 | **XP + Level** (Abschn. 3), Flammen werden bei bestandenem Kapitel zum Multiplikator. | `core/xp.ts` |
| K10 | Lektionsergebnis: „Done!“ entfällt, keine grünen ✓ bei „Übe diese nochmal“ (stattdessen „Richtige Lösung:“), Sterne/Prozent vertikal zentriert. | UI |

## 2. Flammen v2

**Zwei Ebenen:**
- **Runden-Flammen (`pot`)** – sichtbar in der Aufgabenzeile. Je **3 Richtige in Folge = 1 Flamme**.
- **Kapitel-Flammen (`chapterFlames`)** – im Header. Am Ende **jeder Runde** (Lektion, Übungsdurchgang, Testreife, Ziel-Stapel, Test) fliegen die Runden-Flammen nach oben (vorhandene Animation) und erhöhen die Kapitel-Flamme.

**Fehlerregeln (wie bisher, plus Schutz):**
1. 1. Fehler → Runden-Flammen weg, „scharf“ (`armed`).
2. 2. Fehler, bevor wieder eine Flamme kam → **Kapitel-Flammen auf 0** – *außer* ein **Flammenschutz** ist da: dann wird 1 Schutz verbraucht (Animation: Schild bricht), die Kapitel-Flammen bleiben, `armed` bleibt.
3. Eine neue Flamme macht wieder „unscharf“.

**Flammenschutz verdienen:** eine **Lektion mit 100 %** (oder ein Übungsdurchgang mit 100 %) → +1 Schutz, **max. 2**. Gilt bis Kapitelende. Belohnt Genauigkeit, nicht Tempo.

**Farbe nach Kapitel-Flammen** (ein Kapitel hat ~150 Aufgaben, also max. ~50 Flammen):

| Kapitel-Flammen | 0 | 1–9 | 10–19 | 20–34 | ≥ 35 |
|---|---|---|---|---|---|
| Farbe | grau | orange | rot | violett | blau („heißeste Flamme“) |
| Multiplikator | ×1,0 | ×1,02–1,18 | ×1,2–1,38 | ×1,4–1,68 | ×1,7–2,0 |

**Multiplikator** = `1 + 0,02 × chapterFlames`, gedeckelt bei **×2,0** (50 Flammen). Header zeigt Flamme in Stufenfarbe + Zahl, darunter klein `×1,4`.

**Gültigkeit:** Flammen gibt es nur im Kapitelkontext des laufenden Kurskapitels. Bei **bestandenem Kapitel** → Multiplikator anwenden, dann `chapterFlames = 0`, Schutz = 0. Wird das Kapitel wiederholt (Korrekturfehler), bleiben die Flammen erhalten. Wiederholung (Leitner) und Freies Üben: XP ja, Flammen nein *(mein Vorschlag)*.

## 3. XP und Level

XP kommen **sofort** („+5“ an der Antwort), der Flammen-Bonus **beim Bestehen** des Kapitels: `Bonus = Kapitel-XP × (Multiplikator − 1)`.

| Quelle | XP |
|---|---|
| Richtige Antwort: Lektion / Übung / Testreife / Ziel-Stapel / Test | 5 / 5 / 8 / 8 / 10 |
| Lektion erstmals bestanden (≥ 51 %) | +20; 3 Sterne (≥ 90 %) +10 |
| Testreife bestanden | +30 |
| Kapiteltest bestanden | +100; perfekt +50 |
| Wiederholungskarte richtig | 3 |
| Tagesziel erreicht | +25 |
| bereits bestandene Lektion nochmal | 50 % |
| Freier Modus / Freies Üben | 50 %, keine Flammen *(mein Vorschlag)* |

**Level:** Schritt von Level n → n+1 kostet `100 × n` XP (1→2: 100, 2→3: 200 …; Level 10 ≈ 4.500 XP). Ein Kapitel bringt ≈ 600–1.200 XP inkl. Bonus → ein Level alle 1–2 Kapitel am Anfang, später seltener. Anzeige: Ring mit Levelzahl im Header (ersetzt nichts, kommt links vom Menü), XP-Fortschritt im Menü/Seitenleiste.

**Rechenbeispiel Kapitel A1-01** (7 Lektionen à ~7 Aufgaben, 20 Übung, 20 Testreife, 20 Test, ~85 % richtig, 18 Flammen):
- Antworten: 42×5 + 17×5 + 17×8 + 18×10 = 611 · Lektionen 7×20 + 3×10 = 170 · Testreife 30 · Test 100 → **911 XP**
- Bonus ×1,36 → **+328 XP** · Summe **1.239 XP** → von Level 1 auf Level 5 (100 + 200 + 300 + 400 = 1.000 XP bis Level 5; korrigiert in 030).

## 4. Warum es motiviert, ohne falsche Anreize
- **Sofortiges Feedback** (+XP, Flamme springt) bei jeder richtigen Antwort.
- **Risiko/Gewinn:** Serien vervielfachen, Fehler kosten – der Schutz macht es fair statt frustrierend.
- **Langfristig:** Level, Flammenfarbe, Tagesstreak.
- **Lernpsychologisch sauber:** mehr XP für testnähere Aufgaben, Wiederholen lohnt sich (Spaced Repetition), Farmen nicht (50 % bei Wiederholung), Raten wird durch die Fehlerregel bestraft, nichts davon ändert Bestehensregeln.

## 5. Tickets (Reihenfolge)

| Ticket | Inhalt | Modell |
|---|---|---|
| 025 | K1, K2, K10: Lektionsergebnis + Sperre (Reducer + Tests) | Sonnet |
| 026 | K3: Übung 20 + Überspringen | Sonnet |
| 027 | K5, K6: Stepper-Kapitelseite + 🏆-Ergebnis | Opus plant, Sonnet baut |
| 028 | K4: Ziel-Stapel nach Testreife (Reducer + Tests) | Opus |
| 029 | K8: Flammen v2 + Schutz (`core/flames.ts`, ersetzt `core/accuracy.ts`) | Opus |
| 030 | K9: XP + Level + Multiplikator (`core/xp.ts`) | Opus |
| 031 | K7: Herzen in der Übung (Reducer/Policy + Tests) | Sonnet |

## 6. Offen (klein, im jeweiligen Ticket entscheiden)
- Flammen/XP in Wiederholung und Freiem Üben (Vorschlag oben).
- Anzeige der verdienten Herzen in der Übung (Herz-Fortschritt 0/10 neben den Flammen?).
- Sound/Haptik bei Flamme, Schutz, Level-up.
