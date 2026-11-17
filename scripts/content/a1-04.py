# A1-04 "Meine Familie" – lessons, pools, pictures. Run: python3 scripts/content/a1-04.py
import lib
lib.init('A1-04', seed=20261119, sources=['Q36'])
from lib import *  # noqa: E402,F403

GOALS = {
    'A1-04-G1': L('Familienmitglieder nennen', 'Naming family members', 'Pangalanan ang mga miyembro ng pamilya'),
    'A1-04-G2': L('Über die eigene Familie sprechen (mein, meine, dein, Ihr)', 'Talking about your family (mein, meine, dein, Ihr)', 'Pag-usapan ang pamilya (mein, meine, dein, Ihr)'),
    'A1-04-G3': L('Familienstand: verheiratet, ledig, geschieden', 'Marital status: married, single, divorced', 'Civil status: kasal, walang asawa, hiwalay'),
    'A1-04-G4': L('Plural der Nomen', 'Plural of nouns', 'Plural ng noun'),
    'A1-04-G5': L('Verben: sehen, hören, lesen, schreiben, leben, bleiben, lieben, heiraten', 'Verbs: see, hear, read, write, live, stay, love, marry', 'Verbs: makita, marinig, magbasa, sumulat, mabuhay, manatili, magmahal, magpakasal'),
    'A1-04-G6': L('Familienformen in Österreich', 'Family forms in Austria', 'Mga anyo ng pamilya sa Austria'),
}
G1, G2, G3, G4, G5, G6 = GOALS

V = {
    'mein': (None, 'my', 'aking / ko'), 'dein': (None, 'your (du)', 'iyong / mo'), 'Ihr (Possessiv)': (None, 'your (polite)', 'inyong (magalang)'),
    'sehen': (None, 'to see', 'makita'), 'hören': (None, 'to hear', 'marinig'), 'lesen': (None, 'to read', 'magbasa'), 'schreiben': (None, 'to write', 'sumulat'),
    'leben': (None, 'to live', 'mabuhay / tumira'), 'bleiben': (None, 'to stay', 'manatili'), 'zufrieden': (None, 'content, satisfied', 'kuntento'),
    'Mann': ('der', 'man; husband', 'lalaki; asawang lalaki'), 'Kind': ('das', 'child', 'anak / bata'), 'Familie': ('die', 'family', 'pamilya'),
    'Eltern': ('die', 'parents (plural)', 'mga magulang'), 'Mutter': ('die', 'mother', 'nanay'), 'Vater': ('der', 'father', 'tatay'), 'Sohn': ('der', 'son', 'anak na lalaki'),
    'Tochter': ('die', 'daughter', 'anak na babae'), 'Bruder': ('der', 'brother', 'kapatid na lalaki'), 'Schwester': ('die', 'sister', 'kapatid na babae'),
    'Geschwister': ('die', 'siblings (plural)', 'magkakapatid'), 'Großeltern': ('die', 'grandparents (plural)', 'lolo at lola'), 'Oma': ('die', 'grandma', 'lola'),
    'Opa': ('der', 'grandpa', 'lolo'), 'Baby': ('das', 'baby', 'sanggol'), 'Partner, Partnerin': ('der', 'partner (man, woman)', 'partner'),
    'verheiratet': (None, 'married', 'kasal'), 'ledig': (None, 'single (not married)', 'walang asawa'), 'geschieden': (None, 'divorced', 'hiwalay (diborsyado)'),
    'Freund, Freundin': ('der', 'friend; boyfriend, girlfriend', 'kaibigan; nobyo, nobya'), 'Leute': ('die', 'people (plural)', 'mga tao'), 'glücklich': (None, 'happy', 'masaya'),
    'traurig': (None, 'sad', 'malungkot'), 'lieben': (None, 'to love', 'magmahal'), 'heiraten': (None, 'to marry', 'magpakasal'), 'Verwandte': ('die', 'relatives (plural)', 'mga kamag-anak'),
    'Mädchen': ('das', 'girl', 'batang babae'), 'Bub': ('der', 'boy (in Germany: Junge)', 'batang lalaki (sa Germany: Junge)'), 'Jugendliche': ('die', 'young people', 'mga kabataan'),
    'Erwachsene': ('die', 'adults', 'mga nasa hustong gulang'), 'Dame': ('die', 'lady', 'ginang'), 'Ehefrau': ('die', 'wife', 'asawang babae'), 'Ehemann': ('der', 'husband', 'asawang lalaki'),
    'Bekannte': ('die', 'acquaintances', 'mga kakilala'), 'gestorben': (None, 'died, dead', 'namatay'),
}

# ---------------------------------------------------------------- pictures
TREE = ('<g stroke="#8a7a5a" stroke-width="3" fill="none"><path d="M120 88v14h160V88M200 102v28M120 160v14h160v-14"/><path d="M120 196v0"/></g>'
        + ''.join(f'<rect x="{x-58}" y="{y}" width="116" height="34" rx="8" fill="#fff" stroke="{c}" stroke-width="3"/>' + label(x, y + 23, t, 15)
                  for x, y, t, c in ((120, 54, 'Opa Franz', '#34506b'), (280, 54, 'Oma Maria', '#c8102e'), (120, 128, 'Vater Peter', '#34506b'), (280, 128, 'Mutter Anna', '#c8102e'),
                                     (120, 196, 'Lukas (Bub)', '#2a9d8f'), (280, 196, 'Lena (Mädchen)', '#f77f00')))
        + '<path d="M178 145h44" stroke="#c8102e" stroke-width="3"/>' + label(200, 30, 'Familie Huber', 18, '#c8102e'))
PICS['stammbaum'] = TREE.replace('<path d="M120 160v14h160v-14"/>', '').replace('M120 88v14h160V88M200 102v28M120 160v14h160v-14', 'M120 88v14h160V88M200 102v26M200 162v18h-80v16M200 180h80v16')
PICS['geschwister'] = (person(80, '#c8102e', 'b', '#222', long=True) + person(200, '#1d4e89', 'b', '#222') + person(320, '#2a9d8f', 'b', '#222', long=True)
                       + label(80, 240, 'ich: Maria', 14, '#fff') + label(200, 240, 'Jose', 14, '#fff') + label(320, 240, 'Ana', 14, '#fff') + label(200, 34, 'Maria und ihre Geschwister', 17))
PICS['park'] = ('<rect y="200" width="400" height="60" fill="#7cc36a"/><circle cx="350" cy="50" r="26" fill="#ffd23f"/>'
                + person(70, '#34506b', 'a', '#7a4e2d') + person(160, '#c8102e', 'a', '#7a4e2d', long=True) + person(250, '#f77f00', 'a', '#d9a066', long=True, s=0.6)
                + '<ellipse cx="335" cy="220" rx="34" ry="22" fill="#9ed8ff"/><circle cx="335" cy="196" r="16" fill="#f1c9a5"/><path d="M300 236h70" stroke="#555" stroke-width="4"/>'
                + label(70, 250, 'Mann', 13, '#fff') + label(160, 250, 'Frau', 13, '#fff') + label(250, 250, 'Mädchen', 12, '#fff') + label(335, 256, 'Baby', 12, '#1f2937'))
PICS['plural'] = (panel(10, 20, 120, 220, 1) + panel(140, 20, 120, 220, 2) + panel(270, 20, 120, 220, 3)
                  + ''.join(person(x, '#f77f00', 'a', '#4a2f1c', y=-55, s=0.4) for x in (40, 70, 100)) + label(70, 230, 'Kinder', 15)
                  + ''.join(person(x, '#34506b', 'b', '#222', y=-55, s=0.5) for x in (180, 220)) + label(200, 230, 'Männer', 15)
                  + ''.join(person(x, '#c8102e', 'a', '#7a4e2d', y=-55, s=0.4, long=True) for x in (290, 315, 340, 365)) + label(330, 230, 'Frauen', 15))
PICS['foto'] = (person(90, '#2a9d8f', 'a', '#4a2f1c') + label(90, 240, 'Lukas', 14, '#fff') + bubble(140, 18, 230, 'Das ist meine Mutter.', 15, tail_x=160)
                + '<rect x="230" y="80" width="130" height="150" rx="6" fill="#fff" stroke="#8a7a5a" stroke-width="6"/>'
                + '<g transform="translate(295 210) scale(0.42) translate(-295 -210)">' + person(295, '#c8102e', 'a', '#7a4e2d', y=-50, long=True) + '</g>')
PICS['formular'] = ('<rect x="40" y="20" width="320" height="220" rx="8" fill="#fff" stroke="#9ca3af" stroke-width="2"/>' + label(200, 50, 'Familienstand', 20)
                    + label(70, 82, 'Name: Sofia Berger', 15, anchor='start', bold=False)
                    + ''.join(f'<rect x="80" y="{y}" width="24" height="24" fill="#fff" stroke="#1f2937" stroke-width="2"/>' + label(120, y + 19, t, 17, anchor='start', bold=False)
                              for y, t in ((104, 'ledig'), (144, 'verheiratet'), (184, 'geschieden')))
                    + '<path d="M84 148l16 16M100 148l-16 16" stroke="#c8102e" stroke-width="4"/>')
PICS['verben'] = (panel(10, 20, 88, 220, 1) + panel(108, 20, 88, 220, 2) + panel(206, 20, 88, 220, 3) + panel(304, 20, 88, 220, 4)
                  + '<ellipse cx="54" cy="130" rx="30" ry="18" fill="#fff" stroke="#1f2937" stroke-width="3"/><circle cx="54" cy="130" r="10" fill="#1d4e89"/>'
                  + '<path d="M140 104q24-10 30 20t-14 36q-8-4-4-12" stroke="#1f2937" stroke-width="4" fill="#f1c9a5"/>'
                  + '<path d="M222 110l28 8 28-8v52l-28 8-28-8z" fill="#fff" stroke="#1d4e89" stroke-width="3"/><path d="M250 118v52" stroke="#1d4e89" stroke-width="2"/>'
                  + '<path d="M330 160l40-40 8 8-40 40-12 4z" fill="#f2c14e" stroke="#1f2937" stroke-width="2"/><path d="M320 180h50" stroke="#1d4e89" stroke-width="3"/>')
PICS['hochzeit'] = ('<path d="M150 260v-90q50-26 100 0v90z" fill="#fff" stroke="#ddd" stroke-width="2"/>' + person(150, '#1f2937', 'a', '#4a2f1c') + person(250, '#fff', 'b', '#222', long=True)
                    + ''.join(f'<path d="M{x} {y}c-6-10-20-4-14 6l14 12 14-12c6-10-8-16-14-6z" fill="#c8102e"/>' for x, y in ((200, 60), (90, 40), (320, 50)))
                    + label(150, 240, 'Peter', 14, '#fff') + label(250, 240, 'Anna', 14, '#1f2937'))
PICS['leute'] = ('<rect y="190" width="400" height="70" fill="#d9c3a3"/>'
                 + ''.join(person(x, c, sk, hr, s=0.55, long=lg) for x, c, sk, hr, lg in ((50, '#2a9d8f', 'a', '#7a4e2d', True), (125, '#1d4e89', 'b', '#222', False), (200, '#f77f00', 'c', '#222', False), (275, '#c8102e', 'a', '#d9a066', True), (350, '#34506b', 'b', '#222', True)))
                 + bubble(120, 20, 160, 'Hallo, Leute!', 16))
PICS['familien'] = (panel(10, 20, 120, 220, 1) + panel(140, 20, 120, 220, 2) + panel(270, 20, 120, 220, 3)
                    + person(60, '#c8102e', 'a', '#7a4e2d', y=-30, s=0.5, long=True) + person(95, '#f77f00', 'a', '#7a4e2d', y=-30, s=0.35)
                    + person(170, '#34506b', 'a', '#4a2f1c', y=-30, s=0.5) + person(205, '#c8102e', 'b', '#222', y=-30, s=0.5, long=True) + person(235, '#2a9d8f', 'b', '#222', y=-30, s=0.35)
                    + person(300, '#34506b', 'a', '#4a2f1c', y=-30, s=0.5) + person(340, '#1d4e89', 'c', '#222', y=-30, s=0.5) + person(370, '#f77f00', 'b', '#222', y=-30, s=0.33)
                    + ''.join(f'<rect x="{x}" y="250" width="120" height="0"/>' for x in (10,)))

STAMM = lambda: img('stammbaum', 'Ein Stammbaum der Familie Huber mit Großeltern, Eltern und Kindern.', 'A family tree of the Huber family with grandparents, parents and children.', 'Family tree ng pamilyang Huber: lolo at lola, magulang at mga anak.')
FORM = lambda: img('formular', 'Ein Formular mit Name und Familienstand. Ein Feld ist angekreuzt.', 'A form with a name and marital status. One box is ticked.', 'Form na may pangalan at civil status. May isang kahong may ekis.')
FAM = lambda: img('familien', 'Drei Bilder mit drei Familien.', 'Three pictures with three families.', 'Tatlong larawan ng tatlong pamilya.')

# ---------------------------------------------------------------- lessons (10, A1-04 spec)
X = ''
lesson(1, L('Die Familie', 'The family', 'Ang pamilya'), ['Familie', 'Mutter', 'Vater', 'Eltern', 'Sohn', 'Tochter', 'Kind'], [
    C('die Familie', 'Mutter + Vater = die Eltern. Sohn und Tochter = die Kinder.', 'Mother + father = the parents (Eltern). Son and daughter = the children (Kinder).', 'Nanay + tatay = magulang (Eltern). Anak na lalaki at babae = mga anak (Kinder).'),
    C('die Mutter – der Vater', 'Die Mutter und der Vater sind die Eltern.', 'The mother and the father are the parents.', 'Ang nanay at tatay ay ang mga magulang.'),
    C('der Sohn – die Tochter – das Kind', 'Lukas ist der Sohn, Lena ist die Tochter. Beide sind Kinder.', 'Lukas is the son, Lena the daughter. Both are children.', 'Anak na lalaki si Lukas, anak na babae si Lena. Pareho silang anak.'),
    C('die Eltern', 'Eltern gibt es nur im Plural.', '“Eltern” only exists in the plural.', 'Plural lang ang “Eltern”.'),
], [
    choice(X, 'lesen', LOOK, 'Wer ist die Mutter von Lena?', 'Anna', ['Maria', 'Peter'], L('Im Stammbaum: Mutter Anna, Tochter Lena.', 'In the family tree: mother Anna, daughter Lena.', 'Sa family tree: nanay si Anna, anak si Lena.'), [G1], R('Mutter'), img=STAMM()),
    choice(X, 'lesen', LOOK, 'Lukas ist … von Peter.', 'der Sohn', ['der Vater', 'die Tochter'], L('Peter ist der Vater, Lukas ist der Sohn.', 'Peter is the father, Lukas is the son.', 'Tatay si Peter, anak si Lukas.'), [G1], R('Sohn', 'Vater'), img=STAMM()),
    choice(X, 'hoeren', LISTEN, None, 'zwei Kinder', ['drei Kinder'], L('Sie hören: „Ich habe zwei Kinder, einen Sohn und eine Tochter.“', 'You hear: “Ich habe zwei Kinder, einen Sohn und eine Tochter.”', 'Naririnig mo: “Ich habe zwei Kinder, einen Sohn und eine Tochter.”'), [G1], R('Kind'), audio='Ich habe zwei Kinder, einen Sohn und eine Tochter.'),
    cloze(X, 'grammatikWortschatz', GAPS, 'Mutter und Vater sind die {{1}}.', [['Eltern']], L('Mutter + Vater = die Eltern.', 'mother + father = the parents (Eltern).', 'nanay + tatay = Eltern.'), [G1], R('Eltern')),
])
lesson(2, L('Geschwister', 'Siblings', 'Magkakapatid'), ['Bruder', 'Schwester', 'Geschwister'], [
    C('der Bruder – die Schwester', 'Jose ist der Bruder von Maria. Ana ist die Schwester.', 'Jose is Maria’s brother. Ana is her sister.', 'Kuya/kapatid na lalaki ni Maria si Jose. Kapatid na babae si Ana.'),
    C('die Geschwister', 'Bruder und Schwester zusammen = Geschwister.', 'Brothers and sisters together = Geschwister (siblings).', 'Magkapatid na lalaki at babae = Geschwister.'),
    C('Hast du Geschwister? – Ja, zwei.', 'Kurze Antwort mit der Zahl.', 'Short answer with the number.', 'Maikling sagot gamit ang bilang.'),
], [
    choice(X, 'lesen', LOOK, 'Wie viele Geschwister hat Maria?', 'zwei', ['drei', 'eins'], L('Maria hat einen Bruder (Jose) und eine Schwester (Ana): zwei Geschwister.', 'Maria has a brother (Jose) and a sister (Ana): two siblings.', 'May isang kapatid na lalaki (Jose) at babae (Ana) si Maria: dalawa.'), [G1], R('Geschwister'),
           img=img('geschwister', 'Maria mit ihrem Bruder und ihrer Schwester.', 'Maria with her brother and her sister.', 'Si Maria kasama ang kapatid na lalaki at babae.')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Ana ist die … von Jose.', 'Schwester', ['Bruder', 'Mutter'], L('Ana ist eine Frau: die Schwester.', 'Ana is female: die Schwester (sister).', 'Babae si Ana: die Schwester.'), [G1], R('Schwester')),
    choice(X, 'hoeren', LISTEN, None, 'einen Bruder', ['eine Schwester'], L('Sie hören: „Ich habe einen Bruder. Er wohnt in Graz.“', 'You hear: “Ich habe einen Bruder. Er wohnt in Graz.”', 'Naririnig mo: “Ich habe einen Bruder. Er wohnt in Graz.”'), [G1], R('Bruder'), audio='Ich habe einen Bruder. Er wohnt in Graz.'),
    choice(X, 'sprechen', SAY, 'Hast du Geschwister?', 'Ja, eine Schwester.', ['Ja, ich bin Schwester.', 'Ja, Geschwister ist zwei.'], L('Kurz und richtig: „Ja, eine Schwester.“', 'Short and correct: “Ja, eine Schwester.”', 'Maikli at tama: “Ja, eine Schwester.”'), [G2], R('Schwester')),
])
lesson(3, L('Mann, Frau, Kind, Baby', 'Man, woman, child, baby', 'Lalaki, babae, bata, sanggol'), ['Mann', 'Mädchen', 'Bub', 'Baby', 'Erwachsene', 'Jugendliche', 'Dame'], [
    C('der Mann – die Frau', 'Mann und Frau sind Erwachsene.', 'Man and woman are adults (Erwachsene).', 'Ang lalaki at babae ay nasa hustong gulang (Erwachsene).'),
    C('das Mädchen – der Bub', 'In Österreich sagt man „der Bub“. (in Deutschland: „der Junge“). „das Mädchen“ hat den Artikel „das“!', 'In Austria you say “der Bub” (in Germany: “der Junge”). “das Mädchen” takes “das”!', 'Sa Austria: “der Bub” (sa Germany: “der Junge”). May “das” ang “das Mädchen”!'),
    C('das Baby', 'Ein Baby ist ein sehr kleines Kind.', 'A baby is a very small child.', 'Ang baby ay napakaliit na bata.'),
], [
    choice(X, 'lesen', LOOK, 'Wie viele Kinder sind im Bild?', 'zwei', ['drei', 'eins'], L('Ein Mädchen und ein Baby: zwei Kinder. Mann und Frau sind Erwachsene.', 'A girl and a baby: two children. Man and woman are adults.', 'Isang batang babae at baby: dalawang bata. Nasa hustong gulang ang lalaki at babae.'), [G1], R('Kind', 'Mädchen', 'Baby'),
           img=img('park', 'Eine Familie im Park: Mann, Frau, Mädchen und Baby.', 'A family in the park: man, woman, girl and baby.', 'Pamilya sa park: lalaki, babae, batang babae at baby.')),
    choice(X, 'grammatikWortschatz', CHOOSE, '… Mädchen', 'das', ['die', 'der'], L('Achtung: das Mädchen – mit „das“.', 'Careful: das Mädchen – with “das”.', 'Ingat: das Mädchen – may “das”.'), [G1], R('Mädchen')),
    choice(X, 'grammatikWortschatz', CHOOSE, '… Bub', 'der', ['die', 'das'], L('der Bub – ein Mann ist er später: der.', 'der Bub (boy) – masculine: der.', 'der Bub (batang lalaki) – panlalaki: der.'), [G1], R('Bub')),
])
lesson(4, L('Ein Kind, zwei Kinder – der Plural', 'One child, two children – the plural', 'Isang anak, dalawang anak – plural'), [], [
    C('das Kind → die Kinder', 'Im Plural ist der Artikel immer „die“.', 'In the plural the article is always “die”.', 'Sa plural, laging “die” ang article.'),
    C('der Mann → die Männer · die Frau → die Frauen', 'Endungen: -er (oft mit Umlaut), -en/-n, -e, -s oder ohne Endung.', 'Endings: -er (often with umlaut), -en/-n, -e, -s or none.', 'Mga ending: -er (madalas may umlaut), -en/-n, -e, -s o wala.'),
    C('der Sohn → die Söhne · die Tochter → die Töchter', 'Den Plural immer mitlernen!', 'Always learn the plural too!', 'Laging isaulo ang plural!'),
    C('die Mutter → die Mütter · der Vater → die Väter', 'Umlaut im Plural: u → ü, a → ä.', 'Umlaut in the plural: u → ü, a → ä.', 'Umlaut sa plural: u → ü, a → ä.'),
    C('das Baby → die Babys · der Bruder → die Brüder', '-s bei Wörtern wie Baby, Opa, Oma.', '-s with words like Baby, Opa, Oma.', '-s sa mga salitang Baby, Opa, Oma.'),
], [
    choice(X, 'grammatikWortschatz', LOOK, 'Bild 1: drei …', 'Kinder', ['Kinds', 'Kind'], L('das Kind → die Kinder.', 'das Kind → die Kinder (one child → children).', 'das Kind → die Kinder (plural).'), [G4], R('Kind'),
           img=img('plural', 'Drei Bilder: Kinder, Männer und Frauen.', 'Three pictures: children, men and women.', 'Tatlong larawan: mga bata, lalaki at babae.')),
    cloze(X, 'grammatikWortschatz', GAPS, 'ein Mann – zwei {{1}} · eine Frau – vier {{2}}', [['Männer'], ['Frauen']], L('der Mann → die Männer, die Frau → die Frauen.', 'der Mann → die Männer, die Frau → die Frauen (plural).', 'der Mann → die Männer, die Frau → die Frauen (plural).'), [G4], R('Mann')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'ein Sohn – zwei …', 'Söhne', ['Sohns', 'Sohnen'], L('der Sohn → die Söhne (mit Umlaut).', 'der Sohn → die Söhne (with umlaut).', 'der Sohn → die Söhne (may umlaut).'), [G4], R('Sohn')),
    choice(X, 'hoeren', LISTEN, None, 'zwei Töchter', ['zwei Söhne'], L('Sie hören: „Ich habe zwei Töchter.“', 'You hear: “Ich habe zwei Töchter.”', 'Naririnig mo: “Ich habe zwei Töchter.”'), [G4], R('Tochter'), audio='Ich habe zwei Töchter.'),
])
lesson(5, L('Mein, meine – dein, Ihr', 'My – your', 'Aking – iyong'), ['mein', 'dein', 'Ihr (Possessiv)'], [
    C('Das ist mein Bruder. Das ist meine Schwester.', 'der/das → mein, die → meine. Zuerst als feste Form lernen.', 'der/das → mein, die → meine. Learn it as a fixed form first.', 'der/das → mein, die → meine. Isaulo muna bilang buo.'),
    C('Das ist mein Kind. Das sind meine Eltern.', 'Plural → meine.', 'Plural → meine.', 'Plural → meine.'),
    C('dein Vater – deine Mutter', 'Mit „du“: dein, deine.', 'With “du”: dein, deine.', 'Sa “du”: dein, deine.'),
    C('Ihr Vater – Ihre Mutter', 'Höflich (Sie): Ihr, Ihre – groß geschrieben.', 'Polite (Sie): Ihr, Ihre – with a capital I.', 'Magalang (Sie): Ihr, Ihre – malaking I.'),
], [
    choice(X, 'lesen', LOOK, 'Wer ist auf dem Foto?', 'die Mutter von Lukas', ['der Vater von Lukas', 'die Schwester von Lukas'], L('Lukas sagt: „Das ist meine Mutter.“', 'Lukas says: “Das ist meine Mutter.”', 'Sabi ni Lukas: “Das ist meine Mutter.”'), [G2], R('mein', 'Mutter'),
           img=img('foto', 'Lukas zeigt ein Foto und sagt etwas.', 'Lukas shows a photo and says something.', 'Ipinapakita ni Lukas ang litrato at may sinasabi.')),
    cloze(X, 'grammatikWortschatz', GAPS, 'Das ist {{1}} Vater und das ist {{2}} Mutter.', [['mein'], ['meine']], L('der Vater → mein, die Mutter → meine.', 'der Vater → mein (my), die Mutter → meine (my).', 'der Vater → mein (aking), die Mutter → meine (aking).'), [G2], R('mein')),
    choice(X, 'sprechen', L('Sie sprechen mit einer Frau. Sie sagen „Sie“. Was fragen Sie? Wählen Sie, dann sagen Sie es laut.', 'You talk to a woman and say “Sie”. What do you ask? Choose, then say it aloud.', 'Kausap mo ang isang babae, “Sie” ang gamit. Ano ang itatanong mo? Pumili, tapos sabihin nang malakas.'), None, 'Wie heißt Ihr Sohn?', ['Wie heißt dein Sohn?', 'Wie heißt meine Sohn?'], L('Mit „Sie“: Ihr Sohn.', 'With “Sie”: Ihr Sohn.', 'Sa “Sie”: Ihr Sohn.'), [G2], R('Ihr (Possessiv)')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Anna, wie alt ist … Bruder?', 'dein', ['deine', 'Ihre'], L('Mit „du“ (Anna): dein Bruder.', 'With “du” (Anna): dein Bruder.', 'Sa “du” (Anna): dein Bruder.'), [G2], R('dein')),
])
lesson(6, L('Familienstand', 'Marital status', 'Civil status'), ['verheiratet', 'ledig', 'geschieden', 'Ehefrau', 'Ehemann', 'Partner, Partnerin', 'heiraten', 'gestorben'], [
    C('Ich bin verheiratet.', 'Der Familienstand steht in vielen Formularen, z. B. auf dem Meldezettel.', 'Marital status is on many forms, e.g. the Meldezettel (registration form).', 'Nasa maraming form ang civil status, hal. Meldezettel.'),
    C('ledig – verheiratet – geschieden', 'ledig = nicht verheiratet.', 'ledig = not married.', 'ledig = walang asawa.'),
    C('die Ehefrau – der Ehemann – der Partner, die Partnerin', 'Mein Mann = mein Ehemann. Partner/Partnerin: auch ohne Ehe.', 'Mein Mann = my husband. Partner: also without marriage.', 'Mein Mann = asawa kong lalaki. Partner: kahit hindi kasal.'),
    C('Sie heiraten im Mai.', '„heiraten“: ich heirate, du heiratest, er heiratet.', '“heiraten” (marry): ich heirate, du heiratest, er heiratet.', '“heiraten” (magpakasal): ich heirate, du heiratest, er heiratet.'),
], [
    choice(X, 'lesen', LOOK, 'Ist Sofia Berger ledig?', 'Nein, sie ist verheiratet.', ['Ja, sie ist ledig.', 'Nein, sie ist geschieden.'], L('Im Formular ist „verheiratet“ angekreuzt.', '“verheiratet” is ticked on the form.', 'May ekis ang “verheiratet” sa form.'), [G3], R('ledig', 'verheiratet'), img=FORM()),
    choice(X, 'sprechen', L('Sie sind nicht verheiratet. Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'You are not married. What do you say? Choose, then say it aloud.', 'Hindi ka kasal. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'), 'Sind Sie verheiratet?', 'Nein, ich bin ledig.', ['Nein, ich habe ledig.', 'Ja, ich bin ledig.'], L('„Ich bin ledig.“ – mit „sein“.', '“Ich bin ledig.” – with “sein”.', '“Ich bin ledig.” – gamit ang “sein”.'), [G3], R('ledig')),
    choice(X, 'hoeren', LISTEN, None, 'Die Frau ist geschieden.', ['Die Frau ist verheiratet.'], L('Sie hören: „Ich bin geschieden. Ich lebe allein mit meiner Tochter.“', 'You hear: “Ich bin geschieden. Ich lebe allein mit meiner Tochter.”', 'Naririnig mo: “Ich bin geschieden. Ich lebe allein mit meiner Tochter.”'), [G3], R('geschieden'), audio='Ich bin geschieden. Ich lebe allein mit meiner Tochter.'),
    cloze(X, 'grammatikWortschatz', GAPS, 'Peter ist der {{1}} von Anna. Anna ist die {{2}} von Peter.', [['Ehemann', 'Mann'], ['Ehefrau', 'Frau']], L('der Ehemann – die Ehefrau (auch: mein Mann, meine Frau).', 'husband (Ehemann) – wife (Ehefrau); also: mein Mann, meine Frau.', 'Ehemann – Ehefrau (o: mein Mann, meine Frau).'), [G3], R('Ehemann', 'Ehefrau')),
])
lesson(7, L('sehen, hören, lesen, schreiben', 'see, hear, read, write', 'makita, marinig, magbasa, sumulat'), ['sehen', 'hören', 'lesen', 'schreiben'], [
    C('ich sehe – du siehst – er sieht', '„sehen“: e → ie bei du und er/sie/es.', '“sehen”: e → ie with du and er/sie/es.', '“sehen”: e → ie sa du at er/sie/es.'),
    C('ich lese – du liest – sie liest', '„lesen“: e → ie.', '“lesen”: e → ie.', '“lesen”: e → ie.'),
    C('ich höre – du hörst · ich schreibe – du schreibst', '„hören“ und „schreiben“ sind regelmäßig.', '“hören” and “schreiben” are regular.', 'Regular ang “hören” at “schreiben”.'),
], [
    choice(X, 'grammatikWortschatz', LOOK, 'Bild 3: Was macht man hier?', 'lesen', ['hören', 'schreiben'], L('Bild 3 zeigt ein offenes Buch: lesen. 1 = sehen, 2 = hören, 4 = schreiben.', 'Picture 3 shows an open book: lesen (read). 1 = see, 2 = hear, 4 = write.', 'Larawan 3: bukas na libro: lesen. 1 = makita, 2 = marinig, 4 = sumulat.'), [G5], R('lesen'),
           img=img('verben', 'Vier Bilder: ein Auge, ein Ohr, ein Buch, ein Stift.', 'Four pictures: an eye, an ear, a book, a pen.', 'Apat na larawan: mata, tainga, libro, panulat.')),
    cloze(X, 'grammatikWortschatz', GAPS, 'Du {{1}} (sehen) die Kinder. Oma {{2}} (lesen) gern.', [['siehst'], ['liest']], L('du siehst, sie liest – e wird ie.', 'du siehst, sie liest – e becomes ie.', 'du siehst, sie liest – nagiging ie ang e.'), [G5], R('sehen', 'lesen')),
    cloze(X, 'grammatikWortschatz', GAPS, 'Ich {{1}} (hören) Musik. Du {{2}} (schreiben) eine Nachricht.', [['höre'], ['schreibst']], L('ich höre, du schreibst – regelmäßig.', 'ich höre, du schreibst – regular.', 'ich höre, du schreibst – regular.'), [G5], R('hören', 'schreiben')),
])
lesson(8, L('Glücklich und traurig', 'Happy and sad', 'Masaya at malungkot'), ['glücklich', 'traurig', 'lieben', 'zufrieden'], [
    C('Peter und Anna heiraten. Sie sind glücklich.', 'glücklich = sehr froh.', 'glücklich = very happy.', 'glücklich = napakasaya.'),
    C('Ich liebe meine Familie.', '„lieben“: ich liebe, du liebst, er liebt.', '“lieben” (love): ich liebe, du liebst, er liebt.', '“lieben” (magmahal): ich liebe, du liebst, er liebt.'),
    C('Der Opa ist gestorben. Die Familie ist traurig.', 'traurig ist das Gegenteil von glücklich.', 'traurig (sad) is the opposite of glücklich.', 'Kabaligtaran ng glücklich ang traurig (malungkot).'),
], [
    choice(X, 'lesen', LOOK, 'Was machen Peter und Anna heute?', 'Sie heiraten.', ['Sie sind traurig.', 'Sie sind geschieden.'], L('Das Bild zeigt eine Hochzeit: Peter und Anna heiraten und sind glücklich.', 'The picture shows a wedding: Peter and Anna marry and are happy.', 'Kasal ang nasa larawan: ikakasal sina Peter at Anna at masaya sila.'), [G5], R('heiraten', 'glücklich'),
           img=img('hochzeit', 'Ein Paar bei der Hochzeit mit Herzen.', 'A couple at their wedding with hearts.', 'Magkasintahan sa kasal na may mga puso.')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Das Baby lacht. Es ist …', 'glücklich', ['traurig', 'geschieden'], L('Lachen = glücklich.', 'Laughing = happy (glücklich).', 'Tumatawa = masaya (glücklich).'), None, R('glücklich')),
    cloze(X, 'grammatikWortschatz', GAPS, 'Ich {{1}} (lieben) meine Kinder.', [['liebe']], L('ich liebe.', 'ich liebe (I love).', 'ich liebe (mahal ko).'), [G5], R('lieben')),
])
lesson(9, L('Freunde, Verwandte, Leute', 'Friends, relatives, people', 'Kaibigan, kamag-anak, tao'), ['Freund, Freundin', 'Leute', 'Verwandte', 'Bekannte', 'Großeltern', 'Oma', 'Opa', 'leben', 'bleiben'], [
    C('die Großeltern: Oma und Opa', 'Oma = Großmutter, Opa = Großvater.', 'Oma = grandma, Opa = grandpa.', 'Oma = lola, Opa = lolo.'),
    C('der Freund – die Freundin', 'Auch: mein Freund = Partner. Der Kontext zeigt es.', 'Also: mein Freund can mean boyfriend. Context shows it.', 'Puwede ring nobyo ang mein Freund. Konteksto ang magsasabi.'),
    C('die Verwandten – die Bekannten – die Leute', 'Verwandte = Familie. Bekannte = man kennt sie. Leute = Menschen.', 'Verwandte = family. Bekannte = people you know. Leute = people.', 'Verwandte = kamag-anak. Bekannte = kakilala. Leute = mga tao.'),
    C('Meine Eltern leben in Manila. Ich bleibe in Wien.', '„leben“ = wohnen, da sein. „bleiben“ = nicht weggehen.', '“leben” = live; “bleiben” = stay.', '“leben” = tumira; “bleiben” = manatili.'),
], [
    choice(X, 'lesen', LOOK, 'Wie viele Leute sind im Bild?', 'fünf', ['vier', 'sechs'], L('Im Bild sind fünf Personen.', 'There are five people in the picture.', 'Limang tao ang nasa larawan.'), None, R('Leute'),
           img=img('leute', 'Fünf Personen stehen zusammen. Eine sagt „Hallo, Leute!“.', 'Five people stand together. One says “Hallo, Leute!”.', 'Limang tao ang magkakasama. May nagsasabing “Hallo, Leute!”.')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Die Mutter von meiner Mutter ist meine …', 'Oma', ['Tochter', 'Schwester'], L('Die Mutter der Mutter = die Oma (Großmutter).', 'Mother’s mother = Oma (grandma).', 'Nanay ng nanay = Oma (lola).'), [G1], R('Oma')),
    choice(X, 'hoeren', LISTEN, None, 'Die Eltern leben in Manila.', ['Die Eltern leben in Wien.'], L('Sie hören: „Meine Eltern leben in Manila. Ich bleibe in Wien.“', 'You hear: “Meine Eltern leben in Manila. Ich bleibe in Wien.”', 'Naririnig mo: “Meine Eltern leben in Manila. Ich bleibe in Wien.”'), [G5], R('leben', 'bleiben'), audio='Meine Eltern leben in Manila. Ich bleibe in Wien.'),
])
WOW = L('In Österreich gibt es verschiedene Familienformen: Eltern mit Kindern, Paare ohne Kinder, eine Mutter oder ein Vater allein mit Kindern, Familien mit zwei Müttern oder zwei Vätern, Patchwork-Familien.',
        'In Austria there are different family forms: parents with children, couples without children, a mother or father alone with children, families with two mothers or two fathers, patchwork families.',
        'Sa Austria may iba’t ibang anyo ng pamilya: magulang na may anak, mag-asawang walang anak, nanay o tatay na mag-isang may anak, pamilyang may dalawang nanay o dalawang tatay, patchwork.')
lesson(10, L('Familien in Österreich', 'Families in Austria', 'Mga pamilya sa Austria'), [], [
    C('Es gibt viele Familienformen.', 'Vater, Mutter, Kinder – oder eine Mutter allein mit Kind – oder zwei Väter mit Kind. Alles ist Familie.', 'Father, mother, children – or a mother alone with a child – or two fathers with a child. All of it is family.', 'Tatay, nanay, anak – o nanay na mag-isa kasama ang anak – o dalawang tatay at anak. Lahat ay pamilya.'),
    C('Familien sind verschieden.', 'verschieden = nicht gleich. Ein Paar = zwei Menschen, z. B. Mann und Frau.', 'verschieden = different. Ein Paar = a couple.', 'verschieden = magkakaiba. Ein Paar = magkapareha.'),
    C('die Patchwork-Familie', 'Eltern mit Kindern aus einer früheren Beziehung.', 'Parents with children from an earlier relationship.', 'Magulang na may anak mula sa naunang relasyon.'),
], [
    choice(X, 'werte', LOOK, 'Bild 1: eine Mutter mit Kind. Ist das eine Familie?', 'Ja, das ist eine Familie.', ['Nein, das ist keine Familie.'], WOW, [G6], R('Familie'), img=FAM()),
    choice(X, 'werte', LOOK, 'Wie viele Familien sind im Bild?', 'drei', ['eine'], WOW, [G6], R('Familie'), img=FAM()),
    choice(X, 'werte', CHOOSE, 'Gibt es in Österreich nur eine Familienform?', 'Nein, es gibt viele Familienformen.', ['Ja, nur Vater, Mutter und Kinder.'], WOW, [G6], R('Familie')),
])

# ---------------------------------------------------------------- pools
E = L
REL = {'Mutter': ('mother', 'nanay'), 'Vater': ('father', 'tatay'), 'Sohn': ('son', 'anak na lalaki'), 'Tochter': ('daughter', 'anak na babae'), 'Bruder': ('brother', 'kapatid na lalaki'),
       'Schwester': ('sister', 'kapatid na babae'), 'Oma': ('grandma', 'lola'), 'Opa': ('grandpa', 'lolo')}
TREEQ = lambda v, i: choice(i, 'lesen', LOOK, v[0], v[1], v[2], same(v[3]), [G1], R('Familie'), img=STAMM())
fam('LE1', TREEQ, [('Wer ist der Opa von Lukas?', 'Franz', ['Peter', 'Maria'], 'Opa Franz.'), ('Lena ist … von Anna.', 'die Tochter', ['die Mutter', 'die Oma'], 'Mutter Anna – Tochter Lena.'), ('Wie viele Kinder haben Peter und Anna?', 'zwei', ['drei', 'eins'], 'Lukas und Lena: zwei Kinder.')],
    [('Wer ist die Schwester von Lukas?', 'Lena', ['Anna', 'Maria'], 'Lukas und Lena sind Geschwister.'), ('Peter ist … von Franz und Maria.', 'der Sohn', ['der Opa', 'der Bruder'], 'Franz und Maria sind die Eltern von Peter.'),
     ('Wie viele Großeltern sind im Bild?', 'zwei', ['vier', 'eins'], 'Opa Franz und Oma Maria.'), ('Wer ist die Oma von Lena?', 'Maria', ['Anna', 'Lena'], 'Oma Maria.')])

MAIL = lambda v, i: choice(i, 'lesen', READ, f'Hallo Tom!\n{v[0]}\nLiebe Grüße, {v[1]}\n\n{v[2]}', v[3], [v[4]], E(f'Im Text: „{v[5]}“', f'The text says: “{v[5]}”', f'Sabi sa teksto: “{v[5]}”'), [G1, G2], R('Familie'))
fam('LE2', MAIL,
    [('Ich habe zwei Brüder und eine Schwester. Meine Eltern leben in Manila.', 'Maria', 'Hat Maria drei Geschwister?', 'Ja.', 'Nein.', 'zwei Brüder und eine Schwester'),
     ('Ich bin verheiratet. Mein Mann heißt Ali. Wir haben ein Baby.', 'Sofia', 'Hat Sofia Kinder?', 'Ja, ein Baby.', 'Nein.', 'Wir haben ein Baby.'),
     ('Ich bin geschieden. Ich lebe mit meinem Sohn in Linz.', 'Anna', 'Lebt Anna allein?', 'Nein, mit ihrem Sohn.', 'Ja, allein.', 'Ich lebe mit meinem Sohn in Linz.')],
    [('Meine Oma ist 80. Sie wohnt bei uns.', 'Lena', 'Wohnt die Oma bei Lena?', 'Ja.', 'Nein.', 'Sie wohnt bei uns.'), ('Ich bin ledig. Meine Schwester ist verheiratet.', 'Jose', 'Ist Jose verheiratet?', 'Nein.', 'Ja.', 'Ich bin ledig.'),
     ('Mein Bruder heiratet im Mai. Ich bin sehr glücklich!', 'Ana', 'Wer heiratet?', 'der Bruder von Ana', 'Ana', 'Mein Bruder heiratet im Mai.'), ('Wir sind fünf: meine Eltern, zwei Schwestern und ich.', 'Lukas', 'Wie viele Schwestern hat Lukas?', 'zwei', 'fünf', 'zwei Schwestern')])

FORMQ = lambda v, i: choice(i, 'lesen', LOOK, v[0], v[1], v[2], same(v[3]), [G3], R('verheiratet'), img=FORM())
fam('LE3', FORMQ, [('Wie heißt die Frau im Formular?', 'Sofia Berger', ['Anna Huber', 'Maria Santos'], 'Name: Sofia Berger.'), ('Was ist angekreuzt?', 'verheiratet', ['ledig', 'geschieden'], 'Das Kreuz ist bei „verheiratet“.'), ('Ist Frau Berger geschieden?', 'Nein, verheiratet.', ['Ja.', 'Nein, ledig.'], 'Angekreuzt ist „verheiratet“.')],
    [('Was steht nicht im Formular?', 'Kinder', ['ledig', 'geschieden'], 'Im Formular: Name, ledig, verheiratet, geschieden.'), ('Ist Sofia Berger ledig?', 'Nein.', ['Ja.'], 'Sie ist verheiratet.')])

fam('HO1', lambda v, i: choice(i, 'hoeren', LISTEN, None, v[1], [v[2]], E(f'Sie hören: „{v[0]}“', f'You hear: “{v[0]}”', f'Naririnig mo: “{v[0]}”'), [G1], R('Geschwister'), audio=v[0]),
    [('Ich habe zwei Schwestern und einen Bruder.', 'drei Geschwister', 'zwei Geschwister'), ('Wir haben drei Kinder: zwei Söhne und eine Tochter.', 'eine Tochter', 'zwei Töchter'), ('Meine Großeltern leben in Graz.', 'in Graz', 'in Wien')],
    [('Ich habe keine Geschwister.', 'keine Geschwister', 'einen Bruder'), ('Meine Tochter ist zwölf und mein Sohn ist neun.', 'Der Sohn ist neun.', 'Der Sohn ist zwölf.'), ('Mein Opa ist achtzig Jahre alt.', '80 Jahre', '18 Jahre'), ('Wir sind vier: Vater, Mutter, Sohn und Tochter.', 'vier Personen', 'drei Personen')])

fam('HO2', lambda v, i: choice(i, 'hoeren', L('Hören Sie. Was ist der Familienstand?', 'Listen. What is the marital status?', 'Makinig. Ano ang civil status?'), None, v[1], [v[2]], E(f'Sie hören: „{v[0]}“', f'You hear: “{v[0]}”', f'Naririnig mo: “{v[0]}”'), [G3], R('verheiratet', 'ledig', 'geschieden'), audio=v[0]),
    [('Ich bin seit zehn Jahren verheiratet.', 'verheiratet', 'ledig'), ('Ich bin ledig und wohne allein.', 'ledig', 'verheiratet'), ('Ich bin geschieden und habe zwei Kinder.', 'geschieden', 'verheiratet')],
    [('Meine Frau heißt Maria. Wir sind verheiratet.', 'verheiratet', 'geschieden'), ('Ich habe einen Freund, aber ich bin ledig.', 'ledig', 'verheiratet'), ('Wir heiraten bald. Jetzt bin ich noch ledig.', 'ledig', 'verheiratet'), ('Ich bin nicht mehr verheiratet, ich bin geschieden.', 'geschieden', 'verheiratet')])

RE = {'kinder': ('Haben Sie Kinder?', 'Ja, zwei.'), 'gesch': ('Hast du Geschwister?', 'Ja, einen Bruder.'), 'verh': ('Sind Sie verheiratet?', 'Nein, ich bin ledig.'), 'alt': ('Wie alt ist Ihre Tochter?', 'Sieben.'),
      'wo': ('Wo leben Ihre Eltern?', 'In Manila.'), 'name': ('Wie heißt dein Sohn?', 'Lukas.'), 'foto': ('Wer ist das auf dem Foto?', 'Meine Oma.')}
fam('HO3', lambda v, i: choice(i, 'hoeren', L('Hören Sie. Welche Antwort passt?', 'Listen. Which answer fits?', 'Makinig. Aling sagot ang angkop?'), None, RE[v[0]][1], [RE[k][1] for k in v[1]],
    E(f'Frage: „{RE[v[0]][0]}“ – Antwort: „{RE[v[0]][1]}“', f'Question: “{RE[v[0]][0]}” – answer: “{RE[v[0]][1]}”', f'Tanong: “{RE[v[0]][0]}” – sagot: “{RE[v[0]][1]}”'), [G2], R('Kind'), audio=RE[v[0]][0]),
    [('kinder', ['verh', 'wo', 'name']), ('verh', ['kinder', 'alt', 'foto']), ('wo', ['alt', 'name', 'gesch'])], [('gesch', ['wo', 'verh', 'alt']), ('alt', ['wo', 'foto', 'verh']), ('name', ['alt', 'wo', 'verh']), ('foto', ['kinder', 'alt', 'wo'])])

FORMW = lambda v, i: cloze(i, 'schreiben', L('Lesen Sie. Ergänzen Sie das Formular.', 'Read. Complete the form.', 'Basahin. Kumpletuhin ang form.'), f'{v[0]}\nFamilienstand: {{{{1}}}} · Kinder: {{{{2}}}}', [[v[1]], [v[2], de(int(v[2]))] if v[2] != '0' else ['0', 'keine', 'null']],
                           E(f'Familienstand: {v[1]}, Kinder: {v[2]}.', f'Marital status: {v[1]}, children: {v[2]}.', f'Civil status: {v[1]}, anak: {v[2]}.'), [G3], R('verheiratet'))
fam('SC1', FORMW, [('Ich bin Jose. Ich bin verheiratet und habe zwei Töchter.', 'verheiratet', '2'), ('Ich heiße Anna. Ich bin geschieden. Ich habe einen Sohn.', 'geschieden', '1'), ('Mein Name ist Tom. Ich bin ledig und habe keine Kinder.', 'ledig', '0')],
    [('Ich bin Maria, verheiratet, drei Kinder.', 'verheiratet', '3'), ('Ich heiße Ali. Ich bin ledig. Kinder habe ich keine.', 'ledig', '0'), ('Ich bin Sofia. Ich bin geschieden und habe zwei Kinder.', 'geschieden', '2'), ('Ich heiße Lukas, bin verheiratet und habe ein Baby.', 'verheiratet', '1')])

PL = lambda v, i: short(i, 'schreiben', L('Schreiben Sie den Plural.', 'Write the plural.', 'Isulat ang plural.'), f'{v[0]} – zwei …', v[1], same(f'Plural: die {v[1][0]}.'), [G4], R(v[2]))
fam('SC2', PL, [('ein Kind', ['Kinder'], 'Kind'), ('eine Tochter', ['Töchter'], 'Tochter'), ('ein Baby', ['Babys'], 'Baby')],
    [('ein Bruder', ['Brüder'], 'Bruder'), ('eine Schwester', ['Schwestern'], 'Schwester'), ('ein Sohn', ['Söhne'], 'Sohn'), ('eine Oma', ['Omas'], 'Oma'), ('ein Mann', ['Männer'], 'Mann'), ('ein Mädchen', ['Mädchen'], 'Mädchen')])

MSG = lambda v, i: cloze(i, 'schreiben', L('Ergänzen Sie die Nachricht.', 'Complete the message.', 'Kumpletuhin ang mensahe.'), f'Hallo! Das ist {{{{1}}}} Familie: {{{{2}}}} {v[0]} und {{{{3}}}} {v[1]}.', [['meine'], [v[2]], [v[3]]],
                         E('die Familie → meine; der/das → mein; die (auch Plural) → meine.', 'die Familie → meine; der/das → mein; die (and plural) → meine.', 'die Familie → meine; der/das → mein; die (at plural) → meine.'), [G2], R('mein'))
fam('SC3', MSG, [('Mann', 'Kinder', 'mein', 'meine'), ('Mutter', 'Bruder', 'meine', 'mein'), ('Eltern', 'Baby', 'meine', 'mein')], [('Vater', 'Schwester', 'mein', 'meine'), ('Oma', 'Opa', 'meine', 'mein'), ('Frau', 'Sohn', 'meine', 'mein'), ('Tochter', 'Großeltern', 'meine', 'meine')])

CQ = {'Kinder?': 'Haben Sie Kinder?', 'Geschwister?': 'Haben Sie Geschwister?', 'Familienstand?': 'Sind Sie verheiratet?', 'Eltern?': 'Wo leben Ihre Eltern?', 'Partner?': 'Haben Sie einen Partner?', 'Großeltern?': 'Leben Ihre Großeltern noch?', 'Familie?': 'Wie groß ist Ihre Familie?'}
fam('SP1', lambda v, i: choice(i, 'sprechen', L('Wortkarte: Stellen Sie die Frage. Wählen Sie, dann sagen Sie es laut.', 'Word card: ask the question. Choose, then say it aloud.', 'Word card: itanong. Pumili, tapos sabihin nang malakas.'), f'Wortkarte: {v[0]}', CQ[v[0]], [CQ[k] for k in v[1]],
    E(f'Zu „{v[0]}“ passt: „{CQ[v[0]]}“', f'For “{v[0]}”: “{CQ[v[0]]}”', f'Para sa “{v[0]}”: “{CQ[v[0]]}”'), [G2], R('Ihr (Possessiv)')),
    [('Kinder?', ['Geschwister?', 'Eltern?']), ('Familienstand?', ['Kinder?', 'Partner?']), ('Geschwister?', ['Kinder?', 'Großeltern?'])], [('Eltern?', ['Großeltern?', 'Kinder?']), ('Partner?', ['Familienstand?', 'Geschwister?']), ('Großeltern?', ['Eltern?', 'Familie?']), ('Familie?', ['Kinder?', 'Eltern?'])])

OWN = lambda v, i: choice(i, 'sprechen', L(f'{v[0]} Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', f'{v[1]} What do you say? Choose, then say it aloud.', f'{v[2]} Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'), v[3], v[4], v[5], E(f'Richtig: „{v[4]}“', f'Correct: “{v[4]}”', f'Tama: “{v[4]}”'), [G2, G1], R('mein'))
fam('SP2', OWN, [('Sie haben eine Tochter und einen Sohn.', 'You have a daughter and a son.', 'May anak kang babae at lalaki.', 'Haben Sie Kinder?', 'Ja, eine Tochter und einen Sohn.', ['Ja, ich bin Tochter und Sohn.', 'Nein, eine Tochter.']),
                 ('Ihre Eltern leben in Cebu.', 'Your parents live in Cebu.', 'Nasa Cebu ang mga magulang mo.', 'Wo leben Ihre Eltern?', 'Meine Eltern leben in Cebu.', ['Mein Eltern lebt in Cebu.', 'Ich lebe in Cebu Eltern.']),
                 ('Sie haben zwei Brüder.', 'You have two brothers.', 'May dalawa kang kapatid na lalaki.', 'Haben Sie Geschwister?', 'Ja, zwei Brüder.', ['Ja, zwei Bruder.', 'Ja, ich bin zwei Brüder.'])],
    [('Ihre Familie: Mann, zwei Kinder.', 'Your family: husband, two children.', 'Pamilya mo: asawa, dalawang anak.', 'Wie groß ist Ihre Familie?', 'Wir sind vier: mein Mann, zwei Kinder und ich.', ['Ich bin vier.', 'Meine Familie ist Mann.']),
     ('Ihre Oma ist 75.', 'Your grandma is 75.', '75 ang lola mo.', 'Wie alt ist Ihre Oma?', 'Meine Oma ist fünfundsiebzig.', ['Mein Oma hat fünfundsiebzig.', 'Meine Oma ist siebenundfünfzig.']),
     ('Sie haben keine Geschwister.', 'You have no siblings.', 'Wala kang kapatid.', 'Haben Sie Geschwister?', 'Nein, ich habe keine Geschwister.', ['Nein, ich bin Geschwister.', 'Ja, keine.']),
     ('Ihr Sohn heißt Lukas.', 'Your son is called Lukas.', 'Lukas ang pangalan ng anak mo.', 'Wie heißt Ihr Sohn?', 'Mein Sohn heißt Lukas.', ['Meine Sohn heißt Lukas.', 'Mein Sohn ist heißen Lukas.'])])

INTRO = lambda v, i: choice(i, 'sprechen', L(f'Sie zeigen ein Foto: {v[0]}. Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', f'You show a photo: {v[1]}. What do you say? Choose, then say it aloud.', f'Nagpapakita ka ng litrato: {v[2]}. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'), None, v[3], v[4],
                            E('der/das → mein, die und Plural → meine.', 'der/das → mein, die and plural → meine.', 'der/das → mein, die at plural → meine.'), [G2], R('mein'))
fam('SP3', INTRO, [('Ihre Schwester', 'your sister', 'kapatid mong babae', 'Das ist meine Schwester.', ['Das ist mein Schwester.', 'Das ist meiner Schwester.']), ('Ihr Bruder', 'your brother', 'kapatid mong lalaki', 'Das ist mein Bruder.', ['Das ist meine Bruder.', 'Das sind mein Bruder.']), ('Ihre Eltern', 'your parents', 'mga magulang mo', 'Das sind meine Eltern.', ['Das ist mein Eltern.', 'Das sind mein Eltern.'])],
    [('Ihr Baby', 'your baby', 'sanggol mo', 'Das ist mein Baby.', ['Das ist meine Baby.', 'Das sind mein Baby.']), ('Ihre Großeltern', 'your grandparents', 'lolo at lola mo', 'Das sind meine Großeltern.', ['Das ist mein Großeltern.', 'Das sind mein Großeltern.']),
     ('Ihr Mann', 'your husband', 'asawa mong lalaki', 'Das ist mein Mann.', ['Das ist meine Mann.', 'Das ist mein Männer.']), ('Ihre Tochter', 'your daughter', 'anak mong babae', 'Das ist meine Tochter.', ['Das ist mein Tochter.', 'Das sind meine Tochter.'])])

STATUS = lambda v, i: choice(i, 'sprechen', L(f'{v[0]} Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', f'{v[1]} What do you say? Choose, then say it aloud.', f'{v[2]} Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'), 'Sind Sie verheiratet?', v[3], v[4],
                             E('Familienstand mit „sein“: Ich bin verheiratet / ledig / geschieden.', 'Marital status with “sein”: Ich bin verheiratet / ledig / geschieden.', 'Civil status gamit ang “sein”: Ich bin verheiratet / ledig / geschieden.'), [G3], R('verheiratet', 'ledig', 'geschieden'))
fam('SP4', STATUS, [('Sie sind verheiratet.', 'You are married.', 'Kasal ka.', 'Ja, ich bin verheiratet.', ['Ja, ich habe verheiratet.', 'Nein, ich bin verheiratet.']), ('Sie sind geschieden.', 'You are divorced.', 'Hiwalay ka.', 'Nein, ich bin geschieden.', ['Ja, ich bin geschieden.', 'Nein, ich habe geschieden.']), ('Sie sind ledig.', 'You are single.', 'Wala kang asawa.', 'Nein, ich bin ledig.', ['Ja, ich bin ledig.', 'Nein, ich habe ledig.'])],
    [('Sie heiraten bald, jetzt sind Sie ledig.', 'You marry soon; now you are single.', 'Ikakasal ka na, pero ngayon wala kang asawa.', 'Nein, noch nicht. Ich bin ledig.', ['Ja, ich bin ledig.', 'Nein, ich habe ledig.']), ('Sie sind seit 2010 verheiratet.', 'You have been married since 2010.', 'Kasal ka mula 2010.', 'Ja, seit 2010.', ['Nein, seit 2010.', 'Ja, ich habe seit 2010.']),
     ('Sie leben mit Ihrem Partner, ohne Ehe.', 'You live with your partner, not married.', 'Kasama mo ang partner mo, hindi kasal.', 'Nein, aber ich habe einen Partner.', ['Ja, ich habe einen Partner.', 'Nein, ich bin Partner.']), ('Sie sind verheiratet und haben Kinder.', 'You are married and have children.', 'Kasal ka at may mga anak.', 'Ja, und wir haben Kinder.', ['Nein, und wir haben Kinder.', 'Ja, ich habe verheiratet.'])])

DUSIE = lambda v, i: choice(i, 'sprechen', L(f'{v[0]} Was fragen Sie? Wählen Sie, dann sagen Sie es laut.', f'{v[1]} What do you ask? Choose, then say it aloud.', f'{v[2]} Ano ang itatanong mo? Pumili, tapos sabihin nang malakas.'), None, v[3], v[4],
                            E('„du“ → dein/deine; „Sie“ → Ihr/Ihre.', '“du” → dein/deine; “Sie” → Ihr/Ihre.', '“du” → dein/deine; “Sie” → Ihr/Ihre.'), [G2], R('dein', 'Ihr (Possessiv)'))
fam('SP5', DUSIE, [('Sie sprechen mit Ihrer Freundin (du).', 'You talk to your friend (du).', 'Kausap mo ang kaibigan mo (du).', 'Wie heißt deine Tochter?', ['Wie heißt Ihre Tochter?', 'Wie heißt dein Tochter?']),
                   ('Sie sprechen mit dem Lehrer (Sie).', 'You talk to the teacher (Sie).', 'Kausap mo ang guro (Sie).', 'Wie alt ist Ihr Sohn?', ['Wie alt ist dein Sohn?', 'Wie alt ist Ihre Sohn?']),
                   ('Sie sprechen mit einer Kollegin (Sie).', 'You talk to a colleague (Sie).', 'Kausap mo ang katrabaho (Sie).', 'Wo leben Ihre Eltern?', ['Wo leben deine Eltern?', 'Wo leben Ihr Eltern?'])],
    [('Sie sprechen mit Ihrem Bruder (du).', 'You talk to your brother (du).', 'Kausap mo ang kapatid mo (du).', 'Wie geht es deinem Sohn?', ['Wie geht es Ihrem Sohn?', 'Wie geht es dein Sohn?']), ('Sie sprechen mit Frau Huber (Sie).', 'You talk to Mrs Huber (Sie).', 'Kausap mo si Frau Huber (Sie).', 'Wie heißt Ihr Mann?', ['Wie heißt dein Mann?', 'Wie heißt Ihre Mann?']),
     ('Sie sprechen mit einem Kind (du).', 'You talk to a child (du).', 'Kausap mo ang isang bata (du).', 'Wie heißt deine Mutter?', ['Wie heißt Ihre Mutter?', 'Wie heißt dein Mutter?']), ('Sie sprechen mit Herrn Bauer (Sie).', 'You talk to Mr Bauer (Sie).', 'Kausap mo si Herr Bauer (Sie).', 'Wie heißen Ihre Kinder?', ['Wie heißen deine Kinder?', 'Wie heißen Ihr Kinder?'])])

PLC = lambda v, i: choice(i, 'grammatikWortschatz', CHOOSE, v[0], v[1], v[2], E(f'Plural: {v[1]}. Im Plural immer „die“.', f'Plural: {v[1]}. Plural article always “die”.', f'Plural: {v[1]}. Laging “die” sa plural.'), [G4], R(v[3]))
fam('GW1', PLC, [('der Vater → die …', 'Väter', ['Vaters', 'Vatern'], 'Vater'), ('die Familie → die …', 'Familien', ['Families', 'Familie'], 'Familie'), ('der Opa → die …', 'Opas', ['Opa', 'Omas'], 'Opa')],
    [('die Mutter → die …', 'Mütter', ['Mutters', 'Muttern'], 'Mutter'), ('das Kind → die …', 'Kinder', ['Kinds', 'Kinden'], 'Kind'), ('der Bruder → die …', 'Brüder', ['Bruders', 'Brudern'], 'Bruder'), ('die Frau → die …', 'Frauen', ['Fraus', 'Frau'], 'Frau')])

POS = lambda v, i: cloze(i, 'grammatikWortschatz', GAPS, v[0], [v[1]], E('mein/dein/Ihr vor der/das, meine/deine/Ihre vor die und Plural.', 'mein/dein/Ihr before der/das, meine/deine/Ihre before die and plural.', 'mein/dein/Ihr bago der/das, meine/deine/Ihre bago die at plural.'), [G2], R('mein', 'dein'))
fam('GW2', POS, [('Das ist {{1}} (mein) Tochter.', ['meine']), ('Wie heißt {{1}} (dein) Vater?', ['dein']), ('Frau Huber, wo leben {{1}} (Ihr) Kinder?', ['Ihre'])],
    [('Das sind {{1}} (mein) Großeltern.', ['meine']), ('Ist das {{1}} (dein) Bruder?', ['dein']), ('Herr Bauer, wie alt ist {{1}} (Ihr) Sohn?', ['Ihr']), ('Das ist {{1}} (mein) Baby.', ['mein'])])

VB = lambda v, i: cloze(i, 'grammatikWortschatz', GAPS, v[0], [v[1]], same(v[2]), [G5], R(v[3]))
fam('GW3', VB, [('Der Opa {{1}} (lesen) gern.', ['liest'], 'lesen: er liest (e → ie).', 'lesen'), ('Du {{1}} (sehen) deine Familie.', ['siehst'], 'sehen: du siehst (e → ie).', 'sehen'), ('Meine Tochter {{1}} (schreiben) eine Nachricht.', ['schreibt'], 'schreiben: sie schreibt.', 'schreiben')],
    [('Er {{1}} (sehen) die Kinder.', ['sieht'], 'sehen: er sieht.', 'sehen'), ('Du {{1}} (lesen) viel.', ['liest'], 'lesen: du liest.', 'lesen'), ('Wir {{1}} (bleiben) in Wien.', ['bleiben'], 'bleiben: wir bleiben.', 'bleiben'), ('Meine Eltern {{1}} (leben) in Manila.', ['leben'], 'leben: sie leben.', 'leben')])

RELQ = lambda v, i: choice(i, 'grammatikWortschatz', CHOOSE, v[0], v[1], v[2], same(v[3]), [G1], R('Familie'))
fam('GW4', RELQ, [('Der Vater von meinem Vater ist mein …', 'Opa', ['Bruder', 'Sohn'], 'Vater vom Vater = Opa.'), ('Die Tochter von meinen Eltern ist meine …', 'Schwester', ['Oma', 'Mutter'], 'Tochter der Eltern = Schwester.'), ('Mein Bruder und meine Schwester sind meine …', 'Geschwister', ['Eltern', 'Großeltern'], 'Bruder + Schwester = Geschwister.')],
    [('Die Mutter von meinem Vater ist meine …', 'Oma', ['Tochter', 'Schwester'], 'Mutter vom Vater = Oma.'), ('Der Sohn von meinen Eltern ist mein …', 'Bruder', ['Opa', 'Vater'], 'Sohn der Eltern = Bruder.'), ('Oma und Opa sind meine …', 'Großeltern', ['Geschwister', 'Kinder'], 'Oma + Opa = Großeltern.'), ('Mutter und Vater sind meine …', 'Eltern', ['Großeltern', 'Geschwister'], 'Mutter + Vater = Eltern.')])

WQ = lambda v, i: choice(i, 'werte', CHOOSE, v[0], v[1], [v[2]], WOW, [G6], R('Familie'))
fam('WE1', WQ, [('Eine Mutter lebt allein mit ihrem Kind. Ist das eine Familie?', 'Ja.', 'Nein.'), ('Zwei Väter leben mit einem Kind. Ist das eine Familie?', 'Ja.', 'Nein.'), ('Ein Paar hat keine Kinder. Ist das eine Familie?', 'Ja, auch ohne Kinder.', 'Nein, nur mit Kindern.')],
    [('Ein Vater lebt allein mit zwei Kindern. Ist das eine Familie?', 'Ja.', 'Nein.'), ('Zwei Mütter leben mit ihrer Tochter. Ist das eine Familie?', 'Ja.', 'Nein.')])
fam('WE2', WQ, [('Gibt es in Österreich nur eine Familienform?', 'Nein, es gibt viele Familienformen.', 'Ja, nur eine.'), ('Eine Patchwork-Familie ist …', 'eine Familie mit Kindern aus einer früheren Beziehung', 'eine Familie ohne Eltern'), ('Welcher Satz ist richtig?', 'Familien sind verschieden.', 'Alle Familien sind gleich groß.')],
    [('Hat eine Familie immer Kinder?', 'Nein.', 'Ja.'), ('Leben alle Familien gleich?', 'Nein, Familien leben verschieden.', 'Ja, alle gleich.')])
fam('WE3', lambda v, i: choice(i, 'werte', LOOK, v[0], v[1], [v[2]], WOW, [G6], R('Familie'), img=FAM()),
    [('Bild 3: zwei Männer mit Kind. Ist das eine Familie?', 'Ja.', 'Nein.'), ('Bild 2: In welchem Bild sind Vater, Mutter und Kind?', 'Bild 2', 'Bild 1'), ('Wie viele Familien zeigt das Bild?', 'drei', 'zwei')],
    [('Bild 1: Wie viele Erwachsene sind in Bild 1?', 'eine', 'zwei'), ('In welchem Bild sind zwei Väter?', 'Bild 3', 'Bild 1')])

fam('LE4', lambda v, i: choice(i, 'lesen', READ, v[0], v[1], [v[2]], same(v[3]), [G1, G3], R('Familie')),
    [], [('Herr Bauer ist 70. Seine Frau ist gestorben. Er lebt jetzt bei seiner Tochter.\nLebt Herr Bauer allein?', 'Nein, bei seiner Tochter.', 'Ja, allein.', 'Er lebt bei seiner Tochter.'),
         ('Anna und Tom heiraten bald. Sie sind sehr glücklich.\nSind Anna und Tom schon verheiratet?', 'Nein, noch nicht.', 'Ja.', 'Sie heiraten bald.'),
         ('Lena hat einen Bruder und zwei Schwestern.\nWie viele Geschwister hat Lena?', 'drei', 'zwei', '1 Bruder + 2 Schwestern = 3.'),
         ('Meine Großeltern leben in Wien, meine Eltern in Linz.\nWo leben die Eltern?', 'in Linz', 'in Wien', 'meine Eltern in Linz')])
fam('WE4', WQ, [], [('Ist eine Familie mit zwei Müttern in Österreich eine Familie?', 'Ja.', 'Nein.'), ('Eine Oma lebt mit ihrer Tochter und dem Baby. Ist das eine Familie?', 'Ja.', 'Nein.'),
                    ('Was ist eine Familie?', 'Menschen zusammen – in vielen Familienformen', 'nur Vater, Mutter und zwei Kinder'), ('Patchwork-Familie: Die Kinder kommen …', 'auch aus einer früheren Beziehung', 'immer aus dem Ausland'),
                    ('Eltern, Kinder und Oma wohnen zusammen. Ist das eine Familie?', 'Ja.', 'Nein.'), ('Sind alle Familien gleich groß?', 'Nein.', 'Ja.')])

write_svgs('/tmp/a1-04.png')
write_all(V, GOALS, {'lesen': 3, 'hoeren': 3, 'schreiben': 3, 'sprechen': 5, 'grammatikWortschatz': 3, 'werte': 3})
