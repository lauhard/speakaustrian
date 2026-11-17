# A1-02 lessons -> src/lib/content/a1-02.json
import json
from gen_a102_common import *

V = {
    'alle': (None, 'all, everybody', 'lahat'), 'etwas': (None, 'something', 'kaunti / isang bagay'), 'nichts': (None, 'nothing', 'wala'),
    'dieser': (None, 'this (one)', 'ito / itong'), 'wie viel': (None, 'how much', 'magkano / gaano karami'), 'wie viele': (None, 'how many', 'ilan'),
    'nur': (None, 'only', 'lang / lamang'), 'noch': (None, 'still, another', 'pa'), 'schon': (None, 'already', 'na'), 'bald': (None, 'soon', 'malapit na'),
    'viel': (None, 'much, a lot', 'marami'), 'wenig': (None, 'little, few', 'kaunti'), 'mehr': (None, 'more', 'mas marami'), 'genug': (None, 'enough', 'sapat'),
    'zusammen': (None, 'together, in total', 'magkasama / lahat-lahat'), 'allein': (None, 'alone', 'mag-isa'), 'vielleicht': (None, 'maybe', 'siguro'),
    'wieder': (None, 'again', 'ulit'), 'zurück': (None, 'back', 'pabalik / sukli'), 'haben': (None, 'to have', 'magkaroon / mayroon'),
    'werden': (None, 'to become', 'maging'), 'machen': (None, 'to do, to make', 'gumawa'), 'sagen': (None, 'to say', 'sabihin'), 'fragen': (None, 'to ask', 'magtanong'),
    'antworten': (None, 'to answer', 'sumagot'), 'wissen': (None, 'to know (a fact)', 'malaman (alam)'), 'kennen': (None, 'to know (a person, a thing)', 'kilala'),
    'möglich': (None, 'possible', 'posible'), 'buchstabieren': (None, 'to spell', 'i-spell'), 'Buchstabe': ('der', 'letter (of the alphabet)', 'titik'),
    'Alter': ('das', 'age', 'edad'), 'Jahre alt': (None, '… years old', '… taong gulang'), 'Hausnummer': ('die', 'house number', 'numero ng bahay'),
    'Postleitzahl': ('die', 'postcode', 'postal code'), 'Telefonnummer': ('die', 'phone number', 'numero ng telepono'), 'Euro': ('der', 'euro', 'euro'),
    'Cent': ('der', 'cent', 'cent (sentimo)'), 'Preis': ('der', 'price', 'presyo'), 'kosten': (None, 'to cost', 'magkahalaga'),
    'Million': ('die', 'million', 'milyon'), 'Zahl': ('die', 'number (figure)', 'numero (bilang)'), 'Nummer': ('die', 'number (phone, house)', 'numero'),
}
NUM_EN = 'zero one two three four five six seven eight nine ten eleven twelve thirteen'.split()
NUM_TL = 'sero isa dalawa tatlo apat lima anim pito walo siyam sampu labing-isa labindalawa labintatlo'.split()
TENS_EN = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'}
TENS_TL = {20: 'dalawampu', 30: 'tatlumpu', 40: 'apatnapu', 50: 'limampu', 60: 'animnapu', 70: 'pitumpu', 80: 'walumpu', 90: 'siyamnapu', 100: 'sandaan', 1000: 'sanlibo'}
for n in range(14):
    V[de(n)] = (None, f'{NUM_EN[n]} ({n})', f'{NUM_TL[n]} ({n})')
for n in TENS_EN:
    V['tausend' if n == 1000 else de(n)] = (None, f'{TENS_EN[n]} ({n})', f'{TENS_TL[n]} ({n})')

vocab = []
for lemma, wid in A102.items():
    art, en, tl = V[lemma]
    v = {'id': wid, 'lemma': lemma, 'en': en, 'tl': tl}
    if art:
        v['article'] = art
    vocab.append(v)

C = lambda phrase, de_, en, tl: {'phrase': phrase, 'note': L(de_, en, tl)}
lessons = []


def lesson(n, title, introduces, cards, items):
    lid = f'{CH}-L{n:02d}'
    out = []
    for k, it in enumerate(items, 1):
        it['id'] = f'{lid}-I{k}'
        out.append(it)
    lessons.append({'id': lid, 'title': title, 'introduces': [r for r in R(*introduces) if r not in NO_CARD], 'cards': cards, 'items': out})


X = ''  # ids are set by lesson()
LETTER = L('Hören Sie. Welchen Buchstaben hören Sie?', 'Listen. Which letter do you hear?', 'Makinig. Anong titik ang naririnig mo?')
WHICH_WORD = L('Hören Sie. Jemand buchstabiert. Welches Wort ist das?', 'Listen. Someone spells. Which word is it?', 'Makinig. May nag-i-spell. Anong salita ito?')

# L01 ------------------------------------------------------------------ alphabet A–M
lesson(1, L('Das Alphabet: A bis M', 'The alphabet: A to M', 'Ang alpabeto: A hanggang M'), ['Buchstabe'], [
    C('A, B, C, D', 'A sagt man „a“ wie in „Name“. B, C, D sagt man „be“, „ze“, „de“.', 'A sounds like “ah”. B, C, D sound like “bay”, “tsay”, “day”.', 'Ang A ay parang “ah”. Ang B, C, D ay parang “bey”, “tsey”, “dey”.'),
    C('E, F, G', 'E sagt man „e“ wie in „sehr“. Achtung: nicht „i“!', 'German E sounds like “ay” in “say” – not like English “ee”.', 'Ang E sa German ay parang “ey” sa “say” – hindi “i”.'),
    C('H, I, J', 'I sagt man „i“ wie in „Sie“. J heißt „jot“.', 'German I sounds like “ee”. J is called “yot”.', 'Ang I ay parang “i” (ee). Ang J ay “yot”.'),
    C('K, L, M', 'K sagt man „ka“, L „el“, M „em“.', 'K is “kah”, L is “el”, M is “em”.', 'Ang K ay “ka”, L ay “el”, M ay “em”.'),
    C('der Buchstabe – die Buchstaben', 'A, B, C sind Buchstaben.', 'A, B, C are letters (Buchstaben).', 'Ang A, B, C ay mga titik (Buchstaben).'),
], [
    choice(X, 'hoeren', LETTER, None, 'E', ['I', 'A'], L('Sie hören „e“ wie in „sehr“. Das ist E.', 'You hear “ay” as in “sehr”. That is E.', 'Naririnig mo ang “ey” gaya sa “sehr”. Iyan ay E.'), refs=R('Buchstabe'), audio='e'),
    choice(X, 'hoeren', LETTER, None, 'I', ['E', 'J'], L('Sie hören „i“ wie in „Sie“. Das ist I.', 'You hear “ee” as in “Sie”. That is I.', 'Naririnig mo ang “i” gaya sa “Sie”. Iyan ay I.'), refs=R('Buchstabe'), audio='i'),
    choice(X, 'hoeren', LETTER, None, 'J', ['G', 'I'], L('„Jot“ ist J.', '“Yot” is J.', 'Ang “yot” ay J.'), refs=R('Buchstabe'), audio='j'),
    choice(X, 'grammatikWortschatz', L('Welcher Buchstabe fehlt?', 'Which letter is missing?', 'Anong titik ang kulang?'), 'A, B, C, …, E', 'D', ['G', 'T'], L('A, B, C, D, E – D kommt nach C.', 'A, B, C, D, E – D comes after C.', 'A, B, C, D, E – ang D ay pagkatapos ng C.'), refs=R('Buchstabe')),
    cloze(X, 'grammatikWortschatz', GAPS, 'A, B, C, D, {{1}}, F, G, H, {{2}}, J, K, L, M', [['E'], ['I']], L('Das Alphabet: A, B, C, D, E, F, G, H, I, J, K, L, M.', 'The alphabet: A, B, C, D, E, F, G, H, I, J, K, L, M.', 'Ang alpabeto: A, B, C, D, E, F, G, H, I, J, K, L, M.'), refs=R('Buchstabe')),
])

# L02 ------------------------------------------------------------------ alphabet N–Z, umlauts
lesson(2, L('Das Alphabet: N bis Z, Ä, Ö, Ü und ß', 'The alphabet: N to Z, Ä, Ö, Ü and ß', 'Ang alpabeto: N hanggang Z, Ä, Ö, Ü at ß'), ['dieser'], [
    C('N, O, P, Q, R', 'Q sagt man „ku“. R sagt man „er“.', 'Q is “koo”. R is “air”.', 'Ang Q ay “ku”. Ang R ay “er”.'),
    C('S, T, U, V', 'U sagt man „u“ wie in „gut“. V heißt „fau“.', 'U sounds like “oo” in “gut”. V is called “fow”.', 'Ang U ay “u” gaya sa “gut”. Ang V ay “fau”.'),
    C('W, X, Y, Z', 'W heißt „we“. Y heißt „üpsilon“. Z heißt „zett“.', 'W is “vay”. Y is “üpsilon”. Z is “tset”.', 'Ang W ay “vey”. Ang Y ay “üpsilon”. Ang Z ay “tset”.'),
    C('Ä, Ö, Ü', 'Umlaute: Ä wie in „Universität“, Ö wie in „Österreich“, Ü wie in „grüß Gott“.', 'Umlauts: Ä, Ö (as in “Österreich”), Ü (as in “grüß Gott”).', 'Mga umlaut: Ä, Ö (gaya sa “Österreich”), Ü (gaya sa “grüß Gott”).'),
    C('ß – „scharfes S“', 'ß heißt „scharfes S“, z. B. in „heißen“ und „grüß Gott“.', 'ß is called “sharp S”, e.g. in “heißen” and “grüß Gott”.', 'Ang ß ay “matalim na S”, hal. sa “heißen” at “grüß Gott”.'),
    C('Wie heißt dieser Buchstabe?', 'So fragen Sie nach einem Buchstaben.', 'This is how you ask what a letter is called.', 'Ganito magtanong tungkol sa isang titik.'),
], [
    choice(X, 'hoeren', LETTER, None, 'V', ['W', 'F'], L('„Fau“ ist V. W heißt „we“.', '“Fow” is V. W is “vay”.', 'Ang “fau” ay V. Ang W ay “we”.'), refs=R('Buchstabe'), audio='v'),
    choice(X, 'hoeren', LETTER, None, 'W', ['V', 'B'], L('„We“ ist W.', '“Vay” is W.', 'Ang “we” ay W.'), refs=R('Buchstabe'), audio='w'),
    choice(X, 'hoeren', LETTER, None, 'Z', ['S', 'C'], L('„Zett“ ist Z.', '“Tset” is Z.', 'Ang “tset” ay Z.'), refs=R('Buchstabe'), audio='z'),
    choice(X, 'lesen', READ, 'Was schreibt man mit ß?', 'heißen', ['Name', 'Österreich'], L('„heißen“ schreibt man mit ß.', '“heißen” is written with ß.', 'Ang “heißen” ay may ß.'), refs=R('Buchstabe', 'heißen')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Wie heißt dieser Buchstabe? – Ö', 'Ö wie in „Österreich“', ['O wie in „Woher?“', 'Ü wie in „grüß Gott“'], L('Ö ist ein Umlaut, wie in „Österreich“.', 'Ö is an umlaut, as in “Österreich”.', 'Ang Ö ay umlaut, gaya sa “Österreich”.'), refs=R('dieser', 'Buchstabe')),
    cloze(X, 'grammatikWortschatz', GAPS, 'N, O, P, Q, {{1}}, S, T, {{2}}, V, W, X, Y, Z', [['R'], ['U']], L('Das Alphabet: N, O, P, Q, R, S, T, U, V, W, X, Y, Z.', 'The alphabet: N, O, P, Q, R, S, T, U, V, W, X, Y, Z.', 'Ang alpabeto: N, O, P, Q, R, S, T, U, V, W, X, Y, Z.'), refs=R('Buchstabe')),
])

# L03 ------------------------------------------------------------------ spelling
lesson(3, L('Wie schreibt man das? – Buchstabieren', 'How do you write that? – Spelling', 'Paano isulat iyan? – Pag-spell'), ['buchstabieren', 'wissen', 'noch'], [
    C('Wie schreibt man das?', 'So fragen Sie: Welche Buchstaben hat das Wort?', 'This is how you ask how a word is written.', 'Ganito magtanong kung paano isinusulat ang salita.'),
    C('Buchstabieren Sie, bitte.', 'Höflich mit „Sie“. Mit „du“: „Buchstabier bitte.“', 'Polite with “Sie”. With “du”: “Buchstabier bitte.”', 'Magalang gamit ang “Sie”. Sa “du”: “Buchstabier bitte.”'),
    dict(C('B – A – U – E – R', 'So buchstabiert man den Namen „Bauer“.', 'This is how you spell the name “Bauer”.', 'Ganito i-spell ang pangalang “Bauer”.'), audioText=spell_audio('Bauer')),
    C('Noch einmal, bitte.', 'Sie verstehen nicht? Sagen Sie: „Noch einmal, bitte.“', 'You didn’t understand? Say: “Noch einmal, bitte.” (once more, please)', 'Hindi mo naintindihan? Sabihin: “Noch einmal, bitte.” (isa pa, please)'),
    C('Ich weiß es nicht.', '„wissen“: ich weiß, du weißt, er/sie weiß, Sie wissen.', '“wissen” (to know): ich weiß, du weißt, er/sie weiß, Sie wissen.', '“wissen” (alam): ich weiß, du weißt, er/sie weiß, Sie wissen.'),
], [
    choice(X, 'hoeren', WHICH_WORD, None, 'Bauer', ['Baur', 'Bauar'], L('Sie hören: B, A, U, E, R. Das ist „Bauer“.', 'You hear: B, A, U, E, R. That is “Bauer”.', 'Naririnig mo: B, A, U, E, R. Iyan ay “Bauer”.'), [G1], R('buchstabieren'), audio=spell_audio('Bauer')),
    choice(X, 'hoeren', WHICH_WORD, None, 'Meier', ['Mayer', 'Maier'], L('M, E, I, E, R – mit „ei“. Der Name klingt gleich, aber man schreibt ihn anders. Darum buchstabiert man.', 'M, E, I, E, R – with “ei”. The names sound the same but are written differently. That is why people spell.', 'M, E, I, E, R – may “ei”. Pareho ang tunog pero iba ang sulat. Kaya nag-i-spell.'), [G1], R('buchstabieren'), audio=spell_audio('Meier')),
    cloze(X, 'grammatikWortschatz', GAPS, '{{1}} schreibt man das? – B, A, U, E, R.', [['Wie']], L('„Wie schreibt man das?“ – Dann buchstabiert man.', '“Wie schreibt man das?” – then you spell.', '“Wie schreibt man das?” – tapos mag-i-spell.'), [G1, G7], R('wie', 'buchstabieren')),
    choice(X, 'sprechen', L('Sie verstehen den Namen nicht. Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'You don’t understand the name. What do you say? Choose, then say it aloud.', 'Hindi mo naintindihan ang pangalan. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'), None, 'Noch einmal, bitte.', ['Danke, gut.', 'Ich heiße Bauer.'], L('„Noch einmal, bitte.“ – dann sagt die Person den Namen noch einmal.', '“Noch einmal, bitte.” – then the person says the name again.', '“Noch einmal, bitte.” – uulitin ng tao ang pangalan.'), [G1], R('noch', 'bitte')),
    cloze(X, 'grammatikWortschatz', GAPS, 'Wie heißt er? – Ich {{1}} es nicht.', [['weiß', 'weiss']], L('„wissen“: ich weiß. „Ich weiß es nicht.“ = I don’t know.', '“wissen”: ich weiß. “Ich weiß es nicht.” = I don’t know.', '“wissen”: ich weiß. “Ich weiß es nicht.” = Hindi ko alam.'), [G6], R('wissen')),
    short(X, 'schreiben', SPELLED, 'Das Wort:', ['Name'], L('N, A, M, E: „Name“. Nomen schreibt man groß.', 'N, A, M, E: “Name”. Nouns start with a capital letter.', 'N, A, M, E: “Name”. Malaking titik ang simula ng noun.'), [G1], R('Name', 'buchstabieren'), audio=spell_audio('Name')),
])

# L04 ------------------------------------------------------------------ 0–12
lesson(4, L('Zahlen von 0 bis 12', 'Numbers from 0 to 12', 'Mga numero mula 0 hanggang 12'), ['Zahl'], [
    C('null, eins, zwei, drei', '0, 1, 2, 3', '0, 1, 2, 3 – zero, one, two, three', '0, 1, 2, 3 – sero, isa, dalawa, tatlo'),
    C('vier, fünf, sechs', '4, 5, 6 – „fünf“ mit ü.', '4, 5, 6 – “fünf” has an ü.', '4, 5, 6 – may ü ang “fünf”.'),
    C('sieben, acht, neun', '7, 8, 9', '7, 8, 9 – seven, eight, nine', '7, 8, 9 – pito, walo, siyam'),
    C('zehn, elf, zwölf', '10, 11, 12', '10, 11, 12 – ten, eleven, twelve', '10, 11, 12 – sampu, labing-isa, labindalawa'),
    C('die Zahl – die Zahlen', '1, 2, 3 sind Zahlen.', '1, 2, 3 are numbers (Zahlen).', 'Ang 1, 2, 3 ay mga numero (Zahlen).'),
], [
    choice(X, 'hoeren', LISTEN, None, '7', ['8', '11'], L('Sie hören „sieben“ = 7.', 'You hear “sieben” = 7.', 'Naririnig mo ang “sieben” = 7.'), [G2], R('sieben'), audio='sieben'),
    choice(X, 'hoeren', LISTEN, None, '12', ['2', '11'], L('Sie hören „zwölf“ = 12.', 'You hear “zwölf” = 12.', 'Naririnig mo ang “zwölf” = 12.'), [G2], R('zwölf'), audio='zwölf'),
    short(X, 'hoeren', DIGITS, 'Die Zahl:', ['3'], L('Sie hören „drei“ = 3.', 'You hear “drei” = 3.', 'Naririnig mo ang “drei” = 3.'), [G2], R('drei'), audio='drei'),
    choice(X, 'lesen', READ, 'acht', '8', ['6', '3'], L('„acht“ = 8.', '“acht” = 8.', '“acht” = 8.'), [G2], R('acht')),
    short(X, 'schreiben', WORD, '5', ['fünf', 'fuenf'], L('5 = „fünf“ (mit ü).', '5 = “fünf” (with ü).', '5 = “fünf” (may ü).'), [G2], R('fünf')),
    cloze(X, 'grammatikWortschatz', GAPS, 'eins, zwei, {{1}}, vier, fünf, {{2}}, sieben', [['drei'], ['sechs']], L('eins, zwei, drei, vier, fünf, sechs, sieben.', 'one, two, three, four, five, six, seven.', 'isa, dalawa, tatlo, apat, lima, anim, pito.'), [G2], R('drei', 'sechs')),
])

# L05 ------------------------------------------------------------------ 13–19
lesson(5, L('Zahlen von 13 bis 19', 'Numbers from 13 to 19', 'Mga numero mula 13 hanggang 19'), ['dreizehn'], [
    C('dreizehn, vierzehn, fünfzehn', 'Zahl + „zehn“: drei + zehn = dreizehn (13).', 'Number + “zehn”: drei + zehn = dreizehn (13).', 'Numero + “zehn”: drei + zehn = dreizehn (13).'),
    C('sechzehn, siebzehn', 'Achtung: sechzehn (nicht „sechszehn“), siebzehn (nicht „siebenzehn“).', 'Careful: sechzehn (not “sechszehn”), siebzehn (not “siebenzehn”).', 'Ingat: sechzehn (hindi “sechszehn”), siebzehn (hindi “siebenzehn”).'),
    C('achtzehn, neunzehn', '18, 19', '18, 19 – eighteen, nineteen', '18, 19 – labingwalo, labinsiyam'),
    C('dreizehn – dreißig', 'Gut hören: 13 = dreizehn, 30 = dreißig.', 'Listen carefully: 13 = dreizehn, 30 = dreißig.', 'Makinig mabuti: 13 = dreizehn, 30 = dreißig.'),
], [
    choice(X, 'hoeren', LISTEN, None, '16', ['60', '6'], L('„sechzehn“ endet auf „-zehn“: 16.', '“sechzehn” ends in “-zehn”: 16.', 'Nagtatapos sa “-zehn” ang “sechzehn”: 16.'), [G2], R('dreizehn'), audio='sechzehn'),
    choice(X, 'hoeren', LISTEN, None, '13', ['30', '3'], L('„dreizehn“ = 13. 30 ist „dreißig“.', '“dreizehn” = 13. 30 is “dreißig”.', '“dreizehn” = 13. Ang 30 ay “dreißig”.'), [G2], R('dreizehn'), audio='dreizehn'),
    short(X, 'hoeren', DIGITS, 'Die Zahl:', ['17'], L('„siebzehn“ = 17.', '“siebzehn” = 17.', '“siebzehn” = 17.'), [G2], R('dreizehn'), audio='siebzehn'),
    short(X, 'schreiben', WORD, '16', ['sechzehn'], L('16 = „sechzehn“ – ohne s vor „zehn“.', '16 = “sechzehn” – no s before “zehn”.', '16 = “sechzehn” – walang s bago ang “zehn”.'), [G2], R('dreizehn')),
    choice(X, 'grammatikWortschatz', CHOOSE, '7 + 10 = ?', 'siebzehn', ['siebenzehn', 'siebzig'], L('17 = „siebzehn“. „siebzig“ ist 70.', '17 = “siebzehn”. “siebzig” is 70.', '17 = “siebzehn”. Ang “siebzig” ay 70.'), [G2], R('dreizehn')),
])

# L06 ------------------------------------------------------------------ tens
lesson(6, L('20, 30, 40 … 100', '20, 30, 40 … 100', '20, 30, 40 … 100'), ['zwanzig', 'dreißig', 'vierzig', 'fünfzig', 'sechzig', 'siebzig', 'achtzig', 'neunzig', 'hundert', 'tausend', 'Million'], [
    C('zwanzig, dreißig, vierzig', 'Zehner enden auf „-zig“. Aber: dreißig mit ß!', 'Tens end in “-zig”. But: dreißig with ß!', 'Nagtatapos sa “-zig” ang tens. Pero: dreißig may ß!'),
    C('fünfzig, sechzig, siebzig', 'sechzig (nicht „sechszig“), siebzig (nicht „siebenzig“).', 'sechzig (not “sechszig”), siebzig (not “siebenzig”).', 'sechzig (hindi “sechszig”), siebzig (hindi “siebenzig”).'),
    C('achtzig, neunzig, hundert', '80, 90, 100', '80, 90, 100', '80, 90, 100'),
    C('tausend – eine Million', '1000 = tausend. 1 000 000 = eine Million.', '1000 = tausend. 1,000,000 = eine Million.', '1000 = tausend. 1,000,000 = eine Million.'),
], [
    choice(X, 'hoeren', LISTEN, None, '30', ['13', '3'], L('„dreißig“ = 30.', '“dreißig” = 30.', '“dreißig” = 30.'), [G2], R('dreißig'), audio='dreißig'),
    choice(X, 'hoeren', LISTEN, None, '70', ['17', '60'], L('„siebzig“ = 70. 17 ist „siebzehn“.', '“siebzig” = 70. 17 is “siebzehn”.', '“siebzig” = 70. Ang 17 ay “siebzehn”.'), [G2], R('siebzig'), audio='siebzig'),
    choice(X, 'lesen', READ, 'sechzig', '60', ['16', '70'], L('„sechzig“ = 60.', '“sechzig” = 60.', '“sechzig” = 60.'), [G2], R('sechzig')),
    short(X, 'schreiben', WORD, '30', ['dreißig', 'dreissig'], L('30 = „dreißig“ – mit ß, nicht „dreizig“.', '30 = “dreißig” – with ß, not “dreizig”.', '30 = “dreißig” – may ß, hindi “dreizig”.'), [G2], R('dreißig')),
    cloze(X, 'grammatikWortschatz', GAPS, 'zehn, zwanzig, {{1}}, vierzig, fünfzig, {{2}}, siebzig', [['dreißig', 'dreissig'], ['sechzig']], L('10, 20, 30, 40, 50, 60, 70.', '10, 20, 30, 40, 50, 60, 70.', '10, 20, 30, 40, 50, 60, 70.'), [G2], R('dreißig', 'sechzig')),
])

# L07 ------------------------------------------------------------------ 21–99
lesson(7, L('21 bis 99: zuerst die Einer', '21 to 99: the ones come first', '21 hanggang 99: una ang ones'), [], [
    C('einundzwanzig', '21 = ein + und + zwanzig. Zuerst die 1, dann die 20.', '21 = ein + und + zwanzig: first the 1, then the 20 (“one-and-twenty”).', '21 = ein + und + zwanzig: una ang 1, tapos ang 20.'),
    C('siebenundvierzig', '47 = sieben + und + vierzig.', '47 = sieben + und + vierzig (“seven-and-forty”).', '47 = sieben + und + vierzig (pito at apatnapu).'),
    C('vierundsiebzig', '74 = vier + und + siebzig. 47 und 74: gut hören!', '74 = vier + und + siebzig. 47 and 74: listen carefully!', '74 = vier + und + siebzig. 47 at 74: makinig mabuti!'),
    C('hundertzwanzig', '120 = hundert + zwanzig.', '120 = hundert + zwanzig.', '120 = hundert + zwanzig.'),
], [
    choice(X, 'hoeren', LISTEN, None, '47', ['74', '40'], L('„siebenundvierzig“: zuerst 7, dann 40 = 47.', '“siebenundvierzig”: first 7, then 40 = 47.', '“siebenundvierzig”: una 7, tapos 40 = 47.'), [G2], R('vierzig'), audio='siebenundvierzig'),
    choice(X, 'hoeren', LISTEN, None, '25', ['52', '35'], L('„fünfundzwanzig“ = 5 + 20 = 25.', '“fünfundzwanzig” = 5 + 20 = 25.', '“fünfundzwanzig” = 5 + 20 = 25.'), [G2], R('fünf', 'zwanzig'), audio='fünfundzwanzig'),
    short(X, 'hoeren', DIGITS, 'Die Zahl:', ['68'], L('„achtundsechzig“ = 8 + 60 = 68.', '“achtundsechzig” = 8 + 60 = 68.', '“achtundsechzig” = 8 + 60 = 68.'), [G2], R('acht', 'sechzig'), audio='achtundsechzig'),
    choice(X, 'lesen', READ, 'dreiundneunzig', '93', ['39', '903'], L('„dreiundneunzig“ = 3 + 90 = 93.', '“dreiundneunzig” = 3 + 90 = 93.', '“dreiundneunzig” = 3 + 90 = 93.'), [G2], R('drei', 'neunzig')),
    short(X, 'schreiben', WORD, '21', ['einundzwanzig'], L('21 = „einundzwanzig“ – „ein“, nicht „eins“.', '21 = “einundzwanzig” – “ein”, not “eins”.', '21 = “einundzwanzig” – “ein”, hindi “eins”.'), [G2], R('zwanzig')),
    cloze(X, 'grammatikWortschatz', GAPS, '34 = vier{{1}}dreißig', [['und']], L('Zwischen Einer und Zehner steht „und“: vierunddreißig.', 'Between ones and tens comes “und”: vierunddreißig.', 'Sa pagitan ng ones at tens: “und” – vierunddreißig.'), [G2], R('dreißig', 'und')),
])

# L08 ------------------------------------------------------------------ age
lesson(8, L('Wie alt sind Sie?', 'How old are you?', 'Ilang taon ka na?'), ['Alter', 'Jahre alt', 'werden', 'bald'], [
    C('Wie alt sind Sie?', 'So fragen Sie nach dem Alter. Mit „du“: „Wie alt bist du?“', 'This is how you ask about age. With “du”: “Wie alt bist du?”', 'Ganito itanong ang edad. Sa “du”: “Wie alt bist du?”'),
    C('Ich bin 35 Jahre alt.', 'Im Deutschen: „Ich bin … Jahre alt“ – mit „sein“, nicht mit „haben“!', 'In German: “Ich bin … Jahre alt” – with “sein” (to be), not “haben” (to have)!', 'Sa German: “Ich bin … Jahre alt” – gamit ang “sein”, hindi “haben”!'),
    C('Ich bin 35.', 'Kurz und auch richtig.', 'Short and also correct.', 'Maikli at tama rin.'),
    C('das Alter', 'Im Formular: „Alter: 35“.', 'In a form: “Alter (age): 35”.', 'Sa form: “Alter (edad): 35”.'),
    C('Ich werde bald 40.', '„werden“: ich werde, du wirst, er/sie wird. Bald = nicht lange.', '“werden” (to become): ich werde, du wirst, er/sie wird. “bald” = soon.', '“werden” (maging): ich werde, du wirst, er/sie wird. “bald” = malapit na.'),
], [
    choice(X, 'grammatikWortschatz', CHOOSE, 'Wie alt sind Sie?', 'Ich bin 42 Jahre alt.', ['Ich habe 42 Jahre.', 'Ich habe 42.'], L('Richtig ist: „Ich bin 42 Jahre alt.“ Mit „sein“ und mit „alt“.', 'Correct: “Ich bin 42 Jahre alt.” With “sein” and with “alt”.', 'Tama: “Ich bin 42 Jahre alt.” Gamit ang “sein” at “alt”.'), [G3, G6], R('Jahre alt', 'sein')),
    choice(X, 'hoeren', L('Hören Sie. Wie alt ist die Person?', 'Listen. How old is the person?', 'Makinig. Ilang taon na ang tao?'), None, '29', ['92'], L('„neunundzwanzig“ = 9 + 20 = 29.', '“neunundzwanzig” = 9 + 20 = 29.', '“neunundzwanzig” = 9 + 20 = 29.'), [G3, G2], R('Jahre alt'), audio='Ich bin neunundzwanzig Jahre alt.'),
    cloze(X, 'grammatikWortschatz', GAPS, 'Wie alt {{1}} du? – Ich {{2}} zwanzig.', [['bist'], ['bin']], L('du bist, ich bin – das Verb „sein“.', 'du bist, ich bin – the verb “sein”.', 'du bist, ich bin – ang verb na “sein”.'), [G3, G6], R('sein', 'Jahre alt')),
    choice(X, 'lesen', READ, 'Herr Bauer ist 64 Jahre alt. Frau Bauer ist 61. Wie alt ist Frau Bauer?', '61', ['64', '16'], L('Im Text steht: „Frau Bauer ist 61.“', 'The text says: “Frau Bauer ist 61.”', 'Sabi sa teksto: “Frau Bauer ist 61.”'), [G3], R('Jahre alt')),
    cloze(X, 'grammatikWortschatz', GAPS, 'Er ist 39. Er {{1}} bald 40.', [['wird']], L('„werden“: er wird. „Er wird bald 40“ = er ist bald 40 Jahre alt.', '“werden”: er wird. “Er wird bald 40” = he will soon be 40.', '“werden”: er wird. “Er wird bald 40” = malapit na siyang mag-40.'), [G3], R('werden', 'bald')),
])

# L09 ------------------------------------------------------------------ haben
lesson(9, L('haben: ich habe, du hast', 'haben: I have, you have', 'haben: mayroon ako, mayroon ka'), ['haben'], [
    C('ich habe, du hast', '„haben“ ist unregelmäßig: du hast (nicht „du habst“).', '“haben” (to have) is irregular: du hast (not “du habst”).', 'Irregular ang “haben”: du hast (hindi “du habst”).'),
    C('er hat, sie hat', 'er/sie/es hat', 'er/sie/es hat – he/she/it has', 'er/sie/es hat – siya ay may'),
    C('wir haben, ihr habt, Sie haben', 'wir haben · ihr habt · sie/Sie haben', 'we have: wir haben · you (several): ihr habt · they / you (polite): sie/Sie haben', 'tayo: wir haben · kayo: ihr habt · sila / kayo (magalang): sie/Sie haben'),
    C('Ich bin 30. – Ich habe zwei Namen.', 'Alter mit „sein“! „haben“ für Dinge: Ich habe einen Vornamen und einen Familiennamen.', 'Age with “sein”! “haben” for things: I have a first name and a family name.', 'Edad gamit ang “sein”! “haben” para sa bagay: may pangalan at apelyido ako.'),
], [
    cloze(X, 'grammatikWortschatz', GAPS, 'Du {{1}} zwei Namen: Vorname und Familienname.', [['hast']], L('„haben“: du hast (nicht „du habst“).', '“haben”: du hast (not “du habst”).', '“haben”: du hast (hindi “du habst”).'), [G6], R('haben', 'Vorname', 'Familienname')),
    cloze(X, 'grammatikWortschatz', GAPS, 'Der Name „Anna“ {{1}} vier Buchstaben.', [['hat']], L('„haben“: er hat.', '“haben”: er hat.', '“haben”: er hat.'), [G6], R('haben', 'Buchstabe')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Herr und Frau Bauer … vier Namen.', 'haben', ['habt', 'hat'], L('Herr und Frau Bauer = sie (mehrere): sie haben.', 'Mr and Mrs Bauer = sie (several people): sie haben.', 'Si Herr at Frau Bauer = sie (marami): sie haben.'), [G6], R('haben')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Ihr … zwei Namen?', 'habt', ['haben', 'hast'], L('„haben“: ihr habt.', '“haben”: ihr habt.', '“haben”: ihr habt.'), [G6], R('haben')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Was ist richtig?', 'Sie ist 25 Jahre alt.', ['Sie hat 25 Jahre alt.', 'Sie hat 25 Jahre.'], L('Alter immer mit „sein“: Sie ist 25 Jahre alt.', 'Age always with “sein”: Sie ist 25 Jahre alt.', 'Edad laging may “sein”: Sie ist 25 Jahre alt.'), [G6, G3], R('sein', 'Jahre alt')),
])

# L10 ------------------------------------------------------------------ phone number
lesson(10, L('Die Telefonnummer', 'The phone number', 'Ang numero ng telepono'), ['Telefonnummer', 'Nummer', 'kennen'], [
    C('Wie ist Ihre Telefonnummer?', 'So fragen Sie höflich. Mit „du“: „Wie ist deine Telefonnummer?“', 'Polite question. With “du”: “Wie ist deine Telefonnummer?”', 'Magalang na tanong. Sa “du”: “Wie ist deine Telefonnummer?”'),
    dict(C('null – sechs – sechs – vier …', 'Telefonnummern sagt man oft Zahl für Zahl.', 'Phone numbers are often said digit by digit.', 'Kadalasang sinasabi ang numero ng telepono isa-isa.'), audioText='null, sechs, sechs, vier'),
    dict(C('Die Nummer ist 0664 123 45 67.', 'Handynummern in Österreich beginnen oft mit 0664, 0676, 0650 oder 0699.', 'Mobile numbers in Austria often start with 0664, 0676, 0650 or 0699.', 'Ang mobile number sa Austria ay kadalasang nagsisimula sa 0664, 0676, 0650 o 0699.'), audioText=f'Die Nummer ist {digits("06641234567")}.'),
    C('Kennen Sie die Nummer?', '„kennen“: ich kenne, du kennst, er/sie kennt, Sie kennen.', '“kennen” (to know): ich kenne, du kennst, er/sie kennt, Sie kennen.', '“kennen” (kilala/alam): ich kenne, du kennst, er/sie kennt, Sie kennen.'),
], [
    choice(X, 'hoeren', L('Hören Sie. Wie ist die Telefonnummer?', 'Listen. What is the phone number?', 'Makinig. Ano ang numero ng telepono?'), None, '0676 384 21', ['0676 348 21'], L(f'Sie hören: {digits("067638421")}.', f'You hear: {digits("067638421")}.', f'Naririnig mo: {digits("067638421")}.'), [G4, G2], R('Telefonnummer'), audio=f'Meine Nummer ist {digits("067638421")}.'),
    short(X, 'schreiben', L('Hören Sie. Schreiben Sie die Telefonnummer in Ziffern.', 'Listen. Write the phone number in digits.', 'Makinig. Isulat ang numero ng telepono gamit ang digits.'), 'Telefonnummer:', ['0650 7193', '06507193', '0650 71 93', '0650/7193', '0650-7193', '0650 / 7193'], L(f'Sie hören: {digits("06507193")}.', f'You hear: {digits("06507193")}.', f'Naririnig mo: {digits("06507193")}.'), [G4], R('Telefonnummer'), audio=digits('06507193')),
    choice(X, 'sprechen', SAY, 'Wie ist Ihre Telefonnummer?', 'Null, sechs, neun, neun …', ['Ich bin null sechs neun neun.', 'Ich heiße null sechs neun neun.'], L('Sie sagen einfach die Zahlen: „Null, sechs, neun, neun …“ oder: „Meine Nummer ist …“', 'You just say the digits: “Null, sechs, neun, neun …” or: “Meine Nummer ist …”', 'Sabihin lang ang mga numero: “Null, sechs, neun, neun …” o: “Meine Nummer ist …”'), [G4], R('Telefonnummer')),
    cloze(X, 'grammatikWortschatz', GAPS, '{{1}} Sie die Nummer? – Nein, ich kenne die Nummer nicht.', [['Kennen']], L('„kennen“: Sie kennen. Die Frage beginnt mit dem Verb.', '“kennen”: Sie kennen. The question starts with the verb.', '“kennen”: Sie kennen. Nagsisimula sa verb ang tanong.'), [G6], R('kennen', 'Nummer')),
])

# L11 ------------------------------------------------------------------ house number, postcode, picture
lesson(11, L('Hausnummer und Postleitzahl', 'House number and postcode', 'Numero ng bahay at postal code'), ['Hausnummer', 'Postleitzahl'], [
    C('die Hausnummer: 17', 'Die Hausnummer steht am Haus.', 'The house number is on the house.', 'Nasa bahay ang numero ng bahay.'),
    dict(C('die Postleitzahl: 9020 Klagenfurt', 'Postleitzahlen in Österreich haben vier Zahlen: 1010 Wien, 8010 Graz, 4020 Linz, 5020 Salzburg.', 'Postcodes in Austria have four digits: 1010 Vienna, 8010 Graz, 4020 Linz, 5020 Salzburg.', 'Apat na digit ang postal code sa Austria: 1010 Vienna, 8010 Graz, 4020 Linz, 5020 Salzburg.'), audioText=f'die Postleitzahl: {digits("9020")}, Klagenfurt'),
    C('neun – null – zwei – null', 'Die Postleitzahl sagt man meist Zahl für Zahl.', 'The postcode is usually said digit by digit.', 'Kadalasang sinasabi ang postal code isa-isa.'),
    C('Top 3', 'In Österreich hat die Wohnung im Haus eine Nummer: „Top 3“. (in Deutschland: „Wohnung 3“)', 'In Austria the flat in a building has a number: “Top 3” (in Germany: “Wohnung 3”).', 'Sa Austria may numero ang apartment: “Top 3” (sa Germany: “Wohnung 3”).'),
], [
    choice(X, 'lesen', LOOK('Look at the picture. What is the house number?', 'Tingnan ang larawan. Ano ang numero ng bahay?'), 'Was ist die Hausnummer?', '17', ['71', '3'], L('Am Haus steht 17.', 'The house shows 17.', 'Nakasulat sa bahay ang 17.'), [G4], R('Hausnummer'), img=IMG_KLINGEL()),
    choice(X, 'lesen', LOOK('Look at the picture. Which flat number (Top) does Mr Santos have?', 'Tingnan ang larawan. Anong numero (Top) ni Herr Santos?'), 'Santos: Top …', '2', ['1', '4'], L('Auf der Klingel steht: Top 2 – Santos.', 'The doorbell says: Top 2 – Santos.', 'Sa doorbell: Top 2 – Santos.'), [G4], R('Nummer'), img=IMG_KLINGEL()),
    choice(X, 'lesen', LOOK('Look at the picture. Who lives in flat 4 (Top 4)?', 'Tingnan ang larawan. Sino ang nasa Top 4?'), 'Top 4: Wer ist das?', 'Mayer', ['Huber', 'Berger'], L('Auf der Klingel steht: Top 4 – Mayer.', 'The doorbell says: Top 4 – Mayer.', 'Sa doorbell: Top 4 – Mayer.'), [G4], R('Nummer'), img=IMG_KLINGEL()),
    choice(X, 'hoeren', L('Hören Sie. Wie ist die Postleitzahl?', 'Listen. What is the postcode?', 'Makinig. Ano ang postal code?'), None, '8010', ['8100'], L('Sie hören: acht, null, eins, null = 8010 (Graz).', 'You hear: acht, null, eins, null = 8010 (Graz).', 'Naririnig mo: acht, null, eins, null = 8010 (Graz).'), [G4], R('Postleitzahl'), audio=f'Die Postleitzahl ist {digits("8010")}.'),
    cloze(X, 'schreiben', L('Lesen Sie und schreiben Sie die Zahlen.', 'Read and write the numbers.', 'Basahin at isulat ang mga numero.'), 'Ich bin Anna Huber. Hausnummer: zwölf. Postleitzahl: eins, null, eins, null.\nHausnummer: {{1}} · Postleitzahl: {{2}}', [['12'], ['1010']], L('zwölf = 12; eins, null, eins, null = 1010 (Wien).', 'zwölf = 12; eins, null, eins, null = 1010 (Vienna).', 'zwölf = 12; eins, null, eins, null = 1010 (Vienna).'), [G4], R('Hausnummer', 'Postleitzahl')),
])

# L12 ------------------------------------------------------------------ prices, picture
lesson(12, L('Was kostet das? – Euro und Cent', 'How much is it? – Euros and cents', 'Magkano? – Euro at cent'), ['Euro', 'Cent', 'Preis', 'kosten'], [
    C('Was kostet das?', 'So fragen Sie nach dem Preis. Auch: „Wie viel kostet das?“', 'This is how you ask the price. Also: “Wie viel kostet das?”', 'Ganito magtanong ng presyo. Puwede rin: “Wie viel kostet das?”'),
    dict(C('Das kostet 2,50 €.', 'Man sagt: „zwei Euro fünfzig“. Das Komma sagt man nicht.', 'You say: “zwei Euro fünfzig”. You don’t say the comma.', 'Sinasabi: “zwei Euro fünfzig”. Hindi sinasabi ang comma.'), audioText='Das kostet zwei Euro fünfzig.'),
    dict(C('Das kostet 1,20 €.', '„ein Euro zwanzig“ – „ein“, nicht „eins“.', '“ein Euro zwanzig” – “ein”, not “eins”.', '“ein Euro zwanzig” – “ein”, hindi “eins”.'), audioText='Das kostet ein Euro zwanzig.'),
    dict(C('Das kostet 90 Cent.', 'Unter einem Euro: Cent. 100 Cent = 1 Euro.', 'Below one euro: cents. 100 cents = 1 euro.', 'Kulang sa isang euro: cent. 100 cent = 1 euro.'), audioText='Das kostet neunzig Cent.'),
    C('die Äpfel · das Brot · die Milch', 'Wörter aus dem Bild. Sie lernen sie später genau.', 'Words from the picture: apples, bread, milk. You will learn them properly later.', 'Mga salita sa larawan: mansanas, tinapay, gatas. Matututunan mo ito nang maayos mamaya.'),
    dict(C('der Preis', 'Der Preis ist 3,10 €.', 'The price (Preis) is €3.10.', 'Ang presyo (Preis) ay €3.10.'), audioText='der Preis. Der Preis ist drei Euro zehn.'),
], [
    choice(X, 'hoeren', L('Hören Sie. Wie viel kostet das?', 'Listen. How much does it cost?', 'Makinig. Magkano ito?'), None, '4,80 €', ['8,40 €'], L(f'Sie hören: „{euro(480)[1]}“ = 4,80 €.', f'You hear: “{euro(480)[1]}” = €4.80.', f'Naririnig mo: “{euro(480)[1]}” = €4.80.'), [G5], R('kosten', 'Euro'), audio=f'Das kostet {euro(480)[1]}.'),
    choice(X, 'lesen', LOOK('Look at the picture. How much is the bread?', 'Tingnan ang larawan. Magkano ang tinapay?'), 'Wie viel kostet das Brot?', '3,10 €', ['2,40 €', '1,19 €'], L('Am Brot steht 3,10 €.', 'The bread shows €3.10.', 'Nakalagay sa tinapay: €3.10.'), [G5], R('kosten', 'Preis'), img=IMG_MARKT()),
    choice(X, 'lesen', LOOK('Look at the picture. How much is the milk?', 'Tingnan ang larawan. Magkano ang gatas?'), 'Wie viel kostet die Milch?', '1,19 €', ['3,10 €', '1,91 €'], L('An der Milch steht 1,19 € – ein Euro neunzehn.', 'The milk shows €1.19 – ein Euro neunzehn.', 'Nakalagay sa gatas: €1.19 – ein Euro neunzehn.'), [G5], R('kosten', 'Cent'), img=IMG_MARKT()),
    choice(X, 'lesen', LOOK('Look at the picture. How much are the apples?', 'Tingnan ang larawan. Magkano ang mansanas?'), 'Wie viel kosten die Äpfel?', '2,40 €', ['4,20 €', '3,10 €'], L('An den Äpfeln steht 2,40 € – zwei Euro vierzig.', 'The apples show €2.40 – zwei Euro vierzig.', 'Nakalagay sa mansanas: €2.40 – zwei Euro vierzig.'), [G5], R('kosten', 'Preis'), img=IMG_MARKT()),
    choice(X, 'sprechen', L('Wie sagt man den Preis? Wählen Sie, dann sagen Sie es laut.', 'How do you say the price? Choose, then say it aloud.', 'Paano sabihin ang presyo? Pumili, tapos sabihin nang malakas.'), '2,50 €', 'zwei Euro fünfzig', ['zwei Komma fünf Euro', 'fünfzig Euro zwei'], L('Zuerst die Euro, dann die Cent: „zwei Euro fünfzig“.', 'First the euros, then the cents: “zwei Euro fünfzig”.', 'Una ang euro, tapos ang cent: “zwei Euro fünfzig”.'), [G5], R('Euro')),
    cloze(X, 'grammatikWortschatz', GAPS, 'Was {{1}} das? – Das kostet neunzig {{2}}.', [['kostet'], ['Cent']], L('„Was kostet das?“ – unter einem Euro sagt man „Cent“.', '“Was kostet das?” – below one euro you say “Cent”.', '“Was kostet das?” – kulang sa isang euro, “Cent”.'), [G5], R('kosten', 'Cent')),
])

# L13 ------------------------------------------------------------------ wie viel / wie viele, quantities
lesson(13, L('Wie viel? Wie viele?', 'How much? How many?', 'Magkano? Ilan?'), ['wie viel', 'wie viele', 'viel', 'wenig', 'mehr', 'genug', 'nur', 'alle', 'etwas', 'nichts'], [
    C('Wie viel kostet das?', '„wie viel“ für Geld und für Dinge ohne Plural.', '“wie viel” for money and things you can’t count.', '“wie viel” para sa pera at bagay na hindi binibilang.'),
    C('Wie viele Buchstaben hat „Euro“?', '„wie viele“ für Dinge im Plural, die man zählt.', '“wie viele” for plural things you count.', '“wie viele” para sa mga bagay na binibilang (plural).'),
    C('Wie viel? – Wort auf Platz 1, Verb auf Platz 2', 'Bei W-Fragen: Fragewort zuerst, dann das Verb: „Wie viel kostet das?“', 'In W-questions: question word first, then the verb: “Wie viel kostet das?”', 'Sa W-question: una ang tanong na salita, tapos ang verb: “Wie viel kostet das?”'),
    C('viel – wenig – mehr – genug', '100 € – das ist viel. 1 € – das ist wenig. 5 € ist mehr als 2 €. 5 € für 5 € – das ist genug.', 'viel = much, wenig = little, mehr = more, genug = enough.', 'viel = marami, wenig = kaunti, mehr = mas marami, genug = sapat.'),
    C('alle – etwas – nichts – nur', 'Alle sind da. Ich habe etwas. Ich habe nichts. Nur 2 Euro!', 'alle = all, etwas = something, nichts = nothing, nur = only.', 'alle = lahat, etwas = kaunti/isang bagay, nichts = wala, nur = lang.'),
], [
    cloze(X, 'grammatikWortschatz', GAPS, '{{1}} kostet das? – Drei Euro.', [['Wie viel', 'Wieviel', 'Was']], L('Für den Preis fragt man: „Wie viel kostet das?“ oder „Was kostet das?“', 'For the price you ask: “Wie viel kostet das?” or “Was kostet das?”', 'Para sa presyo: “Wie viel kostet das?” o “Was kostet das?”'), [G7], R('wie viel')),
    cloze(X, 'grammatikWortschatz', GAPS, '{{1}} Buchstaben hat „Preis“? – Fünf.', [['Wie viele', 'Wieviele']], L('Buchstaben zählt man: „Wie viele Buchstaben …?“', 'You count letters: “Wie viele Buchstaben …?”', 'Binibilang ang titik: “Wie viele Buchstaben …?”'), [G7], R('wie viele', 'Buchstabe')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Welche Frage ist richtig?', 'Wie viel kostet das?', ['Wie viel das kostet?', 'Kostet wie viel das?'], L('W-Frage: Fragewort auf Platz 1, Verb auf Platz 2.', 'W-question: question word in position 1, verb in position 2.', 'W-question: tanong na salita sa 1, verb sa 2.'), [G7], R('wie viel', 'kosten')),
    choice(X, 'lesen', READ, 'Maria hat 2 Euro. Das kostet 5 Euro. Hat Maria genug?', 'Nein, sie hat nur 2 Euro.', ['Ja, sie hat mehr.', 'Ja, sie hat genug.'], L('2 Euro ist weniger als 5 Euro. Sie hat nicht genug, nur 2 Euro.', '2 euros is less than 5 euros. She doesn’t have enough, only 2 euros.', 'Mas kaunti ang 2 euro kaysa 5 euro. Hindi sapat, 2 euro lang.'), [G5], R('genug', 'nur', 'mehr')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Herr Bauer hat null Euro. Er hat …', 'nichts', ['alle', 'viel'], L('0 Euro = „nichts“.', '0 euros = “nichts” (nothing).', '0 euro = “nichts” (wala).'), [G5], R('nichts')),
])

# L14 ------------------------------------------------------------------ paying, verbs
lesson(14, L('Zusammen, bitte!', 'Together, please!', 'Lahat-lahat na, please!'), ['zusammen', 'allein', 'zurück', 'schon', 'vielleicht', 'möglich', 'machen', 'sagen', 'fragen', 'antworten', 'wieder'], [
    C('Das macht zusammen 7 Euro.', 'So sagt man den Preis für alles: „zusammen“.', 'This is how you say the price for everything: “zusammen” (in total).', 'Ganito sabihin ang kabuuang presyo: “zusammen”.'),
    C('10 Euro, bitte. – 3 Euro zurück.', 'Sie zahlen 10 €. Das kostet 7 €. Sie bekommen 3 € zurück.', 'You pay €10. It costs €7. You get €3 back (zurück).', 'Nagbayad ka ng €10. €7 ang presyo. May €3 kang sukli (zurück).'),
    C('Ich frage, Sie antworten.', '„fragen“ und „antworten“: ich frage, du fragst … ich antworte, du antwortest …', '“fragen” (ask) and “antworten” (answer): ich frage, du fragst … ich antworte, du antwortest …', '“fragen” (magtanong) at “antworten” (sumagot).'),
    C('Was sagen Sie? Noch einmal, bitte – wieder!', '„sagen“: ich sage, du sagst. „wieder“ = noch einmal.', '“sagen” (to say): ich sage, du sagst. “wieder” = again.', '“sagen” (sabihin): ich sage, du sagst. “wieder” = ulit.'),
    C('Vielleicht. – Ist das möglich?', 'vielleicht = nicht sicher.', 'vielleicht = maybe. möglich = possible.', 'vielleicht = siguro. möglich = posible.'),
    C('Ich bin schon da. – Ich bin allein.', 'schon = früher als gedacht. allein = ohne andere Personen.', 'schon = already. allein = alone.', 'schon = na. allein = mag-isa.'),
], [
    choice(X, 'hoeren', L('Hören Sie. Wie viel kostet das zusammen?', 'Listen. How much is it in total?', 'Makinig. Magkano lahat-lahat?'), None, '12 €', ['20 €'], L('Sie hören: „Das macht zusammen zwölf Euro.“', 'You hear: “Das macht zusammen zwölf Euro.”', 'Naririnig mo: “Das macht zusammen zwölf Euro.”'), [G5], R('zusammen', 'machen'), audio='Das macht zusammen zwölf Euro.'),
    choice(X, 'lesen', READ, 'Das kostet 6 Euro. Sie zahlen 10 Euro. Wie viel bekommen Sie zurück?', '4 Euro', ['6 Euro', '16 Euro'], L('10 € – 6 € = 4 € zurück.', '€10 – €6 = €4 back.', '€10 – €6 = €4 na sukli.'), [G5], R('zurück')),
    cloze(X, 'grammatikWortschatz', GAPS, 'Ich {{1}}: „Wie alt bist du?“ – Du {{2}}: „Ich bin zwanzig.“', [['frage'], ['antwortest']], L('ich frage, du antwortest.', 'ich frage (I ask), du antwortest (you answer).', 'ich frage (nagtatanong ako), du antwortest (sumasagot ka).'), [G6], R('fragen', 'antworten')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Sie verstehen nicht. Die Person sagt es …', 'wieder', ['allein', 'schon'], L('„wieder“ = noch einmal.', '“wieder” = again.', '“wieder” = ulit.'), None, R('wieder')),
    choice(X, 'sprechen', SAY, 'Das kostet 3 Euro und das kostet 2 Euro. Sie möchten alles zahlen.', 'Zusammen, bitte.', ['Allein, bitte.', 'Nichts, bitte.'], L('Für alles zusammen sagen Sie: „Zusammen, bitte.“', 'For everything at once you say: “Zusammen, bitte.”', 'Para sa lahat: “Zusammen, bitte.”'), [G5], R('zusammen')),
])

# L15 ------------------------------------------------------------------ emergency numbers (A1-WOW-09, Q101)
EMERG_EXP = L('Notrufe in Österreich: 122 Feuerwehr, 133 Polizei, 144 Rettung, 112 Euro-Notruf.', 'Emergency numbers in Austria: 122 fire brigade, 133 police, 144 ambulance, 112 European emergency number.',
              'Mga emergency number sa Austria: 122 bumbero, 133 pulis, 144 ambulansya, 112 European emergency number.')
lesson(15, L('Notruf: 112, 122, 133, 144', 'Emergency: 112, 122, 133, 144', 'Emergency: 112, 122, 133, 144'), [], [
    C('122 – Feuerwehr', 'Es brennt? Rufen Sie 122 an: hundertzweiundzwanzig, oder: eins – zwei – zwei.', 'Fire? Call 122 (fire brigade).', 'May sunog? Tumawag sa 122 (bumbero).'),
    C('133 – Polizei', 'Ein Diebstahl, Gewalt, Gefahr durch Menschen? Polizei: 133.', 'Theft, violence, danger from people? Police: 133.', 'Nakawan, karahasan, panganib mula sa tao? Pulis: 133.'),
    C('144 – Rettung', 'Eine Person ist schwer krank oder verletzt? Rettung: 144.', 'Someone is seriously ill or injured? Ambulance (Rettung): 144.', 'May taong malubhang may sakit o sugatan? Ambulansya (Rettung): 144.'),
    C('112 – Euro-Notruf', '112 funktioniert in ganz Europa, auch mit dem Handy.', '112 works all over Europe, also from a mobile.', 'Gumagana ang 112 sa buong Europe, pati sa cellphone.'),
    C('141 und 1450', '141: Ärztenotdienst (nachts, am Wochenende). 1450: Gesundheitsberatung am Telefon.', '141: doctor on call (at night, weekends). 1450: health advice by phone.', '141: doktor na naka-duty (gabi, weekend). 1450: payo sa kalusugan sa telepono.'),
], [
    choice(X, 'werte', LOOK('Look at the picture. Which number is for the police?', 'Tingnan ang larawan. Anong numero para sa pulis?'), 'Polizei: Welche Nummer?', '133', ['122', '144'], EMERG_EXP, [G8], R('Nummer'), img=IMG_NOTRUF()),
    choice(X, 'werte', LOOK('Look at the picture. Which number is for the ambulance?', 'Tingnan ang larawan. Anong numero para sa ambulansya?'), 'Rettung: Welche Nummer?', '144', ['133', '122'], EMERG_EXP, [G8], R('Nummer'), img=IMG_NOTRUF()),
    choice(X, 'werte', L('Ein Haus brennt. Welche Nummer rufen Sie an?', 'A house is on fire. Which number do you call?', 'May nasusunog na bahay. Anong numero ang tatawagan mo?'), None, '122', ['133', '1450'], EMERG_EXP, [G8], R('Nummer')),
    choice(X, 'werte', L('Welche Nummer funktioniert in ganz Europa?', 'Which number works all over Europe?', 'Anong numero ang gumagana sa buong Europe?'), None, '112', ['141', '133'], EMERG_EXP, [G8], R('Nummer')),
    choice(X, 'hoeren', LISTEN, None, '144', ['14'], L('Sie hören „hundertvierundvierzig“ = 144: Rettung.', 'You hear “hundertvierundvierzig” = 144: ambulance.', 'Naririnig mo ang “hundertvierundvierzig” = 144: ambulansya.'), [G8, G2], R('hundert'), audio='Die Nummer ist hundertvierundvierzig.'),
])


# ---- one picture task per lesson (rule from 16.11.2026: ≥ 1 meaningful picture per lesson)
PIC = LOOK()
PICS = {
    1: ('replace', 3, choice(X, 'grammatikWortschatz', PIC, 'Welcher Buchstabe fehlt?', 'H', ['G', 'K'], L('G, H, I – H kommt nach G.', 'G, H, I – H comes after G.', 'G, H, I – ang H ay pagkatapos ng G.'), refs=R('Buchstabe'),
                            img=img('alphabet', 'Ein Plakat mit dem Alphabet von A bis M. Ein Buchstabe fehlt.', 'A poster with the alphabet from A to M. One letter is missing.', 'Poster ng alpabeto mula A hanggang M. May isang titik na kulang.'))),
    2: ('add', None, choice(X, 'lesen', PIC, 'Welchen Umlaut sehen Sie auf dem Schild?', 'Ö', ['Ü', 'Ä'], L('„ÖSTERREICH“ beginnt mit Ö.', '“ÖSTERREICH” starts with Ö.', 'Nagsisimula sa Ö ang “ÖSTERREICH”.'), refs=R('Buchstabe', 'Österreich'),
                            img=img('grenze', 'Ein Schild an der Grenze mit der Flagge von Österreich.', 'A sign at the border with the Austrian flag.', 'Karatula sa border na may bandila ng Austria.'))),
    3: ('add', None, choice(X, 'lesen', PIC, 'Welcher Buchstabe fehlt im Formular?', 'B', ['P', 'D'], L('Die Frau buchstabiert H – U – B – E – R. Im Formular fehlt das B.', 'The woman spells H – U – B – E – R. The B is missing in the form.', 'Nag-spell ang babae: H – U – B – E – R. Kulang ang B sa form.'), [G1], R('buchstabieren', 'Buchstabe'),
                            img=img('buchstabieren', 'Eine Frau buchstabiert ihren Namen am Schalter. Ein Mann schreibt ihn in ein Formular.', 'A woman spells her name at a counter. A man writes it on a form.', 'Nag-i-spell ang babae ng pangalan niya sa counter. Isinusulat ito ng lalaki sa form.'))),
    4: ('add', None, choice(X, 'lesen', PIC, 'Welche Zahl sehen Sie vorne?', 'zwölf', ['zwei', 'elf'], L('Vorne steht 12 = zwölf.', 'The front of the tram shows 12 = zwölf.', 'Nakasulat sa harap ng tram ang 12 = zwölf.'), [G2], R('zwölf'),
                            img=img('bim', 'Eine rote Bim an der Haltestelle. Vorne steht eine Zahl.', 'A red tram at the stop. There is a number on the front.', 'Pulang tram sa hintuan. May numero sa harap.'))),
    5: ('add', None, choice(X, 'lesen', PIC, 'Welche Zahl hat der Spieler?', 'achtzehn', ['achtzig', 'acht'], L('Auf dem T-Shirt steht 18 = achtzehn.', 'The shirt shows 18 = achtzehn.', 'Nakasulat sa shirt ang 18 = achtzehn.'), [G2], R('dreizehn'),
                            img=img('trikot', 'Ein Fußballspieler von hinten. Auf dem T-Shirt steht eine Zahl.', 'A football player from behind. There is a number on the shirt.', 'Isang manlalaro ng football mula sa likod. May numero sa shirt.'))),
    6: ('add', None, choice(X, 'lesen', PIC, 'Auf dem Schild steht …', 'fünfzig', ['fünfzehn', 'fünf'], L('Auf dem Schild steht 50 = fünfzig. Im Ort fährt man in Österreich meist 50 km/h.', 'The sign shows 50 = fünfzig. In towns in Austria the limit is usually 50 km/h.', 'Nakasulat sa karatula ang 50 = fünfzig. Sa bayan sa Austria, kadalasang 50 km/h.'), [G2], R('fünfzig'),
                            img=img('tempo', 'Ein Verkehrsschild am Ortsanfang. Daneben stehen Häuser.', 'A traffic sign at the entrance to a town. There are houses next to it.', 'Isang traffic sign sa pasukan ng bayan. May mga bahay sa tabi.'))),
    7: ('add', None, choice(X, 'lesen', PIC, 'Graz: wie viele Kilometer?', 'siebenundvierzig', ['vierundsiebzig', 'vierzig'], L('Graz: 47 km = siebenundvierzig. Linz: 74 km = vierundsiebzig.', 'Graz: 47 km = siebenundvierzig (seven-and-forty). Linz: 74 km = vierundsiebzig.', 'Graz: 47 km = siebenundvierzig (pito at apatnapu). Linz: 74 km = vierundsiebzig.'), [G2], R('vierzig', 'wie viele'),
                            img=img('wegweiser', 'Ein blaues Straßenschild mit zwei Städten und Kilometern.', 'A blue road sign with two cities and distances.', 'Asul na karatula sa kalsada na may dalawang lungsod at kilometro.'))),
    8: ('add', None, choice(X, 'lesen', PIC, 'Wie alt wird Lukas?', 'vierzig', ['vierzehn', 'vier'], L('Auf der Torte steht 40: Lukas wird vierzig.', 'The cake shows 40: Lukas turns forty (vierzig).', 'Nakasulat sa cake ang 40: magiging apatnapu (vierzig) si Lukas.'), [G3], R('werden', 'vierzig'),
                            img=img('geburtstag', 'Eine Geburtstagstorte mit Kerzen und einem Schild für Lukas.', 'A birthday cake with candles and a sign for Lukas.', 'Birthday cake na may kandila at karatula para kay Lukas.'))),
    9: ('add', None, choice(X, 'grammatikWortschatz', PIC, 'Welcher Name hat fünf Buchstaben?', 'MARIA', ['ANNA', 'KATHARINA'], L('M – A – R – I – A: Der Name hat fünf Buchstaben. ANNA hat vier, KATHARINA hat neun.', 'M – A – R – I – A: the name has five letters. ANNA has four, KATHARINA has nine.', 'M – A – R – I – A: limang titik. Apat ang ANNA, siyam ang KATHARINA.'), [G6], R('haben', 'Buchstabe', 'fünf'),
                            img=img('namensschilder', 'Drei Namensschilder mit Namen.', 'Three name badges with names.', 'Tatlong name badge na may pangalan.'))),
    10: ('add', None, choice(X, 'lesen', PIC, 'Wie ist die Telefonnummer von Sofia Berger?', '0676 384 21 50', ['0676 348 21 50', '0667 384 21 50'], L('Auf dem Handy steht: 0676 384 21 50.', 'The phone shows: 0676 384 21 50.', 'Nakalagay sa cellphone: 0676 384 21 50.'), [G4], R('Telefonnummer'),
                             img=img('handy', 'Ein Handy mit einem Kontakt.', 'A mobile phone showing a contact.', 'Cellphone na may contact.'))),
    13: ('add', None, choice(X, 'lesen', PIC, 'Wie viel Euro sind das?', '7,50 €', ['6,50 €', '5,52 €'], L('5 € + 1 € + 1 € + 50 Cent = 7,50 € – sieben Euro fünfzig.', '€5 + €1 + €1 + 50 cents = €7.50 – sieben Euro fünfzig.', '€5 + €1 + €1 + 50 cent = €7.50 – sieben Euro fünfzig.'), [G5], R('wie viel', 'Euro', 'Cent'),
                             img=img('geld', 'Geld auf einem Tisch: ein Geldschein und Münzen.', 'Money on a table: a banknote and coins.', 'Pera sa mesa: isang perang papel at mga barya.'))),
    14: ('add', None, choice(X, 'lesen', PIC, 'Wie viel Geld bekommt man zurück?', '3,31 €', ['6,69 €', '10,00 €'], L('Auf der Rechnung: zusammen 6,69 €, bar 10,00 €, zurück 3,31 €.', 'On the receipt: total €6.69, cash €10.00, back (change) €3.31.', 'Sa resibo: kabuuan €6.69, cash €10.00, sukli €3.31.'), [G5], R('zurück', 'zusammen'),
                             img=img('rechnung', 'Eine Rechnung aus einem Geschäft.', 'A receipt from a shop.', 'Resibo mula sa tindahan.'))),
}
for n, (how, at, it) in PICS.items():
    les = lessons[n - 1]
    if how == 'replace':
        it['id'] = les['items'][at]['id']
        les['items'][at] = it
    else:
        it['id'] = f"{les['id']}-I{len(les['items']) + 1}"
        les['items'].append(it)
assert all(any('image' in i for i in l['items']) for l in lessons), [l['id'] for l in lessons if not any('image' in i for i in l['items'])]

# every vocab id introduced, except the number set (see spec-gaps G-014)
introduced = {r for l in lessons for r in l['introduces']}
missing = [v['lemma'] for v in vocab if v['id'] not in introduced and v['id'] not in NO_CARD]
print('not introduced:', missing)

out = {'schemaVersion': 1, 'chapterId': CH, 'tlReviewStatus': 'machine', 'vocab': vocab, 'lessons': lessons}
json.dump(out, open(f'{ROOT}/src/lib/content/a1-02.json', 'w'), ensure_ascii=False, indent='\t')
print(len(lessons), 'lessons', sum(len(l['items']) for l in lessons), 'items')
