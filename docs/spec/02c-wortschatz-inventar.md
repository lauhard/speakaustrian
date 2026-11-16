# 02c – Wortschatz-Inventar & Austriazismen (Phase 2.3, Lücken L8 + L16)

> **Projekt:** „Weg zur A2“ · **Phase:** 2 · **Stand:** 05.11.2026
> **Grundlage:** `claude/00-masterprompt.md` Phase 2.3 · `01-ressourcen.md` (Q61, Q62, Q70, Q72, Q74) · Handlungsfelder `02b`
> **Datei mit allen Einträgen:** `02c-wortschatz-inventar.tsv` (Projektwissen; maschinenlesbar, UTF-8, Tab-getrennt). Dieses Dokument enthält Herleitung, Schema, Statistik und die Austriazismen-Liste.

---

## 1. Zielgröße (Lücke L8 – geklärt)

### 1.1 Messung der offiziellen Goethe-Wortlisten

Die beiden PDFs wurden lokal ausgewertet (Zählskript über das Seitenlayout: Stichwortspalte, Zeilenabstände). Weil goethe.de aus der Arbeitsumgebung per Shell nicht erreichbar war, stammen die Dateien aus einem öffentlichen GitHub-Spiegel (`ilkermeliksitki/goethe-institute-wordlist`); ihre Echtheit ist über Impressum, Dateikennung und PDF-Metadaten plausibilisiert, die Vorwort-Angaben wurden zusätzlich direkt auf goethe.de per Web-Abruf bestätigt. Ausgewertet wurden nur **Zahlen**, keine Inhalte übernommen.

| Liste | Quelle | Angabe im Vorwort | Gemessen: Stichwort-Zeilen | Gemessen: Eintragsblöcke | Stand |
|---|---|---|---|---|---|
| Goethe-Zertifikat A1: Start Deutsch 1 – Wortliste | Q61 – https://www.goethe.de/pro/relaunch/prf/de/A1_SD1_Wortliste_02.pdf (Alternativpfad `/prf/ca/` erreichbar) | „circa 650 Einträge“, davon ca. die Hälfte aktiv | **703** (inkl. eingerückter Ableitungen) | **688** | Datei 12.04.2012, Erstausgabe 2004 |
| Goethe-Zertifikat A2 – Wortliste | Q62 – https://www.goethe.de/pro/relaunch/prf/en/Goethe-Zertifikat_A2_Wortliste.pdf | „circa 1300 lexikalische Einheiten“ | **1.558** | **1.165** | © 2016, 1. Aufl. (Datei geändert 15.09.2020) |

Zusätzlich gemessen: Überschneidung A1 ∩ A2 ≈ 78 % der A1-Stichwörter; **Vereinigung A1 ∪ A2 ≈ 1.560 Stichwörter** (vor Bereinigung) bzw. **1.284 bereinigte Lemmata** (Referenz für den Abdeckungs-Check). Beide Listen sind **bundesdeutsch**; die A2-Liste sagt ausdrücklich, dass österreichische und Schweizer Varianten nicht aufgeführt werden.

**Lizenz:** Beide Listen sind urheberrechtlich geschützt (© Goethe-Institut). Sie dienen nur als **Abdeckungsreferenz** (Zählung, Abgleich). Das Inventar ist eigenständig nach Handlungsfeldern aufgebaut; Beispielsätze der Goethe-Listen werden nicht übernommen.

### 1.2 Abgeleitete Zielgröße

| Baustein | Umfang | Begründung |
|---|---|---|
| Goethe-A1-Kern | ≈ 650–700 | offizielle A1-Referenz |
| A2-Zuwachs | ≈ 850 | Vereinigung minus A1 |
| Österreich-/ÖIF-spezifisch | ≈ 150–200 | Austriazismen als Hauptform (Masterprompt), Institutionen (AMS, BH, Magistrat, e-card, Meldezettel), WOW-Wortschatz (Q09/Q36), der in keiner Goethe-Liste steht |
| **Zielgröße gesamt** | **≈ 1.700–1.900 lexikalische Einheiten** | davon A1 ≈ 850–900, A2 ≈ 900–1.000 |

**Abgleich mit dem Kapitelrahmen (Masterprompt Phase 3):** 36–40 Kapitel × 30–45 neue Einheiten = 1.080–1.800. Die Zielgröße liegt am oberen Rand. Lösung für Phase 3: **Wortgruppen** (Zahlen, Wochentage, Monate, Farben, Bundesländer, Nachbarländer ≈ 90 Einheiten) zählen als Set, **passive** Einträge werden rezeptiv eingeführt und nicht produktiv abgefragt (siehe 3.3).

## 2. Ergebnis: Inventar v1

| Kennzahl | Wert | Ziel | Status |
|---|---|---|---|
| Einträge gesamt | **1.913** | 1.700–1.900 | ✅ (leicht darüber) |
| davon A1 / A2 | 906 / 1.007 | 850–900 / 900–1.000 | ✅ |
| Abdeckung Goethe-A1 durch eigenes A1 | **88,8 %** | ≥ 85 % | ✅ |
| Abdeckung Goethe-A1∪A2 (1.284 bereinigte Lemmata) durch Inventar | **85,7 %** | ≥ 85 % | ✅ |
| Austriazismen (`at=1`) | **132** | – | ✅ (Liste Abschn. 4) |
| Einträge mit `en` + `tl` | 1.913 / 1.913 | 100 % | ✅ (`review_*: machine`) |
| Beispielsatz | 0 / 1.913 | – | ⚠️ bewusst verschoben, siehe 3.2 |

**Nicht abgedeckte Goethe-Lemmata (≈ 14 %)** sind überwiegend: bundesdeutsche Formen mit österreichischer Hauptform im Inventar (z. B. Januar → Jänner, Tüte → Sackerl), Tourismus-/Hotelwortschatz (Halbpension, Jugendherberge, Rezeption), Jugendthemen (Comic, Motorroller) und Messartefakte (Zeilenumbrüche im PDF). Bewusst ausgelassen, weil sie für das Integrations-Alltagsziel nachrangig sind; im Kapitelbau (Phase 3) bei Bedarf als passive Einträge nachziehbar.

### 2.1 Verteilung nach Handlungsfeld

| HF | A1 aktiv | A1 passiv | A2 aktiv | A2 passiv | Summe |
|---|---|---|---|---|---|
| GW | 272 | 12 | 230 | 68 | 582 |
| HF00 | 36 | 3 | 34 | 5 | 78 |
| HF01 | 79 | 5 | 9 | 3 | 96 |
| HF02 | 59 | 6 | 56 | 13 | 134 |
| HF03 | 98 | 7 | 66 | 43 | 214 |
| HF04 | 37 | 1 | 40 | 9 | 87 |
| HF05 | 21 | 2 | 47 | 10 | 80 |
| HF06 | 22 | 2 | 83 | 12 | 119 |
| HF07 | 11 | 3 | 21 | 10 | 45 |
| HF08 | 43 | 3 | 30 | 18 | 94 |
| HF09 | 6 | 1 | 25 | 6 | 38 |
| HF10 | 43 | 3 | 38 | 26 | 110 |
| HF11 | 16 | 2 | 12 | 3 | 33 |
| HF12 | 81 | 3 | 14 | 6 | 104 |
| HF13 | 13 | 0 | 12 | 2 | 27 |
| HF14 | 10 | 0 | 12 | 4 | 26 |
| HF15 | 3 | 3 | 29 | 11 | 46 |
| **Summe** | **850** | **56** | **758** | **249** | **1913** |

**Befund A1 aktiv/passiv:** 850 von 906 A1-Einträgen sind derzeit `aktiv`. Das Goethe-Vorwort empfiehlt rund die Hälfte aktiv. → **Offener Punkt für Phase 3:** beim Zuordnen zu Kapiteln `use` nachkalibrieren (Zielanteil aktiv A1 ≈ 55–60 %, A2 ≈ 60–65 %). Regel: aktiv = wird in Schreib-/Sprechaufgaben produktiv verlangt; passiv = nur in Lese-/Hörtexten und Distraktoren.

## 3. Datenschema (für Phase 5 `content/*.json`)

### 3.1 Spalten der TSV

| Spalte | Inhalt | Werte / Beispiel |
|---|---|---|
| `id` | stabile ID, ändert sich nie | `W-A1-0123`, `W-A2-0045` |
| `lemma` | Grundform; Personenbezeichnungen als Paar | `Arzt, Ärztin` |
| `article` | Artikel(e) | `der`, `die`, `das`, `der/die`, `das/die`; `(das)` bei artikellos gebrauchten Ländernamen |
| `forms` | Nomen: Plural (`-e`, `¨-er`, `-`, `Sg.`, `Pl.`); Verben: unregelmäßige 3. Sg. und Perfekt | `fährt, ist gefahren` |
| `pos` | Wortart | `n v adj adv prep pron art konj num part interj phr pref` |
| `hf` | Handlungsfeld (02b) oder `GW` = feldübergreifender Grundwortschatz | `HF04` |
| `level` | Einführungsniveau | `A1`, `A2` |
| `use` | `a` aktiv (produktiv), `p` passiv (rezeptiv) | |
| `at` | Austriazismus-Flag | `1` / `0` |
| `variant` | bundesdeutsche Variante bzw. Hinweis | `Kartoffel` |
| `en`, `tl` | Übersetzung | Tagalog einfach, Taglish erlaubt (Masterprompt Abschn. 2) |
| `example` | Beispielsatz (Phase 5) | leer |
| `review_en`, `review_tl` | `machine` / `reviewed` | alle `machine` |

### 3.2 Abweichung vom Masterprompt: Beispielsatz erst in Phase 5

Der Masterprompt verlangt pro Eintrag einen Beispielsatz. Ich habe das Feld **bewusst leer gelassen** und schlage vor, es in Phase 5 je Kapitel zu füllen. Begründung: Die Regel „nur eingeführter Wortschatz + geplante neue Wörter“ (QA-Check Phase 5.11) lässt sich erst prüfen, wenn feststeht, in welchem Kapitel ein Wort eingeführt wird (Phase 3). Ein Beispielsatz jetzt würde zwangsläufig Wörter aus späteren Kapiteln enthalten und müsste neu geschrieben werden. **→ Entscheidung durch dich nötig (offene Frage O2 in `02-aufbereitung.md`).**

### 3.3 Didaktische Regeln für den Einsatz

1. **Österreichische Form ist Hauptform**, die bundesdeutsche Variante erscheint als Hinweis („In Deutschland: Kartoffel“). Bundesdeutsche Formen mit Prüfungsrelevanz (z. B. *Kartoffel* auf Produktverpackungen) sind als eigene passive Einträge geführt.
2. **Wortgruppen** (Zahlen, Tage, Monate, Farben, Bundesländer, Nachbarländer) werden als Set eingeführt und als Set wiederholt – das senkt die kognitive Last pro Lerneinheit (Cognitive Load, Q97).
3. **Personenbezeichnungen** immer als Paar (Arzt/Ärztin) – entspricht der Gleichberechtigungs-Linie der Rahmencurricula (Q36, Werte 2 und 3).
4. **Passive Einträge** dürfen in Lese-/Hörtexten ohne Glossar vorkommen, sobald ihr Kapitel erreicht ist; vorher nur mit Glossar (max. 5 % unbekannte Wörter je Text, Masterprompt 5.4 / Q98).
5. **Prüfungsanweisungen** (HF00: ankreuzen, ergänzen, zuordnen …) werden bis Ende A1 vollständig eingeführt, weil sie Voraussetzung jeder Prüfungsaufgabe sind.

## 4. Austriazismen-Liste A1/A2 (Lücke L16 – geklärt)

### 4.1 Herleitung

Es gibt keinen offiziellen Austriazismen-Katalog für A1/A2 (bestätigt: Goethe-Listen führen keine AT-Varianten; ÖIF-Materialien verwenden AT-Formen, ohne sie zu listen). Die Liste wurde abgeleitet aus:

| Quelle | Beitrag | Stand |
|---|---|---|
| Q70 Ebner, *Österreichisches Deutsch* (Duden), Abschn. Essen, Verwaltung, Schule, Zeit (S. 9–29) | Wortpaare AT–D, plurizentrisches Prinzip (AT-Formen sind gleichwertiger Standard) | 2008 |
| Q74 Protokoll Nr. 10 zum EU-Beitrittsvertrag (23 Lebensmittelbezeichnungen) | Rechtlich geschützte AT-Bezeichnungen (z. B. Erdäpfel, Paradeiser, Topfen, Marillen, Karfiol, Fisolen, Kren, Obers, Ribisel, Melanzani, Kohlsprossen, Vogerlsalat, Weichseln, Faschiertes) | 1994; Liste aus Fachwissen, RIS-Volltext wegen Robots-Sperre nicht abgerufen → Liste `[UNVERIFIZIERT]`, Begriffe einzeln durch Q70 gedeckt |
| Q36 ÖIF-Rahmencurricula und Prüfungsformat (Q05/Q06) | Institutionen- und Alltagswörter im Prüfungskontext (Mobilbox, Meldezettel, e-card, AMS, Magistrat, BH, Elternsprechtag, Matura) | 2025 |
| Fachwissen österreichisches Standarddeutsch | Alltagsgrammatik (Perfekt mit *sein*, Genus) und Alltagswörter (Sackerl, Kasten, Sessel, Stiege, Jause) | – |

Auswahlkriterium: **Vorkommen im Alltag der Lernenden in A1/A2-Handlungsfeldern** (Einkauf, Wohnen, Amt, Schule, Gesundheit) – nicht Vollständigkeit.

### 4.2 Grammatik- und Aussprache-Austriazismen (für 02d und Audio)

| Phänomen | AT-Standard | D-Standard | Niveau | Quelle |
|---|---|---|---|---|
| Perfekt von *liegen, sitzen, stehen* | **ist** gelegen/gesessen/gestanden | hat … | A1 | Q70 S. 14 |
| Genus | **das** Joghurt, **das** E-Mail, **das** SMS, **das** Cola | der Joghurt, die E-Mail, die SMS, die Cola | A1–A2 | Fachwissen; Genus-Kapitel von Q70 im verfügbaren Auszug nicht enthalten → `[UNVERIFIZIERT]`, vor Phase 5 mit Österreichischem Wörterbuch (Q73) prüfen |
| Monatsnamen | **Jänner**, (Feber, regional/amtlich) | Januar, Februar | A1 | Q70 S. 14 |
| Verkleinerung | **-erl** (Sackerl, Zuckerl, Kipferl) neben -chen | -chen | A1 | Q70 S. 22 |
| Zahlwort im Alltag | „ein Viertel/halb/dreiviertel acht“ verbreitet | auch „Viertel nach sieben“ | A1 | Fachwissen |
| Begrüßung | Grüß Gott, Servus, Mahlzeit | Guten Tag, Hallo | A1 | Q36 (Konventionen), Fachwissen |
| Aussprache | Endung *-ig* als [ɪk] (König, zwanzig), langes o in *Geschoß* | [ɪç] | A1 | Q70 S. 7; Fachwissen |
| Hörverstehen | Wechsel zwischen Standard und Umgangssprache im Alltag (Prüfungs-Audios sprechen Standard) | – | A2 | Q70 S. 13 |

**Konsequenz für Hören (Phase 5):** TTS-Stimme `de-AT` bevorzugen; Prüfungsskripte in österreichischem Standard, keine Dialektformen. Dialekt-Hörverstehen nur als Verweis auf das ÖIF-Angebot „Dialekte verstehen“ (Q49).

### 4.3 Wortliste (alle `at=1`-Einträge aus dem Inventar)

| ID | AT-Standard (Hauptform) | Artikel | Bundesdt. Variante / Hinweis | Niveau | HF | aktiv/passiv |
|---|---|---|---|---|---|---|
| W-A1-0168 | liegen |  | hat gelegen (D) | A1 | GW | a |
| W-A1-0170 | sitzen |  | hat gesessen (D) | A1 | GW | a |
| W-A1-0169 | stehen |  | hat gestanden (D) | A1 | GW | a |
| W-A1-0316 | Hausübung | die | Hausaufgabe | A1 | HF00 | a |
| W-A1-0398 | Bub | der | Junge | A1 | HF01 | a |
| W-A1-0373 | E-Mail | das/die | die E-Mail | A1 | HF01 | a |
| W-A1-0376 | grüß Gott |  | guten Tag | A1 | HF01 | a |
| W-A1-0377 | servus |  | hallo/tschüss | A1 | HF01 | a |
| W-A1-0421 | Erdgeschoß | das | Erdgeschoss | A1 | HF02 | a |
| W-A1-0432 | Kasten | der | Schrank | A1 | HF02 | a |
| W-A1-0422 | Lift | der | Aufzug | A1 | HF02 | a |
| W-A1-0449 | Meldezettel | der | Meldebescheinigung/Anmeldung | A1 | HF02 | a |
| W-A1-0454 | Mistkübel | der | Mülleimer | A1 | HF02 | a |
| W-A1-0430 | Sessel | der | Stuhl (AT: Sessel = Stuhl) | A1 | HF02 | a |
| W-A1-0423 | Stiege | die | Treppe | A1 | HF02 | a |
| W-A1-0530 | Deka | das | 10 Gramm (D: -) | A1 | HF03 | a |
| W-A1-0502 | Erdapfel | der | Kartoffel | A1 | HF03 | a |
| W-A1-0496 | Faschiertes | das | Hackfleisch | A1 | HF03 | p |
| W-A1-0552 | Gasthaus | das | Gaststätte | A1 | HF03 | a |
| W-A1-0493 | Hendl | das | Hähnchen | A1 | HF03 | p |
| W-A1-0488 | Joghurt | das | der Joghurt | A1 | HF03 | a |
| W-A1-0570 | Kaffeehaus | das | Café | A1 | HF03 | p |
| W-A1-0505 | Karotte | die | Möhre | A1 | HF03 | a |
| W-A1-0543 | Kassa | die | Kasse | A1 | HF03 | a |
| W-A1-0575 | Mahlzeit |  | guten Appetit (D: seltener) | A1 | HF03 | a |
| W-A1-0513 | Marille | die | Aprikose | A1 | HF03 | p |
| W-A1-0490 | Obers | das | Sahne | A1 | HF03 | p |
| W-A1-0503 | Paradeiser | der | Tomate | A1 | HF03 | a |
| W-A1-0548 | Sackerl | das | Tüte | A1 | HF03 | a |
| W-A1-0483 | Semmel | die | Brötchen | A1 | HF03 | a |
| W-A1-0489 | Topfen | der | Quark | A1 | HF03 | p |
| W-A1-0590 | e-card | die | Versichertenkarte | A1 | HF04 | a |
| W-A1-0583 | Ordination | die | Arztpraxis | A1 | HF04 | a |
| W-A1-0585 | Spital | das | Krankenhaus | A1 | HF04 | p |
| W-A1-0625 | AMS | das | Arbeitsagentur (D) | A1 | HF05 | a |
| W-A1-0641 | Gemeindeamt | das | Gemeindeverwaltung | A1 | HF06 | a |
| W-A1-0640 | Magistrat | der | Stadtverwaltung | A1 | HF06 | a |
| W-A1-0665 | Bankomat | der | Geldautomat | A1 | HF07 | a |
| W-A1-0666 | Bankomatkarte | die | EC-Karte/Girocard | A1 | HF07 | a |
| W-A1-0680 | Bim | die | Straßenbahn (ugs.) | A1 | HF08 | p |
| W-A1-0725 | Volksschule | die | Grundschule | A1 | HF09 | a |
| W-A1-0761 | Bad (Schwimmbad) | das | Freibad/Schwimmbad | A1 | HF10 | p |
| W-A1-0781 | Mobilbox | die | Mailbox | A1 | HF11 | a |
| W-A1-0783 | SMS | das | die SMS | A1 | HF11 | a |
| W-A1-0831 | Jänner | der | Januar | A1 | HF12 | a |
| W-A1-0896 | Rettung | die | Rettungsdienst/Krankenwagen | A1 | HF14 | a |
| W-A2-0357 | Betriebskosten | die | Nebenkosten | A2 | HF02 | a |
| W-A2-0376 | Gang | der | Flur | A2 | HF02 | a |
| W-A2-0364 | Gemeindewohnung | die | Sozialwohnung | A2 | HF02 | p |
| W-A2-0359 | Hausbesorger, Hausbesorgerin | der/die | Hausmeister/in | A2 | HF02 | p |
| W-A2-0383 | läuten |  | klingeln | A2 | HF02 | a |
| W-A2-0401 | Mistplatz | der | Wertstoffhof/Recyclinghof | A2 | HF02 | a |
| W-A2-0379 | Stiegenhaus | das | Treppenhaus | A2 | HF02 | a |
| W-A2-0377 | Vorzimmer | das | Diele/Flur | A2 | HF02 | a |
| W-A2-0428 | Aktion | die | Sonderangebot | A2 | HF03 | a |
| W-A2-0470 | Eierspeise | die | Rührei | A2 | HF03 | p |
| W-A2-0454 | Fisolen | die | grüne Bohnen | A2 | HF03 | p |
| W-A2-0421 | Fleischhauer | der | Metzger/Fleischer | A2 | HF03 | a |
| W-A2-0506 | Geldbörse | die | Portemonnaie/Geldbeutel | A2 | HF03 | a |
| W-A2-0472 | Germ | der/die | Hefe | A2 | HF03 | p |
| W-A2-0445 | Haube | die | Mütze | A2 | HF03 | p |
| W-A2-0482 | Hauptspeise | die | Hauptgericht | A2 | HF03 | a |
| W-A2-0464 | Häuptelsalat | der | Kopfsalat | A2 | HF03 | p |
| W-A2-0485 | Jause | die | Brotzeit/Imbiss | A2 | HF03 | a |
| W-A2-0453 | Karfiol | der | Blumenkohl | A2 | HF03 | p |
| W-A2-0429 | Kassabon | der | Kassenbon/Kassenzettel | A2 | HF03 | a |
| W-A2-0468 | Kipferl | das | Hörnchen | A2 | HF03 | p |
| W-A2-0462 | Kohlsprossen | die | Rosenkohl | A2 | HF03 | p |
| W-A2-0469 | Krapfen | der | Berliner | A2 | HF03 | p |
| W-A2-0455 | Kraut | das | Kohl | A2 | HF03 | p |
| W-A2-0456 | Kren | der | Meerrettich | A2 | HF03 | p |
| W-A2-0484 | Mehlspeise | die | Süßspeise/Kuchen | A2 | HF03 | p |
| W-A2-0461 | Melanzani | die | Aubergine | A2 | HF03 | p |
| W-A2-0483 | Nachspeise | die | Nachtisch | A2 | HF03 | a |
| W-A2-0467 | Palatschinke | die | Pfannkuchen/Crêpe | A2 | HF03 | p |
| W-A2-0459 | Ribisel | die | Johannisbeere | A2 | HF03 | p |
| W-A2-0466 | Sauerrahm | der | saure Sahne/Schmand | A2 | HF03 | p |
| W-A2-0465 | Schlagobers | das | Schlagsahne | A2 | HF03 | p |
| W-A2-0457 | Schwammerl | das | Pilz | A2 | HF03 | p |
| W-A2-0474 | Semmelbrösel | die | Paniermehl | A2 | HF03 | p |
| W-A2-0473 | Staubzucker | der | Puderzucker | A2 | HF03 | p |
| W-A2-0423 | Trafik | die | Kiosk/Tabakladen | A2 | HF03 | a |
| W-A2-0463 | Vogerlsalat | der | Feldsalat | A2 | HF03 | p |
| W-A2-0460 | Weichsel | die | Sauerkirsche | A2 | HF03 | p |
| W-A2-0471 | Zuckerl | das | Bonbon | A2 | HF03 | p |
| W-A2-0458 | Zwetschke | die | Zwetschge/Pflaume | A2 | HF03 | p |
| W-A2-0570 | Ambulanz | die | Notaufnahme/Ambulanz | A2 | HF04 | a |
| W-A2-0541 | Eltern-Kind-Pass | der | (D: Mutterpass/U-Heft) | A2 | HF04 | a |
| W-A2-0540 | Gesundenuntersuchung | die | Vorsorgeuntersuchung | A2 | HF04 | p |
| W-A2-0572 | Gesundheitshotline 1450 |  | (D: 116 117) | A2 | HF04 | a |
| W-A2-0533 | Krankenstand | der | Krankschreibung | A2 | HF04 | a |
| W-A2-0566 | Rezeptgebühr | die | Zuzahlung | A2 | HF04 | p |
| W-A2-0555 | verkühlt |  | erkältet | A2 | HF04 | p |
| W-A2-0529 | ÖGK (Österreichische Gesundheitskasse) | die | (D: AOK/Krankenkasse) | A2 | HF04 | a |
| W-A2-0596 | Dienstgeber, Dienstgeberin | der/die | Arbeitgeber/in | A2 | HF05 | a |
| W-A2-0597 | Dienstnehmer, Dienstnehmerin | der/die | Arbeitnehmer/in | A2 | HF05 | a |
| W-A2-0617 | in Pension gehen |  | in Rente gehen | A2 | HF05 | a |
| W-A2-0626 | Kassier, Kassierin | der/die | Kassierer/in | A2 | HF05 | a |
| W-A2-0595 | Lohnzettel | der | Gehaltsabrechnung | A2 | HF05 | a |
| W-A2-0616 | Pension | die | Rente | A2 | HF05 | a |
| W-A2-0631 | Pensionist, Pensionistin | der/die | Rentner/in | A2 | HF05 | a |
| W-A2-0582 | Stelleninserat | das | Stellenanzeige | A2 | HF05 | a |
| W-A2-0634 | Bezirk | der | Stadtbezirk/Kreis | A2 | HF06 | a |
| W-A2-0637 | Bezirkshauptmannschaft (BH) | die | Landratsamt | A2 | HF06 | a |
| W-A2-0656 | Familienbeihilfe | die | Kindergeld | A2 | HF06 | a |
| W-A2-0728 | Fundamt | das | Fundbüro | A2 | HF06 | p |
| W-A2-0674 | Landeshauptmann, Landeshauptfrau | der/die | Ministerpräsident/in | A2 | HF06 | p |
| W-A2-0655 | Lichtbildausweis | der | Ausweis mit Foto | A2 | HF06 | a |
| W-A2-0649 | Staatsbürgerschaft | die | Staatsangehörigkeit | A2 | HF06 | a |
| W-A2-0747 | Abholschein | der | Benachrichtigungskarte | A2 | HF07 | a |
| W-A2-0743 | Bankomatgebühr | die | Geldautomatengebühr | A2 | HF07 | p |
| W-A2-0735 | Erlagschein | der | Zahlschein/Überweisungsträger | A2 | HF07 | a |
| W-A2-0759 | Haushaltsversicherung | die | Hausratversicherung | A2 | HF07 | p |
| W-A2-0750 | Kuvert | das | Umschlag | A2 | HF07 | a |
| W-A2-0749 | Postkasten | der | Briefkasten | A2 | HF07 | a |
| W-A2-0754 | Wertkarte | die | Prepaidkarte | A2 | HF07 | a |
| W-A2-0734 | Zahlschein | der | Überweisungsträger | A2 | HF07 | a |
| W-A2-0764 | Klimaticket | das | (D: Deutschlandticket) | A2 | HF08 | p |
| W-A2-0792 | Schutzweg | der | Zebrastreifen | A2 | HF08 | a |
| W-A2-0793 | Vorrang | der | Vorfahrt | A2 | HF08 | p |
| W-A2-0760 | Öffis | die | ÖPNV/Öffentliche | A2 | HF08 | a |
| W-A2-0828 | Kindergartenpädagoge, Kindergartenpädagogin | der/die | Erzieher/in | A2 | HF09 | p |
| W-A2-0818 | Klassenvorstand | der | Klassenlehrer/in | A2 | HF09 | a |
| W-A2-0811 | Lehrling | der | Auszubildende/r (Azubi) | A2 | HF09 | a |
| W-A2-0812 | Matura | die | Abitur | A2 | HF09 | a |
| W-A2-0821 | Mitteilungsheft | das | Hausaufgabenheft/Mitteilungsheft | A2 | HF09 | a |
| W-A2-0820 | Schularbeit | die | Klassenarbeit | A2 | HF09 | a |
| W-A2-0822 | Schultasche | die | Schulranzen | A2 | HF09 | a |
| W-A2-0825 | Turnen | das | Sport (Schulfach) | A2 | HF09 | a |
| W-A2-0921 | Feber | der | Februar | A2 | HF12 | p |
| W-A2-0941 | Christkind | das | Weihnachtsmann (D-Nord) | A2 | HF13 | a |
| W-A2-0943 | Fasching | der | Karneval | A2 | HF13 | a |

**Hinweis Prüfungsrelevanz:** Im Prüfungsmodus erscheinen nur österreichische Formen (wie in den ÖIF-Materialien). Die bundesdeutsche Variante wird in Lernkarten und im Feedback gezeigt (Masterprompt Abschn. 1).
