# A1-03 pools -> src/lib/content/a1-03-pools.json
import json
from collections import Counter
from gen_a103_common import *

TEST, PRACTICE = [], []


def fam(code, fn, test, practice):
    assert len(test) in (0, 3) and len(practice) % 2 == 0, code
    t = [fn(v, f'{CH}-T-{code}-{n}') for n, v in enumerate(test, 1)]
    for it in t[1:]:
        it['family'] = t[0]['id']
    p = [fn(v, f'{CH}-P-{code}-{n}') for n, v in enumerate(practice, 1)]
    for a, b in zip(p[::2], p[1::2]):
        b['family'] = a['id']
    TEST.extend(t)
    PRACTICE.extend(p)


E = lambda de_, en, tl: L(de_, en, tl)
AUS = {'Österreich': 'aus Österreich', 'Deutschland': 'aus Deutschland', 'Schweiz': 'aus der Schweiz', 'Philippinen': 'aus den Philippinen'}
EN_C = {'Österreich': 'Austria', 'Deutschland': 'Germany', 'Schweiz': 'Switzerland', 'Philippinen': 'the Philippines'}
TL_C = {'Österreich': 'Austria', 'Deutschland': 'Germany', 'Schweiz': 'Switzerland', 'Philippinen': 'Pilipinas'}

# ================================================================ HÖREN (A1-HOE-T1 style a/b; A1-HUA-T1 reactions)
fam('HO1', lambda v, i: choice(i, 'hoeren', L('Hören Sie. Woher kommt die Person?', 'Listen. Where does the person come from?', 'Makinig. Taga-saan ang tao?'), None, v[0], [v[1]],
    E(f'Sie hören: „Ich komme {AUS[v[0]]}.“', f'You hear: “Ich komme {AUS[v[0]]}.” ({EN_C[v[0]]})', f'Naririnig mo: “Ich komme {AUS[v[0]]}.” ({TL_C[v[0]]})'), [G1], R('aus'), audio=f'Grüß Gott! Ich bin {v[2]}. Ich komme {AUS[v[0]]}.'),
    [('Schweiz', 'Deutschland', 'Herr Gruber'), ('Philippinen', 'Österreich', 'Maria'), ('Deutschland', 'Schweiz', 'Frau Weber')],
    [('Österreich', 'Deutschland', 'Lukas'), ('Philippinen', 'Schweiz', 'Jose'), ('Schweiz', 'Österreich', 'Anna'), ('Deutschland', 'Philippinen', 'Tom')])

fam('HO2', lambda v, i: choice(i, 'hoeren', L('Hören Sie. Wo wohnt die Person?', 'Listen. Where does the person live?', 'Makinig. Saan nakatira ang tao?'), None, f'in {v[0]}', [f'in {v[1]}'],
    E(f'Sie hören: „Ich wohne in {v[0]}.“ {v[1]} ist die Heimat.', f'You hear: “Ich wohne in {v[0]}.” {v[1]} is the home town.', f'Naririnig mo: “Ich wohne in {v[0]}.” {v[1]} ang pinagmulan.'),
    [G2], R('wohnen', 'in'), audio=f'Ich komme aus {v[1]}, aber ich wohne in {v[0]}.'.replace('St. ', 'Sankt ')),
    [('Klagenfurt', 'Manila'), ('Salzburg', 'Berlin'), ('Wien', 'Graz')], [('Linz', 'Cebu'), ('Graz', 'München'), ('Innsbruck', 'Zürich'), ('St. Pölten', 'Wien')])

LANG = {'D': 'Deutsch', 'E': 'Englisch', 'T': 'Tagalog'}
fam('HO3', lambda v, i: choice(i, 'hoeren', L('Hören Sie. Welche Sprachen spricht die Person?', 'Listen. Which languages does the person speak?', 'Makinig. Anong mga wika ang alam ng tao?'), None, v[0], [v[1]],
    E(f'Sie hören: „Ich spreche {v[0]}.“', f'You hear: “Ich spreche {v[0]}.”', f'Naririnig mo: “Ich spreche {v[0]}.”'), [G3], R('sprechen', 'Sprache'), audio=f'Ich spreche {v[0]}.'),
    [('Tagalog und Deutsch', 'Tagalog und Englisch'), ('nur Englisch', 'Englisch und Deutsch'), ('Deutsch und Englisch', 'nur Deutsch')],
    [('Deutsch, Englisch und Tagalog', 'Deutsch und Tagalog'), ('nur Tagalog', 'Tagalog und Deutsch'), ('Englisch und Tagalog', 'Englisch und Deutsch'), ('Tagalog und ein bisschen Englisch', 'nur Tagalog')])

REACT = {'woher': ('Woher kommen Sie?', 'Aus Graz.'), 'wo': ('Wo wohnen Sie?', 'In Linz.'), 'spr': ('Welche Sprachen sprechen Sie?', 'Deutsch und Englisch.'),
         'name': ('Wie heißen Sie?', 'Maria Santos.'), 'tel': ('Auf Wiederhören!', 'Auf Wiederhören!'), 'adr': ('Wie ist Ihre Adresse?', 'Hauptstraße 3.'),
         'nicht': ('Wohnen Sie nicht in Wien?', 'Doch, in Wien.'), 'langsam': ('Verstehen Sie?', 'Nein. Langsam, bitte!')}
fam('HO4', lambda v, i: choice(i, 'hoeren', L('Hören Sie. Was passt? Wählen Sie die Antwort.', 'Listen. Which reply fits? Choose the answer.', 'Makinig. Alin ang angkop na sagot?'), None, REACT[v[0]][1], [REACT[k][1] for k in v[1]],
    E(f'Sie hören: „{REACT[v[0]][0]}“ – passend ist: „{REACT[v[0]][1]}“', f'You hear: “{REACT[v[0]][0]}” – a fitting reply is: “{REACT[v[0]][1]}”', f'Naririnig mo: “{REACT[v[0]][0]}” – angkop: “{REACT[v[0]][1]}”'),
    [G1, G2], R('wo', 'woher'), audio=REACT[v[0]][0]),
    [('woher', ['wo', 'name', 'spr']), ('wo', ['woher', 'adr', 'tel']), ('spr', ['woher', 'wo', 'name'])],
    [('name', ['wo', 'woher', 'spr']), ('adr', ['wo', 'woher', 'name']), ('tel', ['name', 'langsam', 'wo']), ('nicht', ['wo', 'woher', 'name'])])

fam('HO5', lambda v, i: choice(i, 'hoeren', L('Hören Sie. Wie ist die E-Mail-Adresse?', 'Listen. What is the e-mail address?', 'Makinig. Ano ang e-mail address?'), None, v[0], v[1],
    E(f'@ = „ät“, . = „Punkt“: {v[0]}', f'@ = “ät”, . = “Punkt”: {v[0]}', f'@ = “ät”, . = “Punkt”: {v[0]}'), [G2], R('E-Mail'), audio='Die E-Mail-Adresse ist: ' + v[2]),
    [], [('lukas.berger@aon.at', ['lukasberger@aon.at', 'lukas.berger@aon.de'], 'lukas Punkt berger ät a o n Punkt a t'),
         ('jose.cruz@gmx.at', ['jose.cruz@gmx.de', 'josecruz@gmx.at'], 'jose Punkt cruz ät g m x Punkt a t')])

fam('HO6', lambda v, i: short(i, 'hoeren', SPELLED, 'Die Straße:', list(dict.fromkeys([v, v.replace('ß', 'ss')])), E(f'{spell(v.replace("ß", "ss"))[:-1]}: „{v}“.', f'{spell(v.replace("ß", "ss"))[:-1]}: “{v}”.', f'{spell(v.replace("ß", "ss"))[:-1]}: “{v}”.'), [G2], R('Straße', 'buchstabieren'), audio='Die Straße heißt: ' + ', '.join(NAMES[c] for c in v.lower().replace('ß', 'ss'))),
    [], ['Seegasse', 'Feldweg', 'Kirchplatz', 'Ringstraße'])

# ================================================================ LESEN
INTRO = lambda v, i: choice(i, 'lesen', READ, f'Hallo! Ich heiße {v[0]}. Ich komme {AUS[v[1]]}. Ich wohne in {v[2]}. Ich spreche {v[3]}.\n{v[4]}', v[5], v[6],
                            E(f'Im Text steht: „{v[7]}“', f'The text says: “{v[7]}”', f'Sabi sa teksto: “{v[7]}”'), [G1, G2, G3], R('wohnen', 'sprechen', 'aus'))
fam('LE1', INTRO,
    [('Maria', 'Philippinen', 'Wien', 'Tagalog und Englisch', 'Wo wohnt Maria?', 'in Wien', ['in den Philippinen', 'in Manila'], 'Ich wohne in Wien.'),
     ('Tom', 'Deutschland', 'Salzburg', 'Deutsch und Englisch', 'Woher kommt Tom?', 'aus Deutschland', ['aus Salzburg', 'aus Österreich'], 'Ich komme aus Deutschland.'),
     ('Ali', 'Österreich', 'Graz', 'Deutsch und Englisch', 'Welche Sprachen spricht Ali?', 'Deutsch und Englisch', ['nur Deutsch', 'Deutsch und Tagalog'], 'Ich spreche Deutsch und Englisch.')],
    [('Sofia', 'Schweiz', 'Innsbruck', 'Deutsch und Englisch', 'Woher kommt Sofia?', 'aus der Schweiz', ['aus Innsbruck', 'aus Deutschland'], 'Ich komme aus der Schweiz.'),
     ('Jose', 'Philippinen', 'Linz', 'Tagalog und Deutsch', 'Wo wohnt Jose?', 'in Linz', ['in den Philippinen', 'in Wien'], 'Ich wohne in Linz.'),
     ('Anna', 'Österreich', 'Klagenfurt', 'Deutsch und Englisch', 'Welche Sprachen spricht Anna?', 'Deutsch und Englisch', ['nur Englisch', 'Deutsch und Tagalog'], 'Ich spreche Deutsch und Englisch.'),
     ('Tom', 'Deutschland', 'Wien', 'Deutsch', 'Was ist richtig?', 'Tom wohnt in Wien.', ['Tom kommt aus Wien.', 'Tom spricht Englisch.'], 'Ich komme aus Deutschland. Ich wohne in Wien.')])

CARD = lambda v, i: choice(i, 'lesen', READ, f'{v[0]}\n{v[1]}\n{v[2]}\nE-Mail: {v[3]}\n{v[4]}', v[5], v[6],
                           E(f'Auf der Karte steht: {v[5]}.', f'The card says: {v[5]}.', f'Nakasulat sa card: {v[5]}.'), [G2], R('Adresse', 'Straße', 'E-Mail'))
fam('LE2', CARD,
    [('Anna Huber', 'Gartengasse 4', '1100 Wien', 'anna.huber@gmx.at', 'Wie heißt die Straße?', 'Gartengasse', ['Wien', 'Huber']),
     ('Jose Cruz', 'Hauptplatz 9', '4020 Linz', 'jose.cruz@aon.at', 'In welcher Stadt wohnt Jose?', 'Linz', ['Cruz', 'Hauptplatz']),
     ('Sofia Berger', 'Bergstraße 21', '5020 Salzburg', 'sofia.b@gmx.at', 'Wie ist die E-Mail-Adresse?', 'sofia.b@gmx.at', ['Bergstraße 21', '5020 Salzburg'])],
    [('Lukas Mayer', 'Ringstraße 7', '9020 Klagenfurt', 'l.mayer@aon.at', 'Wie ist die Hausnummer?', '7', ['9020', '20']),
     ('Maria Santos', 'Feldweg 2', '8010 Graz', 'maria.s@gmx.at', 'Wie heißt die Straße?', 'Feldweg', ['Graz', 'Santos']),
     ('Ali Novak', 'Seegasse 15', '1010 Wien', 'ali.novak@gmx.at', 'Wie ist die Postleitzahl?', '1010', ['15', '1100']),
     ('Tom Weber', 'Kirchplatz 1', '6020 Innsbruck', 'tom.weber@aon.at', 'In welcher Stadt wohnt Tom?', 'Innsbruck', ['Weber', 'Kirchplatz'])])

WHO_P = lambda: img('herkunft', 'Drei Personen mit Namensschild und Flagge.', 'Three people with name tags and flags.', 'Tatlong tao na may name tag at bandila.')
MAP_P = lambda: img('karte', 'Eine Karte mit Deutschland, Österreich und der Schweiz. Ein Punkt zeigt eine Stadt.', 'A map with Germany, Austria and Switzerland. A dot marks a city.', 'Mapa na may Germany, Austria at Switzerland. May tuldok para sa isang lungsod.')
fam('LE3', lambda v, i: choice(i, 'lesen', LOOK(), v[0], v[1], v[2], v[3], [G1], R('woher', 'aus'), img=v[4]()),
    [('Woher kommt Tom?', 'aus Deutschland', ['aus Österreich', 'aus den Philippinen'], L('Über Tom steht „Deutschland“, er hat die Flagge von Deutschland.', 'Above Tom it says “Deutschland”; he has the German flag.', 'Nakasulat ang “Deutschland” sa itaas ni Tom; may bandila siya ng Germany.'), WHO_P),
     ('Woher kommt Anna?', 'aus Österreich', ['aus Deutschland', 'aus der Schweiz'], L('Über Anna steht „Österreich“, sie hat die Flagge von Österreich.', 'Above Anna it says “Österreich”; she has the Austrian flag.', 'Nakasulat ang “Österreich” sa itaas ni Anna; may bandila siya ng Austria.'), WHO_P),
     ('Wer kommt aus den Philippinen?', 'Jose', ['Anna', 'Tom'], L('Über Jose steht „Philippinen“, er hat die Flagge der Philippinen.', 'Above Jose it says “Philippinen”; he has the flag of the Philippines.', 'Nakasulat ang “Philippinen” sa itaas ni Jose; may bandila siya ng Pilipinas.'), WHO_P)],
    [('Ist Graz auf der Karte?', 'Nein, nur Wien.', ['Ja, Graz und Wien.', 'Ja, nur Graz.'], L('Auf der Karte steht nur eine Stadt: Wien.', 'Only one city is on the map: Vienna.', 'Isang lungsod lang ang nasa mapa: Vienna.'), MAP_P),
     ('Wie viele Länder sind auf der Karte?', 'drei', ['zwei', 'vier'], L('Deutschland, Österreich, die Schweiz: drei Länder.', 'Germany, Austria, Switzerland: three countries.', 'Germany, Austria, Switzerland: tatlong bansa.'), MAP_P)])

DOCH = lambda v, i: choice(i, 'lesen', READ, f'A: {v[0]}\nB: {v[1]}\n{v[2]}', v[3], [v[4]], v[5], [G5], R('doch', 'ja', 'nein'))
fam('LE4', DOCH,
    [('Wohnen Sie nicht in Wien?', 'Doch.', 'Wohnt B in Wien?', 'Ja.', 'Nein.', L('„Doch“ auf eine Frage mit „nicht“ = ja, das stimmt.', '“Doch” to a question with “nicht” = yes, that is right.', '“Doch” sa tanong na may “nicht” = oo, tama.')),
     ('Sprechen Sie Englisch?', 'Nein, nur Deutsch.', 'Spricht B Englisch?', 'Nein.', 'Ja.', L('B sagt „Nein, nur Deutsch.“', 'B says “Nein, nur Deutsch.”', 'Sabi ni B: “Nein, nur Deutsch.”')),
     ('Kommen Sie nicht aus Graz?', 'Doch, aus Graz.', 'Kommt B aus Graz?', 'Ja.', 'Nein.', L('„Doch, aus Graz“ = B kommt aus Graz.', '“Doch, aus Graz” = B comes from Graz.', '“Doch, aus Graz” = taga-Graz si B.'))],
    [('Verstehen Sie nicht?', 'Doch, ich verstehe.', 'Versteht B?', 'Ja.', 'Nein.', L('„Doch, ich verstehe.“ = B versteht.', '“Doch, ich verstehe.” = B understands.', '“Doch, ich verstehe.” = naiintindihan ni B.')),
     ('Wohnen Sie in Linz?', 'Nein, in Wels.', 'Wohnt B in Linz?', 'Nein.', 'Ja.', L('B wohnt in Wels, nicht in Linz.', 'B lives in Wels, not in Linz.', 'Sa Wels nakatira si B, hindi sa Linz.')),
     ('Kommst du nicht aus Manila?', 'Doch!', 'Kommt B aus Manila?', 'Ja.', 'Nein.', L('„Doch!“ = ja, B kommt aus Manila.', '“Doch!” = yes, B comes from Manila.', '“Doch!” = oo, taga-Manila si B.')),
     ('Kommst du aus der Schweiz?', 'Nein, aus Deutschland.', 'Kommt B aus der Schweiz?', 'Nein.', 'Ja.', L('B kommt aus Deutschland.', 'B comes from Germany.', 'Taga-Germany si B.'))])

# ================================================================ SCHREIBEN
FORM = lambda v, i: cloze(i, 'schreiben', L('Lesen Sie den Text. Ergänzen Sie das Formular.', 'Read the text. Complete the form.', 'Basahin ang teksto. Kumpletuhin ang form.'),
                          f'Ich bin {v[0]}. Ich komme {AUS[v[1]]} und wohne jetzt in {v[2]}.\nHeimatland: {{{{1}}}} · Wohnort: {{{{2}}}}', [[v[1], f'die {v[1]}'] if v[1] != 'Österreich' and v[1] != 'Deutschland' else [v[1]], [v[2]]],
                          E(f'Heimatland = {v[1]}, Wohnort = {v[2]}.', f'Home country = {v[1]}, place of residence = {v[2]}.', f'Sariling bansa = {v[1]}, tirahan = {v[2]}.'), [G1, G2], R('Heimatland', 'wohnen'))
fam('SC1', FORM, [('Jose Cruz', 'Philippinen', 'Graz'), ('Tom Weber', 'Deutschland', 'Wien'), ('Sofia Berger', 'Schweiz', 'Linz')],
    [('Anna Huber', 'Österreich', 'Salzburg'), ('Maria Santos', 'Philippinen', 'Innsbruck'), ('Lukas Mayer', 'Österreich', 'Klagenfurt'), ('Ali Novak', 'Österreich', 'Wels')])

fam('SC2', lambda v, i: cloze(i, 'schreiben', L(f'Antworten Sie. ({v[2]})', f'Answer. ({v[3]})', f'Sumagot. ({v[4]})'), f'{v[0]}\n{v[1]}', v[5],
    E(f'Antwort: „{v[6]}“', f'Answer: “{v[6]}”', f'Sagot: “{v[6]}”'), [G1, G2, G3], R('wohnen', 'aus', 'sprechen')),
    [('Wo wohnen Sie?', 'Ich {{1}} (wohnen) {{2}} Graz.', 'Graz', 'You live in Graz', 'Nakatira ka sa Graz', [['wohne'], ['in']], 'Ich wohne in Graz.'),
     ('Woher kommen Sie?', 'Ich {{1}} (kommen) {{2}} Deutschland.', 'Deutschland', 'You come from Germany', 'Taga-Germany ka', [['komme'], ['aus']], 'Ich komme aus Deutschland.'),
     ('Welche Sprachen sprechen Sie?', 'Ich {{1}} (sprechen) Tagalog {{2}} Englisch.', 'Tagalog + Englisch', 'Tagalog and English', 'Tagalog at Ingles', [['spreche'], ['und']], 'Ich spreche Tagalog und Englisch.')],
    [('Wo wohnst du?', 'Ich {{1}} (wohnen) {{2}} Linz.', 'Linz', 'You live in Linz', 'Nakatira ka sa Linz', [['wohne'], ['in']], 'Ich wohne in Linz.'),
     ('Woher kommst du?', 'Ich {{1}} (kommen) {{2}} Österreich.', 'Österreich', 'You come from Austria', 'Taga-Austria ka', [['komme'], ['aus']], 'Ich komme aus Österreich.'),
     ('Sprechen Sie Englisch?', '{{1}}, ich {{2}} (sprechen) Englisch.', 'ja', 'Yes, you do', 'Oo', [['Ja'], ['spreche']], 'Ja, ich spreche Englisch.'),
     ('Wohnen Sie nicht in Graz?', '{{1}}, ich wohne in Graz.', 'Sie wohnen in Graz', 'You do live in Graz', 'Nakatira ka nga sa Graz', [['Doch']], 'Doch, ich wohne in Graz.')])

MSG = lambda v, i: cloze(i, 'schreiben', L('Ergänzen Sie die Nachricht.', 'Complete the message.', 'Kumpletuhin ang mensahe.'), f'Hallo! Ich heiße {v[0]}. Ich {{{{1}}}} (kommen) {AUS[v[1]]} und {{{{2}}}} (wohnen) in {v[2]}. Ich {{{{3}}}} (sprechen) {v[3]}.',
                         [['komme'], ['wohne'], ['spreche']], E('ich heiße, ich komme, ich wohne, ich spreche – bei „ich“ endet das Verb auf -e.', 'ich heiße, ich komme, ich wohne, ich spreche – with “ich” the verb ends in -e.', 'ich heiße, komme, wohne, spreche – sa “ich”, nagtatapos sa -e ang verb.'), [G7], R('heißen', 'kommen', 'wohnen', 'sprechen'))
fam('SC3', MSG, [('Maria', 'Philippinen', 'Wien', 'Tagalog'), ('Lukas', 'Österreich', 'Graz', 'Deutsch'), ('Sofia', 'Schweiz', 'Salzburg', 'Deutsch und Englisch')],
    [('Jose', 'Philippinen', 'Linz', 'Tagalog und Deutsch'), ('Anna', 'Österreich', 'Wien', 'Deutsch und Englisch'), ('Tom', 'Deutschland', 'Innsbruck', 'Deutsch'), ('Ali', 'Österreich', 'Wels', 'Deutsch und Englisch')])

# ================================================================ SPRECHEN (focus; A1-SPR-T1 introduce yourself, A1-SPR-T2 Wortkarte)
fam('SP1', lambda v, i: choice(i, 'sprechen', L(f'{v[0]} Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', f'{v[1]} What do you say? Choose, then say it aloud.', f'{v[2]} Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'), v[3], v[4], v[5],
    E(f'Passend: „{v[4]}“', f'A fitting answer: “{v[4]}”', f'Angkop: “{v[4]}”'), [G1, G2, G3], R('aus', 'in', 'wohnen')),
    [('Sie kommen aus den Philippinen.', 'You come from the Philippines.', 'Taga-Pilipinas ka.', 'Woher kommen Sie?', 'Ich komme aus den Philippinen.', ['Ich wohne aus den Philippinen.', 'Ich komme in den Philippinen.']),
     ('Sie wohnen in Graz.', 'You live in Graz.', 'Nakatira ka sa Graz.', 'Wo wohnen Sie?', 'Ich wohne in Graz.', ['Ich wohne aus Graz.', 'Ich komme in Graz.']),
     ('Sie sprechen Tagalog und Deutsch.', 'You speak Tagalog and German.', 'Marunong ka ng Tagalog at German.', 'Welche Sprachen sprechen Sie?', 'Ich spreche Tagalog und Deutsch.', ['Ich sprecht Tagalog und Deutsch.', 'Ich bin Tagalog und Deutsch.'])],
    [('Sie kommen aus Österreich.', 'You come from Austria.', 'Taga-Austria ka.', 'Woher kommst du?', 'Ich komme aus Österreich.', ['Ich komme in Österreich.', 'Ich bin aus Österreich kommen.']),
     ('Sie wohnen in Wien.', 'You live in Vienna.', 'Nakatira ka sa Vienna.', 'Wo wohnst du?', 'Ich wohne in Wien.', ['Ich wohnst in Wien.', 'Ich wohne aus Wien.']),
     ('Sie sprechen Englisch.', 'You speak English.', 'Marunong ka ng Ingles.', 'Sprechen Sie Englisch?', 'Ja, ich spreche Englisch.', ['Doch, ich spreche Englisch.', 'Ja, ich bin Englisch.']),
     ('Ihr Heimatland ist Deutschland.', 'Your home country is Germany.', 'Germany ang sariling bansa mo.', 'Was ist Ihr Heimatland?', 'Deutschland.', ['In Deutschland wohnen.', 'Aus Deutschland heißen.'])])

CARDQ = {'Wohnort?': 'Wo wohnen Sie?', 'Herkunft?': 'Woher kommen Sie?', 'Sprachen?': 'Welche Sprachen sprechen Sie?', 'Name?': 'Wie heißen Sie?', 'Adresse?': 'Wie ist Ihre Adresse?', 'Hobby?': 'Was ist Ihr Hobby?', 'E-Mail?': 'Wie ist Ihre E-Mail-Adresse?'}
fam('SP2', lambda v, i: choice(i, 'sprechen', L('Wortkarte: Stellen Sie die Frage. Wählen Sie, dann sagen Sie es laut.', 'Word card: ask the question. Choose, then say it aloud.', 'Word card: itanong. Pumili, tapos sabihin nang malakas.'), f'Wortkarte: {v[0]}', CARDQ[v[0]], [CARDQ[k] for k in v[1]],
    E(f'Zur Wortkarte „{v[0]}“ passt: „{CARDQ[v[0]]}“ (Prüfung: Sprechen Teil 2).', f'For the word card “{v[0]}”, ask: “{CARDQ[v[0]]}” (exam: speaking part 2).', f'Para sa word card “{v[0]}”: “{CARDQ[v[0]]}” (exam: speaking part 2).'), [G5, G2], R('wo', 'woher')),
    [('Wohnort?', ['Herkunft?', 'Name?']), ('Herkunft?', ['Wohnort?', 'Sprachen?']), ('Sprachen?', ['Herkunft?', 'Adresse?'])],
    [('Adresse?', ['Wohnort?', 'Name?']), ('Hobby?', ['Sprachen?', 'Name?']), ('E-Mail?', ['Adresse?', 'Wohnort?']), ('Name?', ['Herkunft?', 'Hobby?'])])

HELP = {'slow': ('Die Person spricht sehr schnell.', 'The person talks very fast.', 'Masyadong mabilis magsalita ang tao.', 'Langsam, bitte!'),
        'again': ('Sie haben das Wort nicht verstanden.', 'You did not understand the word.', 'Hindi mo naintindihan ang salita.', 'Wiederholen Sie, bitte.'),
        'spell': ('Sie wissen nicht, wie man die Straße schreibt.', 'You don’t know how the street is written.', 'Hindi mo alam kung paano isulat ang kalye.', 'Wie schreibt man das?'),
        'lang': ('Sie möchten Englisch sprechen.', 'You would like to speak English.', 'Gusto mong mag-Ingles.', 'Sprechen Sie Englisch?'),
        'bye': ('Das Telefongespräch ist zu Ende.', 'The phone call is over.', 'Tapos na ang tawag sa telepono.', 'Auf Wiederhören!'),
        'not': ('Sie verstehen nichts.', 'You understand nothing.', 'Wala kang naintindihan.', 'Ich verstehe nicht.')}
fam('SP3', lambda v, i: choice(i, 'sprechen', L(HELP[v[0]][0] + ' Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', HELP[v[0]][1] + ' What do you say? Choose, then say it aloud.', HELP[v[0]][2] + ' Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'), None, HELP[v[0]][3], [HELP[k][3] for k in v[1]],
    E(f'Passend: „{HELP[v[0]][3]}“', f'A fitting answer: “{HELP[v[0]][3]}”', f'Angkop: “{HELP[v[0]][3]}”'), [G4], R('verstehen', 'langsam', 'wiederholen')),
    [('slow', ['bye', 'lang']), ('again', ['slow', 'bye']), ('spell', ['lang', 'slow'])], [('lang', ['spell', 'bye']), ('bye', ['again', 'lang']), ('not', ['bye', 'lang']), ('slow', ['spell', 'bye'])])

INTRO_SAY = lambda v, i: choice(i, 'sprechen', L(f'Stellen Sie sich vor: {v[0]}. Wählen Sie, dann sagen Sie es laut.', f'Introduce yourself: {v[0]}. Choose, then say it aloud.', f'Ipakilala ang sarili: {v[0]}. Pumili, tapos sabihin nang malakas.'), None, v[1], v[2],
                                E(f'Richtig: „{v[1]}“ – komme aus …, wohne in …', f'Correct: “{v[1]}” – komme aus …, wohne in …', f'Tama: “{v[1]}” – komme aus …, wohne in …'), [G1, G2], R('aus', 'in', 'wohnen'))
fam('SP4', INTRO_SAY,
    [('Maria – Philippinen – Wien', 'Ich heiße Maria. Ich komme aus den Philippinen und wohne in Wien.', ['Ich heiße Maria. Ich komme in den Philippinen und wohne aus Wien.', 'Ich bin Maria. Ich wohne aus den Philippinen und komme in Wien.']),
     ('Tom – Deutschland – Salzburg', 'Ich heiße Tom. Ich komme aus Deutschland und wohne in Salzburg.', ['Ich heiße Tom. Ich komme aus Salzburg und wohne in Deutschland.', 'Ich heiße Tom. Ich wohne aus Deutschland in Salzburg.']),
     ('Sofia – Schweiz – Linz', 'Ich heiße Sofia. Ich komme aus der Schweiz und wohne in Linz.', ['Ich heiße Sofia. Ich komme aus Schweiz und wohne aus Linz.', 'Ich heiße Sofia. Ich komme in der Schweiz und wohne in Linz.'])],
    [('Jose – Philippinen – Graz', 'Ich heiße Jose. Ich komme aus den Philippinen und wohne in Graz.', ['Ich heiße Jose. Ich wohne aus den Philippinen und komme in Graz.', 'Ich heiße Jose. Ich komme in Graz und wohne aus den Philippinen.']),
     ('Anna – Österreich – Klagenfurt', 'Ich heiße Anna. Ich komme aus Österreich und wohne in Klagenfurt.', ['Ich heiße Anna. Ich komme in Österreich und wohne aus Klagenfurt.', 'Ich heiße Anna. Ich wohne aus Österreich.']),
     ('Ali – Österreich – Linz', 'Ich heiße Ali. Ich komme aus Österreich und wohne in Linz.', ['Ich heiße Ali. Ich wohne aus Österreich und komme in Linz.', 'Ich heiße Ali. Ich komme aus Linz und wohne in Österreich.']),
     ('Tom – Deutschland – Wien', 'Ich heiße Tom. Ich komme aus Deutschland und wohne in Wien.', ['Ich heiße Tom. Ich komme in Deutschland und wohne aus Wien.', 'Ich heiße Tom. Ich komme aus Wien und wohne in Deutschland.'])])

YND = lambda v, i: choice(i, 'sprechen', L(f'{v[0]} Antworten Sie. Wählen Sie, dann sagen Sie es laut.', f'{v[1]} Answer. Choose, then say it aloud.', f'{v[2]} Sumagot. Pumili, tapos sabihin nang malakas.'), v[3], v[4], v[5],
                          E('Frage mit „nicht“ + positive Antwort → „Doch“. Sonst „Ja“ oder „Nein“.', 'Question with “nicht” + positive answer → “Doch”. Otherwise “Ja” or “Nein”.', 'Tanong na may “nicht” + positibong sagot → “Doch”. Kung hindi, “Ja” o “Nein”.'), [G5], R('doch', 'ja', 'nein'))
fam('SP5', YND,
    [('Sie wohnen in Wien.', 'You live in Vienna.', 'Nakatira ka sa Vienna.', 'Wohnen Sie nicht in Wien?', 'Doch, ich wohne in Wien.', ['Ja, ich wohne nicht in Wien.', 'Nein, ich wohne in Wien.']),
     ('Sie kommen aus Linz.', 'You come from Linz.', 'Taga-Linz ka.', 'Kommen Sie aus Wien?', 'Nein, ich komme aus Linz.', ['Doch, ich komme aus Linz.', 'Ja, ich komme aus Linz.']),
     ('Sie kommen aus Graz.', 'You come from Graz.', 'Taga-Graz ka.', 'Kommen Sie nicht aus Graz?', 'Doch, aus Graz.', ['Nein, aus Graz.', 'Ja, nicht aus Graz.'])],
    [('Sie verstehen.', 'You understand.', 'Naiintindihan mo.', 'Verstehen Sie nicht?', 'Doch, ich verstehe.', ['Nein, ich verstehe.', 'Ja, ich verstehe nicht.']),
     ('Sie sprechen Englisch.', 'You speak English.', 'Marunong ka ng Ingles.', 'Sprechen Sie Englisch?', 'Ja, ich spreche Englisch.', ['Doch, ich spreche Englisch.', 'Nein, ich spreche Englisch.']),
     ('Sie kommen nicht aus der Schweiz.', 'You do not come from Switzerland.', 'Hindi ka taga-Switzerland.', 'Kommen Sie aus der Schweiz?', 'Nein, ich komme aus Österreich.', ['Doch, ich komme aus Österreich.', 'Ja, ich komme aus Österreich.']),
     ('Sie wohnen in einem Dorf.', 'You live in a village.', 'Nakatira ka sa baryo.', 'Wohnen Sie nicht in einem Dorf?', 'Doch, in einem Dorf.', ['Nein, in einem Dorf.', 'Ja, nicht in einem Dorf.'])])

# ================================================================ GRAMMATIK / WORTSCHATZ
ARTX = L('Den Artikel immer mit dem Nomen lernen: der Mensch, die Stadt, das Land.', 'Always learn the article with the noun: der Mensch, die Stadt, das Land.', 'Laging isaulo ang article kasama ng noun: der Mensch, die Stadt, das Land.')
fam('GW1', lambda v, i: choice(i, 'grammatikWortschatz', CHOOSE, f'… {v[0]}', v[1], [a for a in ('der', 'die', 'das') if a != v[1]], L(f'{v[1]} {v[0]}. ' + ARTX['de'], f'{v[1]} {v[0]}. ' + ARTX['en'], f'{v[1]} {v[0]}. ' + ARTX['tl']), [G6], R(v[0])),
    [('Stadt', 'die'), ('Dorf', 'das'), ('Mensch', 'der')], [('Sprache', 'die'), ('Land', 'das'), ('Adresse', 'die'), ('Hobby', 'das')])

fam('GW2', lambda v, i: cloze(i, 'grammatikWortschatz', GAPS, v[0], [[v[1]]], E('der/das → ein, die → eine.', 'der/das → ein (a), die → eine (a).', 'der/das → ein (isang), die → eine (isang).'), [G6], R('ein')),
    [('Linz ist {{1}} Stadt.', 'eine'), ('Das ist {{1}} Dorf.', 'ein'), ('Tagalog ist {{1}} Sprache.', 'eine')], [('Österreich ist {{1}} Land.', 'ein'), ('Jose ist {{1}} Mensch aus Manila.', 'ein'), ('Das ist {{1}} Straße in Graz.', 'eine'), ('Das ist {{1}} Adresse in Wien.', 'eine')])

fam('GW3', lambda v, i: cloze(i, 'grammatikWortschatz', GAPS, v[0].replace('{{1}}', '{{1}} (' + v[3] + ')'), [[v[1]]], E(v[2] + ' – Formen mitlernen.', v[2].replace('mit', 'with') + ' – learn the forms.', v[2].replace('mit', 'may') + ' – isaulo ang anyo.'), [G7], R(v[3])),
    [('Er {{1}} Tagalog.', 'spricht', 'sprechen: er spricht (e → i).', 'sprechen'), ('Du {{1}} mir die Adresse.', 'gibst', 'geben: du gibst (e → i).', 'geben'), ('Maria {{1}} die Adresse.', 'nimmt', 'nehmen: sie nimmt (e → i).', 'nehmen')],
    [('Du {{1}} Deutsch.', 'sprichst', 'sprechen: du sprichst.', 'sprechen'), ('Maria {{1}} mir die Telefonnummer.', 'gibt', 'geben: sie gibt.', 'geben'), ('Du {{1}} das.', 'nimmst', 'nehmen: du nimmst.', 'nehmen'), ('Er {{1}} die Straße nicht.', 'findet', 'finden: er findet (mit -et).', 'finden')])

QO = lambda v, i: choice(i, 'grammatikWortschatz', L('Welche Frage ist richtig?', 'Which question is correct?', 'Aling tanong ang tama?'), None, v[0], v[1], E('Ja/Nein-Frage: Verb auf Platz 1. W-Frage: Fragewort, dann Verb.', 'Yes/no question: verb first. W-question: question word, then verb.', 'Oo/hindi: una ang verb. W-question: tanong na salita, tapos verb.'), [G5], R('wo'))
fam('GW4', QO, [('Wohnen Sie in Graz?', ['Sie wohnen in Graz?', 'In Graz Sie wohnen?']), ('Kommst du aus Deutschland?', ['Du aus Deutschland kommst?', 'Aus Deutschland du kommst?']), ('Wohnt Maria in Wien?', ['Maria in Wien wohnt?', 'In Wien Maria wohnt?'])],
    [('Spricht er Englisch?', ['Er Englisch spricht?', 'Englisch er spricht?']), ('Woher kommen Sie?', ['Woher Sie kommen?', 'Sie woher kommen?']), ('Verstehen Sie Deutsch?', ['Sie Deutsch verstehen?', 'Deutsch Sie verstehen?']), ('Wo ist die Bahnhofstraße?', ['Wo die Bahnhofstraße ist?', 'Die Bahnhofstraße wo ist?'])])

fam('GW5', lambda v, i: choice(i, 'grammatikWortschatz', CHOOSE, v[0], v[1], v[2], E('aus = Herkunft (woher?), in = Ort (wo?).', 'aus = origin (where from?), in = place (where?).', 'aus = pinagmulan (woher?), in = lugar (wo?).'), [G1, G2], R('aus', 'in')),
    [('Ich wohne … Wien.', 'in', ['aus', 'woher']), ('Ich komme … Deutschland.', 'aus', ['in', 'wo']), ('… wohnen Sie? – In Graz.', 'Wo', ['Woher', 'Wie'])],
    [('Jose kommt … den Philippinen.', 'aus', ['in', 'wo']), ('Wir wohnen … einem Dorf.', 'in', ['aus', 'woher']), ('… kommen Sie? – Aus Linz.', 'Woher', ['Wo', 'Wie']), ('Anna wohnt … Salzburg.', 'in', ['aus', 'woher'])])

NAT = lambda v, i: choice(i, 'grammatikWortschatz', CHOOSE, v[0], v[1], v[2], E('Mann: Österreicher, Philippiner. Frau: mit -in.', 'Man: Österreicher, Philippiner. Woman: with -in.', 'Lalaki: Österreicher, Philippiner. Babae: may -in.'), [G1], R('Österreicher, Österreicherin', 'Philippiner, Philippinerin'))
fam('GW6', NAT, [], [('Maria kommt aus den Philippinen. Sie ist …', 'Philippinerin', ['Philippiner', 'Österreicherin']), ('Lukas kommt aus Wien. Er ist …', 'Österreicher', ['Österreicherin', 'Philippiner']),
                     ('Herr Santos kommt aus Manila. Er ist …', 'Philippiner', ['Philippinerin', 'Österreicher']), ('Frau Huber kommt aus Graz. Sie ist …', 'Österreicherin', ['Österreicher', 'Philippinerin'])])

# ================================================================ WERTE (A1-WOW-19, A1-WOW-01; Q36; format A1-WOW-T1 a/b)
WOW = L('Österreich: Hauptstadt Wien · Geld Euro · Staatssprache Deutsch · in der EU. Deutsch hilft bei der Arbeit, auf dem Amt und in der Schule.',
        'Austria: capital Vienna · money euro · official language German · in the EU. German helps at work, at public offices and at school.',
        'Austria: kabisera Vienna · pera euro · opisyal na wika German · nasa EU. Nakakatulong ang German sa trabaho, sa opisina ng gobyerno at sa paaralan.')
WA = lambda v, i: choice(i, 'werte', CHOOSE, v[0], v[1], [v[2]], L(v[3] + ' ' + WOW['de'], v[4] + ' ' + WOW['en'], v[5] + ' ' + WOW['tl']), [G8], R('Österreich'))
fam('WE1', WA, [('Die Hauptstadt von Österreich ist …', 'Wien', 'Salzburg', 'Hauptstadt: Wien.', 'Capital: Vienna.', 'Kabisera: Vienna.'),
                ('Das Geld in Österreich ist …', 'der Euro', 'der Dollar', 'Heute zahlt man in Österreich mit Euro.', 'Today you pay with euros in Austria.', 'Euro ang pambayad ngayon sa Austria.'),
                ('Die Staatssprache in Österreich ist …', 'Deutsch', 'Englisch', 'Staatssprache: Deutsch.', 'Official language: German.', 'Opisyal na wika: German.')],
    [('Wien ist …', 'die Hauptstadt von Österreich', 'ein Dorf in Österreich', 'Wien ist die Hauptstadt.', 'Vienna is the capital.', 'Kabisera ang Vienna.'),
     ('Welche Sprache spricht man auf dem Amt in Österreich?', 'Deutsch', 'Englisch', 'Die Amtssprache ist Deutsch.', 'The official language is German.', 'German ang wika sa opisina ng gobyerno.')])
fam('WE2', WA, [('Ist Österreich in der EU?', 'Ja.', 'Nein.', 'Österreich ist in der EU.', 'Austria is in the EU.', 'Nasa EU ang Austria.'),
                ('Welches Land ist in der EU?', 'Österreich', 'die Schweiz', 'Österreich ist in der EU, die Schweiz nicht.', 'Austria is in the EU, Switzerland is not.', 'Nasa EU ang Austria, ang Switzerland ay hindi.'),
                ('EU heißt …', 'Europäische Union', 'Europäische Stadt', 'EU = Europäische Union.', 'EU = European Union.', 'EU = European Union.')],
    [('Österreich ist ein Land in …', 'Europa', 'den Philippinen', 'Österreich liegt in Europa.', 'Austria is in Europe.', 'Nasa Europa ang Austria.'),
     ('Ist Deutschland in der EU?', 'Ja.', 'Nein.', 'Auch Deutschland ist in der EU.', 'Germany is in the EU too.', 'Nasa EU rin ang Germany.')])
fam('WE3', WA, [('Deutsch hilft …', 'bei der Arbeit und im Alltag', 'nur in Deutschland', 'Deutsch ist die Staatssprache.', 'German is the official language.', 'German ang opisyal na wika.'),
                ('Auf dem Amt in Österreich spricht man …', 'Deutsch', 'Englisch', 'Auf dem Amt spricht man Deutsch.', 'At public offices people speak German.', 'German ang gamit sa opisina ng gobyerno.'),
                ('In der Schule in Österreich spricht man …', 'Deutsch', 'Tagalog', 'In der Schule spricht man Deutsch.', 'At school people speak German.', 'German ang gamit sa paaralan.')],
    [('Hilft Deutsch bei der Arbeit?', 'Ja.', 'Nein.', 'Mit Deutsch findet man leichter Arbeit.', 'With German it is easier to find work.', 'Mas madaling makahanap ng trabaho kung marunong ng German.'),
     ('Hilft Deutsch auf dem Amt?', 'Ja.', 'Nein.', 'Auf dem Amt spricht man Deutsch.', 'At public offices people speak German.', 'German ang gamit sa opisina ng gobyerno.')])
AT_P = lambda: img('oesterreich', 'Österreich mit einem Stern für die Hauptstadt, eine Euro-Münze, die Flagge der EU und die Flagge von Österreich.', 'Austria with a star for the capital, a euro coin, the EU flag and the Austrian flag.', 'Austria na may bituin para sa kabisera, euro coin, bandila ng EU at ng Austria.')
fam('WE4', lambda v, i: choice(i, 'werte', LOOK(), v[0], v[1], [v[2]], L(v[3] + ' ' + WOW['de'], v[3] + ' ' + WOW['en'], v[3] + ' ' + WOW['tl']), [G8], R('Österreich'), img=AT_P()),
    [], [('Die Hauptstadt im Bild ist …', 'Wien', 'Graz', 'Wien.'), ('Das Geld im Bild ist …', 'der Euro', 'der Dollar', 'Euro.'),
         ('Ist Graz die Hauptstadt?', 'Nein, Wien.', 'Ja.', 'Wien.'), ('Im Bild sind die Flagge von Österreich und die Flagge der …', 'EU', 'Schweiz', 'EU.'),
         ('Ist Österreich in der EU?', 'Ja.', 'Nein.', 'Nur Wien.'), ('Wien ist eine Stadt in …', 'Österreich', 'Deutschland', 'Wien.')])


# ================================================================ checks + write
def interleave(groups):
    out = []
    for k in range(max(len(g) for g in groups)):
        out += [g[k] for g in groups if k < len(g)]
    return out


def group(lst, key):
    d = {}
    for x in lst:
        d.setdefault(key(x), []).append(x)
    return list(d.values())


order = interleave(interleave(group(group(PRACTICE, lambda p: p.get('family', p['id'])), lambda f: f[0]['skill'])))
rest = order[40:]
quota = {'lesen': 3, 'hoeren': 3, 'schreiben': 3, 'sprechen': 5, 'grammatikWortschatz': 3, 'werte': 3}
rs = Counter(p['skill'] for p in rest)
print('test', len(TEST), dict(Counter(t['skill'] for t in TEST)))
print('practice', len(PRACTICE), dict(Counter(p['skill'] for p in PRACTICE)))
for s, q in quota.items():
    if rs[s] < 2 * q:
        print(f'  ! rest {s}: {rs[s]} < {2 * q}')
json.dump({'chapterId': CH, 'goals': GOALS, 'pools': {'practice': PRACTICE, 'test': TEST}}, open(f'{ROOT}/src/lib/content/a1-03-pools.json', 'w'), ensure_ascii=False, indent='\t')
