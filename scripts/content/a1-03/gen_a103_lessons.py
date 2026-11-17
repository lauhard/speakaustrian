# A1-03 lessons -> src/lib/content/a1-03.json
import json
from gen_a103_common import *

V = {
    'der': ('der (article, masculine)', 'der (article, panlalaki)'), 'die': ('die (article, feminine; plural)', 'die (article, pambabae; plural)'),
    'das': ('das (article, neuter)', 'das (article, neutral)'), 'ein': ('a, an (ein / eine)', 'isang (ein / eine)'),
    'wo': ('where', 'saan'), 'doch': ('yes (after a negative question)', 'oo naman (sagot sa negatibong tanong)'), 'hier': ('here', 'dito'),
    'dort': ('there', 'doon'), 'da': ('there, here', 'diyan / nandito'), 'in': ('in', 'sa (loob)'), 'aus': ('from, out of', 'mula sa / galing sa'),
    'sprechen': ('to speak', 'magsalita'), 'verstehen': ('to understand', 'umintindi'), 'geben': ('to give', 'magbigay'), 'nehmen': ('to take', 'kumuha'),
    'finden': ('to find', 'mahanap'), 'suchen': ('to look for', 'maghanap'), 'wohnen': ('to live (somewhere)', 'tumira'), 'langsam': ('slow, slowly', 'mabagal'),
    'Sprache': ('language', 'wika'), 'Deutsch': ('German (language)', 'German (wika)'), 'Englisch': ('English', 'Ingles'), 'Tagalog': ('Tagalog', 'Tagalog'),
    'wiederholen': ('to repeat', 'ulitin'), 'Mensch': ('human being, person', 'tao'), 'Land': ('country', 'bansa'), 'Heimatland': ('home country', 'sariling bansa'),
    'Österreicher, Österreicherin': ('Austrian (man, woman)', 'Austrian (lalaki, babae)'), 'österreichisch': ('Austrian (adjective)', 'Austrian (adjective)'),
    'Deutschland': ('Germany', 'Germany'), 'Schweiz': ('Switzerland', 'Switzerland'), 'Philippiner, Philippinerin': ('Filipino (man, woman)', 'Pilipino, Pilipina'),
    'Europa': ('Europe', 'Europa'), 'Ausland': ('abroad, foreign countries', 'ibang bansa'), 'Stadt': ('town, city', 'lungsod'), 'Dorf': ('village', 'baryo / nayon'),
    'Adresse': ('address', 'address'), 'Straße': ('street', 'kalye'), 'E-Mail': ('e-mail (in Germany: die E-Mail)', 'e-mail (sa Germany: die E-Mail)'),
    'Hobby': ('hobby', 'libangan'), 'auf Wiederhören': ('goodbye (on the phone)', 'paalam (sa telepono)'), 'Ausländer, Ausländerin': ('foreigner (man, woman)', 'dayuhan (lalaki, babae)'),
    'Heimat': ('home, homeland', 'pinagmulan / sariling bayan'), 'ausländisch': ('foreign', 'banyaga'),
}
ART = {'Sprache': 'die', 'Mensch': 'der', 'Land': 'das', 'Heimatland': 'das', 'Stadt': 'die', 'Dorf': 'das', 'Adresse': 'die', 'Straße': 'die', 'E-Mail': 'das', 'Hobby': 'das', 'Heimat': 'die', 'Ausland': 'das', 'Schweiz': 'die', 'Europa': None}
vocab = []
for lemma, wid in A102.items():
    en, tl = V[lemma]
    v = {'id': wid, 'lemma': lemma, 'en': en, 'tl': tl}
    if ART.get(lemma):
        v['article'] = ART[lemma]
    vocab.append(v)

C = lambda phrase, de_, en, tl, audio=None: {'phrase': phrase, 'note': L(de_, en, tl), **({'audioText': audio} if audio else {})}
PIC = LOOK()
lessons = []


def lesson(n, title, introduces, cards, items):
    lid = f'{CH}-L{n:02d}'
    for k, it in enumerate(items, 1):
        it['id'] = f'{lid}-I{k}'
    assert any('image' in i for i in items), lid
    lessons.append({'id': lid, 'title': title, 'introduces': [r for r in R(*introduces) if r not in NO_CARD], 'cards': cards, 'items': items})


X = ''
WHO = lambda: img('herkunft', 'Drei Personen mit Namensschild und Flagge.', 'Three people with name tags and flags.', 'Tatlong tao na may name tag at bandila.')

# L01 ------------------------------------------------------------------ origin
lesson(1, L('Woher kommen Sie?', 'Where are you from?', 'Taga-saan ka?'), ['aus', 'Land', 'Heimat', 'Heimatland'], [
    C('Woher kommen Sie? – Ich komme aus Österreich.', '„aus“ + Land: Ich komme aus Österreich, aus Deutschland.', '“aus” + country: Ich komme aus Österreich (I come from Austria).', '“aus” + bansa: Ich komme aus Österreich (galing ako sa Austria).'),
    C('Ich komme aus den Philippinen.', 'Mit Artikel: aus den Philippinen, aus der Schweiz. Ohne Artikel: aus Österreich.', 'With an article: aus den Philippinen, aus der Schweiz. Without: aus Österreich.', 'May article: aus den Philippinen, aus der Schweiz. Wala: aus Österreich.'),
    C('Woher kommst du? – Aus Manila.', 'Mit „du“: Woher kommst du? Kurze Antwort: „Aus Manila.“', 'With “du”: Woher kommst du? Short answer: “Aus Manila.”', 'Sa “du”: Woher kommst du? Maikling sagot: “Aus Manila.”'),
    C('das Land – das Heimatland – die Heimat', 'Das Heimatland von Jose sind die Philippinen. Seine Heimat ist Manila.', 'Jose’s home country is the Philippines. His home (Heimat) is Manila.', 'Ang sariling bansa ni Jose ay Pilipinas. Ang Heimat niya ay Manila.'),
], [
    choice(X, 'lesen', PIC, 'Woher kommt Jose?', 'aus den Philippinen', ['aus Österreich', 'aus Deutschland'], L('Über Jose steht „Philippinen“, er hat die Flagge der Philippinen.', 'Above Jose it says “Philippinen” and he has the flag of the Philippines.', 'Nakasulat ang “Philippinen” sa itaas ni Jose at may bandila siya ng Pilipinas.'), [G1], R('aus', 'woher'), img=WHO()),
    choice(X, 'hoeren', LISTEN, None, 'Deutschland', ['Österreich'], L('Sie hören: „Ich komme aus Deutschland.“', 'You hear: “Ich komme aus Deutschland.”', 'Naririnig mo: “Ich komme aus Deutschland.”'), [G1], R('aus', 'Deutschland'), audio='Ich komme aus Deutschland.'),
    cloze(X, 'grammatikWortschatz', GAPS, 'Woher kommen Sie? – Ich komme {{1}} Österreich.', [['aus']], L('Herkunft: „aus“ + Land.', 'Origin: “aus” + country.', 'Pinagmulan: “aus” + bansa.'), [G1], R('aus')),
    choice(X, 'sprechen', SAY, 'Woher kommen Sie?', 'Ich komme aus den Philippinen.', ['Ich wohne Philippinen.', 'Ich bin aus Philippinen kommen.'], L('„Ich komme aus …“ – bei den Philippinen mit „den“.', '“Ich komme aus …” – with “den” for the Philippines.', '“Ich komme aus …” – may “den” para sa Pilipinas.'), [G1], R('aus', 'kommen')),
])

# L02 ------------------------------------------------------------------ countries and people
lesson(2, L('Länder und Menschen', 'Countries and people', 'Mga bansa at tao'), ['Österreicher, Österreicherin', 'österreichisch', 'Deutschland', 'Schweiz', 'Philippiner, Philippinerin', 'Europa', 'Mensch', 'Ausländer, Ausländerin', 'Ausland', 'ausländisch'], [
    C('der Österreicher – die Österreicherin', 'Mann: Österreicher. Frau: Österreicherin (mit -in).', 'Man: Österreicher. Woman: Österreicherin (with -in).', 'Lalaki: Österreicher. Babae: Österreicherin (may -in).'),
    C('der Philippiner – die Philippinerin', 'Jose ist Philippiner. Maria ist Philippinerin.', 'Jose is Filipino. Maria is Filipina.', 'Pilipino si Jose. Pilipina si Maria.'),
    C('Österreich, Deutschland, die Schweiz', 'Drei Länder in Europa. Man sagt „die Schweiz“ – mit Artikel.', 'Three countries in Europe. You say “die Schweiz” – with an article.', 'Tatlong bansa sa Europa. Sinasabi “die Schweiz” – may article.'),
    C('der Mensch – die Menschen', 'Mensch = Person, Mann oder Frau.', 'Mensch = person, man or woman.', 'Mensch = tao, lalaki o babae.'),
    C('der Ausländer – die Ausländerin', 'Eine Person aus einem anderen Land. das Ausland = andere Länder.', 'A person from another country. das Ausland = abroad.', 'Taong galing sa ibang bansa. das Ausland = ibang bansa.'),
], [
    choice(X, 'lesen', PIC, 'Welches Land ist nicht auf der Karte?', 'die Philippinen', ['Deutschland', 'die Schweiz'], L('Auf der Karte sind Deutschland, Österreich und die Schweiz.', 'The map shows Germany, Austria and Switzerland.', 'Nasa mapa ang Germany, Austria at Switzerland.'), [G1], R('Deutschland', 'Schweiz'),
           img=img('karte', 'Eine Karte mit Deutschland, Österreich und der Schweiz. Ein Punkt zeigt eine Stadt.', 'A map with Germany, Austria and Switzerland. A dot marks a city.', 'Mapa na may Germany, Austria at Switzerland. May tuldok para sa isang lungsod.')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Anna kommt aus Österreich. Sie ist …', 'Österreicherin', ['Österreicher', 'Philippinerin'], L('Anna ist eine Frau: Österreicherin, mit -in.', 'Anna is a woman: Österreicherin, with -in.', 'Babae si Anna: Österreicherin, may -in.'), [G1], R('Österreicher, Österreicherin')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Jose kommt aus den Philippinen. Er ist …', 'Philippiner', ['Philippinerin', 'Österreicher'], L('Jose ist ein Mann: Philippiner.', 'Jose is a man: Philippiner.', 'Lalaki si Jose: Philippiner.'), [G1], R('Philippiner, Philippinerin')),
    choice(X, 'lesen', READ, 'Österreich, Deutschland und die Schweiz sind in …', 'Europa', ['den Philippinen', 'Wien'], L('Die drei Länder sind in Europa.', 'The three countries are in Europe.', 'Nasa Europa ang tatlong bansa.'), [G1], R('Europa')),
    choice(X, 'hoeren', LISTEN, None, 'Er ist Österreicher.', ['Er ist Philippiner.'], L('Sie hören: „Lukas kommt aus Graz. Er ist Österreicher.“', 'You hear: “Lukas kommt aus Graz. Er ist Österreicher.”', 'Naririnig mo: “Lukas kommt aus Graz. Er ist Österreicher.”'), [G1], R('Österreicher, Österreicherin'), audio='Lukas kommt aus Graz. Er ist Österreicher.'),
])

# L03 ------------------------------------------------------------------ where you live
lesson(3, L('Wo wohnen Sie?', 'Where do you live?', 'Saan ka nakatira?'), ['wohnen', 'wo', 'in', 'Stadt', 'Dorf', 'hier', 'dort', 'da'], [
    C('Wo wohnen Sie? – Ich wohne in Graz.', '„wo“ fragt nach dem Ort. Antwort mit „in“ + Ort.', '“wo” asks for the place. Answer with “in” + place.', 'Ang “wo” ay tanong sa lugar. Sagot: “in” + lugar.'),
    C('ich wohne, du wohnst, er wohnt', 'wir wohnen, ihr wohnt, sie/Sie wohnen – regelmäßig.', 'wir wohnen, ihr wohnt, sie/Sie wohnen – regular.', 'wir wohnen, ihr wohnt, sie/Sie wohnen – regular.'),
    C('Woher? – Wo?', 'Woher? = Herkunft (aus …). Wo? = Ort jetzt (in …).', 'Woher? = origin (aus …). Wo? = place now (in …).', 'Woher? = pinagmulan (aus …). Wo? = lugar ngayon (in …).'),
    C('die Stadt – das Dorf', 'Graz ist eine Stadt. St. Georgen ist ein Dorf.', 'Graz is a town/city (Stadt). St. Georgen is a village (Dorf).', 'Lungsod (Stadt) ang Graz. Baryo (Dorf) ang St. Georgen.'),
    C('der Wohnort', 'Der Wohnort ist die Stadt oder das Dorf, wo man wohnt.', 'Wohnort = the town or village where you live.', 'Wohnort = lungsod o baryo kung saan ka nakatira.'),
    C('hier – da – dort', 'hier/da = nah bei mir. dort = weit weg.', 'hier/da = near me. dort = over there.', 'hier/da = malapit sa akin. dort = doon.'),
], [
    choice(X, 'lesen', PIC, 'Wo wohnt Lukas?', 'in St. Georgen', ['in Graz', 'in Wien'], L('Lukas steht beim Dorf St. Georgen. Maria steht in Graz.', 'Lukas stands by the village of St. Georgen. Maria stands in Graz.', 'Nasa baryo ng St. Georgen si Lukas. Nasa Graz si Maria.'), [G2], R('wo', 'wohnen', 'in'),
           img=img('wohnort', 'Links eine Stadt mit Maria, rechts ein Dorf mit Lukas.', 'A town with Maria on the left, a village with Lukas on the right.', 'Lungsod na may Maria sa kaliwa, baryo na may Lukas sa kanan.')),
    cloze(X, 'grammatikWortschatz', GAPS, '{{1}} wohnen Sie? – In Linz. · {{2}} kommen Sie? – Aus Manila.', [['Wo'], ['Woher']], L('Wo = Ort (in …), Woher = Herkunft (aus …).', 'Wo = place (in …), Woher = origin (aus …).', 'Wo = lugar (in …), Woher = pinagmulan (aus …).'), [G2, G1], R('wo', 'woher')),
    cloze(X, 'grammatikWortschatz', GAPS, 'Ich {{1}} (wohnen) in Wien. Du {{2}} (wohnen) in Salzburg.', [['wohne'], ['wohnst']], L('ich wohne, du wohnst.', 'ich wohne (I live), du wohnst (you live).', 'ich wohne (nakatira ako), du wohnst (nakatira ka).'), [G7], R('wohnen')),
    choice(X, 'hoeren', L('Hören Sie. Wo wohnt die Frau?', 'Listen. Where does the woman live?', 'Makinig. Saan nakatira ang babae?'), None, 'in Linz', ['in Graz'], L('Sie hören: „Ich wohne in Linz.“', 'You hear: “Ich wohne in Linz.”', 'Naririnig mo: “Ich wohne in Linz.”'), [G2], R('wohnen'), audio='Grüß Gott! Ich wohne in Linz.'),
])

# L04 ------------------------------------------------------------------ address and e-mail
ADR = lambda: img('adresse', 'Ein Brief mit Name und Adresse und eine Karte mit einer E-Mail-Adresse.', 'An envelope with a name and address and a card with an e-mail address.', 'Sobre na may pangalan at address, at card na may e-mail address.')
lesson(4, L('Adresse und E-Mail', 'Address and e-mail', 'Address at e-mail'), ['Adresse', 'Straße', 'E-Mail'], [
    C('die Adresse: Hauptstraße 12, 8010 Graz', 'In Österreich: zuerst Straße und Hausnummer, dann Postleitzahl und Stadt.', 'In Austria: street and house number first, then postcode and town.', 'Sa Austria: una ang kalye at numero ng bahay, tapos postal code at lungsod.', 'die Adresse: Hauptstraße zwölf, acht, null, eins, null, Graz'),
    C('die Straße – die Hauptstraße', '„Straße“ mit ß. Straßennamen schreibt man zusammen: Hauptstraße.', '“Straße” with ß. Street names are written as one word: Hauptstraße.', '“Straße” may ß. Isang salita ang pangalan ng kalye: Hauptstraße.'),
    C('das E-Mail', 'In Österreich sagt man oft „das E-Mail“. (in Deutschland: „die E-Mail“)', 'In Austria people often say “das E-Mail” (in Germany: “die E-Mail”).', 'Sa Austria, madalas “das E-Mail” (sa Germany: “die E-Mail”).'),
    C('die E-Mail-Adresse', 'Das E-Mail ist die Nachricht. Die Adresse dafür heißt „die E-Mail-Adresse“.', 'das E-Mail is the message; the address is “die E-Mail-Adresse”.', 'Ang das E-Mail ay mensahe; ang address ay “die E-Mail-Adresse”.'),
    C('die E-Mail-Adresse: maria.santos@gmx.at', '@ sagt man „ät“, der Punkt heißt „Punkt“: maria Punkt santos ät gmx Punkt at.', 'You say @ as “ät” and . as “Punkt”: maria Punkt santos ät gmx Punkt at.', 'Ang @ ay “ät” at ang . ay “Punkt”.', 'maria Punkt santos ät g m x Punkt a t'),
], [
    choice(X, 'lesen', PIC, 'Wie heißt die Straße?', 'Hauptstraße', ['Graz', 'Santos'], L('Auf dem Brief steht: Hauptstraße 12.', 'The envelope says: Hauptstraße 12.', 'Nakasulat sa sobre: Hauptstraße 12.'), [G2], R('Straße'), img=ADR()),
    choice(X, 'lesen', PIC, 'Maria wohnt in …', 'Graz', ['Wien', 'Linz'], L('Auf dem Brief steht: 8010 Graz.', 'The envelope says: 8010 Graz.', 'Nakasulat sa sobre: 8010 Graz.'), [G2], R('wohnen', 'Adresse'), img=ADR()),
    choice(X, 'hoeren', L('Hören Sie. Wie ist die E-Mail-Adresse?', 'Listen. What is the e-mail address?', 'Makinig. Ano ang e-mail address?'), None, 'anna.huber@gmx.at', ['annahuber@gmx.at', 'anna.huber@gmx.de'], L('Sie hören: anna Punkt huber ät g m x Punkt a t.', 'You hear: anna Punkt huber ät g m x Punkt a t.', 'Naririnig mo: anna Punkt huber ät g m x Punkt a t.'), [G2], R('E-Mail'), audio='Die E-Mail-Adresse ist: anna Punkt huber ät g m x Punkt a t.'),
    cloze(X, 'schreiben', L('Lesen Sie und ergänzen Sie das Formular.', 'Read and complete the form.', 'Basahin at kumpletuhin ang form.'), 'Ich heiße Ali Novak. Ich wohne in der Bergstraße 5 in Linz.\nStraße: {{1}} · Stadt: {{2}}', [['Bergstraße 5', 'Bergstrasse 5', 'Bergstraße'], ['Linz']], L('Straße = Bergstraße 5, Stadt = Linz.', 'Street = Bergstraße 5, town = Linz.', 'Kalye = Bergstraße 5, lungsod = Linz.'), [G2], R('Straße', 'Stadt')),
])

# L05 ------------------------------------------------------------------ languages
lesson(5, L('Welche Sprachen sprechen Sie?', 'Which languages do you speak?', 'Anong mga wika ang alam mo?'), ['sprechen', 'Sprache', 'Deutsch', 'Englisch', 'Tagalog'], [
    C('Ich spreche Deutsch und Englisch.', 'Sprachen schreibt man groß: Deutsch, Englisch, Tagalog.', 'Languages start with a capital letter: Deutsch, Englisch, Tagalog.', 'Malaking titik ang simula ng wika: Deutsch, Englisch, Tagalog.'),
    C('ich spreche – du sprichst – er spricht', '„sprechen“ wechselt den Vokal: e → i bei du und er/sie/es.', '“sprechen” changes its vowel: e → i with du and er/sie/es.', 'Nagbabago ang vowel ng “sprechen”: e → i sa du at er/sie/es.'),
    C('Welche Sprachen sprechen Sie?', 'die Sprache – die Sprachen (Plural).', 'one language: die Sprache – several: die Sprachen.', 'isang wika: die Sprache – marami: die Sprachen.'),
    C('Sprechen Sie Deutsch? – Ja, ein bisschen.', 'Eine Ja/Nein-Frage beginnt mit dem Verb.', 'A yes/no question starts with the verb.', 'Nagsisimula sa verb ang tanong na oo/hindi.'),
], [
    choice(X, 'lesen', PIC, 'Welche Sprache spricht Jose?', 'Tagalog', ['Deutsch', 'Englisch'], L('Jose sagt „Kumusta!“ – das ist Tagalog. Anna sagt „Grüß Gott!“ (Deutsch), Tom „Hello!“ (Englisch).', 'Jose says “Kumusta!” – that is Tagalog. Anna says “Grüß Gott!” (German), Tom “Hello!” (English).', '“Kumusta!” ang sabi ni Jose – Tagalog iyan. “Grüß Gott!” si Anna (German), “Hello!” si Tom (English).'), [G3], R('Sprache', 'Tagalog'),
           img=img('sprachen', 'Drei Personen begrüßen in verschiedenen Sprachen.', 'Three people greet in different languages.', 'Tatlong tao na bumabati sa iba’t ibang wika.')),
    cloze(X, 'grammatikWortschatz', GAPS, 'Du {{1}} (sprechen) Englisch. Maria {{2}} (sprechen) Tagalog.', [['sprichst'], ['spricht']], L('du sprichst, sie spricht – e wird i.', 'du sprichst, sie spricht – e becomes i.', 'du sprichst, sie spricht – nagiging i ang e.'), [G3, G7], R('sprechen')),
    choice(X, 'hoeren', L('Hören Sie. Welche Sprachen spricht der Mann?', 'Listen. Which languages does the man speak?', 'Makinig. Anong mga wika ang alam ng lalaki?'), None, 'Englisch und Deutsch', ['Tagalog und Deutsch'], L('Sie hören: „Ich spreche Englisch und Deutsch.“', 'You hear: “Ich spreche Englisch und Deutsch.”', 'Naririnig mo: “Ich spreche Englisch und Deutsch.”'), [G3], R('sprechen', 'Englisch'), audio='Ich spreche Englisch und Deutsch.'),
    choice(X, 'sprechen', SAY, 'Welche Sprachen sprechen Sie?', 'Ich spreche Tagalog und Englisch.', ['Ich sprecht Tagalog.', 'Ich bin Tagalog.'], L('ich spreche – mit -e.', 'ich spreche – with -e.', 'ich spreche – may -e.'), [G3], R('sprechen')),
])

# L06 ------------------------------------------------------------------ not understanding
lesson(6, L('Ich verstehe nicht.', 'I don’t understand.', 'Hindi ko naiintindihan.'), ['verstehen', 'wiederholen', 'langsam'], [
    C('Ich verstehe nicht.', '„verstehen“: ich verstehe, du verstehst. Das dürfen Sie immer sagen!', '“verstehen” (understand): ich verstehe, du verstehst. You may always say it!', '“verstehen”: ich verstehe, du verstehst. Puwede mo itong sabihin palagi!'),
    C('Langsam, bitte!', 'Die Person spricht zu schnell? Sagen Sie: „Langsam, bitte!“', 'The person talks too fast? Say: “Langsam, bitte!” (slowly, please)', 'Masyadong mabilis? Sabihin: “Langsam, bitte!” (dahan-dahan, please)'),
    C('Wiederholen Sie, bitte.', 'Höflich: „Wiederholen Sie, bitte.“ Mit du: „Wiederhol bitte.“', 'Polite: “Wiederholen Sie, bitte.” With du: “Wiederhol bitte.”', 'Magalang: “Wiederholen Sie, bitte.” Sa du: “Wiederhol bitte.”'),
    C('Wie bitte? – Noch einmal, bitte.', 'Auch das kennen Sie schon aus Kapitel 2.', 'You already know these from chapter 2.', 'Alam mo na ito mula sa kabanata 2.'),
], [
    choice(X, 'sprechen', PIC, 'Was sagt Ali?', 'Langsam, bitte!', ['Auf Wiederhören!', 'Ich komme aus Graz.'], L('Der Mann spricht sehr schnell. Ali versteht nicht und sagt: „Langsam, bitte!“', 'The man talks very fast. Ali doesn’t understand and says: “Langsam, bitte!”', 'Mabilis magsalita ang lalaki. Hindi naiintindihan ni Ali: “Langsam, bitte!”'), [G4], R('langsam', 'verstehen'),
           img=img('langsam', 'Ein Mann spricht sehr schnell. Ali hat ein Fragezeichen.', 'A man talks very fast. Ali has a question mark.', 'Mabilis magsalita ang lalaki. May tandang pananong si Ali.')),
    cloze(X, 'grammatikWortschatz', GAPS, 'Entschuldigung, ich {{1}} nicht. {{2}} Sie, bitte.', [['verstehe'], ['Wiederholen']], L('ich verstehe; höflich: Wiederholen Sie, bitte.', 'ich verstehe; polite: Wiederholen Sie, bitte.', 'ich verstehe; magalang: Wiederholen Sie, bitte.'), [G4], R('verstehen', 'wiederholen')),
    choice(X, 'sprechen', L('Die Frau spricht sehr schnell. Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'The woman talks very fast. What do you say? Choose, then say it aloud.', 'Mabilis magsalita ang babae. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'), None, 'Sprechen Sie bitte langsam.', ['Sprechen Sie bitte Englisch?', 'Ich spreche langsam.'], L('Bitte um langsames Sprechen: „Sprechen Sie bitte langsam.“', 'Asking to speak slowly: “Sprechen Sie bitte langsam.”', 'Paghiling na bagalan: “Sprechen Sie bitte langsam.”'), [G4], R('langsam', 'sprechen')),
    choice(X, 'hoeren', L('Hören Sie. Was möchte die Person?', 'Listen. What does the person want?', 'Makinig. Ano ang gusto ng tao?'), None, 'Noch einmal, bitte.', ['Auf Wiederhören!'], L('„Wiederholen Sie, bitte“ heißt: „Noch einmal, bitte.“', '“Wiederholen Sie, bitte” means: “Noch einmal, bitte.” (again, please)', '“Wiederholen Sie, bitte” = “Noch einmal, bitte.” (ulit, please)'), [G4], R('wiederholen'), audio='Wie bitte? Ich verstehe nicht. Wiederholen Sie, bitte.'),
])

# L07 ------------------------------------------------------------------ yes/no questions
ANNA = lambda: img('anna', 'Anna steht neben der Flagge von Österreich und einem Schild „Wien“.', 'Anna next to the Austrian flag and a sign “Wien”.', 'Si Anna sa tabi ng bandila ng Austria at karatulang “Wien”.')
lesson(7, L('Ja oder nein? – Fragen mit dem Verb zuerst', 'Yes or no? – questions with the verb first', 'Oo o hindi? – tanong na una ang verb'), [], [
    C('Kommen Sie aus Österreich?', 'Ja/Nein-Frage: Das Verb steht auf Platz 1.', 'Yes/no question: the verb is in position 1.', 'Tanong na oo/hindi: nasa unang puwesto ang verb.'),
    C('Wohnst du in Wien? – Ja. / Nein, in Graz.', 'Antwort mit „ja“ oder „nein“.', 'Answer with “ja” or “nein”.', 'Sagot: “ja” o “nein”.'),
    C('Wortkarte: Wohnort? → Wo wohnen Sie?', 'In der Prüfung (Sprechen Teil 2) bekommen Sie eine Wortkarte und stellen eine Frage dazu.', 'In the exam (speaking part 2) you get a word card and ask a question about it.', 'Sa exam (speaking part 2), may word card ka at magtatanong ka tungkol dito.'),
    C('Sie kommen aus Wien. → Kommen Sie aus Wien?', 'Aussage: Verb auf Platz 2. Frage: Verb auf Platz 1.', 'Statement: verb in position 2. Question: verb in position 1.', 'Pahayag: verb sa puwesto 2. Tanong: verb sa puwesto 1.'),
], [
    choice(X, 'lesen', PIC, 'Kommt Anna aus Österreich?', 'Ja, sie kommt aus Österreich.', ['Nein, sie kommt aus Deutschland.', 'Nein, sie kommt aus den Philippinen.'], L('Anna hat die Flagge von Österreich.', 'Anna has the Austrian flag.', 'May bandila ng Austria si Anna.'), [G5], R('ja', 'kommen'), img=ANNA()),
    choice(X, 'lesen', PIC, 'Wohnt Anna in Graz?', 'Nein, sie wohnt in Wien.', ['Ja, sie wohnt in Graz.', 'Ja, sie wohnt in Wien.'], L('Auf dem Schild steht Wien – nicht Graz. Also: „Nein, …“', 'The sign says Wien – not Graz. So: “Nein, …”', 'Wien ang nakasulat – hindi Graz. Kaya: “Nein, …”'), [G5], R('nein', 'wohnen'), img=ANNA()),
    choice(X, 'grammatikWortschatz', L('Welche Frage ist richtig?', 'Which question is correct?', 'Aling tanong ang tama?'), None, 'Sprechen Sie Englisch?', ['Sie Englisch sprechen?', 'Englisch Sie sprechen?'], L('Ja/Nein-Frage: Verb zuerst.', 'Yes/no question: verb first.', 'Tanong na oo/hindi: una ang verb.'), [G5], R('sprechen')),
    cloze(X, 'grammatikWortschatz', GAPS, '{{1}} du in Linz? – Ja, ich wohne in Linz.', [['Wohnst']], L('Verb auf Platz 1: Wohnst du …?', 'Verb in position 1: Wohnst du …?', 'Verb sa puwesto 1: Wohnst du …?'), [G5, G7], R('wohnen')),
])

# L08 ------------------------------------------------------------------ doch
lesson(8, L('Ja, nein – doch!', 'Yes, no – doch!', 'Oo, hindi – doch!'), ['doch'], [
    C('Sprechen Sie Deutsch? – Ja.', 'Normale Frage → ja oder nein.', 'Normal question → ja or nein.', 'Normal na tanong → ja o nein.'),
    C('Wohnen Sie nicht in Wien? – Doch!', 'Frage mit „nicht“, aber die Antwort ist positiv → „doch“.', 'Question with “nicht” (not), but the answer is positive → “doch”.', 'Tanong na may “nicht” (hindi), pero positibo ang sagot → “doch”.'),
    C('Kommst du nicht aus Wien? – Doch, aus Wien.', '„Doch“ sagt: Doch, das stimmt!', '“Doch” says: yes, it is true!', '“Doch” = oo, totoo iyan!'),
], [
    choice(X, 'lesen', PIC, 'Wohnt Jose nicht in Wien?', 'Doch, er wohnt in Wien.', ['Nein, er wohnt nicht in Wien.', 'Ja, er wohnt nicht in Wien.'], L('Jose sagt: „Ich wohne in Wien.“ Die Frage hat „nicht“ → „Doch!“', 'Jose says: “Ich wohne in Wien.” The question has “nicht” → “Doch!”', 'Sabi ni Jose: “Ich wohne in Wien.” May “nicht” ang tanong → “Doch!”'), [G5], R('doch', 'wohnen'),
           img=img('jose', 'Jose sagt etwas in einer Sprechblase. Daneben ein Schild mit einer Stadt.', 'Jose says something in a speech bubble. A sign with a city next to it.', 'May sinasabi si Jose sa speech bubble. May karatula ng lungsod.')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Kommen Sie nicht aus Graz? – … , ich komme aus Graz.', 'Doch', ['Ja', 'Nein'], L('Frage mit „nicht“ + positive Antwort = „Doch“.', 'Question with “nicht” + positive answer = “Doch”.', 'Tanong na may “nicht” + positibong sagot = “Doch”.'), [G5], R('doch')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Wohnen Sie in Wien? – … , ich wohne in Wien.', 'Ja', ['Doch', 'Nein'], L('Normale Frage (ohne „nicht“) → „Ja“.', 'Normal question (without “nicht”) → “Ja”.', 'Normal na tanong (walang “nicht”) → “Ja”.'), [G5], R('ja')),
    choice(X, 'hoeren', LISTEN, None, 'Die Frau wohnt in Graz.', ['Die Frau wohnt nicht in Graz.'], L('Sie hören: „Wohnen Sie nicht in Graz?“ – „Doch!“ Also wohnt sie in Graz.', 'You hear: “Wohnen Sie nicht in Graz?” – “Doch!” So she lives in Graz.', 'Naririnig mo: “Wohnen Sie nicht in Graz?” – “Doch!” Kaya nakatira siya sa Graz.'), [G5], R('doch'), audio='Wohnen Sie nicht in Graz? – Doch!'),
])

# L09 ------------------------------------------------------------------ der, die, das
NOMEN = lambda: img('nomen', 'Drei Bilder mit Nummern: 1 ein Land, 2 ein Straßenschild, 3 ein Mensch.', 'Three numbered pictures: 1 a country, 2 a street sign, 3 a person.', 'Tatlong larawang may numero: 1 bansa, 2 karatula ng kalye, 3 tao.')
lesson(9, L('der, die, das', 'der, die, das – the articles', 'der, die, das – mga article'), ['der', 'die', 'das'], [
    C('der Mensch · die Stadt · das Land', 'Jedes Nomen hat einen Artikel: der, die oder das. Den Artikel immer mitlernen!', 'Every noun has an article: der, die or das. Always learn the article with it!', 'May article ang bawat noun: der, die o das. Laging isaulo kasama ang article!'),
    C('die Straße · die Sprache · die Adresse', 'Viele Nomen auf -e haben „die“.', 'Many nouns ending in -e take “die”.', 'Maraming noun na nagtatapos sa -e ay “die”.'),
    C('das Dorf · das E-Mail · das Hobby', 'In Österreich: das E-Mail. (in Deutschland: die E-Mail)', 'In Austria: das E-Mail (in Germany: die E-Mail).', 'Sa Austria: das E-Mail (sa Germany: die E-Mail).'),
    C('Nomen schreibt man groß.', 'die Stadt, das Land – immer mit großem Buchstaben.', 'die Stadt, das Land – always with a capital letter.', 'die Stadt, das Land – laging malaking titik.'),
], [
    choice(X, 'grammatikWortschatz', PIC, 'Bild 1: Was ist das?', 'das Land', ['die Land', 'die Stadt'], L('Bild 1 zeigt Österreich – ein Land: das Land.', 'Picture 1 shows Austria – a country: das Land.', 'Larawan 1: Austria – isang bansa: das Land.'), [G6], R('das', 'Land'), img=NOMEN()),
    choice(X, 'grammatikWortschatz', PIC, 'Bild 2: Was ist das?', 'die Straße', ['das Straße', 'der Mensch'], L('Bild 2 zeigt ein Straßenschild: die Straße.', 'Picture 2 shows a street sign: die Straße.', 'Larawan 2: karatula ng kalye: die Straße.'), [G6], R('die', 'Straße'), img=NOMEN()),
    choice(X, 'grammatikWortschatz', PIC, 'Bild 3: Was ist das?', 'der Mensch', ['das Mensch', 'das Land'], L('Bild 3 zeigt eine Person: der Mensch.', 'Picture 3 shows a person: der Mensch.', 'Larawan 3: isang tao: der Mensch.'), [G6], R('der', 'Mensch'), img=NOMEN()),
    cloze(X, 'grammatikWortschatz', GAPS, '{{1}} Stadt · {{2}} Dorf · {{3}} Sprache', [['die'], ['das'], ['die']], L('die Stadt, das Dorf, die Sprache.', 'die Stadt (town), das Dorf (village), die Sprache (language).', 'die Stadt (lungsod), das Dorf (baryo), die Sprache (wika).'), [G6], R('Stadt', 'Dorf', 'Sprache')),
])

# L10 ------------------------------------------------------------------ ein, eine
lesson(10, L('ein, eine', 'ein, eine (a, an)', 'ein, eine (isang)'), ['ein'], [
    C('der Mensch → ein Mensch', 'der und das → ein.', 'der and das → ein.', 'der at das → ein.'),
    C('das Dorf → ein Dorf', 'Moosbach ist ein Dorf.', 'Moosbach is a village (ein Dorf).', 'Baryo (ein Dorf) ang Moosbach.'),
    C('die Stadt → eine Stadt', 'die → eine. Graz ist eine Stadt.', 'die → eine. Graz is a city (eine Stadt).', 'die → eine. Lungsod (eine Stadt) ang Graz.'),
    C('ein / eine – der / die / das', '„ein/eine“: neu, nicht bekannt. „der/die/das“: bekannt.', '“ein/eine”: new, not known yet. “der/die/das”: already known.', '“ein/eine”: bago, hindi pa kilala. “der/die/das”: kilala na.'),
], [
    choice(X, 'grammatikWortschatz', PIC, 'Moosbach ist …', 'ein Dorf', ['eine Stadt', 'ein Land'], L('Man sieht nur drei Häuser: Moosbach ist ein Dorf. das Dorf → ein Dorf.', 'There are only three houses: Moosbach is a village. das Dorf → ein Dorf.', 'Tatlong bahay lang: baryo ang Moosbach. das Dorf → ein Dorf.'), [G6, G2], R('ein', 'Dorf'),
           img=img('moosbach', 'Ein weißes Ortsschild und ein paar Häuser.', 'A white town sign and a few houses.', 'Puting karatula ng bayan at ilang bahay.')),
    cloze(X, 'grammatikWortschatz', GAPS, 'Graz ist {{1}} Stadt. Österreich ist {{2}} Land.', [['eine'], ['ein']], L('die Stadt → eine Stadt; das Land → ein Land.', 'die Stadt → eine Stadt (a town); das Land → ein Land (a country).', 'die Stadt → eine Stadt (isang lungsod); das Land → ein Land (isang bansa).'), [G6], R('ein', 'Stadt', 'Land')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Deutsch ist … Sprache.', 'eine', ['ein', 'der'], L('die Sprache → eine Sprache.', 'die Sprache → eine Sprache (a language).', 'die Sprache → eine Sprache (isang wika).'), [G6], R('ein', 'Sprache')),
    choice(X, 'lesen', READ, 'Wien ist eine Stadt. Moosbach ist ein Dorf. Was ist Wien?', 'eine Stadt', ['ein Dorf', 'ein Land'], L('Im Text steht: „Wien ist eine Stadt.“', 'The text says: “Wien ist eine Stadt.”', 'Sabi sa teksto: “Wien ist eine Stadt.”'), [G6], R('Dorf')),
])

# L11 ------------------------------------------------------------------ suchen, finden, geben, nehmen
lesson(11, L('suchen, finden, geben, nehmen', 'look for, find, give, take', 'maghanap, makahanap, magbigay, kumuha'), ['suchen', 'finden', 'geben', 'nehmen'], [
    C('Ich suche die Bahnhofstraße.', '„suchen“: ich suche, du suchst, er sucht.', '“suchen” (look for): ich suche, du suchst, er sucht.', '“suchen” (maghanap): ich suche, du suchst, er sucht.'),
    C('Ich finde die Adresse nicht.', '„finden“: ich finde, du findest, er findet.', '“finden” (find): ich finde, du findest, er findet.', '“finden” (mahanap): ich finde, du findest, er findet.'),
    C('Geben Sie mir bitte die Adresse.', '„geben“: ich gebe, du gibst, er gibt – e wird i.', '“geben” (give): ich gebe, du gibst, er gibt – e becomes i.', '“geben” (magbigay): ich gebe, du gibst, er gibt – nagiging i ang e.'),
    C('Ich nehme das.', '„nehmen“: ich nehme, du nimmst, er nimmt.', '“nehmen” (take): ich nehme, du nimmst, er nimmt.', '“nehmen” (kumuha): ich nehme, du nimmst, er nimmt.'),
], [
    choice(X, 'lesen', PIC, 'Was sucht Maria?', 'die Bahnhofstraße', ['die Hauptstraße', 'Graz'], L('Maria fragt: „Wo ist die Bahnhofstraße?“ Das Schild zeigt die Hauptstraße.', 'Maria asks: “Wo ist die Bahnhofstraße?” The sign shows Hauptstraße.', 'Tanong ni Maria: “Wo ist die Bahnhofstraße?” Hauptstraße ang nasa karatula.'), [G7, G2], R('suchen', 'Straße'),
           img=img('suchen', 'Maria hat eine Karte und fragt. Daneben ein Straßenschild.', 'Maria has a map and asks something. A street sign next to her.', 'May mapa si Maria at nagtatanong. May karatula ng kalye sa tabi.')),
    cloze(X, 'grammatikWortschatz', GAPS, 'Du {{1}} (geben) mir die Adresse. Er {{2}} (nehmen) das.', [['gibst'], ['nimmt']], L('du gibst, er nimmt – e wird i.', 'du gibst, er nimmt – e becomes i.', 'du gibst, er nimmt – nagiging i ang e.'), [G7], R('geben', 'nehmen')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Wo ist die Hauptstraße? Ich … sie nicht.', 'finde', ['nehme', 'gebe'], L('Ich suche und ich finde die Straße nicht.', 'I am looking and I can’t find (finde … nicht) the street.', 'Naghahanap ako at hindi ko mahanap (finde … nicht) ang kalye.'), [G7], R('finden')),
    choice(X, 'hoeren', LISTEN, None, 'Er sucht die Adresse.', ['Er gibt die Adresse.'], L('Sie hören: „Entschuldigung, ich suche die Adresse Bergstraße 5.“', 'You hear: “Entschuldigung, ich suche die Adresse Bergstraße 5.”', 'Naririnig mo: “Entschuldigung, ich suche die Adresse Bergstraße 5.”'), [G7], R('suchen'), audio='Entschuldigung, ich suche die Adresse Bergstraße fünf.'),
])

# L12 ------------------------------------------------------------------ hobby, phone goodbye
ABS = lambda: img('abschied', 'Bild 1: ein Telefon. Bild 2: zwei Personen auf der Straße.', 'Picture 1: a phone. Picture 2: two people in the street.', 'Larawan 1: telepono. Larawan 2: dalawang tao sa kalye.')
lesson(12, L('Hobby und Telefon', 'Hobby and phone', 'Libangan at telepono'), ['Hobby', 'auf Wiederhören'], [
    C('das Hobby – die Hobbys', 'Was ist Ihr Hobby? – Mein Hobby ist Deutsch!', 'What is your hobby? – My hobby is German!', 'Ano ang libangan mo? – German ang libangan ko!'),
    C('Auf Wiederhören!', 'Am Telefon: „Auf Wiederhören!“ – man hört, aber sieht nicht.', 'On the phone: “Auf Wiederhören!” – you hear but don’t see each other.', 'Sa telepono: “Auf Wiederhören!” – naririnig pero hindi nakikita.'),
    C('Auf Wiedersehen!', 'Persönlich: „Auf Wiedersehen!“ – man sieht sich.', 'In person: “Auf Wiedersehen!” – you see each other.', 'Harapan: “Auf Wiedersehen!” – nagkikita kayo.'),
], [
    choice(X, 'sprechen', PIC, 'Bild 1: Was sagen Sie am Ende?', 'Auf Wiederhören!', ['Auf Wiedersehen!', 'Gute Nacht!'], L('Am Telefon: „Auf Wiederhören!“', 'On the phone: “Auf Wiederhören!”', 'Sa telepono: “Auf Wiederhören!”'), [G4], R('auf Wiederhören'), img=ABS()),
    choice(X, 'sprechen', PIC, 'Bild 2: Was sagen Sie am Ende?', 'Auf Wiedersehen!', ['Auf Wiederhören!', 'Wie bitte?'], L('Die Personen sehen sich: „Auf Wiedersehen!“', 'The people see each other: “Auf Wiedersehen!”', 'Nagkikita sila: “Auf Wiedersehen!”'), [G4], R('auf Wiedersehen'), img=ABS()),
    cloze(X, 'grammatikWortschatz', GAPS, 'Mein {{1}} ist Englisch.', [['Hobby']], L('das Hobby – mein Hobby.', 'das Hobby – my hobby (mein Hobby).', 'das Hobby – ang libangan ko (mein Hobby).'), None, R('Hobby')),
    choice(X, 'hoeren', L('Hören Sie. Wo sind die Personen?', 'Listen. Where are the people?', 'Makinig. Nasaan ang mga tao?'), None, 'am Telefon', ['zusammen im Haus'], L('Sie hören: „Gut, danke. Auf Wiederhören!“ – das sagt man am Telefon.', 'You hear: “Gut, danke. Auf Wiederhören!” – that is what you say on the phone.', 'Naririnig mo: “Gut, danke. Auf Wiederhören!” – sinasabi ito sa telepono.'), [G4], R('auf Wiederhören'), audio='Gut, danke. Auf Wiederhören!'),
])

# L13 ------------------------------------------------------------------ Austria basics (A1-WOW-19, A1-WOW-01; Q36)
AT = lambda: img('oesterreich', 'Österreich mit einem Stern für die Hauptstadt, eine Euro-Münze, die Flagge der EU und die Flagge von Österreich.', 'Austria with a star for the capital, a euro coin, the EU flag and the Austrian flag.', 'Austria na may bituin para sa kabisera, euro coin, bandila ng EU at ng Austria.')
WOW = L('Österreich: Hauptstadt Wien, Geld Euro, Staatssprache Deutsch, seit 1995 in der EU.', 'Austria: capital Vienna, money euro, official language German, in the EU since 1995.', 'Austria: kabisera Vienna, pera euro, opisyal na wika German, nasa EU mula 1995.')
lesson(13, L('Österreich kurz', 'Austria in brief', 'Austria sa madaling salita'), [], [
    C('Die Hauptstadt ist Wien.', 'Wien ist die größte Stadt und die Hauptstadt von Österreich.', 'Vienna is the biggest city and the capital of Austria.', 'Ang Vienna ang pinakamalaking lungsod at kabisera ng Austria.'),
    C('Das Geld ist der Euro.', 'In Österreich zahlt man mit Euro und Cent.', 'In Austria you pay with euros and cents.', 'Sa Austria, euro at cent ang pambayad.'),
    C('Die Staatssprache ist Deutsch.', 'Auf dem Amt und in der Schule spricht man Deutsch. Deutsch hilft bei der Arbeit und im Alltag.', 'German is the language of offices and schools. German helps at work and in everyday life.', 'German ang wika ng opisina at paaralan. Nakakatulong ang German sa trabaho at araw-araw.'),
    C('Österreich ist seit 1995 in der EU.', 'EU = Europäische Union.', 'EU = European Union.', 'EU = European Union.'),
], [
    choice(X, 'werte', PIC, 'Was ist nicht im Bild?', 'die Flagge der Schweiz', ['die Flagge der EU'], WOW, [G8], R('Österreich'), img=AT()),
    choice(X, 'werte', CHOOSE, 'Das Geld in Österreich ist …', 'der Euro', ['der Dollar'], WOW, [G8], R('Euro')),
    choice(X, 'werte', CHOOSE, 'Die Staatssprache in Österreich ist …', 'Deutsch', ['Englisch'], WOW, [G8], R('Deutsch', 'Sprache')),
    choice(X, 'werte', CHOOSE, 'Österreich ist in der EU seit …', '1995', ['2015'], WOW, [G8], R('Europa')),
])

introduced = {r for l in lessons for r in l['introduces']}
print('not introduced:', [v['lemma'] for v in vocab if v['id'] not in introduced and v['id'] not in NO_CARD])
json.dump({'schemaVersion': 1, 'chapterId': CH, 'tlReviewStatus': 'machine', 'vocab': vocab, 'lessons': lessons}, open(f'{ROOT}/src/lib/content/a1-03.json', 'w'), ensure_ascii=False, indent='\t')
print(len(lessons), 'lessons', sum(len(l['items']) for l in lessons), 'items')
