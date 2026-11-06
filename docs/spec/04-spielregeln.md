# 04 – Spielregeln (Phase 4): Bestehens-Simulation, Zustandsautomat, testbare Regeln

> **Projekt:** „Weg zur A2“ · **Phase:** 4 · **Stand:** 06.11.2026
> **Grundlage:** `00-kurzfassung.md` (Entscheidungen 1–7, E1–E4, D1–D13) · `03-curriculum.md` Rev. 3R (2.2, 3, 4) · `03a` (Meilensteine) · `00-quellen.md` A–C · `02g` · `prototyp-erkenntnisse.md` E-P2
> **Teil-Dokumente:** `04a` Zustandsautomat + Policy-Schicht + normative Regeln + Randfälle · `04b` 174 Testfälle + 11 Invarianten · `04c` Simulationsskript (reproduzierbar)
> **Status:** ✅ abgeschlossen. **Bestätigt am 06.11.2026:** V1–V5 und I-1–I-8 (**D14**), Prognose-Zentralfall jetzt übernehmen (**D15**), Regeln lose gekoppelt für spätere Spezial-Retries und Kapitel-Skip (**D16**, Abschn. 3.1).

---

## 0. Vorprüfungen

### 0.1 Lernforschung Q90–Q99 (Trigger `00-quellen` F, Lücke L14)

Alle zehn Quellen bibliografisch geprüft am 06.11.2026; Details und Korrekturen im Register `00-quellen` Abschn. H.1.

| ID | Quelle (geprüft) | DOI | Ergebnis |
|---|---|---|---|
| Q90 | Roediger & Karpicke (2006), *Psychological Science* 17(3), 249–255 | 10.1111/j.1467-9280.2006.01693.x | ✅ |
| Q91 | Cepeda, Pashler, Vul, Wixted & Rohrer (2006), *Psychological Bulletin* 132(3), 354–380 | 10.1037/0033-2909.132.3.354 | ✅ |
| Q92 | Dunlosky et al. (2013), *Psychological Science in the Public Interest* 14(1), 4–58 | 10.1177/1529100612453266 | ✅ |
| Q93 | Rohrer & Taylor (2007), *Instructional Science* 35, 481–498 | 10.1007/s11251-007-9015-8 | ✅ |
| Q94 | Kang (2016), *Policy Insights from the Behavioral and Brain Sciences* 3(1), 12–19 (Untertitel: *Policy Implications for Instruction*) | 10.1177/2372732215624708 | ✅ |
| Q95 | Settles & Meeder (2016), ACL 2016, 1848–1858 | 10.18653/v1/P16-1174 | ✅ |
| Q96 | Sailer & Homner (2020), *Educational Psychology Review* 32(1), 77–112 | 10.1007/s10648-019-09498-w | ✅ |
| Q97 | Sweller (1988), *Cognitive Science* 12(2), 257–285 | 10.1207/s15516709cog1202_4 | ✅ |
| Q98 | Nation (2006), *Canadian Modern Language Review* 63(1), 59–82 | 10.3138/cmlr.63.1.59 | ✅ – **Inhalt passt nicht zur Projektregel** (K7) |
| Q99 | **bestimmt:** Silverman & Barasch (2023), *Journal of Consumer Research* 49(6), 1095–1117 | 10.1093/jcr/ucac029 | ✅ (war `[UNVERIFIZIERT]`) |
| **Q108** (neu) | Kulik, Kulik & Bangert-Drowns (1990), *Review of Educational Research* 60(2), 265–299 | JSTOR 1170612 | ✅ – Beleg für die Testreife (V2) |

**Was die Prüfung inhaltlich für Phase 4 bringt:**
- Q99: In sieben Studien steigerten **intakte** protokollierte Serien die weitere Beteiligung gegenüber hervorgehobenen **gebrochenen** Serien; der Effekt wird schwächer, wenn sich eine Serie „reparieren“ lässt ([Silverman & Barasch 2023, UDSpace](https://udspace.udel.edu/items/42ce576b-8e1f-429a-8541-e29e48dbcfbb/full)). → stützt den Streak-Freeze (Entscheidung 3) und begründet R-S7 (kein Verlust-Alarm).
- Q96: Gamification wirkt klein bis mittel positiv auf kognitive (g = 0,49), motivationale (0,36) und Verhaltens-Ergebnisse (0,25) ([Sailer & Homner, OPUS Augsburg](https://opus.bibliothek.uni-augsburg.de/opus4/frontdoor/index/index/docId/109056); [BVB-Katalog](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_journals_2273607100)) – passt zu D8: Gamification nur unterstützend.
- Q108: Mastery-Programme erzielen im Mittel 0,52 SD bessere Prüfungsleistung; **höhere** Mastery-Standards wirken stärker, die **Abschlussquote** ist aber in Mastery-Kursen eher niedriger ([Kulik et al. 1990, SciSpace-PDF](https://scispace.com/pdf/effectiveness-of-mastery-learning-programs-a-meta-analysis-45bgwh1byb.pdf)). → genau das Spannungsfeld von Variante A: Strenge bringt Leistung, kostet aber Durchhalten. Darum V1 + V2.
- Q98: Nation rechnet mit **98 %** bekannter Wörter für ungestütztes Verstehen ([Nation 2006, Victoria University](https://www.wgtn.ac.nz/__data/assets/pdf_file/0018/1626120/2006-How-large-a-vocab.pdf)); die Projektregel „≤ 5 % unbekannte Wörter“ (= 95 %) stützt sich also nicht auf Q98 (K7, neue Lücke L21).

### 0.2 IntG-Novelle

Heute ist der 06.11.2026, die Begutachtung endet am 12.11.2026 → **kein Re-Check in diesem Chat**. Trigger „ab 13.11.2026“ in `00-quellen` F bleibt offen. Alle Regeln hier beziehen sich auf das aktuelle Papierformat (E1).

---

## 1. Ergebnis auf einen Blick

**Kernbefund:** Bei Variante A (jeder Fehler in der Korrekturrunde → Kapitel komplett wiederholen) entscheidet vor allem die **Trefferquote beim Testantritt**, erst danach die Testlänge. Erwartete Fehler = Items × Fehlerquote: Bei 25 Items und 90 % sind das 2,5 Fehler – dann besteht man nur 47 % der Versuche. Die in `03` angenommene Wiederholungsquote von 15 % gilt nur, wenn Lernende mit ≈ 95 % in den Test gehen.

### 1.1 Vorschläge V1–V5 (bestätigt, D14)

| # | Vorschlag | Warum | Wirkung (Simulation, Zentralfall 92 %) |
|---|---|---|---|
| **V1** | **Kapiteltest = 20 bewertete Aufgaben** (3 je Disziplin + 2 Fokus; Prüfungstraining L4/H4) + 1 Pflicht-Sprechaufnahme ohne Leben | untere Grenze des Masterprompts (20–30); jedes Item mehr ist ein weiteres Risiko ohne viel mehr Diagnose (Wortschatz wird über Leitner, Wochenreview und Simulationen geprüft) | 20 statt 25 Items: je nach Trefferquote 8–34 h weniger Wiederholungsaufwand (0,95 → 0,88) |
| **V2** | **Testreife-Runde** am Ende des Übungsteils: 20 Übungsitems, Test erst ab **18/20**; sonst Zielübung + neuer Block (ohne Leben, Chat frei) | Mastery-Prinzip (Q108): erst testen, wenn das Können sichtbar ist. Verwandelt teure, frustrierende Kapitelwiederholungen in billige Zusatzübung; die Übung selbst ist Abruf (Q90/Q92) | praktisch gleiche Gesamtzeit (−0,9 h), aber Kapitel mit ≥ 3 Versuchen 2,8 → 1,7; Kapitel mit Wiederholung 10,6 → 9,1 |
| **V3** | **Planungs-Zentralfall Trefferquote 0,92** statt „15 %“: Richtplan rechnet je Kapitel 46–58 min erwartete Wiederholung | ehrliche Prognose (D7, R1); Pilot (Phase 7) kalibriert | 1,5 h/Tag: **172 Plantage** statt 159 (Spanne 159–185), ≈ 260 statt 240 Lernstunden |
| **V4** | **Genus ohne eigene Spur:** Nomenkarte rotiert *Erkennen / Produzieren mit Artikel / der-die-das*; Fach 5 bei Nomen immer *Produzieren mit Artikel* | „gemeistert“ heißt Bedeutung **und** Genus (E-P2), ohne die +5,6 h von S3 | 0 zusätzliche Karten |
| **V5** | Kapiteltest A1-01–A1-04: Anweisung mit einblendbarer Übersetzung; ab A1-05 nur Deutsch | absolute Anfänger:innen können am Tag 1 keine deutschen Anweisungen lesen; A1-05 führt alle Prüfungsanweisungen ein (`03a`) | – |

### 1.2 Auslegungen des Masterprompt-Wortlauts (bestätigt, D14)

| # | Stelle | Auslegung |
|---|---|---|
| I-1 | „Jeder Fehler = −1 Leben“ | eine falsche **Aufgabe** = 1 Leben (mehrteilige Aufgabe falsch, wenn ein Teil falsch); Pflicht-Sprechaufnahme kostet nie ein Leben (`02g` 3.5) |
| I-2 | Bonusleben „bei perfektem Kapitel“, „Leben zurückgesetzt“ | perfekt = **erster** Versuch fehlerfrei; Bonus gilt für **alle** Versuche des nächsten Kapitels; Serie perfekter Kapitel stapelt bis 5 Leben, sonst verfällt der Bonus |
| I-3 | Chat „frei nach jedem Feedback“ | Feedback **innerhalb** von Test und Korrekturrunde öffnet den Chat nicht; beide sind eine gesperrte Einheit |
| I-4 | Freeze „verbraucht automatisch“ | Freezes werden nur verbraucht, wenn sie die **ganze** Lücke schließen; sonst Streak 0 und Freezes bleiben |
| I-5 | „korrekte Mitternachtslogik“ | Tag endet 00:00 Ortszeit; eine laufende Session zählt bis zu 3 h zum Starttag (Session-Anker) |
| I-6 | Wiederholung „an Simulationstagen auf Folgetag verschoben“ | Verschiebung beim Start des **ersten** Simulationsblocks; Tagesziel an dem Tag = 20 min |
| I-7 | Wochenreview „jeder 7. Plantag“ | fällig ab Plantag 7, 14 …, **bleibt fällig bis erledigt**, vor neuem Stoff |
| I-8 | Abbruch mitten im Test | Test wird fortgesetzt, nie neu gestartet; kein „Aufgeben“ |

### 1.3 Prognose neu (Zentralfall V3, übernommen als Planwert – D15)

| Tagespensum | Plantage `03` (15 %) | **Plantage neu (0,92)** | P90 | Spanne 0,95 – 0,90 | Lernstunden neu | A1-Meilenstein |
|---|---|---|---|---|---|---|
| 1 h | 234 | **254** | 269 | 233 – 273 | 261 | Tag 121 |
| 1,5 h | 159 | **172** | 181 | 159 – 185 | 260 | Tag 80 |
| 1,75 h | 138 | **150** | 158 | 137 – 160 | 261 | Tag 68 |
| 2 h | 123 | **132** | 139 | 123 – 142 | 261 | Tag 59 |

≈ 260 Lernstunden = 52 % des ÖIF-Richtwerts 500 h (Q107). Die Spanne zeigt: Jeder Prozentpunkt Trefferquote beim Testantritt ist im Gesamtplan mehrere Tage wert – darum V2.

---

## 2. Bestehens-Simulation zu Entscheidung 1

### 2.1 Modell

- Lernende beantwortet jede Testaufgabe unabhängig mit Wahrscheinlichkeit p richtig; Zwillinge ebenso (Sensitivität ±).
- Ein Versuch: 3 Leben (+ Bonus); bei 0 Leben sofort gescheitert; mit ≥ 1 Leben und Fehlern Korrekturrunde mit je einem Zwilling; ein falscher Zwilling → gescheitert.
- Wiederholung: p steigt um 3 Prozentpunkte je kompletter Wiederholung (Spacing); Kosten 60 % von Input + Üben + neuer Test + 10 min Fehler-Review.
- Kursverlauf: alle 39 Kapitel, Kapitel-Trefferquote streut ± 4 pp um den Mittelwert, Bonusleben nach I-2, 4.000 Läufe, Seed fest. Code und Annahmen: `04c`.

### 2.2 Bestehen je Versuch (exakt, 3 Leben, ohne Testreife)

**Bestehensquote eines Versuchs in %:**

| Items \ p | 0,85 | 0,88 | 0,90 | 0,92 | 0,95 | 0,97 |
|---|---|---|---|---|---|---|
| 18 | 38,3 | 53,7 | 65,0 | 76,2 | 90,7 | 97,0 |
| **20** | **32,1** | **47,6** | **59,6** | **72,0** | **88,7** | **96,3** |
| 22 | 26,6 | 41,8 | 54,3 | 67,7 | 86,6 | 95,6 |
| 25 | 19,8 | 34,1 | 46,7 | 61,2 | 83,2 | 94,3 |
| 28 | 14,5 | 27,3 | 39,7 | 54,8 | 79,6 | 92,9 |
| 30 | 11,7 | 23,5 | 35,4 | 50,7 | 77,0 | 91,9 |

**Erwartete Versuche je Kapitel / Anteil mit ≥ 3 Versuchen:**

| Items \ p | 0,85 | 0,88 | 0,90 | 0,92 | 0,95 | 0,97 |
|---|---|---|---|---|---|---|
| **20** | 2,18 / 35,6 % | 1,73 / 17,9 % | 1,50 / 8,9 % | 1,31 / 3,2 % | 1,11 / 0,2 % | 1,04 / 0,0 % |
| 25 | 2,64 / 52,9 % | 2,04 / 30,5 % | 1,72 / 16,7 % | 1,45 / 6,5 % | 1,17 / 0,4 % | 1,06 / 0,0 % |
| 30 | 3,08 / 67,6 % | 2,36 / 43,9 % | 1,95 / 26,3 % | 1,61 / 11,3 % | 1,24 / 0,7 % | 1,08 / 0,1 % |

**Woran scheitert man?** Bei 20 Items und p = 0,90: fehlerfrei 12,2 % · über Korrekturrunde bestanden 47,4 % · an 0 Leben gescheitert 32,3 % · an einem Zwilling gescheitert 8,1 %. Der Hauptgrund ist also der dritte Fehler im Test, nicht die Korrekturrunde.

### 2.3 Sensitivität

| Bestehen je Versuch in % (20 / 25 Items) | p = 0,90 | p = 0,92 | p = 0,95 |
|---|---|---|---|
| Basis (3 Leben, Zwilling = p) | 59,6 / 46,7 | 72,0 / 61,2 | 88,7 / 83,2 |
| Zwilling 5 pp schwerer | 55,7 / 43,3 | 67,9 / 57,3 | 85,1 / 79,3 |
| Zwilling 3 pp leichter | 61,9 / 48,7 | 74,5 / 63,6 | 90,9 / 85,6 |
| 4 Leben (1 Bonus) | 73,4 / 63,2 | 83,0 / 75,8 | 93,8 / 91,2 |
| 5 Leben (2 Bonus) | 79,3 / 72,3 | 86,8 / 82,3 | 94,9 / 93,4 |

Bonusleben wirken stark – sie belohnen also genau das, was die Strenge von Variante A abfedert (Entscheidung 2 passt gut dazu).

### 2.4 Testreife-Runde (V2)

**Wie gut filtert 18/20?** Wahrscheinlichkeit, die Runde im ersten Block zu bestehen:

| wahre Trefferquote | ≥ 17/20 | **≥ 18/20** | ≥ 19/20 |
|---|---|---|---|
| 0,85 | 64,8 % | **40,5 %** | 17,6 % |
| 0,88 | 78,7 % | **56,3 %** | 28,9 % |
| 0,90 | 86,7 % | **67,7 %** | 39,2 % |
| 0,92 | 92,9 % | **78,8 %** | 51,7 % |
| 0,95 | 98,4 % | **92,5 %** | 73,6 % |

18/20 hält nicht testreife Lernende (85 %) überwiegend zurück und lässt gut vorbereitete (≥ 92 %) meist sofort durch. 19/20 wäre schärfer, kostet aber gut vorbereitete Lernende jede zweite Runde.

**Kursverlauf (39 Kapitel, Mittel aus 4.000 Läufen):**

| p am Kapitelende | Konfiguration | Kapitel mit Wiederholung | Kapitel ≥ 3 Versuche | Wiederholungen gesamt | Testreife-Zusatzrunden | perfekte Kapitel | Zusatzzeit gesamt | Δ zum Plan `03` |
|---|---|---|---|---|---|---|---|---|
| 0,88 | 25 Items | 23,7 | 12,4 | 43,8 | – | 2,9 | 107,4 h | +94,2 h |
| 0,88 | 20 Items | 19,1 | 8,1 | 31,0 | – | 4,4 | 73,8 h | +57,3 h |
| 0,88 | **20 + Testreife 18** | 16,1 | 4,8 | 22,0 | 35,6 | 5,5 | 67,4 h | +51,0 h |
| 0,90 | 25 Items | 19,1 | 8,2 | 31,2 | – | 4,8 | 76,7 h | +63,5 h |
| 0,90 | 20 Items | 14,8 | 5,0 | 21,6 | – | 6,8 | 51,7 h | +35,3 h |
| 0,90 | **20 + Testreife 18** | 12,6 | 3,0 | 16,2 | 23,8 | 7,7 | 48,9 h | +32,5 h |
| 0,90 | 20 + Testreife 19 | 9,6 | 1,5 | 11,2 | 51,8 | 9,9 | 48,9 h | +32,5 h |
| 0,92 | 25 Items | 14,2 | 4,8 | 20,6 | – | 7,6 | 51,1 h | +38,0 h |
| 0,92 | 20 Items | 10,6 | 2,8 | 14,0 | – | 9,9 | 33,9 h | +17,5 h |
| **0,92** | **20 + Testreife 18** | **9,1** | **1,7** | **11,0** | **15,1** | **10,8** | **33,0 h** | **+16,6 h** |
| 0,92 | 20 + Testreife 19 | 7,1 | 0,9 | 8,0 | 35,5 | 12,7 | 34,5 h | +18,1 h |
| 0,95 | 25 Items | 7,5 | 1,6 | 9,4 | – | 13,7 | 23,8 h | +10,6 h |
| 0,95 | 20 Items | 5,3 | 0,8 | 6,2 | – | 16,3 | 15,4 h | −1,0 h |
| 0,95 | **20 + Testreife 18** | 4,7 | 0,6 | 5,3 | 6,6 | 16,9 | 15,9 h | −0,5 h |

„Zusatzzeit“ = Wiederholungen + Korrekturrunden + Fehler-Reviews + Testreife-Zusatzrunden. „Δ zum Plan“ = Zusatzzeit − 790 min (15-%-Annahme in `03`) + Änderung der Testdauer (20 Items: −5 min je Kapitel).

### 2.5 Empfehlung und Begründung

**Kriterien** (aus Entscheidung 1 abgeleitet, damit „fordernd, aber nicht frustrierend“ prüfbar wird):
1. *Fordernd:* Wer nicht testreif ist (p ≈ 0,85), besteht einen Versuch selten (≤ 35 %).
2. *Nicht frustrierend:* Wer testreif ist (p ≥ 0,92), besteht ≥ 70 % der Versuche, und über den ganzen Kurs braucht man höchstens ≈ 2 Kapitel einen dritten Versuch.
3. *Zeit ehrlich:* Der Mehraufwand steht im Richtplan, nicht als Überraschung.

**20 Items + Testreife 18/20** erfüllt alle drei: p = 0,85 → 32 % je Versuch und die Testreife hält die meisten gar nicht erst zum Test durch · p = 0,92 → 72 % je Versuch (mit Bonusleben mehr), 1,7 Kapitel mit ≥ 3 Versuchen · Zeit im Zentralfall +16,6 h, im Richtplan verbucht (V3).

**Warum nicht 18 Items?** Außerhalb des Masterprompt-Rahmens (20–30) und ohne Fokus-Disziplin; Gewinn nur ≈ 4 pp je Versuch. **Warum nicht 25?** Bei gleicher Lernleistung +8 bis +34 h Wiederholung und fast doppelt so viele Kapitel mit ≥ 3 Versuchen. **Warum Testreife 18 statt 19?** Praktisch gleiche Gesamtzeit, aber 19/20 schickt auch gut vorbereitete Lernende jede zweite Runde in eine Zusatzübung – das fühlt sich wie Gängelung an.

**Ehrliche Konsequenz von Variante A:** Auch gut vorbereitet (92 %) muss im Mittel etwa **jedes vierte Kapitel** wiederholt werden (9 von 39). Das ist der Preis der Strenge; Entscheidung 1 ist final, die Simulation macht ihn nur sichtbar. Die App kommuniziert das vorab („Kapitel wiederholen gehört dazu – es festigt“) und zeigt Fortschritt, nicht Scheitern (R-K6, R-S7).

**Didaktische Begründung:**
- *Retrieval Practice* (Q90, Q92): Test, Testreife und Korrekturrunde sind Abruf – Lernen, nicht nur Messen.
- *Mastery Learning* (Q108): höhere Standards wirken stärker; das Risiko geringerer Abschlussquoten wird durch die Testreife abgefangen, weil das Nicht-Bestehen dort billig und ohne Lebensverlust ist.
- *Spacing* (Q91, Q94): Neuer Versuch erst nach Fehler-Review und erneutem Lernteil, Meilenstein-Neuversuch erst ≥ 2 Plantage später.
- *Cognitive Load* (Q97): 20 statt 25–30 Aufgaben am Stück senken Ermüdungsfehler am Testende, die nichts über das Können aussagen.

### 2.6 Auswirkung auf den Richtplan (ersetzt die 15-%-Annahme in `03` 2.1)

| Baustein | `03` Rev. 3R | **Phase 4 (Zentralfall)** |
|---|---|---|
| Kapiteltest | 25 Items × 1 min + 5 = 30 min | 20 × 1 + 5 = **25 min** |
| Erwartete Wiederholung je Kapitel | 17–24 min (Summe 790 min) | **46–58 min** (Summe 2.002 min, 33,4 h); P90 Kurs 2.699 min |
| Kapitelarbeit gesamt | 146,6 h | **163,5 h** |
| Puffer | 5 Puffertage + Erwartungswert in Kapitelzeit | **unverändert** + Erwartungswert neu; die **P90-Spanne** erscheint in der Prognose (1,5 h: +9 Plantage) statt als feste Puffertage |

**Warum kein zusätzlicher fester Puffer?** Seit D7 gibt es kein Enddatum, gegen das ein Puffer schützen müsste. Der Erwartungswert steckt in den Kapitelminuten, die Streuung zeigt die Prognose als Spanne, und der persönliche Faktor k (R-P3) passt die Prognose nach drei Kapiteln an die echte Lernende an.

**Freigabeplan (`03` Abschn. 7)** bleibt gültig: Er rechnet mit dem schnellsten Tempo; längere Kapitel verschaffen der Produktion nur mehr Vorlauf.

---

## 3. Masterprompt Phase 4 → Regeln (Überblick)

| Masterprompt 4.x | umgesetzt in (`04a`) |
|---|---|
| 1 Freischaltung linear, bestanden = alles richtig | R-F1–R-F3, Kursautomat 4.1 |
| 2 Kapiteltest, alle Disziplinen, Pool | R-T1–R-T9 (V1, V5), R-G1–R-G3 (V2) |
| 3 Leben | R-L1, R-L2 |
| 4 Korrekturrunde, Variante A | R-K1–R-K6, Kapitelautomat 4.2 |
| 5 Bonusleben | R-L3 (I-2) |
| 6 Erfolgsstreak | R-E1, R-E2 |
| 7 Tagesstreak, Mitternacht, Heatmap, Badges, Freeze | R-S1–R-S7, R-D1–R-D6 (I-4, I-5) |
| 8 Wiederholung (Leitner, S2, ohne Deckel, Wochenreview, Genus) | R-W1–R-W11 (V4, I-6, I-7) |
| 9 Meilensteine, Urkunde, Austritt als eigener Zustand | R-M1–R-M7, R-X1–R-X5, Automaten 4.3/4.4 (`READY_FOR_EXAM`) |
| 10 Frage-Chat und Prüfungsmodus | R-C1–R-C4 (I-3) |
| 11 Fortschritt und Diagnose | R-P1–R-P4 |
| DoD Randfälle | `04a` Abschn. 6 (RF-01–RF-25) |

### 3.1 Lose Kopplung der Regeln (D16)

Auftrag: Die Regeln so schneiden, dass spätere **Spezial-Retries** und **Kapitel-Skips** eingebaut werden können, ohne uns auszusperren; deren Logik wird erst entworfen, wenn es so weit ist.

Umsetzung (`04a` Abschn. 1a): Der Reducer enthält nur Mechanik und wird aus einer **`RulePolicy`** gebaut (`makeReducer(policy)`). Alle Regelentscheidungen – Kapitelzugang, Teststart und -ausgang, Leben, Bonus, Wiederholungsplan nach Scheitern, Meilenstein-Bestehen, `isExamReady` – sind Funktionen der Policy; die heutigen Regeln sind die `defaultPolicy`. Vorkehrungen im Datenmodell: Kapitel-Erledigung mit Grund (`passed` / `skipped` / `waived`), Wiederholungsplan als Daten (`RecoveryPlan`), ein generisches Event `OVERRIDE_GRANTED` mit Protokoll in `overrides`, `ruleset`-Version im Spielstand und im Export. Die `defaultPolicy` lehnt jede Override ab – das heutige Verhalten bleibt exakt wie spezifiziert. 9 Naht-Tests (`04b` 13a) sichern das ab.

**Benannter Zielkonflikt:** Ein Kapitel-Skip widerspricht heute D11. Die Policy-Schicht macht ihn technisch möglich, nicht erlaubt; ein Skip braucht später eine eigene Entscheidung.

### 3.2 Die drei Randfälle aus der DoD in Kurzform

- **Abbruch mitten im Test (RF-01–RF-04):** Der Versuch bleibt offen und läuft beim nächsten Öffnen an der nächsten Aufgabe weiter – gleiche Aufgaben, gleiche Leben, Chat gesperrt. Kein Neustart, kein „Aufgeben“ (I-8), sonst ließe sich eine schlechte Ziehung wegklicken. Hören: nur vollständige Durchläufe zählen. Simulationen: Timer läuft weiter wie in der echten Prüfung.
- **App-Neustart (RF-05):** Snapshot + Event-Log, Reducer spielt ab; Ergebnis ist bitgleich (Invariante P-05). Streak-Bewertung läuft beim Öffnen.
- **Datumswechsel während einer Session (RF-06–RF-08):** Session-Anker – was vor Mitternacht begonnen wurde, zählt bis Session-Ende (max. 3 h) zum alten Tag; die neue Queue erscheint erst danach. Tests laufen unverändert weiter, Simulationsblöcke nach Timer.

---

## 4. Didaktik und Motivation – weitere Begründungen

- **Interleaving** (Q93): Queue im Wechsel der Kartenarten (R-W6), Wochenreview aus allen Kapiteln (R-W9), Testreife gemischt über Disziplinen (R-G1).
- **Genus** (E-P2, V4): Genus ist Grundlage von Akkusativ, Dativ und Adjektivendungen (`02d`). Die Rotation sorgt für aktiven Abruf, Fach 5 verlangt Produktion mit Artikel. Farbcodierung der Artikel wird ohne Beleg **nicht** als Standard eingesetzt (offen, E-P2 Punkt 3).
- **Streaks** (Q99): Belohnen, was zählt (20 min + Queue), Reparatur über Freeze, Bruch nicht dramatisieren (R-S7).
- **Gamification** (Q96): kleine Effekte, nur in Verbindung mit gutem Inhalt – darum hängen Leben, Bonus und Streak an echten Lernhandlungen (D8, Q9 „keine Belohnung ohne Lernhandlung“).
- **Ehrliche Rückmeldung:** Prognose als Spanne, nie „Rückstand“ (R-P3); Selbstbewertungen sind als solche gekennzeichnet (R-M3).

---

## 5. Widersprüche und Abweichungen (benannt)

| # | Thema | Befund | Umgang |
|---|---|---|---|
| K1 | Wiederholungsquote 15 % (`03` 2.1, R3) | gilt nur bei ≈ 95 % Trefferquote am Testantritt | ersetzt durch Simulation (V3); Prognose 1,5 h 159 → 172 Plantage |
| K2 | Testplan 25 Items je Kapitel (`03a`, `03e2` `test_plan()`) | 20 Items (V1) | `03a`-Verteilung je Kapitel in Phase 5 nach R-T1 neu erzeugen; Pool ≥ 60 bleibt |
| K3 | `02g`: Kapiteltest-Feedback sofort vs. Entscheidung 7 „frei nach jedem Feedback“ | würde den Chat mitten im Test öffnen | I-3: Test + Korrekturrunde sind eine gesperrte Einheit |
| K4 | Masterprompt „Prüfungsmodus nur Deutsch“ | in A1-01–A1-04 für absolute Anfänger:innen nicht lesbar | V5 (Kapiteltest); Simulationen bleiben nur Deutsch |
| K5 | „Leben zurückgesetzt“ (Masterprompt 4.3) | unklar, ob mit Bonus | I-2: zurück auf 3 + Bonus des Kapitels |
| K6 | E-P2 Vorschlag „getrennte Spuren je Richtung“ | S3 kostet +5,6 h | V4 Rotation ohne Mehrkosten |
| K7 | `02g` 2.1 / `03` Q9 „≤ 5 % unbekannte Wörter (Q98)“ | Q98 nennt 98 % Abdeckung für ungestütztes Verstehen; 95 % stammt aus anderer Literatur | Regel bleibt als **Obergrenze**; Beleg offen → L21; strengere Grenze für Lesetexte in Phase 5 prüfen |
| K8 | Masterprompt/Q6 „jedes Item ≥ 1 Zwilling“ | Wiederholungsversuche brauchen neue Zwillinge | Test-Pool-Items ≥ 2 Zwillinge (R-K3), Übungs-Pool bleibt ≥ 1 |
| K9 | `03` Leitner-Modell: 6 Fehlerkarten je Kapitel | R-W3 (jede falsche Aufgabe inkl. Testreife) ergibt bei 90 % ≈ 8 | ≈ +3 h Wiederholung über den Kurs `[SCHÄTZUNG]`, innerhalb der Prognose-Spanne; Nachrechnen mit `model3r` in Phase 5 |
| K10 | Quellenangaben Q91/Q93/Q94 in `01` unvollständig (Mitautoren, Seiten, Untertitel) | `01` ist abgeschlossen | Korrekturen nur im Lockfile `00-quellen` H.1 |

---

## 6. Risiken (neu und aktualisiert)

| # | Risiko | Wirkung | Gegenmaßnahme |
|---|---|---|---|
| R3 (akt.) | Trefferquote am Testantritt < 0,92 | bei 0,90: 185 statt 172 Plantage (1,5 h) | Testreife (V2), Pilot misst Testreife- und Testergebnisse, k in der Prognose |
| R12 | Strenge → Abbruch (Q108: geringere Abschlussquoten in Mastery-Kursen) | Lernende hört auf | Testreife ohne Lebensverlust, kurze Tests, Bonusleben, kein Bruch-Alarm, Fortschritt sichtbar; Pilot-Kennzahl „Abbruch nach gescheitertem Kapitel“ |
| R13 | Selbstbewertung Schreiben/Sprechen zu großzügig | Meilenstein-Ergebnis überschätzt | konkrete Checklisten, Musterantwort-Vergleich, KI als zweite Meinung, externer Modelltest, ÖIF-Kursraum (Austrittskriterium 6) |
| R14 | Keyword-Leitpunkt-Check irrt | ungerechter Lebensverlust | Zuordnung durch die Lernende (R-T7), formale Checks bleiben hart |
| R15 | Testreife „durchklicken“ bis zum Glückstreffer | Test zu früh | jeder neue Block mit neuen Items + Zielübung dazwischen; Glück bei p = 0,85 nur 40 % je Block; Pilot prüft Gate-Wert gegen Testergebnis |

---

## 7. Definition of Done – Phase 4

- [x] **DOIs Q90–Q99 verifiziert**, Q99 bestimmt, Q108 ergänzt (Abschn. 0.1, `00-quellen` H.1); IntG-Novelle: Re-Check erst ab 13.11.2026 (Abschn. 0.2).
- [x] **Bestehens-Simulation zu Entscheidung 1 mit empfohlener Testlänge** – exakt je Versuch und als Kursverlauf, Sensitivitäten, Empfehlung 20 Items + Testreife 18/20, Prognose neu gerechnet (Abschn. 2, `04c`); ersetzt die 15-%-Annahme.
- [x] **Zustandsautomat vollständig inkl. Austrittskriterien** – Kurs, Kapitelversuch, Simulation, Austrittskette mit `READY_FOR_EXAM`, Sperren; Zustandsmodell, Events, Übergangstabellen, Konstanten (`04a`).
- [x] **Jede Regel als Testfall** – 174 Testfälle + 11 Invarianten, Abdeckungsmatrix Regel → Test (`04b`).
- [x] **Lose Kopplung (D16)** – Policy-Schicht mit Erweiterungspunkten für Spezial-Retries und Kapitel-Skip, Naht-Tests (`04a` 1a, `04b` 13a).
- [x] **Randfälle geklärt** – Abbruch im Test, App-Neustart, Datumswechsel während Session und 22 weitere (`04a` 6, `04b` 12).
- [x] **Als Dokumente gespeichert** – `04`, `04a`, `04b`, `04c`; `00-quellen` und `00-kurzfassung` nachgetragen.

---

## 8. Weiter offen (aus früheren Phasen, unverändert)

L1/L2 Punkte je Kriterium A2 Schreiben/Sprechen · L12 IntG-DV (ab 13.11.2026) · L15 Sprechtempo · L18–L20 · offene WOW-Belege (vor Phase 5) · Audio-Spike + Gerätecheck (D13, E4) · Tagalog-Review (E2) · **neu L21** (Beleg 95-%-Abdeckung) · Beleg Genus-Farbcodierung (E-P2).

## 9. Entscheidungen zu den offenen Fragen (06.11.2026)

| # | Frage | Entscheidung |
|---|---|---|
| O1 | V1–V5 übernehmen? | **Ja → D14** |
| O2 | I-1–I-8 übernehmen? | **Ja → D14** |
| O3 | Prognose jetzt in Kurzfassung und Masterprompt? | **Ja, jetzt als Zentralfall mit Spanne → D15**; Pilot kalibriert |
| – | Zusatz: Regeln lose koppeln für spätere Spezial-Retries und Kapitel-Skip | **D16**, umgesetzt in `04a` 1a, Logik der Features später |

## 10. Nächster Schritt

Kurzfassung und Masterprompt sind nachgezogen (Rev. 4: Abschn. 2, 3b, Phase 4, 5.2, 5.11, 6.2, 6.8). Nächste Phase: **Phase 5 – Content** in Claude Code. Vorher fällig: Re-Check IntG-Novelle (ab 13.11.2026), offene WOW-Belege, Audio-Spike + Gerätecheck (D13).
