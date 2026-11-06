# Prototyp „Weg zur A2“ – Erkenntnisse aus dem Praxistest

> **Stand:** 06.11.2026 · **Prototyp:** Claude-Artifact „Weg zur A2“ (Vokabeltrainer, 906 A1-Wörter aus `02c`, Leitner 1/3/7/14/30, lokaler Fortschritt + Export) · aktuell **Version 4**
> **Zweck:** Befunde aus dem Prototyp sammeln, die Phase 3–6 beeinflussen. Kein Phasenergebnis; der Prototyp ersetzt Phase 6 nicht.
> **Hinweis D17b (06.11.2026):** Audio vorerst **nur Geräte-TTS**, zuverlässig gemacht für Android/iOS/Web. Die Vorschläge unten zu vorproduziertem Audio (E-P1 Punkt 1, 5; E-P3 Konsequenz) sind damit **zurückgestellt**, nicht verworfen. Das Muster aus v4 (E-P3) ist die Basis für den `SpeechOutPort`.

---

## 0. Regel: Wann der Prototyp angefasst wird (bestätigt 06.11.2026)

- Der Prototyp wird **nicht** automatisch mit dem Projektstand mitgebaut. Die Daten sind fest im HTML; Änderungen an `02c`/`03…` wirken nicht von selbst.
- **Gezielte Updates nur, wenn sie Lernenden oder dem Produkt etwas bringen** (Befund testen, Lernwert erhöhen) und wenig kosten. Spiellogik aus Phase 4 (Leben, Kapiteltests, Korrekturrunde) wird **nicht** im Prototyp nachgebaut – das entsteht einmal sauber in Phase 6.
- Sinnvolle Update-Punkte: **nach Phase 3** (Kapitelreihenfolge statt vorläufiger Themen, A2-Wortschatz, Ergänzungen aus `03d` – begonnen, pausiert) · **nach ersten Content-Batches in Phase 5** (Beispielsätze, Test vorproduzierter Audios) · **Phase 6** löst den Prototyp ab.
- **Fortschritt übertragbar:** Prototyp speichert Leitner-Daten unter den stabilen Inventar-IDs (`W-A1-0001` …). Phase 6 muss den Prototyp-Export (`{"app":"weg-zur-a2-prototyp","schema":1,"state":{profile,cards,days,settings}}`) als Importformat akzeptieren.
- Prototyp-Updates laufen als eigener, ausdrücklich so benannter Chat-Auftrag – nicht als Nebenbei-Arbeit in einem Phasen-Chat.

---

## E-P1 – Audio (Web Speech / Geräte-TTS) zu schnell und undeutlich, Artikel kaum hörbar (06.11.2026)

**Befund (Test durch Betreiber):** Vorlesen über `speechSynthesis` mit Rate 0,85 war zu schnell und teilweise undeutlich. Der Artikel („der/die/das“) ging im zusammenhängenden Sprechen fast unter.

**Folgebefund (v2):** Nach dem Aufteilen in „Artikel – Pause – Nomen“ wurde teilweise **nur der Artikel** gesprochen, das Nomen fiel weg. v3 versuchte eine sequenzielle Abspielkette – siehe E-P3: auf Android ebenfalls unzuverlässig.

**Warum das wichtig ist:** Der Artikel ist bei A1 Lerninhalt, nicht Beiwerk. Wer ihn nicht klar hört, speichert das Nomen ohne Genus ab, und spätere Grammatik (Akkusativ, Dativ, Adjektivendungen) baut auf falschem Input auf. Für Hören-Aufgaben gilt dasselbe: undeutliches Audio misst das Gerät, nicht das Hörverstehen. **Geräte-TTS ist auch technisch unzuverlässig** (geräte- und browserabhängiges Verhalten, s. E-P3).

**Maßnahmen im Prototyp:**
- Tempo-Stufen langsam 0,6 / mittel 0,75 (Standard) / normal 0,9
- Artikel abgesetzt („der. Bahnhof.“), abschaltbar; Knopf „langsam“: Artikel und Wort abgesetzt, danach die ganze Wortgruppe
- Stimmenwahl (de-AT bevorzugt, dann neuronale/Online-Stimmen) + Probe-Knopf
- v4: eine Äußerung pro Wort statt Kette (s. E-P3)

**Konsequenzen für das Produkt (Vorschlag, zur Bestätigung):**
1. **Phase 6.3 `SpeechOutPort`:** Geräte-TTS nur als Fallback. Für Wortschatz (Lemma mit Artikel) und alle Hörtexte **vorproduzierte Audiodateien** mit einer hochwertigen, gleichbleibenden Stimme (österreichische Aussprache) – im Masterprompt bisher „optional“, nach diesem Befund **Pflicht** für Wortschatz und Hören. *(D17b: zurückgestellt.)*
2. **Phase 5.3 Hören:** Die Annahme „TTS-Rate ~0,8 → 1,0“ gilt nicht für Geräte-TTS; Tempo-Progression an vorproduziertem Audio festlegen (Sprechtempo der Modelltests, Lücke L15, als Zielwert).
3. **Didaktik Wortschatz:** Jedes Nomen im Audio als „Artikel – Pause – Nomen – Wortgruppe“ einführen; in Wiederholungen nur die Wortgruppe. Mit vorproduziertem Audio ist die Pause im Audio selbst geschnitten – keine Laufzeit-Tricks nötig.
4. **Gerätecheck (Phase 6.1):** Prüfpunkte „deutsche Stimme vorhanden? Artikel verständlich? Bleibt die Ausgabe über 20+ Wörter stabil? Browser vs. In-App-Ansicht?“ ergänzen.
5. **Phase 6.1 Stufe 1 (Artifact):** Audiodateien müssen mitveröffentlicht werden (Größenlimit 16 MB je Datei beachten; Kompression z. B. Opus/AAC mono) – Mengengerüst in Phase 5 rechnen. *(D17b: zurückgestellt.)*
6. **Phase 6 Fallback-Code:** Wenn Geräte-TTS genutzt wird, dann nach dem Muster aus Prototyp v4 (s. E-P3), nie mehrere Äußerungen in Folge.

**Offene Frage:** Welche Stimme/welcher TTS-Dienst für vorproduziertes Audio (Lizenz für Weitergabe, österreichische Aussprache, Kosten)? → Recherche spätestens vor Phase 5.

---

## E-P2 – Artikel (Genus) wurde nicht abgefragt (06.11.2026)

**Befund (Frage des Betreibers):** In der Übersetzung (en/tl) fehlt der Artikel – das ist korrekt, weil Englisch und Tagalog kein Genus haben („the“, „ang“ für alle Nomen). Dabei fiel auf: Der Prototyp zeigte den Artikel nur an, **fragte ihn aber nie ab**. Bei „Wie heißt das auf Deutsch?“ waren die Distraktoren andere Wörter; das richtige Wort war auch ohne Genuswissen wählbar.

**Warum das wichtig ist:** Nur aktiv Abgerufenes festigt sich (Retrieval Practice). Genus ist Grundlage für G-Themen in `02d` (Artikel & Nomen → Akkusativ → Dativ → Adjektivendungen) und für Sprachbausteine/Schreiben in der Prüfung.

**Maßnahme im Prototyp (v3):** Aufgabentyp **„der, die oder das?“** – ab Fach 2 für Nomen mit eindeutigem Einzelartikel (434 von 476 Nomen; ausgenommen Paare wie „Lehrer, Lehrerin“, Plural-Wörter, Länder mit „(das)“). Wechselt sich pro Wiederholung mit der Bedeutungs-/Produktionsfrage ab (Interleaving). Falscher Artikel = Fehler → Fach 1; die Wiederholung in der Runde fragt wieder den Artikel. Vor der Antwort kein Audio (würde den Artikel verraten).

**Konsequenzen für das Produkt (Vorschlag):** *(entschieden in D14/V4: Richtungsrotation derselben Nomenkarte, Fach 5 = Produktion mit Artikel)*
1. **Phase 5:** Genus-Abfrage als eigener Item-Typ im Pool je Kapitel (passt zu `02g` Übungstypen „Grammatik-Drill“/„Zuordnung“) – mit eigenem Leitner-Eintrag oder als Richtung desselben Vokabel-Items (in Phase 4 entscheiden).
2. **Phase 4:** Leitner-Regel klären: zählt ein Wort als „gefestigt“ erst, wenn Bedeutung **und** Genus sicher sitzen? Vorschlag: getrennte Leitner-Spuren je Abfragerichtung.
3. Prüfen, ob Genus-Farbcodierung (der/die/das) als Gedächtnisstütze sinnvoll ist – Lernforschungsbeleg vor Einsatz suchen.

---

## E-P3 – Vorlesen auf Android (Google Pixel 9 Pro, Chrome) instabil (06.11.2026)

**Befund (Test durch Betreiber):** Auf dem Pixel 9 Pro funktionierte Vorlesen zuerst gar nicht, in Chrome dann nur teilweise und fiel nach einigen Wörtern ganz aus. Mit „Artikel einzeln“ (Kette aus mehreren Äußerungen, v3) funktionierte es praktisch nicht.

**Wahrscheinliche Ursachen** (bekanntes Verhalten von Chrome/Android, am Gerät noch nicht bestätigt):
- In-App-Ansichten (z. B. Claude-App, Android WebView) bieten `speechSynthesis` oft gar nicht an → Link im Browser öffnen.
- Mehrere Äußerungen hintereinander bzw. `speak()` kurz nach `cancel()` werden verworfen; `cancel()` auf eine leerlaufende Engine und Wechsel in den Hintergrund lassen die Engine hängen, bis die Seite neu geladen wird.
- Fehlende/abweichende Sprachvariante (`de-AT`) bei der Google-Sprachausgabe → Ausgabe bleibt stumm.

**Maßnahme im Prototyp (v4):** eine Äußerung pro Wort, Pause über Satzzeichen („der. Bahnhof.“) · `cancel()` nur, wenn etwas läuft · `resume()` einer pausierten Engine · Start direkt im Tipp (Nutzeraktivierung) · Watchdog: kein Start nach 2,5 s → Engine zurücksetzen, zweiter Versuch mit Standardstimme `de-DE` · Stopp beim Ausblenden der Seite · Knopf „Sprachausgabe zurücksetzen“ · **Diagnose-Protokoll** in den Einstellungen (Start/Ende/Fehlercodes, Stimme, Tempo).

**Status:** Fix ungetestet. Nächster Test am Pixel: 20–30 Wörter in Chrome durchklicken; bei Ausfall das Diagnose-Protokoll abschreiben bzw. Screenshot. Ergebnis gehört in `geraetecheck.md` (E4).

**Konsequenz für das Produkt:** Bestätigt E-P1 Punkt 1 deutlich – Geräte-TTS ist für Lerninhalte nicht verlässlich genug; vorproduziertes Audio (normales `<audio>`-Element, auf Android stabil) wird zur Voraussetzung, nicht zur Option. *(D17b: Andi hält Geräte-TTS mit Härtung für machbar; Entscheidung steht, R6 bleibt offen.)*
