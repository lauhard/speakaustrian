# A1-02 pools -> src/lib/content/a1-02-pools.json
import json
from collections import Counter, defaultdict
from gen_a102_common import *

TEST, PRACTICE = [], []


def fam(code, fn, test, practice):
    """Test: one family of 3 (base + 2 twins, R-K3). Practice: pairs."""
    assert len(test) in (0, 3) and len(practice) % 2 == 0, code
    t = [fn(v, f'{CH}-T-{code}-{n}') for n, v in enumerate(test, 1)]
    for it in t[1:]:
        it['family'] = t[0]['id']
    p = [fn(v, f'{CH}-P-{code}-{n}') for n, v in enumerate(practice, 1)]
    for a, b in zip(p[::2], p[1::2]):
        b['family'] = a['id']
    TEST.extend(t)
    PRACTICE.extend(p)


E3 = lambda de_, en, tl: L(de_, en, tl)
swap = lambda n: int(str(n)[::-1])
acc = lambda w: 'einen' + w[3:] if w.startswith('ein Euro') else w  # 'kosten' + accusative: 'Das kostet einen Euro …'

# ================================================================ HÖREN (exam format A1-HOE-T2: a/b)
fam('HO1', lambda v, i: choice(i, 'hoeren', L('Hören Sie. Wie viel kostet das?', 'Listen. How much does it cost?', 'Makinig. Magkano ito?'), None, euro(v[0])[0], [euro(v[1])[0]],
    E3(f'Sie hören: „{euro(v[0])[1]}“ = {euro(v[0])[0]}. Zuerst die Euro, dann die Cent.', f'You hear: “{euro(v[0])[1]}” = {euro(v[0])[0]}. First euros, then cents.', f'Naririnig mo: “{euro(v[0])[1]}” = {euro(v[0])[0]}. Una euro, tapos cent.'),
    [G5, G2], R('kosten', 'Euro', 'Cent'), audio=f'Das kostet {euro(v[0])[1]}.'),
    [(790, 970), (1250, 1520), (345, 354)], [(680, 860), (1430, 1340), (275, 257), (1990, 1909), (560, 650), (2120, 1220)])

fam('HO2', lambda v, i: choice(i, 'hoeren', L('Hören Sie. Wie ist die Telefonnummer?', 'Listen. What is the phone number?', 'Makinig. Ano ang numero ng telepono?'), None, v[0], [v[1]],
    E3(f'Sie hören: {digits(v[0])}.', f'You hear: {digits(v[0])}.', f'Naririnig mo: {digits(v[0])}.'), [G4, G2], R('Telefonnummer', 'Nummer'), audio=f'Die Nummer ist {digits(v[0])}.'),
    [('0664 52 18', '0664 25 18'), ('0676 9034', '0676 9304'), ('0699 71 66', '0699 17 66')],
    [('0650 38 42', '0650 83 42'), ('0664 11 79', '0664 11 97'), ('0676 25 05', '0676 52 05'), ('0699 40 13', '0699 40 31')])

fam('HO3', lambda v, i: choice(i, 'hoeren', L('Hören Sie. Jemand buchstabiert den Familiennamen. Wie schreibt man den Namen?', 'Listen. Someone spells the family name. How is it written?', 'Makinig. May nag-i-spell ng apelyido. Paano ito isinusulat?'), None, v[0], v[1],
    E3(f'Sie hören: {spell(v[0])[:-1]}. Die Namen klingen ähnlich – darum buchstabiert man.', f'You hear: {spell(v[0])[:-1]}. The names sound alike – that is why people spell names.', f'Naririnig mo: {spell(v[0])[:-1]}. Magkatunog ang mga pangalan – kaya nag-i-spell.'),
    [G1], R('buchstabieren', 'Familienname'), audio=f'Der Familienname: {spell_audio(v[0])}'),
    [('Schmid', ['Schmidt']), ('Mayer', ['Maier']), ('Lehner', ['Lener'])],
    [('Fischer', ['Vischer']), ('Novak', ['Nowak']), ('Reyes', ['Reies']), ('Cruz', ['Kruz']), ('Fuchs', ['Fux']), ('Seidl', ['Seidel'])])

fam('HO4', lambda v, i: choice(i, 'hoeren', L('Hören Sie. Wie alt ist die Person?', 'Listen. How old is the person?', 'Makinig. Ilang taon na ang tao?'), None, str(v), [str(swap(v))],
    E3(f'Sie hören „{de(v)}“: zuerst {v % 10}, dann {v - v % 10}. Das ist {v}.', f'You hear “{de(v)}”: first {v % 10}, then {v - v % 10}. That is {v}.', f'Naririnig mo ang “{de(v)}”: una {v % 10}, tapos {v - v % 10}. Iyan ay {v}.'),
    [G3, G2], R('Jahre alt'), audio=f'Ich bin {de(v)} Jahre alt.'),
    [47, 36, 58], [29, 41, 67, 83, 52, 74])

fam('HO5', lambda v, i: choice(i, 'hoeren', L('Hören Sie. Was ist die Hausnummer?', 'Listen. What is the house number?', 'Makinig. Ano ang numero ng bahay?'), None, str(v[0]), [str(v[1])],
    E3(f'Sie hören „{de(v[0])}“ = {v[0]}. 13–19 enden auf „-zehn“, 20, 30 … auf „-zig“ oder „-ßig“.', f'You hear “{de(v[0])}” = {v[0]}. 13–19 end in “-zehn”, 20, 30 … in “-zig” or “-ßig”.', f'Naririnig mo ang “{de(v[0])}” = {v[0]}. Ang 13–19 ay nagtatapos sa “-zehn”, ang 20, 30 … sa “-zig” o “-ßig”.'),
    [G4, G2], R('Hausnummer'), audio=f'Die Hausnummer ist {de(v[0])}.'),
    [(13, 30), (60, 16), (18, 80)], [(14, 40), (50, 15), (17, 70), (90, 19), (30, 13), (16, 60)])

fam('HO6', lambda v, i: short(i, 'hoeren', DIGITS, 'Die Zahl:', [str(v)], E3(f'Sie hören „{de(v)}“ = {v}.', f'You hear “{de(v)}” = {v}.', f'Naririnig mo ang “{de(v)}” = {v}.'), [G2], R('Zahl'), audio=de(v)),
    [58, 93, 71], [44, 27, 86, 65, 39, 12])

fam('HO7', lambda v, i: choice(i, 'hoeren', L('Hören Sie. Wie ist die Postleitzahl?', 'Listen. What is the postcode?', 'Makinig. Ano ang postal code?'), None, v[0], [v[1]],
    E3(f'Sie hören: {digits(v[0])} = {v[0]}.', f'You hear: {digits(v[0])} = {v[0]}.', f'Naririnig mo: {digits(v[0])} = {v[0]}.'), [G4], R('Postleitzahl'), audio=f'Die Postleitzahl ist {digits(v[0])}.'),
    [], [('4020', '4200'), ('5020', '5002'), ('9020', '9200'), ('1100', '1010')])

fam('HO8', lambda v, i: choice(i, 'hoeren', L('Hören Sie. Wie viel kostet das zusammen?', 'Listen. How much is it in total?', 'Makinig. Magkano lahat-lahat?'), None, euro(v[0] + v[1])[0], [euro(v[0])[0]],
    E3(f'{euro(v[0])[0]} + {euro(v[1])[0]} = {euro(v[0] + v[1])[0]}. „Zusammen“ heißt: alles zusammen.', f'{euro(v[0])[0]} + {euro(v[1])[0]} = {euro(v[0] + v[1])[0]}. “Zusammen” means: all together.', f'{euro(v[0])[0]} + {euro(v[1])[0]} = {euro(v[0] + v[1])[0]}. “Zusammen” = lahat-lahat.'),
    [G5], R('zusammen', 'kosten'), audio=f'Das kostet {acc(euro(v[0])[1])} und das kostet {acc(euro(v[1])[1])}. Zusammen {euro(v[0] + v[1])[1]}.'),
    [], [(300, 200), (150, 250), (400, 120), (90, 210)])

# ================================================================ LESEN
fam('LE1', lambda v, i: choice(i, 'lesen', READ, f'Das kostet {euro(v[0])[1]}.', euro(v[0])[0], [euro(c)[0] for c in v[1]],
    E3(f'„{euro(v[0])[1]}“ = {euro(v[0])[0]}.', f'“{euro(v[0])[1]}” = {euro(v[0])[0]}.', f'“{euro(v[0])[1]}” = {euro(v[0])[0]}.'), [G5, G2], R('kosten', 'Euro', 'Cent')),
    [(420, [402, 2040]), (1590, [1509, 1950]), (75, [57, 750])], [(630, [603, 360]), (1280, [1208, 2180]), (990, [909, 1990]), (2150, [2105, 1520])])

AGE = lambda v, i: choice(i, 'lesen', READ, f'Herr {v[0]} ist {v[1]} Jahre alt. Frau {v[0]} ist {v[2]}. Wie alt ist {v[3]} {v[0]}?',
                          str(v[1] if v[3] == 'Herr' else v[2]), [str(v[2] if v[3] == 'Herr' else v[1]), str((v[1] if v[3] == 'Herr' else v[2]) + 10)],
                          E3(f'Lesen Sie genau: {v[3]} {v[0]} ist {v[1] if v[3] == "Herr" else v[2]}.', f'Read carefully: {v[3]} {v[0]} is {v[1] if v[3] == "Herr" else v[2]}.', f'Basahing mabuti: si {v[3]} {v[0]} ay {v[1] if v[3] == "Herr" else v[2]}.'), [G3], R('Jahre alt', 'Herr', 'Frau'))
fam('LE2', AGE, [('Gruber', 71, 68, 'Herr'), ('Santos', 34, 43, 'Frau'), ('Huber', 59, 55, 'Herr')],
    [('Berger', 62, 26, 'Frau'), ('Mayer', 45, 54, 'Herr'), ('Bauer', 38, 83, 'Frau'), ('Reyes', 27, 72, 'Herr')])

FIELD = {'Postleitzahl': ('postcode', 'postal code'), 'Hausnummer': ('house number', 'numero ng bahay'), 'Telefonnummer': ('phone number', 'numero ng telepono')}
CARD = lambda v, i: choice(i, 'lesen', READ,
                           f'{v[0]}\nHausnummer: {v[1]} · Postleitzahl: {v[2]} · Telefonnummer: {v[3]}\nWas ist die {v[4]}?',
                           {'Hausnummer': v[1], 'Postleitzahl': v[2], 'Telefonnummer': v[3]}[v[4]],
                           [x for k, x in (('Hausnummer', v[1]), ('Postleitzahl', v[2]), ('Telefonnummer', v[3])) if k != v[4]],
                           E3(f'Suchen Sie das Wort „{v[4]}“. Daneben steht die Zahl.', f'Look for the word “{v[4]}” ({FIELD[v[4]][0]}). The number is next to it.', f'Hanapin ang salitang “{v[4]}” ({FIELD[v[4]][1]}). Katabi nito ang numero.'),
                           [G4], R(v[4]))
fam('LE3', CARD, [('Sofia Berger', '9', '5020', '0650 12 34', 'Postleitzahl'), ('Jose Cruz', '23', '1100', '0664 88 21', 'Hausnummer'), ('Anna Lehner', '6', '4020', '0699 50 17', 'Telefonnummer')],
    [('Ali Novak', '41', '8010', '0676 33 90', 'Hausnummer'), ('Maria Reyes', '15', '9020', '0650 71 08', 'Postleitzahl'), ('Lukas Fischer', '2', '1010', '0664 19 46', 'Telefonnummer'), ('Frau Wagner', '30', '5020', '0699 62 25', 'Postleitzahl')])

KL = lambda q, en, tl, correct, others, exp: (q, en, tl, correct, others, exp)
fam('LE4', lambda v, i: choice(i, 'lesen', LOOK(v[1], v[2]), v[0], v[3], v[4], v[5], [G4], R('Nummer', 'Hausnummer'), img=IMG_KLINGEL()),
    [KL('Berger: Top …', '', '', '3', ['2', '4'], L('Auf der Klingel steht: Top 3 – Berger.', 'The doorbell says: Top 3 – Berger.', 'Sa doorbell: Top 3 – Berger.')),
     KL('Huber: Top …', 'Look at the picture. Which flat number (Top) does Huber have?', 'Tingnan ang larawan. Anong Top ang kay Huber?', '1', ['3', '4'], L('Auf der Klingel steht: Top 1 – Huber.', 'The doorbell says: Top 1 – Huber.', 'Sa doorbell: Top 1 – Huber.')),
     KL('Die Hausnummer ist …', 'Look at the picture. What is the house number in words?', 'Tingnan ang larawan. Ano ang numero ng bahay sa salita?', 'siebzehn', ['siebzig', 'sieben'], L('Am Haus steht 17 = siebzehn.', 'The house shows 17 = siebzehn.', 'Nakasulat sa bahay ang 17 = siebzehn.'))],
    [KL('Hausnummer und Top von Huber: Welche Zahlen?', '', '', '17 und 1', ['71 und 1', '17 und 4'], L('Am Haus steht 17, auf der Klingel: Top 1 – Huber.', 'The house shows 17, the doorbell: Top 1 – Huber.', 'Sa bahay: 17, sa doorbell: Top 1 – Huber.')),
     KL('Mayer: Top …', '', '', '4', ['1', '3'], L('Auf der Klingel steht: Top 4 – Mayer.', 'The doorbell says: Top 4 – Mayer.', 'Sa doorbell: Top 4 – Mayer.'))])

MK = lambda q, en, tl, cents, others: (q, en, tl, euro(cents)[0], [euro(o)[0] for o in others])
fam('LE5', lambda v, i: choice(i, 'lesen', LOOK(v[1], v[2]), v[0], v[3], v[4], L(f'Lesen Sie die Preise im Bild. Richtig ist {v[3]}.', f'Read the prices in the picture. Correct: {v[3]}.', f'Basahin ang mga presyo sa larawan. Tama: {v[3]}.'), [G5], R('kosten', 'Preis', 'zusammen'), img=IMG_MARKT()),
    [MK('Äpfel und Milch: Wie viel kostet das zusammen?', 'Look at the picture. Apples and milk – how much together?', 'Tingnan ang larawan. Mansanas at gatas – magkano lahat?', 359, [240, 119]),
     MK('Brot und Milch: Wie viel kostet das zusammen?', 'Look at the picture. Bread and milk – how much together?', 'Tingnan ang larawan. Tinapay at gatas – magkano lahat?', 429, [310, 119]),
     MK('Äpfel, Brot und Milch zusammen: Wie viel kostet das?', 'Look at the picture. Everything together – how much?', 'Tingnan ang larawan. Lahat-lahat – magkano?', 669, [550, 240])],
    [MK('Brot: Wie viel kostet das?', '', '', 310, [130, 240]),
     MK('Brot und Äpfel: Wie viel kostet das zusammen?', 'Look at the picture. How much do bread and apples cost together?', 'Tingnan ang larawan. Magkano ang tinapay at mansanas nang magkasama?', 550, [359, 429])])

ENOUGH = lambda v, i: choice(i, 'lesen', READ, f'Sie haben {euro(v[0])[0]}. Das kostet {euro(v[1])[0]}. Haben Sie genug?',
                             'Ja, das ist genug.' if v[0] >= v[1] else 'Nein, das ist nicht genug.', ['Nein, das ist nicht genug.' if v[0] >= v[1] else 'Ja, das ist genug.'],
                             E3(f'{euro(v[0])[0]} ist {"mehr als" if v[0] > v[1] else "genau" if v[0] == v[1] else "weniger als"} {euro(v[1])[0]}.', f'{euro(v[0])[0]} is {"more than" if v[0] > v[1] else "exactly" if v[0] == v[1] else "less than"} {euro(v[1])[0]}.',
                                f'Ang {euro(v[0])[0]} ay {"mas marami sa" if v[0] > v[1] else "eksaktong" if v[0] == v[1] else "mas kaunti sa"} {euro(v[1])[0]}.'), [G5], R('genug', 'haben', 'mehr'))
fam('LE6', ENOUGH, [], [(500, 480), (300, 350), (1000, 1000), (250, 520)])

# ================================================================ SCHREIBEN
fam('SC1', lambda v, i: short(i, 'schreiben', WORD, str(v), [de(v)] + ([de(v).replace('ß', 'ss')] if 'ß' in de(v) else []) + (['einhundert'] if v == 100 else []),
    E3(f'{v} = „{de(v)}“.' + (' Zuerst die Einer, dann „und“, dann die Zehner.' if v > 20 and v % 10 else ''), f'{v} = “{de(v)}”.' + (' First the ones, then “und”, then the tens.' if v > 20 and v % 10 else ''),
       f'{v} = “{de(v)}”.' + (' Una ang ones, tapos “und”, tapos ang tens.' if v > 20 and v % 10 else '')), [G2], R('Zahl')),
    [36, 74, 92], [19, 70, 22, 85, 11, 100, 63, 47])

fam('SC2', lambda v, i: short(i, 'schreiben', SPELLED, 'Das Wort:', [v], E3(f'{spell(v)[:-1]} = „{v}“. Nomen schreibt man groß.', f'{spell(v)[:-1]} = “{v}”. Nouns start with a capital letter.', f'{spell(v)[:-1]} = “{v}”. Malaking titik ang simula ng noun.'),
    [G1], R(v, 'buchstabieren'), audio=spell_audio(v)),
    ['Preis', 'Zahl', 'Alter'], ['Cent', 'Nummer', 'Vorname', 'Euro', 'Frau', 'Herr'])

FORM = lambda v, i: cloze(i, 'schreiben', L('Lesen Sie den Text. Schreiben Sie die Zahlen in das Formular.', 'Read the text. Write the numbers into the form.', 'Basahin ang teksto. Isulat ang mga numero sa form.'),
                          f'Ich heiße {v[0]}. Ich bin {de(v[1])} Jahre alt. {v[2]}: {de(v[3]) if v[2] == "Hausnummer" else digits(str(v[3]))}.\nAlter: {{{{1}}}} · {v[2]}: {{{{2}}}}',
                          [[str(v[1])], [str(v[3])]], E3(f'{de(v[1])} = {v[1]}; {v[2]}: {v[3]}. Im Formular schreibt man Zahlen in Ziffern.', f'{de(v[1])} = {v[1]}; {v[2]}: {v[3]}. In a form you write numbers in digits.', f'{de(v[1])} = {v[1]}; {v[2]}: {v[3]}. Sa form, digits ang gamit.'),
                          [G4, G3], R('Alter', v[2]))
fam('SC3', FORM, [('Ali Mayer', 33, 'Hausnummer', 14), ('Maria Santos', 28, 'Postleitzahl', 9020), ('Lukas Bauer', 61, 'Hausnummer', 20)],
    [('Anna Huber', 45, 'Postleitzahl', 1100), ('Jose Cruz', 52, 'Hausnummer', 16), ('Sofia Reyes', 19, 'Postleitzahl', 4020), ('Ali Novak', 70, 'Hausnummer', 3)])

PRICE_W = lambda v, i: short(i, 'schreiben', L('Hören Sie. Schreiben Sie den Preis in Ziffern (z. B. 2,50).', 'Listen. Write the price in digits (e.g. 2,50).', 'Makinig. Isulat ang presyo gamit ang digits (hal. 2,50).'), 'Preis in Euro:',
                             [f'{v // 100},{v % 100:02d}{s}' for s in ('', ' €', '€', ' Euro')] + [f'€ {v // 100},{v % 100:02d}', f'€{v // 100},{v % 100:02d}'] + [f'{v // 100}.{v % 100:02d}{s}' for s in ('', ' €', '€')],
                             E3(f'„{euro(v)[1]}“ = {euro(v)[0]}.', f'“{euro(v)[1]}” = {euro(v)[0]}.', f'“{euro(v)[1]}” = {euro(v)[0]}.'), [G5], R('Preis', 'Euro'), audio=f'Das kostet {euro(v)[1]}.')
fam('SC4', PRICE_W, [], [(350), (1290), (480), (2015)])

# ================================================================ SPRECHEN (A1-SPR-T1: introduce, spell, number)
fam('SP1', lambda v, i: choice(i, 'sprechen', L(f'Sie sind {v} Jahre alt. Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', f'You are {v} years old. What do you say? Choose, then say it aloud.', f'{v} taong gulang ka. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'),
    'Wie alt sind Sie?', f'Ich bin {de(v)} Jahre alt.', [f'Ich habe {de(v)} Jahre.', f'Ich habe {de(v)}.'],
    E3('Das Alter sagt man immer mit „sein“: „Ich bin … Jahre alt.“', 'You always say your age with “sein”: “Ich bin … Jahre alt.”', 'Ang edad ay laging sinasabi gamit ang “sein”: “Ich bin … Jahre alt.”'), [G3, G6], R('Jahre alt', 'sein')),
    [35, 52, 27], [44, 19, 61, 30])

ASK = {'Name': ('Sie verstehen den Namen nicht.', 'You don’t understand the name.', 'Hindi mo naintindihan ang pangalan.', 'Wie bitte? Noch einmal, bitte.'),
       'spell': ('Sie wissen nicht: Wie schreibt man den Namen?', 'You don’t know how the name is written.', 'Hindi mo alam kung paano isinusulat ang pangalan.', 'Wie schreibt man das?'),
       'price': ('Sie möchten den Preis wissen.', 'You want to know the price.', 'Gusto mong malaman ang presyo.', 'Was kostet das?'),
       'age': ('Sie möchten das Alter wissen.', 'You want to know the age.', 'Gusto mong malaman ang edad.', 'Wie alt sind Sie?'),
       'phone': ('Sie möchten die Telefonnummer wissen.', 'You want to know the phone number.', 'Gusto mong malaman ang numero ng telepono.', 'Wie ist Ihre Telefonnummer?'),
       'plz': ('Sie möchten die Postleitzahl wissen.', 'You want to know the postcode.', 'Gusto mong malaman ang postal code.', 'Wie ist die Postleitzahl?'),
       'pay': ('Sie möchten alles auf einmal zahlen.', 'You want to pay for everything at once.', 'Gusto mong bayaran lahat nang sabay.', 'Zusammen, bitte.')}
fam('SP2', lambda v, i: choice(i, 'sprechen', L(ASK[v[0]][0] + ' Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', ASK[v[0]][1] + ' What do you say? Choose, then say it aloud.', ASK[v[0]][2] + ' Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'),
    None, ASK[v[0]][3], [ASK[k][3] for k in v[1]], E3(f'Passend ist: „{ASK[v[0]][3]}“', f'The right sentence is: “{ASK[v[0]][3]}”', f'Ang angkop: “{ASK[v[0]][3]}”'), [G7], R('wie', 'bitte')),
    [('Name', ['price', 'age']), ('spell', ['Name', 'phone']), ('price', ['spell', 'plz'])],
    [('age', ['phone', 'pay']), ('phone', ['age', 'plz']), ('plz', ['price', 'Name']), ('pay', ['spell', 'age'])])

fam('SP3', lambda v, i: choice(i, 'sprechen', L('Wie sagt man den Preis? Wählen Sie, dann sagen Sie es laut.', 'How do you say the price? Choose, then say it aloud.', 'Paano sabihin ang presyo? Pumili, tapos sabihin nang malakas.'),
    euro(v[0])[0], euro(v[0])[1], v[1], E3(f'Man sagt: „{euro(v[0])[1]}“. Das Komma sagt man nicht.', f'You say: “{euro(v[0])[1]}”. You don’t say the comma.', f'Sinasabi: “{euro(v[0])[1]}”. Hindi sinasabi ang comma.'), [G5, G2], R('Euro', 'Cent')),
    [(380, ['drei Komma acht null Euro', 'achtzig Euro drei']), (1220, ['zwölf Komma zwanzig', 'zwanzig Euro zwölf']), (99, ['neunzig neun Cent', 'null Euro neun neun'])],
    [(450, ['vier Komma fünf Euro', 'fünfzig Euro vier']), (1150, ['elf Komma fünfzig', 'fünfzig Euro elf']), (175, ['eins Euro fünfundsiebzig', 'ein Euro siebenundfünfzig']), (2030, ['zwanzig Komma dreißig', 'dreißig Euro zwanzig'])])

# Spelling aloud with letter names: the options show the names (Pe – Er – E …), so they cannot be matched to the word by eye.
SPELL_SAY = lambda v, i: choice(i, 'sprechen', L('Wie buchstabiert man das Wort? Wählen Sie, dann sagen Sie es laut.', 'How do you spell the word? Choose, then say it aloud.', 'Paano i-spell ang salita? Pumili, tapos sabihin nang malakas.'), v[0],
                                letter_names(v[0]), [letter_names(w) for w in v[1]],
                                E3(f'„{v[0]}“: {letter_names(v[0])}.', f'“{v[0]}”: {letter_names(v[0])}.', f'“{v[0]}”: {letter_names(v[0])}.'), [G1], R(v[0], 'buchstabieren'))
fam('SP4', SPELL_SAY, [], [('Euro', ['Euru', 'Ejro']), ('Zahl', ['Sahl', 'Zal']), ('Preis', ['Breis', 'Prais']), ('Vorname', ['Worname', 'Forname'])])

# ================================================================ GRAMMATIK / WORTSCHATZ
SEIN = L('„sein“: ich bin · du bist · er/sie ist · wir sind · ihr seid · sie/Sie sind.', '“sein”: ich bin · du bist · er/sie ist · wir sind · ihr seid · sie/Sie sind.', '“sein”: ich bin · du bist · er/sie ist · wir sind · ihr seid · sie/Sie sind.')
HABEN = L('„haben“: ich habe · du hast · er/sie hat · wir haben · ihr habt · sie/Sie haben.', '“haben”: ich habe · du hast · er/sie hat · wir haben · ihr habt · sie/Sie haben.', '“haben”: ich habe · du hast · er/sie hat · wir haben · ihr habt · sie/Sie haben.')
fam('GW1', lambda v, i: cloze(i, 'grammatikWortschatz', GAPS, v[0], [v[1]], SEIN, [G6, G3], R('sein', 'Jahre alt')),
    [('Wie alt {{1}} Sie?', ['sind']), ('Frau Huber {{1}} siebzig Jahre alt.', ['ist']), ('Ihr {{1}} schon achtzehn.', ['seid'])],
    [('Ich {{1}} einundvierzig.', ['bin']), ('Wie alt {{1}} du?', ['bist']), ('Herr und Frau Santos {{1}} sechzig.', ['sind']), ('Er {{1}} dreißig Jahre alt.', ['ist'])])

fam('GW2', lambda v, i: cloze(i, 'grammatikWortschatz', GAPS, v[0], [v[1]], HABEN, [G6], R('haben')),
    [('Ich {{1}} nur zwei Euro.', ['habe']), ('{{1}} du eine Telefonnummer?', ['Hast']), ('Ihr {{1}} genug.', ['habt'])],
    [('Frau Berger {{1}} etwas.', ['hat']), ('Wir {{1}} zusammen zwanzig Euro.', ['haben']), ('Er {{1}} die Postleitzahl.', ['hat']), ('Du {{1}} mehr als ich.', ['hast'])])

WQ = lambda v, i: choice(i, 'grammatikWortschatz', L('Welche Frage ist richtig?', 'Which question is correct?', 'Aling tanong ang tama?'), None, v[0], v[1],
                         E3('W-Frage: Fragewort auf Platz 1, Verb auf Platz 2.', 'W-question: question word in position 1, verb in position 2.', 'W-question: ang tanong na salita sa posisyon 1, ang verb sa posisyon 2.'), [G7], R('wie'))
fam('GW3', WQ, [('Wie alt sind Sie?', ['Wie alt Sie sind?', 'Sind wie alt Sie?']), ('Wie ist die Postleitzahl?', ['Wie die Postleitzahl ist?', 'Die Postleitzahl wie ist?']), ('Wie viele Buchstaben hat das?', ['Wie viele Buchstaben das hat?', 'Hat das wie viele Buchstaben?'])],
    [('Wie schreibt man das?', ['Wie man das schreibt?', 'Man schreibt wie das?']), ('Wie ist die Hausnummer?', ['Wie die Hausnummer ist?', 'Ist wie die Hausnummer?']), ('Wie heißen Sie?', ['Wie Sie heißen?', 'Heißen wie Sie?']), ('Was kostet das?', ['Was das kostet?', 'Kostet was das?'])])

WV = lambda v, i: choice(i, 'grammatikWortschatz', CHOOSE, v[0], v[1], ['Wie viele' if v[1] == 'Wie viel' else 'Wie viel'],
                         E3('„Wie viel kostet …?“ fragt nach dem Preis. „Wie viele“ steht vor Dingen im Plural, die man zählt: Buchstaben, Zahlen, Namen.', '“Wie viel kostet …?” asks for the price. “Wie viele” comes before plural things you count: letters, numbers, names.', 'Ang “Wie viel kostet …?” ay tanong sa presyo. Ang “wie viele” ay ginagamit bago ang mga bagay sa plural na binibilang: titik, numero, pangalan.'), [G7], R('wie viel', 'wie viele'))
fam('GW4', WV, [('… Buchstaben hat „Alter“?', 'Wie viele'), ('… kostet das zusammen?', 'Wie viel'), ('… Buchstaben hat „Postleitzahl“?', 'Wie viele')],
    [('… Buchstaben hat „Cent“?', 'Wie viele'), ('… kostet die Milch?', 'Wie viel'), ('… Namen hat Herr Bauer?', 'Wie viele'), ('… kostet das Brot?', 'Wie viel')])

fam('GW5', lambda v, i: choice(i, 'grammatikWortschatz', CHOOSE, f'{de(v)} = ?', str(v), [str(swap(v)), str(v // 10 * 100 + v % 10)],
    E3(f'„{de(v)}“: zuerst {v % 10}, dann {v - v % 10} = {v}.', f'“{de(v)}”: first {v % 10}, then {v - v % 10} = {v}.', f'“{de(v)}”: una {v % 10}, tapos {v - v % 10} = {v}.'), [G2], R('Zahl')),
    [67, 84, 52], [79, 31, 46, 28])

QUANT = lambda v, i: choice(i, 'grammatikWortschatz', CHOOSE, v[0], v[1], v[2], v[3], [G5], R(v[1], *v[2]))
fam('GW6', QUANT, [], [('Das kostet hundert Euro. Das ist …', 'viel', ['wenig', 'nichts'], L('100 Euro sind viel.', '100 euros are a lot (viel).', 'Marami (viel) ang 100 euro.')),
                       ('Das kostet zehn Cent. Das ist …', 'wenig', ['viel', 'genug'], L('10 Cent sind wenig.', '10 cents are little (wenig).', 'Kaunti (wenig) ang 10 cent.')),
                       ('Ich habe null Euro. Ich habe …', 'nichts', ['alle', 'etwas'], L('0 Euro = nichts.', '0 euros = nothing (nichts).', '0 euro = wala (nichts).')),
                       ('Ich habe fünf Euro. Das kostet fünf Euro. Ich habe …', 'genug', ['nichts', 'wenig'], L('5 € für 5 €: Das ist genug.', '€5 for €5: that is enough (genug).', '€5 para sa €5: sapat (genug).'))])

# ================================================================ WERTE (A1-WOW-09, Q101; format A1-WOW-T2 a/b/c)
case = lambda n, extra=('', '', ''): L(f'{n}: {SERV[n]}.{extra[0]} ' + WEXP['de'], f'{n}: {SERV_EN[n]}.{extra[1]} ' + WEXP['en'], f'{n}: {SERV_TL[n]}.{extra[2]} ' + WEXP['tl'])
WEXP = L('Notrufe in Österreich: 122 Feuerwehr · 133 Polizei · 144 Rettung · 112 Euro-Notruf · 141 Ärztenotdienst · 1450 Gesundheitsberatung.',
         'Emergency numbers in Austria: 122 fire brigade · 133 police · 144 ambulance · 112 European emergency number · 141 doctor on call · 1450 health advice line.',
         'Mga emergency number sa Austria: 122 bumbero · 133 pulis · 144 ambulansya · 112 European emergency number · 141 doktor na naka-duty · 1450 health hotline.')
SERV_EN = {'122': 'the fire brigade', '133': 'the police', '144': 'the ambulance', '141': 'the doctor on call', '1450': 'the health advice line', '112': 'the European emergency number'}
SERV_TL = {'122': 'bumbero', '133': 'pulis', '144': 'ambulansya', '141': 'doktor na naka-duty', '1450': 'health hotline', '112': 'European emergency number'}
SERV = {'122': 'die Feuerwehr', '133': 'die Polizei', '144': 'die Rettung', '141': 'der Ärztenotdienst', '1450': 'die Gesundheitsberatung am Telefon', '112': 'der Euro-Notruf'}
SIT = lambda de_, en, tl, correct, others: (de_, en, tl, correct, others)
fam('WE1', lambda v, i: choice(i, 'werte', L(v[0] + ' Welche Nummer rufen Sie an?', v[1] + ' Which number do you call?', v[2] + ' Anong numero ang tatawagan mo?'), None, v[3], v[4], case(v[3]), [G8], R('Nummer')),
    [SIT('Es brennt!', 'There is a fire!', 'May sunog!', '122', ['133', '144']),
     SIT('Ein Dieb nimmt eine Tasche.', 'A thief takes a bag.', 'May magnanakaw na kumuha ng bag.', '133', ['144', '122']),
     SIT('Ein Mann ist sehr krank und kann nicht atmen.', 'A man is very ill and cannot breathe.', 'May lalaking malubha at hindi makahinga.', '144', ['122', '141'])],
    [SIT('Ein Unfall auf der Straße. Eine Frau ist verletzt.', 'An accident on the road. A woman is injured.', 'May aksidente sa kalsada. May babaeng sugatan.', '144', ['122', '1450']),
     SIT('Im Haus ist viel Rauch.', 'There is a lot of smoke in the house.', 'Maraming usok sa bahay.', '122', ['144', '133']),
     SIT('Jemand ist in Ihrer Wohnung. Sie kennen die Person nicht.', 'Someone is in your flat. You don’t know the person.', 'May tao sa apartment mo. Hindi mo siya kilala.', '133', ['122', '141']),
     SIT('Sie sind in Italien und brauchen schnell Hilfe.', 'You are in Italy and need help quickly.', 'Nasa Italy ka at kailangan mo agad ng tulong.', '112', ['1450', '141'])])

fam('WE2', lambda v, i: choice(i, 'werte', CHOOSE, f'Die Nummer {v[0]} – was ist das?', SERV[v[0]], [SERV[k] for k in v[1]], case(v[0]), [G8], R('Nummer')),
    [('122', ['133', '144']), ('133', ['122', '144']), ('144', ['133', '122'])], [('141', ['144', '1450']), ('1450', ['141', '133']), ('112', ['141', '1450']), ('133', ['112', '144'])])

fam('WE3', lambda v, i: choice(i, 'werte', CHOOSE, f'Welche Nummer hat {SERV[v[0]]}?', v[0], v[1], case(v[0]), [G8], R('Nummer')),
    [('1450', ['141', '112']), ('141', ['1450', '144']), ('112', ['122', '1450'])], [('144', ['141', '133']), ('122', ['112', '133'])])

fam('WE4', lambda v, i: choice(i, 'werte', LOOK(), v[0], v[3], v[4], case(v[3]), [G8], R('Nummer'), img=IMG_NOTRUF()),
    [], [('Feuerwehr: Welche Nummer?', 'Look at the picture. Which number is for the fire brigade?', 'Tingnan ang larawan. Anong numero para sa bumbero?', '122', ['133', '144']),
         ('Euro-Notruf: Welche Nummer?', 'Look at the picture. Which number is the European emergency number?', 'Tingnan ang larawan. Ano ang European emergency number?', '112', ['122', '144'])])

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


fams = interleave(group(group(PRACTICE, lambda p: p.get('family', p['id'])), lambda f: f[0]['skill']))
order = interleave(fams)
part, rest = order[:40], order[40:]
quota = {'lesen': 3, 'hoeren': 5, 'schreiben': 3, 'sprechen': 3, 'grammatikWortschatz': 3, 'werte': 3}
rs = Counter(p['skill'] for p in rest)
print('test', len(TEST), dict(Counter(t['skill'] for t in TEST)))
print('practice', len(PRACTICE), dict(Counter(p['skill'] for p in PRACTICE)))
print('rest', dict(rs))
for s, q in quota.items():
    if rs[s] < 2 * q:
        print(f'  ! rest {s}: {rs[s]} < {2 * q}')
json.dump({'chapterId': CH, 'goals': GOALS, 'pools': {'practice': PRACTICE, 'test': TEST}}, open(f'{ROOT}/src/lib/content/a1-02-pools.json', 'w'), ensure_ascii=False, indent='\t')
