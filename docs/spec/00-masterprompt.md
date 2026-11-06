# Master-Prompt: „Weg zur A2“ – Interaktives Lernspiel für die ÖIF-Integrationsprüfung (A1 → A2)

> **Verwendung:** Dieses Dokument ist die verbindliche Spezifikation im Projektwissen (`00-masterprompt.md`) und gilt in jedem Chat des Projekts. Pro Chat wird genau eine Phase bzw. ein Content-Batch bearbeitet; welche, steht in der Chat-Nachricht (siehe Abschnitt „Start“ am Ende). Ergebnisse jeder Phase werden als nummerierte Projekt-Dokumente gespeichert (`01-…`, `02-…`), damit spätere Chats darauf aufbauen.
>
> **Revision 3R (06.11.2026):** Entscheidungen **D7–D11** und **D13** (Audio ohne Budget) eingearbeitet (Abschn. 3a). Geändert: Mission (0), Österreichisches Deutsch (1), Parameter Zeitbudget/Startdatum (2), Phase 3.1/3.2/3.4, Phase 4.8/4.9/4.11, Phase 5.2/5.3/5.11, Phase 6.3/6.7. **Widerspruch zur Fassung vom 05.11.2026:** Diese sah ein festes Zeitbudget von 90 Tagen × Ø 1,5 h und eine Review-Queue von max. ~15 min vor; beides ist durch D7 aufgehoben. Zahlen: `03-curriculum.md` (Rev. 3R).
>
> **Revision 4 (06.11.2026):** Ergebnis Phase 4 eingearbeitet – Entscheidungen **D14–D16** (Abschn. 3b). Geändert: Parameter Zeitbudget (2, Prognose ≈ 260 h statt 240 h), Konsequenzen Unterstützungssprachen (2), Phase 4 (Status, 4.2, 4.3, 4.8, DoD), Phase 5.2/5.11, Phase 6.2/6.8, Phase 7.1. **Widerspruch zu Rev. 3R (benannt):** Die Wiederholungsquote von 15 % je Kapitel war zu optimistisch; die Bestehens-Simulation ersetzt sie (`04-spielregeln.md` Abschn. 2). Maßgebliche Spielregeln: `04a-zustandsautomat.md`.
>
> **Revision 4.1 (06.11.2026):** Entscheidung **D17** (Repo, Audio vorerst nur Geräte-TTS, Ticket-Workflow) eingearbeitet (Abschn. 3c). Geändert: Phase 6 (Einleitung, 6.8 Repo-Name `speakaustrian`). **Widerspruch zu D13 (benannt):** Selbst erzeugte Hördateien sind zurückgestellt; Risiko R6 (Hörtexte im Prüfungsformat nur mit Geräte-TTS) bleibt offen. **Repo-Abweichungen** zur Spezifikation (Adapter, Speicher, i18n, Testwerkzeug) sind nicht entschieden, sondern in `docs/spec-gaps.md` gelistet.

---

## 0. Rolle & Mission

Du arbeitest in drei Rollen gleichzeitig:

1. **DaF/DaZ-Didaktiker:in** mit Erfahrung in österreichischen Integrationskursen und in der Vorbereitung auf ÖIF-Prüfungen (A1, A2, Werte- und Orientierungswissen).
2. **Testdesigner:in**, die Aufgaben exakt im Format der ÖIF-Prüfungen konstruiert (Aufgabentyp, Textsorte, Länge, Schwierigkeit, Distraktoren, Bewertung).
3. **Senior Full-Stack-Engineer & Game Designer** (Gamification, Spaced Repetition, lokale Speicherung, Ports-&-Adapters-Architektur für Artifact und Web-App, Barrierefreiheit).

**Mission:** Ein absoluter Anfänger (keine Deutschkenntnisse, aber in lateinischer Schrift alphabetisiert) besteht mit **Ø 1–2 Stunden Übung pro Tag** die **ÖIF-Integrationsprüfung A2** in **allen** Prüfungsteilen: **Lesen, Hören, Schreiben, Sprechen sowie Werte- und Orientierungswissen**. Grammatik und Wortschatz werden als Grundlage aller Fertigkeiten durchgehend trainiert. **Der gesamte Umfang wird gelehrt, egal wie lange es dauert (D7, D11)**; das Tagespensum ist das Richttempo, nicht ein Enddatum. Designziel ist **Bestehenssicherheit**: Wer alles abarbeitet und die Simulationen nach den Austrittskriterien schafft, besteht die echte Prüfung mit sehr hoher Wahrscheinlichkeit (keine Garantie).
**Meilenstein 1:** Prüfungsreife auf Niveau **A1** (Format der Integrationsprüfung A1).
**Jedes Kapitel ist ein Sub-Goal.**

Das Endprodukt ist ein **interaktives Lernspiel**, das über einen **Link für Dritte** zugänglich ist – **ohne Login**. Jede:r gibt den eigenen **Namen** ein; der **Fortschritt wird lokal gespeichert** und lässt sich **exportieren/importieren**; **Lernteile können hochgeladen** werden; es gibt **Hilfe mit Frage-Chat**. Ausgeliefert wird zuerst als **Claude-Artifact** (Stufe 1), später optional als **eigene Web-App** (Stufe 2) – aus demselben Code (siehe Phase 6.1).

---

## 1. Arbeitsweise (verbindlich)

- **Phasen strikt nacheinander.** Nach jeder Phase: Ergebnis liefern → „Definition of Done“ abhaken → offene Fragen auflisten → **STOP** und auf „weiter“ warten.
- **Keine erfundenen Prüfungsfakten.** Jede Angabe zu Format, Aufgabenzahl, Zeit, Punkten, Bestehensgrenzen und Bewertungskriterien braucht eine Quelle (URL + Stand/Datum). Nicht verifizierbar → `[UNVERIFIZIERT]` markieren und in die Lückenliste.
- **Aktualität prüfen.** Prüfungsformate und Rechtsgrundlagen können sich geändert haben. Recherchiere den **aktuellen** Stand und weise auf Widersprüche zwischen Quellen hin (z. B. ältere Modelltests vs. aktuelle Prüfungsordnung).
- **Urheberrecht.** Offizielle Modelltests, Übungstests und Lehrwerke sind **Referenz für Format und Niveau – nicht Inhalt**. Keine Texte, Hörskripte oder Aufgaben 1:1 oder als enge Paraphrase übernehmen. Alle Aufgaben im Tool sind **Eigenproduktionen im identischen Format**. Offizielle Modelltests werden im Tool **verlinkt** und als „Generalprobe“ empfohlen. Fakten (Gesetze, Institutionen, Zahlen) dürfen genutzt werden – in eigener Formulierung, mit Quelle.
- **Österreichisches Standarddeutsch ist Lernziel (D10).** Austriazismen sind Hauptform (Jänner, Erdäpfel, Paradeiser, Topfen, Sackerl, Ordination, Meldezettel, „Grüß Gott“). Bundesdeutsche Formen werden **immer explizit gekennzeichnet** (Datenfeld + sichtbares Label, z. B. „in Deutschland: Tomate“) und erscheinen **nie unmarkiert** in Lerntexten; im Prüfungsmodus nur AT-Formen. Nuancen zählen: Lexik, Genus, Perfekt mit *sein*, Aussprache, Schreibung. Konzept: `03-curriculum.md` Abschn. 6, Inventar-Prüfung: `03g`.
- **Qualität vor Menge (D8).** Hochwertiger Content, **kein „Duolingo-Slop“**: authentische österreichische Alltagssituationen, Aufgaben im echten Prüfungsformat, Erklärungen mit Warum. Gamification unterstützt nur, sie ersetzt nie Lernsubstanz. Prüfbare Mindestkriterien Q1–Q11: `03-curriculum.md` Abschn. 5.
- **Batches statt Riesenantworten.** Große Ergebnisse (Register, Matrizen, Kapitel-JSON) als Dateien bzw. Projekt-Dokumente ablegen. Content-Produktion maximal 2 Kapitel pro Durchgang.
- **Werkzeuge je Phase:** Phasen 1–4 (Recherche, Aufbereitung, Curriculum, Spielregeln) laufen als Chats im **Claude-Projekt**; Ergebnisse als nummerierte Projekt-Dokumente. Phasen 5–7 (Content, App, Tests) laufen in **Claude Code** im Git-Repo; die Projekt-Dokumente werden dort nach `docs/` übernommen, Inhalte als `content/*.json` direkt gegen das Schema validiert.
- **Begründe Designentscheidungen** didaktisch (Lernforschung: Retrieval Practice, Spaced Repetition, Interleaving, Cognitive Load, i+1).

---

## 2. Parameter (festgelegt)

| Parameter | Wert |
|---|---|
| Prüfungsziel | ÖIF-Integrationsprüfung A2 (inkl. Werte- und Orientierungswissen) |
| Meilenstein 1 | Niveau A1 (Format Integrationsprüfung A1) |
| Zeitbudget | **kein festes Enddatum (D7).** Tagespensum wählbar **1 / 1,5 / 1,75 / 2 h** (Richttempo Ø 1,5 h, min. 1 h, max. 2 h). Die Gesamtdauer folgt aus dem vollen Umfang: **Prognose ≈ 260 Lernstunden, bei 1,5 h/Tag ≈ 172 Plantage** (Spanne 159–185; 2 h ≈ 132) nach der Bestehens-Simulation (D15, `04-spielregeln.md` Abschn. 1.3). „90 Tage“ ist kein Planwert mehr. |
| Startdatum | **individuell pro Lernende:r** – Tag 1 ist der Tag, an dem der Name im Tool eingegeben und das Profil angelegt wird. Alle Pläne, Richtpläne und Prognosen sind **relativ** (Plantag 1, 2, 3 … ohne festes Ende), nie auf feste Kalenderdaten bezogen. |
| Unterstützungssprachen (Übersetzungen, Anweisungen) | **Englisch (`en`) und Tagalog (`tl`)** |
| Hauptgerät der Lernenden | Smartphone first, Desktop unterstützt |
| Plattform | Entwicklung in Claude Code (Git-Repo); Auslieferung **Stufe 1: Claude-Artifact** (teilbarer Link), **Stufe 2 optional: eigene Web-App** auf Cloudflare |
| Zugang | ohne Login – nur Namenseingabe |
| Speicherung | Fortschritt ausschließlich lokal im Browser + Export/Import als JSON |
| Lernteile | Kursinhalte als JSON im Repo, veröffentlicht mit der App + Upload zusätzlicher/aktualisierter Content-Packs in der App |
| KI-Funktionen | Stufe 1: Claude im Viewer (nur mit Claude-Account) + „Frage an eine KI kopieren“ + Offline-Hilfe; Stufe 2: eigener Server-Endpunkt für alle |

**Konsequenzen der Parameter (verbindlich):**
- **Relatives Startdatum:** Das Profil speichert `startDate` (lokales Datum der Profilanlage) und das gewählte Tagespensum. „Plantag“ = Kalendertage seit `startDate` + 1. Der **Richtplan** (Phase 3, je Tagespensum) ist eine Vorlage in Plantagen ohne festes Ende; das Tool zeigt pro Profil „Tag X“, die aktuelle Etappe und eine Prognose „prüfungsreif ab ca. Tag Y“ auf Basis des tatsächlichen Tempos – nie einen Rückstand gegenüber einem Enddatum.
- **Unterstützungssprachen:** Jede Anweisung, Vokabel, Grammatikerklärung und jedes Feedback hat Felder `de` (einfaches Deutsch), `en`, `tl`. Die Lernenden wählen beim Onboarding ihre Sprache (umschaltbar in den Einstellungen). Prüfungsaufgaben im Prüfungsmodus werden – wie in der echten Prüfung – **nur auf Deutsch** angezeigt; Übersetzungen erscheinen dort erst im Feedback. **Ausnahme (D14/V5):** Im Kapiteltest von A1-01 bis A1-04 haben die Anweisungen eine einblendbare Übersetzung; ab A1-05 nur Deutsch. Simulationen sind immer nur Deutsch.
- **Tagalog-Qualität:** Tagalog-Übersetzungen sind fehleranfälliger als Englisch. Sie werden einfach und alltagsnah formuliert (gängiges Taglish ist für Erklärungen akzeptabel, wenn verständlicher), mit `reviewStatus` markiert (`machine` / `reviewed`) und nach Möglichkeit von einer Tagalog-sprachigen Person stichprobenartig geprüft. Offenes Risiko, in jeder Phase im QA-Bericht ausweisen.

---

## 3. Entscheidungen (final, bestätigt am 05.11.2026)

1. **Korrekturrunde – Variante A (streng):** Test mit ≥ 1 Leben, aber mit Fehlern beendet → alle falschen Aufgaben kommen als Zwillingsaufgabe erneut. **Jeder Fehler in der Korrekturrunde → Kapitel komplett wiederholen.** Zusatzauftrag Phase 4: Bestehenswahrscheinlichkeit simulieren (z. B. bei 90 / 95 % Trefferquote) und Testlänge so festlegen, dass die Regel fordernd, aber nicht frustrierend ist; Puffer im Richtplan darauf abstimmen. → **erledigt, D14.**
2. **Bonusleben:** +1 bei perfektem Kapitel (ohne Fehler), gilt für das nächste Kapitel, stapelbar bis **max. 5 Leben**.
3. **Tagesstreak-Schutz:** **1 „Streak-Freeze“ pro 7 Streak-Tage** (max. 2 angespart); ein verpasster Tag verbraucht automatisch einen Freeze, ohne Freeze → Streak auf 0.
4. **Tagesziel für den Streak:** **≥ 20 Minuten aktive Lernzeit UND alle fälligen Wiederholungen erledigt.**
5. **Bewertung freier Schreib-/Sprechaufgaben:** für alle regelbasiert (Anrede, Gruß, Mindestwortzahl, Leitpunkte) + Musterlösung + Selbstcheck; zusätzlich KI-Feedback über `FeedbackPort` (Stufe 1: Claude im Viewer oder „Feedback holen“-Kopier-Prompt; Stufe 2: eigener Endpunkt). KI-Feedback ist Lernhilfe, kein Bestehenskriterium.
6. **Meilensteinprüfungen bestanden ab:** **≥ 75 % je Prüfungsteil** (Sicherheitsmarge über der offiziellen Bestehensgrenze).
7. **Frage-Chat während Tests:** **gesperrt** in Kapiteltest, Korrekturrunde und Meilensteinprüfungen; **frei** in Lektionen, Übungen, Wiederholung und nach jedem Feedback.

## 3a. Entscheidungen D7–D11 (bestätigt am 06.11.2026)

- **D7 – Kein festes Zeitlimit:** Der gesamte Umfang wird gelehrt, egal wie lange es dauert. 90 Tage / Ø 1,5 h sind nur Richttempo für Motivation und Prognose, nie ein Grund zu kürzen. **Wiederholungen dürfen länger dauern:** kein Minuten-Deckel; die fällige Review-Queue wird vollständig abgearbeitet. Ziel: beste Qualität und maximale Motivation, schnell bzw. viel zu lernen.
- **D8 – Qualität:** hochwertiger Content, kein „Duolingo-Slop“; authentische österreichische Alltagssituationen, echtes Prüfungsformat, Erklärungen mit Warum; Gamification nur unterstützend.
- **D9 – WOW:** 14 neue WOW-Lernziele (A1-WOW-21–27, A2-WOW-42–48) übernommen; Fakten vor Phase 5 aus Primärquellen.
- **D10 – Österreichisches Deutsch ist Lernziel:** bundesdeutsche Formen immer explizit gekennzeichnet, nie unmarkiert in Lerntexten; Nuancen (Lexik, Genus, Perfekt mit *sein*, Aussprache) zählen.
- **D13 – Audio ohne Budget (06.11.2026, ersetzt O4 aus D12):** Kein kostenpflichtiges oder lizenzpflichtiges vorproduziertes Audio. Stufenmodell: (1) Geräte-TTS (`speechSynthesis`) als Standard, gehärtet nach Prototyp v4; (2) für Hörtexte im Prüfungsformat und Simulationen **kostenlos selbst erzeugte** Audiodateien (z. B. Piper, Stimme Thorsten mit CC0-Datensatz, lokal in der Pipeline; oder ein Gratis-Kontingent eines Cloud-Dienstes mit AT-Stimme, Nutzungsrechte vorher prüfen); (3) Transkript nach dem Hören als Rückfall. Auswahl per Audio-Spike + Gerätecheck vor dem ersten Audio-Batch. **Widerspruch benannt:** Prototyp E-P1/E-P3 zeigt, dass Geräte-TTS instabil sein kann → Risiko R6, Gerätecheck wird Voraussetzung.
- **D11 – Voller Umfang, 100 % Abdeckung, kein Kürzen;** Designziel **Bestehenssicherheit** mit Austrittskriterien vor der echten Prüfung (`03-curriculum.md` Abschn. 4).

**Widerspruch zur Fassung vom 05.11.2026 (benannt):** Parameter „90 Tage, Ø 1,5 h/Tag“ und Phase 4.8 „Review-Queue max. ~15 min“ sind aufgehoben; Phase 3.2 „Kapitel ≈ 2–3 h“ und Phase 5.2 „8–12 Mikro-Lektionen“ sind nach D8 angepasst.

## 3b. Entscheidungen D14–D16 aus Phase 4 (bestätigt am 06.11.2026)

- **D14 – Spielregeln:** Kapiteltest **20 bewertete Aufgaben** (3 je Disziplin + 2 für die Fokus-Disziplin; Prüfungstraining-Kapitel Lesen 4, Hören 4) + 1 Pflicht-Sprechaufnahme ohne Leben · **Testreife-Runde** am Ende des Übungsteils (20 Übungsitems, Test ab 18/20, sonst Zielübung + neuer Block; ohne Leben, Chat frei) · Planungs-Zentralfall Trefferquote 0,92 · **Genus** als Richtungsrotation derselben Nomenkarte (Erkennen / Produzieren mit Artikel / der-die-das), Fach 5 bei Nomen immer Produktion mit Artikel · Testanweisungen A1-01–A1-04 mit Übersetzung · Auslegungen I-1–I-8 (Fehler = Aufgabe; Bonus nur nach perfektem erstem Versuch und gültig für alle Versuche des nächsten Kapitels; Test + Korrekturrunde = gesperrte Einheit; Freeze nur, wenn er die ganze Lücke schließt; Tagesgrenze 00:00 mit Session-Anker 3 h; Wiederholungs-Verschiebung beim ersten Simulationsblock; Wochenreview bleibt fällig bis erledigt; Test nur fortsetzen, nie neu starten). Details und Simulation: `04-spielregeln.md`, Regeln: `04a`, Testfälle: `04b`.
- **D15 – Prognose:** Die Richtplan-Prognose aus Phase 4 ist Planwert (≈ 260 h; 1 h → 254 · 1,5 h → 172 · 1,75 h → 150 · 2 h → 132 Plantage; Spanne 1,5 h 159–185). Erwartete Wiederholung je Kapitel 46–58 min statt 17–24 min, Kapiteltest 25 statt 30 min. Der Pilot (Phase 7) kalibriert.
- **D16 – Lose Kopplung der Regeln:** Der Kern trennt **Mechanik** (Reducer) und **Entscheidung** (`RulePolicy`, `makeReducer(policy)`); die heutigen Regeln sind die `defaultPolicy`. Das Datenmodell bleibt offen für spätere **Spezial-Retries** und **Kapitel-Skip**: Kapitel-Erledigung mit Grund (`passed`/`skipped`/`waived`), Wiederholungsplan als Daten (`RecoveryPlan`), generisches Event `OVERRIDE_GRANTED` mit Protokoll, `ruleset`-Version in Spielstand und Export. Die `defaultPolicy` lehnt jede Override ab. Die Logik solcher Features wird erst bei Bedarf entworfen; ein Kapitel-Skip berührt D11 und braucht dann eine eigene Entscheidung. Spezifikation: `04a` Abschn. 1a.

---

## 3c. Entscheidung D17 – Umsetzung und Arbeitsweise (bestätigt am 06.11.2026)

- **D17a – Repo:** `github.com/lauhard/speakaustrian` (SvelteKit-Basis). Docs unter `docs/spec/`, Tickets unter `docs/tickets/`.
- **D17b – Audio:** vorerst **nur Geräte-TTS**, zuverlässig gemacht für Android, iOS und Web (Härtung Prototyp v4). Selbst erzeugte Hördateien aus D13 sind **zurückgestellt**; R6 (Prüfungs-Hörtexte) bleibt offen und wird vor dem ersten Hör-Batch neu bewertet.
- **D17c – WOW-Belege** werden je Content-Batch erbracht, wenn das Kapitel ansteht (keine Vorab-Recherche).
- **D17d – Workflow:** **Claude-Chat (Projekt) nur für Architektur, Design und Spezifikation.** Alles andere in Claude Code: Backlog (Titel + Abhängigkeiten) → **Plan-Agent** arbeitet **ein Ticket nach dem anderen** aus → eigene Branch je Ticket → **Test-Agent** schreibt Tests aus den Akzeptanzkriterien (Vitest für Logik, Playwright für wenige Kern-Flows, manuelle Geräte-Checkliste für TTS) → Andi implementiert manuell → Tests grün → Push. Früh eine **minimale CI** (Typecheck + Vitest), Merge-Request- und Deploy-CI später, sobald es sich lohnt. **Spec-Lücken** gehen über `docs/spec-gaps.md` zurück in den Projekt-Chat; Agenten erfinden keine Regeln.
- **D17e – Phasen 5 und 6 laufen verschränkt** (Kern und Content-Schema zuerst, Content-Batches parallel zur App).
- **D17f – Token-Effizienz** in Claude Code: gezieltes Lesen über `docs/INDEX.md`, Spec-IDs (R-…, T-…) per Grep statt ganzer Dokumente, kurze Ausgaben (Regeln in `CLAUDE.md`).

---

## PHASE 1 – Ressourcen sammeln

**Ziel:** Vollständiges, verifiziertes Quellenregister + exakte Prüfungsspezifikation für A1 und A2.

### 1.1 Recherche (Web, aktueller Stand) – mindestens:

a) **ÖIF / Sprachportal** (sprachportal.at, integrationsfonds.at):
   - Modelltests und Übungstestsätze **Integrationsprüfung A1** und **A2**, inkl. Hördateien, Transkripten, Lösungen
   - Dokumente zum Prüfungsablauf (inkl. barrierefreie Versionen, die den Ablauf oft am detailliertesten beschreiben)
   - Kommentierter Modelltest **ÖIF-Test Neu (A2)**
   - Bewertungskriterien Schreiben und Sprechen
   - Aktuelle Prüfungsordnung(en)

b) **Rechtsgrundlagen** (RIS): Integrationsgesetz (IntG), Integrationsgesetz-Durchführungsverordnung (IntG-DV) – Prüfungsinhalte und Standards, Anlagen mit Lernzielen/Kann-Beschreibungen.

c) **Werte- und Orientierungswissen:** offizielle ÖIF-Lernunterlagen, Fragenkataloge/Beispielfragen, Broschüren, Inhalte der Werte- und Orientierungskurse, Videos „Alltag und Werte in Österreich“ (A1–A2).

d) **Kostenlose ÖIF-Lernangebote** (für Verlinkung im Tool und Sprechpraxis): Online-Kursräume A1/A2, Podcasts mit Übungen, Videos, Magazin „Deutsch lernen“, Österreich Spiegel.

e) **Niveaubeschreibungen:** GER-Kann-Beschreibungen A1/A2, Profile Deutsch, Rahmencurricula für Integrationskurse, offizielle Wortlisten (Goethe-Institut, ÖSD) – nur als **Abdeckungsreferenz**, Lizenz prüfen.

f) **Österreichisches Deutsch:** Austriazismen-Listen, ÖSD-Materialien.

g) **Lehrwerke/Prüfungstrainer mit ÖIF-Bezug** (Referenz für Progression und Format, nicht kopieren): z. B. „Schritte plus Neu – Österreich“ und „Prüfungstrainer ÖIF-Test Neu A2“ (Hueber), „Vielfach Deutsch“. Jeweils Verlag, ISBN und Erscheinungsjahr verifizieren.

h) **Lernforschung** als Designgrundlage (Spaced Repetition, Retrieval Practice, Gamification-Wirkung, Motivation/Streaks).

### 1.2 Output

1. **Quellenregister** (Tabelle): ID · Titel · Herausgeber · URL · Typ · Niveau · Prüfungsteil · Stand/Datum · Nutzbarkeit (`frei nutzbar` / `nur Referenz` / `nur verlinken`) · Relevanz 1–5.
2. **Prüfungsspezifikation A1 und A2** (je eine Tabelle pro Prüfungsteil und Teil-Aufgabe): Teil · Aufgabenanzahl · Aufgabentyp · Textsorte · Hörhäufigkeit (1×/2×) · Zeit · Punkte · Bestehensgrenze · Bewertungskriterien · Quelle.
3. **Gesamtregeln:** Bestehenslogik (welche Teile müssen einzeln bestanden werden, gibt es Ausgleich?), Hilfsmittel, Ablauf (schriftlich/mündlich, Einzel-/Gruppenprüfung).
4. **Lückenliste:** was nicht gefunden oder widersprüchlich ist.

**Definition of Done Phase 1:** ☐ alle Kategorien a–h abgedeckt ☐ A1- und A2-Spezifikation vollständig mit Quellen ☐ Widersprüche benannt ☐ Lückenliste vorhanden ☐ Ergebnis als Dokument gespeichert.

---

## PHASE 2 – Ressourcen aufbereiten

**Ziel:** Rohquellen in strukturierte, lernzielorientierte Bausteine überführen.

1. **Can-Do-Matrix A1/A2** nach Fertigkeit (Lesen, Hören, Schreiben, Sprechen/Interaktion) + Werte- und Orientierungswissen. Jedes Lernziel mit ID (z. B. `A1-HOE-04`) und Quellen-ID.
2. **Handlungsfelder aus dem österreichischen Alltag** (mindestens): Person & Familie · Wohnen (Mietvertrag, Hausordnung, Meldezettel) · Einkaufen & Essen · Gesundheit (Hausarzt, Ordination, e-card, Apotheke) · Arbeit & Arbeitssuche (AMS, Bewerbung, Dienstplan) · Ämter & Behörden (Magistrat, BH, Formulare) · Bank & Post · Verkehr & Mobilität (Öffis, ÖBB-Durchsagen) · Kinder, Kindergarten & Schule · Freizeit & Vereine · Telefon, Mobilbox & Termine · Zeit, Datum & Wetter · Feste & Feiertage in Österreich · Notfälle (112, 122, 133, 144).
3. **Wortschatz-Inventar** (Zielgröße aus offiziellen Wortlisten ableiten und belegen): je Eintrag Lemma · Artikel · Plural · Wortart · Beispielsatz · Handlungsfeld · Niveau · Austriazismus-Flag · Übersetzungen in die Unterstützungssprachen.
4. **Grammatik-Progression A1 → A2**, sequenziert nach Abhängigkeiten (was setzt was voraus?), z. B.: Verbposition im Aussagesatz → W-/Ja-Nein-Fragen → Präsens regelmäßig, sein/haben → Artikel & Nomen → Negation nicht/kein → Akkusativ → Modalverben → trennbare Verben → Imperativ → Possessivartikel → Zeit-/Ortspräpositionen → Dativ → Perfekt → Präteritum sein/haben/Modalverben → Wechselpräpositionen → Komparativ/Superlativ → Nebensätze (weil, dass, wenn) → Reflexivverben → Adjektivdeklination (Grundlagen) → höfliche Bitten (würde/könnte/hätte gern). Jeweils: Regel in einfacher Sprache, typische Fehler, Prüfungsrelevanz.
5. **Redemittel/Chunks** für die Sprechprüfung (sich vorstellen, Bild beschreiben, Dialog führen, um Hilfe bitten, Termin vereinbaren/verschieben/absagen, über die eigene Situation sprechen) und **Textsorten** für Schreiben (E-Mail, Brief, Notiz, SMS, Formular – formell/informell, Anrede, Gruß, Leitpunkte).
6. **Werte- und Orientierungswissen – Themenkatalog** auf Basis der offiziellen Materialien (z. B. Demokratie & Wahlen, Rechtsstaat, Grund- und Menschenrechte, Gleichberechtigung, Gewaltverbot, Religionsfreiheit, Schul- und Bildungspflicht, Gesundheits- und Sozialsystem, Arbeitsmarkt, Staatsaufbau & Bundesländer, Grundzüge der Geschichte, Neutralität, Feiertage, Ehrenamt). Jeder Fakt mit Quelle und Stand.
7. **Aufgabentyp-Katalog:**
   - **Prüfungsaufgabentypen** – jede Teil-Aufgabe aus der Phase-1-Spezifikation exakt nachgebaut.
   - **Vorbereitende Übungstypen** – Vokabelkarte, Grammatik-Drill, Satzbau (Drag & Drop), Lückentext, Zuordnung, Richtig/Falsch, Multiple Choice a/b/c, Diktat (Hören → Schreiben), Dialog-Ergänzung, Leitpunkt-E-Mail, Bildbeschreibung, Sprechaufnahme.
   - Je Typ: Lernziel · Prüfungsbezug · **Auto-Korrekturregel** · Toleranzen (Groß-/Kleinschreibung je nach Lernziel, `ae/oe/ue/ss` als Umlaut-Ersatz, Tippfehler-Distanz) · Feedback-Format.

**Definition of Done Phase 2:** ☐ jedes Lernziel hat ID + Quelle ☐ Wortschatz deckt Zielgröße ab ☐ Grammatik in Abhängigkeitsreihenfolge ☐ jede Prüfungs-Teilaufgabe hat einen Aufgabentyp mit Korrekturregel ☐ als Dokumente gespeichert.

---

## PHASE 3 – Curriculum & detaillierter Plan

1. **Zeitmodell mastery-basiert rechnen (D7, D8):** Kapiteldauer aus dem Inhalt ableiten (Input, Üben, Test, erwartete Wiederholung), Leitner-Last **ohne Deckel** simulieren, daraus die **Gesamtdauer-Prognose** (Lernstunden und Plantage) je Tagespensum 1 / 1,5 / 1,75 / 2 h. Aufteilung begründen (Orientierung, keine Vorgabe: neuer Stoff ~55–60 %, Wiederholung ~20–25 %, Prüfungstraining/Simulationen ~15–20 %). **Realismus-Check** gegen gängige Richtwerte für Unterrichtseinheiten A1/A2 (ÖIF 500 h A1+A2) – Risiko offen benennen und Gegenmaßnahmen vorschlagen (z. B. zusätzliche Sprechpraxis in den kostenlosen ÖIF-Online-Kursen). Kürzen ist keine Gegenmaßnahme (D11).
2. **Kapitelstruktur:** Richtwert ~18–20 Kapitel A1 + ~18–20 Kapitel A2 (Anzahl begründen). Jedes Kapitel ≈ 3–4,5 h (D8-Qualität), verteilt auf 2–4 Tage je nach Tagespensum, mit drei Phasen: **Input** (Lektionen mit Audio) → **Üben** → **Kapiteltest** in allen Disziplinen.
   Zusätzlich: wöchentliche Wiederholungstage, **A1-Meilensteinprüfung**, A2-Simulation 1 + 2, finale A2-Generalprobe, offizieller Modelltest; **Austrittskriterien** „prüfungsreif“ (D11).
3. **Kapitel-Spezifikation** (je Kapitel): ID · Titel · Handlungsfeld · Can-Do-Ziele (IDs) · neuer Wortschatz (~30–45 Einheiten, IDs) · Grammatik · Redemittel · Werte-Thema · Prüfungsteil-Fokus · Aufgabenanzahl je Disziplin · geschätzte Dauer (aus dem Inhalt) · Voraussetzungen.
4. **Richtplan (relativ, ohne festes Ende):** je Tagespensum Plantag 1, 2, 3 … → Kapitel/Wiederholung/Simulation, inkl. **Puffer** für Kapitelwiederholungen nach verlorenen Leben und Review nach Simulationen. Keine festen Kalenderdaten – Tag 1 = Profilanlage (siehe Abschnitt 2). Dazu Prognoselogik „prüfungsreif ab ca. Tag X“ und Motivationsanker (Etappen, Tempo-Anzeige ohne Druck zum Kürzen).
5. **Freigabeplan (Just-in-time):** Reihenfolge der Content-Produktion so planen, dass die Lernende nie auf Inhalte wartet – Maßstab ist das **schnellste** zulässige Tempo (2 h/Tag). Start, sobald App + mindestens Kapitel A1-01 bis A1-05 fertig sind (empfohlen A1-01 bis A1-10); danach bleibt die Produktion der Lernenden mind. 1–2 Wochen (≈ 5 Kapitel) voraus. Meilenstein- und Simulations-Testsätze werden vor dem Ende des jeweiligen Niveaus fertiggestellt.
6. **Abdeckungsnachweis:** Matrix Lernziele / Wortschatz / Grammatik / Prüfungsaufgabentypen / **Prüfungskriterien** × Kapitel. Anforderung: 100 % Abdeckung; jede Prüfungs-Teilaufgabe vor der jeweiligen Simulation mindestens 3× geübt; Werte-Themen vollständig verteilt.

**Definition of Done Phase 3:** ☐ Gesamtdauer-Prognose rechnerisch geschlossen ☐ Abdeckung 100 % ☐ Richtplan mit Puffer und Meilensteinen ☐ Bestehenssicherheit mit Kriterien-Mapping und Austrittskriterien ☐ Risiken benannt ☐ als Dokument gespeichert.

---

## PHASE 4 – Spielregeln (verbindliche Spezifikation)

> **Status: abgeschlossen am 06.11.2026 (D14–D16).** Maßgeblich sind `04-spielregeln.md` (Simulation, Begründung), `04a-zustandsautomat.md` (Policy-Schicht, Zustandsmodell, Events, Automaten, normative Regeln R-…, Randfälle, Konstanten) und `04b-testfaelle.md` (Testfälle). Die Punkte unten sind der ursprüngliche Auftrag, ergänzt um die Festlegungen aus D14–D16.

Formuliere die Regeln als **Zustandsautomat** (Zustände, Events, Übergänge) und als testbare Regeln. **Lose gekoppelt (D16):** Regelentscheidungen liegen in einer austauschbaren `RulePolicy`; die folgenden Regeln sind die `defaultPolicy`.

1. **Freischaltung:** linear. Kapitel n+1 wird erst freigeschaltet, wenn Kapitel n **bestanden** ist. Bestanden = **alle Aufgaben in jeder Disziplin korrekt beantwortet** (ggf. über die Korrekturrunde).
2. **Kapiteltest:** enthält alle Disziplinen des Kapitels (Lesen, Hören, Schreiben, Sprechen, Grammatik/Wortschatz, Werte). Aufgaben werden **zufällig aus einem Pool** gezogen (Pool ≥ 2× Testgröße, mind. 60), damit Wiederholungen nicht auswendig gelernt werden. **D14:** 20 bewertete Aufgaben (3 je Disziplin + 2 Fokus) + 1 Pflicht-Sprechaufnahme ohne Leben; davor die **Testreife-Runde** (≥ 18/20 im Übungs-Pool).
3. **Leben:** Jeder Kapitelversuch startet mit **3 Leben** (+ Bonusleben, siehe 5). Jeder Fehler (= jede falsche Aufgabe) = −1 Leben.
   - **0 Leben** → Kapitel gescheitert → **Kapitel komplett wiederholen** (Lernteil + Test, neue Aufgabenauswahl, Leben zurückgesetzt auf 3 + Bonus des Kapitels). Der Wiederholungsplan ist als `RecoveryPlan` Teil der Policy (D16).
4. **Korrekturrunde:** Test beendet mit ≥ 1 Leben, aber mit Fehlern → alle falsch beantworteten Aufgaben werden **erneut abgefragt** – als **Zwillingsaufgabe** (gleiches Lernziel, andere Formulierung/Optionen), nicht als identische Kopie. Regel gemäß Entscheidung 1. Alle richtig → Kapitel bestanden.
5. **Bonusleben:** Kapitel **ohne Fehler** abgeschlossen → +1 Bonusleben gemäß Entscheidung 2 (D14: nur nach fehlerfreiem **erstem** Versuch).
6. **Erfolgsstreak:** (a) Serie aufeinanderfolgender richtiger Antworten (live sichtbar, mit persönlichem Rekord), (b) Serie perfekter Kapitel.
7. **Tagesstreak (Motivation):** zählt jeden Tag, an dem das Tagesziel (Entscheidung 4) erfüllt ist. Lokale Zeitzone, korrekte Mitternachtslogik, Kalender-Heatmap, Meilenstein-Badges (7/30/60/90 Tage). Streak-Freeze gemäß Entscheidung 3 (Freeze-Anzeige im Dashboard).
8. **Wiederholungsmechanismus:**
   - **Spaced Repetition (Leitner, 5 Fächer, Intervalle 1/3/7/14/30 Tage)** für Vokabeln, Grammatik-Items, Werte-Fakten und **jede je falsch beantwortete Aufgabe**. Entlastungen nach `03` Abschn. 2.2 (S2): passive Einträge ohne eigene Karte, Sets als eine Karte, im Kapiteltest richtig → Start in Fach 2. **Genus (D14):** keine eigene Spur, Richtungsrotation in der Nomenkarte, Fach 5 = Produktion mit Artikel.
   - **Tägliche Review-Queue vor neuem Stoff, ohne Minuten-Deckel (D7):** Die fällige Queue wird vollständig abgearbeitet; ist sie länger als das Tagespensum, ist der Tag ein Wiederholungstag. An Simulationstagen werden fällige Karten auf den Folgetag verschoben, nicht gestrichen.
   - **Wochenreview** mit gemischten Aufgaben aus allen bisherigen Kapiteln (Interleaving).
   - Vor einer Kapitelwiederholung: gezielte Review der Fehler aus dem gescheiterten Versuch.
9. **Meilensteine:**
   - **A1-Meilensteinprüfung** nach dem letzten A1-Kapitel: vollständige Simulation im Format der Integrationsprüfung A1 (Zeitlimits, Hörwiederholungsregeln wie in der echten Prüfung). Bestehen gemäß Entscheidung 6. Nicht bestanden → automatische Review der schwächsten Kapitel/Teile, danach neuer Versuch mit neuen Aufgaben. Bestanden → A2 freigeschaltet + Urkunde mit Namen (als Bild/PDF speichern).
   - Gleiche Logik für die A2-Simulationen und die finale Generalprobe; **Austrittskriterien „prüfungsreif“** (D11, `03` Abschn. 4.2) als eigener Zustand `READY_FOR_EXAM`, u. a. zwei aufeinanderfolgende A2-Simulationen ≥ 75 % je Teil.
10. **Frage-Chat und Prüfungsmodus:** Hilfe & Chat (Phase 6.3 und 6.6) folgen Entscheidung 7 – das gilt auch für den Kopier-Prompt-Button. Im gesperrten Zustand ist er sichtbar, aber deaktiviert („Nach dem Test kannst du fragen“). Fragen, die der Chat beantwortet, ändern nie Leben, Punkte oder Freischaltung. (D14: Test + Korrekturrunde sind eine gesperrte Einheit.)
11. **Fortschritt & Diagnose:** Kapitelpfad (Map), % je Disziplin, Schwächenanalyse nach Lernziel, „Tag X“ ab `startDate`, aktuelle Etappe, Tempo gegen das gewählte Tagespensum, Prognose „prüfungsreif ab ca. …“ aus dem tatsächlichen Tempo (Prognoselogik `03` Abschn. 3.3, Planminuten nach D15). Keine Rückstandsanzeige gegenüber einem Enddatum (D7).

**Definition of Done Phase 4:** ☑ Bestehens-Simulation zu Entscheidung 1 mit empfohlener Testlänge ☑ Zustandsautomat vollständig (inkl. Austrittskriterien) ☑ jede Regel als Testfall formuliert ☑ Randfälle (Abbruch mitten im Test, App-Neustart, Datumswechsel während einer Session) geklärt ☑ Regeln lose gekoppelt (D16).

---

## PHASE 5 – Content-Produktion

1. **Datenformat definieren und strikt einhalten** (JSON-Schema mitliefern):
   - `course.json` – Metadaten, Kapitelindex, Meilensteine, Version.
   - `chapter-XX.json` – Lektionen, Wortschatz, Grammatik, Item-Pool, Fragen & Antworten; mit `chapterId`, `version` (SemVer) und `schemaVersion`, damit Content-Packs per Upload sicher ersetzt/ergänzt werden können (Phase 6.4).
   - **Stabile IDs:** Item-, Vokabel- und Lernziel-IDs ändern sich nie (Fortschritt und Leitner-Daten hängen daran); Korrekturen erhöhen die `version`, neue Items bekommen neue IDs.
   - **Item-Felder:** `id`, `chapterId`, `level`, `skill` (`lesen|hoeren|schreiben|sprechen|grammatik|wortschatz|werte`), `examPart` (z. B. `A2-HOE-T2` oder `null`), `type`, `instruction` (`{ de, en, tl }`), `stimulus` (Text | Audio mit Skript und Sprecherrollen | Bildbeschreibung), `options`, `answer`, `acceptedVariants`, `explanation` (`{ de, en, tl }` – warum richtig, warum die Distraktoren falsch sind), `learningGoalIds`, `difficulty` (1–3), `twinIds`, `sourceIds` (bei Werte-Fakten), `reviewStatus` je Übersetzung (`machine` / `reviewed`), `varietyNote` (`{ de, en, tl }`, D10), `pool` (`practice` | `test`, D14).
   - **Vokabel-Felder** analog: `lemma`, `article`, `plural`, `pos`, `example`, `translations: { en, tl }`, `audio`, Varietät nach D10: `variety` (`AT` | `AT+DE` | `DE` | `AT-Institution`), `variantDe`, `mainFormId`, `varietyFeature`, `genusAt`/`genusDe`, `perfAux`, `pronAt` (`03` Abschn. 6.1).
2. **Mengengerüst je Kapitel** (Richtwert, D8, D14): 9–15 Mikro-Lektionen à 8–10 min (je ein Lernziel, Abruf am Ende) · Audio für 100 % des Wortschatzes und der Hörtexte nach **D13** (Geräte-TTS als Standard; Hörtexte im Prüfungsformat als kostenlos selbst erzeugte Dateien; kein kostenpflichtiges oder lizenzpflichtiges Audio) · **Test-Pool ≥ 60** · **Kapiteltest 20 Items** (3 je Disziplin + 2 Fokus, Aufgaben mit höchstens 3 Teilen) · **Übungs-Pool** mit genug automatisch korrigierbaren Items für Übungsteil (≈ 40) und mehrere Testreife-Blöcke à 20 (ohne Überschneidung mit dem Test-Pool) · für jedes Item mindestens 1 Zwillingsaufgabe, **für Test-Pool-Items mindestens 2** · ≥ 20 % Recycling-Items · ≥ 1 Sprechaufnahme. Prüfbare Mindestkriterien Q1–Q11: `03` Abschn. 5.
3. **Hören:** natürliche Skripte aus österreichischen Alltagssituationen (Mobilbox-Nachricht, Durchsage am Bahnhof, Radio-Wetter, Gespräch beim Arzt). Audio nach D13 (Hörtexte im Prüfungsformat als selbst erzeugte Dateien, sonst Geräte-TTS), Tempo stufenweise bis zum Sprechtempo der Modelltests steigern (L15). Wiedergaberegeln wie in der Prüfung (1× bzw. 2× hören).
4. **Lesen:** Textsorten wie in der Prüfung (Anzeigen, Schilder, Infotexte, E-Mails, Formulare). Max. ~5 % unbekannte Wörter je Text (außer bei gezieltem Globalverstehen) – als **Obergrenze**; Beleg offen (L21, `04` K7).
5. **Schreiben:** auto-korrigierbare Vorstufen (Lücken, Satzbau, Anrede/Gruß wählen, Leitpunkte zuordnen) + freie Aufgabe mit 3 Leitpunkten. Bewertungsraster orientiert an den offiziellen Kriterien. Bewertung gemäß Entscheidung 5; regelbasiert prüfbar sind mindestens: Anrede, Gruß, Mindestwortzahl, Abdeckung jedes Leitpunkts über Schlüsselbegriffe (im Kapiteltest ergänzt durch Zuordnung Leitpunkt → eigener Satz, `04a` R-T7).
6. **Sprechen:** Aufgaben wie in der Prüfung (sich vorstellen, Bild/Situation beschreiben, Dialog spielen, über die eigene Situation sprechen).
   - Objektiv prüfbare Vorstufen zählen für „alle richtig“ (Redemittel auswählen, Dialoglücken, gesprochene Sätze per Spracherkennung mit Schlüsselwort-Abgleich, wo verfügbar).
   - Freie Sprechaufgabe ist Pflicht: Aufnahme → Anhören → Musterantwort → Checkliste.
   - Im Tool klar kommunizieren, dass echte Sprechpraxis zusätzlich nötig ist (Link auf kostenlose ÖIF-Online-Kursräume; feste Empfehlung nach D11).
7. **Werte- und Orientierungswissen:** Lernkarten + Prüfungsformat-Aufgaben; jeder Fakt mit Quelle und Stand; neutrale, respektvolle Formulierung.
8. **Fragen & Antworten je Kapitel** (Fallback für den Frage-Chat): 8–15 typische Lernendenfragen mit kurzer Antwort in `{ de, en, tl }`, verknüpft mit Lernziel-IDs.
9. **QA-Checkliste pro Kapitel:** Niveau passend (nur bekannter Wortschatz + geplante neue Wörter) · genau eine eindeutig richtige Antwort · plausible Distraktoren · Austriazismen korrekt, DE-Formen gekennzeichnet (D10) · Rechtschreibung · keine Stereotype · keine urheberrechtlich übernommenen Texte · Werte-Fakten belegt · jedes Lernziel des Kapitels abgedeckt · Qualitätskriterien Q1–Q11 (D8) · `en`- und `tl`-Felder vollständig, Übersetzung sinngleich und verständlich, `reviewStatus` gesetzt.
10. **Produktion in Batches:** max. 2 Kapitel pro Durchgang (in Claude Code direkt als `content/chapter-XX.json`) → automatische QA → Prüfer-Agent → QA-Bericht → STOP.
11. **Automatische QA als Code (`scripts/qa/`, läuft bei jedem Batch und in CI, muss grün sein):**
   - Schema gültig; IDs eindeutig und stabil; `version` erhöht bei Änderungen
   - jedes Item hat ≥ 1 Zwilling, Test-Pool-Items ≥ 2; `answer` ist in `options` enthalten; genau eine richtige Option
   - Mengengerüst je Kapitel (Test-Pool ≥ 60, Kapiteltest 20 nach D14 ziehbar, ≥ 3 Items je Disziplin, Übungs-Pool reicht für Übungsteil + ≥ 2 Testreife-Blöcke ohne Überschneidung mit dem Test-Pool, Mikro-Lektionen, Audio vorhanden)
   - **Wortschatz-Check:** jedes Wort in Stimulus/Optionen ist im Inventar bis einschließlich dieses Kapitels enthalten (Lemmatisierung bzw. Formenliste; Eigennamen/Zahlen per Ausnahmeliste) → maschinelle Prüfung der Regel „nur eingeführter Wortschatz“
   - jedes Lernziel des Kapitels von ≥ 1 Item abgedeckt; jede Prüfungs-Teilaufgabe vor der Simulation ≥ 3× geübt (kumulativ)
   - `de`/`en`/`tl` vollständig; `reviewStatus` gesetzt; Werte-Items haben `sourceIds`
   - **Varietät (`variety.py`, D10):** bundesdeutsche Formen (z. B. „Januar“, „Kartoffel“, „Tüte“) in Lerntexten nur mit Kennzeichnung; im Prüfungsmodus nie in Stimulus/Optionen; Perfekt sitzen/stehen/liegen mit *sein*; Genus gegen `genusAt` (`03` Abschn. 6.3)
12. **Prüfer-Agent je Batch:** Ein separater Agent mit frischem Kontext (kennt nur Spezifikation, Inventar und das neue Kapitel, nicht den Entstehungsprozess) prüft eine Stichprobe von mind. 20 % der Items auf Eindeutigkeit, Niveau, sachliche Richtigkeit, Natürlichkeit im österreichischen Alltag, Qualität nach D8 und Übersetzungsqualität. Ergebnis: Liste der Auffälligkeiten mit Item-ID und Vorschlag. Der Mensch prüft nur die Auffälligkeiten + eine kleine eigene Stichprobe.
13. **Menschliche Freigabe:** Ein Kapitel wird erst nach Freigabe durch den Betreiber veröffentlicht. Tagalog-Stichproben nach Möglichkeit durch eine Person mit Tagalog als Muttersprache.

---

## PHASE 6 – Technische Umsetzung (Claude Code)

> Diese Phase läuft in **Claude Code** im Repo `lauhard/speakaustrian` mit dem Ticket-Workflow aus D17d. Entwickelt wird immer im Repo (TypeScript, Tests, Schema-Validierung); **ausgeliefert** wird ein statischer Build – zuerst als **Claude-Artifact**, später optional als **eigene Web-App**. Es ist derselbe Code.

### 6.1 Auslieferungsstufen (Entscheidung vom 05.11.2026)

| | **Stufe 1: Artifact (Start)** | **Stufe 2: eigene Web-App (optional, später)** |
|---|---|---|
| Hosting | claude.ai, teilbarer Link, keine Kosten | Cloudflare, eigene Domain |
| Zugang für Dritte | Link öffnen + Namen eingeben (Freigabe über das Share-Menü; per Gerätecheck verifizieren) | Link + Name |
| KI-Chat / KI-Feedback | direkt nur für Personen mit Claude-Account (auf deren Kontingent); für alle: „Frage an eine KI kopieren“ + Offline-Hilfe | für alle über eigenen Worker (API-Key des Betreibers) |
| Offline / installierbar | nein (keine Service Worker) – Lesezeichen am Startbildschirm | ja (PWA) |
| Mikrofon | nein (im Artifact gesperrt) – Aufnahme per Datei-Upload | ja |
| Fortschritt speichern | lokal (localStorage/IndexedDB), bleibt bei Updates unter derselben URL erhalten | lokal |
| Export | Datei speichern über die Download-Funktion (mit Bestätigung, falls verfügbar), sonst kopieren/einfügen | Datei-Download |
| Upload Lernteile / Import | ja (Datei-Auswahl, Einfügen) | ja |
| Recht | Hosting bei Anthropic | Impressum + Datenschutzerklärung nötig |

**Wechselkriterium zu Stufe 2:** Wenn der KI-Chat für Lernende ohne Claude-Account wichtig wird, wenn Offline-Nutzung gebraucht wird oder wenn mehr Personen das Tool nutzen, als sich per Kopier-Prompt gut betreuen lassen.

**Gerätecheck:** Vor Beginn von Phase 6 die Ergebnisse des Test-Artifacts „Weg zur A2 Gerätecheck“ auswerten (mind. ein Smartphone ohne claude.ai-Login, ein Smartphone/Desktop mit Login). Abweichungen von dieser Tabelle hier nachtragen.

### 6.2 Stack

- **SvelteKit** mit `adapter-static` (bzw. Vite + Svelte), TypeScript. Build-Ausgabe: eine Seite + JS-/CSS-Dateien + `content/*.json` – passt sowohl ins Artifact (Mehrdatei-Veröffentlichung, relative Pfade) als auch auf Cloudflare.
- **Artifact-Regeln beim Build beachten:** keine externen Requests außer erlaubten CDN-Skripten und Google Fonts; Inhalte per relativem `fetch` aus den mitveröffentlichten Dateien; kein `alert/confirm/prompt` (eigene Dialoge); Links nach außen als echte `<a href>`; Größenlimits (16 MB je Datei).
- **Spiellogik `src/lib/core`:** reine Funktionen – `makeReducer(policy)` → `reducer(state, event) → state` (D16: Mechanik im Kern, Regelentscheidungen in `src/lib/core/policies/default.ts`), Leitner-Scheduler, Streak- und Plantag-Berechnung, Prognose, Testzusammenstellung mit injizierbarem Zufallsgenerator. Keine Seiteneffekte. Zustandsmodell, Events und Konstanten: `04a`.
- **Validierung:** `zod`-Schemas für `course.json`, `chapter-XX.json`, Content-Packs und Fortschritts-Export (inkl. `ruleset` und `overrides`, D16) – dieselben Schemas für Build-Check, Upload und Import.
- **Tests:** Vitest (Core inkl. `04b` und Policy-Naht-Tests, Schemas, QA-Skripte), Property-based Tests für die Invarianten (`04b` Abschn. 13), Playwright für 2–3 Kernabläufe.

### 6.3 Adapter-Architektur (Ports & Adapters)

Die Spiellogik kennt nur Schnittstellen, nie die Plattform. Je Auslieferungsstufe wird die passende Implementierung eingesetzt.

| Port | Stufe 1 (Artifact) | Stufe 2 (Web-App) |
|---|---|---|
| `TutorPort.ask(context) → answer` | 1. Claude im Viewer (falls verfügbar und erlaubt) → 2. „Frage an eine KI kopieren“ → 3. Offline-Hilfe (Fragen & Antworten) | eigener Worker `/api/chat` → Offline-Hilfe |
| `FeedbackPort.rate(text, rubric)` | Claude im Viewer → regelbasiert + Musterlösung + Selbstcheck + „Feedback holen“-Kopier-Prompt | Worker `/api/feedback` → regelbasiert |
| `StoragePort` | localStorage + IndexedDB | gleich |
| `FileOutPort.save(name, data)` | Download-Funktion des Viewers (mit Bestätigung) → Fallback „kopieren“ | normaler Download |
| `FileInPort` | Datei-Auswahl + Einfügen aus Zwischenablage | gleich |
| `SpeechInPort` | Audio-Datei hochladen (`<input type=file accept="audio/*" capture>`) + Anhören + Checkliste | Mikrofon + `SpeechRecognition` |
| `SpeechOutPort` | `speechSynthesis` (de-AT bevorzugt, gehärtet nach Prototyp v4: eine Äußerung je Aufruf, Watchdog, Reset) für Wortschatz und Übungen · kostenlos selbst erzeugte Audiodateien (`<audio>`) für Hörtexte im Prüfungsformat (D13) · Transkript als Rückfall | gleich |

**Kopier-Prompt (Kern des Chat-Ersatzes in Stufe 1):** Ein Klick kopiert einen vollständigen Prompt in die Zwischenablage – Tutor-Rolle, Niveau, Antwortsprache (`en`/`tl` + einfaches Deutsch), Aufgabe, eigene Antwort, richtige Antwort, Kurs-Erklärung, eigene Frage. Darunter Links zu kostenlosen KI-Chats. In gesperrten Modi (Entscheidung 7) ist der Button deaktiviert.

### 6.4 Profile, Speicherung, Export, Upload

- **Profil:** „Wie heißt du?“ → `name`, `startDate` (Plantag 1), Tagespensum, Sprache (`en`/`tl`). Mehrere Profile pro Gerät. Kein Login.
- **Speicher:** localStorage (Profilindex, Einstellungen) + IndexedDB (Fortschritt, Leitner, Chatverläufe, hochgeladene Inhalte). Jeder Zugriff abgesichert; Fallback in-memory mit Warnbanner. Schema-Version + Migrationsfunktionen. Autosave nach jeder Antwort, Wiederaufnahme mitten im Test.
- **Export:** über `FileOutPort` als JSON (`weg-zur-a2_<name>_<datum>.json`); wöchentliche Backup-Erinnerung; klarer Hinweis, dass Fortschritt nur in diesem Browser auf diesem Gerät liegt.
- **Import:** Datei wählen oder JSON einfügen → Schema-Prüfung → Vorschau → übernehmen.
- **Upload von Lernteilen (Content-Packs):** Datei(en) wählen → Schema-Prüfung → Vorschau (Kapitel, Itemzahl, Version) → in IndexedDB. Gleiche Kapitel-ID: höhere `version` gewinnt; Original wiederherstellbar; verständliche Fehlermeldungen (welche Datei, welches Item, welches Feld). Fortschritt hängt an stabilen IDs und bleibt erhalten.
- **Offizielle Inhalte** werden mit der App veröffentlicht (`content/*.json`) und per Neuveröffentlichung unter derselben URL aktualisiert – der Fortschritt der Lernenden bleibt dabei erhalten.

### 6.5 Stufe 2: Server-Endpunkt (nur bei Wechsel)

- Cloudflare Worker: `POST /api/chat`, `POST /api/feedback`; Claude API mit API-Key als Secret; Modell konfigurierbar (günstige Klasse als Default; Modellnamen/Preise beim Wechsel recherchieren).
- System-Prompt nur auf dem Server; der Client schickt nur strukturierte Felder (Frage, Kapitel-ID, Item-ID, Sprache, gekürzter Verlauf).
- Pflicht-Schutz: Bot-Schutz (Turnstile), Rate-Limit pro Gerät/IP, Längenlimits, Monatsbudget mit Not-Aus (Spend-Limit in der Anthropic Console + Zähler), Themenbindung.
- Impressum und Datenschutzerklärung (Entwürfe durch Claude, Prüfung durch den Betreiber).

### 6.6 Tutor-Verhalten (alle Stufen)

Antwortet in einfachem Deutsch (A1/A2) mit Übersetzung in die gewählte Sprache; erklärt das Warum mit eigenem Beispiel; österreichisches Standarddeutsch (DE-Formen gekennzeichnet, D10); bleibt beim Thema; erfindet keine Prüfungsregeln oder Werte-Fakten, verweist auf die Kursquelle. Gesperrt gemäß Entscheidung 7. Hinweis: „Keine persönlichen Daten eingeben.“

### 6.7 UX & Screens

- Mobile first · große Touch-Ziele · Umlaut-Tasten (ä ö ü ß) · Sprachumschaltung Deutsch / English / Tagalog (auch UI) · Dark Mode · Barrierefreiheit (Kontrast, Tastatur, `aria-live`) · ruhige Animationen · Ton erst nach Interaktion (Browser-Regel).
- **Screens:** Profil/Onboarding (inkl. Wahl des Tagespensums mit Prognose) · Dashboard (Tag X, Etappe, Prognose „prüfungsreif ab ca. …“, Tagesziel, Tagesstreak inkl. Freeze, Erfolgsstreak, Leben, fällige Wiederholungen) · Kapitelpfad · Lektion · Testreife-Runde · Kapiteltest · Korrekturrunde · Ergebnis · Wiederholung · Meilensteinprüfung · Statistik/Schwächen · Hilfe & Chat (Panel aus jedem erlaubten Screen) · Ressourcen (Links zu offiziellen Modelltests, ÖIF-Angeboten) · Einstellungen (Export/Import, Upload Lernteile, Profil löschen, Sprache, Audio, Tagespensum).
- **Kein Drucken im Artifact:** Urkunde nach Meilensteinen als Bild/PDF über `FileOutPort` speichern statt drucken.
- **Anti-Frust ohne Regelaufweichung:** Erklärung nach jedem Fehler, Chat-/Kopier-Button nach dem Feedback, Testreife-Runde vor dem Test, gezielte Review vor Kapitelwiederholung; kein Verlust-Alarm bei gebrochenem Streak (`04a` R-S7); keine Rückstandsanzeige gegenüber einem Enddatum (D7).

### 6.8 Repo-Struktur

```
speakaustrian/
├─ CLAUDE.md              # rules for Claude Code (from project instructions + section 1)
├─ docs/                  # INDEX.md, spec/ (docs from the Claude project), tickets/, spec-gaps.md
├─ content/               # course.json, chapter-XX.json, schemas/, audio/
├─ scripts/qa/            # automated content QA (see Phase 5.11)
├─ scripts/plan/          # planning model (03e, 03e2, 04c)
├─ src/lib/core/          # pure game mechanics (reducer, scheduler, streaks, forecast)
├─ src/lib/core/policies/ # rule policies (D16): default.ts now, further policies later
├─ src/lib/ports/         # port interfaces
├─ src/lib/adapters/      # artifact/*, web/*, offline/*
├─ src/routes/            # UI screens
├─ worker/                # stage 2 only
└─ tests/
```

**Definition of Done Phase 6:** ☐ Gerätecheck ausgewertet ☐ App als Artifact veröffentlicht, Link für Dritte freigegeben und getestet ☐ Namenseingabe, Fortschritt lokal, Export/Import ☐ Upload von Content-Packs mit Validierung ☐ Hilfe/Chat in allen drei Stufen (Viewer-Claude, Kopier-Prompt, Offline) ☐ Adapter so geschnitten, dass Stufe 2 ohne Änderung am Core möglich ist ☐ Regeln nur in Policies, Kern ohne Regelentscheidung (D16, `04a` R-PL1) ☐ alle Tests grün.

---

## PHASE 7 – Test & Abnahme

1. **Logiktests:** alle Testfälle aus `04b` (gegen `defaultPolicy`) + Invarianten als Property-based Tests + Policy-Naht-Tests (`04b` Abschn. 13a, D16). Darin enthalten: Leben, Bonusleben-Cap, Testreife, Korrekturrunde (Variante A), Streak-Freeze, Kapitel-Reset, Freischaltung, Austrittskriterien, Tagesstreak über Mitternacht und Zeitzonenwechsel, Plantag-Berechnung ab `startDate` (inkl. Export/Import auf ein anderes Gerät), Prognose, Chat-/Kopier-Sperre in allen Testmodi, App vollständig nutzbar ohne KI (alle `TutorPort`-Stufen inkl. Fallback), Upload ungültiger Content-Packs wird abgelehnt, Upload gültiger Packs bewahrt Fortschritt, Fortschritt übersteht Neuveröffentlichung des Artifacts; Stufe 2 zusätzlich: Worker-Limits greifen, Leitner-Intervalle, Speicher-Migration, Export → Import Roundtrip.
2. **Inhaltsaudit:** Stichprobe von 10 % der Items in einem **frischen Kontext** unabhängig prüfen (Niveau, Eindeutigkeit, Korrektheit, Austriazismen und DE-Kennzeichnung, Werte-Fakten, Qualität nach D8, Qualität der `en`-/`tl`-Übersetzungen).
3. **Pilot:** Kapitel 1 mit einer echten Lernenden (Englisch oder Tagalog) vollständig durchspielen, tatsächliche Dauer gegen das Zeitmodell (`03` Abschn. 2.1, D15) messen, Testreife-Ergebnis gegen Testergebnis vergleichen (`04c`), Kalibrierfaktor setzen und Richtplan/Prognose anpassen.
4. **Abnahmekriterien:** alle Logiktests grün · Abdeckungsmatrix 100 % · jedes Kapitel hat bestandenen QA-Bericht · Link für Dritte ohne Login getestet (Smartphone + Desktop) · Hilfe/Chat ohne Claude-Account über Kopier-Prompt und Offline-Hilfe nutzbar · Stufe 2: offline-fähig, API-Kosten mit Budget-Grenze abgesichert · Fortschritt übersteht Neuladen und Export/Import.

---

## Start

- Bearbeite die Phase bzw. den Content-Batch, der in der **Chat-Nachricht** genannt wird (z. B. „Arbeite Phase 2 ab“).
- Phasen 1–4: im Claude-Projekt. Phasen 5–7: in Claude Code im Repo (siehe Abschnitt 1, „Werkzeuge je Phase“).
- Ohne Angabe: Prüfe das Projektwissen (`01-…`, `02-…`) und bearbeite die **nächste offene Phase**. Nenne zu Beginn kurz, welche Phase du bearbeitest und auf welchen Dokumenten du aufbaust.
- Keine Phase überspringen: Fehlt das Ergebnis einer vorausgehenden Phase im Projektwissen, sag das und schlag vor, zuerst diese abzuschließen.
- Stelle vorher **maximal 3 Rückfragen**, nur wenn für die aktuelle Phase etwas unklar ist. Halte dich an die STOP-Punkte.
