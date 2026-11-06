# 00 – Kurzfassung: Arbeitsstand für jeden Chat

> **Projekt:** „Weg zur A2“ · **Stand:** 06.11.2026 (Phase 4 abgeschlossen, D14–D17)
> **Abgeleitet aus:** `00-masterprompt.md` (Rev. 4.1, 06.11.2026) · `01-ressourcen.md` Abschn. 7 (E1–E4) · `02-aufbereitung.md` Abschn. 5.1 (D1–D6) · `03-curriculum.md` (Rev. 3R, D7–D11) · `04-spielregeln.md` (Phase 4, D14–D16)
> **Vorrang:** Bei Widerspruch gilt `00-masterprompt.md`. Jede neue Entscheidung wird hier **und** im Phasen-Dokument nachgetragen.
> **Den vollen Masterprompt lesen nur:** bei Unklarheit, bei Änderungen an der Spezifikation oder in Phasen 5–7 (Claude Code, `docs/`).
> **Prüfungsfakten:** stehen verifiziert in `00-quellen.md` – dort nachschlagen, nicht neu recherchieren.

---

## 1. Mission und Parameter

- **Ziel:** Absolute:r Anfänger:in (lateinisch alphabetisiert) besteht mit **Ø 1–2 h Übung pro Tag** die **ÖIF-Integrationsprüfung A2** in allen Teilen: Lesen, Hören, Schreiben, Sprechen, Werte- und Orientierungswissen (WOW). Grammatik und Wortschatz durchgehend.
- **Zeit (D7):** **kein festes Enddatum.** Der **gesamte Umfang** wird gelehrt, egal wie lange es dauert. Tagespensum wählbar 1 / 1,5 / 1,75 / 2 h (Richttempo Ø 1,5 h). **Prognose (D15, `04` Abschn. 1.3):** ≈ 260 Lernstunden; 1 h → 254 · **1,5 h → 172** · 1,75 h → 150 · 2 h → 132 Plantage (Spanne bei 1,5 h: 159–185, je nach Trefferquote beim Testantritt). Ersetzt die Phase-3R-Werte (240 h, 159 Plantage). „90 Tage“ ist kein Planwert mehr. **Wiederholung ohne Minuten-Deckel:** fällige Queue wird täglich vollständig abgearbeitet.
- **Qualität (D8):** hochwertiger Content, **kein „Duolingo-Slop“** – authentische österreichische Alltagssituationen, echtes Prüfungsformat, Erklärungen mit Warum, Audio nach D13 (kostenlos); Gamification nur unterstützend. Mindestkriterien Q1–Q11 (`03` Abschn. 5).
- **Bestehenssicherheit (D11):** voller Umfang, 100 % Abdeckung, kein Kürzen. Austrittskriterien „prüfungsreif“ (`03` Abschn. 4.2, Zustand `READY_FOR_EXAM` in `04a` 4.4): alle Kapitel + A1-Meilenstein + **zwei aufeinanderfolgende A2-Simulationen ≥ 75 % je Teil** (zweite am Stück) + offizieller Modelltest + Wiederholung im Griff; Sprechpraxis im ÖIF-Kursraum als feste Empfehlung. Keine Garantie behaupten.
- **Meilenstein 1:** Prüfungsreife A1 (Format Integrationsprüfung A1). **Jedes Kapitel ist ein Sub-Goal.**
- **Produkt:** interaktives Lernspiel, per Link für Dritte, **ohne Login**, nur Namenseingabe; Fortschritt **nur lokal** + Export/Import (JSON); Upload von Content-Packs; Hilfe mit Frage-Chat.
- **Auslieferung:** Stufe 1 Claude-Artifact (Start) · Stufe 2 optional eigene Web-App auf Cloudflare – derselbe Code (Ports & Adapters).
- **Startdatum relativ:** Tag 1 = Profilanlage (`startDate`). Plantag = Kalendertage seit `startDate` + 1, **ohne festes Ende**. Tool zeigt „Tag X“, Etappe, Tempo gegen das gewählte Pensum und Prognose „prüfungsreif ab ca. Tag Y“ – nie einen Rückstand gegenüber einem Enddatum.
- **Sprachen:** jede Anweisung, Vokabel, Erklärung, jedes Feedback hat `de` (einfach), `en`, `tl`. Prüfungsmodus **nur Deutsch**, Übersetzung erst im Feedback (Ausnahme V5: Kapiteltest-Anweisungen A1-01–A1-04 mit einblendbarer Übersetzung).
- **Österreichisches Deutsch ist Lernziel (D10):** AT-Form = Hauptform; bundesdeutsche Formen **immer gekennzeichnet** („in Deutschland: Tomate“), nie unmarkiert in Lerntexten, im Prüfungsmodus nie in Stimulus/Optionen. Nuancen: Lexik, Genus, Perfekt mit *sein*, Aussprache. Konzept `03` Abschn. 6, Inventar-Prüfung `03g`.
- **Tagalog:** einfach, alltagsnah, Taglish erlaubt wenn verständlicher; `reviewStatus` `machine`/`reviewed`; Risiko in jedem QA-Bericht ausweisen.
- **Gerät:** Smartphone first, Desktop unterstützt.
- **KI:** Stufe 1 Claude im Viewer (nur mit Account) + „Frage an eine KI kopieren“ + Offline-Hilfe; Stufe 2 eigener Endpunkt.

## 2. Entscheidungen (final, bestätigt 05.11.2026 – Wortlaut Masterprompt Abschn. 3)

1. **Korrekturrunde – Variante A (streng):** Test mit ≥ 1 Leben, aber mit Fehlern beendet → alle falschen Aufgaben kommen als Zwillingsaufgabe erneut. **Jeder Fehler in der Korrekturrunde → Kapitel komplett wiederholen.** Phase 4 hat die Bestehenswahrscheinlichkeit simuliert (`04` Abschn. 2): Testlänge 20 + Testreife 18/20 festgelegt (D14).
2. **Bonusleben:** +1 bei perfektem Kapitel (ohne Fehler), gilt für das nächste Kapitel, stapelbar bis **max. 5 Leben**.
3. **Tagesstreak-Schutz:** **1 „Streak-Freeze“ pro 7 Streak-Tage** (max. 2 angespart); ein verpasster Tag verbraucht automatisch einen Freeze, ohne Freeze → Streak auf 0.
4. **Tagesziel für den Streak:** **≥ 20 Minuten aktive Lernzeit UND alle fälligen Wiederholungen erledigt.**
5. **Bewertung freier Schreib-/Sprechaufgaben:** für alle regelbasiert (Anrede, Gruß, Mindestwortzahl, Leitpunkte) + Musterlösung + Selbstcheck; zusätzlich KI-Feedback über `FeedbackPort` (Stufe 1: Claude im Viewer oder „Feedback holen“-Kopier-Prompt; Stufe 2: eigener Endpunkt). KI-Feedback ist Lernhilfe, kein Bestehenskriterium.
6. **Meilensteinprüfungen bestanden ab:** **≥ 75 % je Prüfungsteil** (Sicherheitsmarge über der offiziellen Bestehensgrenze).
7. **Frage-Chat während Tests:** **gesperrt** in Kapiteltest, Korrekturrunde und Meilensteinprüfungen; **frei** in Lektionen, Übungen, Wiederholung und nach jedem Feedback.

## 3. Folge-Entscheidungen aus Phase 1, 2 und 3

| # | Entscheidung | Wirkt auf |
|---|---|---|
| E1 | Planung fix auf dem **aktuellen Papierformat**. IntG-Novelle/IntG-DV-Entwurf nach Ende der Begutachtung (12.11.2026) erneut prüfen → Trigger in `00-quellen.md`. | 2–5 |
| E2 | Tagalog-Review durch Muttersprachler:in angestrebt; bis dahin `reviewStatus: machine`, Risiko im QA-Bericht. | 2, 5, 7 |
| E3 | 75 %-Regel bei **A1 je Subtest** (Sprachbausteine · Hören · Hören und antworten · Lesen · Schreiben · Sprechen · WOW); offizielle Gesamtlogik (≥ 240/400, WOW ≥ 25/45) nur als Info. **A2** je offiziellem Teil (Lesen, Hören, Schreiben, Sprechen, WOW) ≥ 75 %. | 4 |
| E4 | Gerätecheck → `geraetecheck.md`, sobald Smartphone-Test ohne Login (inkl. Neuladen/localStorage) vorliegt. Bisher: Desktop Debian/Brave – TTS ohne deutsche Stimme (`synthesis-failed`); Pixel 9 Pro/Chrome instabil (Prototyp E-P3). | 6 |
| D1 | **IntG-DV Anl. A/B = rechtlicher Mindestumfang; ÖIF-Rahmencurriculum 2025 = Arbeitsbasis** der Can-Do-Matrix. Fakten nur aus Primärquellen. | 3, 5 |
| D2 | **Beispielsätze im Wortschatz erst in Phase 5**, je Kapitel, nur mit bis dahin eingeführtem Wortschatz. | 5 |
| D3 | **Keine Herabstufung aktiver Wörter**; Inventar eher erweitern. Goethe-Lücken in Phase 3 ergänzt (Inventar v2: 2.035 Einträge). Leitner-Mehraufwand ausdrücklich gerechnet. | 3, 4 |
| D4 | **Wortgruppen zählen als Set, passive Einträge nicht als „neue Einheiten“**; Inventar wird nicht gekürzt. | 3 |
| D5 | Fragenkatalog Q09/Q10 **nur auf Themen** durchgesehen (keine Fragen übernommen). | 3, 5 |
| D6 | Veraltete Wurzel-Kopie `01-ressourcen.md` gelöscht; maßgeblich nur `claude/01-ressourcen.md`. | – |
| **D7** | **Kein festes 90-Tage-Limit;** gesamter Umfang, egal wie lange. 90 Tage / Ø 1,5 h nur Richttempo, nie Kürzungsgrund. **Wiederholung ohne Deckel**, fällige Queue vollständig. Ersetzt Masterprompt-Parameter „90 Tage“ und Phase 4.8 „max. ~15 min“. | 3–7 |
| **D8** | **Hochwertiger Content, kein „Duolingo-Slop“**: authentische AT-Situationen, echtes Prüfungsformat, Erklärungen mit Warum; Gamification nur unterstützend. Kapitel ≈ 3–4,5 h, 9–15 Mikro-Lektionen, Audio für Wortschatz und Hörtexte (Umsetzung D13). | 4, 5 |
| **D9** | **14 neue WOW-Lernziele** (A1-WOW-21–27, A2-WOW-42–48) übernommen; Fakten vor Phase 5 belegen. | 5 |
| **D10** | **Österreichisches Deutsch ist Lernziel;** bundesdeutsche Formen immer gekennzeichnet, nie unmarkiert; Lexik, Genus, Perfekt mit *sein*, Aussprache. | 3, 5, 6 |
| **D11** | **Voller Umfang, 100 % Abdeckung, kein Kürzen;** Designziel **Bestehenssicherheit** mit Austrittskriterien. | 3, 4, 5 |
| **D12** | Zu 3R: O1 Prognose + Etappen statt 90-Tage-Countdown · O2 Austrittskriterien bestätigt · O3 D10-Lücken pragmatisch im jeweiligen Content-Batch · O4 durch D13 ersetzt. | 4, 5, 6 |
| **D13** | **Audio ohne Budget:** Geräte-TTS als Standard (gehärtet, Prototyp v4) · Hörtexte im Prüfungsformat als kostenlos selbst erzeugte Dateien (z. B. Piper/Thorsten CC0 lokal, oder Gratis-Kontingent Cloud-TTS mit AT-Stimme nach Lizenzprüfung) · Transkript als Rückfall · Entscheidung per Audio-Spike + Gerätecheck vor dem ersten Audio-Batch. Widerspruch zu E-P1 benannt (R6). | 5, 6 |
| **D14** | **Phase-4-Regeln bestätigt (06.11.2026):** V1 Kapiteltest 20 Aufgaben (3 je Disziplin + 2 Fokus) + Pflicht-Sprechaufnahme ohne Leben · V2 Testreife-Runde 18/20 vor dem Test · V3 Zentralfall Trefferquote 0,92 · V4 Genus als Richtungsrotation, Fach 5 = Produktion mit Artikel · V5 Testanweisungen A1-01–A1-04 mit Übersetzung · Auslegungen I-1–I-8 (`04` Abschn. 1.2). | 4–7 |
| **D15** | **Prognose aus Phase 4 ist Planwert:** ≈ 260 h, 1,5 h → 172 Plantage (159–185); Pilot (Phase 7) kalibriert. | 5–7 |
| **D16** | **Regeln lose gekoppelt:** Reducer = Mechanik, Regeln = austauschbare `RulePolicy` (`makeReducer(policy)`), heutige Regeln = `defaultPolicy`. Datenmodell offen für spätere **Spezial-Retries** und **Kapitel-Skip** (`completed` mit Grund, `RecoveryPlan` als Daten, Event `OVERRIDE_GRANTED`, `ruleset`-Version). Logik der Features erst bei Bedarf; Skip würde D11 berühren → eigene Entscheidung nötig (`04a` 1a). | 5–7 |
| **D17** | **Umsetzung:** Repo `github.com/lauhard/speakaustrian` · Audio **vorerst nur Geräte-TTS** (Android/iOS/Web zuverlässig; Hördateien aus D13 zurückgestellt, R6 offen) · WOW-Belege je Batch · **Claude-Chat nur Architektur/Design/Spec**, Rest in Claude Code: Backlog → Plan-Agent (1 Ticket) → Branch → Test-Agent (Vitest/Playwright/Geräte-Checkliste) → manuelle Implementierung → Push; minimale CI früh, MR-CI später · Spec-Lücken über `docs/spec-gaps.md` zurück in den Chat · Phasen 5+6 verschränkt · token-effizient (`CLAUDE.md`, `docs/INDEX.md`). | 5–7 |

### 3.1 Phase 4 – Vorschläge und Auslegungen im Detail (bestätigt als D14)

| # | Inhalt |
|---|---|
| V1 | Kapiteltest **20** bewertete Aufgaben (3 je Disziplin + 2 Fokus; Prüfungstraining L4/H4) + 1 Pflicht-Sprechaufnahme ohne Leben |
| V2 | **Testreife-Runde** vor dem Test: 20 Übungsitems, Test ab **18/20**, sonst Zielübung + neuer Block (ohne Leben, Chat frei) |
| V3 | Planungs-Zentralfall Trefferquote 0,92 statt 15-%-Annahme → 1,5 h ≈ 172 Plantage (159–185), ≈ 260 h |
| V4 | Genus ohne eigene Spur: Richtungsrotation in der Nomenkarte, Fach 5 = Produktion mit Artikel |
| V5 | Kapiteltest-Anweisungen A1-01–A1-04 mit einblendbarer Übersetzung, ab A1-05 nur Deutsch |
| I-1–I-8 | Fehler = Aufgabe · Bonus nur nach perfektem 1. Versuch, gilt für alle Versuche des nächsten Kapitels · Test + Korrektur = gesperrte Einheit · Freeze nur, wenn er die ganze Lücke schließt · 00:00 + Session-Anker 3 h · Verschiebung beim 1. Simulationsblock · Wochenreview bleibt fällig bis erledigt · Test nur fortsetzen, nie neu starten |

**Design-Konsequenzen aus Prüfungsfakten (verbindlich):**
- Auswendig gelernte Mustertexte im Schreiben → 0 Punkte (PO 2024 § 13c). **Schreiben nie über Auswendiglernen von Mustertexten trainieren**; Musterlösungen variieren, Fokus auf Leitpunkt-Bearbeitung.
- Hörwiederholung im Tool exakt wie Prüfung (A2: Hören 1+2 2×, Hören 3+4 1×; A1: alle Hörteile 2×), keine zusätzliche Wiederholung.
- WOW-Fakten nie aus Curriculum oder Modelltest übernehmen (veraltet, W8/W12), nur aus Primärquellen mit Stand.

## 4. Arbeitsregeln

- **Pro Chat genau eine Phase.** Ende: Ergebnis → DoD abhaken → offene Fragen → **STOP**. Kurze Statusmeldung (fertig / offen / nächster Schritt).
- Vorher **max. 3 Rückfragen**, nur wenn für die Phase etwas unklar ist.
- Keine Phase überspringen; fehlt ein Vorgänger-Ergebnis, das sagen.
- Ergebnisse als `claude/NN-thema.md`; große Ergebnisse als Teil-Dokumente (`NNa-…`).
- Widersprüche zu früheren Ergebnissen **benennen**, nicht stillschweigend überschreiben.
- **Prüfungsfakten** nur mit Quelle (URL + Stand), sonst `[UNVERIFIZIERT]` + Lückenliste. Nachschlagen in `00-quellen.md`; nur **neue** Fakten recherchieren und dort eintragen.
- **Urheberrecht:** offizielle Tests/Lehrwerke nur Format-/Niveau-Referenz; keine Texte, Hörskripte, Aufgaben 1:1 oder eng paraphrasiert. Alles Eigenproduktion im identischen Format; offizielle Modelltests im Tool **verlinken** (Generalprobe).
- **Österreichisches Standarddeutsch ist Lernziel (D10):** Austriazismen als Hauptform (Jänner, Erdäpfel, Paradeiser, Topfen, Sackerl, Ordination, Meldezettel, „Grüß Gott“); bundesdeutsche Formen **immer** gekennzeichnet, nie unmarkiert.
- **Niveau strikt:** nur eingeführter Wortschatz + geplante neue Wörter.
- **Nie kürzen, um schneller zu werden (D7, D11);** Tempo kommt aus dem Pensum, nicht aus weniger Inhalt.
- **Designentscheidungen didaktisch begründen** (Retrieval Practice, Spaced Repetition, Interleaving, Cognitive Load, i+1).
- **Code:** Kommentare Englisch, funktionale Patterns, Spiellogik als reine Funktionen. Planungszahlen per Skript (`03e`, `03e2`, `04c`).
- **Werkzeuge:** Phasen 1–4 im Claude-Projekt · Phasen 5–7 in Claude Code (Docs nach `docs/`, Content als `content/*.json` gegen Schema).

## 5. Phasenstand

| Phase | Ort | Status | Ergebnis |
|---|---|---|---|
| 1 Ressourcen sammeln | Projekt | ✅ 05.11.2026 | `01-ressourcen.md` |
| 2 Ressourcen aufbereiten | Projekt | ✅ 06.11.2026 (D1–D6 bestätigt) | `02-aufbereitung.md` + `02a`–`02g` + `02c-…tsv` |
| 3 Curriculum & Plan | Projekt | ✅ 06.11.2026 | `03`, `03a`–`03e` |
| 3R Revision (D7–D11) | Projekt | ✅ 06.11.2026 | `03` (Rev. 3R), `03a`, `03b` (Rev. 3R), `03e2`, `03f`, `03g` |
| 4 Spielregeln | Projekt | ✅ 06.11.2026 (D14–D16 bestätigt) | `04`, `04a` (Automat, Policy-Schicht, Regeln), `04b` (174 Testfälle), `04c` (Skript) |
| **5 Content** | Claude Code | **nächste Phase**, verschränkt mit 6 (D17e) | `content/*.json` |
| **6 App** | Claude Code | **gestartet:** Repo vorbereitet (D17), Backlog folgt | `speakaustrian` |
| 7 Test & Abnahme | Claude Code | offen | Repo |

## 6. Dokumentenkarte – was pro Phase lesen (in **einem** Aufruf)

| Phase | Immer | Zusätzlich |
|---|---|---|
| 5 | `CLAUDE.md` im Repo | `docs/00-masterprompt.md`, `03` Abschn. 5–6 (Q1–Q11, D10), `03a`, `03g`, `04` Abschn. 1 + 5 (V1/V2, K2/K7/K8: Testlänge, Testreife-Pool, Zwillinge), `00-quellen` D. |
| 6 | `CLAUDE.md` im Repo | `docs/00-masterprompt.md`, **`04a`** (Policy-Schicht D16, Zustandsmodell, Events, Automaten, Konstanten), **`04b`** (Testfälle = Vitest-Spezifikation), `geraetecheck.md`. |
| 7 | `CLAUDE.md` im Repo | `04b` (Logiktests), `04` Abschn. 6 (Pilot-Kennzahlen: Testreife-Wert vs. Testergebnis, Abbrüche), `04c` (Kalibrierung). |

`01-ressourcen.md` (vollständiges Quellenregister Q01–Q99, Widersprüche W1–W11, Lücken L1–L17) nur bei Quellenarbeit öffnen. `03f-richtplan.tsv` nur bei Bedarf (Tagesplan je Pensum).

---

## 7. Ergebnis Phase 3 + 3R (Kernzahlen)

- **39 Kapitel** (A1 20 · A2 19), Kapitel Ø 226 min (Input, Üben, Test, erwartete Wiederholung), 9–15 Mikro-Lektionen. *(Phase 4 V3: Test 25 statt 30 min, erwartete Wiederholung 46–58 statt 17–24 min je Kapitel.)*
- **Gesamtdauer** (S2, ohne Deckel): 1 h → 234 · 1,5 h → 159 · 1,75 h → 138 · 2 h → 123 Plantage; ≈ 240 Lernstunden (48 % des ÖIF-Richtwerts 500 h). *(Phase 4 V3: 254 · 172 · 150 · 132; ≈ 260 h.)*
- **Leitner S2** (passive ohne Karte, Sets als 1 Karte, Start Fach 2 nach richtigem Test): bei 1,5 h Ø 19 min/Tag, 90-%-Tag 26 min.
- **Meilensteine:** A1-Meilenstein (Sperre) · SIM 1 (Diagnose) · SIM 2 · Generalprobe am Stück · offizieller Modelltest; 3 A1- + 5 A2-Testsätze.
- **Abdeckung 100 %:** 97/97 Sprach-Lernziele · 75/75 WOW · 49/49 Grammatik · 55/55 Redemittel · 7/7 Textsorten · 2.035/2.035 Wortschatz · 29/29 Prüfungsteile ≥ 3× · Prüfungskriterien je Teil gemappt (`03b` Abschn. 8).
- **Entschieden zu 3R (D12, 06.11.2026):** O1 kein 90-Tage-Countdown, UI zeigt Prognose zum Pensum + Etappen · O2 Austrittskriterien wie `03` Abschn. 4.2 · O3 D10-Feinschliff **pragmatisch**: Lücken aus `03g` werden im Content-Batch des jeweiligen Kapitels nebenbei behoben, keine eigene Vorarbeit; L19 nur bei Zweifel nachschlagen · O4 ersetzt durch **D13** (Audio ohne Budget, s. Abschn. 3).

## 8. Ergebnis Phase 4 (Kernzahlen)

- **DOIs Q90–Q99 verifiziert** (H.1 in `00-quellen`); Q99 = Silverman & Barasch 2023 (Streaks); neu Q108 Kulik et al. 1990 (Mastery Learning). IntG-Novelle: Re-Check ab 13.11.2026.
- **Bestehens-Simulation (Variante A):** Bestehen je Versuch bei 20 Items: 92 % Trefferquote → 72 %, 95 % → 89 %; bei 25 Items 61 % bzw. 83 %. Kurs (Zentralfall 0,92, 20 Items + Testreife): 9 von 39 Kapiteln mit Wiederholung, 1,7 mit ≥ 3 Versuchen, +16,6 h gegenüber `03`.
- **Zustandsautomat:** Kurs → Kapitelversuch (Lernteil → Übung → Testreife → Test → Korrektur → Fehler-Review) → Meilenstein/Simulation → Austrittskette → `READY_FOR_EXAM`; Sperren abgeleitet (`chatLocked`). Reducer `(state, event)`, Zeit nur aus Events.
- **Regeln:** R-F, R-T, R-G, R-L, R-K, R-M, R-X, R-C, R-E, R-S, R-D, R-W, R-P, R-PL (`04a`); **174 Testfälle + 11 Invarianten** (`04b`); 25 Randfälle geklärt (Abbruch im Test, Neustart, Datumswechsel, Zeitzone, Uhr, Tabs, Import, Content-Update …).
- **Lose Kopplung (D16):** Policy-Schicht mit Erweiterungspunkten für Spezial-Retries und Kapitel-Skip; `defaultPolicy` lehnt Overrides ab, Verhalten unverändert; 9 Naht-Tests.
- **Neu offen:** L21 (Beleg 95-%-Textabdeckung, Q98 trägt die Regel nicht), Genus-Farbcodierung ohne Beleg nicht Standard.

## 9. Phasen 5–7 – Eckpunkte (nur Orientierung, maßgeblich: Masterprompt)

- **5 Content:** JSON-Schema (`course.json`, `chapter-XX.json` mit `version`/`schemaVersion`), **stabile IDs**, Item-Felder inkl. `instruction`/`explanation` `{de,en,tl}`, `twinIds`, `sourceIds`, `reviewStatus`, `varietyNote`; Vokabeln mit Audio-Quelle nach D13 und Varietätsfeldern (D10). Je Kapitel 9–15 Mikro-Lektionen, Audio nach D13, **Test-Pool ≥ 60 (Test 20 Items, V1), Übungs-Pool mit Testreife-Blöcken (V2)**, ≥ 3 je Disziplin, Test-Pool-Items **≥ 2 Zwillinge** (R-K3), Kapiteltest-Aufgaben ≤ 3 Teile (R-T3), ≥ 20 % Recycling. Max. 2 Kapitel pro Batch → automatische QA (`scripts/qa/`, inkl. Wortschatz- und Varietäts-Check) → Prüfer-Agent mit frischem Kontext (≥ 20 % Stichprobe) → menschliche Freigabe. Produktion bleibt dem 2-h-Tempo voraus; B01–B05 vor Tag 1.
- **6 App:** SvelteKit (Repo `speakaustrian`; Adapter, Speicher, i18n offen → `docs/spec-gaps.md`), TS, `zod`, Vitest/Playwright; Core als reine Funktionen (`makeReducer(policy)` → `reducer(state, event)`, Regeln in `defaultPolicy`, D16; Zustandsmodell und Konstanten `04a`); Ports `TutorPort`, `FeedbackPort`, `StoragePort`, `FileOutPort`, `FileInPort`, `SpeechInPort`, `SpeechOutPort` (vorerst nur Geräte-TTS, D17b); Artifact-Regeln (keine externen Requests außer erlaubter CDNs, kein `alert/confirm/prompt`, 16 MB je Datei, kein Mikrofon → Audio-Upload).
- **7 Test:** Logiktests aller Regeln (`04b`), 10 %-Inhaltsaudit im frischen Kontext, Pilot Kapitel 1 mit echter Lernender (Kalibrierung Zeitmodell, Testreife-Wert vs. Testergebnis, `04c`), Abnahmekriterien laut Masterprompt.
