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
def at(x, y, s, inner):
    """Draw `inner` in the same scaled frame as person(x, ..., y=y, s=s)."""
    return f'<g transform="translate({x} {y+260}) scale({s}) translate({-x} {-(y+260)})">{inner}</g>'


def tie(x, y, s):
    return at(x, y, s, f'<path d="M{x-5} {y+146}h10l-3 8 4 34-6 7-6-7 4-34z" fill="#c8102e"/>')


def glasses(x, y, s):
    return at(x, y, s, f'<g fill="none" stroke="#222" stroke-width="2.5"><circle cx="{x-9}" cy="{y+118}" r="8"/><circle cx="{x+9}" cy="{y+118}" r="8"/><path d="M{x-1} {y+118}h2"/></g>')


def bow(x, y, s):
    return at(x, y, s, f'<path d="M{x+16} {y+92}l-9-6v12zM{x+16} {y+92}l9-6v12z" fill="#e0457b"/><circle cx="{x+16}" cy="{y+92}" r="3" fill="#e0457b"/>')


def tag(x, y, text, w=76, hot=False):
    return (f'<rect x="{x-w/2}" y="{y}" width="{w}" height="24" rx="6" fill="{"#c8102e" if hot else "#fff"}" stroke="#c8102e" stroke-width="2"/>'
            + label(x, y + 17, text, 14, '#fff' if hot else '#1f2937'))


def tbox(cx, y, t, c, w=126):
    return f'<rect x="{cx-w/2}" y="{y}" width="{w}" height="34" rx="8" fill="#fff" stroke="{c}" stroke-width="3"/>' + label(cx, y + 22, t, 14)


# 1 family tree: three generations; blue = man, red = woman (Opa Franz, Oma Maria → Peter; Peter + Anna → Lukas, Lena)
PICS['stammbaum'] = (label(200, 26, 'Familie Huber', 18, '#c8102e')
                     + '<g stroke="#8a7a5a" stroke-width="3" fill="none"><path d="M162 61h76M200 61v29M100 90h100M100 90v26M162 133h76M200 133v29M100 162h200M100 162v26M300 162v26"/></g>'
                     + '<circle cx="200" cy="61" r="5" fill="#8a7a5a"/><circle cx="200" cy="133" r="5" fill="#8a7a5a"/>'
                     + tbox(100, 44, 'Opa Franz', '#34506b') + tbox(300, 44, 'Oma Maria', '#c8102e')
                     + tbox(100, 116, 'Vater Peter', '#34506b') + tbox(300, 116, 'Mutter Anna', '#c8102e')
                     + tbox(100, 188, 'Lukas (Bub)', '#34506b') + tbox(300, 188, 'Lena (Mädchen)', '#c8102e'))

# 2 Maria (centre, speaking) with brother Jose and sister Ana
PICS['geschwister'] = (person(80, '#1d4e89', 'b', '#222') + person(320, '#2a9d8f', 'b', '#222', long=True) + person(200, '#c8102e', 'b', '#222', long=True)
                       + bubble(70, 14, 260, 'Das sind meine Geschwister.', 16, tail_x=200)
                       + tag(80, 230, 'Jose') + tag(320, 230, 'Ana') + tag(200, 230, 'Maria', hot=True))

# 3 park: man, woman, boy, girl, baby in a pram (2 adults, 3 children)
PICS['park'] = ('<rect y="196" width="400" height="64" fill="#7cc36a"/><circle cx="352" cy="46" r="24" fill="#ffd23f"/>'
                + '<rect x="14" y="120" width="10" height="80" fill="#8a6a43"/><circle cx="19" cy="104" r="30" fill="#5aa65a"/>'
                + person(100, '#34506b', 'a', '#4a2f1c', y=-10, s=0.82) + tie(100, -10, 0.82)
                + person(185, '#c8102e', 'a', '#7a4e2d', y=-10, s=0.78, long=True)
                + person(250, '#2a9d8f', 'a', '#4a2f1c', y=-4, s=0.5)
                + person(298, '#e0457b', 'a', '#d9a066', y=-4, s=0.5, long=True) + bow(298, -4, 0.5)
                + '<g><path d="M330 226h56a0 0 0 0 1 0 0q0 22-28 22t-28-22z" fill="#9ed8ff" stroke="#34506b" stroke-width="3"/><path d="M330 226q0-26 28-26v26z" fill="#6fb6e8" stroke="#34506b" stroke-width="3"/>'
                + '<circle cx="372" cy="218" r="13" fill="#f1c9a5"/><path d="M360 214q12-14 24 0" fill="#fff" stroke="#c8102e" stroke-width="2"/><circle cx="368" cy="219" r="1.8" fill="#222"/><circle cx="376" cy="219" r="1.8" fill="#222"/>'
                + '<path d="M386 226l8-24" stroke="#34506b" stroke-width="3"/><circle cx="342" cy="252" r="6" fill="#444"/><circle cx="376" cy="252" r="6" fill="#444"/></g>')

# 4 plural: 3 children · 2 men · 4 women
PICS['plural'] = (panel(10, 20, 120, 220, 1) + panel(140, 20, 120, 220, 2) + panel(270, 20, 120, 220, 3)
                  + ''.join(person(x, c, 'a', '#4a2f1c', y=-45, s=0.45) for x, c in ((40, '#f77f00'), (70, '#2a9d8f'), (100, '#7a4e9a')))
                  + person(168, '#34506b', 'b', '#222', y=-45, s=0.6) + tie(168, -45, 0.6) + person(222, '#1f2937', 'a', '#7a4e2d', y=-45, s=0.6) + tie(222, -45, 0.6)
                  + ''.join(person(x, c, 'a', '#7a4e2d', y=-45, s=0.42, long=True) for x, c in ((296, '#c8102e'), (322, '#2a9d8f'), (348, '#f77f00'), (374, '#7a4e9a'))))

# 5 Lukas shows three framed photos on the wall: Mutter, Vater, Schwester
def frame(cx, n, who, shirt, hair, long, s, ties=False):
    return (f'<rect x="{cx-36}" y="86" width="72" height="84" rx="4" fill="#fff" stroke="#8a7a5a" stroke-width="5"/><rect x="{cx-31}" y="91" width="62" height="74" fill="#dfe9f3"/>'
            + person(cx, shirt, 'a', hair, y=-92, s=s, long=long) + (tie(cx, -92, s) if ties else '')
            + f'<rect x="{cx-31}" y="165" width="62" height="3" fill="#fff"/><circle cx="{cx-36}" cy="86" r="11" fill="#c8102e"/>' + label(cx - 36, 91, str(n), 13, '#fff') + label(cx, 192, who, 15))


PICS['foto'] = ('<rect y="64" width="400" height="136" fill="#fbf6ea"/><rect y="200" width="400" height="60" fill="#d9c3a3"/>'
                + person(52, '#2a9d8f', 'a', '#4a2f1c', y=-8, s=0.95) + label(52, 246, 'Lukas', 14, '#fff')
                + bubble(14, 12, 196, 'Das ist meine Familie.', 15, tail_x=52)
                + frame(140, 1, 'Mutter', '#c8102e', '#7a4e2d', True, 0.31)
                + frame(226, 2, 'Vater', '#34506b', '#4a2f1c', False, 0.31, True)
                + frame(312, 3, 'Schwester', '#e0457b', '#d9a066', True, 0.27))

# 6 form (pool facts: Name Sofia Berger, three boxes, "verheiratet" ticked, no "Kinder" line)
PICS['formular'] = ('<rect x="40" y="20" width="320" height="220" rx="8" fill="#fff" stroke="#9ca3af" stroke-width="2"/><rect x="40" y="20" width="320" height="40" rx="8" fill="#c8102e"/><rect x="40" y="44" width="320" height="16" fill="#c8102e"/>'
                    + label(200, 47, 'Familienstand', 20, '#fff')
                    + label(70, 86, 'Name: Sofia Berger', 15, anchor='start', bold=False)
                    + ''.join(f'<rect x="80" y="{y}" width="24" height="24" fill="#fff" stroke="#1f2937" stroke-width="2"/>' + label(120, y + 19, t, 17, anchor='start', bold=False)
                              for y, t in ((106, 'ledig'), (146, 'verheiratet'), (186, 'geschieden')))
                    + '<path d="M84 150l16 16M100 150l-16 16" stroke="#c8102e" stroke-width="4"/>')

# 7 four verbs as four scenes: 1 sehen · 2 hören · 3 lesen · 4 schreiben
_P = lambda x0, c, hair='#4a2f1c', long=False: person(x0 + 44, c, 'a', hair, y=-40, s=0.62, long=long)
PICS['verben'] = (panel(10, 20, 88, 220, 1) + panel(108, 20, 88, 220, 2) + panel(206, 20, 88, 220, 3) + panel(304, 20, 88, 220, 4)
                  # 1 sehen: person looks at a tree (dashed line of sight)
                  + _P(10, '#34506b') + '<path d="M66 128L76 100" stroke="#8a7a5a" stroke-width="2.5" stroke-dasharray="5 4"/>'
                  + '<rect x="75" y="64" width="9" height="34" fill="#8a6a43"/><circle cx="79" cy="52" r="20" fill="#5aa65a"/>'
                  # 2 hören: headphones + music notes
                  + _P(108, '#c8102e', long=True) + '<path d="M130 134q22-36 44 0" stroke="#222" stroke-width="5" fill="none"/><rect x="127" y="126" width="9" height="18" rx="4" fill="#222"/><rect x="168" y="126" width="9" height="18" rx="4" fill="#222"/>'
                  + '<g fill="#1d4e89"><circle cx="134" cy="92" r="6"/><path d="M140 92v-26h12" stroke="#1d4e89" stroke-width="3.5" fill="none"/><circle cx="170" cy="76" r="6"/><path d="M176 76v-26h12" stroke="#1d4e89" stroke-width="3.5" fill="none"/></g>'
                  # 3 lesen: open book held in front
                  + _P(206, '#2a9d8f') + '<path d="M228 168l22 6 22-6v38l-22 6-22-6z" fill="#fff" stroke="#1d4e89" stroke-width="3"/><path d="M250 174v38M234 176l11 3M234 184l11 3M234 192l11 3M255 179l11-3M255 187l11-3M255 195l11-3" stroke="#1d4e89" stroke-width="2"/>'
                  # 4 schreiben: pencil over a sheet
                  + _P(304, '#7a4e9a', long=True) + '<rect x="324" y="172" width="48" height="38" rx="2" fill="#fff" stroke="#9ca3af" stroke-width="2.5"/><path d="M331 184h34M331 193h34M331 202h20" stroke="#1d4e89" stroke-width="2"/>'
                  + '<path d="M370 150l-12 30" stroke="#f2c14e" stroke-width="8" stroke-linecap="round"/><path d="M358 180l-1.5 8 7-4z" fill="#1f2937"/>')

# 8 wedding: arch with flowers, groom Peter, bride Anna with veil, bouquet, hearts
PICS['hochzeit'] = ('<path d="M60 260V110q0-80 140-80t140 80v150" fill="none" stroke="#7cc36a" stroke-width="12"/>'
                    + ''.join(f'<circle cx="{x}" cy="{y}" r="6" fill="{c}"/>' for x, y, c in ((74, 150, '#e0457b'), (66, 100, '#fff'), (92, 62, '#e0457b'), (140, 38, '#fff'), (200, 30, '#e0457b'), (262, 38, '#fff'), (310, 62, '#e0457b'), (334, 100, '#fff'), (326, 150, '#e0457b')))
                    + person(145, '#1f2937', 'a', '#4a2f1c') + '<path d="M133 156l12 36 12-36z" fill="#fff"/><path d="M137 160l8 5 8-5v10l-8-5-8 5z" fill="#c8102e"/>'
                    + person(255, '#fff', 'a', '#7a4e2d', long=True) + '<path d="M215 260v-60q0-44 40-44t40 44v60z" fill="none" stroke="#c4ccd6" stroke-width="2"/>'
                                        + '<path d="M223 172L225 112q30-52 60 0L287 172z" fill="#fff" opacity="0.7" stroke="#c4ccd6" stroke-width="1.5"/>'
                    + '<g><circle cx="200" cy="232" r="9" fill="#e0457b"/><circle cx="189" cy="238" r="8" fill="#fff" stroke="#e0457b" stroke-width="1.5"/><circle cx="211" cy="238" r="8" fill="#ffd23f"/><path d="M200 241v18" stroke="#5aa65a" stroke-width="3"/></g>'
                    + ''.join(f'<path d="M{x} {y}c-6-10-20-4-14 6l14 12 14-12c6-10-8-16-14-6z" fill="#c8102e"/>' for x, y in ((200, 12), (30, 40), (370, 40)))
                    + tag(145, 232, 'Peter') + tag(255, 232, 'Anna'))

# 9 family gathering: Opa, Oma (grey hair, glasses), Lena, Lukas, Sara (a friend) → 5 people, 2 grandparents
GREY = '#c9ced3'
PICS['leute'] = ('<rect y="196" width="400" height="64" fill="#d9c3a3"/>'
                 + person(50, '#7a4e9a', 'a', GREY, y=-45, s=0.62) + glasses(50, -45, 0.62)
                 + person(125, '#e0457b', 'a', GREY, y=-45, s=0.62, long=True) + glasses(125, -45, 0.62)
                 + person(200, '#f77f00', 'a', '#4a2f1c', y=-45, s=0.5, long=True) + bow(200, -45, 0.5)
                 + person(275, '#2a9d8f', 'a', '#4a2f1c', y=-45, s=0.5)
                 + person(350, '#1d4e89', 'c', '#222', y=-45, s=0.62, long=True)
                 + bubble(160, 14, 150, 'Hallo, Leute!', 16, tail_x=275)
                 + ''.join(tag(x, 224, t, 66) for x, t in ((50, 'Opa'), (125, 'Oma'), (200, 'Lena'), (275, 'Lukas'), (350, 'Sara'))))

# 10 three families: 1 mother + child · 2 father, mother, child · 3 grandma + child (pool facts, see WE3)
PICS['familien'] = (panel(10, 20, 120, 220, 1) + panel(140, 20, 120, 220, 2) + panel(270, 20, 120, 220, 3)
                    + person(52, '#c8102e', 'a', '#7a4e2d', y=-40, s=0.62, long=True) + person(100, '#f77f00', 'a', '#4a2f1c', y=-40, s=0.42)
                    + person(166, '#34506b', 'a', '#4a2f1c', y=-40, s=0.56) + person(210, '#c8102e', 'b', '#222', y=-40, s=0.56, long=True) + person(244, '#2a9d8f', 'b', '#222', y=-40, s=0.38)
                    + person(318, '#7a4e9a', 'a', GREY, y=-40, s=0.62, long=True) + glasses(318, -40, 0.62) + person(362, '#f77f00', 'b', '#222', y=-40, s=0.42)
                    + tag(52, 216, 'Mutter', 58) + tag(168, 216, 'Vater', 48) + tag(222, 216, 'Mutter', 58) + tag(318, 216, 'Oma', 48))

STAMM = lambda: img('stammbaum', 'Ein Stammbaum der Familie Huber mit Großeltern, Eltern und Kindern.', 'A family tree of the Huber family with grandparents, parents and children.', 'Family tree ng pamilyang Huber: lolo at lola, magulang at mga anak.')
FORM = lambda: img('formular', 'Ein Formular mit Name und Familienstand. Ein Feld ist angekreuzt.', 'A form with a name and marital status. One box is ticked.', 'Form na may pangalan at civil status. May isang kahong may ekis.')
FAM = lambda: img('familien', 'Drei Bilder mit drei Familien: Frau mit Kind; Mann, Frau und Kind; Frau mit grauen Haaren und Kind.', 'Three pictures with three families: a woman and a child; a man, a woman and a child; a grey-haired woman and a child.', 'Tatlong larawan ng tatlong pamilya: babae at bata; lalaki, babae at bata; babaeng may puting buhok at bata.')

# ---------------------------------------------------------------- lessons (content standard v2: intro + cards + 6–8 items)
X = ''
SEE = L('Schauen Sie das Bild an.', 'Look at the picture.', 'Tingnan ang larawan.')
WOW = L('In Österreich gibt es verschiedene Familienformen: Eltern mit Kindern, Paare ohne Kinder, eine Mutter oder ein Vater allein mit Kindern, Großeltern mit Enkelkindern, Patchwork-Familien.',
        'In Austria there are different family forms: parents with children, couples without children, a mother or father alone with children, grandparents with grandchildren, patchwork families.',
        'Sa Austria may iba’t ibang anyo ng pamilya: magulang na may anak, mag-asawang walang anak, nanay o tatay na mag-isang may anak, lolo at lola kasama ang apo, patchwork.')

# L01 ------------------------------------------------------------------ Die Familie
lesson(1, L('Die Familie', 'The family', 'Ang pamilya'), ['Familie', 'Mutter', 'Vater', 'Eltern', 'Sohn', 'Tochter', 'Kind'], [
    PHRASE('Das ist meine Familie. Das ist meine Mutter, das ist mein Vater.', 'So zeigen Sie Ihre Familie. „meine Mutter“ und „mein Vater“ lernen Sie zuerst als feste Wörter, Lektion 5 erklärt sie.',
           'This is how you introduce your family. Learn “meine Mutter” and “mein Vater” as fixed phrases first; lesson 5 explains them.',
           'Ganito mo ipakilala ang pamilya mo. Isaulo muna ang “meine Mutter” at “mein Vater” bilang buong parirala; ipapaliwanag ito sa lesson 5.'),
    RULE('Mutter + Vater = die Eltern', 'Die Eltern sind Mutter und Vater zusammen. „Eltern“ gibt es nur im Plural: die Eltern (nicht „der Eltern“).',
         'The parents are mother and father together. “Eltern” only exists in the plural: die Eltern.',
         'Ang Eltern ay nanay at tatay na magkasama. Plural lang ang “Eltern”: die Eltern.',
         ['Anna ist die Mutter. Peter ist der Vater.', 'Anna und Peter sind die Eltern.']),
    RULE('der Sohn · die Tochter · das Kind', 'Sohn = Bub, Tochter = Mädchen. „das Kind“ ist beides: Sohn und Tochter sind Kinder. Das Wort „Kind“ hat den Artikel „das“.',
         'Sohn = boy, Tochter = girl. “das Kind” is both: son and daughter are children. “Kind” takes “das”.',
         'Sohn = lalaki, Tochter = babae. Ang “das Kind” ay para sa dalawa: ang anak na lalaki at babae ay Kinder. “das” ang article ng “Kind”.',
         ['Lukas ist der Sohn.', 'Lena ist die Tochter.', 'Lukas und Lena sind die Kinder.']),
    PHRASE('Haben Sie Kinder? – Ja, ich habe zwei Kinder.', 'Mit „haben“ sagen Sie, wie viele Kinder Sie haben. „Ich bin zwei Kinder“ geht nicht: „sein“ sagt, wer Sie sind.',
           'With “haben” you say how many children you have. “Ich bin zwei Kinder” is wrong: “sein” says who you are.',
           'Gamit ang “haben” sinasabi mo kung ilan ang anak mo. Mali ang “Ich bin zwei Kinder”: ang “sein” ay para sa kung sino ka.'),
], [
    choice(X, 'lesen', L('Anna Huber zeigt ihren Stammbaum. Schauen Sie das Bild an.', 'Anna Huber shows her family tree. Look at the picture. The lines go from the parents down to their children.', 'Ipinapakita ni Anna Huber ang family tree niya. Tingnan ang larawan. Ang mga linya ay mula sa magulang pababa sa mga anak.'),
           'Lukas und Lena haben eine Mutter. Wie heißt sie?', 'Anna', ['Maria', 'Lena'],
           L('Richtig: Anna. Von Peter und Anna führt die Linie zu Lukas und Lena: Anna ist die Mutter. Maria steht in der Zeile darüber: Maria ist die Oma. Lena ist ein Kind, nicht die Mutter.',
             'Correct: Anna. The line goes from Peter and Anna down to Lukas and Lena: Anna is the mother. Maria is in the row above: she is the grandmother. Lena is a child, not the mother.',
             'Tama: Anna. Ang linya ay mula kina Peter at Anna pababa kina Lukas at Lena: nanay si Anna. Si Maria ay nasa itaas na hanay: lola siya. Anak si Lena, hindi nanay.'),
           [G1], R('Mutter', 'Kind'), img=STAMM()),
    choice(X, 'lesen', L('Schauen Sie den Stammbaum noch einmal an. Die Kinder heißen Lukas und Lena.', 'Look at the family tree again. The children are Lukas and Lena.', 'Tingnan muli ang family tree. Sina Lukas at Lena ang mga anak.'),
           'Wer ist die Tochter, Lukas oder Lena?', 'Lena', ['Lukas'],
           L('Richtig: Lena. Im Stammbaum steht „Lena (Mädchen)“: Mädchen = Tochter. Lukas ist ein Bub: der Sohn.',
             'Correct: Lena. The tree says “Lena (Mädchen)”: girl = daughter. Lukas is a boy: the son.',
             'Tama: Lena. Nakasulat sa family tree ang “Lena (Mädchen)”: babae = Tochter. Lalaki si Lukas (Bub): ang Sohn.'),
           [G1], R('Tochter', 'Sohn'), img=STAMM()),
    choice(X, 'hoeren', L('Lena stellt ihre Familie vor. Hören Sie.', 'Lena introduces her family. Listen.', 'Ipinakikilala ni Lena ang pamilya niya. Makinig.'),
           'Wie heißt die Mutter?', 'Anna', ['Peter', 'Lena'],
           L('Sie hören: „Hallo! Ich bin Lena. Das ist mein Vater Peter und das ist meine Mutter Anna.“ Peter ist der Vater, Lena spricht – sie ist das Kind. Die Mutter heißt Anna.',
             'You hear: “Hallo! Ich bin Lena. Das ist mein Vater Peter und das ist meine Mutter Anna.” Peter is the father, Lena is speaking – she is the child. The mother is Anna.',
             'Naririnig mo: “Hallo! Ich bin Lena. Das ist mein Vater Peter und das ist meine Mutter Anna.” Tatay si Peter, si Lena ang nagsasalita – anak siya. Anna ang nanay.'),
           [G1], R('Mutter', 'Vater'), audio='Hallo! Ich bin Lena. Das ist mein Vater Peter und das ist meine Mutter Anna.'),
    cloze(X, 'grammatikWortschatz', L('Lena ist acht Jahre alt. Ergänzen Sie, was Lena sagt. Nehmen Sie die Wörter unten.', 'Lena is eight years old. Complete what Lena says. Use the words below.', 'Walong taong gulang si Lena. Kumpletuhin ang sinasabi ni Lena. Gamitin ang mga salita sa ibaba.'),
          'Peter ist mein {{1}}. Anna ist meine {{2}}. Peter und Anna sind meine {{3}}.', [['Vater'], ['Mutter'], ['Eltern']],
          L('Richtig: Vater, Mutter, Eltern. Lena ist das Kind – darum sind Peter und Anna ihre Eltern. „Kinder“ passt nicht: Lena ist selbst ein Kind, ihre Eltern sind keine Kinder.',
            'Correct: Vater, Mutter, Eltern. Lena is the child – so Peter and Anna are her parents. “Kinder” does not fit: Lena is a child herself, her parents are not.',
            'Tama: Vater, Mutter, Eltern. Anak si Lena – kaya magulang niya sina Peter at Anna. Hindi bagay ang “Kinder”: bata si Lena mismo, hindi ang magulang niya.'),
          [G1], R('Vater', 'Mutter', 'Eltern'), bank=['Vater', 'Mutter', 'Eltern', 'Kinder']),
    choice(X, 'grammatikWortschatz', L('Anna spricht über ihren Sohn Lukas. Er ist ein Bub. Was sagt sie?', 'Anna talks about her son Lukas. He is a boy. What does she say?', 'Nagsasalita si Anna tungkol sa anak niyang si Lukas. Lalaki siya. Ano ang sinasabi niya?'),
           'Lukas ist mein …', 'Sohn', ['Tochter', 'Vater'],
           L('Richtig: Sohn. Lukas ist ein Bub, also männlich: der Sohn. „Tochter“ ist ein Mädchen (die Tochter) und braucht „meine“. „Vater“ ist Peter, nicht Lukas.',
             'Correct: Sohn. Lukas is a boy, so masculine: der Sohn. “Tochter” is a girl (die Tochter) and needs “meine”. “Vater” is Peter, not Lukas.',
             'Tama: Sohn. Lalaki si Lukas, kaya panlalaki: der Sohn. Ang “Tochter” ay babae (die Tochter) at kailangan ng “meine”. Si Peter ang “Vater”, hindi si Lukas.'),
           [G1], R('Sohn')),
    choice(X, 'sprechen', L('Eine Frau in Wien fragt Sie. Sie haben zwei Kinder. Was antworten Sie? Wählen Sie, dann sagen Sie es laut.', 'A woman in Vienna asks you. You have two children. What do you answer? Choose, then say it aloud.', 'Nagtanong sa iyo ang isang babae sa Vienna. May dalawa kang anak. Ano ang sagot mo? Pumili, tapos sabihin nang malakas.'),
           'Frau: „Haben Sie Kinder?“', 'Ja, ich habe zwei Kinder.', ['Ja, ich bin zwei Kinder.', 'Nein, ich habe zwei Kinder.'],
           L('Richtig: „Ja, ich habe zwei Kinder.“ Wer Kinder hat, sagt „haben“. „Ich bin zwei Kinder“ heißt: Ich selbst bin zwei Kinder – das ist falsch. „Nein“ passt nicht zu „zwei Kinder“: Auf „Haben Sie Kinder?“ mit zwei Kindern sagen Sie „Ja“.',
             'Correct: “Ja, ich habe zwei Kinder.” Use “haben” for your children. “Ich bin zwei Kinder” would mean I myself am two children – wrong. “Nein” does not fit “two children”: you answer “Haben Sie Kinder?” with “Ja”.',
             'Tama: “Ja, ich habe zwei Kinder.” “Haben” ang gamit para sa mga anak mo. Ang “Ich bin zwei Kinder” ay ako mismo ang dalawang bata – mali. Hindi bagay ang “Nein” sa “zwei Kinder”: “Ja” ang sagot sa “Haben Sie Kinder?”.'),
           [G1], R('Kind', 'haben')),
    choice(X, 'lesen', L('Lukas schreibt an Tom. Lesen Sie die E-Mail.', 'Lukas writes an e-mail to Tom. Read it.', 'Sumulat si Lukas ng e-mail kay Tom. Basahin ito.'),
           'Servus Tom! Wir sind vier: mein Vater Peter, meine Mutter Anna, meine Schwester Lena und ich. Servus, Lukas\n\nWie viele Kinder sind in der Familie?', 'zwei', ['drei', 'vier'],
           L('Richtig: zwei. Die Kinder sind Lukas und Lena. Peter und Anna sind die Eltern, keine Kinder. „vier“ sind alle Menschen zusammen, „drei“ wären Lena und die Eltern.',
             'Correct: zwei. The children are Lukas and Lena. Peter and Anna are the parents. “vier” is everyone together; “drei” would be Lena and the parents.',
             'Tama: zwei. Ang mga anak ay sina Lukas at Lena. Magulang sina Peter at Anna. Ang “vier” ay lahat ng tao; ang “drei” ay si Lena at ang mga magulang.'),
           [G1], R('Kind', 'Eltern')),
], intro=INTRO(L('Anna wohnt in Wien. Sie zeigt Ihnen die Familie Huber: Vater, Mutter und zwei Kinder.',
                 'Anna lives in Vienna. She shows you the Huber family: father, mother and two children.',
                 'Nakatira si Anna sa Vienna. Ipinapakita niya sa iyo ang pamilyang Huber: tatay, nanay at dalawang anak.'),
               L('Am Ende kannst du Familienmitglieder nennen: Mutter, Vater, Sohn, Tochter, Eltern, Kinder.',
                 'By the end you can name family members: mother, father, son, daughter, parents, children.',
                 'Sa dulo, mapapangalanan mo ang mga miyembro ng pamilya: nanay, tatay, anak na lalaki, anak na babae, magulang, mga anak.')))

# L02 ------------------------------------------------------------------ Geschwister
lesson(2, L('Geschwister', 'Siblings', 'Magkakapatid'), ['Bruder', 'Schwester', 'Geschwister'], [
    PHRASE('Hast du Geschwister? – Ja, ich habe einen Bruder und eine Schwester.', 'So fragen Sie einen Freund (du) nach den Geschwistern. Die Antwort: „Ja, ich habe …“ und die Zahl oder Bruder und Schwester.',
           'This is how you ask a friend (du) about siblings. The answer: “Ja, ich habe …” plus a number or brother and sister.',
           'Ganito ka magtatanong sa kaibigan (du) tungkol sa kapatid. Ang sagot: “Ja, ich habe …” at bilang o kapatid na lalaki at babae.'),
    RULE('der Bruder · die Schwester · die Geschwister', 'Bruder = männlich, Schwester = weiblich. „die Geschwister“ sind Brüder und Schwestern zusammen. Das Wort gibt es nur im Plural.',
         'Bruder = male, Schwester = female. “die Geschwister” are brothers and sisters together. The word only exists in the plural.',
         'Bruder = lalaki, Schwester = babae. Ang “die Geschwister” ay magkapatid na lalaki at babae. Plural lang ang salita.',
         ['Jose ist der Bruder.', 'Ana ist die Schwester.', 'Maria hat zwei Geschwister.']),
    RULE('Ich habe einen Bruder. · Ich habe eine Schwester.', 'Nach „haben“ wird „ein“ bei männlichen Wörtern zu „einen“: einen Bruder. Bei „die“-Wörtern bleibt es „eine“: eine Schwester. Lernen Sie es als feste Wendung.',
         'After “haben”, “ein” becomes “einen” for masculine words: einen Bruder. For “die” words it stays “eine”: eine Schwester. Learn it as a fixed phrase.',
         'Pagkatapos ng “haben”, ang “ein” ay nagiging “einen” sa panlalaki: einen Bruder. Sa “die” na salita, “eine” pa rin: eine Schwester. Isaulo bilang buong parirala.',
         ['Ich habe einen Bruder.', 'Ich habe eine Schwester.', 'Wir haben zwei Kinder.']),
], [
    choice(X, 'lesen', L('Maria zeigt ihre Geschwister. Schauen Sie das Bild an: Maria spricht.', 'Maria shows her siblings. Look at the picture: Maria is the one speaking.', 'Ipinapakilala ni Maria ang mga kapatid niya. Tingnan ang larawan: si Maria ang nagsasalita.'),
           'Wie viele Geschwister hat Maria?', 'zwei', ['drei', 'eins'],
           L('Richtig: zwei – Jose und Ana. Maria spricht und steht in der Mitte: Sie ist keine Schwester von sich selbst. „drei“ zählt Maria mit, das ist falsch.',
             'Correct: zwei – Jose and Ana. Maria is speaking, in the middle: she does not count herself. “drei” counts Maria too – wrong.',
             'Tama: zwei – sina Jose at Ana. Si Maria ang nagsasalita sa gitna: hindi niya binibilang ang sarili niya. Ang “drei” ay kasama si Maria – mali.'),
           [G1], R('Geschwister'),
           img=img('geschwister', 'Eine junge Frau in der Mitte sagt „Das sind meine Geschwister.“ Links und rechts steht je ein Mensch mit Namensschild.', 'A young woman in the middle says “Das sind meine Geschwister.” A person with a name tag stands on each side.', 'Isang dalaga sa gitna ang nagsasabi ng “Das sind meine Geschwister.” May taong may name tag sa magkabilang gilid.')),
    choice(X, 'lesen', L('Schauen Sie das Bild noch einmal an.', 'Look at the picture again.', 'Tingnan muli ang larawan.'),
           'Wer ist der Bruder?', 'Jose', ['Ana', 'Maria'],
           L('Richtig: Jose. Ein Bruder ist männlich: Jose. Ana und Maria sind Frauen – Ana ist die Schwester, Maria spricht.',
             'Correct: Jose. A brother is male: Jose. Ana and Maria are women – Ana is the sister, Maria is the speaker.',
             'Tama: Jose. Panlalaki ang Bruder: si Jose. Babae sina Ana at Maria – si Ana ang Schwester, si Maria ang nagsasalita.'),
           [G1], R('Bruder'),
           img=img('geschwister', 'Eine junge Frau in der Mitte sagt „Das sind meine Geschwister.“ Links und rechts steht je ein Mensch mit Namensschild.', 'A young woman in the middle says “Das sind meine Geschwister.” A person with a name tag stands on each side.', 'Isang dalaga sa gitna ang nagsasabi ng “Das sind meine Geschwister.” May taong may name tag sa magkabilang gilid.')),
    choice(X, 'hoeren', L('Jose stellt sich vor. Hören Sie.', 'Jose introduces himself. Listen.', 'Nagpapakilala si Jose. Makinig.'),
           'Wie viele Geschwister hat Jose?', 'drei', ['zwei', 'vier'],
           L('Sie hören: „Ich bin Jose. Ich habe einen Bruder und zwei Schwestern.“ 1 + 2 = drei Geschwister. „zwei“ sind nur die Schwestern, „vier“ zählt Jose selbst mit.',
             'You hear: “Ich bin Jose. Ich habe einen Bruder und zwei Schwestern.” 1 + 2 = three siblings. “zwei” is only the sisters; “vier” counts Jose himself.',
             'Naririnig mo: “Ich bin Jose. Ich habe einen Bruder und zwei Schwestern.” 1 + 2 = tatlong kapatid. Ang “zwei” ay ang mga kapatid na babae lang; ang “vier” ay kasama si Jose.'),
           [G1], R('Geschwister', 'Bruder', 'Schwester'), audio='Ich bin Jose. Ich habe einen Bruder und zwei Schwestern.'),
    cloze(X, 'grammatikWortschatz', L('Anna fragt Maria. Ergänzen Sie den Dialog. Nehmen Sie die Wörter unten.', 'Anna asks Maria. Complete the dialogue. Use the words below.', 'Nagtanong si Anna kay Maria. Kumpletuhin ang dialogo. Gamitin ang mga salita sa ibaba.'),
          'Anna: Hast du {{1}}? – Maria: Ja, ich habe einen {{2}} und eine {{3}}.', [['Geschwister'], ['Bruder'], ['Schwester']],
          L('Richtig: Geschwister, Bruder, Schwester. „einen“ gehört zu einem männlichen Wort: einen Bruder. „eine“ gehört zu „die Schwester“. „Eltern“ passt nicht zu der Antwort: Maria spricht über Bruder und Schwester.',
            'Correct: Geschwister, Bruder, Schwester. “einen” goes with a masculine word: einen Bruder. “eine” goes with “die Schwester”. “Eltern” does not fit the answer: Maria talks about a brother and a sister.',
            'Tama: Geschwister, Bruder, Schwester. Ang “einen” ay para sa panlalaking salita: einen Bruder. Ang “eine” ay para sa “die Schwester”. Hindi bagay ang “Eltern”: tungkol sa kapatid na lalaki at babae ang sagot ni Maria.'),
          [G1], R('Geschwister', 'Bruder', 'Schwester'), bank=['Geschwister', 'Bruder', 'Schwester', 'Eltern']),
    choice(X, 'grammatikWortschatz', L('Tom spricht über seinen Bruder. Wählen Sie die richtige Form.', 'Tom talks about his brother. Choose the right form.', 'Nagsasalita si Tom tungkol sa kapatid niyang lalaki. Piliin ang tamang anyo.'),
           'Tom: „Ich habe … Bruder.“', 'einen', ['eine', 'ein'],
           L('Richtig: einen Bruder. Nach „haben“ wird „ein“ bei „der Bruder“ zu „einen“. „eine“ gehört zu „die“-Wörtern (eine Schwester). „ein Bruder“ sagt man nur bei „Das ist ein Bruder.“',
             'Correct: einen Bruder. After “haben”, “ein” becomes “einen” for “der Bruder”. “eine” belongs to “die” words (eine Schwester). “ein Bruder” is only used in “Das ist ein Bruder.”',
             'Tama: einen Bruder. Pagkatapos ng “haben”, ang “ein” ay nagiging “einen” sa “der Bruder”. Ang “eine” ay para sa “die” na salita (eine Schwester). Ang “ein Bruder” ay sa “Das ist ein Bruder.” lang.'),
           [G1], R('Bruder', 'haben')),
    choice(X, 'sprechen', L('Im Kurs fragt ein Freund Sie: „Hast du Geschwister?“ Sie haben eine Schwester. Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'In class a friend asks you: “Hast du Geschwister?” You have one sister. What do you say? Choose, then say it aloud.', 'Sa klase, tinanong ka ng kaibigan: “Hast du Geschwister?” May isa kang kapatid na babae. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'),
           'Freund: „Hast du Geschwister?“', 'Ja, ich habe eine Schwester.', ['Ja, ich bin eine Schwester.', 'Ja, ich habe einen Schwester.'],
           L('Richtig: „Ja, ich habe eine Schwester.“ „haben“ + „eine Schwester“ (die-Wort). „Ich bin eine Schwester“ sagt, was Sie selbst sind. „einen Schwester“ ist falsch: „einen“ gibt es nur bei männlichen Wörtern.',
             'Correct: “Ja, ich habe eine Schwester.” “haben” + “eine Schwester” (a “die” word). “Ich bin eine Schwester” says what you yourself are. “einen Schwester” is wrong: “einen” is only for masculine words.',
             'Tama: “Ja, ich habe eine Schwester.” “haben” + “eine Schwester” (“die” na salita). Ang “Ich bin eine Schwester” ay kung ano ka mismo. Mali ang “einen Schwester”: ang “einen” ay para lang sa panlalaking salita.'),
           [G2], R('Schwester', 'haben')),
    choice(X, 'lesen', L('Maria schreibt eine E-Mail. Lesen Sie.', 'Maria writes an e-mail. Read it.', 'Sumulat si Maria ng e-mail. Basahin ito.'),
           'Servus! Ich heiße Maria. Ich habe einen Bruder: Jose. Er wohnt in Graz. Meine Schwester heißt Ana. Sie wohnt in Wien.\n\nWer wohnt in Graz?', 'Jose', ['Ana', 'Maria'],
           L('Im Text: „Ich habe einen Bruder: Jose. Er wohnt in Graz.“ „Er“ ist Jose. Ana wohnt in Wien, Maria schreibt die E-Mail.',
             'The text says: “Ich habe einen Bruder: Jose. Er wohnt in Graz.” “Er” is Jose. Ana lives in Vienna; Maria is the writer.',
             'Sabi sa teksto: “Ich habe einen Bruder: Jose. Er wohnt in Graz.” Si Jose ang “Er”. Si Ana ay nakatira sa Wien; si Maria ang sumulat.'),
           [G1], R('Bruder', 'wohnen')),
], intro=INTRO(L('Maria kommt aus den Philippinen. Sie wohnt jetzt in Wien. Ihr Bruder Jose und ihre Schwester Ana sind auch da.',
                 'Maria is from the Philippines. She now lives in Vienna. Her brother Jose and her sister Ana are there too.',
                 'Taga-Pilipinas si Maria. Nakatira na siya ngayon sa Vienna. Nandoon din ang kuya/kapatid niyang si Jose at ang kapatid niyang si Ana.'),
               L('Am Ende kannst du sagen, ob du Geschwister hast, und Bruder und Schwester nennen.',
                 'By the end you can say whether you have siblings and name brother and sister.',
                 'Sa dulo, masasabi mo kung may kapatid ka at mapapangalanan mo ang kapatid na lalaki at babae.')))

# L03 ------------------------------------------------------------------ Mann, Frau, Kind, Baby
lesson(3, L('Mann, Frau, Kind, Baby', 'Man, woman, child, baby', 'Lalaki, babae, bata, sanggol'), ['Mann', 'Mädchen', 'Bub', 'Baby', 'Erwachsene', 'Jugendliche', 'Dame'], [
    RULE('der Mann · die Frau · das Baby', 'Mann und Frau sind Erwachsene. Ein Baby ist ein sehr kleines Kind. Das Wort „Baby“ hat den Artikel „das“.',
         'Man and woman are adults (Erwachsene). A baby is a very small child. “Baby” takes “das”.',
         'Ang lalaki at babae ay Erwachsene (nasa hustong gulang). Ang baby ay napakaliit na bata. “das” ang article ng “Baby”.',
         ['Das ist ein Mann.', 'Das ist eine Frau.', 'Das ist ein Baby.']),
    RULE('das Mädchen – auch bei einem Mädchen „das“', 'Alle Wörter auf -chen haben den Artikel „das“, auch wenn der Mensch weiblich ist: das Mädchen, ein Mädchen (nicht „eine“).',
         'All words ending in -chen take “das”, even if the person is female: das Mädchen, ein Mädchen (not “eine”).',
         'Lahat ng salitang nagtatapos sa -chen ay “das”, kahit babae ang tao: das Mädchen, ein Mädchen (hindi “eine”).',
         ['Das ist ein Mädchen.', 'Das Mädchen ist sieben Jahre alt.']),
    CULTURE('der Bub (in Deutschland: der Junge)', 'In Österreich sagen die Menschen „der Bub“ für ein männliches Kind, in Deutschland sagt man „der Junge“. Im Alltag hören Sie bei uns also: Bub und Mädchen.',
            'In Austria people say “der Bub” for a male child; in Germany people say “der Junge”. In everyday Austrian speech you hear: Bub and Mädchen.',
            'Sa Austria, “der Bub” ang tawag sa batang lalaki; sa Germany, “der Junge”. Sa araw-araw na usapan sa Austria maririnig mo: Bub at Mädchen.'),
    RULE('Erwachsene und Kinder', 'Erwachsene sind große Menschen: Mann, Frau. Kinder sind Baby, Bub, Mädchen. Jugendliche sind Menschen zwischen Kind und Erwachsener. „Dame“ ist ein höfliches Wort für „Frau“.',
         'Erwachsene (adults) are grown-up people: man, woman. Children are baby, boy, girl. Jugendliche (teenagers) are between child and adult. “Dame” is a polite word for “Frau”.',
         'Ang Erwachsene ay mga nasa hustong gulang: lalaki, babae. Ang Kinder ay baby, Bub, Mädchen. Ang Jugendliche ay nasa pagitan ng bata at matanda. Ang “Dame” ay magalang na salita para sa “Frau”.',
         ['Ein Mann und eine Frau sind Erwachsene.', 'Ein Baby, ein Bub und ein Mädchen sind Kinder.']),
], [
    choice(X, 'lesen', L('Die Familie ist im Park. Schauen Sie das Bild an.', 'The family is in the park. Look at the picture. Count the grown-ups.', 'Nasa park ang pamilya. Tingnan ang larawan. Bilangin ang mga nasa hustong gulang.'),
           'Wie viele Erwachsene sind im Park?', 'zwei', ['drei', 'vier'],
           L('Richtig: zwei – ein Mann und eine Frau. Der Bub, das Mädchen und das Baby sind Kinder, keine Erwachsenen. Mit „vier“ oder „drei“ zählen Sie Kinder mit.',
             'Correct: zwei – a man and a woman. The boy, the girl and the baby are children, not adults. With “vier” or “drei” you count children too.',
             'Tama: zwei – isang lalaki at isang babae. Ang Bub, Mädchen at Baby ay mga bata, hindi Erwachsene. Sa “vier” o “drei” kasama mo ang mga bata.'),
           [G1], R('Erwachsene', 'Mann'),
           img=img('park', 'Im Park stehen ein Mann, eine Frau, ein Bub und ein Mädchen. Ein Baby liegt im Kinderwagen.', 'In a park stand a man, a woman, a boy and a girl. A baby lies in a pram.', 'Sa park may lalaki, babae, batang lalaki at batang babae. May sanggol sa stroller.')),
    choice(X, 'lesen', L('Schauen Sie das Bild noch einmal an. Zählen Sie die Kinder.', 'Look at the picture again. Count the children.', 'Tingnan muli ang larawan. Bilangin ang mga bata.'),
           'Wie viele Kinder sind im Park?', 'drei', ['zwei', 'vier'],
           L('Richtig: drei – der Bub, das Mädchen und das Baby. Auch das Baby ist ein Kind. Mit „zwei“ vergessen Sie das Baby, „vier“ zählt einen Erwachsenen mit.',
             'Correct: drei – the boy, the girl and the baby. The baby is a child too. With “zwei” you forget the baby; “vier” counts an adult.',
             'Tama: drei – ang Bub, Mädchen at Baby. Bata rin ang Baby. Sa “zwei” nakalimutan mo ang baby; ang “vier” ay kasama ang isang Erwachsene.'),
           [G1], R('Kind', 'Baby', 'Mädchen', 'Bub'),
           img=img('park', 'Im Park stehen ein Mann, eine Frau, ein Bub und ein Mädchen. Ein Baby liegt im Kinderwagen.', 'In a park stand a man, a woman, a boy and a girl. A baby lies in a pram.', 'Sa park may lalaki, babae, batang lalaki at batang babae. May sanggol sa stroller.')),
    choice(X, 'grammatikWortschatz', L('Sie zeigen im Park auf ein Mädchen. Was sagen Sie?', 'In the park you point at a girl. What do you say?', 'Sa park, itinuturo mo ang isang batang babae. Ano ang sasabihin mo?'),
           'Das ist … Mädchen.', 'ein', ['eine', 'einen'],
           L('Richtig: ein Mädchen. Alle Wörter auf -chen haben „das“ und damit „ein“. „eine“ passt nicht, obwohl der Mensch weiblich ist. „einen“ gibt es nur bei männlichen Wörtern (der Bruder).',
             'Correct: ein Mädchen. All words ending in -chen take “das” and so “ein”. “eine” does not fit although the person is female. “einen” is only for masculine words (der Bruder).',
             'Tama: ein Mädchen. Lahat ng salitang -chen ay “das” kaya “ein”. Hindi bagay ang “eine” kahit babae ang tao. Ang “einen” ay para sa panlalaking salita (der Bruder).'),
           [G1], R('Mädchen')),
    choice(X, 'grammatikWortschatz', L('Sie lernen die Wörter für Kinder. Welcher Artikel passt?', 'You are learning the words for children. Which article fits?', 'Inaaral mo ang mga salita para sa mga bata. Aling article ang bagay?'),
           '… Bub', 'der', ['das', 'die'],
           L('Richtig: der Bub. „Bub“ ist männlich: der Bub. „das“ gehört zu „Mädchen“ und „Baby“, „die“ zu „Frau“ und „Tochter“.',
             'Correct: der Bub. “Bub” is masculine: der Bub. “das” belongs to “Mädchen” and “Baby”, “die” to “Frau” and “Tochter”.',
             'Tama: der Bub. Panlalaki ang “Bub”: der Bub. Ang “das” ay para sa “Mädchen” at “Baby”, ang “die” sa “Frau” at “Tochter”.'),
           [G1], R('Bub')),
    choice(X, 'hoeren', L('Eine Frau erzählt, was sie im Park sieht. Hören Sie.', 'A woman tells what she sees in the park. Listen.', 'Isang babae ang nagsasabi ng nakikita niya sa park. Makinig.'),
           'Wie viele Kinder sind im Park?', 'zwei', ['drei', 'vier'],
           L('Sie hören: „Im Park sind ein Mann, eine Frau, ein Mädchen und ein Baby.“ Kinder sind das Mädchen und das Baby: zwei. Mann und Frau sind Erwachsene. „vier“ zählt alle Menschen.',
             'You hear: “Im Park sind ein Mann, eine Frau, ein Mädchen und ein Baby.” The children are the girl and the baby: two. Man and woman are adults. “vier” counts everyone.',
             'Naririnig mo: “Im Park sind ein Mann, eine Frau, ein Mädchen und ein Baby.” Ang mga bata ay ang Mädchen at Baby: dalawa. Erwachsene ang lalaki at babae. Ang “vier” ay lahat ng tao.'),
           [G1], R('Kind', 'Erwachsene'), audio='Im Park sind ein Mann, eine Frau, ein Mädchen und ein Baby.'),
    cloze(X, 'grammatikWortschatz', L('Ergänzen Sie die Sätze über den Park. Nehmen Sie die Wörter unten.', 'Complete the sentences about the park. Use the words below.', 'Kumpletuhin ang mga pangungusap tungkol sa park. Gamitin ang mga salita sa ibaba.'),
          'Ein Mann und eine Frau sind {{1}}. Ein Baby und ein Mädchen sind {{2}}.', [['Erwachsene'], ['Kinder']],
          L('Richtig: Erwachsene, Kinder. Mann und Frau sind große Menschen: Erwachsene. Baby und Mädchen sind klein: Kinder. „Babys“ passt nicht: Das Mädchen ist kein Baby.',
            'Correct: Erwachsene, Kinder. Man and woman are grown-ups: Erwachsene. Baby and girl are small: Kinder. “Babys” does not fit: the girl is not a baby.',
            'Tama: Erwachsene, Kinder. Malalaki ang lalaki at babae: Erwachsene. Maliliit ang baby at batang babae: Kinder. Hindi bagay ang “Babys”: hindi baby ang Mädchen.'),
          [G1], R('Erwachsene', 'Kind'), bank=['Erwachsene', 'Kinder', 'Babys']),
    choice(X, 'sprechen', L('Ein Mann im Park fragt Sie: „Ist das Ihr Sohn?“ Es ist Ihre Tochter, ein Mädchen. Was antworten Sie? Wählen Sie, dann sagen Sie es laut.', 'A man in the park asks you: “Ist das Ihr Sohn?” It is your daughter, a girl. What do you answer? Choose, then say it aloud.', 'Tinanong ka ng isang lalaki sa park: “Ist das Ihr Sohn?” Anak mong babae ito. Ano ang sagot mo? Pumili, tapos sabihin nang malakas.'),
           'Mann: „Ist das Ihr Sohn?“', 'Nein, das ist meine Tochter.', ['Ja, das ist meine Tochter.', 'Nein, das ist mein Tochter.'],
           L('Richtig: „Nein, das ist meine Tochter.“ Auf „Sohn?“ antworten Sie „Nein“, weil es ein Mädchen ist. „Tochter“ ist ein „die“-Wort: meine Tochter. „Ja“ passt nicht zu „Tochter“, „mein Tochter“ ist falsch.',
             'Correct: “Nein, das ist meine Tochter.” To “Sohn?” you answer “Nein” because it is a girl. “Tochter” is a “die” word: meine Tochter. “Ja” does not fit “Tochter”; “mein Tochter” is wrong.',
             'Tama: “Nein, das ist meine Tochter.” Sa “Sohn?” sasagot ka ng “Nein” dahil babae ito. Ang “Tochter” ay “die” na salita: meine Tochter. Hindi bagay ang “Ja” sa “Tochter”; mali ang “mein Tochter”.'),
           [G1, G2], R('Tochter', 'mein')),
], intro=INTRO(L('Die Familie Huber ist im Park. Dort sind viele Menschen: Mann, Frau, Mädchen, Bub und ein Baby.',
                 'The Huber family is in the park. Many people are there: man, woman, girl, boy and a baby.',
                 'Nasa park ang pamilyang Huber. Maraming tao roon: lalaki, babae, batang babae, batang lalaki at isang sanggol.'),
               L('Am Ende kannst du Menschen im Bild nennen und sagen, wer Erwachsene und wer Kinder sind.',
                 'By the end you can name people in a picture and say who is an adult and who is a child.',
                 'Sa dulo, mapapangalanan mo ang mga tao sa larawan at masasabi mo kung sino ang matanda at sino ang bata.')))

# L04 ------------------------------------------------------------------ Plural
PLURAL = lambda: img('plural', 'Drei Bilder: Nummer 1 zeigt Kinder, Nummer 2 zwei Männer mit Krawatte, Nummer 3 mehrere Frauen.', 'Three pictures: number 1 shows children, number 2 two men with ties, number 3 several women.', 'Tatlong larawan: Nummer 1 mga bata, Nummer 2 dalawang lalaking may kurbata, Nummer 3 ilang babae.')
lesson(4, L('Ein Kind, zwei Kinder – der Plural', 'One child, two children – the plural', 'Isang anak, dalawang anak – plural'), [], [
    RULE('Plural: immer „die“', 'Im Plural ist der Artikel immer „die“: der Mann → die Männer, die Frau → die Frauen, das Kind → die Kinder. Das Nomen ändert sich: Lernen Sie den Plural zu jedem Wort mit!',
         'In the plural the article is always “die”: der Mann → die Männer, die Frau → die Frauen, das Kind → die Kinder. The noun changes: learn the plural with every word!',
         'Sa plural, laging “die” ang article: der Mann → die Männer, die Frau → die Frauen, das Kind → die Kinder. Nagbabago ang noun: isaulo ang plural ng bawat salita! (Sa Tagalog, “mga” lang ang idinadagdag.)',
         ['Ein Kind, zwei Kinder.', 'Ein Mann, zwei Männer.', 'Eine Frau, drei Frauen.']),
    RULE('-en / -n: die Frau → die Frauen', 'Viele „die“-Wörter haben im Plural die Endung -en oder -n: die Frau → die Frauen, die Schwester → die Schwestern, die Familie → die Familien.',
         'Many “die” words add -en or -n in the plural: die Frau → die Frauen, die Schwester → die Schwestern, die Familie → die Familien.',
         'Maraming “die” na salita ang nagdaragdag ng -en o -n sa plural: die Frau → die Frauen, die Schwester → die Schwestern, die Familie → die Familien.',
         ['Eine Schwester, zwei Schwestern.', 'Eine Familie, zwei Familien.']),
    RULE('Umlaut: Mutter → Mütter · Sohn → Söhne', 'Bei vielen Familienwörtern kommt im Plural ein Umlaut: a → ä, o → ö, u → ü. Dazu kommt oft -e oder -er: der Sohn → die Söhne, der Mann → die Männer, der Bruder → die Brüder.',
         'Many family words get an umlaut in the plural: a → ä, o → ö, u → ü. Often with -e or -er: der Sohn → die Söhne, der Mann → die Männer, der Bruder → die Brüder.',
         'Maraming salita sa pamilya ang may umlaut sa plural: a → ä, o → ö, u → ü. Madalas may -e o -er: der Sohn → die Söhne, der Mann → die Männer, der Bruder → die Brüder.',
         ['Eine Mutter, zwei Mütter.', 'Ein Vater, zwei Väter.', 'Eine Tochter, zwei Töchter.']),
    RULE('-s: das Baby → die Babys · die Oma → die Omas', 'Wörter wie Baby, Oma, Opa bekommen im Plural ein -s: die Babys, die Omas, die Opas.',
         'Words like Baby, Oma, Opa take -s in the plural: die Babys, die Omas, die Opas.',
         'Ang mga salitang tulad ng Baby, Oma, Opa ay may -s sa plural: die Babys, die Omas, die Opas.',
         ['Ein Baby, zwei Babys.', 'Eine Oma, zwei Omas.']),
    RULE('Nur Plural: die Eltern · die Geschwister · die Leute', 'Manche Wörter gibt es fast nur im Plural. Sie sagen: „Meine Eltern sind da.“ Für eine Person sagen Sie Mutter oder Vater, Bruder oder Schwester.',
         'Some words almost only exist in the plural. You say: “Meine Eltern sind da.” For one person you say Mutter or Vater, Bruder or Schwester.',
         'May mga salitang halos plural lang. Sasabihin mo: “Meine Eltern sind da.” Para sa isang tao, Mutter o Vater, Bruder o Schwester ang gamit.',
         ['Meine Eltern wohnen in Graz.', 'Meine Geschwister sind da.']),
], [
    choice(X, 'lesen', L('Sie sehen drei Bilder mit Menschen. Schauen Sie das Bild an.', 'You see three pictures with people. Look at the picture.', 'May tatlong larawan ng mga tao. Tingnan ang larawan.'),
           'Nummer 2: zwei …', 'Männer', ['Mann', 'Kinder'],
           L('Richtig: zwei Männer. Nummer 2 zeigt zwei Männer. Der Plural von „Mann“ ist „Männer“ (Umlaut + -er). „Mann“ ist der Singular (eine Person), „Kinder“ zeigt Nummer 1.',
             'Correct: zwei Männer. Number 2 shows two men. The plural of “Mann” is “Männer” (umlaut + -er). “Mann” is the singular (one person); “Kinder” is number 1.',
             'Tama: zwei Männer. Dalawang lalaki ang nasa Nummer 2. Ang plural ng “Mann” ay “Männer” (umlaut + -er). Ang “Mann” ay singular (isang tao); ang “Kinder” ay Nummer 1.'),
           [G4], R('Mann'), img=PLURAL()),
    choice(X, 'lesen', L('Schauen Sie das Bild noch einmal an. Zählen Sie die Frauen.', 'Look at the picture again. Count the women.', 'Tingnan muli ang larawan. Bilangin ang mga babae.'),
           'Nummer 3: Wie viele Frauen sind das?', 'vier', ['drei', 'fünf'],
           L('Richtig: vier Frauen. Der Plural von „die Frau“ ist „die Frauen“ (-en). In Nummer 1 sind es drei Kinder, in Nummer 3 vier Frauen.',
             'Correct: vier Frauen. The plural of “die Frau” is “die Frauen” (-en). Number 1 has three children, number 3 has four women.',
             'Tama: vier Frauen. Ang plural ng “die Frau” ay “die Frauen” (-en). Tatlong bata ang nasa Nummer 1, apat na babae ang nasa Nummer 3.'),
           [G4], R('Frau'), img=PLURAL()),
    choice(X, 'grammatikWortschatz', L('Anna zeigt, wie viele Kinder sie hat: ein Sohn, zwei Söhne. Wählen Sie den Plural.', 'Anna talks about sons: one son, two sons. Choose the plural.', 'Nagsasalita si Anna tungkol sa mga anak na lalaki: isang anak, dalawang anak. Piliin ang plural.'),
           'ein Sohn – zwei …', 'Söhne', ['Sohns', 'Sohnen'],
           L('Richtig: zwei Söhne. „der Sohn“ bekommt im Plural einen Umlaut (o → ö) und -e. „Sohns“ und „Sohnen“ gibt es nicht.',
             'Correct: zwei Söhne. “der Sohn” takes an umlaut (o → ö) and -e in the plural. “Sohns” and “Sohnen” do not exist.',
             'Tama: zwei Söhne. Ang “der Sohn” ay may umlaut (o → ö) at -e sa plural. Walang “Sohns” at “Sohnen”.'),
           [G4], R('Sohn')),
    cloze(X, 'grammatikWortschatz', L('Maria beschreibt ein Foto. Ergänzen Sie den Plural. Nehmen Sie die Wörter unten.', 'Maria describes a photo. Complete the plural. Use the words below.', 'Inilalarawan ni Maria ang isang litrato. Kumpletuhin ang plural. Gamitin ang mga salita sa ibaba.'),
          'ein Mann – zwei {{1}} · eine Frau – vier {{2}} · ein Kind – drei {{3}}', [['Männer'], ['Frauen'], ['Kinder']],
          L('Richtig: Männer, Frauen, Kinder. Mann → Männer (Umlaut + -er), Frau → Frauen (-en), Kind → Kinder (-er). „Kinds“ gibt es nicht: Das Wort „Kind“ nimmt im Plural -er.',
            'Correct: Männer, Frauen, Kinder. Mann → Männer (umlaut + -er), Frau → Frauen (-en), Kind → Kinder (-er). “Kinds” does not exist: “Kind” takes -er in the plural.',
            'Tama: Männer, Frauen, Kinder. Mann → Männer (umlaut + -er), Frau → Frauen (-en), Kind → Kinder (-er). Walang “Kinds”: ang “Kind” ay may -er sa plural.'),
          [G4], R('Mann', 'Frau', 'Kind'), bank=['Männer', 'Frauen', 'Kinder', 'Kinds']),
    choice(X, 'hoeren', L('Maria erzählt von ihrer Familie. Hören Sie.', 'Maria talks about her family. Listen.', 'Nagkukuwento si Maria tungkol sa pamilya niya. Makinig.'),
           'Wie viele Geschwister hat Maria?', 'fünf', ['drei', 'zwei'],
           L('Sie hören: „Ich habe zwei Brüder und drei Schwestern.“ Brüder und Schwestern sind Plural: 2 + 3 = fünf Geschwister. „drei“ sind nur die Schwestern, „zwei“ nur die Brüder.',
             'You hear: “Ich habe zwei Brüder und drei Schwestern.” Brüder and Schwestern are plurals: 2 + 3 = five siblings. “drei” is only the sisters, “zwei” only the brothers.',
             'Naririnig mo: “Ich habe zwei Brüder und drei Schwestern.” Plural ang Brüder at Schwestern: 2 + 3 = limang kapatid. Ang “drei” ay mga kapatid na babae lang, ang “zwei” ay mga kapatid na lalaki lang.'),
           [G4], R('Bruder', 'Schwester', 'Geschwister'), audio='Ich habe zwei Brüder und drei Schwestern.'),
    choice(X, 'grammatikWortschatz', L('Ana schreibt über ihre Familie. Welcher Plural ist richtig?', 'Ana writes about her family. Which plural is correct?', 'Sumusulat si Ana tungkol sa pamilya niya. Aling plural ang tama?'),
           'eine Schwester – zwei …', 'Schwestern', ['Schwester', 'Schwesters'],
           L('Richtig: zwei Schwestern. „die Schwester“ bekommt im Plural -n. „zwei Schwester“ ist falsch: Im Deutschen muss das Nomen den Plural zeigen (nicht nur die Zahl). „Schwesters“ gibt es nicht.',
             'Correct: zwei Schwestern. “die Schwester” takes -n in the plural. “zwei Schwester” is wrong: in German the noun itself must show the plural (not just the number). “Schwesters” does not exist.',
             'Tama: zwei Schwestern. Ang “die Schwester” ay may -n sa plural. Mali ang “zwei Schwester”: sa German, ang noun mismo ang nagpapakita ng plural (hindi lang ang bilang). Walang “Schwesters”.'),
           [G4], R('Schwester')),
    short(X, 'schreiben', L('Sie schreiben an Tom über Ihre Familie. Schreiben Sie den Plural.', 'You write to Tom about your family. Write the plural.', 'Sumusulat ka kay Tom tungkol sa pamilya mo. Isulat ang plural.'),
          'eine Mutter – zwei …', ['Mütter'],
          L('Richtig: Mütter. „die Mutter“ bekommt im Plural einen Umlaut (u → ü): die Mütter. Der Artikel im Plural ist immer „die“.',
            'Correct: Mütter. “die Mutter” takes an umlaut in the plural (u → ü): die Mütter. The plural article is always “die”.',
            'Tama: Mütter. Ang “die Mutter” ay may umlaut sa plural (u → ü): die Mütter. Laging “die” ang article sa plural.'),
          [G4], R('Mutter')),
], intro=INTRO(L('Maria schreibt eine E-Mail an Tom. Sie spricht über Frauen, Männer und Kinder.',
                 'Maria writes an e-mail to Tom. She talks about women, men and children.',
                 'Sumusulat si Maria ng e-mail kay Tom. Nagsasalita siya tungkol sa mga babae, lalaki at bata.'),
               L('Am Ende kannst du von einer Person und von mehreren Personen sprechen: ein Kind, zwei Kinder.',
                 'By the end you can talk about one person and several people: ein Kind, zwei Kinder.',
                 'Sa dulo, masasabi mo ang isang tao at ang maraming tao: ein Kind, zwei Kinder.')))

# L05 ------------------------------------------------------------------ mein, meine – dein, Ihr
FOTO = lambda: img('foto', 'Lukas sagt „Das ist meine Familie.“ An der Wand hängen drei Fotos mit den Nummern 1, 2, 3. Darunter steht Mutter, Vater, Schwester.', 'Lukas says “Das ist meine Familie.” Three photos numbered 1, 2, 3 hang on the wall. Underneath it says Mutter, Vater, Schwester.', 'Sinasabi ni Lukas ang “Das ist meine Familie.” May tatlong larawan sa dingding, may numero 1, 2, 3. Sa ilalim nakasulat ang Mutter, Vater, Schwester.')
lesson(5, L('Mein, meine – dein, Ihr', 'My – your', 'Aking – iyong'), ['mein', 'dein', 'Ihr (Possessiv)'], [
    PHRASE('Das ist meine Familie. Das ist mein Bruder und das ist meine Schwester.', 'So stellen Sie Menschen aus Ihrer Familie vor. „mein“ und „meine“ zeigen: Das gehört zu mir.',
           'This is how you introduce people from your family. “mein” and “meine” show: this belongs to me.',
           'Ganito mo ipakikilala ang mga tao sa pamilya mo. Ipinapakita ng “mein” at “meine”: sa akin ito.'),
    RULE('mein Vater · meine Mutter', 'Wie bei „ein / eine“: bei „der“- und „das“-Wörtern sagen Sie „mein“ (mein Vater, mein Kind), bei „die“-Wörtern „meine“ (meine Mutter). Der Artikel bestimmt die Form, nicht, ob der Mensch männlich oder weiblich ist: mein Mädchen, aber meine Frau.',
         'Like “ein / eine”: for “der” and “das” words you say “mein” (mein Vater, mein Kind), for “die” words “meine” (meine Mutter). The article decides, not the sex of the person.',
         'Tulad ng “ein / eine”: sa “der” at “das” na salita, “mein” (mein Vater, mein Kind); sa “die” na salita, “meine” (meine Mutter). Ang article ang nagpapasya.',
         ['Das ist mein Vater.', 'Das ist meine Mutter.', 'Das ist mein Kind.']),
    RULE('Plural: meine Eltern · meine Kinder', 'Im Plural sagen Sie immer „meine“, wie bei „die“: meine Eltern, meine Kinder, meine Geschwister.',
         'In the plural you always say “meine”, like “die”: meine Eltern, meine Kinder, meine Geschwister.',
         'Sa plural, laging “meine” ang sasabihin mo, tulad ng “die”: meine Eltern, meine Kinder, meine Geschwister.',
         ['Das sind meine Eltern.', 'Das sind meine Kinder.']),
    RULE('du → dein / deine · Sie → Ihr / Ihre', 'Mit „du“ (Freunde, Kinder) sagen Sie dein / deine. Mit „Sie“ (Beamtin, Lehrer, fremde Erwachsene) sagen Sie Ihr / Ihre – „Ihr“ schreiben Sie immer groß. Die Endung folgt wieder dem Artikel.',
         'With “du” (friends, children) you say dein / deine. With “Sie” (an official, a teacher, strangers) you say Ihr / Ihre – “Ihr” always starts with a capital. The ending follows the article again.',
         'Sa “du” (kaibigan, bata) sinasabi mo ang dein / deine. Sa “Sie” (opisyal, guro, estranghero) ang Ihr / Ihre – laging malaking I ang “Ihr”. Sinusunod muli ng ending ang article.',
         ['Wie heißt dein Bruder?', 'Wie heißt Ihr Bruder?', 'Wie heißen Ihre Eltern?']),
], [
    choice(X, 'lesen', L('Lukas zeigt seine Familie an der Wand. Schauen Sie das Bild an.', 'Lukas shows his family on the wall. Look at the picture. Which photo does he mean?', 'Ipinapakita ni Lukas ang pamilya niya sa dingding. Tingnan ang larawan. Aling larawan ang tinutukoy niya?'),
           'Lukas zeigt Nummer 3. Was sagt er?', 'Das ist meine Schwester.', ['Das ist mein Schwester.', 'Das ist meine Mutter.'],
           L('Richtig: „Das ist meine Schwester.“ Nummer 3 ist die Schwester, und „Schwester“ ist ein „die“-Wort: meine. „mein Schwester“ ist falsch. „meine Mutter“ ist Nummer 1.',
             'Correct: “Das ist meine Schwester.” Number 3 is the sister, and “Schwester” is a “die” word: meine. “mein Schwester” is wrong. “meine Mutter” is number 1.',
             'Tama: “Das ist meine Schwester.” Ang Nummer 3 ay ang kapatid na babae, at “die” na salita ang “Schwester”: meine. Mali ang “mein Schwester”. Ang “meine Mutter” ay Nummer 1.'),
           [G2], R('mein', 'Schwester'), img=FOTO()),
    choice(X, 'lesen', L('Lukas zeigt jetzt Nummer 2. Schauen Sie das Bild noch einmal an.', 'Lukas now shows number 2. Look at the picture again.', 'Ipinapakita na ni Lukas ang Nummer 2. Tingnan muli ang larawan.'),
           'Lukas zeigt Nummer 2. Was sagt er?', 'Das ist mein Vater.', ['Das ist meine Vater.', 'Das ist meine Mutter.'],
           L('Richtig: „Das ist mein Vater.“ Nummer 2 ist der Vater, und „Vater“ ist ein „der“-Wort: mein. „meine Vater“ ist falsch, „meine Mutter“ ist Nummer 1.',
             'Correct: “Das ist mein Vater.” Number 2 is the father, and “Vater” is a “der” word: mein. “meine Vater” is wrong; “meine Mutter” is number 1.',
             'Tama: “Das ist mein Vater.” Ang Nummer 2 ay ang tatay, at “der” na salita ang “Vater”: mein. Mali ang “meine Vater”; ang “meine Mutter” ay Nummer 1.'),
           [G2], R('mein', 'Vater'), img=FOTO()),
    cloze(X, 'grammatikWortschatz', L('Lukas zeigt Frau Berger seine Eltern. Ergänzen Sie. Nehmen Sie die Wörter unten.', 'Lukas shows Mrs Berger his parents. Complete the sentences. Use the words below.', 'Ipinapakita ni Lukas kay Frau Berger ang mga magulang niya. Kumpletuhin. Gamitin ang mga salita sa ibaba.'),
          'Das ist {{1}} Vater und das ist {{2}} Mutter. Das sind {{3}} Eltern.', [['mein'], ['meine'], ['meine']],
          L('Richtig: mein Vater (der-Wort), meine Mutter (die-Wort), meine Eltern (Plural). „meinen“ gibt es hier nicht: Nach „Das ist“ steht „mein / meine“ ohne -n.',
            'Correct: mein Vater (der word), meine Mutter (die word), meine Eltern (plural). “meinen” does not fit here: after “Das ist” you say “mein / meine” without -n.',
            'Tama: mein Vater (der na salita), meine Mutter (die na salita), meine Eltern (plural). Hindi bagay ang “meinen”: pagkatapos ng “Das ist” ay “mein / meine” na walang -n.'),
          [G2], R('mein', 'Vater', 'Mutter', 'Eltern'), bank=['mein', 'meine', 'meine', 'meinen']),
    choice(X, 'grammatikWortschatz', L('Sie sprechen mit Anna, Ihrer Freundin. Sie sagen „du“. Was fragen Sie?', 'You talk to Anna, your friend. You say “du”. What do you ask?', 'Kausap mo si Anna, kaibigan mo. “du” ang gamit mo. Ano ang itatanong mo?'),
           'Anna, wie heißt … Schwester?', 'deine', ['dein', 'Ihre'],
           L('Richtig: deine Schwester. Mit „du“ sagen Sie „dein / deine“, und „Schwester“ ist ein „die“-Wort: deine. „Ihre“ ist die höfliche Form für „Sie“ – Sie sagen aber „du“ zu Anna.',
             'Correct: deine Schwester. With “du” you say “dein / deine”, and “Schwester” is a “die” word: deine. “Ihre” is the polite form for “Sie” – but you say “du” to Anna.',
             'Tama: deine Schwester. Sa “du”, “dein / deine” ang gamit, at “die” na salita ang “Schwester”: deine. Ang “Ihre” ay magalang na anyo para sa “Sie” – pero “du” ang gamit mo kay Anna.'),
           [G2], R('dein', 'Schwester')),
    choice(X, 'grammatikWortschatz', L('Sie sprechen mit Herrn Bauer, Ihrem Lehrer. Sie sagen „Sie“. Was fragen Sie?', 'You talk to Mr Bauer, your teacher. You say “Sie”. What do you ask?', 'Kausap mo si Herr Bauer, guro mo. “Sie” ang gamit mo. Ano ang itatanong mo?'),
           'Herr Bauer, wie alt ist … Sohn?', 'Ihr', ['Ihre', 'dein'],
           L('Richtig: Ihr Sohn. Mit „Sie“ sagen Sie „Ihr / Ihre“, und „Sohn“ ist ein „der“-Wort: Ihr. „Ihre“ gehört zu „die“-Wörtern. „dein“ ist die Form für „du“ – bei Herrn Bauer sagen Sie „Sie“.',
             'Correct: Ihr Sohn. With “Sie” you say “Ihr / Ihre”, and “Sohn” is a “der” word: Ihr. “Ihre” belongs to “die” words. “dein” is the “du” form – to Mr Bauer you say “Sie”.',
             'Tama: Ihr Sohn. Sa “Sie”, “Ihr / Ihre” ang gamit, at “der” na salita ang “Sohn”: Ihr. Ang “Ihre” ay para sa “die” na salita. Ang “dein” ay anyo ng “du” – kay Herr Bauer, “Sie” ang gamit mo.'),
           [G2], R('Ihr (Possessiv)', 'Sohn')),
    choice(X, 'sprechen', L('Sie sind beim Magistrat. Die Beamtin fragt: „Wie heißt Ihre Tochter?“ Ihre Tochter heißt Lena. Was antworten Sie? Wählen Sie, dann sagen Sie es laut.', 'You are at the Magistrat (city office). The official asks: “Wie heißt Ihre Tochter?” Your daughter is called Lena. What do you answer? Choose, then say it aloud.', 'Nasa Magistrat (city office) ka. Tinanong ka ng opisyal: “Wie heißt Ihre Tochter?” Lena ang pangalan ng anak mong babae. Ano ang sagot mo? Pumili, tapos sabihin nang malakas.'),
           'Beamtin: „Wie heißt Ihre Tochter?“', 'Meine Tochter heißt Lena.', ['Mein Tochter heißt Lena.', 'Ihre Tochter heißt Lena.'],
           L('Richtig: „Meine Tochter heißt Lena.“ Es ist Ihre eigene Tochter: meine. „Tochter“ ist ein „die“-Wort: meine, nicht „mein“. „Ihre Tochter“ wäre die Tochter der Beamtin.',
             'Correct: “Meine Tochter heißt Lena.” It is your own daughter: meine. “Tochter” is a “die” word: meine, not “mein”. “Ihre Tochter” would be the official’s daughter.',
             'Tama: “Meine Tochter heißt Lena.” Sarili mong anak ito: meine. “die” na salita ang “Tochter”: meine, hindi “mein”. Ang “Ihre Tochter” ay anak ng opisyal.'),
           [G2], R('mein', 'Tochter')),
    choice(X, 'hoeren', L('Lukas stellt seine Eltern vor. Hören Sie.', 'Lukas introduces his parents. Listen.', 'Ipinakikilala ni Lukas ang mga magulang niya. Makinig.'),
           'Wie heißt der Vater?', 'Peter', ['Anna', 'Lukas'],
           L('Sie hören: „Das sind meine Eltern. Mein Vater heißt Peter und meine Mutter heißt Anna.“ „Mein Vater“ ist Peter, „meine Mutter“ ist Anna. Lukas spricht selbst.',
             'You hear: “Das sind meine Eltern. Mein Vater heißt Peter und meine Mutter heißt Anna.” “Mein Vater” is Peter, “meine Mutter” is Anna. Lukas is the speaker.',
             'Naririnig mo: “Das sind meine Eltern. Mein Vater heißt Peter und meine Mutter heißt Anna.” Si Peter ang “mein Vater”, si Anna ang “meine Mutter”. Si Lukas ang nagsasalita.'),
           [G2], R('mein', 'Vater'), audio='Das sind meine Eltern. Mein Vater heißt Peter und meine Mutter heißt Anna.'),
], intro=INTRO(L('Lukas sagt: „Das ist meine Mutter. Das ist mein Vater.“ Zu Anna sagen Sie „du“, zu Herrn Bauer sagen Sie „Sie“.',
                 'Lukas says: “Das ist meine Mutter. Das ist mein Vater.” You say “du” to Anna and “Sie” to Mr Bauer.',
                 'Sabi ni Lukas: “Das ist meine Mutter. Das ist mein Vater.” “du” ang sinasabi mo kay Anna at “Sie” kay Herr Bauer.'),
               L('Am Ende kannst du sagen: mein Vater, meine Mutter – und fragen: dein Bruder? Ihre Tochter?',
                 'By the end you can say: mein Vater, meine Mutter – and ask: dein Bruder? Ihre Tochter?',
                 'Sa dulo, masasabi mo ang: mein Vater, meine Mutter – at makakatanong ka ng: dein Bruder? Ihre Tochter?')))

# L06 ------------------------------------------------------------------ Familienstand
lesson(6, L('Familienstand', 'Marital status', 'Civil status'), ['verheiratet', 'ledig', 'geschieden', 'Ehefrau', 'Ehemann', 'Partner, Partnerin', 'heiraten', 'gestorben'], [
    PHRASE('Sind Sie verheiratet? – Ja, ich bin verheiratet.', 'So fragt man nach dem Familienstand. Der Familienstand sagt, ob jemand verheiratet, ledig oder geschieden ist.',
           'This is how people ask about marital status. The Familienstand says whether someone is married, single or divorced.',
           'Ganito itinatanong ang civil status. Sinasabi ng Familienstand kung kasal, walang asawa o hiwalay ang isang tao.'),
    RULE('ich bin verheiratet · ledig · geschieden', 'verheiratet = mit Ehemann oder Ehefrau. ledig = nicht verheiratet, auch früher nicht. geschieden = früher verheiratet, jetzt nicht mehr. Man sagt „ich bin …“ (mit „sein“), nicht „ich habe …“.',
         'verheiratet = married. ledig = not married (never married). geschieden = was married, not any more. You say “ich bin …” (with “sein”), not “ich habe …”.',
         'verheiratet = kasal. ledig = walang asawa (hindi pa kasal). geschieden = dating kasal, hiwalay na. Sinasabi: “ich bin …” (gamit ang “sein”), hindi “ich habe …”.',
         ['Ich bin ledig.', 'Anna ist verheiratet.', 'Sofia ist geschieden.']),
    RULE('der Ehemann · die Ehefrau · der Partner, die Partnerin', 'Ehemann und Ehefrau sind verheiratet. Im Alltag sagt man auch: mein Mann, meine Frau. Partner und Partnerin kann auch ein Mensch sein, den Sie nicht geheiratet haben.',
         'Ehemann and Ehefrau are married. In everyday speech you also say: mein Mann, meine Frau. Partner and Partnerin can also be a person you have not married.',
         'Ang Ehemann at Ehefrau ay kasal. Sa araw-araw: mein Mann, meine Frau. Ang Partner at Partnerin ay puwedeng taong hindi mo pa naaasawa.',
         ['Das ist mein Mann.', 'Das ist meine Frau.', 'Das ist meine Partnerin.']),
    RULE('heiraten: ich heirate · du heiratest · er heiratet', '„heiraten“ ist ein Verb: ich heirate, du heiratest, er heiratet, wir heiraten. Vor -st steht ein „e“, damit man es gut sprechen kann.',
         '“heiraten” (to marry) is a verb: ich heirate, du heiratest, er heiratet, wir heiraten. An “e” comes before -st so you can say it easily.',
         'Ang “heiraten” (magpakasal) ay verb: ich heirate, du heiratest, er heiratet, wir heiraten. May “e” bago ang -st para madaling bigkasin.',
         ['Ich heirate bald.', 'Anna und Peter heiraten.']),
    CULTURE('Familienstand auf Formularen', 'Auf vielen Formularen in Österreich steht „Familienstand“: ledig, verheiratet oder geschieden. Sie kreuzen an, was für Sie stimmt.',
            'On many forms in Austria you find “Familienstand”: ledig, verheiratet or geschieden. You tick what is true for you.',
            'Sa maraming form sa Austria may nakasulat na “Familienstand”: ledig, verheiratet o geschieden. Ie-ekis mo ang totoo para sa iyo.'),
], [
    choice(X, 'lesen', L('Sofia Berger füllt ein Formular aus. Schauen Sie das Bild an.', 'Sofia Berger fills in a form. Look at the picture. One box is ticked.', 'Pinupunan ni Sofia Berger ang isang form. Tingnan ang larawan. May isang kahong may ekis.'),
           'Was ist Sofia Berger?', 'verheiratet', ['ledig', 'geschieden'],
           L('Richtig: verheiratet. Im Formular ist nur „verheiratet“ angekreuzt. „ledig“ und „geschieden“ sind leer.',
             'Correct: verheiratet. Only “verheiratet” is ticked on the form. “ledig” and “geschieden” are empty.',
             'Tama: verheiratet. “verheiratet” lang ang may ekis sa form. Walang laman ang “ledig” at “geschieden”.'),
           [G3], R('verheiratet'), img=FORM()),
    choice(X, 'lesen', L('Schauen Sie das Formular noch einmal an. Sie lesen die Frage und die Antwort.', 'Look at the form again. You read the question and the answer.', 'Tingnan muli ang form. Binabasa mo ang tanong at ang sagot.'),
           'Ist Sofia Berger ledig?', 'Nein, sie ist verheiratet.', ['Ja, sie ist ledig.', 'Nein, sie ist geschieden.'],
           L('Richtig: „Nein, sie ist verheiratet.“ Das Kreuz steht bei „verheiratet“. „ledig“ ist falsch, „geschieden“ ist auch nicht angekreuzt.',
             'Correct: “Nein, sie ist verheiratet.” The cross is at “verheiratet”. “ledig” is wrong; “geschieden” is not ticked either.',
             'Tama: “Nein, sie ist verheiratet.” Ang ekis ay nasa “verheiratet”. Mali ang “ledig”; walang ekis din ang “geschieden”.'),
           [G3], R('ledig', 'verheiratet'), img=FORM()),
    choice(X, 'hoeren', L('Eine Frau stellt sich vor. Hören Sie.', 'A woman introduces herself. Listen.', 'Nagpapakilala ang isang babae. Makinig.'),
           'Was ist der Familienstand?', 'geschieden', ['ledig', 'verheiratet'],
           L('Sie hören: „Ich bin geschieden. Ich habe eine Tochter. Sie wohnt in Linz.“ „geschieden“ steht am Anfang. Dass sie eine Tochter hat, sagt nichts über „ledig“ oder „verheiratet“.',
             'You hear: “Ich bin geschieden. Ich habe eine Tochter. Sie wohnt in Linz.” “geschieden” is right at the start. Having a daughter says nothing about “ledig” or “verheiratet”.',
             'Naririnig mo: “Ich bin geschieden. Ich habe eine Tochter. Sie wohnt in Linz.” Nasa simula ang “geschieden”. Ang pagkakaroon ng anak ay walang sinasabi tungkol sa “ledig” o “verheiratet”.'),
           [G3], R('geschieden'), audio='Ich bin geschieden. Ich habe eine Tochter. Sie wohnt in Linz.'),
    cloze(X, 'grammatikWortschatz', L('Peter und Anna sind verheiratet. Ergänzen Sie, was sie sagen. Nehmen Sie die Wörter unten.', 'Peter and Anna are married. Complete what they say. Use the words below.', 'Kasal sina Peter at Anna. Kumpletuhin ang sinasabi nila. Gamitin ang mga salita sa ibaba.'),
          'Peter sagt: „Das ist meine {{1}} Anna.“ Anna sagt: „Das ist mein {{2}} Peter.“', [['Ehefrau', 'Frau'], ['Ehemann', 'Mann']],
          L('Richtig: Ehefrau, Ehemann. Peter und Anna sind verheiratet: Anna ist seine Ehefrau, Peter ist ihr Ehemann. „meine“ + Ehefrau (die), „mein“ + Ehemann (der). „Tochter“ passt nicht: Verheiratete Menschen sind Mann und Frau, nicht Vater und Tochter.',
            'Correct: Ehefrau, Ehemann. Peter and Anna are married: Anna is his wife, Peter is her husband. “meine” + Ehefrau (die), “mein” + Ehemann (der). “Tochter” does not fit: a married couple are husband and wife, not father and daughter.',
            'Tama: Ehefrau, Ehemann. Kasal sina Peter at Anna: asawang babae ni Peter si Anna, asawang lalaki ni Anna si Peter. “meine” + Ehefrau (die), “mein” + Ehemann (der). Hindi bagay ang “Tochter”: mag-asawa ang kasal, hindi tatay at anak.'),
          [G3], R('Ehemann', 'Ehefrau'), bank=['Ehefrau', 'Ehemann', 'Tochter']),
    choice(X, 'grammatikWortschatz', L('Sie sagen Ihren Familienstand. Wählen Sie das richtige Verb.', 'You state your marital status. Choose the right verb.', 'Sinasabi mo ang civil status mo. Piliin ang tamang verb.'),
           'Ich … verheiratet.', 'bin', ['habe', 'ist'],
           L('Richtig: Ich bin verheiratet. Der Familienstand kommt mit „sein“: ich bin. „haben“ sagt, was Sie besitzen (Kinder, Geschwister). „ist“ gehört zu er/sie/es.',
             'Correct: Ich bin verheiratet. Marital status goes with “sein”: ich bin. “haben” says what you have (children, siblings). “ist” belongs to er/sie/es.',
             'Tama: Ich bin verheiratet. Ang civil status ay gamit ang “sein”: ich bin. Ang “haben” ay sa mayroon ka (anak, kapatid). Ang “ist” ay para sa er/sie/es.'),
           [G3], R('verheiratet', 'sein')),
    choice(X, 'sprechen', L('Eine Frau in Wien fragt Sie. Sie sind nicht verheiratet und waren nie verheiratet. Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'A woman in Vienna asks you. You are not married and never were. What do you say? Choose, then say it aloud.', 'Tinanong ka ng isang babae sa Vienna. Hindi ka kasal at hindi ka pa nagkaroon ng asawa. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'),
           'Frau: „Sind Sie verheiratet?“', 'Nein, ich bin ledig.', ['Ja, ich bin ledig.', 'Nein, ich habe ledig.'],
           L('Richtig: „Nein, ich bin ledig.“ „ledig“ heißt: nicht verheiratet – also „Nein“. „Ja, ich bin ledig“ widerspricht sich. Der Familienstand kommt mit „sein“, nicht mit „haben“.',
             'Correct: “Nein, ich bin ledig.” “ledig” means not married – so “Nein”. “Ja, ich bin ledig” contradicts itself. Marital status goes with “sein”, not “haben”.',
             'Tama: “Nein, ich bin ledig.” Ang “ledig” ay walang asawa – kaya “Nein”. Salungat sa sarili ang “Ja, ich bin ledig”. Ang civil status ay gamit ang “sein”, hindi “haben”.'),
           [G3], R('ledig', 'verheiratet')),
    choice(X, 'lesen', L('Tom schreibt an Lukas. Lesen Sie die E-Mail.', 'Tom writes to Lukas. Read the e-mail.', 'Sumulat si Tom kay Lukas. Basahin ang e-mail.'),
           'Servus Lukas! Ich bin Tom. Ich bin ledig. Meine Freundin heißt Anna. Wir heiraten bald. Servus, Tom\n\nIst Tom verheiratet?', 'Nein, er ist ledig.', ['Ja, er ist verheiratet.', 'Nein, er ist geschieden.'],
           L('Im Text: „Ich bin ledig.“ „Wir heiraten bald“ heißt: Tom und Anna heiraten später – jetzt ist Tom noch nicht verheiratet. „geschieden“ steht nicht im Text.',
             'The text says: “Ich bin ledig.” “Wir heiraten bald” means Tom and Anna will marry later – now Tom is not yet married. “geschieden” is not in the text.',
             'Sabi sa teksto: “Ich bin ledig.” Ang “Wir heiraten bald” ay ikakasal pa lang sina Tom at Anna – hindi pa kasal si Tom ngayon. Wala ang “geschieden” sa teksto.'),
           [G3], R('ledig', 'heiraten')),
], intro=INTRO(L('Sofia Berger ist in Wien. Eine Frau fragt: „Sind Sie verheiratet?“ Sofia antwortet.',
                 'Sofia Berger is in Vienna. A woman asks: “Sind Sie verheiratet?” Sofia answers.',
                 'Nasa Vienna si Sofia Berger. Nagtanong ang isang babae: “Sind Sie verheiratet?” Sumagot si Sofia.'),
               L('Am Ende kannst du sagen, ob du verheiratet, ledig oder geschieden bist – und danach fragen.',
                 'By the end you can say whether you are married, single or divorced – and ask about it.',
                 'Sa dulo, masasabi mo kung kasal, walang asawa o hiwalay ka – at makakatanong ka tungkol dito.')))

# L07 ------------------------------------------------------------------ sehen, hören, lesen, schreiben
VERBEN = lambda: img('verben', 'Vier Bilder mit Nummern: 1 ein Mann schaut zu einem Baum, 2 eine Frau mit Kopfhörern und Noten, 3 ein Mann mit einem offenen Buch, 4 eine Frau mit Stift und Papier.', 'Four numbered pictures: 1 a man looks at a tree, 2 a woman with headphones and music notes, 3 a man with an open book, 4 a woman with a pencil and paper.', 'Apat na larawang may numero: 1 lalaking tumitingin sa puno, 2 babaeng may headphones at nota, 3 lalaking may bukas na libro, 4 babaeng may lapis at papel.')
lesson(7, L('sehen, hören, lesen, schreiben', 'see, hear, read, write', 'makita, marinig, magbasa, sumulat'), ['sehen', 'hören', 'lesen', 'schreiben'], [
    PHRASE('Ich sehe Lukas. Ich höre Lena. Ich lese eine E-Mail. Ich schreibe an Tom.', 'Vier wichtige Verben für den Alltag: sehen, hören, lesen, schreiben. Zuerst die „ich“-Form lernen: ich sehe, ich höre, ich lese, ich schreibe.',
           'Four important everyday verbs: sehen, hören, lesen, schreiben. Learn the “ich” form first: ich sehe, ich höre, ich lese, ich schreibe.',
           'Apat na mahalagang verb sa araw-araw: sehen, hören, lesen, schreiben. Unahin ang “ich” na anyo: ich sehe, ich höre, ich lese, ich schreibe.'),
    RULE('sehen: ich sehe · du siehst · er sieht', '„sehen“ ändert den Vokal bei „du“ und „er/sie/es“: e → ie. Bei „ich“, „wir“ und „Sie“ bleibt das „e“: ich sehe, wir sehen, Sie sehen.',
         '“sehen” changes its vowel with “du” and “er/sie/es”: e → ie. With “ich”, “wir” and “Sie” the “e” stays: ich sehe, wir sehen, Sie sehen.',
         'Nagbabago ang patinig ng “sehen” sa “du” at “er/sie/es”: e → ie. Sa “ich”, “wir” at “Sie” nananatili ang “e”: ich sehe, wir sehen, Sie sehen.',
         ['Ich sehe Lena.', 'Du siehst Lukas.', 'Anna sieht Peter.']),
    RULE('lesen: ich lese · du liest · er liest', '„lesen“ macht dasselbe: e → ie bei „du“ und „er/sie/es“. Bei „du“ und „er“ ist die Form gleich: du liest, er liest.',
         '“lesen” does the same: e → ie with “du” and “er/sie/es”. “du” and “er” have the same form: du liest, er liest.',
         'Ganoon din ang “lesen”: e → ie sa “du” at “er/sie/es”. Pareho ang anyo ng “du” at “er”: du liest, er liest.',
         ['Ich lese die E-Mail.', 'Du liest viel.', 'Oma liest.']),
    RULE('hören, schreiben: regelmäßig', 'Bei „hören“ und „schreiben“ ändert sich der Vokal nicht. Die Endungen: ich -e, du -st, er/sie/es -t, wir/Sie/sie -en: ich höre, du hörst, er hört; ich schreibe, du schreibst, sie schreibt.',
         'With “hören” and “schreiben” the vowel does not change. Endings: ich -e, du -st, er/sie/es -t, wir/Sie/sie -en: ich höre, du hörst, er hört; ich schreibe, du schreibst, sie schreibt.',
         'Sa “hören” at “schreiben” hindi nagbabago ang patinig. Mga ending: ich -e, du -st, er/sie/es -t, wir/Sie/sie -en: ich höre, du hörst, er hört; ich schreibe, du schreibst, sie schreibt.',
         ['Ich schreibe eine E-Mail.', 'Du hörst Anna.', 'Lukas und Lena schreiben.']),
], [
    choice(X, 'lesen', L('Sie sehen vier Bilder. Jedes Bild zeigt einen Menschen mit einer Tätigkeit. Schauen Sie das Bild an.', 'You see four pictures. Each shows a person doing something. Look at the picture.', 'May apat na larawan. Bawat isa ay may taong may ginagawa. Tingnan ang larawan.'),
           'Was macht die Frau in Nummer 4?', 'Sie schreibt.', ['Sie liest.', 'Sie hört.'],
           L('Richtig: „Sie schreibt.“ In Nummer 4 hat die Frau Stift und Papier: schreiben. Nummer 3 hat ein Buch (lesen), Nummer 2 Kopfhörer (hören).',
             'Correct: “Sie schreibt.” In number 4 the woman has a pencil and paper: schreiben. Number 3 has a book (lesen), number 2 headphones (hören).',
             'Tama: “Sie schreibt.” Sa Nummer 4, may lapis at papel ang babae: schreiben. Ang Nummer 3 ay may libro (lesen), ang Nummer 2 ay may headphones (hören).'),
           [G5], R('schreiben'), img=VERBEN()),
    choice(X, 'lesen', L('Schauen Sie das Bild noch einmal an.', 'Look at the picture again.', 'Tingnan muli ang larawan.'),
           'In welchem Bild hört jemand?', 'Nummer 2', ['Nummer 1', 'Nummer 3'],
           L('Richtig: Nummer 2. Die Frau trägt Kopfhörer, über ihr sind Noten: sie hört. In Nummer 1 sieht der Mann einen Baum (sehen), in Nummer 3 liest der Mann ein Buch.',
             'Correct: Nummer 2. The woman wears headphones and there are music notes above her: she hears. In number 1 the man looks at a tree (sehen), in number 3 the man reads a book.',
             'Tama: Nummer 2. May headphones ang babae at may nota sa itaas niya: nakikinig siya. Sa Nummer 1, tinitingnan ng lalaki ang puno (sehen); sa Nummer 3, nagbabasa ang lalaki ng libro.'),
           [G5], R('hören'), img=VERBEN()),
    cloze(X, 'grammatikWortschatz', L('Anna und Lukas sind im Park. Setzen Sie das Verb in der richtigen Form ein.', 'Anna and Lukas are in the park. Put the verb in the right form.', 'Nasa park sina Anna at Lukas. Ilagay ang verb sa tamang anyo.'),
          'Du {{1}} die Kinder. Anna {{2}} die E-Mail.', [['siehst'], ['liest']],
          L('Richtig: du siehst, Anna liest. Bei „du“ und „er/sie/es“ wird e zu ie: sehen → du siehst, lesen → sie liest. Bei „lesen“ gibt es kein zusätzliches -t: „sie liest“, nicht „sie liesst“.',
            'Correct: du siehst, Anna liest. With “du” and “er/sie/es”, e becomes ie: sehen → du siehst, lesen → sie liest. “lesen” takes no extra -t: “sie liest”, not “sie liesst”.',
            'Tama: du siehst, Anna liest. Sa “du” at “er/sie/es”, ang e ay nagiging ie: sehen → du siehst, lesen → sie liest. Walang dagdag na -t ang “lesen”: “sie liest”, hindi “sie liesst”.'),
          [G5], R('sehen', 'lesen'), hints=['sehen', 'lesen']),
    cloze(X, 'grammatikWortschatz', L('Lena erzählt. Setzen Sie das Verb in der richtigen Form ein.', 'Lena tells a story. Put the verb in the right form.', 'Nagkukuwento si Lena. Ilagay ang verb sa tamang anyo.'),
          'Lukas und Lena {{1}} eine E-Mail. Ich {{2}} Peter.', [['schreiben'], ['höre']],
          L('Richtig: Lukas und Lena schreiben, ich höre. Bei „Lukas und Lena“ (sie, Plural) endet das Verb auf -en. Bei „ich“ endet es auf -e. „schreibt“ gehört zu er/sie/es (eine Person), nicht zu zwei Personen.',
            'Correct: Lukas und Lena schreiben, ich höre. With “Lukas und Lena” (they, plural) the verb ends in -en. With “ich” it ends in -e. “schreibt” belongs to er/sie/es (one person), not to two people.',
            'Tama: Lukas und Lena schreiben, ich höre. Sa “Lukas und Lena” (sila, plural), nagtatapos sa -en ang verb. Sa “ich”, sa -e. Ang “schreibt” ay para sa er/sie/es (isang tao), hindi sa dalawang tao.'),
          [G5], R('schreiben', 'hören'), hints=['schreiben', 'hören']),
    choice(X, 'grammatikWortschatz', L('Tom fragt seine Freundin Lena. Sie sagen „du“. Wählen Sie die richtige Form.', 'Tom asks his friend Lena. They say “du”. Choose the right form.', 'Tinatanong ni Tom ang kaibigan niyang si Lena. “du” ang gamit nila. Piliin ang tamang anyo.'),
           'Tom: „Lena, … du Lukas?“ (sehen)', 'siehst', ['sehst', 'sieht'],
           L('Richtig: „siehst du“. Bei „du“ wird „sehen“ zu „siehst“ (e → ie, Endung -st). „sehst“ vergisst den Vokalwechsel. „sieht“ gehört zu er/sie/es, nicht zu „du“.',
             'Correct: “siehst du”. With “du”, “sehen” becomes “siehst” (e → ie, ending -st). “sehst” forgets the vowel change. “sieht” belongs to er/sie/es, not “du”.',
             'Tama: “siehst du”. Sa “du”, ang “sehen” ay nagiging “siehst” (e → ie, ending -st). Nakalimutan ng “sehst” ang pagbabago ng patinig. Ang “sieht” ay para sa er/sie/es, hindi sa “du”.'),
           [G5], R('sehen')),
    choice(X, 'hoeren', L('Lena erzählt von Lukas und seiner Familie. Hören Sie.', 'Lena tells about Lukas and his family. Listen.', 'Nagkukuwento si Lena tungkol kay Lukas at sa pamilya niya. Makinig.'),
           'Wer liest?', 'Lukas', ['Lena', 'Anna'],
           L('Sie hören: „Das ist Lukas. Er liest. Ich bin Lena, ich sehe Lukas.“ „Er liest“ – Lukas liest. Lena sieht Lukas, sie liest nicht.',
             'You hear: “Das ist Lukas. Er liest. Ich bin Lena, ich sehe Lukas.” “Er liest” – Lukas is reading. Lena sees Lukas; she is not reading.',
             'Naririnig mo: “Das ist Lukas. Er liest. Ich bin Lena, ich sehe Lukas.” “Er liest” – nagbabasa si Lukas. Nakikita ni Lena si Lukas; hindi siya nagbabasa.'),
           [G5], R('lesen', 'sehen'), audio='Das ist Lukas. Er liest. Ich bin Lena, ich sehe Lukas.'),
    choice(X, 'sprechen', L('Sie sind im Park. Ihr Freund Lukas fragt Sie: „Siehst du Lena?“ Sie sehen Lena dort. Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'You are in the park. Your friend Lukas asks you: “Siehst du Lena?” You see Lena over there. What do you say? Choose, then say it aloud.', 'Nasa park ka. Tinanong ka ng kaibigan mong si Lukas: “Siehst du Lena?” Nakikita mo si Lena doon. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'),
           'Lukas: „Siehst du Lena?“', 'Ja, ich sehe Lena.', ['Ja, ich siehst Lena.', 'Ja, du siehst Lena.'],
           L('Richtig: „Ja, ich sehe Lena.“ Sie sprechen über sich: „ich“ + sehe. „ich siehst“ mischt zwei Formen. „du siehst“ wäre Lukas, nicht Sie.',
             'Correct: “Ja, ich sehe Lena.” You talk about yourself: “ich” + sehe. “ich siehst” mixes two forms. “du siehst” would be Lukas, not you.',
             'Tama: “Ja, ich sehe Lena.” Sarili mo ang pinag-uusapan: “ich” + sehe. Pinaghalo ng “ich siehst” ang dalawang anyo. Ang “du siehst” ay si Lukas, hindi ikaw.'),
           [G5], R('sehen')),
], intro=INTRO(L('Anna ist in Wien. Sie schreibt eine E-Mail an Tom. Sie liest die Antwort. Sie hört Lukas und sie sieht Lena.',
                 'Anna is in Vienna. She writes an e-mail to Tom. She reads the answer. She hears Lukas and sees Lena.',
                 'Nasa Vienna si Anna. Sumusulat siya ng e-mail kay Tom. Binabasa niya ang sagot. Naririnig niya si Lukas at nakikita niya si Lena.'),
               L('Am Ende kannst du sagen, was du siehst, hörst, liest und schreibst – mit der richtigen Verbform.',
                 'By the end you can say what you see, hear, read and write – with the right verb form.',
                 'Sa dulo, masasabi mo ang nakikita, naririnig, binabasa at isinusulat mo – gamit ang tamang anyo ng verb.')))

# L08 ------------------------------------------------------------------ Glücklich und traurig
HOCH = lambda: img('hochzeit', 'Ein Mann im dunklen Anzug und eine Frau im weißen Kleid mit Schleier stehen unter einem Bogen mit Blumen. Daneben die Namen Peter und Anna.', 'A man in a dark suit and a woman in a white dress with a veil stand under a flower arch. Their names are Peter and Anna.', 'Isang lalaking naka-dark suit at isang babaeng naka-puting damit at belo ang nakatayo sa ilalim ng arko ng bulaklak. Peter at Anna ang pangalan nila.')
lesson(8, L('Glücklich und traurig', 'Happy and sad', 'Masaya at malungkot'), ['glücklich', 'traurig', 'lieben', 'zufrieden'], [
    PHRASE('Ich bin glücklich. Ich bin zufrieden.', '„glücklich“ = sehr froh. „zufrieden“ = es ist gut genug, ich brauche nichts mehr. „zufrieden“ ist weniger stark als „glücklich“.',
           '“glücklich” = very happy. “zufrieden” = content, it is good enough, I need nothing more. “zufrieden” is weaker than “glücklich”.',
           '“glücklich” = napakasaya. “zufrieden” = kuntento, sapat na, wala nang kailangan. Mas mahina ang “zufrieden” kaysa “glücklich”.'),
    RULE('ich bin traurig · glücklich · zufrieden', 'Gefühle sagen Sie mit „sein“: ich bin, du bist, er ist, wir sind. Das Adjektiv bleibt gleich: Lena ist glücklich, Lukas ist traurig. „traurig“ ist das Gegenteil von „glücklich“.',
         'You say feelings with “sein”: ich bin, du bist, er ist, wir sind. The adjective does not change: Lena ist glücklich, Lukas ist traurig. “traurig” is the opposite of “glücklich”.',
         'Ang damdamin ay sinasabi gamit ang “sein”: ich bin, du bist, er ist, wir sind. Hindi nagbabago ang adjective: Lena ist glücklich, Lukas ist traurig. Kabaligtaran ng “glücklich” ang “traurig”.',
         ['Lena ist glücklich.', 'Lukas ist traurig.', 'Wir sind zufrieden.']),
    RULE('lieben: ich liebe · du liebst · er liebt', '„lieben“ ist regelmäßig: ich liebe, du liebst, er liebt, wir lieben. Sie lieben Menschen, die Ihnen sehr wichtig sind – zum Beispiel Ihre Familie.',
         '“lieben” (to love) is regular: ich liebe, du liebst, er liebt, wir lieben. You love people who are very important to you – for example your family.',
         'Regular ang “lieben” (magmahal): ich liebe, du liebst, er liebt, wir lieben. Minamahal mo ang mga taong napakahalaga sa iyo – halimbawa ang pamilya mo.',
         ['Ich liebe meine Kinder.', 'Peter liebt Anna.']),
    PHRASE('Der Opa ist gestorben. Wir sind traurig.', '„gestorben“ heißt: Der Mensch lebt nicht mehr. Dann sind die Menschen in der Familie traurig.',
           '“gestorben” means: the person is no longer alive. Then the people in the family are sad.',
           'Ang “gestorben” ay: hindi na buhay ang tao. Malungkot ang pamilya.'),
], [
    choice(X, 'lesen', L('Peter und Anna feiern ihre Hochzeit. Schauen Sie das Bild an.', 'Peter and Anna are at their wedding. Look at the picture.', 'Kasal nina Peter at Anna. Tingnan ang larawan.'),
           'Was machen Peter und Anna?', 'Sie heiraten.', ['Sie lesen.', 'Sie schreiben eine E-Mail.'],
           L('Richtig: „Sie heiraten.“ Das Bild zeigt eine Hochzeit: Anzug, weißes Kleid, Blumenbogen. Sie lesen oder schreiben nichts.',
             'Correct: “Sie heiraten.” The picture shows a wedding: suit, white dress, flower arch. They are not reading or writing anything.',
             'Tama: “Sie heiraten.” Kasal ang nasa larawan: suit, puting damit, arko ng bulaklak. Wala silang binabasa o isinusulat.'),
           [G5], R('heiraten'), img=HOCH()),
    choice(X, 'lesen', L('Schauen Sie das Bild noch einmal an. Sehen Sie auf die Gesichter.', 'Look at the picture again. Look at their faces.', 'Tingnan muli ang larawan. Tingnan ang mga mukha nila.'),
           'Peter und Anna sind …', 'glücklich', ['traurig', 'geschieden'],
           L('Richtig: glücklich. Peter und Anna lachen, über ihnen sind Herzen. „traurig“ passt nicht zu den Gesichtern. „geschieden“ heißt: nicht mehr verheiratet – aber sie heiraten gerade.',
             'Correct: glücklich. Peter and Anna are smiling and there are hearts above them. “traurig” does not fit their faces. “geschieden” means no longer married – but they are just getting married.',
             'Tama: glücklich. Nakangiti sina Peter at Anna at may mga puso sa itaas nila. Hindi bagay ang “traurig” sa mga mukha nila. Ang “geschieden” ay hindi na kasal – pero ikakasal pa lang sila.'),
           [G5], R('glücklich'), img=HOCH()),
    choice(X, 'grammatikWortschatz', L('Lukas erzählt. Welches Wort passt? Denken Sie an den Opa.', 'Lukas tells a story. Which word fits? Think of grandpa.', 'Nagkukuwento si Lukas. Aling salita ang bagay? Isipin ang lolo.'),
           'Der Opa ist gestorben. Die Familie ist …', 'traurig', ['glücklich', 'zufrieden'],
           L('Richtig: traurig. Wenn ein Mensch gestorben ist, ist die Familie traurig. „glücklich“ ist das Gegenteil. „zufrieden“ passt auch nicht: Das sagt man, wenn alles gut ist.',
             'Correct: traurig. When a person has died, the family is sad. “glücklich” is the opposite. “zufrieden” does not fit either: you say it when everything is fine.',
             'Tama: traurig. Kapag may namatay, malungkot ang pamilya. Kabaligtaran ang “glücklich”. Hindi rin bagay ang “zufrieden”: sinasabi ito kapag maayos ang lahat.'),
           [G5], R('traurig', 'gestorben')),
    cloze(X, 'grammatikWortschatz', L('Peter spricht über seine Familie. Ergänzen Sie. Nehmen Sie die Wörter unten.', 'Peter talks about his family. Complete the sentences. Use the words below.', 'Nagsasalita si Peter tungkol sa pamilya niya. Kumpletuhin. Gamitin ang mga salita sa ibaba.'),
          'Ich {{1}} meine Kinder. Und Peter {{2}} Anna.', [['liebe'], ['liebt']],
          L('Richtig: ich liebe, Peter liebt. Bei „ich“ endet das Verb auf -e, bei „Peter“ (er) auf -t. „liebst“ gehört zu „du“.',
            'Correct: ich liebe, Peter liebt. With “ich” the verb ends in -e, with “Peter” (er) in -t. “liebst” belongs to “du”.',
            'Tama: ich liebe, Peter liebt. Sa “ich”, nagtatapos sa -e ang verb; sa “Peter” (er), sa -t. Ang “liebst” ay para sa “du”.'),
          [G5], R('lieben'), bank=['liebe', 'liebt', 'liebst']),
    choice(X, 'hoeren', L('Peter und Anna erzählen. Hören Sie.', 'Peter and Anna tell a story. Listen.', 'Nagkukuwento sina Peter at Anna. Makinig.'),
           'Wie sind die Eltern?', 'glücklich', ['traurig', 'geschieden'],
           L('Sie hören: „Das Baby ist da! Wir sind sehr glücklich.“ Die Eltern freuen sich: glücklich. „traurig“ ist das Gegenteil. „geschieden“ ist ein Familienstand, kein Gefühl.',
             'You hear: “Das Baby ist da! Wir sind sehr glücklich.” The parents are pleased: glücklich. “traurig” is the opposite. “geschieden” is a marital status, not a feeling.',
             'Naririnig mo: “Das Baby ist da! Wir sind sehr glücklich.” Masaya ang mga magulang: glücklich. Kabaligtaran ang “traurig”. Ang “geschieden” ay civil status, hindi damdamin.'),
           [G5], R('glücklich'), audio='Das Baby ist da! Wir sind sehr glücklich.'),
    choice(X, 'sprechen', L('Ihr Freund Tom fragt: „Wie geht’s?“ Sie sind sehr glücklich: Ihre Tochter heiratet bald. Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'Your friend Tom asks: “Wie geht’s?” You are very happy: your daughter is getting married soon. What do you say? Choose, then say it aloud.', 'Tinanong ka ng kaibigan mong si Tom: “Wie geht’s?” Napakasaya mo: ikakasal na ang anak mong babae. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'),
           'Tom: „Wie geht’s?“', 'Sehr gut, ich bin glücklich.', ['Sehr gut, ich habe glücklich.', 'Sehr gut, ich liebe glücklich.'],
           L('Richtig: „Ich bin glücklich.“ Gefühle sagen Sie mit „sein“. „habe“ sagt, was Sie haben (Kinder, Geschwister), „lieben“ braucht einen Menschen: „ich liebe meine Tochter“.',
             'Correct: “Ich bin glücklich.” You say feelings with “sein”. “habe” says what you have (children, siblings); “lieben” needs a person: “ich liebe meine Tochter”.',
             'Tama: “Ich bin glücklich.” Ang damdamin ay gamit ang “sein”. Ang “habe” ay sa mayroon ka (anak, kapatid); ang “lieben” ay kailangan ng tao: “ich liebe meine Tochter”.'),
           [G5], R('glücklich', 'sein')),
    choice(X, 'lesen', L('Anna schreibt an Tom. Lesen Sie die E-Mail.', 'Anna writes to Tom. Read the e-mail.', 'Sumulat si Anna kay Tom. Basahin ang e-mail.'),
           'Servus Tom! Peter und ich heiraten bald. Meine Eltern sind glücklich. Mein Bruder ist traurig. Er wohnt in Graz. Servus, Anna\n\nWer ist traurig?', 'der Bruder', ['die Eltern', 'Peter'],
           L('Im Text: „Mein Bruder ist traurig.“ Die Eltern sind glücklich, Peter heiratet Anna und ist nicht traurig. „Er wohnt in Graz“ gehört zum Bruder.',
             'The text says: “Mein Bruder ist traurig.” The parents are happy; Peter is marrying Anna and is not sad. “Er wohnt in Graz” belongs to the brother.',
             'Sabi sa teksto: “Mein Bruder ist traurig.” Masaya ang mga magulang; ikakasal si Peter kay Anna at hindi malungkot. Ang “Er wohnt in Graz” ay tungkol sa kapatid.'),
           [G5], R('traurig', 'glücklich')),
], intro=INTRO(L('Peter und Anna heiraten. Lukas und Lena sind auch da. Alle sind glücklich.',
                 'Peter and Anna are getting married. Lukas and Lena are there. Everyone is happy. Only grandpa is no longer here.',
                 'Ikakasal sina Peter at Anna. Nandoon sina Lukas at Lena. Masaya ang lahat. Wala na lang ang lolo.'),
               L('Am Ende kannst du sagen, wie es dir geht (glücklich, traurig, zufrieden), und sagen, wen du liebst.',
                 'By the end you can say how you feel (happy, sad, content) and say whom you love.',
                 'Sa dulo, masasabi mo kung ano ang nararamdaman mo (masaya, malungkot, kuntento) at kung sino ang mahal mo.')))

# L09 ------------------------------------------------------------------ Freunde, Verwandte, Leute
LEUTE = lambda: img('leute', 'Fünf Menschen stehen zusammen: Opa und Oma mit grauen Haaren und Brille, zwei Kinder und eine junge Frau. Jeder hat ein Namensschild. Einer sagt „Hallo, Leute!“.', 'Five people stand together: grandpa and grandma with grey hair and glasses, two children and a young woman. Each has a name tag. One says “Hallo, Leute!”.', 'Limang tao ang magkakasama: lolo at lola na may puting buhok at salamin, dalawang bata at isang dalaga. Bawat isa ay may name tag. May nagsasabi ng “Hallo, Leute!”.')
lesson(9, L('Freunde, Verwandte, Leute', 'Friends, relatives, people', 'Kaibigan, kamag-anak, tao'), ['Freund, Freundin', 'Leute', 'Verwandte', 'Bekannte', 'Großeltern', 'Oma', 'Opa', 'leben', 'bleiben'], [
    RULE('die Großeltern: Oma und Opa', 'Oma = Großmutter, Opa = Großvater. Im Alltag sagt man fast nur „Oma“ und „Opa“. Oma und Opa zusammen sind die Großeltern – das Wort gibt es nur im Plural.',
         'Oma = grandmother, Opa = grandfather. In everyday speech people almost only say “Oma” and “Opa”. Oma and Opa together are the Großeltern – only in the plural.',
         'Oma = lola, Opa = lolo. Sa araw-araw, “Oma” at “Opa” halos ang sinasabi. Ang Oma at Opa na magkasama ay ang Großeltern – plural lang.',
         ['Das sind meine Großeltern.', 'Meine Oma heißt Maria.', 'Mein Opa heißt Franz.']),
    RULE('der Freund · die Freundin', 'Ein Freund oder eine Freundin ist ein Mensch, den Sie gern haben. „Mein Freund“ kann auch „mein Partner“ heißen. Der Satz zeigt, was gemeint ist: „Das ist mein Freund Tom. Wir heiraten bald.“',
         'A Freund or Freundin is a person you like. “Mein Freund” can also mean “my boyfriend”. The sentence shows which: “Das ist mein Freund Tom. Wir heiraten bald.”',
         'Ang Freund o Freundin ay taong gusto mo. Ang “mein Freund” ay puwede ring “nobyo ko”. Ipinapakita ng pangungusap kung alin: “Das ist mein Freund Tom. Wir heiraten bald.”',
         ['Das ist meine Freundin Sara.', 'Mein Freund wohnt in Graz.']),
    RULE('die Verwandten · die Bekannten · die Leute', 'Verwandte gehören zur Familie. Bekannte sind Menschen, die Sie kennen – aber keine Freunde. „die Leute“ heißt „die Menschen“ und gibt es nur im Plural. Im Alltag sagt man: „Hallo, Leute!“',
         'Verwandte (relatives) belong to the family. Bekannte (acquaintances) are people you know – but not friends. “die Leute” means “people” and only exists in the plural. In everyday speech: “Hallo, Leute!”',
         'Ang Verwandte ay kasama sa pamilya. Ang Bekannte ay mga taong kilala mo – pero hindi kaibigan. Ang “die Leute” ay “mga tao” at plural lang. Sa araw-araw: “Hallo, Leute!”',
         ['Meine Verwandten leben in Manila.', 'Viele Leute wohnen in Wien.']),
    RULE('leben · bleiben', '„leben“ sagt, wo jemand lebt: Meine Eltern leben in Manila. „bleiben“ sagt, dass jemand nicht weggeht: Ich bleibe in Wien. Beide sind regelmäßig: ich lebe, du lebst, er lebt; ich bleibe, du bleibst, er bleibt.',
         '“leben” says where someone lives: Meine Eltern leben in Manila. “bleiben” says that someone does not leave: Ich bleibe in Wien. Both are regular: ich lebe, du lebst, er lebt; ich bleibe, du bleibst, er bleibt.',
         'Sinasabi ng “leben” kung saan nakatira ang tao: Meine Eltern leben in Manila. Sinasabi ng “bleiben” na hindi umaalis ang tao: Ich bleibe in Wien. Parehong regular: ich lebe, du lebst, er lebt; ich bleibe, du bleibst, er bleibt.',
         ['Meine Eltern leben in Manila.', 'Ich bleibe in Wien.', 'Wo lebt dein Opa?']),
], [
    choice(X, 'lesen', L('Die Familie Huber ist zusammen. Auch eine Freundin ist da. Schauen Sie das Bild an.', 'The Huber family is together. A friend is there too. Look at the picture and count the people.', 'Magkakasama ang pamilyang Huber. Nandoon din ang isang kaibigan. Tingnan ang larawan at bilangin ang mga tao.'),
           'Wie viele Leute sind im Bild?', 'fünf', ['vier', 'sechs'],
           L('Richtig: fünf Leute – Opa, Oma, Lena, Lukas und Sara. „Leute“ ist der Plural von „Mensch“: viele Menschen. Jeder Mensch hat ein Namensschild, so zählen Sie ohne Fehler.',
             'Correct: fünf – Opa, Oma, Lena, Lukas and Sara. “Leute” means many people. Each person has a name tag, so you can count without mistakes.',
             'Tama: fünf – sina Opa, Oma, Lena, Lukas at Sara. Ang “Leute” ay maraming tao. Bawat tao ay may name tag, kaya madali ang bilang.'),
           [G1], R('Leute'), img=LEUTE()),
    choice(X, 'lesen', L('Schauen Sie das Bild noch einmal an. Die Großeltern haben graue Haare.', 'Look at the picture again. The grandparents have grey hair.', 'Tingnan muli ang larawan. Puti ang buhok ng mga lolo at lola.'),
           'Wer sind die Großeltern?', 'Oma und Opa', ['Lena und Lukas', 'Sara und Opa'],
           L('Richtig: Oma und Opa. Großeltern sind Oma und Opa zusammen. Lena und Lukas sind Kinder. Sara ist eine junge Frau, eine Freundin – keine Oma.',
             'Correct: Oma und Opa. Grandparents are Oma and Opa together. Lena and Lukas are children. Sara is a young woman, a friend – not a grandma.',
             'Tama: Oma und Opa. Ang Großeltern ay Oma at Opa na magkasama. Mga bata sina Lena at Lukas. Si Sara ay dalaga, kaibigan – hindi lola.'),
           [G1], R('Großeltern', 'Oma', 'Opa'), img=LEUTE()),
    choice(X, 'grammatikWortschatz', L('Lena zeigt auf Oma und Opa. Was sagt sie?', 'Lena points at Oma and Opa. What does she say?', 'Itinuturo ni Lena sina Oma at Opa. Ano ang sinasabi niya?'),
           'Lena: „Das sind meine …“', 'Großeltern', ['Eltern', 'Geschwister'],
           L('Richtig: Großeltern. Oma und Opa sind Lenas Großeltern. „Eltern“ sind Peter und Anna. „Geschwister“ wären Lukas und Sara oder Bruder und Schwester, nicht Oma und Opa.',
             'Correct: Großeltern. Oma and Opa are Lena’s grandparents. “Eltern” are Peter and Anna. “Geschwister” would be brothers and sisters, not Oma and Opa.',
             'Tama: Großeltern. Ang Oma at Opa ay mga lolo’t lola ni Lena. Ang “Eltern” ay sina Peter at Anna. Ang “Geschwister” ay magkapatid, hindi sina Oma at Opa.'),
           [G1], R('Großeltern')),
    cloze(X, 'grammatikWortschatz', L('Anna und Peter sprechen über ihre Familie. Ergänzen Sie den Dialog. Nehmen Sie die Wörter unten.', 'Anna and Peter talk about their family. Complete the dialogue. Use the words below.', 'Nag-uusap sina Anna at Peter tungkol sa pamilya nila. Kumpletuhin ang dialogo. Gamitin ang mga salita sa ibaba.'),
          'Peter: Wo {{1}} deine Eltern? – Anna: In Manila. – Peter: Bleibst du in Wien? – Anna: Ja, ich {{2}} in Wien.', [['leben'], ['bleibe']],
          L('Richtig: „Wo leben deine Eltern?“ und „Ich bleibe in Wien.“ „Eltern“ ist Plural: sie leben. Auf „Bleibst du …?“ antworten Sie mit „bleibe“. „bleibst“ gehört zu „du“, „lebt“ zu er/sie/es.',
            'Correct: “Wo leben deine Eltern?” and “Ich bleibe in Wien.” “Eltern” is plural: sie leben. You answer “Bleibst du …?” with “bleibe”. “bleibst” belongs to “du”, “lebt” to er/sie/es.',
            'Tama: “Wo leben deine Eltern?” at “Ich bleibe in Wien.” Plural ang “Eltern”: sie leben. Sa “Bleibst du …?” sasagot ka ng “bleibe”. Ang “bleibst” ay para sa “du”, ang “lebt” sa er/sie/es.'),
          [G5], R('leben', 'bleiben'), bank=['leben', 'bleibe', 'lebt', 'bleibst']),
    choice(X, 'hoeren', L('Ein Mann erzählt von seiner Familie. Hören Sie.', 'A man talks about his family. Listen.', 'May lalaking nagkukuwento tungkol sa pamilya niya. Makinig.'),
           'Wo bleibt der Mann?', 'in Wien', ['in Manila', 'in Graz'],
           L('Sie hören: „Meine Eltern leben in Manila. Ich bleibe in Wien.“ Die Eltern leben in Manila, der Mann bleibt in Wien. „in Graz“ kommt nicht vor.',
             'You hear: “Meine Eltern leben in Manila. Ich bleibe in Wien.” The parents live in Manila; the man stays in Vienna. “in Graz” is not mentioned.',
             'Naririnig mo: “Meine Eltern leben in Manila. Ich bleibe in Wien.” Nakatira sa Manila ang mga magulang; nananatili sa Vienna ang lalaki. Hindi binanggit ang “in Graz”.'),
           [G5], R('bleiben', 'leben'), audio='Meine Eltern leben in Manila. Ich bleibe in Wien.'),
    choice(X, 'sprechen', L('Sie sind im Park. Eine Frau fragt Sie: „Wer ist das?“ Sie zeigen auf Oma und Opa. Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'You are in the park. A woman asks you: “Wer ist das?” You point at your grandma and grandpa. What do you say? Choose, then say it aloud.', 'Nasa park ka. Tinanong ka ng isang babae: “Wer ist das?” Itinuturo mo ang lolo at lola mo. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'),
           'Frau: „Wer ist das?“', 'Das sind meine Großeltern.', ['Das ist meine Großeltern.', 'Das sind mein Großeltern.'],
           L('Richtig: „Das sind meine Großeltern.“ Großeltern ist Plural: „sind“ und „meine“. „Das ist“ passt zu einer Person. „mein“ passt zu „der“- und „das“-Wörtern, nicht zum Plural.',
             'Correct: “Das sind meine Großeltern.” Großeltern is plural: “sind” and “meine”. “Das ist” fits one person. “mein” fits “der” and “das” words, not the plural.',
             'Tama: “Das sind meine Großeltern.” Plural ang Großeltern: “sind” at “meine”. Ang “Das ist” ay para sa isang tao. Ang “mein” ay para sa “der” at “das” na salita, hindi sa plural.'),
           [G2], R('Großeltern', 'mein')),
    choice(X, 'lesen', L('Lukas schreibt an Tom. Lesen Sie die E-Mail.', 'Lukas writes to Tom. Read the e-mail.', 'Sumulat si Lukas kay Tom. Basahin ang e-mail.'),
           'Servus Tom! Wir sind sechs Leute: meine Eltern, meine Großeltern, mein Bruder und ich. Ich wohne in Wien. Meine Großeltern leben in Graz. Servus, Lukas\n\nWo leben die Großeltern?', 'in Graz', ['in Wien', 'in Manila'],
           L('Im Text: „Meine Großeltern leben in Graz.“ „in Wien“ ist der Wohnort von Lukas, nicht von den Großeltern. „in Manila“ steht nicht im Text.',
             'The text says: “Meine Großeltern leben in Graz.” “in Wien” is where Lukas lives, not the grandparents. “in Manila” is not in the text.',
             'Sabi sa teksto: “Meine Großeltern leben in Graz.” Ang “in Wien” ay tirahan ni Lukas, hindi ng mga lolo’t lola. Wala ang “in Manila” sa teksto.'),
           [G5], R('leben', 'Großeltern')),
], intro=INTRO(L('Die Familie Huber ist zusammen. Oma und Opa sind da. Auch Sara ist da: Sara ist eine Freundin.',
                 'The Huber family is together. Oma and Opa are there. Sara is there too: Sara is a friend.',
                 'Magkakasama ang pamilyang Huber. Nandoon sina Oma at Opa. Nandoon din si Sara: kaibigan siya.'),
               L('Am Ende kannst du sagen: Das sind meine Großeltern, das ist meine Freundin – und wo deine Verwandten leben.',
                 'By the end you can say: These are my grandparents, this is my friend – and where your relatives live.',
                 'Sa dulo, masasabi mo: Ito ang mga lolo’t lola ko, ito ang kaibigan ko – at kung saan nakatira ang mga kamag-anak mo.')))

# L10 ------------------------------------------------------------------ Familien in Österreich
lesson(10, L('Familien in Österreich', 'Families in Austria', 'Mga pamilya sa Austria'), [], [
    PHRASE('Vater, Mutter und Kind – das ist eine Familie.', 'Das ist die bekannte Form: Eltern und Kinder. Aber das ist nicht die einzige Form.',
           'This is the well-known form: parents and children. But it is not the only form.',
           'Ito ang kilalang anyo: magulang at mga anak. Pero hindi lang ito ang anyo.'),
    PHRASE('Mutter und Kind – das ist auch eine Familie.', 'Eine Mutter oder ein Vater kann allein mit dem Kind leben. Das ist auch eine Familie.',
           'A mother or a father can live alone with a child. That is a family too.',
           'Ang nanay o tatay ay puwedeng mag-isang kasama ang anak. Pamilya rin iyon.'),
    PHRASE('Oma und Kind – das ist auch eine Familie.', 'Manchmal leben Großeltern und Enkelkinder zusammen. „Enkelkind“ heißt: das Kind von meinem Sohn oder von meiner Tochter.',
           'Sometimes grandparents and grandchildren live together. “Enkelkind” means: the child of my son or daughter.',
           'Minsan magkasama ang mga lolo’t lola at apo. Ang “Enkelkind” ay anak ng anak ko.'),
    CULTURE('Familien in Österreich', 'In Österreich gibt es verschiedene Familienformen: Eltern mit Kindern, Paare ohne Kinder, eine Mutter oder ein Vater allein mit Kindern, Großeltern mit Enkelkindern und Patchwork-Familien (Eltern mit Kindern aus früheren Beziehungen).',
            'In Austria there are different family forms: parents with children, couples without children, a mother or father alone with children, grandparents with grandchildren, and patchwork families (parents with children from earlier relationships).',
            'Sa Austria may iba’t ibang anyo ng pamilya: magulang na may anak, mag-asawang walang anak, nanay o tatay na mag-isang may anak, lolo at lola kasama ang apo, at patchwork na pamilya (magulang na may anak mula sa naunang relasyon).'),
], [
    choice(X, 'werte', L('Sie sehen drei Familien im Park. Schauen Sie das Bild an.', 'You see three families in the park. Look at the picture.', 'May tatlong pamilya sa park. Tingnan ang larawan.'),
           'Nummer 1: eine Frau und ein Kind. Ist das eine Familie?', 'Ja.', ['Nein.'],
           L('Richtig: Ja. Auch eine Mutter allein mit ihrem Kind ist eine Familie. In Österreich gibt es viele Familienformen, nicht nur Vater, Mutter und Kinder.',
             'Correct: Ja. A mother alone with her child is a family too. In Austria there are many family forms, not only father, mother and children.',
             'Tama: Ja. Pamilya rin ang nanay na mag-isang kasama ang anak. Sa Austria may maraming anyo ng pamilya, hindi lang tatay, nanay at mga anak.'),
           [G6], R('Familie', 'Mutter'), img=FAM()),
    choice(X, 'werte', L('Schauen Sie das Bild noch einmal an. Unter den Erwachsenen stehen Namen.', 'Look at the picture again. The adults have name tags.', 'Tingnan muli ang larawan. May name tag ang mga nasa hustong gulang.'),
           'Nummer 3: Das Kind und … sind eine Familie.', 'die Oma', ['der Vater', 'die Mutter'],
           L('Richtig: die Oma. In Nummer 3 steht „Oma“ unter der Frau mit grauen Haaren und Brille. Großeltern mit Enkelkindern sind eine Familienform in Österreich. „Vater“ ist ein Mann, „Mutter“ ist in Nummer 1.',
             'Correct: die Oma. The woman with grey hair and glasses is the grandmother. Grandparents with grandchildren are a family form in Austria. “Vater” is a man; “Mutter” is in number 1.',
             'Tama: die Oma. Ang babaeng may puting buhok at salamin ay ang lola. Ang lolo’t lola kasama ang apo ay isang anyo ng pamilya sa Austria. Ang “Vater” ay lalaki; ang “Mutter” ay nasa Nummer 1.'),
           [G6], R('Oma', 'Familie'), img=FAM()),
    choice(X, 'werte', L('Schauen Sie das Bild noch einmal an. Eine Familie hat Vater, Mutter und Kind.', 'Look at the picture again. One family has father, mother and child.', 'Tingnan muli ang larawan. May tatay, nanay at anak ang isang pamilya.'),
           'Wo sind Vater, Mutter und Kind?', 'Nummer 2', ['Nummer 1', 'Nummer 3'],
           L('Richtig: Nummer 2 zeigt einen Mann, eine Frau und ein Kind. In Nummer 1 ist nur eine Frau, in Nummer 3 lebt eine Oma mit dem Kind. Alle drei Bilder zeigen eine Familie.',
             'Correct: Nummer 2 shows a man, a woman and a child. Number 1 has no man; in number 3 a grandma is with the child. All three pictures show a family.',
             'Tama: Ang Nummer 2 ay lalaki, babae at bata. Walang lalaki sa Nummer 1; sa Nummer 3 ang lola kasama ang bata. Lahat ng tatlong larawan ay pamilya.'),
           [G6], R('Familie', 'Eltern'), img=FAM()),
    choice(X, 'werte', CHOOSE,
           'Welcher Satz ist richtig?', 'Auch eine Mutter und ein Kind sind eine Familie.', ['Nur Vater, Mutter und Kinder sind eine Familie.'],
           L('Richtig: Auch eine Mutter und ein Kind sind eine Familie. In Österreich gibt es verschiedene Familienformen. Der zweite Satz ist falsch, weil er nur eine Form nennt.',
             'Correct: a mother and a child are a family too. In Austria there are different family forms. The second sentence is wrong because it names only one form.',
             'Tama: pamilya rin ang nanay at anak. Sa Austria may iba’t ibang anyo ng pamilya. Mali ang ikalawang pangungusap dahil isa lang ang binabanggit na anyo.'),
           [G6], R('Familie')),
    choice(X, 'werte', L('Eine Frau, ihre Mutter und ihr Kind wohnen zusammen. Eine Freundin fragt Sie.', 'A woman, her mother and her child live together. A friend asks you.', 'Magkasamang nakatira ang isang babae, ang nanay niya at ang anak niya. May kaibigang nagtanong sa iyo.'),
           'Ist das eine Familie?', 'Ja.', ['Nein.'],
           L('Richtig: Ja. Drei Menschen aus der Familie wohnen zusammen: Großmutter, Mutter und Kind. In Österreich gibt es viele Familienformen, auch mit Oma.',
             'Correct: Ja. Three family members live together: grandmother, mother and child. In Austria there are many family forms, also with a grandmother.',
             'Tama: Ja. Tatlong miyembro ng pamilya ang magkasama: lola, nanay at anak. Sa Austria may maraming anyo ng pamilya, kasama ang lola.'),
           [G6], R('Familie', 'Oma')),
    choice(X, 'hoeren', L('Ein Mädchen erzählt von seiner Familie. Hören Sie.', 'A girl tells about her family. Listen.', 'Nagkukuwento ang isang batang babae tungkol sa pamilya niya. Makinig.'),
           'Wer lebt in Wien?', 'die Mutter und das Kind', ['der Vater und das Kind', 'der Vater und die Mutter'],
           L('Sie hören: „Meine Eltern sind geschieden. Mein Vater lebt in Graz. Meine Mutter und ich leben in Wien.“ In Wien leben die Mutter und das Mädchen. Der Vater lebt in Graz.',
             'You hear: “Meine Eltern sind geschieden. Mein Vater lebt in Graz. Meine Mutter und ich leben in Wien.” In Vienna live the mother and the girl. The father lives in Graz.',
             'Naririnig mo: “Meine Eltern sind geschieden. Mein Vater lebt in Graz. Meine Mutter und ich leben in Wien.” Sa Vienna nakatira ang nanay at ang batang babae. Ang tatay ay sa Graz.'),
           [G6], R('leben', 'Eltern'), audio='Meine Eltern sind geschieden. Mein Vater lebt in Graz. Meine Mutter und ich leben in Wien.'),
    cloze(X, 'grammatikWortschatz', L('Lena erzählt von Familien. Ergänzen Sie. Nehmen Sie die Wörter unten.', 'Lena tells about families. Complete the sentences. Use the words below.', 'Nagkukuwento si Lena tungkol sa mga pamilya. Kumpletuhin. Gamitin ang mga salita sa ibaba.'),
          'Vater, Mutter und Kind sind eine {{1}}. Oma und Kind sind auch eine {{2}}.', [['Familie'], ['Familie']],
          L('Richtig: Familie – zweimal. Beide Gruppen sind eine Familie. „Eltern“ passt nicht: „eine Eltern“ geht nicht, „Eltern“ ist Plural.',
            'Correct: Familie – twice. Both groups are a family. “Eltern” does not fit: “eine Eltern” is impossible, “Eltern” is plural.',
            'Tama: Familie – dalawang beses. Parehong grupo ay pamilya. Hindi bagay ang “Eltern”: hindi puwede ang “eine Eltern”, plural ang “Eltern”.'),
          [G6], R('Familie'), bank=['Familie', 'Familie', 'Eltern']),
], intro=INTRO(L('Sie sind im Park. Sie sehen drei Familien.',
                 'You are in the park. You see three families. Every family looks different.',
                 'Nasa park ka. May nakikita kang tatlong pamilya. Magkakaiba ang hitsura ng bawat isa.'),
               L('Am Ende kannst du sagen: In Österreich gibt es viele Familienformen – auch Mutter und Kind oder Oma und Kind sind eine Familie.',
                 'By the end you can say: in Austria there are many family forms – a mother and child or a grandma and child are a family too.',
                 'Sa dulo, masasabi mo: sa Austria may maraming anyo ng pamilya – pamilya rin ang nanay at anak o ang lola at anak.')))

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
fam('GW4', RELQ, [('Der Vater von meinem Vater ist mein …', 'Opa', ['Bruder', 'Sohn'], 'Vater vom Vater = Opa.'), ('Der Vater von meiner Mutter ist mein …', 'Opa', ['Bruder', 'Sohn'], 'Vater der Mutter = Opa.'), ('Mein Bruder und meine Schwester sind meine …', 'Geschwister', ['Eltern', 'Großeltern'], 'Bruder + Schwester = Geschwister.')],
    [('Die Mutter von meinem Vater ist meine …', 'Oma', ['Tochter', 'Schwester'], 'Mutter vom Vater = Oma.'), ('Die Mutter von meiner Mutter ist meine …', 'Oma', ['Schwester', 'Tochter'], 'Mutter der Mutter = Oma.'), ('Oma und Opa sind meine …', 'Großeltern', ['Geschwister', 'Kinder'], 'Oma + Opa = Großeltern.'), ('Mutter und Vater sind meine …', 'Eltern', ['Großeltern', 'Geschwister'], 'Mutter + Vater = Eltern.')])

WQ = lambda v, i: choice(i, 'werte', CHOOSE, v[0], v[1], [v[2]], WOW, [G6], R('Familie'))
fam('WE1', WQ, [('Eine Mutter lebt allein mit ihrem Kind. Ist das eine Familie?', 'Ja.', 'Nein.'), ('Ein Vater lebt mit seinem Kind und der Oma. Ist das eine Familie?', 'Ja.', 'Nein.'), ('Ein Paar hat keine Kinder. Ist das eine Familie?', 'Ja, auch ohne Kinder.', 'Nein, nur mit Kindern.')],
    [('Ein Vater lebt allein mit zwei Kindern. Ist das eine Familie?', 'Ja.', 'Nein.'), ('Opa und Oma leben mit dem Kind von ihrer Tochter. Ist das eine Familie?', 'Ja.', 'Nein.')])
fam('WE2', WQ, [('Gibt es in Österreich nur eine Familienform?', 'Nein, es gibt viele Familienformen.', 'Ja, nur eine.'), ('Eine Patchwork-Familie ist …', 'eine Familie mit Kindern aus einer früheren Beziehung', 'eine Familie ohne Eltern'), ('Welcher Satz ist richtig?', 'Familien sind verschieden.', 'Alle Familien sind gleich groß.')],
    [('Hat eine Familie immer Kinder?', 'Nein.', 'Ja.'), ('Leben alle Familien gleich?', 'Nein, Familien leben verschieden.', 'Ja, alle gleich.')])
fam('WE3', lambda v, i: choice(i, 'werte', LOOK, v[0], v[1], [v[2]], WOW, [G6], R('Familie'), img=FAM()),
    [('Bild 3: Wer ist hier mit dem Kind?', 'die Oma', 'der Vater'), ('In welchem Bild sind Vater, Mutter und Kind?', 'Bild 2', 'Bild 1'), ('Wie viele Familien zeigt das Bild?', 'drei', 'zwei')],
    [('Bild 1: Wie viele Erwachsene sind in Bild 1?', 'eine', 'zwei'), ('In welchem Bild ist die Oma?', 'Bild 3', 'Bild 1')])

fam('LE4', lambda v, i: choice(i, 'lesen', READ, v[0], v[1], [v[2]], same(v[3]), [G1, G3], R('Familie')),
    [], [('Herr Bauer ist 70. Seine Frau ist gestorben. Er lebt jetzt bei seiner Tochter.\nLebt Herr Bauer allein?', 'Nein, bei seiner Tochter.', 'Ja, allein.', 'Er lebt bei seiner Tochter.'),
         ('Anna und Tom heiraten bald. Sie sind sehr glücklich.\nSind Anna und Tom schon verheiratet?', 'Nein, noch nicht.', 'Ja.', 'Sie heiraten bald.'),
         ('Lena hat einen Bruder und zwei Schwestern.\nWie viele Geschwister hat Lena?', 'drei', 'zwei', '1 Bruder + 2 Schwestern = 3.'),
         ('Meine Großeltern leben in Wien, meine Eltern in Linz.\nWo leben die Eltern?', 'in Linz', 'in Wien', 'meine Eltern in Linz')])
fam('WE4', WQ, [], [('Ein Paar ohne Kinder: Ist das eine Familie?', 'Ja.', 'Nein.'), ('Eine Oma lebt mit ihrer Tochter und dem Baby. Ist das eine Familie?', 'Ja.', 'Nein.'),
                    ('Was ist eine Familie?', 'Menschen zusammen – in vielen Familienformen', 'nur Vater, Mutter und zwei Kinder'), ('Patchwork-Familie: Die Kinder kommen …', 'auch aus einer früheren Beziehung', 'immer aus dem Ausland'),
                    ('Eltern, Kinder und Oma wohnen zusammen. Ist das eine Familie?', 'Ja.', 'Nein.'), ('Sind alle Familien gleich groß?', 'Nein.', 'Ja.')])

write_svgs('/tmp/a1-04.png')
write_all(V, GOALS, {'lesen': 3, 'hoeren': 3, 'schreiben': 3, 'sprechen': 5, 'grammatikWortschatz': 3, 'werte': 3})
