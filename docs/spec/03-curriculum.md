# 03 – Curriculum & Plan (Phase 3, **Revision 3R**): mastery-basiertes Zeitmodell, Richtplan, Bestehenssicherheit

> **Projekt:** „Weg zur A2“ · **Phase:** 3R · **Stand:** 06.11.2026
> **Grundlage:** `00-masterprompt.md` (Rev. 3R) · `00-kurzfassung.md` · Phase-3-Ergebnisse (`03`, `03a`–`03e`) · Entscheidungen **D7–D11** (bestätigt 06.11.2026) · `00-quellen.md` A–C · `prototyp-erkenntnisse.md` E-P1–E-P3
> **Teil-Dokumente:** `03a` Kapitel-Spezifikation (Rev. 3R) · `03b` Abdeckung + Kriterien-Mapping (Rev. 3R) · `03c`/`03d` Wortschatz (unverändert) · `03e` Planungsskript Phase 3 (Zuordnung, Inventar – unverändert gültig) · **`03e2`** Planungsskript 3R (Zeitmodell, Leitner, Richtplan, Freigabe) · **`03f`** Richtplan je Tag (TSV, 4 Tagespensen) · **`03g`** Varietäten AT/DE (D10)

> **Revision:** Diese Fassung **ersetzt** Abschn. 1–8 und 10–12 der Phase-3-Fassung. Ersetzt wurden das Zeitbudget 135 h, der 90-Tage-Kalender, der Leitner-Deckel 25 min und der Freigabeplan auf Basis Plantag 90. Unverändert gelten: Kapitelzuschnitt (39 Kapitel), Wortschatz-Zuordnung (`03c`), Grammatik-Progression, Abdeckung. Alle Zahlen erzeugt `03e2` (`model3r.py` → `writer3r.py`).


---

## 0. Was D7–D11 ändern (Widersprüche benannt)

| Thema | Phase 3 (alt) | Revision 3R (neu) | Grund |
|---|---|---|---|
| Zeitrahmen | fix 90 Tage × 1,5 h = 135 h | **kein Enddatum**; Dauer folgt aus dem Inhalt; Tagespensum 1–2 h ist das Tempo | D7, D11 |
| Kapiteldauer | aus Kalender abgeleitet (netto Ø 107 min) | aus dem Inhalt abgeleitet (D8): Ø 226 min | D8 |
| Wiederholung | Vorschlag 25 min/Tag + 60 min Wochenreview, Rückstau möglich | **ohne Deckel**: fällige Queue jeden Tag vollständig | D7 |
| Kalender | Plantag 1–90 fest | **Richtplan** je Tagespensum, offene Plantage, Etappen statt Enddatum | D7 |
| Simulationen | MS-A1, SIM 1, SIM 2, Generalprobe (je 1 Testsatz) | dazu **Austrittskriterien** (2 Simulationen in Folge ≥ 75 % je Teil) + offizieller Modelltest; 8 eigene Testsätze | D11 |
| Kapitelgröße (Masterprompt 3.2) | ≈ 2–3 h | ≈ 3–4,5 h (D8-Qualität) – **Abweichung vom Masterprompt-Richtwert, dort angepasst** | D8 |
| Mikro-Lektionen (Masterprompt 5.2) | 8–12 | **9–15** à 8–10 min (aus Inhalt berechnet) | D8 |
| AT/DE | AT Hauptform, DE als Hinweis „wo prüfungsrelevant“ | DE-Formen **immer** gekennzeichnet, Varietät ist Lernziel | D10 |
| WOW-Lernziele | 14 neue vorgeschlagen (O3) | übernommen | D9 |

---

## 1. Ergebnis in Zahlen

| Baustein | Wert |
|---|---|
| Kapitel | 39 (A1 20 · A2 19), unverändert |
| Kapitelarbeit (Input + Üben + Test + erwartete Wiederholung) | **146,6 h** = Ø 226 min je Kapitel (Spanne 189–268) |
| Gesamt-Lernzeit bis „prüfungsreif“ (S2, Mittel aus 5 Läufen) | **240,4 h** bei 1,5 h/Tag (Spanne 239,6–241,4 h über alle Tagespensen) |
| Plantage bis „prüfungsreif“ | 1 h/Tag: **234** · 1,5 h/Tag: **159** · 1,75 h/Tag: **138** · 2 h/Tag: **123** |
| Leitner ohne Deckel (S2, 1,5 h) | Ø 18,9 min/Tag · 90-%-Tag 25,8 · Max 57,4 min |
| Vergleich ÖIF-Richtwert 500 h A1+A2 (Q107) | 240,4 h = **48 %** |
| Abdeckung | 97/97 Sprach-Lernziele · 75/75 WOW · 49/49 Grammatik (0 Voraussetzungsfehler) · 55/55 Redemittel · 7/7 Textsorten · 2.035/2.035 Einträge · 29/29 Prüfungsteile ≥ 3× – unverändert ✅ |
| Testsätze | 3 A1 (1 + 2 Reserve) · 5 A2 (SIM 1, SIM 2, Generalprobe, 2 Reserve) + offizieller Modelltest (Link) |

---

## 2. Zeitmodell mastery-basiert

### 2.1 Kapiteldauer aus dem Inhalt (D8)

Statt „Kalender ÷ Kapitel“ wird jedes Kapitel aus seinen Bausteinen gerechnet. Die Minutenwerte sind **Annahmen** für hochwertigen Content (Audio, authentische Situation, Erklärung mit Warum, Abruf statt Lesen) und werden im Pilot A1-01 (Phase 7) kalibriert.

| Baustein | Minuten | Begründung |
|---|---|---|
| Einstieg (Situation, Kann-Ziele) | 5 | Ziel vorab sichtbar → Orientierung, weniger Cognitive Load |
| je aktivem Wort | 0,8 | Audio „Artikel – Pause – Nomen – Wortgruppe“ (E-P1), Bild/Beispiel, erster Abruf |
| je passivem Wort | 0,3 | einmal im Kontext hören/erkennen (D4: rezeptiv) |
| je Set (Zahlen, Monate …) | 8 | Reihen-Drill mit Audio |
| je neuem Grammatikthema | 20 | Regel mit Warum, Beispiele, geführte Übung; ohne neues Thema 10 min Wiederholung im Kontext |
| je Kann-Ziel | 5 | eine authentische AT-Situation (Dialog/Text mit Audio) |
| je Redemittel / WOW-Lernziel / Textsorte | 2 / 4 / 6 | Chunk-Training · Lernkarte mit Quelle · Muster + Leitpunkte |
| Varietäten-Fenster (D10) | 3 | AT/DE-Kontrast, Aussprache, Genus |
| Üben | 40 Items × 0,75 + 3 je Prüfungsformat + Schreiben 10 (vor A1-16: 5 gelenkt) + Sprechaufnahme 8 | ≥ 20 % Recycling-Items (Interleaving) |
| Kapiteltest | 25 Items × 1,0 + 5 Feedback | Planwert, Länge legt Phase 4 fest |
| Prüfungstraining-Kapitel (A1-20, A2-19) | + 30 | Teilsimulationen |
| Erwartete Wiederholung (Variante A) | 15 % × (60 % Lernteil + Test) | `[ANNAHME]`, Phase 4 ersetzt die Quote durch die Bestehens-Simulation |

| Kapitel | Input | Üben | Test | Erw. Wiederh. | **Summe min** | Mikro-Lektionen | Audio min (≈ MB) |
|---|---|---|---|---|---|---|---|
| `A1-01` | 124 | 52 | 30 | 20 | **227** | 14 | 22,8 (≈ 4,0) |
| `A1-02` | 131 | 52 | 30 | 21 | **234** | 15 | 26,7 (≈ 4,7) |
| `A1-03` | 118 | 55 | 30 | 20 | **223** | 13 | 23,1 (≈ 4,1) |
| `A1-04` | 87 | 55 | 30 | 17 | **189** | 10 | 18,8 (≈ 3,3) |
| `A1-05` | 100 | 55 | 30 | 18 | **203** | 11 | 20,9 (≈ 3,7) |
| `A1-06` | 112 | 55 | 30 | 20 | **217** | 12 | 18,2 (≈ 3,2) |
| `A1-07` | 122 | 58 | 30 | 21 | **231** | 14 | 23,2 (≈ 4,1) |
| `A1-08` | 116 | 58 | 30 | 20 | **225** | 13 | 21,6 (≈ 3,8) |
| `A1-09` | 118 | 61 | 30 | 21 | **230** | 13 | 16,1 (≈ 2,8) |
| `A1-10` | 126 | 58 | 30 | 21 | **235** | 14 | 23,1 (≈ 4,1) |
| `A1-11` | 104 | 61 | 30 | 19 | **214** | 12 | 22,2 (≈ 3,9) |
| `A1-12` | 86 | 58 | 30 | 17 | **192** | 10 | 20,4 (≈ 3,6) |
| `A1-13` | 86 | 58 | 30 | 17 | **192** | 10 | 20,5 (≈ 3,6) |
| `A1-14` | 118 | 64 | 30 | 21 | **233** | 13 | 19,2 (≈ 3,4) |
| `A1-15` | 116 | 58 | 30 | 20 | **225** | 13 | 21,8 (≈ 3,8) |
| `A1-16` | 113 | 66 | 30 | 21 | **230** | 13 | 23,9 (≈ 4,2) |
| `A1-17` | 107 | 66 | 30 | 20 | **223** | 12 | 18,7 (≈ 3,3) |
| `A1-18` | 99 | 66 | 30 | 19 | **214** | 11 | 16,9 (≈ 3,0) |
| `A1-19` | 106 | 69 | 30 | 20 | **225** | 12 | 24,2 (≈ 4,3) |
| `A1-20` | 82 | 108 | 30 | 22 | **242** | 9 | 19,8 (≈ 3,5) |
| `A2-01` | 106 | 60 | 30 | 19 | **215** | 12 | 22,4 (≈ 3,9) |
| `A2-02` | 118 | 63 | 30 | 21 | **232** | 13 | 18,6 (≈ 3,3) |
| `A2-03` | 128 | 66 | 30 | 22 | **246** | 14 | 18,8 (≈ 3,3) |
| `A2-04` | 136 | 63 | 30 | 22 | **251** | 15 | 26,6 (≈ 4,7) |
| `A2-05` | 118 | 66 | 30 | 21 | **235** | 13 | 24,4 (≈ 4,3) |
| `A2-06` | 103 | 66 | 30 | 20 | **219** | 11 | 21,3 (≈ 3,7) |
| `A2-07` | 101 | 72 | 30 | 20 | **223** | 11 | 20,4 (≈ 3,6) |
| `A2-08` | 132 | 69 | 30 | 23 | **253** | 15 | 22,5 (≈ 4,0) |
| `A2-09` | 130 | 69 | 30 | 22 | **252** | 14 | 20,9 (≈ 3,7) |
| `A2-10` | 109 | 69 | 30 | 21 | **228** | 12 | 25,0 (≈ 4,4) |
| `A2-11` | 101 | 63 | 30 | 19 | **214** | 11 | 23,9 (≈ 4,2) |
| `A2-12` | 115 | 66 | 30 | 21 | **232** | 13 | 26,8 (≈ 4,7) |
| `A2-13` | 115 | 66 | 30 | 21 | **232** | 13 | 19,3 (≈ 3,4) |
| `A2-14` | 108 | 63 | 30 | 20 | **221** | 12 | 20,3 (≈ 3,6) |
| `A2-15` | 114 | 63 | 30 | 20 | **227** | 13 | 26,9 (≈ 4,7) |
| `A2-16` | 94 | 63 | 30 | 19 | **206** | 10 | 21,6 (≈ 3,8) |
| `A2-17` | 114 | 66 | 30 | 21 | **231** | 13 | 23,8 (≈ 4,2) |
| `A2-18` | 98 | 60 | 30 | 19 | **206** | 11 | 15,8 (≈ 2,8) |
| `A2-19` | 94 | 120 | 30 | 24 | **268** | 10 | 31,2 (≈ 5,5) |
| **Summe** | 4305 | 2526 | 1170 | 790 | **8795** = 146,6 h | | 853 min (≈ 150 MB) |

Audio-Mengengerüst: Opus mono 24 kbit/s `[ANNAHME]` → je Kapitel ≈ 2,8–5,5 MB, unter 16 MB je Datei (Artifact-Grenze), wenn Audio je Kapitel in einer oder mehreren Dateien liegt. Die Mengen gelten für selbst erzeugte Hördateien (D13); Wortschatz läuft über Geräte-TTS und braucht keinen Speicher.

### 2.2 Wiederholungslast ohne Deckel (D7)

**Regel:** Die fällige Leitner-Queue wird jeden Tag **vollständig** abgearbeitet, bevor neuer Stoff kommt. Ist sie länger als das Tagespensum, ist der Tag ein reiner Wiederholungstag. Simulationstage: nur Simulation; die an diesem Tag fälligen Karten rutschen auf den Folgetag (verschoben, nicht gestrichen).

**Modell** wie Phase 3 (5 Fächer 1/3/7/14/30 Tage, Trefferquote 80/85/88/90/93 %, Fehler → Fach 1, nach Fach 5 gemeistert), Karten entstehen mit der Kapitelarbeit. **Korrektur gegenüber Phase 3:** Eine Set-Karte (z. B. Zahlen 0–100) ist ein Reihen-Drill und kostet 40 s statt 6 s (Phase 3 hat S1/S2 damit leicht unterschätzt).

| Szenario | 1 h: Ø / 90 % / Max min · Lernstunden · Plantage | 1,5 h: Ø / 90 % / Max min · Lernstunden · Plantage | 1,75 h: Ø / 90 % / Max min · Lernstunden · Plantage | 2 h: Ø / 90 % / Max min · Lernstunden · Plantage |
|---|---|---|---|---|
| S0 – jeder Eintrag eine Karte | 15,5 / 20,2 / 46,0 · 250,3 h · 244 T | 21,8 / 29,2 / 71,9 · 249,8 h · 166 T | 24,8 / 35,3 / 74,9 · 249,8 h · 143 T | 27,5 / 40,3 / 87,7 · 247,3 h · 125 T |
| S1 – passive ohne Karte, Sets als 1 Karte | 14,8 / 19,4 / 41,0 · 247,4 h · 241 T | 20,8 / 28,1 / 52,7 · 246,7 h · 163 T | 23,8 / 33,8 / 69,6 · 247,4 h · 142 T | 26,2 / 38,2 / 81,1 · 246,0 h · 124 T |
| S2 – wie S1 + im Kapiteltest richtig → Start Fach 2 | 13,5 / 18,0 / 43,9 · 240,6 h · 234 T | 18,9 / 25,8 / 57,4 · 240,4 h · 159 T | 21,3 / 29,3 / 71,9 · 239,6 h · 138 T | 23,3 / 34,6 / 72,8 · 241,4 h · 123 T |
| S3 – wie S2 + eigene Genus-Spur für Nomen | 14,7 / 19,5 / 42,8 · 246,7 h · 240 T | 20,7 / 27,9 / 70,5 · 246,0 h · 163 T | 23,4 / 33,7 / 70,2 · 246,6 h · 142 T | 25,6 / 37,2 / 87,1 · 245,2 h · 124 T |

**Bewertung der Entlastungen (S2 gegenüber S0):**

1. **Passive ohne eigene Karte** – didaktisch sauber, weil passive Einträge nur Wiedererkennen verlangen (D4); sie kommen in Lese-/Hörtexten und als Distraktoren wieder. Risiko: passives Wort wird nie wiedergesehen → QA-Regel Phase 5: jedes passive Wort erscheint in ≥ 2 späteren Texten.
2. **Sets als eine Karte** – Reihen-Drill ist für geschlossene Reihen (Zahlen, Monate) der natürliche Abruf; Einzelkarten würden die Reihe zerreißen. Fehler innerhalb der Reihe erzeugen gezielte Einzelkarten.
3. **Start in Fach 2 nach richtigem Kapiteltest** – der Test war ein erfolgreicher Abruf unter Prüfungsbedingungen; ein zweiter Abruf am Folgetag bringt wenig (Spacing-Effekt wächst mit dem Abstand). Fehler starten in Fach 1.

Zusammen sparen sie **9,4 h** bei 1,5 h/Tag (Ø Queue 21,8 → 18,9 min/Tag) – ohne aktive Wörter herabzustufen (D3). **Empfehlung: S2.** S3 zeigt den Preis einer eigenen Genus-Spur (Prototyp E-P2): +5,6 h; Alternative ohne Mehrkosten: Genus als **abwechselnde Richtung derselben Karte** (Entscheidung Phase 4).

Die Queue bleibt auch ohne Deckel beherrschbar: Bei 1,5 h liegt sie an 90 % der Tage unter 26 min; reine Wiederholungstage entstehen in keinem Tagespensum. Spitzen (Max) treten in Wochen mit vielen neuen Wörtern auf und sind Einzeltage.

### 2.3 Gesamtdauer-Prognose (S2, Mittel aus 5 Läufen)

| Tagespensum | Plantage bis prüfungsreif | Lernstunden | Kapitelarbeit | Leitner | Wochenreview | Simulationen | Puffer | Tage über Pensum* | A1-Meilenstein | SIM 1 | SIM 2 | Generalprobe | Modelltest |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 h | **234** | **240,6** | 146,6 | 52,5 | 24,7 | 13,5 | 3,2 | 20 | Tag 110 | Tag 174 | Tag 229 | Tag 232 | Tag 234 |
| 1,5 h | **159** | **240,4** | 146,6 | 50,2 | 25,3 | 13,5 | 4,9 | 13 | Tag 73 | Tag 116 | Tag 155 | Tag 157 | Tag 159 |
| 1,75 h | **138** | **239,6** | 146,6 | 48,8 | 24,7 | 13,5 | 6,1 | 10 | Tag 61 | Tag 100 | Tag 133 | Tag 136 | Tag 138 |
| 2 h | **123** | **241,4** | 146,6 | 47,7 | 26,4 | 13,5 | 7,2 | 7 | Tag 54 | Tag 88 | Tag 118 | Tag 121 | Tag 123 |

\* Simulationstage (Prüfungsformat am Stück) und Wochenreview-Tage mit Mindestdauer 30 min können das Pensum überschreiten; das ist so gewollt.

**Rechnerische Geschlossenheit:** Lernstunden = Kapitelarbeit + Leitner + Wochenreview + Simulationen + Puffer; das Skript summiert je Lauf exakt, die Tabelle zeigt Mittelwerte aus 5 Läufen, gerundet auf 0,1 h (Rundungsdifferenz ≤ 0,1 h). Die Kapitelarbeit ist in jedem Tagespensum gleich (inhaltsbestimmt), Leitner sinkt mit höherem Pensum leicht, weil weniger Kalendertage vergehen und Karten früher „gemeistert“ sind.

**Erwartete Zusatzsimulationen:** Die Austrittsregel verlangt zwei Simulationen in Folge ≥ 75 % (Abschn. 4). Bei einer Teil-Bestehensquote q pro Simulation braucht man im Mittel (1+q)/q² Versuche: q = 0,68 → 3,6, q = 0,91 → 2,3. Jeder Zusatzversuch kostet ≈ 2 Review-Tage + 1–2 Simulationstage → **Prognose-Spanne +0 bis +8 Plantage**.

### 2.4 Realismus-Check

| Vergleich | Umfang | Quelle | Plan 3R (1,5 h) entspricht |
|---|---|---|---|
| ÖIF-Kurs A1 + A2 (Präsenz + Selbstlernzeit) | 500 h | Q107 | **48 %** |
| nur Präsenzanteil ÖIF A1 + A2 | 300 h | Q107 | 80 % |
| Phase-3-Plan (alt) | 135 h | `03` alt | +78 % |

**Bewertung:** Mit vollem Umfang und D8-Qualität liegt der Plan bei knapp der Hälfte des ÖIF-Kursrahmens. Das ist ambitioniert, aber nicht unplausibel: Eins-zu-eins-Tempo ohne Kurs-Leerlauf, hoher Abrufanteil, verteiltes Wiederholen und Prüfungsformat-Fokus verdichten die Zeit. Nicht ersetzt werden echte Gesprächspartner:innen → ÖIF-Kursraum und Online-Kurs Sprechen sind **feste Empfehlung** (Abschn. 4.5). Das alte 90-Tage-Ziel ist mit vollem Umfang **nur mit ≈ 2,7 h/Tag** erreichbar und damit außerhalb von max. 2 h → es bleibt nur als Motivationsgeschichte, nicht als Plan (offene Frage O1).


---

## 3. Richtplan statt fixem Kalender

### 3.1 Regeln

- **Plantag** = Kalendertage seit `startDate` + 1 (unverändert). Es gibt **kein Enddatum**; der Plan endet, wenn die Austrittskriterien erfüllt sind.
- **Tagesablauf:** fällige Wiederholung (vollständig) → Kapitelarbeit bis zum gewählten Tagespensum. Das Tagespensum (1 / 1,5 / 1,75 / 2 h) wählt die Lernende im Onboarding; änderbar.
- **Wochenreview:** jeder 7. Plantag, Interleaving aus allen bisherigen Kapiteln, mind. 30 min, kein neuer Stoff.
- **Puffer:** je ein Tag vor/nach dem A1-Meilenstein, vor/nach SIM 2, nach der Generalprobe; zusätzlich steckt der Erwartungswert für Kapitelwiederholungen in jeder Kapitelzeit (Abschn. 2.1). Ungenutzter Puffer → Schwächen-Review + Sprechpraxis.
- **Meilensteine:** A1-Meilenstein nach A1-20 (Sperre), SIM 1 nach A2-10 (Diagnose), SIM 2 nach A2-19, Generalprobe am Stück, offizieller Modelltest (Abschn. 4).
- Der **vollständige Tagesplan** je Tagespensum steht in `03f-richtplan.tsv` (Spalten: Pensum, Plantag, Typ, Inhalt, Leitner-min, Arbeit-min).

### 3.2 Richtplan 1,5 h/Tag nach Wochen

| Woche | Plantage | Kapitel (Beginn → Ende) / Ereignisse |
|---|---|---|
| 1 | 1–7 | `A1-01` · `A1-02` · `A1-03` |
| 2 | 8–14 | `A1-03` · `A1-04` · `A1-05` |
| 3 | 15–21 | `A1-05` · `A1-06` · `A1-07` |
| 4 | 22–28 | `A1-07` · `A1-08` · `A1-09` |
| 5 | 29–35 | `A1-09` · `A1-10` · `A1-11` |
| 6 | 36–42 | `A1-11` · `A1-12` · `A1-13` |
| 7 | 43–49 | `A1-13` · `A1-14` · `A1-15` |
| 8 | 50–56 | `A1-15` · `A1-16` · `A1-17` |
| 9 | 57–63 | `A1-17` · `A1-18` · `A1-19` |
| 10 | 64–70 | `A1-19` · `A1-20` |
| 11 | 71–77 | `A2-01` · **Tag 71: Puffer vor A1-Meilenstein: gezielte Review schwacher Lernziele; Tag 72: A1-Meilenstein schriftlich; Tag 73: A1-Meilenstein WOW; Tag 74: Puffer nach A1-Meilenstein: Fehler-Review bzw. Vorbereitung 2. Versuch** |
| 12 | 78–84 | `A2-01` · `A2-02` · `A2-03` |
| 13 | 85–91 | `A2-03` · `A2-04` · `A2-05` |
| 14 | 92–98 | `A2-05` · `A2-06` · `A2-07` |
| 15 | 99–105 | `A2-07` · `A2-08` |
| 16 | 106–112 | `A2-08` · `A2-09` · `A2-10` |
| 17 | 113–119 | `A2-10` · `A2-11` · **Tag 115: A2-Simulation 1 schriftlich; Tag 116: A2-Simulation 1 WOW** |
| 18 | 120–126 | `A2-11` · `A2-12` · `A2-13` |
| 19 | 127–133 | `A2-13` · `A2-14` · `A2-15` |
| 20 | 134–140 | `A2-15` · `A2-16` · `A2-17` |
| 21 | 141–147 | `A2-17` · `A2-18` · `A2-19` |
| 22 | 148–154 | `A2-19` · **Tag 152: Puffer vor A2-Simulation 2; Tag 153: A2-Simulation 2 schriftlich + Auswertung** |
| 23 | 155–159 | – · **Tag 155: A2-Simulation 2 WOW + Sprechen + Auswertung; Tag 156: Puffer: gezielte Review nach Simulation 2; Tag 157: A2-Generalprobe am Stück; Tag 158: Puffer: Review nach Generalprobe; Tag 159: Offizieller ÖIF-Modelltest A2 am Stück** |

### 3.3 Prognoselogik „prüfungsreif ab ca. Tag X“

1. **Restaufwand** R = Σ Planminuten der offenen Kapitel × persönlicher Faktor k + offene Simulations-/Pufferblöcke.
2. **Persönlicher Faktor** k = tatsächliche ÷ geplante Minuten der letzten 3 abgeschlossenen Kapitel (gleitender Mittelwert, begrenzt auf 0,6–2,0). Vor dem 3. Kapitel gilt k = 1.
3. **Tempo** v = Kapitelminuten pro Kalendertag über die letzten 14 Tage (Pausentage zählen mit – ehrliche Prognose). Vor Tag 14: Richtwert aus Abschn. 2.3 für das gewählte Pensum.
4. **Prognose** X = heute + ⌈R ÷ v⌉ + Anzahl künftiger Wochenreview-Tage im Zeitraum. Angezeigt als Spanne ±15 % und als Lernstunden („noch ca. 140 h“).
5. **Was-wäre-wenn:** „Mit +15 min/Tag: ca. N Tage früher“ – berechnet mit derselben Formel. Nie: „Du bist im Rückstand“.

### 3.4 Motivationsanker (ohne Druck zum Kürzen)

- **Etappenleiste** statt Countdown: 39 Kapitel + 5 Meilensteine; jede Etappe mit Lernstunden-Anteil (z. B. „A1 geschafft = 46 % des Weges“).
- **Tempo-Anzeige** in Kapitel/Woche gegen das selbst gewählte Pensum, nicht gegen ein Enddatum. Schneller sein wird gefeiert, langsamer sein ist neutral.
- **Qualität vor Tempo sichtbar:** Kapitel bestanden = alle Disziplinen richtig (Phase 4). Es gibt keinen Weg, Inhalte zu überspringen, um schneller zu sein (D11).
- **Tagesziel und Streak** bleiben (Entscheidungen 3/4); „alle fälligen Wiederholungen“ ist durch D7 ohne Deckel definiert.
- **Wochenrückblick** am Wochenreview-Tag: gelernte Wörter, gemeisterte Karten, Lernstunden – Fortschritt, den man sieht (Kompetenzerleben).


---

## 4. Bestehenssicherheit (D11)

### 4.1 Prüfungskriterien → Kapitel und Aufgabentypen

Vollständige Matrix mit Kapitellisten in `03b` Abschn. 8. Kurzfassung:

| Prüfung | Teil | offiziell (Punkte · Bestehen) | Tool-Schwelle ≥ 75 % | geübt in Kapiteln | Kriterien → Aufgabentypen |
|---|---|---|---|---|---|
| A1 | Sprachbausteine | 60 P · Ausgleich über Gesamt ≥ 240/400 | ≥ 45/60 | 11 | MC-Lückentext, Grammatik-Drills G01–G28 |
| A1 | Hören | 68 P · s. o. | ≥ 51/68 | 11 | R/F Alltagstext 2×, Zahlen/Buchstaben 2× |
| A1 | Hören und antworten | 56 P · s. o. | ≥ 42/56 | 13 | Reaktion wählen, Redemittel R-SP |
| A1 | Lesen | 96 P · s. o. | ≥ 72/96 | 15 | Überschrift, R/F E-Mail, Anzeige wählen |
| A1 | Schreiben | 40 P · s. o. | ≥ 30/40 | 5 | Formular (Eigennamen/Zahlen ohne Toleranz), Nachricht 30 Wörter: 3 Leitpunkte + kommunikative Gestaltung |
| A1 | Sprechen | 80 P · s. o. | ≥ 60/80 | 16 | Vorstellen + buchstabieren, Fragen mit Wortkarten, Bitten/Reaktion |
| A1 | WOW | 45 P · ≥ 25/45 Pflicht | ≥ 34/45 | 20 | a/b- und a/b/c-Fragen, Lernkarten mit Quelle |
| A2 | Lesen | 20 P · L + H ≥ 25/50 | ≥ 15/20 | 18 | Zuordnung, MC, Formular-Lücken (Distraktoren Ziffern/Datum/Umlaut), Infotext |
| A2 | Hören | 30 P · L + H ≥ 25/50 | ≥ 23/30 | 17 | Mobilbox 2×, Radio/Durchsage 1×, Gespräche R/F 1× – Wiedergabe exakt wie Prüfung |
| A2 | Schreiben | 20 P · ≥ 10/20 | ≥ 15/20 | 10 | (1) Vollständigkeit → Leitpunkt-Zuordnung, Schlüsselbegriff-Check · (2) kommunikative Realisierung → Anrede/Gruß, Register, Textsorten T-01–T-07 · (3) Wortschatz → Leitner, Diktat · (4) Grammatik → Drills, Satzbau |
| A2 | Sprechen | 30 P · ≥ 15/30 | ≥ 23/30 | 17 | Kommunikative Kompetenz → Kontaktgespräch, Bildbeschreibung + Rollenspiel mit ≥ 2 eigenen Fragen · formale Richtigkeit → Satzklammer G49 · Aussprache → Audio-Nachsprechen, Aufnahme-Vergleich |
| A2 | WOW | 45 P · ≥ 25/45, sonst ganze Prüfung nicht bestanden | ≥ 34/45 | 19 | 18 Fragen, ≥ 1 je Wertebereich, keine Teilpunkte |

Punkte und Bestehensregeln: `00-quellen.md` A/B (Q05, Q06, Q09, Q10). Punkte je Kriterium A2 Schreiben/Sprechen bleiben unbelegt (L1/L2) → Tool-Raster aus `02g` als `[ANNAHME]`.

### 4.2 Austrittskriterien „prüfungsreif“ (Vorschlag, in Phase 4 als Zustand festschreiben)

Alle müssen erfüllt sein, bevor das Tool „Jetzt zur Prüfung anmelden“ empfiehlt:

1. **Alle 39 Kapitel bestanden** (jede Disziplin, ggf. über Korrekturrunde).
2. **A1-Meilenstein bestanden** – ≥ 75 % je Subtest (E3).
3. **Zwei aufeinanderfolgende vollständige A2-Simulationen ≥ 75 % in jedem Teil** (Lesen, Hören, Schreiben, Sprechen, WOW) mit unterschiedlichen Testsätzen; die zweite **am Stück** im echten Ablauf (Generalprobe). SIM 1 zählt nicht (Diagnose mitten im A2-Stoff).
4. **Offizieller ÖIF-Modelltest A2** (Link, Q05) am Stück durchgeführt: Lesen/Hören/WOW selbst ausgewertet ≥ 75 %; Schreiben/Sprechen mit Checkliste + KI-Feedback (Entscheidung 5). Externer Abgleich, weil eigene Tests das eigene Format bestätigen.
5. **Wiederholung im Griff:** keine Leitner-Karte mehr als 7 Tage überfällig; alle Fehler-Zwillinge der letzten Simulation erledigt.
6. **Sprechen mit Menschen** (Selbstauskunft, feste Empfehlung, nicht sperrend): ≥ 6 Einheiten ÖIF-Kursraum oder Online-Kurs Sprechen ab A2-01.

Fällt eine Simulation unter 75 % in einem Teil: 2 Review-Tage für die schwächsten Lernziele (automatisch aus der Fehleranalyse), danach nächster Reserve-Testsatz; die Zählung „zwei in Folge“ beginnt neu.

### 4.3 Simulationen und Testsätze

| Paket | Testsätze | Einsatz |
|---|---|---|
| A1 | 3 (MS-A1 + 2 Reserve) | Sperre vor A2; Reserve für 2./3. Versuch |
| A2 | 5: SIM 1 (Diagnose), SIM 2, Generalprobe, Reserve R1, R2 | Austrittsregel; R1/R2 decken den Erwartungswert bis q ≈ 0,68 |
| extern | offizieller Modelltest A2 (+ weitere offizielle Übungstests als Link, L4) | Abgleich vor Anmeldung |

Jeder Testsatz ist vollständig eigenständig (keine Items aus Kapitel-Pools, keine Überschneidung zwischen Sätzen); WOW je Satz 18 neue Fragen mit ≥ 1 je Wertebereich.

### 4.4 Quantitative Abschätzung (objektiv auswertbare Teile)

Binomialmodell: Lernende beantwortet jedes Item mit Wahrscheinlichkeit p richtig (Lesen 20 Items, Hören 15 Items à 2 P, WOW 9 × 2 P + 9 × 3 P). „Tool“ = Lesen, Hören und WOW einer Simulation je ≥ 75 % (Schreiben/Sprechen nicht modelliert); „Austritt“ = zweimal in Folge; „echt“ = offizielle Regel (L + H ≥ 25/50 und WOW ≥ 25/45); „schlechter Tag“ = p − 15 Prozentpunkte am Prüfungstag.

| p | Tool-Simulation bestanden | Austritt (2 in Folge) | echte Prüfung (L/H/WOW) | echte Prüfung, schlechter Tag |
|---|---|---|---|---|
| 0,65 | 0,9 % | 0,0 % | 79,33 % | 19,6 % |
| 0,70 | 4,4 % | 0,2 % | 90,90 % | 39,2 % |
| 0,75 | 15,3 % | 2,4 % | 96,81 % | 61,2 % |
| 0,80 | 38,0 % | 14,5 % | 99,19 % | 79,3 % |
| 0,85 | 67,9 % | 46,1 % | 99,88 % | 90,9 % |
| 0,90 | 90,8 % | 82,4 % | 99,99 % | 96,8 % |

**Lesart:** Wer die Austrittsregel realistisch schafft (p ≈ 0,85 und mehr), besteht Lesen/Hören/WOW der echten Prüfung im Modell mit > 99 %, selbst an einem schlechten Tag mit ≈ 91 %. Die 75-%-Schwelle in zwei Simulationen filtert Zufallstreffer heraus: Bei p = 0,75 gelingt der Austritt nur in ≈ 2 % der Fälle. **Grenzen:** Items sind in Wahrheit unterschiedlich schwer, und Lernende sind nicht über alle Themen gleich stark; Schreiben und Sprechen sind nicht modelliert (Bewertung durch Menschen).

### 4.5 Restrisiken (ehrlich) und Gegenmaßnahmen

| Restrisiko | Warum das Tool es nicht ganz schließt | Gegenmaßnahme |
|---|---|---|
| Sprechen mit echten Prüfer:innen | Artifact ohne Mikrofon (Audio-Upload), keine Live-Interaktion, Bewertung im Tool nur Checkliste/KI | **feste Empfehlung** ÖIF-Kursraum A1/A2 und Online-Kurs Sprechen (Q40–Q42) ab A1-05 bzw. A2-01, mind. 2×/Woche; Austrittskriterium 6 |
| Schreiben-Bewertung | Punkte je Kriterium unbelegt (L1); KI-Feedback ist Lernhilfe | zwei Musterlösungen, Leitpunkt-Checks, keine Mustertexte (Plagiat § 13c) |
| Tagesform, Prüfungsangst | im Modell nur als −15 pp | Generalprobe am Stück, Prüfungsablauf-Lektion, Pausenregeln wie echt |
| Unbekannte Stimmen/Varietäten im Hören | Tool-Audio meist AT-Standard (D10) | ab A2 einzelne Hörtexte mit DE-Sprecher:in, gekennzeichnet (L18) |
| Formatänderung durch IntG-Novelle | Begutachtung bis 12.11.2026 (E1) | Re-Check ab 13.11.2026 (Trigger `00-quellen` F) |

**Keine Garantie:** Das Tool kann die Bestehenswahrscheinlichkeit messbar erhöhen und ehrlich anzeigen, aber das Ergebnis der echten Prüfung nicht garantieren. So wird es auch in der App formuliert.


---

## 5. Qualitätsstandard Content (D8) – prüfbare Mindestkriterien je Kapitel

| # | Kriterium | Prüfbar durch (Phase 5) |
|---|---|---|
| Q1 | **Mikro-Lektionen:** 9–15 je Kapitel (aus Inhalt berechnet, Tabelle 2.1), je 8–10 min, je **ein** Lernziel, jede endet mit ≥ 1 Abrufaufgabe | QA-Skript: Anzahl, Dauer-Schätzung, `learningGoalIds` je Lektion |
| Q2 | **Audio (D13):** 100 % des Wortschatzes (Lemma mit Artikel, „Artikel – Pause – Nomen – Wortgruppe“) über Geräte-TTS (gehärtet, Prototyp v4); 100 % der Hörtexte im Prüfungsformat als **kostenlos selbst erzeugte** Dateien, ≥ 2 Stimmen; Transkript als Rückfall; kein kostenpflichtiges Audio | QA-Skript: jede Vokabel/jeder Hörstimulus hat `audio`-Datei; Stimmenliste |
| Q3 | **Authentische AT-Situation:** ≥ 1 Leitsituation je Kann-Ziel mit realem österreichischem Ort/Ablauf (Magistrat, Ordination, Öffis, Trafik …); Realia im AT-Format (Datum TT.MM.JJJJ, „€ 3,50“, +43, PLZ 4-stellig) | Prüfer-Agent (Natürlichkeit), Regex-Checks Formate |
| Q4 | **Echtes Prüfungsformat:** Prüfungsitems exakt wie `02g` (Optionenzahl, Textsorte, Hörhäufigkeit, Lesezeit); Hörwiederholung wie Prüfung | QA-Skript gegen Format-Tabelle je `examPart` |
| Q5 | **Erklärungen mit Warum:** jedes Item erklärt, warum richtig **und** warum jeder Distraktor falsch ist; Grammatik mit Regel-Logik, nicht nur Tabelle; `de`/`en`/`tl` | QA: `explanation` je Option nicht leer; Prüfer-Agent Stichprobe |
| Q6 | **Zwillinge:** jedes Item ≥ 1 Zwilling (gleiches Lernziel, andere Oberfläche); Pool ≥ 60 und ≥ 2,5 × Test | QA-Skript (bestehend, 5.11) |
| Q7 | **Produktion:** je Kapitel ≥ 1 Sprechaufnahme; ab A1-16 ≥ 1 freie Schreibaufgabe mit 3 Leitpunkten (vorher gelenkt); ≥ 2 Musterlösungen, nie zum Auswendiglernen | QA-Zählung; Plagiat-Hinweis im Item |
| Q8 | **Interleaving:** ≥ 20 % der Übungsitems recyceln Stoff früherer Kapitel; jedes passive Wort in ≥ 2 späteren Texten | QA über `learningGoalIds` und Wortschatz-Index |
| Q9 | **Kein Slop:** kein isoliertes Wort-Raten als Haupttest, keine sinnfreien Sätze, keine Belohnung ohne Lernhandlung; ≤ 5 % unbekannte Wörter je Text; plausible Distraktoren | Prüfer-Agent mit Checkliste; Wortschatz-Check (5.11) |
| Q10 | **Varietät (D10):** AT-Hauptform in allen Lerntexten, DE-Formen nur gekennzeichnet (Abschn. 6) | QA-Skript `variety.py` |
| Q11 | **Werte-Fakten** mit Quelle und Stand (`sourceIds`); offene 🔶/❌ vor Freigabe geschlossen | QA (bestehend) |

**Mengengerüst angepasst** (Masterprompt 5.2): Mikro-Lektionen **9–15** statt 8–12 (Grund: Inhalt pro Kapitel + D8-Tiefe, Kapitel ≈ 3–4,5 h); Pool ≥ 60, Test 20–30, ≥ 3 je Disziplin, ≥ 1 Zwilling bleiben; neu: Audio nach D13, ≥ 20 % Recycling, ≥ 1 Sprechaufnahme.


---

## 6. Österreichisches Deutsch als Lernziel (D10)

### 6.1 Datenfelder (Inventar und Items, Phase 5)

| Feld | Werte | Zweck |
|---|---|---|
| `variety` | `AT` · `AT+DE` (gemeinsam) · `DE` · `AT-Institution` | Varietät des Eintrags |
| `variantDe` | `{ lemma, article?, note? }` | bundesdeutsche Entsprechung eines AT-Eintrags (ohne eigenen Eintrag) |
| `mainFormId` | Inventar-ID | bei `DE`-Einträgen: Verweis auf die AT-Hauptform |
| `varietyFeature` | `lexik` · `genus` · `perfekt` · `aussprache` · `schreibung` · `bedeutung` | Art des Unterschieds |
| `genusAt` / `genusDe` | der/die/das | bei Genus-Unterschied |
| `perfAux` | `{ at: 'sein', de: 'haben' }` | sitzen/stehen/liegen |
| `pronAt` | Hinweis/IPA | AT-Aussprache (z. B. -ig [ɪk]) |
| Item: `varietyNote` | `{ de, en, tl }` | Feedback-Hinweis, wenn DE-Form verwendet wurde |

Die bisherige Spalte `at` (0/1) und `kind=dvar` gehen verlustfrei in `variety` auf.

### 6.2 Anzeige

| Modus | Regel |
|---|---|
| Lernmodus | AT-Form groß; DE-Form als Chip **„in Deutschland: Tomate“** unter dem Wort (nie umgekehrt). DE-Einträge erscheinen nur als Chip oder in einer markierten Mini-Lektion „Das hörst du auch“. |
| Übungen | Abgefragt wird die AT-Form. Eine DE-Form in Freitext/Lücken gilt als **richtig mit Hinweis** (Standarddeutsch ist plurizentrisch). |
| Prüfungsmodus | Stimulus und Optionen **nur AT-Formen**; DE-Formen nie als Option oder Distraktor (sonst zwei richtige Antworten). Varietäts-Hinweise erst im Feedback. |
| Schreiben/Sprechen frei | DE-Formen werden nicht abgewertet; regelbasiertes Feedback nennt die AT-Form. Ob ÖIF-Bewerter:innen DE-Formen neutral werten, ist unbelegt (L20) → Tool trainiert AT als sichere Wahl. |
| Audio | AT-Aussprache; DE-Sprecher:innen nur gekennzeichnet (Abschn. 4.5). |

### 6.3 QA-Regel Phase 5 (`scripts/qa/variety.py`)

1. Jedes Token in `stimulus`, `options`, Lektionstext und `explanation.de` wird gegen die DE-Liste geprüft (`variety=DE` + alle `variantDe`). Treffer ohne Kennzeichnung (`varietyNote` bzw. Chip-Markup) → **Fehler**.
2. Prüfungsitems: Treffer der DE-Liste in Stimulus/Optionen → **Fehler**, ohne Ausnahme.
3. Perfekt von sitzen/stehen/liegen mit *haben* in Lerntexten → Fehler; Genus gegen `genusAt`.
4. Neue Lemmata im Content, die nicht im Inventar stehen, werden gegen eine Austriazismen-/Teutonismen-Liste geprüft (Quelle vor Phase 5 festlegen, L19).
5. Bericht je Batch: Anzahl AT/DE-Treffer, Kennzeichnungsquote (Ziel 100 %).

### 6.4 Prüfung des Inventars (Ergebnis)

Durchgesehen: vollständige Liste `03c` (2.035 Einträge, darunter die 132 AT- und 14 DE-Varianten-Einträge). Die 14 DE-Einträge sind korrekt mit ihrer AT-Hauptform verknüpft (Liste `03g`). **Lücken: 10** – vor allem Kartoffel (unmarkiert), Mütze/Haube (AT-Form nur passiv) und Stuhl/Sessel (Falscher Freund). Rund 90 AT-Einträge brauchen das Feld `variantDe` nachgetragen; Einzelheiten und Vorschläge in `03g`.


---

## 7. Freigabeplan (Just-in-time, Maßstab: schnellstes Tempo)

**Regel:** Die Produktion muss der **schnellsten** zulässigen Lernenden (2 h/Tag) voraus sein – wer langsamer lernt, hat dann automatisch mehr Vorlauf. Jedes Batch ist fertig spätestens (a) 10 Plantage vor seinem ersten Kapiteltag bei 2 h/Tag **und** (b) wenn die Lernende das Kapitel fünf Positionen davor beginnt. „≤ 0“ = vor Tag 1. Ein Batch = max. 2 Kapitel (Masterprompt 5.10).

| Batch | Kapitel | erster Kapiteltag (2 h) | spätestens fertig (Plantag) | bei 1,5 h erster Tag |
|---|---|---|---|---|
| B01 | `A1-01` + `A1-02` | 1 | ≤ 0 | 1 |
| B02 | `A1-03` + `A1-04` | 4 | ≤ 0 | 6 |
| B03 | `A1-05` + `A1-06` | 9 | ≤ 0 | 12 |
| B04 | `A1-07` + `A1-08` | 13 | 2 | 18 |
| B05 | `A1-09` + `A1-10` | 19 | 8 | 25 |
| B06 | `A1-11` + `A1-12` | 24 | 11 | 33 |
| B07 | `A1-13` + `A1-14` | 30 | 16 | 39 |
| B08 | `A1-15` + `A1-16` | 34 | 22 | 46 |
| B09 | `A1-17` + `A1-18` | 40 | 26 | 54 |
| B10 | `A1-19` + `A1-20` | 45 | 31 | 61 |
| B11 | `A2-01` + `A2-02` | 57 | 37 | 75 |
| B12 | `A2-03` + `A2-04` | 61 | 43 | 82 |
| B13 | `A2-05` + `A2-06` | 67 | 47 | 90 |
| B14 | `A2-07` + `A2-08` | 73 | 59 | 97 |
| B15 | `A2-09` + `A2-10` | 79 | 65 | 106 |
| B16 | `A2-11` + `A2-12` | 89 | 71 | 117 |
| B17 | `A2-13` + `A2-14` | 95 | 76 | 124 |
| B18 | `A2-15` + `A2-16` | 101 | 82 | 132 |
| B19 | `A2-17` + `A2-18` | 106 | 92 | 139 |
| B20 | `A2-19` | 111 | 97 | 146 |

| Testsatz-Paket | Inhalt | spätestens fertig (Plantag, 2 h) |
|---|---|---|
| T-A1 | A1-Meilenstein: 3 Testsätze (1 + 2 Reserve) | 37 |
| T-S1 | A2-Simulation 1: 1 Testsatz | 71 |
| T-S2 | A2-Simulation 2 + Generalprobe + 2 Reserve: 4 Testsätze | 101 |

**Startbedingung:** App + 3 Batches (A1-01–A1-06) vor Tag 1. **Empfehlung** wegen D8-Aufwand je Kapitel (Audio, Zwillinge, Prüfer-Agent): **B01–B05 (A1-01–A1-10) vor Tag 1** – das sind bei 2 h/Tag ≈ 23 Plantage Vorlauf. Danach braucht die Produktion im Schnitt ein Batch alle 5,8 Plantage (bei 2 h-Tempo); bei 1,5 h-Tempo alle 7,5.


---

## 8. Risiken und Gegenmaßnahmen (aktualisiert)

| # | Risiko | Wirkung | Gegenmaßnahme | Wo |
|---|---|---|---|---|
| R1 | Gesamtumfang 240,4 h vs. ÖIF 500 h | Dauer länger als erhofft, Motivation | Prognose ehrlich, Etappen statt Countdown, Pensum frei wählbar | Abschn. 2.3, 3.4 |
| R2 | Wiederholungslast ohne Deckel | Spitzentage | S2-Entlastungen; Queue an 90 % der Tage ≤ 26 min (1,5 h) | Abschn. 2.2 |
| R3 | Variante A (Entscheidung 1) häufiger als 15 % | Prognose zu optimistisch | Phase 4: Testlänge per Simulation; Faktor k in Prognose | Abschn. 2.1, 3.3 |
| R4 | Zeitannahmen D8 falsch | Kapitel dauern länger/kürzer | Pilot A1-01 (Phase 7), Kalibrierfaktor k | Abschn. 2.1 |
| R5 | Sprechen ohne Gesprächspartner | Sprechen ≥ 15/30 unsicher | ÖIF-Kursraum/Online-Kurs Sprechen als feste Empfehlung, Austrittskriterium 6 | Abschn. 4.5 |
| R6 | Audio ohne Budget (D13): Geräte-TTS instabil/ohne deutsche Stimme (E-P1, E-P3), AT-Aussprache nicht garantiert | Hören-Training unzuverlässig | Stufenmodell D13, Audio-Spike + Gerätecheck vor erstem Audio-Batch; Hörtexte im Prüfungsformat als selbst erzeugte Dateien | Abschn. 5, 11.1 |
| R7 | Tagalog-Qualität (E2) | Missverständnisse | einfache Sprache, `machine`-Status, Review anstreben | E2 |
| R8 | IntG-Novelle 2027 (E1) | Formatänderung | Re-Check ab 13.11.2026 | E1 |
| R9 | Produktions-Engpass (D8 + 8 Testsätze) | Lernende wartet | B01–B05 vor Start, Maßstab 2 h-Tempo | Abschn. 7 |
| R10 | Austrittsregel zu streng | Frust durch wiederholte Simulationen | Reserve-Sätze, gezielte 2-Tage-Review, Fortschrittsanzeige je Teil | Abschn. 4.2 |
| R11 | AT/DE-Kennzeichnung lückenhaft | D10 verfehlt | QA `variety.py`, Lücken aus `03g` vor Phase 5 schließen | Abschn. 6 |

---

## 9. Widersprüche und Abweichungen (benannt)

| # | Thema | Befund | Umgang |
|---|---|---|---|
| K1 | Kapitelzahl | 02 O4: 38 | 39, unverändert |
| K2 | Zeitbudget-Richtwert 55–60 / 20–25 / 15–20 % | 3R (1,5 h): Kapitelarbeit 61 % · Wiederholung (Leitner + Wochenreview) 31 % · Simulationen 6 % (Kapiteltests stecken in der Kapitelarbeit) | Richtwert im Masterprompt 3.1 als Orientierung, nicht als Vorgabe (D7) |
| K3 | Review-Queue max. ~15 min (Masterprompt 4.8) | durch D7 aufgehoben | Masterprompt 4.8 geändert |
| K4 | WOW-Geschichtslücke | unverändert | D9: 14 neue Lernziele übernommen |
| K5 | Goethe-Abdeckung | unverändert | – |
| K6 | Kapiteldauer „2–3 h“ (Masterprompt 3.2) | D8-Modell: 189–268 min | Masterprompt 3.2 auf „≈ 3–4,5 h, verteilt auf 2–4 Tage“ geändert |
| K7 | 30–45 Einheiten | A1-20, A2-19 darunter | unverändert bewusst |
| K8 | D4-Einheiten A1 | 03 nannte 813, Summe je Kapitel 814 | SET-ZAHLEN liegt in A1-02 und A1-15 und zählt je Kapitel einmal; niveauweit 813 – beide Zahlen korrekt |
| K9 | Kalender „Tag X von 90“ (Masterprompt 2, 4.11) | kein Enddatum mehr | Anzeige „Tag X“ + Etappe + Prognose; Masterprompt geändert |
| K10 | Set-Karten 6 s (Phase-3-Simulation) | Reihen-Drill dauert länger | 40 s je Set-Karte; S1/S2 dadurch etwas teurer |
| K11 | Kurzfassung Abschn. 4: DE-Variante „als Hinweis, wo prüfungsrelevant“ | D10: immer kennzeichnen | Kurzfassung und Masterprompt geändert |
| K12 | Planungsskript | 03e (Phase 3) enthält das alte Zeit-/Kalendermodell | neu `03e2`; 03e bleibt für Inventar/Zuordnung gültig, sein Zeitmodell ist überholt |

---

## 10. Definition of Done – Phase 3R

- [x] **Masterprompt und Kurzfassung tragen D7–D11** (Abschn. 2/3/3.1/3.2/3.4/4.8/4.11/5.2 bzw. 1/3/4/5/7/8).
- [x] **Gesamtdauer-Prognose rechnerisch geschlossen** für 1 / 1,5 / 1,75 / 2 h (Abschn. 2.3; Summe der Kategorien = Lernstunden).
- [x] **Leitner-Last ohne Deckel simuliert** – S0–S3 × 4 Tagespensen, S2 empfohlen (Abschn. 2.2).
- [x] **Richtplan mit Puffer und Meilensteinen** (Abschn. 3, `03f`).
- [x] **Bestehenssicherheit** – Kriterien-Mapping (Abschn. 4.1, `03b` Abschn. 8), Austrittskriterien (4.2), Testsätze (4.3), Abschätzung (4.4), Restrisiken (4.5).
- [x] **D10-Kennzeichnungskonzept** (Abschn. 6, `03g`).
- [x] **Abdeckung weiterhin 100 %** – Prüfungen im Skript ohne Fehler (`03b` Abschn. 0).
- [x] **Als Dokumente gespeichert** – 03, 03a, 03b, 03e2, 03f, 03g, 00-masterprompt, 00-kurzfassung, 00-quellen (L18–L20).

---

## 11. Offene Fragen

| # | Frage | Vorschlag |
|---|---|---|
| O1 | Welcher Anker im UI? „90 Tage“ ist bei vollem Umfang nur mit ≈ 2,7 h/Tag erreichbar. | Kein 90-Tage-Countdown; Onboarding zeigt die Prognose zum gewählten Pensum (1,5 h → ≈ 159 Plantage) und Etappen. |
| O2 | Austrittskriterien (Abschn. 4.2) so übernehmen – insbesondere „2 Simulationen in Folge“ und Modelltest? | Ja; Phase 4 bildet sie als Zustand `READY_FOR_EXAM` ab. |
| O3 | D10-Lücken: Haube aktiv als Hauptform (Mütze bleibt aktiv), Nachtmahl passiv ergänzen? | Ja – keine Herabstufung (D3), nur Ergänzung. |
| O4 | Audio-Pflicht (Q2): vorproduziertes Audio für 100 % Wortschatz und Hörtexte, Geräte-TTS nur Fallback – bestätigt damit Prototyp E-P1 Punkt 1. So übernehmen? (Masterprompt 5.2/6.3 ist bereits so formuliert.) | Ja; TTS-Dienst (Lizenz, AT-Stimme) vor Phase 5 recherchieren. |

### 11.1 Entscheidungen zu O1–O4 (D12, bestätigt am 06.11.2026)

| # | Entscheidung |
|---|---|
| O1 | Kein 90-Tage-Countdown; Onboarding und Dashboard zeigen die Prognose zum gewählten Pensum und Etappen. |
| O2 | Austrittskriterien wie Abschn. 4.2 (zwei A2-Simulationen in Folge ≥ 75 % je Teil, zweite am Stück, offizieller Modelltest). |
| O3 | **Pragmatisch:** Die D10-Lücken aus `03g` werden im Content-Batch des betroffenen Kapitels nebenbei behoben; keine eigene Vorarbeit vor Phase 5. L19 nur nachschlagen, wenn im Batch Zweifel auftreten. |
| O4 | ~~Vorproduziertes Audio als Pflicht~~ – **ersetzt durch D13** (gleicher Tag): kein Budget für kostenpflichtiges Audio. Geräte-TTS als Standard, Hörtexte im Prüfungsformat kostenlos selbst erzeugt (z. B. Piper/Thorsten CC0 oder Gratis-Kontingent Cloud-TTS nach Lizenzprüfung), Transkript als Rückfall. |

**Weiter offen:** L1/L2 Punkte je Kriterium · L12 IntG-DV (ab 13.11.2026) · L15 Sprechtempo · **L18–L20 neu** (`00-quellen` G) · offene WOW-Belege · TTS-Dienst für Audio (E-P1) · Tagalog-Review (E2) · Gerätecheck (E4) · DOIs Q90–Q99 vor Phase 4.


## 12. Nächster Schritt

**Phase 4 – Spielregeln:** Zustandsautomat inkl. `READY_FOR_EXAM`, Bestehens-Simulation zu Entscheidung 1 (ersetzt die 15-%-Annahme), Leitner-Regeln S2 ohne Deckel, Genus-Richtung, Randfälle. Vorher: DOIs Q90–Q99 verifizieren.
