# 04b – Testfälle zu allen Spielregeln (Phase 4)

> **Projekt:** „Weg zur A2“ · **Phase:** 4 · **Stand:** 06.11.2026 · Regeln: `04a`
> **Form:** Given / When / Then – direkt als Vitest-Fälle gegen `reducer(state, event)` umsetzbar (Phase 6/7). Zeit kommt immer aus `event.at` (Beispiele: Ortszeit Wien, `tzOffsetMin = +60` im Winter). „Fixture“ = ein gebauter `GameState`.
> **Abdeckung:** jede Regel-ID aus `04a` hat ≥ 1 Testfall (Matrix in Abschn. 14). Alle Fälle laufen gegen `makeReducer(defaultPolicy)`; Abschn. 13a prüft die Policy-Naht (D16). Dazu Invarianten (Abschn. 13), die als Property-based Tests (z. B. `fast-check`) über zufällige Event-Folgen laufen.

---

## 1. Freischaltung (R-F)

| ID | Regel | Given | When | Then |
|---|---|---|---|---|
| T-F01 | R-F1 | Kapitel A1-03 aktuell, A1-04 gesperrt | Lernende öffnet A1-04 | Zugriff verweigert; Phase bleibt `CHAPTER(A1-03)` |
| T-F02 | R-F1 | A1-01 bestanden, A1-02 aktuell | Lektion aus A1-01 öffnen und Übung beantworten | erlaubt; keine Änderung an `completed`, Leben, Bonus |
| T-F03 | R-F2 | Test A1-02 läuft, 1 Fehler, 2 Leben | letzte Aufgabe richtig | Zustand `CORRECTION`, **nicht** `PASSED` |
| T-F04 | R-F2 | Korrekturrunde mit 1 Zwilling | Zwilling richtig | `PASSED(perfectFirst=false)`; Phase `CHAPTER(A1-03)` |
| T-F05 | R-F3 | A1-20 bestanden | – | Phase `MILESTONE_A1`; A2-01 gesperrt |
| T-F06 | R-F3 | MS-A1 ausgewertet, WOW 32/45 (71 %), Rest ≥ 75 % | `EXAM_EVALUATED` | A2-01 bleibt gesperrt; Review-Phase aktiv |
| T-F07 | R-F3 | A2-10 bestanden, SIM-A2-1 alle Teile < 75 % abgegeben | `EXAM_EVALUATED` | Phase `CHAPTER(A2-11)` (Diagnose sperrt nicht); Fehlerkarten in der Queue; Übungspaket als freiwillige Empfehlung |
| T-F08 | R-F3 | A2-10 bestanden, SIM-A2-1 nur Block 1 abgegeben | Lernende öffnet A2-11 | gesperrt bis alle Blöcke abgegeben |

## 2. Kapiteltest (R-T)

| ID | Regel | Given | When | Then |
|---|---|---|---|---|
| T-T01 | R-T1 | Kapitel mit Fokus „Hören“ | `TEST_STARTED` | 20 Items: Hören 5, übrige Disziplinen je 3; + 1 Pflicht-Sprechaufnahme ohne Leben |
| T-T02 | R-T1 | Kapitel A2-19 (Prüfungstraining) | `TEST_STARTED` | Lesen 4, Hören 4, übrige je 3 = 20 |
| T-T03 | R-T2 | Pool mit Item X und dessen Zwilling X' | 1.000 Ziehungen mit Seeds 0–999 | nie X und X' im selben Test |
| T-T04 | R-T2 | gleicher Seed, gleicher Pool | zweimal ziehen | identische Itemliste (Determinismus) |
| T-T05 | R-T2 | Kapitel mit 5 Lernzielen, Disziplin hat Items zu allen | ziehen | Disziplin-Items decken verschiedene Lernziele, bevor eines doppelt kommt |
| T-T06 | R-T3 | Formular-Aufgabe mit 3 Feldern, 1 Feld falsch | `TEST_ANSWERED(correct=false)` | genau −1 Leben, nicht −1 je Feld |
| T-T07 | R-T4 | Versuch 1 nutzte Items S1 (20), Pool 60 | Versuch 2 startet | S2 ∩ S1 = ∅ |
| T-T08 | R-T4 | 3 Versuche haben alle 60 Items genutzt | Versuch 4 startet | Items mit ältestem letzten Einsatz zuerst; Test hat 20 Items |
| T-T09 | R-T5 | Test läuft | `TEST_ANSWERED` falsch | Feedback mit Erklärung und Leben-Anzeige wird erzeugt; Chat bleibt gesperrt (→ T-C02) |
| T-T10 | R-T6 | A2-Hören-Teil-3-Item (1×) | Audio bis Ende gespielt, Lernende tippt erneut auf Play | Play verweigert |
| T-T11 | R-T6 | A2-Hören-Teil-1-Item (2×), 1. Durchlauf nach 40 % vom System unterbrochen | Fortsetzen | Fortsetzung ab Abbruchstelle erlaubt; danach noch 1 voller Durchlauf |
| T-T12 | R-T6 | wie T-T11, zweite Systemunterbrechung im selben Durchlauf | Fortsetzen | keine weitere Fortsetzung; Durchlauf zählt als gespielt |
| T-T13 | R-T7 | freie Nachricht A1-16 ohne Gruß | Abgabe | Item falsch (−1 Leben) |
| T-T14 | R-T7 | freie Nachricht, Keyword für Leitpunkt 2 nicht gefunden, Lernende ordnet Satz 3 Leitpunkt 2 zu | Abgabe | Leitpunkt 2 gilt als bearbeitet; Item richtig, wenn alle anderen Checks passen |
| T-T15 | R-T7 | Text mit Kosinus-Ähnlichkeit 0,72 zur Musterlösung | Abgabe versuchen | Abgabe blockiert, Hinweis „mit eigenen Worten“; kein Leben verloren |
| T-T16 | R-T7 | Pflicht-Sprechaufnahme, Checkliste „verständlich gesprochen“ = nein | Abgabe | kein Leben verloren; Aufgabe erledigt |
| T-T17 | R-T8 | Test offen seit 26 h | nächste Antwort | normal gewertet, keine Zeitüberschreitung |
| T-T18 | R-T9 | Kapitel A1-03 | Test-Item anzeigen | Anweisung de + einblendbare Übersetzung |
| T-T19 | R-T9 | Kapitel A1-05 | Test-Item anzeigen | Anweisung nur de; Übersetzung erst im Feedback |

## 3. Testreife (R-G)

| ID | Regel | Given | When | Then |
|---|---|---|---|---|
| T-G01 | R-G1 | Übungsteil fertig | Gate startet | 20 Items, alle aus Übungs-Pool, keines aus Test-Pool; keine Leben; Chat frei |
| T-G02 | R-G2 | Gate: 18/20 richtig | 20. Antwort | `TEST_READY` |
| T-G03 | R-G2 | Gate: 17/20 richtig | 20. Antwort | `TARGETED_PRACTICE` mit Lernzielen der 3 falschen Items |
| T-G04 | R-G2 | Zielübung fertig | `TARGETED_PRACTICE_DONE` | neuer Gate-Block; ∩ mit vorigem Block = ∅ (solange Pool reicht) |
| T-G05 | R-G3 | Karte K in Fach 1, Gate-Item zu K richtig | Antwort | K bleibt Fach 1 |
| T-G06 | R-G3 | Gate-Item zu K falsch | Antwort | Fehlerkarte für das Item in Fach 1, fällig morgen |

## 4. Leben und Bonus (R-L)

| ID | Regel | Given | When | Then |
|---|---|---|---|---|
| T-L01 | R-L1 | `startLives = 3`, Test läuft, 2 Fehler | 3. Fehler | Leben 0, Versuch endet sofort → `ERROR_REVIEW`; restliche Items nicht gezeigt |
| T-L02 | R-L1 | `startLives = 5` | 4 Fehler, Rest richtig | `CORRECTION` mit 4 Zwillingen |
| T-L03 | R-L1 | Bonus 2 aus Vorkapitel, eigener Bonus-Rechner würde 6 ergeben | Kapitelstart | `startLives = 5` (Deckel) |
| T-L04 | R-L2 | Korrekturrunde läuft | Zwilling falsch | keine Leben-Änderung angezeigt/verrechnet; Versuch gescheitert |
| T-L05 | R-L3 | Kapitel n im 1. Versuch fehlerfrei, eigener Bonus 0 | `PASSED` | Kapitel n+1 `startLives = 4`; Perfekt-Serie +1 |
| T-L06 | R-L3 | Kapitel n+1 (Bonus 1) im 1. Versuch fehlerfrei | `PASSED` | Kapitel n+2 `startLives = 5` |
| T-L07 | R-L3 | Kapitel n+2 (Bonus 2) im 1. Versuch fehlerfrei | `PASSED` | Kapitel n+3 `startLives = 5` (nicht 6) |
| T-L08 | R-L3 | Kapitel mit Bonus 1, über Korrekturrunde bestanden | `PASSED` | nächstes Kapitel `startLives = 3` |
| T-L09 | R-L3 | Kapitel mit Bonus 1, Versuch 1 gescheitert | neuer Versuch | `startLives = 4` (Bonus gilt für alle Versuche) |
| T-L10 | R-L3, I-2 | Versuch 1 gescheitert, Versuch 2 fehlerfrei | `PASSED` | **kein** Bonus für nächstes Kapitel; Perfekt-Serie = 0 |

## 5. Korrekturrunde und Wiederholung (R-K)

| ID | Regel | Given | When | Then |
|---|---|---|---|---|
| T-K01 | R-K1 | 2 falsche Items A, B; Zwillinge A', A'', B' | Korrekturrunde startet | 2 Aufgaben: je ein Zwilling von A und B, keiner davon im Test vorgekommen |
| T-K02 | R-K1 | Test endet mit 1 Fehler | – | Korrekturrunde startet **direkt** (kein Zwischenzustand, in dem Chat frei ist) |
| T-K03 | R-K2 | Korrekturrunde mit 3 Zwillingen | 1. Zwilling falsch | Runde endet sofort; `ERROR_REVIEW`; Zwillinge 2–3 nicht gezeigt |
| T-K04 | R-K2 | Korrekturrunde mit 3 Zwillingen | alle richtig | `PASSED` |
| T-K05 | R-K3 | Item A hat nur Zwilling A', A' war im selben Test | Korrekturrunde | A' wird trotzdem gezeigt (ältester), Warnung im QA-Log |
| T-K06 | R-K4 | Versuch gescheitert mit 3 Fehlerkarten | 2 davon richtig beantwortet | bleibt `ERROR_REVIEW`; falsche Karte kommt in derselben Runde wieder |
| T-K07 | R-K4 | alle 3 Fehlerkarten je 1× richtig | – | `LESSONS(repeatMode=true)`, `attemptNo = 2`, Leben = `startLives` |
| T-K08 | R-K5 | Wiederholungsmodus | Lektion öffnen | Erklärseiten mit „überspringen“; Abrufaufgaben nicht überspringbar |
| T-K09 | R-K6 | 2. Versuch gescheitert | `ERROR_REVIEW` erreicht | Hinweis mit Top-Fehler-Lernzielen + Chat/ÖIF-Kursraum-Empfehlung; kein Überspringen angeboten |

## 6. Prüfungssimulation (R-M)

| ID | Regel | Given | When | Then |
|---|---|---|---|---|
| T-M01 | R-M1 | MS-A1, Block „schriftlich“ | Blockstart | Reihenfolge SB → Hören → HuA → Lesen → Schreiben, 70 min, keine Pause im Block |
| T-M02 | R-M1 | A2-Simulation | Blockreihenfolge | Lesen → Hören → Schreiben → Pause ≥ 15 min → WOW → Sprechen |
| T-M03 | R-M2 | Block Lesen (40 min) gestartet 10:00, App 10:15 geschlossen | `APP_OPENED` 10:50 | Block mit gespeicherten Antworten abgegeben (`EXAM_BLOCK_TIMEOUT`) |
| T-M04 | R-M2 | Hören A2 läuft | Lernende tippt Pause | nicht möglich |
| T-M05 | R-M2 | Hören vom System unterbrochen | Fortsetzen | einmal ab Abbruchstelle, Vermerk „unterbrochen“ im Ergebnis |
| T-M06 | R-M3 | A2: Lesen 15/20, Hören 22/30, rest ≥ 75 % | `EXAM_EVALUATED` | nicht bestanden (Hören 73 %) |
| T-M07 | R-M3 | A2: Lesen 15/20 (75 %), Hören 23/30, Schreiben 15/20, Sprechen 23/30, WOW 34/45 | `EXAM_EVALUATED` | bestanden (Grenzwerte zählen) |
| T-M08 | R-M3 | WOW a/b/c-Frage halb richtig markiert | Auswertung | 0 Punkte (keine Teilpunkte) |
| T-M09 | R-M3 | KI-Feedback sagt „Schreiben schwach“, Raster ergibt 16/20 | Auswertung | Schreiben bestanden (KI ist kein Kriterium) |
| T-M10 | R-M4 | Simulation am Plantag 80 nicht bestanden | Neuversuch Plantag 81 | gesperrt (≥ 2 Plantage) |
| T-M11 | R-M4 | Plantag 82, Review-Paket nicht fertig | Neuversuch | gesperrt |
| T-M12 | R-M4 | Plantag 82, Paket fertig | Neuversuch | erlaubt, neuer Testsatz |
| T-M13 | R-M5 | A1-Sätze 1–3 benutzt, Satz 1 vor 20 Tagen | 4. Versuch | Satz 1 mit Hinweis „bekannter Satz“ |
| T-M14 | R-M5 | wie T-M13, Satz 1 vor 10 Tagen, alle anderen jünger | 4. Versuch | gesperrt bis Tag 14 nach Erstnutzung des ältesten Satzes; Meldung an Produktion |
| T-M15 | R-M6 | MS-A1 bestanden | Urkunde anfordern | Datei mit Name, Datum, % je Subtest und Hinweis „kein offizielles Zertifikat“; kein `print()` |
| T-M16 | R-M7 | Plantag 72: 25 Karten fällig, 0 beantwortet | `EXAM_BLOCK_STARTED` | 25 Karten `due = Plantag 73`, Fach unverändert; Tagesziel für Tag 72 = nur 20 min |
| T-M17 | R-M7 | Block 2 derselben Simulation am Folgetag | Blockstart | keine erneute Verschiebung der Karten des Folgetags (nur erster Block verschiebt) |

## 7. Austritt (R-X)

| ID | Regel | Given | When | Then |
|---|---|---|---|---|
| T-X01 | R-X2 | `chain = 0` | SIM-Modus-Versuch alle Teile ≥ 75 % | `chain = 1`; nächster Versuch nur im GP-Modus startbar |
| T-X02 | R-X2 | `chain = 1` | GP ≥ 75 %, Pausen 20 und 15 min | Phase `MODEL_TEST` |
| T-X03 | R-X2 | `chain = 1` | GP Lesen 70 % | `chain = 0`; Review-Phase |
| T-X04 | R-X2 | SIM-A2-1 alle ≥ 75 % | – | `chain` bleibt 0 (Diagnose zählt nie) |
| T-X05 | R-X3 | `chain = 1`, GP alle ≥ 75 %, Pause 75 min | `EXAM_EVALUATED` | Ergebnis gespeichert, `chain = 0`, Hinweis „nicht am Stück“ |
| T-X06 | R-X4 | Modelltest: L 15/20, H 24/30, WOW 35/45, Checklisten S 80 %, Sp 75 % | Eintrag | `modelTestPassed = true` |
| T-X07 | R-X4 | Modelltest: WOW 33/45 | Eintrag | nicht bestanden; Review; erneuter Modelltest danach |
| T-X08 | R-X1 | alles erfüllt, aber 1 Karte 8 Tage überfällig | – | nicht `READY_FOR_EXAM`; Hinweis „Wiederholung nachholen“ |
| T-X09 | R-X1 | wie T-X08 | Karte beantwortet | `READY_FOR_EXAM` (automatisch, ohne weiteres Event) |
| T-X10 | R-X1 | alles erfüllt, 0 Einheiten Sprechpraxis protokolliert | – | `READY_FOR_EXAM`, mit Empfehlung Sprechpraxis (nicht sperrend) |
| T-X11 | R-X1 | Fehlerkarte aus der GP nie beantwortet | – | nicht bereit |
| T-X12 | R-X5 | `READY_FOR_EXAM` seit Tag 160; Tag 175 Karte 9 Tage überfällig | – | Status bleibt; Banner „Vor der Anmeldung: Wiederholung nachholen“ |

## 8. Chat und Prüfungsmodus (R-C)

| ID | Regel | Given | When | Then |
|---|---|---|---|---|
| T-C01 | R-C1 | Zustand `LESSONS`/`PRACTICE`/`GATE`/`TARGETED_PRACTICE` | `chatLocked` | false |
| T-C02 | R-C1 | Zustand `TEST` direkt nach Feedback zu Item 5 | `chatLocked` | true |
| T-C03 | R-C1 | Zustand `CORRECTION` | `chatLocked` | true |
| T-C04 | R-C1 | Korrekturrunde bestanden | `chatLocked` | false |
| T-C05 | R-C1 | Simulationsblock läuft (SIM- oder GP-Modus) | `chatLocked` | true |
| T-C05b | R-C1 | GP-Modus, Pause zwischen Schreiben und WOW | `chatLocked` | true (Pause gehört zur Prüfung); nach `EXAM_EVALUATED` false |
| T-C05c | R-C1 | SIM-Modus, Block 1 gestern abgegeben, Block 2 noch nicht gestartet | `chatLocked` | false |
| T-C06 | R-C2 | gesperrt | Render Chat-Button und Kopier-Button | sichtbar, `disabled`, Text „Nach dem Test kannst du fragen“ |
| T-C07 | R-C3 | beliebiger Zustand S | `CHAT_OPENED`, `COPY_PROMPT_USED` | Zustand gleich S bis auf Protokollfeld (Leben, Karten, Phase unverändert) |
| T-C08 | R-C4 | Simulation | Item rendern | keine `en`/`tl`-Texte im DOM vor `EXAM_EVALUATED` |

> Zu T-C05b/c: Im GP-Modus gehört die Pause zur Prüfung (Chat gesperrt); im SIM-Modus mit Blöcken an zwei Tagen ist der Chat zwischen den Blöcken frei, weil dazwischen Wiederholung stattfindet (`04a` R-C1).

## 9. Streaks und Tage (R-E, R-S, R-D)

| ID | Regel | Given | When | Then |
|---|---|---|---|---|
| T-E01 | R-E1 | Antwort-Serie 12 | Leitner-Karte richtig | 13 |
| T-E02 | R-E1 | Serie 13, Rekord 20 | Antwort falsch | Serie 0, Rekord 20 |
| T-E03 | R-E1 | Karte gerade falsch, kommt in derselben Runde wieder | richtig | Serie unverändert (zählt nicht) |
| T-E04 | R-E1 | Simulation läuft | Antworten | Serie unverändert |
| T-E05 | R-E2 | Perfekt-Serie 3 | Kapitel über Korrekturrunde bestanden | 0 |
| T-S01 | R-S1 | Tag D: 5 Karten fällig, 0 aktiv | 20 min aktiv, 4 Karten beantwortet | Ziel nicht erfüllt |
| T-S02 | R-S1 | wie T-S01 | 5. Karte beantwortet | Ziel erfüllt, Streak +1 sofort |
| T-S03 | R-S1 | Tag D: 0 Karten fällig | 19 min aktiv | nicht erfüllt; bei 20 min erfüllt |
| T-S04 | R-S1 | Ziel um 18:00 erfüllt | 21:00 Leitner-Karte falsch (neu fällig morgen) | Tag bleibt erfüllt |
| T-S05 | R-S2/S3 | Streak 10, 1 Freeze, letzter erfüllter Tag Mo | `APP_OPENED` Mi | Di geschützt, Freeze 0, Streak 10 |
| T-S06 | R-S3, I-4 | Streak 10, 2 Freezes, letzter erfüllter Tag Mo | `APP_OPENED` Fr (Di, Mi, Do verpasst) | Streak 0, Freezes 2 |
| T-S07 | R-S3 | Streak 10, 2 Freezes | 2 Tage verpasst | Streak 10, Freezes 0 |
| T-S08 | R-S4 | Streak 6, Freezes 2 | Tag erfüllt (Streak 7) | Freezes 2 (Deckel) |
| T-S09 | R-S4 | Streak 13, Freezes 0 | Tag erfüllt (14) | Freezes 1 |
| T-S10 | R-S4 | Streak 6, 1 Tag per Freeze geschützt | nächster erfüllter Tag | Streak 7 (geschützter Tag zählt nicht), Freeze +1 |
| T-S11 | R-S5 | Streak erreicht 30 | – | Badge 30 dauerhaft, auch nach Bruch |
| T-S12 | R-S6 | Tage mit erfüllt/geschützt/aktiv ohne Ziel/leer | Heatmap berechnen | 4 Kategorien korrekt; Intensität nach Minuten |
| T-S13 | R-S7 | Streak bricht | Dashboard | kein Verlust-Alarm; Rekord + Neustart + Freezes angezeigt |
| T-D01 | R-D1 | `at = 2026-11-06T22:30Z`, Offset +60 | lokales Datum | 2026-11-06 (23:30) |
| T-D02 | R-D1 | `at = 2026-11-06T23:30Z`, Offset +60 | lokales Datum | 2026-11-07 (00:30) |
| T-D03 | R-D2 | Session-Start 23:50, Queue Tag D noch 6 Karten | 00:05 letzte Karte beantwortet, Session ohne 90-s-Pause | Karten zählen zu D; D erfüllt (wenn ≥ 20 min) |
| T-D04 | R-D2 | wie T-D03, Session läuft bis 03:10 | Antwort 03:05 | zählt noch zu D; Antwort 03:10+ (nach 3 h) zählt zu D+1 |
| T-D05 | R-D2 | Session-Start 23:50, 2 min Pause um 00:01 | Aktivität 00:03 | gehört zu D+1 (Anker beendet) |
| T-D06 | R-D3 | App sichtbar, letzte Interaktion vor 100 s, kein Audio | Tick | 0 s gezählt |
| T-D07 | R-D3 | Hörtext läuft, keine Interaktion seit 3 min | Tick | 15 s gezählt |
| T-D08 | R-D4 | `startDate` 2026-11-06 | heute 2026-11-06 / 2026-12-06 | Plantag 1 / 31 |
| T-D09 | R-D5 | Flug Wien → Manila (+60 → +480), letztes Event Mo 20:00 Wien, nächstes Mi 08:00 Manila (Di lokal übersprungen, 29 h vergangen) | `APP_OPENED` | Di zählt nicht als verpasst |
| T-D10 | R-D6 | `lastEventAt` 10:00, neues Event 09:00 (Uhr zurückgestellt) | `APP_OPENED` | `skewNotice = true`; `lastLocalDate` unverändert; keine Streak-Bewertung rückwärts |
| T-D11 | Idempotenz | `TEST_ANSWERED(a1, item7)` verarbeitet | dasselbe Event erneut | Zustand unverändert (kein zweites Leben weg) |

## 10. Wiederholung (R-W)

| ID | Regel | Given | When | Then |
|---|---|---|---|---|
| T-W01 | R-W1 | Lektion führt 10 aktive, 3 passive Wörter, 1 Set ein | `LESSON_COMPLETED` | 11 Karten (10 vocab + 1 set), keine für passive |
| T-W02 | R-W2 | Lektion an Tag D abgeschlossen | – | neue Karten Fach 1, `due = D+1` |
| T-W03 | R-W3 | Übungsitem I falsch, Fehlerkarte zu I existiert in Fach 4 | Antwort | Fehlerkarte zu I zurück auf Fach 1, `due = morgen` |
| T-W04 | R-W3 | Fehlerkarte zu I mit Zwillingen I', I'' | 2 Abrufe | 1. Abruf zeigt I', 2. Abruf I'' |
| T-W05 | R-W3 | Leitner-Karte falsch | Antwort | keine zusätzliche Fehlerkarte |
| T-W06 | R-W4 | Vokabel V in Fach 1, im Kapiteltest an Tag D richtig | Test bestanden | V Fach 2, `due = D+3` |
| T-W07 | R-W4 | Vokabel V in Fach 3, im Test richtig | – | Fach 3 unverändert |
| T-W08 | R-W5 | Karte Fach 2, Tag D | richtig | Fach 3, `due = D+7` |
| T-W09 | R-W5 | Karte Fach 5 | richtig | `mastered = true`, nicht mehr in der Tages-Queue |
| T-W10 | R-W5 | Karte Fach 4 | falsch | Fach 1, `due = D+1`, in derselben Runde erneut gezeigt (ohne Fachwirkung) |
| T-W11 | R-W5 | `due = D−3` | Queue am Tag D | Karte enthalten (überfällig) |
| T-W12 | R-W6 | Queue: 3 Fehlerkarten, 10 vocab, 4 grammar | Reihenfolge | erst 3 Fehlerkarten; danach Wechsel vocab/grammar/… nach Fälligkeit |
| T-W13 | R-W7 | Nomenkarte, letzter Abruf Richtung *Genus* falsch | nächster Abruf | Richtung *Genus* |
| T-W14 | R-W7 | Nomenkarte in Fach 5 | Abruf | Richtung immer *Produzieren* mit Artikel |
| T-W15 | R-W7 | Produktion „Tisch“ ohne Artikel | Antwort | falsch (`strictToken` Artikel) |
| T-W16 | R-W7 | Genus-Abfrage „E-Mail“: Antwort „die“ (`genusAt = das`, `genusDe = die`) | Antwort | richtig mit Hinweis „In Österreich: das E-Mail“ |
| T-W17 | R-W7 | Genus-Richtung | Item rendern | kein Audio vor der Antwort |
| T-W18 | R-W8 | Queue 12 Karten offen | Lektion starten | gesperrt; Hinweis „erst Wiederholung“ |
| T-W19 | R-W8 | Queue 60 Karten (≈ 14 min) | Anzeige | Etappen à 10 min mit Fortschrittsbalken; kein Abschneiden |
| T-W20 | R-W9 | Plantag 7, Wochenreview nicht gemacht | Plantag 8 | Wochenreview weiterhin fällig, vor neuem Stoff |
| T-W21 | R-W9 | Wochenreview-Block (ausgelegt auf ≈ 30 min) nach 25 min vollständig beantwortet | – | erledigt (Block vollständig); alternativ erledigt nach 30 aktiven Minuten, auch wenn Items übrig sind |
| T-W22 | R-W9 | Wochenreview-Item falsch | Antwort | Fehlerkarte |
| T-W23 | R-W11 | 14 Tage Pause, 180 Karten überfällig | `APP_OPENED` | alle 180 in der Queue (kein Deckel), Zeitschätzung angezeigt |

## 11. Daten (R-D7–R-D11) und Prognose (R-P)

| ID | Regel | Given | When | Then |
|---|---|---|---|---|
| T-D12 | R-D7 | 50 Events, Snapshot nach Event 30 | Neustart | Zustand = Replay aller 50 Events auf leeren Zustand |
| T-D13 | R-D8 | letzter Export vor 8 Tagen | `APP_OPENED` | Export-Erinnerung |
| T-D14 | R-D9 | Prototyp-Export `{"app":"weg-zur-a2-prototyp","schema":1,…}` | Import | Leitner-Karten über stabile IDs übernommen; Profil übernommen |
| T-D15 | R-D9 | Import mit Streak 12, letztes erfülltes Datum vor 3 Tagen, 0 Freezes | `IMPORT_APPLIED` + `APP_OPENED` | Streak 0 nach R-S3 |
| T-D16 | R-D10 | Test offen | `CONTENT_PACK_LOADED` | abgelehnt mit Hinweis |
| T-D17 | R-D10 | Karte zu entfernter ID | Pack geladen | Karte `archived`, nicht fällig, nicht gelöscht |
| T-D18 | R-D11 | Tab A schreibt, Tab B geöffnet | Antwort in Tab B | blockiert, Hinweis „anderes Fenster“ |
| T-P01 | R-P3 | 3 Kapitel mit tatsächlich 1,3 × Planminuten | Prognose | k = 1,3; Spanne ±15 % |
| T-P02 | R-P3 | k aus Daten 2,6 | Prognose | k = 2,0 (Deckel) |
| T-P03 | R-P3 | beliebig | Prognose-Text | enthält nie „Rückstand“/„hinter dem Plan“ |
| T-P04 | R-P4 | Lernziel L: letzte 5 Antworten r, f, r, f, r | Schwächenanalyse | L ist schwach |
| T-P05 | R-P2 | Disziplin Hören: letzte 100 Erstantworten 84 richtig | Anzeige | 84 % |

## 12. Randfälle (RF, `04a` Abschn. 6)

| ID | Fall | Given | When | Then |
|---|---|---|---|---|
| T-RF01 | RF-01 | Test Item 8/20, Leben 2 | App geschlossen, nach 2 Tagen geöffnet | Test bei Item 9, Leben 2, gleiche Itemliste, Chat gesperrt |
| T-RF02 | RF-01, I-8 | Test offen | Suche nach „Neu starten“/„Aufgeben“ | nicht vorhanden |
| T-RF03 | RF-02 | Korrekturrunde Zwilling 1/3 richtig | Neustart | Fortsetzung bei Zwilling 2 |
| T-RF04 | RF-06 | Leitner-Runde 23:58–00:12 ohne Pause | 00:12 Runde fertig | Queue von Tag D+1 erst jetzt berechnet; keine Karte von D+1 in die laufende Runde eingefügt |
| T-RF05 | RF-07 | Test über Mitternacht | Antworten nach 00:00 | Leben/Items unverändert; aktive Zeit nach R-D2 |
| T-RF06 | RF-13 | Speicher-Schreibfehler (`QuotaExceededError`) | Event | Hinweis + Export-Angebot; Event bleibt im Arbeitsspeicher, keine stille Löschung |
| T-RF07 | RF-14 | Snapshot mit offenem Test auf Gerät B importiert | `APP_OPENED` | Test fortsetzbar wie T-RF01 |
| T-RF08 | RF-16 | Pool 60, 4. Versuch | – | T-T08 |
| T-RF09 | RF-25 | kein Audio-Upload möglich | Pflicht-Sprechaufnahme | „laut gesprochen + Checkliste“ akzeptiert, gekennzeichnet |
| T-RF10 | RF-21 | Wochenreview fällig, Simulation freigeschaltet | Simulation starten | erst nach Wochenreview |

## 13. Invarianten (Property-based)

| ID | Invariante |
|---|---|
| P-01 | 0 ≤ `lives` ≤ `startLives` ≤ 5 in jedem erreichbaren Zustand. |
| P-02 | *(defaultPolicy)* Die Kapitel in `completed` bilden immer ein Präfix der Kursreihenfolge, alle mit `reason: 'passed'`. |
| P-03 | `chatLocked` ist true in jedem Zustand `TEST`, `CORRECTION` und in jedem laufenden Simulationsblock – für jede Event-Folge. |
| P-04 | Kein Event außer `TEST_ANSWERED`/`CORRECTION_ANSWERED`/`EXAM_*` (und unter einer anderen Policy `OVERRIDE_GRANTED`) ändert Leben, Phase oder `completed`. |
| P-05 | Der Reducer ist deterministisch: gleiche Event-Folge → gleicher Zustand (inkl. Itemziehung über Seed). |
| P-06 | `lastLocalDate` ist monoton nicht fallend. |
| P-07 | Jede Karte hat `box ∈ {1..5}`; `mastered ⇒ box = 5`. |
| P-08 | `streak.freezes ∈ {0, 1, 2}`; Streak steigt pro lokalem Datum höchstens um 1. |
| P-09 | *(defaultPolicy)* Kein Weg von `CHAPTER(c)` zu `CHAPTER(next(c))` ohne `PASSED` in `c` (kein Überspringen, D11). |
| P-10 | `READY_FOR_EXAM` nur, wenn `isExamReady` zum Zeitpunkt des Übergangs true ist. |
| P-11 | Import(Export(S)) = S (Roundtrip). |


## 13a. Policy-Schicht (R-PL, D16)

Alle Testfälle der Abschnitte 1–12 laufen gegen `makeReducer(defaultPolicy)`. Die folgenden Fälle prüfen die **Naht** zur Policy mit Stub-Policies; sie sichern ab, dass spätere Sonderwege möglich bleiben, ohne deren Logik festzulegen.

| ID | Regel | Given | When | Then |
|---|---|---|---|---|
| T-PL01 | R-PL2 | `defaultPolicy`, Kapitel A1-05 aktuell | `OVERRIDE_GRANTED{kind:'CHAPTER_SKIP', target:'A1-05'}` | `overrides` +1 mit `accepted:false`; Phase, `completed`, Leben, Karten unverändert |
| T-PL02 | R-PL3 | Stub-Policy akzeptiert Skip mit Effekt `COMPLETE_CHAPTER(A1-05, skipped)` | gleiches Event | `completed['A1-05'].reason = 'skipped'`; Phase `CHAPTER(A1-06)`; offene Testversuche von A1-05 geschlossen |
| T-PL03 | R-PL3 | Stub-Policy liefert `recoveryAfterFail = {errorReview:true, entry:'TEST_READY', resetLives:true, newSelection:true, repeatMode:false}` | Versuch scheitert, Fehler-Review fertig | Zustand `TEST_READY` statt `LESSONS`; neue Itemauswahl; Leben = `startLives` |
| T-PL04 | R-PL3 | Stub-Policy akzeptiert `EXTRA_RETRY` mit `GRANT_ATTEMPT` | Event während `ERROR_REVIEW` | Plan des Grants ersetzt den Default-Plan; Grant in `overrides` protokolliert |
| T-PL05 | R-PL4 | Import mit `overrides[0].grant.kind = 'TELEPORT'` und Stand mit `entry: 'SOMEWHERE'` | `IMPORT_APPLIED` | Schemafehler mit Feldpfad; Zustand unverändert |
| T-PL06 | R-PL5 | Import mit `ruleset = {id:'default', version: 99}` | Import | schreibgeschützt geöffnet, Hinweis; keine Events möglich |
| T-PL07 | R-PL1 | Stub-Policy mit `config.TEST_ITEMS = 25`, `startLives = 4` | `TEST_STARTED` | 25 Items, 4 Leben – ohne Änderung am Kern |
| T-PL08 | R-PL6 | beliebige Stub-Policy | Test läuft | `chatLocked = true`; Hörregeln und Leitner-Intervalle unverändert |
| T-PL09 | Export | Stand mit 2 Overrides (1 abgelehnt, 1 akzeptiert) | Export → Import | `overrides`, `completed[].reason`, `ruleset` identisch (Roundtrip, P-11) |

## 14. Abdeckungsmatrix Regel → Testfälle

| Regel | Testfälle |
|---|---|
| R-F1–R-F3 | T-F01–T-F08 |
| R-T1–R-T9 | T-T01–T-T19, T-C02 |
| R-G1–R-G3 | T-G01–T-G06 |
| R-L1–R-L3 | T-L01–T-L10 |
| R-K1–R-K6 | T-K01–T-K09 |
| R-M1–R-M7 | T-M01–T-M17 |
| R-X1–R-X5 | T-X01–T-X12 |
| R-C1–R-C4 | T-C01–T-C08 |
| R-E1–R-E2 | T-E01–T-E05 |
| R-S1–R-S7 | T-S01–T-S13 |
| R-D1–R-D11 | T-D01–T-D18 |
| R-W1–R-W11 | T-W01–T-W23 |
| R-PL1–R-PL6 | T-PL01–T-PL09 |
| R-P1–R-P4 | T-P01–T-P05 (R-P1 per Playwright-Snapshot in Phase 7) |
| RF-01–RF-25 | T-RF01–T-RF10 + Verweise in den Gruppen oben (RF-03 → T-T11/12, RF-04 → T-M03, RF-05 → T-D12, RF-08 → T-M16/17, RF-09 → T-D09, RF-10 → T-D10, RF-11 → T-D11, RF-12 → T-D18, RF-15 → T-D16, RF-17 → T-T14, RF-18 → T-P01, RF-19 → T-W23/T-S06, RF-20 → T-M16, RF-22 → T-M13/14, RF-23 → T-C07, RF-24 → T-RF07) |

**Summe:** 174 Testfälle + 11 Invarianten.
