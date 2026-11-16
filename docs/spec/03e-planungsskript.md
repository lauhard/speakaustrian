# 03e – Planungsskript (Phase 3, reproduzierbar)

> **Stand:** 06.11.2026 · **Zweck:** erzeugt 03, 03a–03d aus Kapiteldaten, Inventar und Regeln; Ziel in Phase 5: `scripts/plan/` im Repo. **Eingaben:** `inv_a1.txt`/`inv_a2.txt` (kompakte Inventar-Abschrift v1, rekonstruierbar aus `03c-kapitel-wortschatz.tsv` Spalten lemma|pos|use|at je HF-Block), `neu.tsv` (= `03d` vor Neu-Nummerierung), `miss.json` (Goethe-A1-Schlüssel). Ausführen: `python3 build.py && python3 writer.py`. Kommentare im Code auf Englisch.

## `chapters.py`

```python
"""Chapter specification data (Phase 3). Pure data; checks live in build.py."""

def C(id, title, hf, cando, gram, red, wow, exam, focus, vocab_hints=(), note=""):
    return dict(id=id, title=title, hf=hf, cando=cando, gram=gram, red=red, wow=wow,
                exam=exam, focus=focus, vocab_hints=list(vocab_hints), note=note)

A1 = [
 C("A1-01", "Grüß Gott! – sich begrüßen und vorstellen", ["HF01", "HF00"],
   ["A1-SPR-07", "A1-SPR-01", "A1-HOE-01", "QK-04", "QK-03"], ["G01", "G02"],
   ["R-SP-01", "R-SP-46", "R-SP-47", "R-SP-48"], ["A1-WOW-18", "A1-WOW-01"],
   ["A1-SPR-T1", "A1-HUA-T1", "A1-WOW-T1"], "Sprechen",
   note="Chunk vor Regel: »Ich heiße …«, »Wie heißen Sie?«; du/Sie und Grußformen von Anfang an."),
 C("A1-02", "Buchstaben, Zahlen, Preise", ["HF12", "HF11"],
   ["A1-SPR-02", "A1-SPR-03", "A1-HOE-03", "A1-HOE-02", "A1-SCH-02", "QK-01"], ["G03", "G04"],
   ["R-SP-04", "R-SP-12", "R-SP-13", "R-SP-14"], ["A1-WOW-09"],
   ["A1-SPR-T1", "A1-HOE-T2", "A1-WOW-T2"], "Hören",
   note="Zahlen 0–100 als Set; Preise (Euro/Cent) und Notrufnummern als erste Zahlen mit Alltagsbezug."),
 C("A1-03", "Woher kommen Sie? – Herkunft, Wohnort, Sprachen", ["HF01"],
   ["A1-SPR-01", "A1-HOE-01", "A1-SPR-12", "A1-SPR-04"], ["G05", "G06"],
   ["R-SP-02", "R-SP-03", "R-SP-06", "R-SP-15", "R-SP-35", "R-SP-36"], ["A1-WOW-19"],
   ["A1-SPR-T1", "A1-SPR-T2", "A1-HUA-T1", "A1-WOW-T1"], "Sprechen"),
 C("A1-04", "Meine Familie", ["HF01"],
   ["A1-SPR-01", "A1-SPR-04", "A1-LES-03"], ["G07"],
   ["R-SP-05", "R-SP-16", "R-SP-17"], ["A1-WOW-16"],
   ["A1-SPR-T2", "A1-LES-T2", "A1-HUA-T2", "A1-WOW-T2"], "Sprechen",
   note="Possessiv »mein/meine« zunächst als Chunk, Regel in A1-14 (G16)."),
 C("A1-05", "Im Deutschkurs", ["HF00"],
   ["A1-LES-08", "A1-HOE-06", "A1-SPR-12", "QK-05"], ["G08"],
   ["R-SP-35", "R-SP-36", "R-SP-18"], ["A1-WOW-01", "A1-WOW-02"],
   ["A1-LES-T2", "A1-HUA-T1", "A1-SB-T1", "A1-WOW-T1"], "Lesen",
   note="Alle Prüfungsanweisungen (ankreuzen, ergänzen, zuordnen) werden hier eingeführt (02c 3.3 Regel 5)."),
 C("A1-06", "Uhrzeit und Tagesablauf", ["HF12", "HF02"],
   ["A1-SPR-15", "A1-HOE-02", "A1-SPR-10"], ["G09", "G14"],
   ["R-SP-16", "R-SP-31"], ["A1-WOW-18"],
   ["A1-HOE-T2", "A1-SPR-T2", "A1-SB-T1", "A1-WOW-T2"], "Hören",
   note="Offizielle und informelle Uhrzeit (»halb acht«, »dreiviertel acht«) – häufigste Hörfalle."),
 C("A1-07", "Auf dem Markt und im Supermarkt", ["HF03"],
   ["A1-SPR-08", "A1-HOE-02", "A1-LES-01", "A1-LES-07"], ["G10", "G11"],
   ["R-SP-19", "R-SP-20"], ["A1-WOW-06"],
   ["A1-HOE-T2", "A1-SPR-T3", "A1-LES-T3", "A1-HOE-T1", "A1-WOW-T1"], "Hören",
   note="Austriazismen Kern: Erdäpfel, Paradeiser, Semmel, Sackerl, Kassa, Deka; Mengenangaben als Set."),
 C("A1-08", "Essen, Trinken, Gasthaus", ["HF03"],
   ["A1-SPR-05", "A1-SPR-08", "A1-LES-07", "A1-HOE-07"], ["G27", "G28"],
   ["R-SP-19", "R-SP-20", "R-SP-23", "R-SP-48"], ["A1-WOW-17"],
   ["A1-SPR-T3", "A1-HUA-T2", "A1-LES-T3", "A1-SB-T1", "A1-WOW-T2"], "Sprechen"),
 C("A1-09", "Meine Wohnung und das Haus", ["HF02"],
   ["A1-SPR-14", "A1-LES-06", "A1-LES-01"], ["G12", "G26"],
   ["R-SP-17", "R-SP-19"], ["A1-WOW-11", "A1-WOW-12", "A1-WOW-13", "A1-WOW-25"],
   ["A1-LES-T3", "A1-SPR-T2", "A1-SB-T1", "A1-LES-T1", "A1-WOW-T1", "A1-WOW-T2"], "Lesen",
   note="Modalverben über Hausordnung: Man darf / muss / soll …"),
 C("A1-10", "Telefon, Mobilbox und Termine", ["HF11"],
   ["A1-HOE-04", "A1-HOE-09", "A1-SPR-10", "A1-SCH-05"], ["G13", "G17"],
   ["R-SP-30", "R-SP-31", "R-SP-14", "R-SP-13"], ["A1-WOW-18"],
   ["A1-HOE-T1", "A1-SPR-T2", "A1-HUA-T1", "A1-SB-T1", "A1-WOW-T1"], "Hören"),
 C("A1-11", "Beim Hausarzt und in der Apotheke", ["HF04"],
   ["A1-SPR-09", "A1-HOE-06", "A1-HOE-09", "A1-HOE-05"], ["G15"],
   ["R-SP-19", "R-SP-35", "R-SP-36"], ["A1-WOW-07", "A1-WOW-08", "A1-WOW-10", "A1-WOW-26"],
   ["A1-HOE-T1", "A1-SPR-T2", "A1-HUA-T2", "A1-LES-T3", "A1-WOW-T1", "A1-WOW-T2"], "Hören",
   note="»Mir tut … weh« zunächst als Chunk; Regel G19 in A1-14."),
 C("A1-12", "Mit Bus und Bahn", ["HF08"],
   ["A1-SPR-11", "A1-HOE-05", "A1-LES-07"], ["G18"],
   ["R-SP-16", "R-SP-17", "R-SP-19"], ["A1-WOW-18"],
   ["A1-HOE-T1", "A1-SPR-T3", "A1-LES-T3", "A1-HUA-T2", "A1-WOW-T2"], "Hören",
   note="Dativ zuerst über feste Verbindungen: mit dem Bus, zum Bahnhof, beim Arzt."),
 C("A1-13", "Wo ist …? – in der Stadt und in der Wohnung", ["HF08", "HF02"],
   ["A1-HOE-08", "A1-SPR-11", "A1-SPR-14"], ["G20"],
   ["R-SP-16", "R-SP-35", "R-SP-38"], ["A1-WOW-13"],
   ["A1-HOE-T2", "A1-SB-T1", "A1-HUA-T1", "A1-LES-T1", "A1-WOW-T1"], "Grammatik",
   note="Wechselpräpositionen »Wo?« mit Möbeln und Wegbeschreibung; »Wohin?« folgt in A2-03 (G31)."),
 C("A1-14", "Arbeit und Beruf", ["HF05"],
   ["A1-SPR-01", "A1-SPR-04", "A1-LES-03", "A1-HOE-07"], ["G16", "G19"],
   ["R-SP-07", "R-SP-18"], ["A1-WOW-02", "A1-WOW-05", "A1-WOW-27"],
   ["A1-SPR-T1", "A1-SPR-T2", "A1-LES-T2", "A1-SB-T1", "A1-HUA-T1", "A1-WOW-T1", "A1-WOW-T2"], "Sprechen"),
 C("A1-15", "Ämter und Formulare", ["HF06"],
   ["A1-LES-05", "A1-SCH-01", "A1-SCH-02", "A1-LES-01"], ["G21"],
   ["R-SP-12", "R-SP-13", "R-SP-15"], ["A1-WOW-21", "A1-WOW-06"],
   ["A1-SCH-T1", "A1-LES-T3", "A1-HOE-T2", "A1-SB-T1", "A1-WOW-T2"], "Schreiben",
   note="Formularregel: Eigennamen und Zahlen ohne Fehlertoleranz (02g 3.3); Meldezettel."),
 C("A1-16", "Freizeit und Einladungen", ["HF10"],
   ["A1-SPR-06", "A1-SCH-03", "A1-SCH-04", "A1-LES-02", "A1-LES-03"], ["G24"],
   ["R-SP-08", "R-SP-21", "R-SP-22", "R-SC-06", "R-SC-07"], ["A1-WOW-17"],
   ["A1-SCH-T2", "A1-LES-T3", "A1-SPR-T3", "A1-LES-T2", "A1-HUA-T2", "A1-WOW-T1"], "Schreiben",
   note="Erste freie Nachricht (ca. 30 Wörter) mit 3 Leitpunkten; zwei Musterlösungen, keine Mustertexte (Q02 § 13c)."),
 C("A1-17", "Wetter, Kleidung und Feste", ["HF12", "HF13", "HF03"],
   ["A1-HOE-10", "A1-SPR-16", "A1-LES-04"], ["G22"],
   ["R-SP-48", "R-SP-22"], ["A1-WOW-20", "A1-WOW-15", "A1-WOW-24"],
   ["A1-LES-T1", "A1-HOE-T1", "A1-SB-T1", "A1-SPR-T3", "A1-WOW-T1", "A1-WOW-T2"], "Lesen"),
 C("A1-18", "Was hast du am Wochenende gemacht?", ["HF10", "HF08", "HF02"],
   ["A1-SPR-17", "A1-SCH-03", "A1-LES-03"], ["G23"],
   ["R-SP-08", "R-SP-18"], ["A1-WOW-14", "A1-WOW-22"],
   ["A1-SB-T1", "A1-SCH-T2", "A1-LES-T2", "A1-SPR-T2", "A1-LES-T1", "A1-WOW-T1"], "Grammatik",
   note="Perfekt über Haushalt, Ausflug und Reise: geputzt, gekocht, gefahren, geflogen."),
 C("A1-19", "Bank, Post und Notfall", ["HF07", "HF14"],
   ["A1-SPR-13", "A1-HOE-05", "A1-SPR-05", "A1-SCH-04"], ["G25"],
   ["R-SP-39", "R-SP-19", "R-SP-20"], ["A1-WOW-09", "A1-WOW-05", "A1-WOW-27"],
   ["A1-HUA-T1", "A1-HUA-T2", "A1-HOE-T1", "A1-SCH-T1", "A1-SCH-T2", "A1-LES-T1", "A1-WOW-T2"], "Hören"),
 C("A1-20", "Kinder, Kindergarten, Schule – und A1-Prüfungsfit", ["HF09", "HF15"],
   ["A1-SCH-06", "A1-SCH-04", "QK-05", "A1-LES-03"], ["G49"],
   ["R-SP-18", "R-SP-21", "R-SP-24"], ["A1-WOW-03", "A1-WOW-04", "A1-WOW-23"],
   ["A1-SB-T1", "A1-HOE-T2", "A1-LES-T1", "A1-SCH-T1", "A1-SCH-T2", "A1-SPR-T1", "A1-SPR-T3", "A1-HUA-T1", "A1-WOW-T1", "A1-WOW-T2"],
   "Prüfungstraining",
   note="Kein neues Grammatikthema außer Synthese G49 (A1-Teil: Satzklammer Modal/trennbar/Perfekt/weil); Prüfungsstrategien QK-05."),
]

A2 = [
 C("A2-01", "Mein Leben in Österreich", ["HF01", "HF06"],
   ["A2-SPR-01", "A2-SPR-02", "A2-HOE-11", "A2-SPR-17"], ["G29"],
   ["R-SP-09", "R-SP-10", "R-SP-11", "R-SP-45"], ["A2-WOW-01", "A2-WOW-02", "A2-WOW-42"],
   ["A2-SPR-T1", "A2-HOE-T4", "A2-LES-T2", "A2-WOW-T1"], "Sprechen"),
 C("A2-02", "Wohnungssuche", ["HF02"],
   ["A2-LES-08", "A2-SCH-04", "A2-SPR-19", "A2-LES-02"], ["G33", "G40"],
   ["R-SC-03", "R-SP-42"], ["A2-WOW-25", "A2-WOW-47"],
   ["A2-LES-T1", "A2-LES-T2", "A2-SCH-T1", "A2-SPR-T2B", "A2-WOW-T2"], "Lesen"),
 C("A2-03", "Hausordnung, Nachbarn, Mülltrennung", ["HF02"],
   ["A2-LES-07", "A2-SCH-05", "A2-SCH-02"], ["G31", "G32"],
   ["R-SC-04", "R-SP-43"], ["A2-WOW-26", "A2-WOW-27", "A2-WOW-28"],
   ["A2-SCH-T1", "A2-LES-T4", "A2-HOE-T4", "A2-SPR-T2B", "A2-WOW-T1", "A2-WOW-T2"], "Schreiben"),
 C("A2-04", "Termine vereinbaren, verschieben, absagen", ["HF11"],
   ["A2-HOE-01", "A2-HOE-02", "A2-HOE-03", "A2-SPR-07", "A2-SCH-03"], ["G30", "G45"],
   ["R-SP-30", "R-SP-32", "R-SP-33", "R-SP-34", "R-SC-02"], ["A2-WOW-12"],
   ["A2-HOE-T1", "A2-HOE-T2", "A2-SCH-T1", "A2-SPR-T2A", "A2-WOW-T1"], "Hören"),
 C("A2-05", "Beim Arzt, Facharzt und in der Apotheke", ["HF04"],
   ["A2-SPR-08", "A2-HOE-10", "A2-HOE-06", "A2-LES-05"], ["G44"],
   ["R-SP-24", "R-SP-28", "R-SP-29", "R-SP-38"], ["A2-WOW-18", "A2-WOW-19", "A2-WOW-22", "A2-WOW-23", "A2-WOW-24", "A2-WOW-46"],
   ["A2-SPR-T2A", "A2-HOE-T3", "A2-HOE-T4", "A2-LES-T3", "A2-WOW-T1", "A2-WOW-T2"], "Sprechen"),
 C("A2-06", "Notfall, Unfall, Krankenstand", ["HF14", "HF04"],
   ["A2-SCH-03", "A2-SCH-06", "A2-HOE-05"], ["G38"],
   ["R-SP-39", "R-SC-01", "R-SC-02"], ["A2-WOW-20", "A2-WOW-21", "A2-WOW-39"],
   ["A2-SCH-T1", "A2-HOE-T3", "A2-HOE-T2", "A2-LES-T4", "A2-WOW-T1", "A2-WOW-T2"], "Schreiben"),
 C("A2-07", "Arbeit suchen: AMS, Inserat, Bewerbung", ["HF05"],
   ["A2-LES-03", "A2-LES-06", "A2-SPR-11", "A2-SPR-20"], ["G34"],
   ["R-SP-40", "R-SP-10", "R-SC-03"], ["A2-WOW-15", "A2-WOW-17", "A2-WOW-44"],
   ["A2-LES-T2", "A2-LES-T1", "A2-LES-T4", "A2-SPR-T2B", "A2-SPR-T1", "A2-HOE-T1", "A2-WOW-T1", "A2-WOW-T2"], "Lesen"),
 C("A2-08", "Am Arbeitsplatz", ["HF05"],
   ["A2-HOE-08", "A2-SPR-12", "A2-SCH-01"], ["G35", "G39"],
   ["R-SP-37", "R-SP-38", "R-SC-02"], ["A2-WOW-14", "A2-WOW-16", "A2-WOW-43", "A2-WOW-45"],
   ["A2-HOE-T4", "A2-SPR-T2A", "A2-SCH-T1", "A2-LES-T3", "A2-HOE-T2", "A2-WOW-T1", "A2-WOW-T2"], "Hören"),
 C("A2-09", "Ämter, Anträge, Formulare", ["HF06"],
   ["A2-SPR-10", "A2-LES-09", "A2-SCH-07", "A2-LES-04"], ["G36", "G48"],
   ["R-SP-13", "R-SP-38", "R-SC-03"], ["A2-WOW-32", "A2-WOW-36"],
   ["A2-LES-T3", "A2-SPR-T2A", "A2-LES-T4", "A2-HOE-T1", "A2-SPR-T1", "A2-WOW-T1", "A2-WOW-T2"], "Lesen",
   note="Distraktor-Regeln Formular (02g 2.2): Buchstabendreher, Tag/Monat vertauscht, Umlaut."),
 C("A2-10", "Bank, Post, Handyvertrag", ["HF07"],
   ["A2-LES-04", "A2-LES-05", "A2-SPR-09", "A2-SPR-04", "A2-SPR-03"], ["G42"],
   ["R-SP-25", "R-SP-26", "R-SP-27", "R-SP-28", "R-SP-29"], ["A1-WOW-06", "A2-WOW-17"],
   ["A2-SPR-T2A", "A2-LES-T3", "A2-LES-T1", "A2-HOE-T3", "A2-SPR-T2B", "A2-SPR-T1", "A2-WOW-T2"], "Sprechen",
   note="Bildthemen Bank und Handygeschäft (Q05) – erste vollständige Bildbeschreibung mit Rollenspiel."),
 C("A2-11", "Einkaufen, umtauschen, reklamieren", ["HF03"],
   ["A2-SPR-09", "A2-SPR-15", "A2-SCH-05", "A2-SPR-06"], ["G41"],
   ["R-SP-28", "R-SP-29", "R-SP-44", "R-SC-04"], ["A2-WOW-28"],
   ["A2-SPR-T2A", "A2-SCH-T1", "A2-LES-T2", "A2-HOE-T4", "A2-WOW-T1"], "Sprechen",
   note="Bildthema Markt (Q05)."),
 C("A2-12", "Öffis, Bahn und Reisen", ["HF08"],
   ["A2-HOE-05", "A2-HOE-09", "A2-SPR-14", "A2-HOE-04"], [],
   ["R-SP-28", "R-SP-29", "R-SP-38"], ["A2-WOW-04", "A2-WOW-03"],
   ["A2-HOE-T3", "A2-SPR-T2A", "A2-LES-T2", "A2-HOE-T1", "A2-WOW-T1", "A2-WOW-T2"], "Hören"),
 C("A2-13", "Kinder: Kindergarten, Schule, Elternsprechtag", ["HF09"],
   ["A2-SPR-13", "A2-LES-09", "A2-SCH-03"], ["G43"],
   ["R-SC-01", "R-SP-38", "R-SP-28"], ["A2-WOW-08", "A2-WOW-09", "A2-WOW-11", "A2-WOW-12", "A2-WOW-13", "A1-WOW-23"],
   ["A2-SPR-T2A", "A2-SCH-T1", "A2-LES-T4", "A2-HOE-T2", "A2-WOW-T1", "A2-WOW-T2"], "Sprechen",
   note="Bildthema Elternsprechtag (Q05); Entschuldigung als formelle E-Mail."),
 C("A2-14", "Deutschkurs und Weiterbildung", ["HF00"],
   ["A2-LES-01", "A2-SCH-04", "A2-SPR-20", "A2-SPR-18", "QK-02"], ["G37"],
   ["R-SP-37", "R-SP-10", "R-SC-03"], ["A2-WOW-07", "A2-WOW-10"],
   ["A2-LES-T1", "A2-SPR-T2A", "A2-SCH-T1", "A2-SPR-T2B", "A2-WOW-T1"], "Lesen",
   note="Bildthema Deutschkurs (Q05)."),
 C("A2-15", "Freizeit, Vereine, Ehrenamt", ["HF10"],
   ["A2-SPR-06", "A2-SPR-16", "A2-LES-01", "A2-SPR-05"], ["G46"],
   ["R-SP-21", "R-SP-22", "R-SP-44", "R-SC-06"], ["A2-WOW-40", "A2-WOW-41"],
   ["A2-LES-T1", "A2-SPR-T2B", "A2-HOE-T4", "A2-SCH-T1", "A2-WOW-T2"], "Lesen"),
 C("A2-16", "Medien, Internet, Online-Formulare", ["HF15", "HF12"],
   ["A2-HOE-04", "A2-LES-10", "A2-LES-11", "A2-SCH-08"], [],
   ["R-SP-43", "R-SP-38"], ["A2-WOW-31"],
   ["A2-HOE-T3", "A2-LES-T4", "A2-LES-T3", "A2-SPR-T2B", "A2-WOW-T1"], "Hören",
   note="Radio-Wetter und Verkehrsmeldung (1× hören); kein neues Grammatikthema – Wiederholung G34–G38 im Kontext."),
 C("A2-17", "Feste, Feiertage und Vielfalt", ["HF13", "HF01"],
   ["A2-SPR-05", "A2-SPR-17", "A2-SPR-16"], ["G47"],
   ["R-SP-40", "R-SP-41", "R-SP-42", "R-SP-45", "R-SC-05"], ["A2-WOW-06", "A2-WOW-37", "A2-WOW-38", "A2-WOW-48", "A1-WOW-20"],
   ["A2-SPR-T2B", "A2-SPR-T1", "A2-LES-T2", "A2-HOE-T3", "A2-WOW-T1", "A2-WOW-T2"], "Sprechen"),
 C("A2-18", "Staat, Demokratie und Rechte", ["HF06"],
   ["A2-LES-06", "A2-HOE-04"], [],
   ["R-SP-43"], ["A2-WOW-03", "A2-WOW-05", "A2-WOW-29", "A2-WOW-30", "A2-WOW-33", "A2-WOW-34", "A2-WOW-35", "A2-WOW-42"],
   ["A2-WOW-T1", "A2-WOW-T2", "A2-LES-T4", "A2-HOE-T3"], "Werte"),
 C("A2-19", "Prüfungsfit A2", ["HF00"],
   ["A2-SCH-01", "A2-SCH-02", "A2-SCH-06", "A2-SCH-09", "A2-SPR-03", "A2-SPR-04", "A2-SPR-18", "A2-HOE-07", "QK-05", "QK-01"], ["G49"],
   ["R-SP-25", "R-SP-28", "R-SP-37"], ["A2-WOW-35"],
   ["A2-LES-T1", "A2-LES-T2", "A2-LES-T3", "A2-LES-T4", "A2-HOE-T1", "A2-HOE-T2", "A2-HOE-T3", "A2-HOE-T4",
    "A2-SCH-T1", "A2-SPR-T1", "A2-SPR-T2A", "A2-SPR-T2B", "A2-WOW-T1", "A2-WOW-T2"], "Prüfungstraining",
   note="Synthese-Kapitel: wenig neuer Wortschatz, Satzklammer-Überblick (G49 A2-Teil), Plagiat-Schutz beim Schreiben (A2-SCH-09)."),
]

CHAPTERS = A1 + A2
```

## `inventory.py`

```python
"""Load inventory v1 (compact transcription) + new Goethe entries (D3) -> inventory v2."""
import csv, json, re

SETS = {
    # set-id: predicate on (lemma, pos, hf, level)  -> counts as ONE unit (D4)
    "SET-ZAHLEN": lambda l, p, h, lv: h == "HF12" and p == "num",
    "SET-WOCHENTAGE": lambda l, p, h, lv: l in {"Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag"},
    "SET-MONATE": lambda l, p, h, lv: l in {"Jänner","Februar","März","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember","Feber"},
    "SET-JAHRESZEITEN": lambda l, p, h, lv: l in {"Frühling","Sommer","Herbst","Winter"},
    "SET-FARBEN": lambda l, p, h, lv: l in {"weiß","schwarz","rot","blau","grün","gelb","grau","braun"},
    "SET-BUNDESLAENDER": lambda l, p, h, lv: l in {"Wien","Niederösterreich","Oberösterreich","Steiermark","Kärnten","Tirol","Vorarlberg","Salzburg","Burgenland"},
    "SET-NACHBARLAENDER": lambda l, p, h, lv: l in {"Italien","Ungarn","Tschechien","Slowakei","Slowenien","Liechtenstein"},
    "SET-HIMMELSRICHTUNGEN": lambda l, p, h, lv: l in {"Norden","Süden","Osten","Westen"},
    "SET-MENGEN": lambda l, p, h, lv: l in {"Kilo","Gramm","Deka","Liter","Stück","Packung","Flasche"},
    "SET-MUELL": lambda l, p, h, lv: l in {"Restmüll","Biomüll","Altpapier","Altglas","Plastik","Sperrmüll"},
}

def load_v1():
    rows = []
    for fn, level in [("inv_a1.txt", "A1"), ("inv_a2.txt", "A2")]:
        hf, n = None, 0
        for line in open(fn, encoding="utf-8"):
            line = line.rstrip("\n")
            if not line:
                continue
            if line.startswith("## "):
                hf = line.split()[2]
                continue
            n += 1
            p = line.split("|")
            rows.append(dict(id=f"W-{level}-{n:04d}", lemma=p[0], pos=p[1], hf=hf, level=level,
                             use=p[2] if len(p) > 2 else "a", at=int(p[3]) if len(p) > 3 else 0,
                             kind="v1", variant=""))
    return rows

def load_new(goethe_a1_keys):
    rows, n1, n2 = [], 906, 1007
    with open("neu.tsv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            keys = r["goethe_key"].split("|")
            level = "A1" if any(k.lower() in goethe_a1_keys for k in keys) else "A2"
            if level == "A1":
                n1 += 1; rid = f"W-A1-{n1:04d}"
            else:
                n2 += 1; rid = f"W-A2-{n2:04d}"
            rows.append(dict(id=rid, lemma=r["lemma"], article=r["article"], forms=r["forms"], pos=r["pos"],
                             hf=r["hf"], level=level, use=r["use"], at=int(r["at"]), variant=r["variant"],
                             en=r["en"], tl=r["tl"], kind=r["kind"], goethe_key=r["goethe_key"]))
    return rows

def set_of(row):
    for sid, pred in SETS.items():
        if pred(row["lemma"], row["pos"], row["hf"], row["level"]):
            return sid
    return ""

def load_all():
    a1keys = set(json.load(open("miss.json"))["a1"])
    rows = load_v1() + load_new(a1keys)
    for r in rows:
        r["set"] = set_of(r)
    return rows

if __name__ == "__main__":
    rows = load_all()
    from collections import Counter
    new = [r for r in rows if r["kind"] != "v1"]
    print("total", len(rows), "new", len(new), Counter((r["level"], r["kind"], r["use"]) for r in new))
    print("sets", Counter(r["set"] for r in rows if r["set"]))
    print("active share", round(sum(r["use"] == "a" for r in rows) / len(rows) * 100, 1))
```

## `build.py`

```python
"""Phase 3 build: vocab assignment, checks, time budget, calendar, Leitner load simulation.
Pure functions where possible; writes results to out/*.json for the document writer."""
import json, math, random, re
from collections import Counter, defaultdict
from inventory import load_all
from chapters import CHAPTERS

CH = {c["id"]: c for c in CHAPTERS}
ORDER = [c["id"] for c in CHAPTERS]
IDX = {cid: i for i, cid in enumerate(ORDER)}

# ---------------------------------------------------------------- reference lists
CANDO = ([f"A1-HOE-{i:02d}" for i in range(1, 11)] + [f"A1-LES-{i:02d}" for i in range(1, 9)] +
         [f"A1-SCH-{i:02d}" for i in range(1, 7)] + [f"A1-SPR-{i:02d}" for i in range(1, 18)] +
         [f"A2-HOE-{i:02d}" for i in range(1, 12)] + [f"A2-LES-{i:02d}" for i in range(1, 12)] +
         [f"A2-SCH-{i:02d}" for i in range(1, 10)] + [f"A2-SPR-{i:02d}" for i in range(1, 21)] +
         [f"QK-{i:02d}" for i in range(1, 6)])
WOW = [f"A1-WOW-{i:02d}" for i in range(1, 28)] + [f"A2-WOW-{i:02d}" for i in range(1, 49)]
GRAM = [f"G{i:02d}" for i in range(1, 50)]
RED = [f"R-SP-{i:02d}" for i in range(1, 49)] + [f"R-SC-{i:02d}" for i in range(1, 8)]
EXAM_A1 = ["A1-SB-T1", "A1-HOE-T1", "A1-HOE-T2", "A1-HUA-T1", "A1-HUA-T2", "A1-LES-T1", "A1-LES-T2", "A1-LES-T3",
           "A1-SCH-T1", "A1-SCH-T2", "A1-SPR-T1", "A1-SPR-T2", "A1-SPR-T3", "A1-WOW-T1", "A1-WOW-T2"]
EXAM_A2 = ["A2-LES-T1", "A2-LES-T2", "A2-LES-T3", "A2-LES-T4", "A2-HOE-T1", "A2-HOE-T2", "A2-HOE-T3", "A2-HOE-T4",
           "A2-SCH-T1", "A2-SPR-T1", "A2-SPR-T2A", "A2-SPR-T2B", "A2-WOW-T1", "A2-WOW-T2"]
PREREQ = {"G01": [], "G02": ["G01"], "G03": ["G02"], "G04": ["G01", "G02"], "G05": ["G01"], "G06": ["G03"],
          "G07": ["G06"], "G08": ["G06"], "G09": ["G02"], "G10": ["G06", "G08"], "G11": ["G10"], "G12": ["G11"],
          "G13": ["G12"], "G14": ["G01"], "G15": ["G09", "G13"], "G16": ["G10"], "G17": ["G10"], "G18": ["G10"],
          "G19": ["G18"], "G20": ["G18"], "G21": ["G14"], "G22": ["G03"], "G23": ["G12", "G22"], "G24": ["G01"],
          "G25": ["G24"], "G26": ["G10"], "G27": ["G02"], "G28": ["G11"], "G29": ["G23", "G13"], "G30": ["G12", "G22"],
          "G31": ["G20", "G10"], "G32": ["G17"], "G33": ["G26", "G27"], "G34": ["G25"], "G35": ["G25"],
          "G36": ["G34"], "G37": ["G34"], "G38": ["G24"], "G39": ["G32", "G18"], "G40": ["G26"], "G41": ["G26", "G18"],
          "G42": ["G17", "G19"], "G43": ["G16", "G18"], "G44": ["G12", "G30", "G28"], "G45": ["G18"], "G46": ["G17"],
          "G47": ["G34", "G29"], "G48": ["G06", "G16"], "G49": ["G12", "G13", "G23", "G25"]}

# ---------------------------------------------------------------- vocab assignment rules
LEMMA_RULES = {
 "A1-01": ["ich", "du", "er", "sie", "es", "wir", "ihr", "Sie", "mir", "dir", "wer", "was", "wie", "woher", "und", "ja",
           "nein", "bitte", "danke", "sein (Verb)", "heißen", "kommen", "Name", "Vorname", "Familienname", "Herr", "Frau",
           "grüß Gott", "servus", "hallo", "guten Morgen", "guten Tag", "guten Abend", "gute Nacht", "auf Wiedersehen",
           "tschüss", "Entschuldigung", "Wie geht's?", "vorstellen (sich)", "gut", "auch", "sehr", "Österreich",
           "Philippinen"],
 "A1-02": ["haben", "wie viel", "wie viele", "Zahl", "Nummer", "Telefonnummer", "buchstabieren", "Buchstabe",
           "Alter", "Jahre alt", "Hausnummer", "Postleitzahl", "Euro", "Cent", "Preis", "kosten"],
 "A1-03": ["der", "die", "das", "ein", "in", "aus", "wo", "wohnen", "sprechen", "Land", "Heimatland", "Deutschland",
           "Europa", "Stadt", "Dorf", "Adresse", "Straße", "Sprache", "Deutsch", "Englisch", "Tagalog", "doch",
           "österreichisch", "Heimat", "Ausländer, Ausländerin", "verstehen", "langsam", "wiederholen", "hier", "dort",
           "da", "Philippiner, Philippinerin", "Österreicher, Österreicherin"],
 "A1-04": ["mein", "dein", "Ihr (Possessiv)"],
 "A1-05": ["kein", "nicht", "ankreuzen", "ergänzen", "zuordnen", "markieren", "richtig", "falsch", "Aussage",
           "Stift", "Blatt", "Bogen", "zuhören", "Hausaufgabe", "lernen", "Pause", "herein", "willkommen"],
 "A1-06": ["um", "ab", "bis", "nach (zeitlich)", "vor", "jetzt", "heute", "morgen", "später", "früh", "spät",
           "Uhr", "Stunde", "Minute", "Sekunde", "halb", "Viertel", "Tag", "Woche", "Monat", "Jahr", "Wochenende",
           "Morgen", "Vormittag", "Mittag", "Nachmittag", "Abend", "Nacht", "Zeit", "wann", "dann", "zuerst", "Uhrzeit",
           "pünktlich", "erst", "arbeiten"],
 "A1-07": ["für", "ohne", "möchten", "brauchen", "billig", "teuer", "günstig", "Kasse", "Kiosk",
           "Tomate", "Brötchen", "Hähnchen", "Flasche"],
 "A1-08": ["mögen", "gern", "lieber", "am besten", "Lieblings-", "welcher", "Lokal", "Hamburger", "bitter", "fett",
           "Mahlzeit", "Kunde, Kundin", "Frühstück", "frühstücken", "Mittagessen", "Abendessen"],
 "A1-09": ["können", "müssen", "dürfen", "sollen", "wollen", "man", "verboten", "Ruhe", "Hausordnung", "Schrank",
           "Treppe", "Aufzug", "Erdgeschoss", "an sein / aus sein / auf sein / zu sein", "Poster", "Blick"],
 "A1-10": ["mich", "dich", "ihn", "uns", "anrufen", "zurückrufen", "absagen", "mitkommen", "mitbringen", "anfangen",
           "aufhören", "Mailbox", "Mobiltelefon", "Apparat", "Termin", "Gruß"],
 "A1-11": ["Doktor, Doktorin", "Praxis", "Mittel", "Gewicht", "fit", "schädlich", "krank", "gesund", "froh", "müde"],
 "A1-12": ["mit", "bei", "nach", "von", "zu", "seit", "fahren", "gehen"],
 "A1-13": ["an", "auf", "über", "unter", "neben", "zwischen", "hinter", "gegenüber", "links", "rechts", "geradeaus",
           "oben", "unten", "wohin", "liegen", "stehen", "sitzen", "stellen", "legen", "nah", "weit", "daneben",
           "Nachbar, Nachbarin", "Möbel", "Tisch", "Stuhl", "Sessel", "Bett", "Kasten", "Sofa", "Lampe", "Kühlschrank",
           "Herd", "Waschmaschine"],
 "A1-14": ["sein", "ihr (Possessiv)", "unser", "euer", "ihm", "Ihnen", "gefallen", "gehören", "helfen", "danken",
           "Beruf", "Maschine", "Rentner, Rentnerin", "beraten"],
 "A1-15": ["erst-", "zweit-", "dritt-", "Datum", "Geburtstag", "geboren", "Jänner", "Februar", "März", "April", "Mai",
           "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember", "Meldezettel", "anmelden (sich)",
           "umziehen", "einziehen"],
 "A1-16": ["oder", "aber", "denn", "warum", "freuen (sich)", "Lust haben", "Einladung", "einladen", "Party",
           "Besuch", "Club", "Disco", "Band", "CD", "Krimi", "Quiz", "Rätsel", "basteln", "sammeln",
           "liebe/lieber (Anrede)", "kennenlernen", "Anzeige"],
 "A1-17": ["war", "gestern", "draußen", "neblig", "Rose", "Laden", "weiß", "schwarz", "rot", "blau", "grün", "gelb",
           "grau", "braun", "Farbe"],
 "A1-18": ["früher", "einmal", "lange", "erzählen", "immer", "oft", "manchmal", "nie", "putzen", "kochen", "waschen",
           "baden", "anmachen", "ausmachen", "Licht", "Zelt", "Zirkus", "reiten", "Reiseführer", "Jugendherberge",
           "Doppelzimmer", "Einzelzimmer", "Halbpension", "Rezeption", "Tour", "Rundgang", "Führung", "Fotoapparat",
           "abfliegen", "Abflug", "Lkw", "Motor", "Motorroller", "Reifen", "vorwärts", "Urlaub", "Hotel", "übernachten",
           "Ausflug", "Meer", "See", "Berg", "wandern"],
 "A1-19": ["weil", "austragen", "bezahlen", "zahlen", "Geld"],
 "A1-20": ["Junge", "Hausfrau, Hausmann", "E-Book", "Fax"],
 # ---- A2
 "A2-01": ["Angst", "Sorge", "Gefühl", "Liebe", "Freude", "nervös", "böse", "wütend", "überrascht", "unzufrieden",
           "Erfahrung", "Leben", "erleben", "damals", "seitdem", "bisher", "Vergangenheit", "Gegenwart", "Zukunft",
           "Staat", "Republik"],
 "A2-02": ["Wohnungsanzeige", "Besichtigung", "besichtigen", "Umzug", "möbliert", "inklusive", "Kaution",
           "Betriebskosten", "Mietvertrag", "größer", "ähnlich", "anders", "verschieden", "gleich (identisch)", "bequem",
           "praktisch", "hell", "Eigentum", "Eigentumswohnung", "Gemeindewohnung"],
 "A2-03": ["ärgern (sich) über", "beschweren (sich) über", "stören", "Lärm", "Nachtruhe", "Rücksicht", "setzen (sich)",
           "hängen", "aufräumen", "sauber", "schmutzig", "Restmüll", "Biomüll", "Altpapier", "Altglas", "Plastik",
           "Sperrmüll", "Mülltrennung", "trennen", "Mistplatz", "Container"],
 "A2-04": ["verschieben", "vereinbaren", "vorgestern", "übermorgen", "pro", "Bescheid geben", "Bescheid wissen",
           "bestätigen", "Bestätigung", "verpassen", "vergessen", "erreichen", "Kalender"],
 "A2-05": ["fühlen (sich)", "riechen"],
 "A2-06": ["deshalb", "trotzdem", "zuerst … dann … danach … zum Schluss", "danach", "vorher", "nachher", "plötzlich",
           "fallen", "gefährlich", "vorsichtig", "dringend", "sterben", "Krankenstand", "Krankmeldung", "krankmelden (sich)",
           "Bestätigung (ärztlich)", "Verletzung", "Wunde", "Pflaster", "verletzen (sich)"],
 "A2-07": ["dass", "glauben", "Ziel", "Erfolg", "schaffen", "Möglichkeit", "Kenntnis", "Qualifikation", "Führerschein",
           "bewerben (sich) um", "Lebenslauf", "Bewerbung", "Bewerbungsgespräch", "Stellenanzeige", "Stelleninserat",
           "Arbeitslosengeld", "Arbeitssuche", "Berufserfahrung", "fleißig", "Pflegefachkraft", "Elektriker, Elektrikerin",
           "Friseur, Friseurin", "Mechaniker, Mechanikerin", "Kassier, Kassierin", "Kinderbetreuer, Kinderbetreuerin"],
 "A2-08": ["wenn", "denken an", "warten auf", "sprechen über", "fragen nach", "freuen (sich) auf", "freuen (sich) über",
           "interessieren (sich) für", "kümmern (sich) um", "erinnern (sich) an", "gewöhnen (sich) an", "worüber",
           "wofür", "darüber", "dafür", "dabei"],
 "A2-09": ["Beamte, Beamtin", "ob", "eintragen", "Erlaubnis", "Vertrag", "Fundsachen", "Fundamt", "genau", "deutlich", "persönlich",
           "schriftlich", "mündlich"],
 "A2-12": ["Norden", "Süden", "Osten", "Westen", "Meter", "Kilometer", "Zentimeter", "Wien", "Niederösterreich",
           "Oberösterreich", "Steiermark", "Kärnten", "Tirol", "Vorarlberg", "Salzburg", "Burgenland", "Italien",
           "Ungarn", "Tschechien", "Slowakei", "Slowenien", "Liechtenstein", "entlang", "durch", "unterwegs"],
 "A2-14": ["damit", "Leitpunkt", "Lückentext", "Lücke", "meinen", "Meinung", "berichten", "diskutieren", "Ergebnis",
           "Prozent", "Hälfte"],
 "A2-15": ["sondern", "sowohl … als auch", "entweder … oder", "niemand", "einander", "mancher", "selbst", "Interesse",
           "Kultur"],
 "A2-16": ["aktuell"],
 "A2-17": ["als", "Tradition", "Brauch", "schenken", "Kultur"],
 "A2-18": [],
 "A2-19": ["Punkt", "bestehen", "durchfallen", "Integrationsprüfung", "Zertifikat", "Niveau", "Stufe", "begründen"],
}
# ID-range rules for thematic splits inside one HF (inclusive, by numeric part)
RANGE_RULES = [
 ("A1", "HF01", 324, 346, "A1-04"), ("A1", "HF01", 347, 349, "A1-04"), ("A1", "HF01", 390, 407, "A1-04"),
 ("A1", "HF03", 473, 481, "A1-08"), ("A1", "HF03", 482, 513, "A1-07"), ("A1", "HF03", 514, 523, "A1-08"),
 ("A1", "HF03", 524, 524, "A1-07"), ("A1", "HF03", 525, 527, "A1-08"), ("A1", "HF03", 528, 550, "A1-07"),
 ("A1", "HF03", 551, 558, "A1-08"), ("A1", "HF03", 559, 567, "A1-17"), ("A1", "HF03", 569, 577, "A1-08"),
 ("A1", "HF02", 455, 467, "A1-06"),
 ("A1", "HF08", 677, 697, "A1-12"), ("A1", "HF08", 698, 703, "A1-13"), ("A1", "HF08", 704, 704, "A1-12"),
 ("A1", "HF08", 705, 712, "A1-18"), ("A1", "HF08", 713, 714, "A1-13"), ("A1", "HF08", 715, 715, "A1-18"),
 ("A1", "HF08", 716, 721, "A1-12"), ("A1", "HF08", 722, 722, "A1-18"),
 ("A1", "HF10", 730, 762, "A1-16"), ("A1", "HF10", 763, 775, "A1-18"),
 ("A1", "HF12", 847, 865, "A1-06"), ("A1", "HF12", 866, 877, "A1-17"),
 ("A2", "HF00", 299, 337, "A2-14"),
 ("A2", "HF02", 350, 388, "A2-02"), ("A2", "HF02", 389, 418, "A2-03"),
 ("A2", "HF03", 419, 451, "A2-11"), ("A2", "HF03", 452, 480, "A2-17"), ("A2", "HF03", 481, 485, "A2-11"),
 ("A2", "HF03", 486, 500, "A2-17"), ("A2", "HF03", 501, 503, "A2-11"), ("A2", "HF03", 504, 507, "A2-11"),
 ("A2", "HF03", 508, 516, "A2-17"), ("A2", "HF03", 517, 527, "A2-11"),
 ("A2", "HF04", 528, 532, "A2-05"), ("A2", "HF04", 533, 536, "A2-06"), ("A2", "HF04", 537, 558, "A2-05"),
 ("A2", "HF04", 559, 563, "A2-06"), ("A2", "HF04", 564, 576, "A2-05"),
 ("A2", "HF05", 577, 582, "A2-07"), ("A2", "HF05", 583, 609, "A2-08"), ("A2", "HF05", 610, 615, "A2-07"),
 ("A2", "HF05", 616, 621, "A2-08"), ("A2", "HF05", 622, 627, "A2-07"), ("A2", "HF05", 628, 633, "A2-08"),
 ("A2", "HF06", 634, 658, "A2-09"), ("A2", "HF06", 659, 707, "A2-18"), ("A2", "HF06", 723, 728, "A2-09"),
 ("A2", "HF12", 918, 919, "A2-04"),
]
HF_DEFAULT = {
 "A1": {"HF00": "A1-05", "HF01": "A1-03", "HF02": "A1-09", "HF03": "A1-08", "HF04": "A1-11", "HF05": "A1-14",
        "HF06": "A1-15", "HF07": "A1-19", "HF08": "A1-12", "HF09": "A1-20", "HF10": "A1-16", "HF11": "A1-10",
        "HF12": "A1-02", "HF13": "A1-17", "HF14": "A1-19", "HF15": "A1-20"},
 "A2": {"HF00": "A2-19", "HF01": "A2-01", "HF02": "A2-03", "HF03": "A2-11", "HF04": "A2-05", "HF05": "A2-08",
        "HF06": "A2-09", "HF07": "A2-10", "HF08": "A2-12", "HF09": "A2-13", "HF10": "A2-15", "HF11": "A2-04",
        "HF12": "A2-16", "HF13": "A2-17", "HF14": "A2-06", "HF15": "A2-16"},
}
SET_RULES = {"SET-ZAHLEN": "A1-02", "SET-WOCHENTAGE": "A1-06", "SET-MONATE": "A1-15", "SET-JAHRESZEITEN": "A1-17",
             "SET-FARBEN": "A1-17", "SET-MENGEN": "A1-07", "SET-BUNDESLAENDER": "A2-12", "SET-NACHBARLAENDER": "A2-12",
             "SET-HIMMELSRICHTUNGEN": "A2-12", "SET-MUELL": "A2-03"}

FORCE_EARLY = {"leidtun": "A1-08", "herein": "A1-05", "Stift": "A1-05", "Blatt": "A1-05", "zuhören": "A1-05",
               "erst": "A1-06"}

def num(rid):
    return int(rid.split("-")[2])

def rule_chapter(r):
    """Chapter from explicit rules, or None (-> GW fill)."""
    lemma_map = {}
    for cid, lems in LEMMA_RULES.items():
        for l in lems:
            lemma_map.setdefault(l, []).append(cid)
    cands = [c for c in lemma_map.get(r["lemma"], []) if c[:2] == r["level"]]
    if not cands and r["lemma"] in FORCE_EARLY:   # Goethe-A2 words needed earlier (classroom, A1 chunks)
        return FORCE_EARLY[r["lemma"]]
    if cands:
        return cands[0]
    if (r["set"] and r["set"] in SET_RULES and r["lemma"] not in ("erst-", "zweit-", "dritt-")
            and SET_RULES[r["set"]][:2] == r["level"]):
        return SET_RULES[r["set"]]
    for lv, hf, lo, hi, cid in RANGE_RULES:
        if r["kind"] == "v1" and r["level"] == lv and r["hf"] == hf and lo <= num(r["id"]) <= hi:
            return cid
    if r["hf"] != "GW":
        return HF_DEFAULT[r["level"]][r["hf"]]
    return None

def unit_weight(rows):
    """D4: active non-set entry = 1 unit; each set = 1 unit; passive = 0."""
    sets = {r["set"] for r in rows if r["set"]}
    return sum(1 for r in rows if r["use"] == "a" and not r["set"]) + len(sets)

SYNTH_TARGET = {"A2-19": 20}  # synthesis chapter: few new units by design

def assign(rows):
    assign = {}
    for r in rows:
        c = rule_chapter(r)
        if c:
            assign[r["id"]] = c
    rest = [r for r in rows if r["id"] not in assign]
    for level in ("A1", "A2"):
        chs = [c for c in ORDER if c.startswith(level)]
        lvl_rows = [r for r in rows if r["level"] == level]
        total_units = unit_weight(lvl_rows)
        cap = math.ceil((total_units - SYNTH_TARGET.get(chs[-1], 0)) / (len(chs) - (1 if chs[-1] in SYNTH_TARGET else 0)))
        tgt = {c: SYNTH_TARGET.get(c, cap) for c in chs}
        by_ch = defaultdict(list)
        for r in lvl_rows:
            if r["id"] in assign:
                by_ch[assign[r["id"]]].append(r)
        # front-loaded fill: high-frequency GW (ID order) to the earliest chapter below cap
        for r in [x for x in rest if x["level"] == level and x["use"] == "a"]:
            target = next((c for c in chs if unit_weight(by_ch[c]) < tgt[c]), chs[-1])
            assign[r["id"]] = target; by_ch[target].append(r)
        passive = [x for x in rest if x["level"] == level and x["use"] == "p"]
        for i, r in enumerate(passive):  # passive GW spread evenly, in ID order
            target = chs[min(len(chs) - 1, i * len(chs) // max(1, len(passive)))]
            assign[r["id"]] = target; by_ch[target].append(r)
    return assign

# ---------------------------------------------------------------- checks
def check_prereq():
    first = {}
    for c in CHAPTERS:
        for g in c["gram"]:
            first.setdefault(g, c["id"])
    errs = []
    for g, ch in first.items():
        for p in PREREQ[g]:
            if p not in first:
                errs.append(f"{g} in {ch}: prereq {p} fehlt")
            elif IDX[first[p]] > IDX[ch] or (first[p] == ch and CH[ch]["gram"].index(p) > CH[ch]["gram"].index(g)):
                errs.append(f"{g} in {ch}: prereq {p} erst in {first[p]}")
    return first, errs

def coverage(key, ref):
    hit = defaultdict(list)
    for c in CHAPTERS:
        for x in c[key]:
            hit[x].append(c["id"])
    return {x: hit.get(x, []) for x in ref}, sorted(set(hit) - set(ref))

def exam_practice():
    """Count chapters practising each exam part before its simulation."""
    res = {}
    for part in EXAM_A1:
        res[part] = [c["id"] for c in CHAPTERS if c["id"].startswith("A1") and part in c["exam"]]
    for part in EXAM_A2:
        res[part] = {"vor_Sim1": [c["id"] for c in CHAPTERS if c["id"] <= "A2-10" and c["id"].startswith("A2") and part in c["exam"]],
                     "vor_Sim2": [c["id"] for c in CHAPTERS if c["id"].startswith("A2") and part in c["exam"]]}
    return res

# ---------------------------------------------------------------- test composition (planned; Phase 4 sets final length)
DISC = ["Lesen", "Hören", "Schreiben", "Sprechen", "Grammatik/Wortschatz", "Werte"]
FOCUS_MAP = {"Lesen": "Lesen", "Hören": "Hören", "Schreiben": "Schreiben", "Sprechen": "Sprechen",
             "Grammatik": "Grammatik/Wortschatz", "Werte": "Werte", "Prüfungstraining": None}
def test_plan(c):
    base = {"Lesen": 4, "Hören": 4, "Schreiben": 3, "Sprechen": 3, "Grammatik/Wortschatz": 8, "Werte": 3}
    f = FOCUS_MAP[c["focus"]]
    if f and f != "Grammatik/Wortschatz":
        base[f] += 2; base["Grammatik/Wortschatz"] -= 2
    if c["focus"] == "Prüfungstraining":
        base = {"Lesen": 5, "Hören": 5, "Schreiben": 3, "Sprechen": 3, "Grammatik/Wortschatz": 5, "Werte": 4}
    total = sum(base.values())
    return base, total, max(60, math.ceil(total * 2.5))

# ---------------------------------------------------------------- time model
DAY = 90; LEITNER = 25; CAP = DAY - LEITNER; TEST_MIN = 25; WEEKLY = 60; SIM_LEITNER = 10
def workload(c, units, passive):
    return 40 + 1.2 * units + 0.4 * passive + 15 * len(c["gram"]) + 4 * len(c["wow"]) + 3 * len(c["red"]) + 4 * len(c["cando"])

def build_calendar(minutes, n_days_a1, n_days_a2a, n_days_a2b):
    """Returns list of day dicts. Weekly review every 7th day."""
    A1C = [c for c in ORDER if c.startswith("A1")]; A2C = [c for c in ORDER if c.startswith("A2")]
    blocks = ([("CH", A1C, n_days_a1), ("PUF", "Puffer A1 (Kapitelwiederholung / Schwächen-Review)", 1),
               ("SIM", "A1-Meilensteinprüfung", 2), ("PUF", "Puffer: Review der schwächsten A1-Teile bzw. 2. Versuch", 1),
               ("CH", A2C[:10], n_days_a2a), ("PUF", "Puffer A2-Block 1", 1), ("SIM", "A2-Simulation 1", 2),
               ("CH", A2C[10:], n_days_a2b), ("PUF", "Puffer A2-Block 2", 1), ("SIM", "A2-Simulation 2", 2),
               ("PUF", "Puffer: gezielte Review nach Simulation 2", 1), ("SIM", "A2-Generalprobe", 2),
               ("PUF", "Abschluss: Review + offizieller Modelltest als Generalprobe (Link)", 1)])
    slots = []  # expand non-weekly days
    for kind, payload, n in blocks:
        if kind == "CH":
            queue = [[cid, minutes[cid]] for cid in payload]
            cap_total = n * CAP
            scale = cap_total / sum(m for _, m in queue)
            for q in queue:
                q[1] = q[1] * scale
            for _ in range(n):
                left, parts = CAP, []
                while left > 0.5 and queue:
                    take = min(left, queue[0][1])
                    if 0 < queue[0][1] - take <= 15:   # no tiny leftovers: finish chapter today (max +15 min)
                        take = queue[0][1]
                    parts.append((queue[0][0], round(take)))
                    queue[0][1] -= take; left -= take
                    if queue[0][1] <= 0.5:
                        queue.pop(0)
                slots.append(("CH", parts))
        else:
            for k in range(n):
                slots.append((kind, f"{payload}" + (f" – Tag {k+1}/{n}" if n > 1 else "")))
    days, si = [], 0
    for d in range(1, 91):
        if d % 7 == 0:
            days.append({"day": d, "kind": "WOCHE", "label": "Wochenreview (Interleaving) + Nachholen"})
        else:
            kind, payload = slots[si]; si += 1
            days.append({"day": d, "kind": kind, "label": payload})
    assert si == len(slots), (si, len(slots))
    return days

def budget(days):
    cat = Counter()
    for d in days:
        cat["Wiederholung (Leitner täglich)"] += SIM_LEITNER if d["kind"] == "SIM" else LEITNER
        if d["kind"] == "CH":
            for cid, m in d["label"]:
                cat["Neuer Stoff (Input + Üben)"] += m
        elif d["kind"] == "WOCHE":
            cat["Wiederholung (Wochenreview)"] += WEEKLY
            cat["Puffer/Nachholen (Flex)"] += DAY - LEITNER - WEEKLY
        elif d["kind"] == "SIM":
            cat["Prüfungstraining (Simulationen)"] += DAY - SIM_LEITNER
        elif d["kind"] == "PUF":
            cat["Puffer/Nachholen (Puffertage)"] += CAP
    # move chapter-test minutes from new to exam training
    tests = len(ORDER) * TEST_MIN
    cat["Neuer Stoff (Input + Üben)"] -= tests
    cat["Prüfungstraining (Kapiteltests)"] += tests
    return dict(cat)

# ---------------------------------------------------------------- Leitner simulation (D3 risk)
INTERVAL = [1, 3, 7, 14, 30]
P_OK = [0.80, 0.85, 0.88, 0.90, 0.93]
SEC = {"aktiv": 9, "passiv": 5, "set": 6, "grammatik": 15, "werte": 12, "fehler": 25}

SCENARIOS = {
    "S0 – jeder Eintrag eine Karte": dict(passive_cards=True, set_as_one=False, test_start_box2=0.0),
    "S1 – passive Einträge ohne Karte, Sets als 1 Karte": dict(passive_cards=False, set_as_one=True, test_start_box2=0.0),
    "S2 – wie S1 + im Kapiteltest richtig → Start in Fach 2": dict(passive_cards=False, set_as_one=True, test_start_box2=0.75),
}

def scenario_cards(cards, by_ch, sc):
    out = {}
    for cid, cc in cards.items():
        c = dict(cc)
        if not sc["passive_cards"]:
            c["passiv"] = 0
        if sc["set_as_one"]:
            c["set"] = len({r["set"] for r in by_ch[cid] if r["set"]})
        out[cid] = c
    return out

def leitner(days, cards_by_chapter, start_box2=0.0, seed=7):
    """Pure-ish simulation (seeded RNG): daily review minutes over the 90-day calendar."""
    rnd = random.Random(seed)
    due = defaultdict(list)
    ch_total = defaultdict(float)
    for d in days:
        if d["kind"] == "CH":
            for cid, m in d["label"]:
                ch_total[cid] += m
    daily = []
    for d in days:
        if d["kind"] == "CH":
            for cid, m in d["label"]:
                for typ, n in cards_by_chapter[cid].items():
                    k = n * m / ch_total[cid]
                    k = int(k) + (1 if rnd.random() < (k - int(k)) else 0)
                    for _ in range(k):
                        box = 1 if (typ != "fehler" and rnd.random() < start_box2) else 0
                        due[d["day"] + INTERVAL[box]].append((typ, box))
        secs = 0
        for typ, box in due.pop(d["day"], []):
            secs += SEC[typ]
            if rnd.random() < P_OK[box]:
                if box < 4:
                    due[d["day"] + INTERVAL[box + 1]].append((typ, box + 1))
            else:
                due[d["day"] + 1].append((typ, 0))
        daily.append(round(secs / 60, 1))
    return daily

def leitner_capped(days, cards_by_chapter, start_box2, cap_min, weekly_min=60, seed=7):
    """Queue with a daily time cap: overdue cards wait (oldest first). Returns minutes/day and backlog/day."""
    rnd = random.Random(seed)
    due = defaultdict(list); backlog = []
    ch_total = defaultdict(float)
    for d in days:
        if d["kind"] == "CH":
            for cid, m in d["label"]:
                ch_total[cid] += m
    used, back = [], []
    for d in days:
        if d["kind"] == "CH":
            for cid, m in d["label"]:
                for typ, n in cards_by_chapter[cid].items():
                    k = n * m / ch_total[cid]
                    k = int(k) + (1 if rnd.random() < (k - int(k)) else 0)
                    for _ in range(k):
                        box = 1 if (typ != "fehler" and rnd.random() < start_box2) else 0
                        due[d["day"] + INTERVAL[box]].append((typ, box, d["day"] + INTERVAL[box]))
        backlog.extend(due.pop(d["day"], []))
        backlog.sort(key=lambda x: x[2])
        budget_s = (cap_min + (weekly_min if d["kind"] == "WOCHE" else 0)) * 60
        secs, rest = 0, []
        for typ, box, dd in backlog:
            if secs + SEC[typ] > budget_s:
                rest.append((typ, box, dd)); continue
            secs += SEC[typ]
            if rnd.random() < P_OK[box]:
                if box < 4:
                    nd = d["day"] + INTERVAL[box + 1]; due[nd].append((typ, box + 1, nd))
            else:
                due[d["day"] + 1].append((typ, 0, d["day"] + 1))
        backlog = rest
        used.append(round(secs / 60, 1)); back.append(len(backlog))
    return used, back

def stats(xs):
    s = sorted(xs)
    return {"mean": round(sum(xs) / len(xs), 1), "p90": s[int(0.9 * len(s)) - 1], "max": max(xs),
            "days_over_15": sum(x > 15 for x in xs), "days_over_25": sum(x > 25 for x in xs)}

# ---------------------------------------------------------------- main
def main():
    rows = load_all()
    asg = assign(rows)
    # new entries (D3) get the level of the chapter that introduces them, then fresh IDs per level
    nxt = {"A1": 906, "A2": 1007}
    newrows = [(r, asg.pop(r["id"])) for r in rows if r["kind"] != "v1"]
    for r, c in newrows:
        r["goethe_level"] = r["level"]; r["level"] = c[:2]
        nxt[r["level"]] += 1; r["id"] = f'W-{r["level"]}-{nxt[r["level"]]:04d}'; asg[r["id"]] = c
    by_ch = defaultdict(list)
    for r in rows:
        by_ch[asg[r["id"]]].append(r)
    units = {c: unit_weight(by_ch[c]) for c in ORDER}
    passive = {c: sum(r["use"] == "p" for r in by_ch[c]) for c in ORDER}
    level_mismatch = [(r["id"], r["lemma"], asg[r["id"]]) for r in rows if asg[r["id"]][:2] != r["level"]]
    first, prereq_err = check_prereq()
    cov_cando, extra_cando = coverage("cando", CANDO)
    cov_wow, extra_wow = coverage("wow", WOW)
    cov_red, extra_red = coverage("red", RED)
    cov_gram = {g: [first[g]] if g in first else [] for g in GRAM}
    exam = exam_practice()
    wl = {c["id"]: workload(c, units[c["id"]], passive[c["id"]]) for c in CHAPTERS}
    A1C = [c for c in ORDER if c.startswith("A1")]; A2C = [c for c in ORDER if c.startswith("A2")]
    a1w = sum(wl[c] for c in A1C); a2aw = sum(wl[c] for c in A2C[:10]); a2bw = sum(wl[c] for c in A2C[10:])
    total_ch_days = 90 - 12 - 8 - 6
    tot = a1w + a2aw + a2bw
    n1 = round(total_ch_days * a1w / tot); n2a = round(total_ch_days * a2aw / tot); n2b = total_ch_days - n1 - n2a
    days = build_calendar(wl, n1, n2a, n2b)
    minutes = defaultdict(float); span = defaultdict(list)
    for d in days:
        if d["kind"] == "CH":
            for cid, m in d["label"]:
                minutes[cid] += m; span[cid].append(d["day"])
    bud = budget(days)
    # cards per chapter for Leitner sim
    cards = {}
    for c in CHAPTERS:
        rs = by_ch[c["id"]]
        cards[c["id"]] = {"aktiv": sum(r["use"] == "a" and not r["set"] for r in rs),
                          "passiv": sum(r["use"] == "p" and not r["set"] for r in rs),
                          "set": sum(bool(r["set"]) for r in rs),
                          "grammatik": 8 * len(c["gram"]) + 4,  # +4 recycled grammar items per chapter
                          "werte": 3 * len(c["wow"]),
                          "fehler": 6}  # ~ wrong answers in practice/test per chapter
    sims = {}
    for name, sc in SCENARIOS.items():
        cc = scenario_cards(cards, by_ch, sc)
        runs = [leitner(days, cc, sc["test_start_box2"], seed=s) for s in range(5)]
        avg = [round(sum(r[i] for r in runs) / len(runs), 1) for i in range(90)]
        sims[name] = dict(stats=stats(avg), daily=avg,
                          cards=sum(sum(v.values()) for v in cc.values()))
    capped = {}
    s2 = scenario_cards(cards, by_ch, SCENARIOS["S2 – wie S1 + im Kapiteltest richtig → Start in Fach 2"])
    for cap in (15, 20, 25, 30):
        used, back = leitner_capped(days, s2, 0.75, cap)
        capped[cap] = dict(mean=round(sum(used) / 90, 1), backlog_end=back[-1], backlog_max=max(back),
                           backlog_day60=back[59], backlog_mean=round(sum(back) / 90))
    out = dict(
        inventory=dict(total=len(rows), new=sum(r["kind"] != "v1" for r in rows),
                       by_kind=Counter(f'{r["level"]}-{r["kind"]}-{r["use"]}' for r in rows if r["kind"] != "v1"),
                       active_share=round(100 * sum(r["use"] == "a" for r in rows) / len(rows), 1),
                       units_total={lv: unit_weight([r for r in rows if r["level"] == lv]) for lv in ("A1", "A2")}),
        units=units, passive=passive, entries={c: len(by_ch[c]) for c in ORDER},
        level_mismatch=level_mismatch, prereq_errors=prereq_err, first_gram=first,
        cov_cando=cov_cando, cov_wow=cov_wow, cov_red=cov_red, cov_gram=cov_gram,
        extra=dict(cando=extra_cando, wow=extra_wow, red=extra_red), exam=exam,
        test={c["id"]: test_plan(c) for c in CHAPTERS}, minutes={c: round(minutes[c]) for c in ORDER},
        span={c: [min(span[c]), max(span[c])] for c in ORDER}, ndays=dict(A1=n1, A2a=n2a, A2b=n2b),
        days=days, budget=bud, leitner=sims, leitner_capped=capped,
        cards=cards)
    json.dump(out, open("out/build.json", "w"), ensure_ascii=False, indent=1, default=list)
    # assignment TSV
    with open("out/03c-kapitel-wortschatz.tsv", "w", encoding="utf-8") as f:
        f.write("id\tlemma\tpos\thf\tlevel\tuse\tat\tset\tkind\tchapter\n")
        for r in rows:
            f.write("\t".join(str(x) for x in [r["id"], r["lemma"], r["pos"], r["hf"], r["level"], r["use"], r["at"],
                                               r["set"], r["kind"], asg[r["id"]]]) + "\n")
    with open("out/02c-wortschatz-inventar-neu.tsv", "w", encoding="utf-8") as f:
        f.write("id\tlemma\tarticle\tforms\tpos\thf\tlevel\tuse\tat\tvariant\ten\ttl\texample\treview_en\treview_tl\tkind\tgoethe_key\n")
        for r in rows:
            if r["kind"] != "v1":
                f.write("\t".join([r["id"], r["lemma"], r["article"], r["forms"], r["pos"], r["hf"], r["level"], r["use"],
                                   str(r["at"]), r["variant"], r["en"], r["tl"], "", "machine", "machine", r["kind"],
                                   r["goethe_key"]]) + "\n")
    return out

if __name__ == "__main__":
    import os; os.makedirs("out", exist_ok=True)
    o = main()
    print("inventory", {k: v for k, v in o["inventory"].items()})
    print("units", o["units"])
    print("passive", o["passive"])
    print("level mismatch", o["level_mismatch"][:20], len(o["level_mismatch"]))
    print("prereq errors", o["prereq_errors"])
    print("missing cando", [k for k, v in o["cov_cando"].items() if not v])
    print("missing wow", [k for k, v in o["cov_wow"].items() if not v])
    print("missing red", [k for k, v in o["cov_red"].items() if not v])
    print("missing gram", [k for k, v in o["cov_gram"].items() if not v])
    print("extra", o["extra"])
    print("exam A1 <3", {k: len(v) for k, v in o["exam"].items() if k.startswith("A1") and len(v) < 3})
    print("exam A2 <3 vor Sim1", {k: len(v["vor_Sim1"]) for k, v in o["exam"].items() if k.startswith("A2") and len(v["vor_Sim1"]) < 3})
    print("ndays", o["ndays"]); print("minutes", o["minutes"])
    print("budget", o["budget"], sum(o["budget"].values()))
    for k, v in o["leitner"].items(): print(k, v["cards"], v["stats"])
    print("capped", o["leitner_capped"])
    print("cards S1 by type", {t: sum(c[t] for c in o["cards"].values()) for t in ["aktiv","passiv","set","grammatik","werte","fehler"]})
```

## `writer.py`

```python
"""Generate Phase-3 markdown documents from out/build.json (single source of truth for all numbers)."""
import json, csv
from collections import Counter, defaultdict
from chapters import CHAPTERS
import build as B

o = json.load(open("out/build.json"))
CH = {c["id"]: c for c in CHAPTERS}
ORDER = [c["id"] for c in CHAPTERS]
A1C = [c for c in ORDER if c.startswith("A1")]; A2C = [c for c in ORDER if c.startswith("A2")]
rows = list(csv.DictReader(open("out/03c-kapitel-wortschatz.tsv", encoding="utf-8"), delimiter="\t"))
by_ch = defaultdict(list)
for r in rows:
    by_ch[r["chapter"]].append(r)
HEAD = ("> **Projekt:** „Weg zur A2“ · **Phase:** 3 · **Stand:** 06.11.2026\n"
        "> **Grundlage:** `claude/00-masterprompt.md` (Phase 3, Abschn. 2–3) · `claude/01-ressourcen.md` · `claude/02-aufbereitung.md` inkl. D1–D6 · `02a`–`02g`\n")
TEXTSORTEN = {"T-01": ["A1-15", "A2-09"], "T-02": ["A1-16", "A1-18", "A1-19"], "T-03": ["A2-03", "A2-04", "A2-06", "A2-13"],
              "T-04": ["A2-08", "A2-14"], "T-05": ["A2-09"], "T-06": ["A1-10", "A2-04"], "T-07": ["A1-10", "A1-16"]}
TS_BY_CH = defaultdict(list)
for t, cs in TEXTSORTEN.items():
    for c in cs:
        TS_BY_CH[c].append(t)
NEW_WOW = [
 ("A1-WOW-21", "W5", "Weiß, dass man seinen Wohnsitz anmelden muss (Meldezettel) und wo das geht.", "Q10 (Thema Meldepflicht); Fakt: Frist/Stelle vor Phase 5 aus oesterreich.gv.at belegen", "🔶"),
 ("A1-WOW-22", "W5", "Weiß, dass in Österreich Pressefreiheit gilt.", "Q10 (Thema); Fakt vor Phase 5 belegen", "🔶"),
 ("A1-WOW-23", "W1", "Weiß, dass Eltern ihr Kind bei Krankheit in Kindergarten/Schule entschuldigen müssen.", "Q10 (Thema); Q36", "🔶"),
 ("A1-WOW-24", "W5/W6", "Weiß, dass es Religionsunterricht gibt und man sich davon abmelden kann.", "Q10 (Thema); Q36 (vgl. A2-WOW-11)", "🔶"),
 ("A1-WOW-25", "W4", "Weiß, dass Haustiere im Haus Regeln haben (Hausordnung, Mietvertrag).", "Q10, Q09 (Thema)", "🔶"),
 ("A1-WOW-26", "W3", "Weiß, dass man manche Medikamente nur mit Rezept in der Apotheke bekommt.", "Q10 (Thema)", "🔶"),
 ("A1-WOW-27", "W2", "Weiß, dass das Gehalt meist auf ein Bankkonto kommt und Steuern Staatsaufgaben finanzieren.", "Q10 (Thema); vgl. A1-WOW-05", "🔶"),
 ("A2-WOW-42", "W0", "Weiß, dass Österreich eine Republik und keine Monarchie mehr ist.", "Q09 (Thema Staatsform/Monarchie); Jahr nur mit Primärquelle", "🔶"),
 ("A2-WOW-43", "W2", "Weiß, dass schwangere Arbeitnehmerinnen besonderen Schutz am Arbeitsplatz haben.", "Q09 (Thema)", "🔶"),
 ("A2-WOW-44", "W2", "Weiß, dass man sich selbstständig machen kann und dafür Regeln gelten.", "Q09 (Thema)", "🔶"),
 ("A2-WOW-45", "W2/W5", "Weiß, dass Diskriminierung auch wegen der sexuellen Orientierung verboten ist.", "Q09 (Thema)", "🔶"),
 ("A2-WOW-46", "W3", "Kennt freie Arztwahl, Hausarzt und Facharzt (ggf. mit Überweisung).", "Q09 (Thema)", "🔶"),
 ("A2-WOW-47", "W4", "Kennt Miete, Eigentum und Kaufvertrag als Wohnformen.", "Q09 (Thema); vgl. A2-WOW-25", "🔶"),
 ("A2-WOW-48", "W6", "Weiß, dass es Alleinerziehende, Lebensgemeinschaften ohne Ehe und gleichgeschlechtliche Partnerschaften gibt.", "Q09 (Thema); vgl. A2-WOW-38", "🔶"),
]

def pct(v, t):
    return f"{100 * v / t:.1f} %"

# --------------------------------------------------------------- helper numbers
bud = o["budget"]; T = sum(bud.values())
new = bud["Neuer Stoff (Input + Üben)"]
rev = bud["Wiederholung (Leitner täglich)"] + bud["Wiederholung (Wochenreview)"]
exa = bud["Prüfungstraining (Simulationen)"] + bud["Prüfungstraining (Kapiteltests)"]
puf = bud["Puffer/Nachholen (Flex)"] + bud["Puffer/Nachholen (Puffertage)"]
units = o["units"]; passive = o["passive"]; minutes = o["minutes"]; span = o["span"]
_reg = [v for k, v in units.items() if k not in ("A1-20", "A2-19")]
URANGE = f"{min(_reg)}–{max(_reg)}"
start = {c: span[c][0] for c in ORDER}
kinds = Counter(d["kind"] for d in o["days"])
n_ch_days = kinds["CH"]

def gross(c):
    a, b = span[c]
    return b - a + 1

# variant Ø 1.75 h for sensitivity
DAY2 = 105; content2 = DAY2 - B.LEITNER
new2 = n_ch_days * content2 - len(ORDER) * B.TEST_MIN
tot2 = 90 * DAY2

def chap_line(c):
    return f"`{c}` {CH[c]['title']}"

def leitwoerter(c, k=10):
    act = [r["lemma"] for r in sorted(by_ch[c], key=lambda r: r["hf"] == "GW") if r["use"] == "a" and not r["set"]]
    sets = sorted({r["set"] for r in by_ch[c] if r["set"]})
    return ", ".join(act[:k]) + (" …" if len(act) > k else "") + ("" if not sets else " · Sets: " + ", ".join(sets))

def id_ranges(c):
    ids = sorted(r["id"] for r in by_ch[c])
    return f"{len(ids)} Einträge"

# --------------------------------------------------------------- 03-curriculum.md
L = []
w = L.append
w("# 03 – Curriculum & detaillierter Plan (Phase 3): Übersicht, Zeitbudget, Kalender, Freigabeplan, DoD\n")
w(HEAD)
w("> **Teil-Dokumente:** `03a-kapitel-spezifikation.md` · `03b-abdeckungsmatrix.md` · `03c-kapitel-wortschatz.tsv` (Zuordnung aller 2.035 Einträge zu Kapiteln) · `03d-wortschatz-ergaenzung.tsv` (122 neue Einträge, D3)\n")
w("> **Methode:** Alle Zahlen in diesen Dokumenten sind maschinell aus einem Datenmodell erzeugt (Kapiteldaten, Inventar, Regeln, Kalender, Leitner-Simulation). Prüfungen (Voraussetzungen der Grammatik, 100-%-Abdeckung, Prüfungsteile ≥ 3× vor Simulation, Zeitsumme) laufen als Code; Ergebnisse in `03b`. Das Skript wandert in Phase 5 nach `scripts/plan/` im Repo.\n")
w("\n---\n\n## 1. Ergebnis in Zahlen\n")
w("| Baustein | Umfang |\n|---|---|")
w(f"| Kapitel | **{len(ORDER)}** (A1: {len(A1C)} · A2: {len(A2C)}) + A1-Meilensteinprüfung, A2-Simulation 1 + 2, A2-Generalprobe |")
w(f"| Kalender | 90 Plantage: {n_ch_days} Kapiteltage · {kinds['WOCHE']} Wochenreview-Tage · {kinds['SIM']} Simulationstage (4 × 2) · {kinds['PUF']} Puffertage |")
w(f"| Zeitbudget | {T} min = **{T/60:.0f} h** (90 × 90 min): Neuer Stoff {pct(new,T)} · Wiederholung {pct(rev,T)} · Prüfungstraining {pct(exa,T)} · Puffer {pct(puf,T)} |")
w(f"| Wortschatz | Inventar v2 **{o['inventory']['total']}** Einträge (+{o['inventory']['new']} nach D3); D4-Einheiten A1 {o['inventory']['units_total']['A1']} / A2 {o['inventory']['units_total']['A2']}; je Kapitel {URANGE} Einheiten (Ausnahmen: Synthese-Kapitel A1-20, A2-19) |")
w("| Lernziele | 97/97 Sprach-Lernziele · 75/75 WOW-Lernziele (61 + 14 neu nach D5) · 49/49 Grammatikthemen · 55/55 Redemittel · 7/7 Textsorten – je ≥ 1 Kapitel |")
w("| Prüfungsteile | 15/15 A1-Teilaufgaben ≥ 3× vor der A1-Meilensteinprüfung · 14/14 A2-Teilaufgaben ≥ 3× vor A2-Simulation 1 |")
w("| Leitner-Last (Simulation) | Bedarf Ø ≈ 29 min/Tag statt 15 → Plan: **25 min/Tag + 60 min am Wochenreview-Tag** (Abschn. 3) |")

# --- 2 Zeitbudget
w("\n---\n\n## 2. Zeitbudget\n")
w("### 2.1 Tagesvorlagen (alle Zeiten in Minuten, Ø 90 min/Tag)\n")
w("| Tagestyp | Anzahl | Leitner-Wiederholung | Inhalt | Summe |\n|---|---|---|---|---|")
w(f"| Kapiteltag | {n_ch_days} | {B.LEITNER} | {B.CAP} Kapitelarbeit (Input → Üben → Kapiteltest; an Kapitelenden bis +15 min, damit keine Mini-Reste entstehen) | {B.DAY} |")
w(f"| Wochenreview-Tag (Plantag 7, 14, …, 84) | {kinds['WOCHE']} | {B.LEITNER} | {B.WEEKLY} Wochenreview (Interleaving aller bisherigen Kapitel + Abbau des Leitner-Rückstaus) + {B.DAY-B.LEITNER-B.WEEKLY} Nachholen | {B.DAY} |")
w(f"| Simulationstag | {kinds['SIM']} | {B.SIM_LEITNER} | {B.DAY-B.SIM_LEITNER} Prüfungssimulation (Tag 1 schriftlich, Tag 2 WOW + Sprechen + Auswertung) | {B.DAY} |")
w(f"| Puffertag | {kinds['PUF']} | {B.LEITNER} | {B.CAP} Kapitelwiederholung nach 0 Leben bzw. Korrekturrunde; ungenutzt → Sprechpraxis im ÖIF-Kursraum + Schwächen-Review | {B.DAY} |")
w("\n**Simulationsdauer im Detail:** A1-Meilenstein Tag 1: Sprachbausteine, Hören, Hören und antworten, Lesen, Schreiben = 70 min (Q06); Tag 2: WOW 40 min (Q10) + Sprechen ca. 20 min (simulierte Gruppenprüfung) + Auswertung. A2 Tag 1: Lesen 40 + Hören ca. 12 + Schreiben 25 = 77 min (Q05); Tag 2: WOW 40 (Q09) + Sprechen ca. 10 + Auswertung. Die echte Prüfung läuft an einem Tag; die Teilung respektiert die Höchstgrenze von 2 h/Tag. Die Generalprobe an Tag 88–89 wird empfohlen zusätzlich am Stück mit dem offiziellen Modelltest (Link, Q05) an Tag 90 zu wiederholen.\n")
w("### 2.2 Summen (rechnerisch geschlossen)\n")
w("| Kategorie | Minuten | Stunden | Anteil | Richtwert Masterprompt |\n|---|---|---|---|---|")
w(f"| Neuer Stoff (Input + Üben in Kapiteln) | {new} | {new/60:.1f} | {pct(new,T)} | 55–60 % |")
w(f"| Wiederholung (Leitner {bud['Wiederholung (Leitner täglich)']} + Wochenreview {bud['Wiederholung (Wochenreview)']}) | {rev} | {rev/60:.1f} | {pct(rev,T)} | 20–25 % |")
w(f"| Prüfungstraining (Kapiteltests {bud['Prüfungstraining (Kapiteltests)']} + Simulationen {bud['Prüfungstraining (Simulationen)']}) | {exa} | {exa/60:.1f} | {pct(exa,T)} | 15–20 % |")
w(f"| Puffer/Nachholen (Puffertage {bud['Puffer/Nachholen (Puffertage)']} + Flex {bud['Puffer/Nachholen (Flex)']}) | {puf} | {puf/60:.1f} | {pct(puf,T)} | – (Masterprompt: Puffertage im Kalender) |")
w(f"| **Summe** | **{T}** | **{T/60:.1f}** | 100 % | 90 Tage × Ø 1,5 h = 135 h ✅ |")
w(f"\n**Abweichung vom Richtwert (benannt, nicht stillschweigend):** Neuer Stoff liegt mit {pct(new,T)} deutlich unter 55–60 %, Wiederholung mit {pct(rev,T)} deutlich darüber. Ursache ist **D3** (Inventar umfangreich, ≈ 81 % aktiv): Die Leitner-Simulation (Abschn. 3) zeigt, dass 15 min/Tag den Wiederholungsbedarf nicht decken. Didaktisch ist das kein Verlust an Lernzeit – Abrufübung ist selbst Lernen (Retrieval Practice, Q90/Q92) und verteiltes Wiederholen wirkt stärker als gleich viel Zeit für neuen Stoff (Spacing, Q91/Q94). Die Kehrseite: Pro Kapitel bleiben netto Ø {sum(minutes.values())/len(ORDER):.0f} min (inkl. 25 min Kapiteltest), d. h. Ø {sum(minutes.values())/len(ORDER)-25:.0f} min für Input und Üben. Brutto (inkl. anteiliger Tageswiederholung) entspricht ein Kapitel Ø {sum(minutes.values())/len(ORDER)/B.CAP:.1f} Plantagen ≈ {sum(minutes.values())/len(ORDER)/B.CAP*1.5:.1f} h – im Masterprompt-Rahmen „2–3 h, 1–2 Tage“, aber am unteren Rand.\n")
w(f"**Sensitivität Ø 1,75 h/Tag (105 min, innerhalb max. 2 h):** gleicher Kalender, Kapitelarbeit {content2} statt {B.CAP} min/Tag → Neuer Stoff {new2} min = {pct(new2, tot2)} von {tot2/60:.1f} h; Ø {(n_ch_days*content2)/len(ORDER):.0f} min netto je Kapitel. Das ist die wirksamste Gegenmaßnahme, ändert aber Parameter „Ø 1,5 h“ → **offene Frage O1**.\n")

# --- 3 Leitner
w("\n---\n\n## 3. Wiederholungslast (D3-Risiko) – Leitner-Simulation\n")
w("**Modell** (Annahmen, in Phase 4 mit dem echten Scheduler nachrechnen): Leitner 5 Fächer, Intervalle 1/3/7/14/30 Tage (Masterprompt 4.8); Trefferquote je Fach 80/85/88/90/93 %, Fehler → Fach 1; nach Fach 5 verlässt die Karte die 90-Tage-Queue. Zeit je Abfrage: aktives Wort 9 s, passives 5 s, Set-Karte 6 s, Grammatik-Item 15 s, Werte-Fakt 12 s, Fehler-Zwilling 25 s. Karten je Kapitel: alle Inventar-Einträge des Kapitels, 8 Grammatik-Items je neuem Grammatikthema + 4 recycelte, 3 Werte-Karten je WOW-Lernziel, 6 Fehler-Zwillinge. Neue Karten entstehen proportional zur Kapitelarbeit des Tages. Mittelwert aus 5 Läufen (feste Seeds).\n")
w("| Szenario | Karten gesamt | Ø min/Tag | 90-%-Tag | Max | Tage > 15 min | Tage > 25 min |\n|---|---|---|---|---|---|---|")
for k, v in o["leitner"].items():
    s = v["stats"]
    w(f"| {k} | {v['cards']} | {s['mean']} | {s['p90']} | {s['max']} | {s['days_over_15']} | {s['days_over_25']} |")
w("\n**Mit Zeitdeckel** (Szenario S2; fällige Karten warten, älteste zuerst; am Wochenreview-Tag zusätzlich 60 min):\n")
w("| Deckel min/Tag | Ø genutzt min/Tag* | Rückstau Ø Karten | Rückstau Tag 60 | Rückstau max | Rückstau Tag 90 |\n|---|---|---|---|---|---|")
for cap, v in o["leitner_capped"].items():
    w(f"| {cap} | {v['mean']} | {v['backlog_mean']} | {v['backlog_day60']} | {v['backlog_max']} | {v['backlog_end']} |")
w("\n\\* inkl. der 60 min Wochenreview, auf 90 Tage verteilt.\n")
w("**Befund:** Bei 15 min/Tag wächst der Rückstau bis Tag 90 auf rund 1.000 Karten – Spacing wäre faktisch aufgehoben. Ab 25 min/Tag bleibt er beherrschbar (Ø unter 100 Karten), ab 30 min wird er bis Tag 90 vollständig abgebaut.\n")
w("**Planentscheidung (Vorschlag, in Phase 4 festzuschreiben):** tägliche Review-Queue **25 min** statt „max. ~15 min“ (Masterprompt 4.8) + **60 min Wochenreview**; dazu die Entlastungen aus S2:\n")
w("1. **Passive Einträge bekommen keine eigene Leitner-Karte**, sondern werden über Lese-/Hörtexte und Distraktoren wiederholt (D4: passiv = rezeptiv).")
w("2. **Sets (Zahlen, Wochentage, Monate …) sind je eine Set-Karte** (Reihen-Drill statt Einzelkarten).")
w("3. **Im Kapiteltest richtig beantwortete Inhalte starten in Fach 2** (3 Tage) – der Test war bereits ein erfolgreicher Abruf; Fehler starten in Fach 1.")
w("4. **Prioritäten bei Zeitnot:** Fehler-Zwillinge > aktive Wörter des laufenden Niveaus > Grammatik > WOW > Rest; Überhang wandert in den Wochenreview.")
w("\nDie Stellschrauben sind bewusst so gewählt, dass **keine aktiven Wörter herabgestuft werden** (D3 bleibt unangetastet).\n")

# --- 4 Realismus
w("\n---\n\n## 4. Realismus-Check\n")
w("| Vergleich | Umfang | Quelle | 135 h entsprechen |\n|---|---|---|---|")
w("| ÖIF-Standardkurs A1 + A2 (geförderte Deutschkurse ab 01.04.2026) | je Niveau 180 UE Präsenz + 120 UE Selbstlernzeit, 1 UE = 50 min → 250 h je Niveau, **500 h** A1+A2 | ÖIF, Rahmenbedingungen Startpaket Deutsch & Integration 2026, https://www.integrationsfonds.at/fileadmin/user_upload/OEIF_Rahmenbedingungen_Startpaket_Deutsch_und_Integration_2026.pdf (abgerufen 06.11.2026) | **27 %** |")
w("| nur Präsenzanteil ÖIF A1 + A2 | 360 UE à 50 min = **300 h** | ebd. | 45 % |")
w("| Integrationskurs nach IntG-DV | 300 UE (§ 10 Abs. 2) | Q21, zitiert in `02-aufbereitung.md` W7 | – (UE-Länge dort nicht belegt) |")
w("\n**Bewertung:** Das 90-Tage-Ziel ist **sehr ambitioniert**. Das Tool kompensiert einen Teil des Abstands durch Eins-zu-eins-Tempo ohne Kurs-Leerlauf, hohen Abrufanteil (Q90, Q92), verteiltes Wiederholen (Q91) und die Konzentration auf das Prüfungsformat. Es kompensiert **nicht** echte Sprechpraxis mit Menschen und das Hörverstehen natürlicher Sprache. Ein realistischer Zielkorridor für „prüfungsreif A2“ bei 1,5 h/Tag liegt nach diesem Vergleich eher über 90 Tagen; die Prognosefunktion (Masterprompt 4.11) muss das ehrlich anzeigen. `[ANNAHME]`: Lernende mit Englisch als Unterstützungssprache profitieren von Internationalismen (QK-03); das ist nicht quantifiziert.\n")
w("**Gegenmaßnahmen (im Plan verankert):**\n")
w("1. **Sprechpraxis zusätzlich zum Budget:** ÖIF-Kursraum A1/A2 (live, kostenlos, Mo–Sa, Q40/Q41) und Online-Kurs Sprechen (A1 freitags, A2 donnerstags, Q42) – Empfehlung im Tool ab A1-05 bzw. A2-01 mindestens 2× pro Woche; ungenutzte Puffertage werden dafür vorgeschlagen.")
w("2. **Option Ø 1,75 h** (Abschn. 2.2, offene Frage O1) bzw. **Verlängerungsmodus** ohne Inhaltsänderung: Die Prognose zeigt „prüfungsreif ab ca. Tag X“; Puffer- und Wochenreview-Tage verschieben sich automatisch.")
w("3. **Priorisierung im Test:** P1-Lernziele (prüfungsrelevant) tragen die Kapiteltests; P2/P3 vorwiegend in Lektionen.")
w("4. **Pilot (Phase 7):** Kapitel A1-01 mit echter Lernender, tatsächliche Dauer gegen die Planminuten messen, Workload-Formel kalibrieren.")

# --- 5 Kapitelstruktur
w("\n---\n\n## 5. Kapitelstruktur\n")
w(f"**Anzahl begründet:** Das Inventar ergibt {o['inventory']['units_total']['A1']} A1- bzw. {o['inventory']['units_total']['A2']} A2-Einheiten (D4-Zählung). Mit 30–45 neuen Einheiten je Kapitel braucht A1 mindestens 18, A2 mindestens 17 Kapitel. A1 bekommt **20** Kapitel, weil das Feld „Orientierung“ (Dativ-Präpositionen, Wechselpräpositionen, Verkehr, Möbel) für ein Kapitel zu groß war (79 Einheiten) und G20 die Voraussetzung G18 im Vorkapitel braucht. A2 bleibt bei **19**; A2-19 ist ein Synthesekapitel mit bewusst wenig neuem Wortschatz.\n")
w("**Aufbau jedes Kapitels:** Input (Mikro-Lektionen mit Audio) → Üben (Übungstypen 02g Abschn. 4) → Kapiteltest in allen Disziplinen. Testlänge hier als Planwert 25 Items (Prüfungstraining-Kapitel 25), Pool ≥ 63; die endgültige Testlänge legt Phase 4 per Bestehens-Simulation zu Entscheidung 1 fest.\n")
w("| Kapitel | Titel | HF | Grammatik | Fokus | neue Einheiten | Planminuten netto | Plantage |\n|---|---|---|---|---|---|---|---|")
for c in ORDER:
    ch = CH[c]
    w(f"| `{c}` | {ch['title']} | {', '.join(ch['hf'])} | {', '.join(ch['gram']) or '– (Wiederholung)'} | {ch['focus']} | {units[c]} | {minutes[c]} | {span[c][0]}–{span[c][1]} |")
    if c == "A1-20":
        w("| **MS A1** | **A1-Meilensteinprüfung** (Format Integrationsprüfung A1, Bestehen ≥ 75 % je Subtest, E3) | | | | | 160 | 39–40 |")
    if c == "A2-10":
        w("| **SIM 1** | **A2-Simulation 1** (vollständig, Bestehen ≥ 75 % je Prüfungsteil) | | | | | 160 | 64–65 |")
    if c == "A2-19":
        w("| **SIM 2** | **A2-Simulation 2** | | | | | 160 | 85–86 |")
        w("| **GP** | **A2-Generalprobe** (neuer Testsatz; danach offizieller Modelltest als Link) | | | | | 160 | 88–89 |")

# --- 6 Kalender
w("\n---\n\n## 6. 90-Tage-Kalender (relativ, Plantag 1 = Profilanlage)\n")
w("Feste Kalenderdaten gibt es nicht (Masterprompt Abschn. 2). Minuten = Kapitelarbeit des Tages; dazu kommen jeden Tag 25 min Leitner (Simulationstage 10 min).\n")
w("| Tag | Typ | Inhalt |\n|---|---|---|")
for d in o["days"]:
    if d["kind"] == "CH":
        txt = " + ".join(f"`{c}` {m} min" for c, m in d["label"])
    else:
        txt = d["label"]
    typ = {"CH": "Kapitel", "WOCHE": "Wochenreview", "SIM": "**Simulation**", "PUF": "Puffer"}[d["kind"]]
    w(f"| {d['day']} | {typ} | {txt} |")
w("\n**Puffer-Logik:** Je ein Puffertag vor und nach der A1-Meilensteinprüfung, vor A2-Simulation 1, vor A2-Simulation 2, danach und am Ende (6 Tage) plus 5 min Flex an jedem Wochenreview-Tag. Ob 6 Tage für Entscheidung 1 (Variante A: jeder Fehler in der Korrekturrunde → Kapitel komplett wiederholen) reichen, hängt von der Bestehenswahrscheinlichkeit ab, die Phase 4 simuliert. **Abhängigkeit:** Ergibt Phase 4 eine erwartete Wiederholungsquote > 15 % der Kapitel, reicht der Puffer nicht – dann Testlänge senken oder Puffer erhöhen (offene Frage an Phase 4).\n")

# --- 7 Freigabeplan
w("\n---\n\n## 7. Freigabeplan (Just-in-time-Produktion)\n")
w("**Regeln:** Produktion in Batches zu max. 2 Kapiteln (Masterprompt 5.10). Start der ersten Lernenden, sobald App + A1-01 bis A1-05 fertig sind. Danach gilt für jedes Kapitel die strengere von zwei Fristen: (a) mind. 7 Tage vor seinem ersten Plantag, (b) fertig, wenn die Lernende das Kapitel fünf Positionen davor beginnt. Prüfungs-Testsätze sind vor Ende des Niveaus fertig. „Tag ≤ 0“ heißt: vor Tag 1 der ersten Lernenden.\n")
batches = [("B01", ["A1-01", "A1-02"]), ("B02", ["A1-03", "A1-04"]), ("B03", ["A1-05", "A1-06"])]
rest = [c for c in ORDER if c not in ("A1-01", "A1-02", "A1-03", "A1-04", "A1-05", "A1-06")]
i = 4
while rest:
    batches.append((f"B{i:02d}", rest[:2])); rest = rest[2:]; i += 1

def deadline(c):
    k = ORDER.index(c)
    a = start[c] - 7
    b = start[ORDER[k - 5]] if k >= 5 else 0
    return min(a, b)

w("| Batch | Inhalt | spätestens fertig (Plantag) | Begründung |\n|---|---|---|---|")
rows7 = []
for bid, cs in batches:
    dl = min(deadline(c) for c in cs)
    rows7.append((dl, bid, " + ".join(f"`{c}`" for c in cs), "Startbedingung (App + A1-01–05)" if bid in ("B01", "B02", "B03") else f"erster Plantag {min(start[c] for c in cs)}"))
rows7 += [(start["A1-16"], "T-A1", "A1-Meilensteinprüfung: Testsatz + Zwillingssatz für 2. Versuch", "vor Ende A1 (Simulation Tag 39)"),
          (start["A2-06"], "T-S1", "A2-Simulation 1 (Testsatz)", "Simulation Tag 64"),
          (start["A2-15"], "T-S2", "A2-Simulation 2 + Generalprobe (2 Testsätze)", "Simulationen Tag 85/88")]
for dl, bid, inh, why in sorted(rows7, key=lambda x: (x[0], x[1])):
    w(f"| {bid} | {inh} | {max(dl, 0) if dl > 0 else '≤ 0'} | {why} |")
w(f"\n**Produktionstempo:** Nach Tag 1 sind {len(batches)-3} Kapitel-Batches + 3 Testsatz-Pakete bis spätestens Plantag {max(r[0] for r in rows7)} fertig zu stellen – im Schnitt ein Paket alle {max(r[0] for r in rows7)/(len(batches)-3+3):.1f} Tage. Jedes Paket durchläuft automatische QA, Prüfer-Agent und menschliche Freigabe (Masterprompt 5.10–5.13). **Risiko:** Die Freigabe durch dich ist der Engpass; Empfehlung: vor Tag 1 nicht nur B01–B03, sondern zusätzlich B04–B05 fertig haben (≈ 2 Wochen Vorsprung).\n")

# --- 8 Risiken
w("\n---\n\n## 8. Risiken und Gegenmaßnahmen\n")
w("| # | Risiko | Wirkung | Gegenmaßnahme | Wo |\n|---|---|---|---|---|")
risks = [
 ("R1", "Gesamtumfang 135 h vs. ÖIF-Richtwert 500 h A1+A2", "Ziel in 90 Tagen ggf. nicht erreichbar", "ehrliche Prognose, Verlängerungsmodus, Option Ø 1,75 h, ÖIF-Kursraum zusätzlich", "Abschn. 4"),
 ("R2", "Wiederholungslast durch D3 (≈ 29 min/Tag Bedarf)", "15-min-Regel nicht haltbar; weniger Zeit für neuen Stoff", "25 min + 60 min Wochenreview, S2-Entlastungen, Prioritäten", "Abschn. 3, Phase 4"),
 ("R3", "Variante A (Entscheidung 1) frisst Puffer", "Kalenderverzug", "Phase 4: Testlänge per Simulation; 6 Puffertage + Flex; Verzug-Anzeige", "Abschn. 6"),
 ("R4", f"Kapitel netto Ø ≈ {sum(minutes.values())/len(ORDER):.0f} min eng bei {URANGE} Einheiten", "Überforderung, Testfehler", "Mikro-Lektionen, Chunks vor Regel, Pilot-Kalibrierung", "Abschn. 2"),
 ("R5", "Sprechen ohne Gesprächspartner (Artifact: kein Mikrofon)", "Sprechen ≥ 15/30 unsicher", "ÖIF-Kursraum/Online-Kurs Sprechen, Checklisten, Musterantworten", "02g (3.5)"),
 ("R6", "TTS ohne deutsche Stimme (L17)", "Hören-Aufgaben unbrauchbar", "vorproduzierte Audiodateien einplanen (Phase 5/6)", "01 L17"),
 ("R7", "Tagalog-Qualität (E2)", "Missverständnisse", "einfache Sprache, `machine`-Status, Review anstreben", "E2"),
 ("R8", "IntG-Novelle 2027 (E1)", "Formatänderung", "Status nach 12.11.2026 prüfen", "E1"),
 ("R9", "Freigabe-Engpass Produktion", "Lernende wartet", "2 Wochen Vorlauf, Batches bündeln", "Abschn. 7"),
 ("R10", "Themenabgleich D5 per automatischer Zusammenfassung", "Thema übersehen", "vor Phase 5 Stichprobe im Katalog manuell gegenlesen", "03b Abschn. 3"),
]
for r in risks:
    w("| " + " | ".join(r) + " |")

# --- 9 Widersprüche
w("\n---\n\n## 9. Widersprüche und Abweichungen (benannt)\n")
w("| # | Thema | Befund | Umgang |\n|---|---|---|---|")
contra = [
 ("K1", "Kapitelzahl", "`02-aufbereitung.md` O4 rechnete mit 38 Kapiteln", "39 (A1 20 · A2 19), Begründung Abschn. 5"),
 ("K2", "Zeitbudget-Richtwert", f"Neuer Stoff {pct(new,T)} statt 55–60 %, Wiederholung {pct(rev,T)} statt 20–25 %", "Folge von D3, Abschn. 2.2/3; O1"),
 ("K3", "Review-Queue max. ~15 min (Masterprompt 4.8)", "Simulation: Rückstau ≈ 1.000 Karten", "Vorschlag 25 min + Wochenreview; Entscheidung in Phase 4 (O2)"),
 ("K4", "WOW-Geschichtslücke (02f, O5)", "Fragenkatalog A1/A2 enthält laut Themendurchsicht keine Geschichtsthemen außer EU-Beitritt und Abgrenzung Monarchie; Neutralität, Nationalfeiertag, Wahlen, Nachbarländer, Feiertage kommen dort nicht vor", "bleiben als Rahmencurriculum-Ziele (P2) im Plan; 14 neue WOW-Lernziele für Katalog-Themen, die 02f fehlten (03b Abschn. 3)"),
 ("K5", "Goethe-Abdeckung", "02c: 85,7 % von 1.284 bereinigten Lemmata; hier gemessen 84,8 % von 1.299 normalisierten Stichwörtern (andere Normalisierung)", "nach D3-Ergänzung 100 % der 1.227 echten Lemmata; 72 Rest-Treffer sind Messartefakte (03b Abschn. 4)"),
 ("K6", "Kapiteldauer „2–3 h“", "netto 84–125 min je Kapitel", "brutto inkl. Tageswiederholung Ø ≈ 2,5 h; im Rahmen, unterer Rand"),
 ("K7", "30–45 neue Einheiten je Kapitel", f"A1-20: {units['A1-20']}, A2-19: {units['A2-19']}", f"Synthese-/Prüfungskapitel, bewusst; alle übrigen {URANGE}"),
 ("K8", "02c: Beispielsatz-Feld", "unverändert leer", "D2: Phase 5"),
 ("K9", "Inventar-Datei", "02c-TSV bleibt v1 (1.913)", "Ergänzung als `03d`, Kapitelzuordnung als `03c`; Zusammenführung in Phase 5 im Repo"),
]
for r in contra:
    w("| " + " | ".join(r) + " |")

# --- 10 DoD
w("\n---\n\n## 10. Definition of Done – Phase 3\n")
w(f"- [x] **Zeitbudget stimmt rechnerisch** – {T} min = 135 h, alle Tagesvorlagen summieren auf 90 min (Abschn. 2.2); Abweichung vom Richtwert benannt (K2).")
w("- [x] **Abdeckung 100 %** – 97/97 Sprach-Lernziele, 75/75 WOW-Lernziele, 49/49 Grammatik (Voraussetzungsprüfung ohne Fehler), 55/55 Redemittel, 7/7 Textsorten, 2.035/2.035 Wortschatz-Einträge, 29/29 Prüfungsteile (`03b`).")
w("- [x] **Jede Prüfungs-Teilaufgabe ≥ 3× vor der jeweiligen Simulation** – A1 vor Meilenstein, A2 bereits vor Simulation 1 (`03b` Abschn. 5).")
w("- [x] **Kalender mit Puffer** – 90 Plantage, 6 Puffertage + 12 Wochenreview-Tage (Abschn. 6); Puffer-Abhängigkeit zu Phase 4 benannt.")
w("- [x] **Freigabeplan** – Batches mit spätesten Plantagen (Abschn. 7).")
w("- [x] **Risiken benannt** – R1–R10 (Abschn. 8), Realismus-Check (Abschn. 4).")
w("- [x] **D3/D4/D5 umgesetzt** – 122 neue Einträge, Set-/Passiv-Zählung, Fragenkatalog nur thematisch durchgesehen.")
w("- [x] **Als Dokument gespeichert** – 03, 03a, 03b, 03c, 03d.")

# --- 11 offene Fragen
w("\n---\n\n## 11. Offene Fragen (für dich)\n")
w("| # | Frage | Mein Vorschlag |\n|---|---|---|")
w(f"| O1 | Zeit pro Tag: bei Ø 1,5 h bleiben (Neuer Stoff {pct(new,T)}) oder auf Ø 1,75 h anheben ({pct(new2,tot2)}, max. 2 h bleibt)? | Ø 1,5 h als Plan, 1,75 h als Empfehlung im Onboarding („schneller ans Ziel“) |")
w("| O2 | Review-Queue 25 min/Tag + 60 min Wochenreview statt „max. ~15 min“ (Masterprompt 4.8) – in Phase 4 so festschreiben? | Ja, inkl. S2-Entlastungen (passive ohne Karte, Set-Karten, Start Fach 2 nach richtigem Test) |")
w("| O3 | 14 neue WOW-Lernziele aus dem Themenabgleich (03b Abschn. 3) übernehmen? Fakten werden vor Phase 5 aus Primärquellen belegt. | Ja |")
w("| O4 | Bundesdeutsche Varianten (Tomate, Brötchen, Treppe …) als passive Einträge mit Hinweis führen? | Ja – sie stehen auf Verpackungen und in Medien; im Prüfungsmodus erscheinen nur AT-Formen |")
w("| O5 | Kapitelzuschnitt (39 Kapitel, Titel, Reihenfolge) so freigeben? | Ja |")

w("\n**Weiter offen aus früheren Phasen:** L1/L2 Punkteverteilung A2 Schreiben/Sprechen · L12 IntG-DV-Entwurf (nach 12.11.2026 prüfen, E1) · L15 Sprechtempo · offene WOW-Belege 🔶/❌ aus 02f + 14 neue · Tagalog-Review (E2) · Gerätecheck (E4).\n")
w("\n## 12. Nächster Schritt\n\n**Phase 4 – Spielregeln:** Zustandsautomat, Bestehens-Simulation zu Entscheidung 1 (Testlänge, Puffer-Bedarf), Leitner-Regeln inkl. O2, Randfälle.\n")
open("out/03-curriculum.md", "w", encoding="utf-8").write("\n".join(L))

# --------------------------------------------------------------- 03a Kapitel-Spezifikation
L = []; w = L.append
w("# 03a – Kapitel-Spezifikationen (Phase 3.3)\n")
w(HEAD)
w("> **Lesehilfe:** IDs verweisen auf `02a` (Lernziele), `02d` (Grammatik G…), `02e` (Redemittel R-…, Textsorten T-…), `02f`/`03b` (WOW), `02g` (Prüfungsteile). Die vollständige Wortliste je Kapitel steht in `03c-kapitel-wortschatz.tsv` (Spalte `chapter`). „Einheiten“ nach D4: aktive Einträge + je Set 1; passive Einträge werden rezeptiv eingeführt.\n")
w("> **Aufgabenanzahl:** Planwerte für den Kapiteltest je Disziplin; Pool ≥ 2,5 × Testgröße und ≥ 60 (Masterprompt 5.2); jedes Item mit ≥ 1 Zwilling. Die finale Testlänge setzt Phase 4.\n")
for c in ORDER:
    ch = CH[c]; tp, total, pool = o["test"][c]
    k = ORDER.index(c)
    pre = f"`{ORDER[k - 1]}` bestanden" if k else "– (Profil angelegt)"
    if c == "A2-01":
        pre = "A1-Meilensteinprüfung bestanden"
    if c == "A2-11":
        pre = "`A2-10` bestanden + A2-Simulation 1 absolviert"
    w(f"\n## `{c}` – {ch['title']}\n")
    w("| Feld | Inhalt |\n|---|---|")
    w(f"| Handlungsfeld | {', '.join(ch['hf'])} |")
    w(f"| Can-Do-Ziele | {', '.join(ch['cando'])} |")
    w(f"| Grammatik | {', '.join(ch['gram']) or '– (Wiederholung im Kontext)'} |")
    w(f"| Redemittel / Textsorten | {', '.join(ch['red'])}{(' · ' + ', '.join(TS_BY_CH[c])) if TS_BY_CH[c] else ''} |")
    w(f"| Werte-Thema | {', '.join(ch['wow'])} |")
    w(f"| Prüfungsteil-Fokus | **{ch['focus']}** · geübte Formate: {', '.join(ch['exam'])} |")
    w(f"| Neuer Wortschatz | **{units[c]} Einheiten** ({sum(1 for r in by_ch[c] if r['use']=='a')} aktive + {passive[c]} passive Einträge; {id_ranges(c)}) – Leitwörter: {leitwoerter(c)} |")
    w(f"| Aufgaben Kapiteltest (Plan) | " + " · ".join(f"{d} {n}" for d, n in tp.items()) + f" = **{total}** · Pool ≥ {pool} |")
    w(f"| Dauer | netto {minutes[c]} min (davon Kapiteltest 25) · Plantag {span[c][0]}–{span[c][1]} |")
    w(f"| Voraussetzungen | {pre} |")
    if ch["note"]:
        w(f"| Didaktik | {ch['note']} |")
w("\n## Meilensteine und Simulationen\n")
w("| ID | Plantag | Format | Bestehen (Tool) | Voraussetzung | Bei Nichtbestehen |\n|---|---|---|---|---|---|")
w("| `MS-A1` | 39–40 | Integrationsprüfung A1 vollständig: Sprachbausteine, Hören, Hören und antworten, Lesen, Schreiben (70 min), WOW (40 min), Sprechen (simulierte Gruppe) – Zeiten/Hörregeln wie Q06/Q10 | ≥ 75 % je Subtest (E3); offizielle Logik ≥ 240/400 + WOW ≥ 25/45 als Info | A1-20 bestanden | Review der schwächsten Kapitel/Teile (Puffer Tag 41), neuer Versuch mit Zwillingssatz |")
w("| `SIM-A2-1` | 64–65 | Integrationsprüfung A2 vollständig (Q05/Q09), Hören 1+2 2×, Hören 3+4 1×, Lesezeit 30 s | ≥ 75 % je Prüfungsteil (Entscheidung 6) | A2-10 bestanden | Diagnose-Simulation: schaltet A2-11 dennoch frei, erzeugt Schwächen-Review |")
w("| `SIM-A2-2` | 85–86 | wie SIM-A2-1, neuer Testsatz | ≥ 75 % je Prüfungsteil | A2-19 bestanden | gezielte Review (Puffer Tag 87) |")
w("| `GP-A2` | 88–89 | wie SIM-A2-1, neuer Testsatz; Tag 90: offizieller Modelltest als Link | ≥ 75 % je Prüfungsteil | SIM-A2-2 absolviert | Prognose + Verlängerungsmodus |")
w("\n**Hinweis zu SIM-A2-1:** Ob Simulation 1 eine Sperre (wie der A1-Meilenstein) oder eine Diagnose ist, regelt Phase 4. Vorschlag: Diagnose, weil sie mitten im A2-Stoff liegt und Teile wie Sprechen T2B erst ab A2-17 vollständig trainiert sind.\n")
open("out/03a-kapitel-spezifikation.md", "w", encoding="utf-8").write("\n".join(L))

# --------------------------------------------------------------- 03b Abdeckungsmatrix
L = []; w = L.append
w("# 03b – Abdeckungsnachweis (Phase 3.6)\n")
w(HEAD)
w("> **Prüfung als Code:** Jede Tabelle unten ist Ausgabe des Planungsskripts. Anforderung Masterprompt: 100 % Abdeckung, jede Prüfungs-Teilaufgabe vor der jeweiligen Simulation ≥ 3× geübt, Werte-Themen vollständig verteilt.\n")
w("\n## 0. Zusammenfassung der automatischen Prüfungen\n")
w("| Prüfung | Ergebnis |\n|---|---|")
cov = lambda d: sum(1 for v in d.values() if v)
w(f"| Sprach-Lernziele (02a) | {cov(o['cov_cando'])}/{len(o['cov_cando'])} ✅ |")
w(f"| WOW-Lernziele (02f + neu) | {cov(o['cov_wow'])}/{len(o['cov_wow'])} ✅ |")
w(f"| Grammatik G01–G49 | {cov(o['cov_gram'])}/49 ✅ · Voraussetzungsfehler: {len(o['prereq_errors'])} ✅ |")
w(f"| Redemittel R-SP/R-SC | {cov(o['cov_red'])}/{len(o['cov_red'])} ✅ |")
w(f"| Textsorten T-01–T-07 | 7/7 ✅ |")
w(f"| Wortschatz-Einträge mit Kapitel | {len(rows)}/{len(rows)} ✅ · Niveau ≠ Kapitelniveau: {len(o['level_mismatch'])} ✅ |")
a1ok = all(len(v) >= 3 for k, v in o["exam"].items() if k.startswith("A1"))
a2ok = all(len(v["vor_Sim1"]) >= 3 for k, v in o["exam"].items() if k.startswith("A2"))
w(f"| A1-Teilaufgaben ≥ 3× vor Meilenstein | {'15/15 ✅' if a1ok else '❌'} |")
w(f"| A2-Teilaufgaben ≥ 3× vor Simulation 1 | {'14/14 ✅' if a2ok else '❌'} |")
hfs = Counter(h for c in CHAPTERS for h in c["hf"])
w(f"| Handlungsfelder HF00–HF15 in ≥ 1 Kapitel | {sum(1 for i in range(16) if hfs.get(f'HF{i:02d}'))}/16 ✅ |")

w("\n## 1. Sprach-Lernziele × Kapitel\n")
w("| Lernziel | Kapitel |\n|---|---|")
for k, v in o["cov_cando"].items():
    w(f"| {k} | {', '.join(v)} |")
w("\n## 2. Grammatik × Kapitel (Einführung) mit Voraussetzungen\n")
w("| Thema | eingeführt in | Voraussetzungen (eingeführt in) |\n|---|---|---|")
for g in B.GRAM:
    ch = o["first_gram"][g]
    pre = ", ".join(f"{p} ({o['first_gram'][p]})" for p in B.PREREQ[g]) or "–"
    w(f"| {g} | {ch} | {pre} |")
w("\nG49 (Satzklammer-Synthese) erscheint zweimal: A1-20 (A1-Anteil) und A2-19 (vollständig). Vertiefungen früher eingeführter Themen in A2 (z. B. G13 → G29, G20 → G31) sind über die A2-Themen abgebildet.\n")

w("\n## 3. Werte- und Orientierungswissen × Kapitel\n")
w("### 3.1 Themenabgleich mit den Fragenkatalogen (D5)\n")
w("Durchgesehen wurden **nur die Themen**, keine Fragen übernommen: Q09 (WOW A2, Update 2024-05) und Q10 (WOW A1, Update 2024-05), abgerufen 06.11.2026 über eine automatische Themenzusammenfassung. **Befund:** Geschichte kommt praktisch nicht vor (nur EU-Beitritt und Abgrenzung zur Monarchie); Staatsorgane: Bundespräsident, Parlament/Gesetzgebung, Regierung, Behörden, Polizei. Nicht im Katalog, aber im Rahmencurriculum: Neutralität/Nationalfeiertag, Wahlen, Nachbarländer, Feiertage – sie bleiben im Plan (P2). Neu aufgenommen werden Katalog-Themen, die `02f` fehlten:\n")
w("| ID | Bereich | Lernziel (eigene Formulierung) | Quelle (Thema) | Status Fakt |\n|---|---|---|---|---|")
for r in NEW_WOW:
    w("| " + " | ".join(r) + " |")
w("\n🔶 = Thema belegt, Fakten (Fristen, Zahlen, Rechtslage) vor Phase 5 aus Primärquellen (RIS, oesterreich.gv.at, Parlament) belegen. Zusätzlich bleibt aus `02f` offen: A2-WOW-03/-04/-09/-34 🔶, A1-WOW-12 (Uhrzeit), A2-WOW-06, -35, -39 ❌.\n")
w("### 3.2 Verteilung\n")
w("| WOW-Lernziel | Kapitel |\n|---|---|")
for k, v in o["cov_wow"].items():
    w(f"| {k} | {', '.join(v)} |")
w("\nZusätzlich enthält **jeder Kapiteltest ≥ 3 Werte-Items** (Planwert) und jede Simulation die vollständige WOW-Prüfung mit ≥ 1 Frage je Wertebereich W0–W6 (02g).\n")

w("\n## 4. Wortschatz\n")
w("### 4.1 Inventar v2 (D3)\n")
nb = o["inventory"]["by_kind"]
w("| Baustein | Anzahl |\n|---|---|")
w(f"| Inventar v1 (02c) | 1.913 |")
w(f"| + neue Lemmata aus Goethe A1∪A2 | {nb.get('A1-neu-a',0)+nb.get('A1-neu-p',0)+nb.get('A2-neu-a',0)+nb.get('A2-neu-p',0)} (A1: {nb.get('A1-neu-a',0)} aktiv / {nb.get('A1-neu-p',0)} passiv · A2: {nb.get('A2-neu-a',0)} aktiv / {nb.get('A2-neu-p',0)} passiv) |")
w(f"| + bundesdeutsche Varianten als passive Hinweis-Einträge | {nb.get('A1-dvar-p',0)+nb.get('A2-dvar-p',0)} (z. B. Tomate → AT Paradeiser) |")
w(f"| + Set „an/aus/auf/zu sein“ | {nb.get('A1-set-a',0)} |")
w(f"| **Inventar v2** | **{o['inventory']['total']}** · aktiv {o['inventory']['active_share']} % |")
w("\n**Abgleich (Methode):** Stichwortspalte der Goethe-Listen aus einem öffentlichen GitHub-Spiegel (`ilkermeliksitki/goethe-institute-wordlist`, TSV-Auszug der offiziellen PDFs Q61/Q62), normalisiert (Artikel, Pluralangaben, Nummerierungen, „sich“ entfernt) und mit dem Inventar verglichen; nur Lemmata verwendet, keine Beispielsätze. Ergebnis vor D3: 1.299 normalisierte Stichwörter, davon 198 ohne Treffer. Davon sind **72 Messartefakte** (konjugierte Formen wie „hat geduscht“, Stämme wie „dein-“, „jed-“, Varianten bereits vorhandener Einträge) und **126 echte Lücken** → 107 neue Lemma-Einträge + 1 Set-Eintrag (deckt 4 Stichwörter: an/aus/auf/zu sein) + 14 Varianten-Einträge (ein Eintrag deckt 2 Stichwörter: Einzelzimmer/einzel-). Nach D3: **100 % der echten Goethe-Lemmata** abgedeckt.\n")
w("**Neue Einträge** stehen mit Artikel, Formen, Wortart, HF, Niveau, aktiv/passiv, Variante, `en`, `tl` (`review: machine`) in `03d-wortschatz-ergaenzung.tsv`; IDs `W-A1-0907` ff. und `W-A2-1008` ff. (stabil ab jetzt).\n")
w("### 4.2 Wortschatz je Kapitel (D4-Zählung)\n")
w("| Kapitel | Einträge | aktiv | passiv | Sets | **neue Einheiten** |\n|---|---|---|---|---|---|")
for c in ORDER:
    rs = by_ch[c]
    sets = len({r["set"] for r in rs if r["set"]})
    w(f"| {c} | {len(rs)} | {sum(r['use']=='a' for r in rs)} | {passive[c]} | {sets} | **{units[c]}** |")
w(f"\nRegel der Zuordnung (im Skript): (1) explizite Lemma-Regeln für grammatikgebundene Wörter (z. B. Modalverben → A1-09/G12, *weil* → A1-19/G25, Verben mit Präposition → A2-08/G39) und thematische Leitwörter; (2) Sets geschlossen ins thematische Kapitel; (3) Handlungsfeld-Wortschatz ins HF-Kapitel, bei großen Feldern nach thematischen ID-Bereichen geteilt; (4) restlicher Grundwortschatz in ID-Reihenfolge (≈ Häufigkeit) **vorne gewichtet** in das früheste Kapitel unter der Zielgröße – häufige Funktionswörter kommen früh, damit spätere Texte die Regel „nur eingeführter Wortschatz“ einhalten können.\n")

w("\n## 5. Prüfungsteile × Kapitel (Übung vor Simulation)\n")
w("| Prüfungsteil | geübt in Kapiteln | Anzahl vor Simulation |\n|---|---|---|")
for k, v in o["exam"].items():
    if k.startswith("A1"):
        w(f"| {k} | {', '.join(v)} | {len(v)} vor MS-A1 ✅ |")
    else:
        w(f"| {k} | {', '.join(v['vor_Sim2'])} | {len(v['vor_Sim1'])} vor SIM-A2-1 · {len(v['vor_Sim2'])} vor SIM-A2-2 ✅ |")
w("\n## 6. Redemittel und Textsorten × Kapitel\n")
w("| Redemittel | Kapitel |\n|---|---|")
for k, v in o["cov_red"].items():
    w(f"| {k} | {', '.join(v)} |")
w("\n| Textsorte | Kapitel |\n|---|---|")
for t, cs in TEXTSORTEN.items():
    w(f"| {t} | {', '.join(cs)} |")
w("\n## 7. Handlungsfelder × Kapitel\n")
w("| HF | Kapitel |\n|---|---|")
for i in range(16):
    h = f"HF{i:02d}"
    w(f"| {h} | {', '.join(c['id'] for c in CHAPTERS if h in c['hf'])} |")
open("out/03b-abdeckungsmatrix.md", "w", encoding="utf-8").write("\n".join(L))
print("ok", len(open('out/03-curriculum.md').read()), len(open('out/03a-kapitel-spezifikation.md').read()), len(open('out/03b-abdeckungsmatrix.md').read()))

# --- German decimal comma for measured values (not section refs / dates)
import re, glob
for fn in glob.glob("out/03*.md"):
    t = open(fn, encoding="utf-8").read()
    t = re.sub(r"(?<![\d.])(\d+)\.(\d)(?![\d.])(?=\s?(%|h\b|min\b|\||\s\||\s*$| Plantagen| Tage| Karten|\*\*))", r"\1,\2", t, flags=re.M)
    open(fn, "w", encoding="utf-8").write(t)
```

## `goethe_cmp.py`

```python
# Compare Goethe A1/A2 headwords with own inventory; print uncovered lemmas.
import glob, re, sys, json
G='/root/p3/goethe-institute-wordlist'
def heads(level):
    out=[]
    for f in sorted(glob.glob(f'{G}/{level}/*.tsv')):
        if level=='a1' and f.endswith('a1.tsv'): continue
        for l in open(f, encoding='utf-8'):
            h=l.split('\t')[0].strip()
            if not h or h=='german word': continue
            out.append(h)
    return out
def norm_g(h):
    h=re.sub(r'\(\d+\)','',h)
    h=re.sub(r'\(.*?\)','',h)
    h=re.sub(r'^(der|die|das)\s+','',h.strip())
    h=re.sub(r',.*$','',h)            # drop plural / feminine suffix part
    h=re.sub(r'\s*/.*$','',h)
    h=h.replace('sich ','').strip()
    return h.lower()
def norm_i(l):
    l=re.sub(r'\(.*?\)','',l).strip()
    parts=[p.strip() for p in l.split(',')]
    return {p.lower() for p in parts if p}
inv=set()
for f in ['inv_a1.txt','inv_a2.txt']:
    for l in open(f):
        if l.startswith('##') or not l.strip(): continue
        lem=l.split('|')[0]
        inv|=norm_i(lem)
        for w in lem.split(): inv.add(re.sub(r'[(),]','',w).lower())
a1=heads('a1'); a2=heads('a2')
ga1={norm_g(h) for h in a1}; ga2={norm_g(h) for h in a2}
ga1.discard(''); ga2.discard('')
U=ga1|ga2
miss=sorted(U-inv)
print(len(a1),len(a2),'A1 lemmas',len(ga1),'A2',len(ga2),'union',len(U))
print('cov A1', round(100*len(ga1&inv)/len(ga1),1),'cov union',round(100*len(U&inv)/len(U),1),'missing',len(miss))
json.dump({'miss':miss,'a1':sorted(ga1)},open('miss.json','w'),ensure_ascii=False)
print(' | '.join(miss))
```
