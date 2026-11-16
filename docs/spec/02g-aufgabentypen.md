# 02g – Aufgabentyp-Katalog (Phase 2.7)

> **Projekt:** „Weg zur A2“ · **Phase:** 2 · **Stand:** 05.11.2026
> **Grundlage:** `claude/00-masterprompt.md` Phase 2.7, Entscheidungen 1, 5, 7 · Prüfungsspezifikation `01-ressourcen.md` Abschn. 2 (Q05, Q06, Q09, Q10) · Can-Do `02a`, Redemittel `02e`
> **Zweck:** Jede Prüfungs-Teilaufgabe hat einen nachgebauten Aufgabentyp mit Korrekturregel; dazu die vorbereitenden Übungstypen. Die Korrekturregeln sind so formuliert, dass sie in Phase 6 als **reine Funktionen** (`src/lib/core/grading/*`) umgesetzt werden können.

---

## 1. Prüfungsaufgabentypen (exakter Nachbau)

**Gemeinsame Regeln im Prüfungsmodus:** nur Deutsch (keine `en`/`tl` bis zum Feedback) · Frage-Chat und Kopier-Prompt gesperrt (Entscheidung 7) · Zeitlimit und Hörhäufigkeit wie in der Prüfung · Audio nicht pausierbar, keine Zusatzwiederholung (Q05) · Antworten werden wie auf dem Antwortbogen erst am Ende gewertet (Simulation) bzw. sofort (Kapiteltest).

### 1.1 Integrationsprüfung A1 (Meilenstein 1)

| examPart | Aufgabentyp-ID | Items | Interaktion | Optionen | Stimulus | Hören | Zeit | Punkte (je Item) | Korrekturregel | Lernziele |
|---|---|---|---|---|---|---|---|---|---|---|
| A1-SB-T1 | `EX-A1-SB` Sprachbausteine | 10 | Lücke im Text, Auswahl | 2 (a/b) | 2 kurze Mitteilungen | – | 10 min | 6 | exakter Optionsvergleich | A1-LES-03, G-Themen |
| A1-HOE-T1 | `EX-A1-HOE1` | 4 | Richtig/Falsch | 2 | kurze Alltagstexte mit Situationsangabe (Mobilbox, Arzt, Durchsage) | 2× | Teil von ca. 15 min | 12 | exakter Vergleich | A1-HOE-04/05/09 |
| A1-HOE-T2 | `EX-A1-HOE2` | 5 | MC | 2 (a/b) | Frage-Antwort-Dialoge mit Zahl/Buchstaben | 2× | ″ | 4 | exakter Vergleich | A1-HOE-02/03 |
| A1-HUA-T1 | `EX-A1-HUA1` | 3 | Reaktion zuordnen | 4 (a–d) | kurze Äußerung (Audio) | 2× | ″ | 8 | exakter Vergleich; jede Option höchstens einmal | A1-HOE-06/07 |
| A1-HUA-T2 | `EX-A1-HUA2` | 4 | Reaktion zuordnen | 5 (e–i) | ″ | 2× | ″ | 8 | ″ | A1-HOE-06/07 |
| A1-LES-T1 | `EX-A1-LES1` | 3 | Überschrift zuordnen | 4 (1 Distraktor) | 3 Kurzmeldungen | – | Teil von 45 min | 12 | exakter Vergleich | A1-LES-04 |
| A1-LES-T2 | `EX-A1-LES2` | 3 | Richtig/Falsch | 2 | E-Mail | – | ″ | 12 | ″ | A1-LES-03 |
| A1-LES-T3 | `EX-A1-LES3` | 3 | passende Anzeige wählen | 2 (a/b) | je 2 Anzeigen/Aushänge | – | ″ | 8 | ″ | A1-LES-01/02/07 |
| A1-SCH-T1 | `EX-A1-FORM` | 5 | Formularfeld ausfüllen (Freitext) | – | Kurztext + Formular | – | ≥ 15 min (mit T2) | 2 | **Feldregel** (Abschn. 3.3): Eigennamen und Zahlen **T0 exakt**, übrige Felder T1+T2+T3 | A1-SCH-01/02 |
| A1-SCH-T2 | `EX-A1-NACHRICHT` | 1 | freier Text ca. 30 Wörter, 3 Leitpunkte, informell | – | Situationsbeschreibung | – | ″ | 30 = 3 × (8/4/0) + 6/3/0 | **regelbasiert + Selbstcheck + KI-Feedback** (Abschn. 3.4) | A1-SCH-03/04 |
| A1-SPR-T1 | `EX-A1-SPR1` | 1 Block | Vorstellen nach Stichwörtern + Buchstabieren + Zahl | – | Stichwortkarte | – | ca. 3 min | 24 | Aufnahme + Checkliste (Abschn. 3.5) | A1-SPR-01–03 |
| A1-SPR-T2 | `EX-A1-SPR2` | 2 Runden | Frage zur Wortkarte stellen + antworten | – | Thema + Wortkarte | – | ca. 4 min | 28 | Vorstufe auto (Fragesatz bauen), Endstufe Checkliste | A1-SPR-04 |
| A1-SPR-T3 | `EX-A1-SPR3` | 2 Runden | Bitte/Vorschlag formulieren + reagieren | – | Bild-/Handlungskarte | – | ca. 4 min | 28 | ″ | A1-SPR-05/06 |
| A1-WOW-T1 | `EX-WOW-AB` | 9 | Entscheidungsfrage | 2 (a/b) | Aussage/Frage | – | 40 min gesamt | 2 | exakter Vergleich | A1-WOW-* |
| A1-WOW-T2 | `EX-WOW-ABC` | 9 | Single Choice | 3 (a/b/c) | Frage | – | ″ | 3 | ″ | A1-WOW-* |

**Gruppenprüfung A1 (Sprechen):** Die echte Prüfung ist eine Gruppenprüfung. Im Tool wird der Partner simuliert (vorgegebene Partnerfrage per Audio, eigene Antwort als Aufnahme). Hinweis an Lernende: Sprechpraxis mit Menschen im ÖIF-Kursraum (Q40/Q42).

### 1.2 Integrationsprüfung A2 (Prüfungsziel)

| examPart | Aufgabentyp-ID | Items | Interaktion | Optionen | Stimulus | Hören | Zeit | Punkte (je Item) | Korrekturregel | Lernziele |
|---|---|---|---|---|---|---|---|---|---|---|
| A2-LES-T1 | `EX-A2-LES1` | 3 | Person → Anzeige zuordnen | 6 (a–f), 3 Distraktoren | 6 Kurzanzeigen | – | Teil von 40 min | 1 | exakter Vergleich, jede Anzeige höchstens einmal | A2-LES-01 |
| A2-LES-T2 | `EX-A2-LES2` | 4 | MC | 3 (a/b/c) | 4 Kurztexte | – | ″ | 1 | ″ | A2-LES-02/03 |
| A2-LES-T3 | `EX-A2-LES3` | 8 | Formularlücke per MC | 3 (a/b/c) | Formular + 2–3 Kurztexte/Karten | – | ″ | 1 | ″; **Distraktor-Regeln** (Abschn. 2.2) | A2-LES-04/05 |
| A2-LES-T4 | `EX-A2-LES4` | 5 | Satzergänzung MC | 3 (a/b/c) | 1 längerer Infotext | – | ″ | 1 | ″ | A2-LES-06/07/09/10 |
| A2-HOE-T1 | `EX-A2-HOE1` | 7 | Notizzettel-Lücke MC | 3 (a/b/c) | 1 Mobilbox-Nachricht (mit Buchstabieren, Ziffern) | 2× | 30 s Lesezeit | 2 | ″ | A2-HOE-01/02 |
| A2-HOE-T2 | `EX-A2-HOE2` | 2 | MC | 3 (a/b/c) | 2 Mobilbox-Nachrichten | 2× | 30 s | 2 | ″ | A2-HOE-03 |
| A2-HOE-T3 | `EX-A2-HOE3` | 3 | MC | 3 (a/b/c) | Radio-Meldung, Durchsage, Bandansage | **1×** | 30 s | 2 | ″ | A2-HOE-04–06 |
| A2-HOE-T4 | `EX-A2-HOE4` | 3 | Richtig/Falsch | 2 | 3 Alltagsgespräche | **1×** | 30 s | 2 | ″ | A2-HOE-07 |
| A2-SCH-T1 | `EX-A2-EMAIL` | 1 (Wahl aus 2 Themen) | freier Text ca. 50 Wörter, 3 Leitpunkte, überw. formell | – | Situation + Leitpunkte | – | 25 min | 20 | **regelbasiert + Selbstcheck + KI-Feedback** (Abschn. 3.4) | A2-SCH-01–06, -09 |
| A2-SPR-T1 | `EX-A2-KONTAKT` | 1 | Vorstellen nach Impulswörtern + eigene Fragen bei markierten Impulsen | – | Impulskarte | – | Teil von ca. 10 min | ┐ | Aufnahme + Checkliste | A2-SPR-01/02 |
| A2-SPR-T2A | `EX-A2-BILD` | 1 | Bild wählen (3 aus 5), Situation beschreiben, Rollenspiel mit ≥ 2 eigenen Fragen | – | Bildkarte + Situationskärtchen | – | ″ | ├ 30 gesamt `[Verteilung UNVERIFIZIERT, L2]` | Vorstufen auto (Fragen bilden), Endstufe Checkliste | A2-SPR-03/04, -07–-16 |
| A2-SPR-T2B | `EX-A2-GESPRAECH` | 1 | über eigene Erfahrung sprechen, vergleichen | – | Rückseite Bildkarte (Sprechblasen) | – | ″ | ┘ | Aufnahme + Checkliste | A2-SPR-05/06 |
| A2-WOW-T1 | `EX-WOW-AB` | 9 | Entscheidungsfrage | 2 (a/b) | Aussage/Frage | – | 40 min gesamt | 2 | exakter Vergleich | A2-WOW-* |
| A2-WOW-T2 | `EX-WOW-ABC` | 9 | Single Choice | 3 (a/b/c) | Frage | – | ″ | 3 | ″ | A2-WOW-* |

**Testzusammenstellung WOW (Simulation):** mindestens 1 Frage je Wertebereich W0–W6, Zwillinge nie im selben Testsatz (Q09/Q10).

## 2. Konstruktionsregeln für Prüfungsitems

### 2.1 Allgemein

- Genau **eine** eindeutig richtige Option; Distraktoren plausibel und im Text/Audio erwähnt (Distraktor-Typ wird im Item gespeichert: `mentioned-but-wrong`, `similar-number`, `similar-spelling`, `opposite`, `wrong-person`, `wrong-time`).
- Wortschatz nur bis zum aktuellen Kapitel (Inventar `02c`), max. 5 % unbekannte Wörter je Lese-/Hörtext (Q98).
- Hörskripte: österreichischer Standard, TTS `de-AT`, Tempo 0,8 → 1,0 (Masterprompt 5.3); Rollen und Pausen im Skript markiert.

### 2.2 Distraktor-Regeln A2-LES-T3 (Formular) und A2-HOE-T1 (Notizzettel)

Abgeleitet aus dem Format (Q05), eigene Ausgestaltung:

| Datentyp | Richtige Option | Distraktor 1 | Distraktor 2 |
|---|---|---|---|
| Name | `Reyes` | Buchstabendreher (`Reyse`) | ähnlich klingend (`Reis`) |
| Datum | `03.05.1990` | Tag/Monat vertauscht (`05.03.1990`) | Jahr aus anderem Datum im Text |
| Telefonnummer | `0664 123 45 78` | zwei Ziffern vertauscht | Nummer einer anderen Person im Text |
| Straße/Nr. | `Grazer Straße 12` | Nummer aus anderem Kontext (`21`) | ähnliche Straße (`Grabenstraße`) |
| Umlaut | `Müller` | `Muller` | `Mühler` |

## 3. Korrekturregeln (Auto-Korrektur)

### 3.1 Toleranzstufen

| Stufe | Name | Regel | Einsatz |
|---|---|---|---|
| T0 | exakt | Zeichenfolge identisch nach Trim und Mehrfach-Leerzeichen-Reduktion | Eigennamen, Zahlen, Daten, Telefonnummern (Prüfungsregel A1-SCH-T1: keine Fehlertoleranz, Q06) |
| T1 | Umlaut-Ersatz | `ae→ä, oe→ö, ue→ü, ss→ß` akzeptiert (beidseitig normalisiert) | alle Freitext-Eingaben außer T0-Felder |
| T2 | Groß/klein tolerant | Vergleich case-insensitiv | **nicht** bei Lernzielen zur Nomen-Großschreibung (G06, G48) – dort Groß/klein Pflicht |
| T3 | Tippfehler-Distanz | Damerau-Levenshtein ≤ 1 bei Wortlänge 5–8, ≤ 2 bei ≥ 9; bei < 5 Zeichen keine Toleranz | Wortschatz-Eingaben, Diktat; **nicht** bei Grammatik-Drills, wenn der Unterschied die Zielform ist (z. B. `den` vs. `dem`) |
| T4 | Variantenliste | `acceptedVariants` aus dem Item (z. B. `Jänner`/`Januar`, `Erdäpfel`/`Kartoffeln`, Zahlwort/Ziffer) | alle Typen |

**Regel „Zielform schlägt Toleranz“:** Ist die geprüfte Form genau das Lernziel (Endung, Artikel, Umlaut im Plural), wird T3 für diesen Teil abgeschaltet. Umsetzung: Item-Feld `strictTokens: [...]`.

**Bundesdeutsche Form:** wird akzeptiert (T4), Feedback zeigt die österreichische Hauptform („Richtig! In Österreich sagt man meistens *Jänner*.“). Im Prüfungsmodus zählt sie als richtig, sofern sie in `acceptedVariants` steht.

### 3.2 Normalisierung als reine Funktion (Skizze für Phase 6)

```ts
// Pure normalization pipeline; tolerance flags come from the item definition.
type Tolerance = { umlaut: boolean; caseInsensitive: boolean; typoDistance: 0 | 1 | 2 };

const collapse = (s: string): string => s.trim().replace(/\s+/g, " ");
const foldUmlauts = (s: string): string =>
  s.replace(/ä/g, "ae").replace(/ö/g, "oe").replace(/ü/g, "ue")
   .replace(/Ä/g, "Ae").replace(/Ö/g, "Oe").replace(/Ü/g, "Ue").replace(/ß/g, "ss");

export const normalize = (t: Tolerance) => (s: string): string =>
  [collapse, t.umlaut ? foldUmlauts : (x: string) => x, t.caseInsensitive ? (x: string) => x.toLowerCase() : (x: string) => x]
    .reduce((acc, f) => f(acc), s);

export const isCorrect = (t: Tolerance, accepted: readonly string[], input: string): boolean => {
  const n = normalize(t);
  const given = n(input);
  return accepted.some(a => {
    const target = n(a);
    return given === target || (t.typoDistance > 0 && damerauLevenshtein(given, target) <= t.typoDistance);
  });
};
```

### 3.3 Formular-Feldregel (`EX-A1-FORM`, `UE-FORMULAR`)

| Feldtyp | Toleranz | Begründung |
|---|---|---|
| Vorname, Familienname, Straßenname, Ortsname | T0 (+ Groß/klein Pflicht) | Prüfungsregel „Eigennamen ohne Fehlertoleranz“ (Q06) |
| Datum | T0 auf normalisiertes Datum: `3.5.1990`, `03.05.1990` beide gültig; Reihenfolge TT.MM.JJJJ Pflicht | österr. Datumsformat |
| Zahlen (PLZ, Hausnr., Tel.) | T0 nach Entfernen von Leerzeichen | Q06 |
| Freitextfeld (Beruf, Familienstand) | T1 + T2 + T3 | Rechtschreibung tolerant (Q06) |
| Auswahlfeld (männlich/weiblich, ja/nein) | exakt | – |

### 3.4 Schreiben frei (`EX-A1-NACHRICHT`, `EX-A2-EMAIL`) – Entscheidung 5

**Stufe 1 – regelbasiert (zählt für „alle Aufgaben richtig“):**

| Check | A1 Nachricht | A2 E-Mail | Methode |
|---|---|---|---|
| Anrede vorhanden und registerpassend | informell | formell bzw. laut Aufgabe | Muster aus `02e` 2.2 (Regex-Liste), am Textanfang |
| Gruß vorhanden und registerpassend | ✔ | ✔ | Muster aus `02e` 2.2, am Textende |
| Name/Unterschrift | ✔ | ✔ | letzte Zeile ≠ Gruß, ≥ 2 Buchstaben |
| Mindestwortzahl | ≥ 20 (Ziel ca. 30) | ≥ 35 (Ziel ca. 50) | Wörter ohne Anrede/Gruß/Name; Obergrenze nur Hinweis (> 2× Ziel) |
| Leitpunkt-Abdeckung | 3/3 | 3/3 | je Leitpunkt Schlüsselbegriff-Liste im Item (`leitpunkte[i].keywords`, ≥ 1 Treffer, Lemmatisierung über Formenliste); kein Treffer → Leitpunkt „nicht erkannt“ |
| Verknüpfung | – | ≥ 2 Konnektoren | Liste aus G24/G25/G34/G35/G38 |
| Plagiat-Schutz | ✔ | ✔ | Kosinus-Ähnlichkeit (Wort-3-Gramme) zur Musterlösung > 0,6 → Hinweis „Bitte mit eigenen Worten schreiben“ (Q02 § 13c) |

**Stufe 2 – Musterlösung + Selbstcheck:** zwei unterschiedliche Musterlösungen; Selbstcheck-Liste entlang der Prüfungskriterien (Q05): Inhalt vollständig? · verständlich und verbunden? · passende Wörter, lesbar geschrieben? · Grammatik (geringer gewichtet).

**Stufe 3 – KI-Feedback (`FeedbackPort`)**: Lernhilfe, kein Bestehenskriterium (Entscheidung 5). Rubrik-Prompt mit den vier Kriterien.

**Raster A2 (Simulation, Schätzung):** Die offizielle Punkteverteilung je Kriterium ist ungeklärt (L1). Vorschlag als `[ANNAHME]` bis zur Klärung: Inhalt 8 · Kommunikative Realisierung 5 · Wortschatz/Verschriftlichung 4 · Grammatik 3 = 20. Grundlage: Q05 nennt Grammatik als geringer gewichtet als Kriterien 2 und 3.

### 3.5 Sprechen frei (`EX-A1-SPR*`, `EX-A2-KONTAKT/BILD/GESPRAECH`)

- Stufe 1 (Artifact): Audio-Aufnahme per Datei-Upload (`SpeechInPort`, Masterprompt 6.3) → Anhören → Musterantwort (Audio + Text) → **Checkliste** (Selbstbewertung, ja/nein pro Punkt). Die Checkliste ist Pflicht, damit die Aufgabe als erledigt gilt; sie bestimmt nicht „richtig/falsch“.
- Vorstufen mit Auto-Korrektur zählen für „alle richtig“: Redemittel wählen, Dialoglücke, Fragesatz bauen (Satzbau), ggf. Spracherkennung mit Schlüsselwort-Abgleich (Stufe 2).
- Checklisten je Teil (Beispiel A2-SPR-T2A): Ort/Situation genannt · ≥ 2 Personen/Handlungen beschrieben · ≥ 2 eigene Fragen gestellt · auf Antwort reagiert · verständlich gesprochen.
- Punkte je Teil/Kriterium A2: `[UNVERIFIZIERT]` (L2) – im Tool keine Punkt-Prognose für Sprechen, nur Checkliste.

### 3.6 Feedback-Format (alle Typen)

```json
{
  "verdict": "correct | incorrect | partial",
  "given": "…", "expected": "…",
  "explanation": { "de": "…", "en": "…", "tl": "…" },
  "distractorNotes": [{ "option": "b", "de": "…", "en": "…", "tl": "…" }],
  "learningGoalIds": ["A2-HOE-01"],
  "austriaNote": { "de": "In Deutschland: Januar" },
  "next": "leitner-box-1 | twin-in-correction-round"
}
```

Im Prüfungsmodus erscheint das Feedback erst nach Abgabe; im Lernmodus sofort. Nach jedem Feedback ist der Frage-Chat wieder frei (Entscheidung 7).

---

## 4. Vorbereitende Übungstypen

| Typ-ID | Übungstyp | Lernziel-Fokus | Prüfungsbezug | Auto-Korrektur | Toleranzen | Feedback |
|---|---|---|---|---|---|---|
| `UE-VOKABEL` | Vokabelkarte (de→en/tl, en/tl→de, Bild→de, Audio→de) | Wortschatz `02c` | alle | Eingabe: `isCorrect`; Richtung de→Übersetzung als Auswahl (MC) | T1, T3, T4; Artikel als eigenes Token mit `strictTokens` | Lösung + Artikel-Farbe + AT/D-Hinweis |
| `UE-GRAMMATIK` | Grammatik-Drill (Form bilden, Endung wählen) | G01–G49 | A1-SB-T1, Schreiben | exakter Vergleich der Zielform | T1; **kein** T3 auf Zielform | Regel in einfacher Sprache + eigenes Beispiel |
| `UE-SATZBAU` | Satzbau (Drag & Drop der Satzteile) | G01, G04, G12, G13, G25, G49 | Schreiben, Sprechen | Reihenfolge-Vergleich gegen Liste gültiger Reihenfolgen (`acceptedOrders`) | Zeitangabe vorne oder nach dem Verb als Varianten | Farbcode Verbposition |
| `UE-LUECKE` | Lückentext (Eingabe oder Auswahl) | G-Themen, Wortschatz | A1-SB-T1 | Eingabe: `isCorrect`; Auswahl: exakt | T1, T2 (außer Nomen), T3 (außer Zielform) | Lösung im Satz hervorgehoben |
| `UE-ZUORDNUNG` | Zuordnung (Bild–Wort, Frage–Antwort, Person–Anzeige) | Wortschatz, A2-LES-01, A1-HOE-07 | A1-HUA, A1-LES-T1, A2-LES-T1 | Paare exakt; jede Option max. 1× (wie Prüfung) | – | falsche Paare markiert |
| `UE-RF` | Richtig/Falsch | Lesen/Hören Detail | A1-HOE-T1, A1-LES-T2, A2-HOE-T4, WOW a/b | exakt | – | Textstelle markiert |
| `UE-MC` | Multiple Choice a/b bzw. a/b/c | alle | A1-HOE-T2, A1-LES-T3, A2-LES/HOE, WOW | exakt | – | warum richtig + Distraktor-Notizen |
| `UE-DIKTAT` | Diktat (Hören → Schreiben): Wörter, Zahlen, buchstabierte Namen | A1-HOE-02/03, A2-HOE-02 | A2-HOE-T1 | `isCorrect` je Token | Namen/Zahlen T0; Wörter T1+T3 | Token-Diff (richtig/falsch/fehlt) |
| `UE-DIALOG` | Dialog-Ergänzung (Redemittel wählen oder eintippen) | R-SP-* | A1-SPR-T3, A2-SPR-T2A, A1-HUA | Auswahl exakt; Eingabe gegen Varianten | T1, T2, T3, T4 | passende Alternativen zeigen |
| `UE-FORMULAR` | Formular ausfüllen (Freitext) | A1-SCH-01/02, A2-SCH-07 | A1-SCH-T1 | Feldregel 3.3 | wie 3.3 | Feld-für-Feld |
| `UE-EMAIL-VOR` | Leitpunkt-E-Mail – Vorstufen: Anrede/Gruß wählen, Leitpunkt ↔ Satz zuordnen, Sätze verbinden | A1/A2-SCH | A1-SCH-T2, A2-SCH-T1 | exakt / Zuordnung | – | Begründung Register |
| `UE-EMAIL` | Leitpunkt-E-Mail frei | A1-SCH-03, A2-SCH-01–06 | A1-SCH-T2, A2-SCH-T1 | Stufe 1 aus 3.4 | wie 3.4 | Check-Ergebnisse + 2 Musterlösungen + Selbstcheck + optional KI |
| `UE-BILD` | Bildbeschreibung – Vorstufen (Wörter im Bild antippen, Sätze ordnen) + frei (Aufnahme) | A2-SPR-03 | A2-SPR-T2A | Vorstufen exakt; frei Checkliste | – | Musterbeschreibung (2 Varianten) |
| `UE-SPRECHEN` | Sprechaufnahme (vorstellen, Frage stellen, auf Situation reagieren) | A1-SPR, A2-SPR | alle Sprechteile | Checkliste (3.5); Stufe 2: Spracherkennung + Schlüsselwörter | – | Musterantwort Audio + Text |
| `UE-WOW-KARTE` | Werte-Lernkarte (Fakt mit Quelle) → Abruf als a/b bzw. a/b/c | A1/A2-WOW | WOW | exakt | – | Erklärung + Quelle + Stand |
| `UE-ZAHLEN` | Zahlen/Uhrzeit/Preise hören und eintippen | A1-HOE-02, G14, G21 | A1-HOE-T2, A2-HOE-T1 | T0 auf normalisierte Zahl (`halb acht` ↔ `7:30` ↔ `07.30`) | Zeitformate als Varianten | Ziffern + Wortform |

**Didaktische Begründung der Typmischung:** Abrufübungen (Retrieval Practice, Q90/Q92) dominieren; jede Vorstufe ist kürzer und eindeutiger korrigierbar als die Prüfungsaufgabe (Cognitive Load, Q97); Interleaving der Typen im Wochenreview (Q93). Zwillingsaufgaben (Masterprompt Phase 4.4) entstehen pro Typ über Parametervariation (andere Person, Zahl, Option) bei gleichem Lernziel.

## 5. Abdeckungsnachweis

| Prüfungs-Teilaufgabe | Aufgabentyp | Korrekturregel | Vorbereitende Typen |
|---|---|---|---|
| A1-SB-T1 | EX-A1-SB | exakt | UE-GRAMMATIK, UE-LUECKE |
| A1-HOE-T1 | EX-A1-HOE1 | exakt | UE-RF, UE-DIKTAT |
| A1-HOE-T2 | EX-A1-HOE2 | exakt | UE-ZAHLEN, UE-DIKTAT, UE-MC |
| A1-HUA-T1/T2 | EX-A1-HUA1/2 | exakt | UE-DIALOG, UE-ZUORDNUNG |
| A1-LES-T1–T3 | EX-A1-LES1–3 | exakt | UE-ZUORDNUNG, UE-RF, UE-MC |
| A1-SCH-T1 | EX-A1-FORM | Feldregel 3.3 | UE-FORMULAR, UE-DIKTAT |
| A1-SCH-T2 | EX-A1-NACHRICHT | 3.4 | UE-EMAIL-VOR, UE-SATZBAU, UE-EMAIL |
| A1-SPR-T1–T3 | EX-A1-SPR1–3 | 3.5 | UE-DIALOG, UE-SATZBAU, UE-SPRECHEN |
| A1-WOW-T1/T2, A2-WOW-T1/T2 | EX-WOW-AB/ABC | exakt | UE-WOW-KARTE |
| A2-LES-T1–T4 | EX-A2-LES1–4 | exakt, Distraktor-Regeln 2.2 | UE-ZUORDNUNG, UE-MC, UE-FORMULAR |
| A2-HOE-T1–T4 | EX-A2-HOE1–4 | exakt | UE-DIKTAT, UE-ZAHLEN, UE-MC, UE-RF |
| A2-SCH-T1 | EX-A2-EMAIL | 3.4 | UE-EMAIL-VOR, UE-EMAIL |
| A2-SPR-T1/T2A/T2B | EX-A2-KONTAKT/BILD/GESPRAECH | 3.5 | UE-DIALOG, UE-BILD, UE-SPRECHEN |

**Ergebnis:** 29 Prüfungs-Teilaufgaben (A1: 15, A2: 14) → jede hat einen Aufgabentyp mit Korrekturregel (27 verschiedene Typen; `EX-WOW-AB/ABC` gelten für A1 und A2). Dazu 16 vorbereitende Übungstypen.
