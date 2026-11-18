# A1-01 "Grüß Gott und Servus" – lessons and pictures (content standard v2). Run: python3 scripts/content/a1-01.py
# Writes src/lib/content/a1-01.json (vocab + 7 lessons) and static/img/a1-01-*.svg.
# The pools (src/lib/content/a1-01-pools.json) were written by hand and are NOT touched by this script.
import json
import lib
lib.init('A1-01', seed=20261118, sources=[])
from lib import *  # noqa: E402,F403

# The hand-written A1-01 file lists the set words "grüß Gott" and "servus" in `introduces` of lesson 1 (cards for all 44 words).
lib.NO_CARD.clear()

GOALS = {
    'A1-01-G1': L('Grüßen und sich verabschieden', 'Greeting and saying goodbye', 'Bumati at magpaalam'),
    'A1-01-G2': L('Sich mit Namen vorstellen', 'Introducing yourself by name', 'Magpakilala gamit ang pangalan'),
    'A1-01-G3': L('du oder Sie – höflich ansprechen', 'du or Sie – addressing people politely', 'du o Sie – magalang na pakikipag-usap'),
    'A1-01-G4': L('Fragen zu Name und Herkunft', 'Questions about name and origin', 'Mga tanong tungkol sa pangalan at pinagmulan'),
    'A1-01-G5': L('Die Verben sein, heißen, kommen', 'The verbs sein, heißen, kommen', 'Ang mga pandiwang sein, heißen, kommen'),
    'A1-01-G6': L("Wie geht's? Danke, ja, nein", 'How are you? Thanks, yes, no', 'Kumusta? Salamat, oo, hindi'),
    'A1-01-G7': L('Pronomen ich, du, er, sie, wir, ihr', 'Pronouns ich, du, er, sie, wir, ihr', 'Mga panghalip na ich, du, er, sie, wir, ihr'),
}
G1, G2, G3, G4, G5, G6, G7 = GOALS

# Vocabulary of the chapter in the order of the existing file: 03c lemma -> (lemma shown in the app, article, en, tl). Glosses unchanged (proofread in 037).
VOCAB = {
    'grüß Gott': ('grüß Gott', None, 'hello (standard greeting in Austria)', 'kumusta po (karaniwang pagbati sa Austria)'),
    'servus': ('servus', None, 'hi / bye (among friends)', 'hi / paalam (sa kaibigan)'),
    'hallo': ('hallo', None, 'hello (informal)', 'hello (di-pormal)'),
    'guten Morgen': ('guten Morgen', None, 'good morning', 'magandang umaga'),
    'guten Tag': ('guten Tag', None, 'hello / good day (during the day)', 'magandang araw'),
    'guten Abend': ('guten Abend', None, 'good evening', 'magandang gabi (pagdating)'),
    'gute Nacht': ('gute Nacht', None, 'good night (going to bed)', 'magandang gabi (bago matulog)'),
    'auf Wiedersehen': ('auf Wiedersehen', None, 'goodbye (polite)', 'paalam (magalang)'),
    'tschüss': ('tschüss', None, 'bye (informal)', 'paalam (di-pormal)'),
    'ich': ('ich', None, 'I', 'ako'),
    'heißen': ('heißen', None, 'to be called', 'tawagin / pangalan ay'),
    'Name': ('Name', 'der', 'name', 'pangalan'),
    'Vorname': ('Vorname', 'der', 'first name', 'pangalan (unang pangalan)'),
    'Familienname': ('Familienname', 'der', 'family name', 'apelyido'),
    'Herr': ('Herr', 'der', 'Mr / gentleman', 'Ginoo'),
    'Frau': ('Frau', 'die', 'Ms / woman', 'Ginang / babae'),
    'wie': ('wie', None, 'how', 'paano'),
    'Sie': ('Sie', None, 'you (polite)', 'kayo / ikaw (magalang)'),
    'du': ('du', None, 'you (informal)', 'ikaw (di-pormal)'),
    'woher': ('woher', None, 'where … from', 'taga-saan'),
    'kommen': ('kommen', None, 'to come', 'dumating / manggaling'),
    'sein (Verb)': ('sein', None, 'to be', 'maging (ay)'),
    'wer': ('wer', None, 'who', 'sino'),
    'Österreich': ('Österreich', None, 'Austria', 'Austria'),
    'Philippinen': ('Philippinen', None, 'Philippines', 'Pilipinas'),
    "Wie geht's?": ("Wie geht's?", None, 'How are you?', 'Kumusta?'),
    'danke': ('danke', None, 'thank you', 'salamat'),
    'bitte': ('bitte', None, "please / you're welcome", 'pakiusap / walang anuman'),
    'gut': ('gut', None, 'good, well', 'mabuti'),
    'sehr': ('sehr', None, 'very', 'napaka- / sobra'),
    'Entschuldigung': ('Entschuldigung', 'die', 'sorry / excuse me', 'paumanhin'),
    'dir': ('dir', None, '(to) you (informal)', 'sa iyo'),
    'und': ('und', None, 'and', 'at'),
    'er': ('er', None, 'he', 'siya (lalaki)'),
    'sie': ('sie', None, 'she', 'siya (babae)'),
    'es': ('es', None, 'it', 'ito'),
    'ja': ('ja', None, 'yes', 'oo'),
    'nein': ('nein', None, 'no', 'hindi'),
    'auch': ('auch', None, 'also, too', 'din / rin'),
    'was': ('was', None, 'what', 'ano'),
    'wir': ('wir', None, 'we', 'kami / tayo'),
    'ihr': ('ihr', None, 'you (several friends)', 'kayo (mga kaibigan)'),
    'mir': ('mir', None, '(to) me', 'sa akin'),
    'vorstellen (sich)': ('sich vorstellen', None, 'to introduce oneself', 'magpakilala'),
}

# ---------------------------------------------------------------- pictures (flat style, see content standard §5)
FLAG_AT = lambda x, y, w=34, h=22: (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#fff" stroke="#6b7280" stroke-width="1"/>'
                                    f'<rect x="{x}" y="{y}" width="{w}" height="{h/3:.1f}" fill="#c8102e"/><rect x="{x}" y="{y + 2*h/3:.1f}" width="{w}" height="{h/3:.1f}" fill="#c8102e"/>')
FLAG_PH = lambda x, y, w=34, h=22: (f'<rect x="{x}" y="{y}" width="{w}" height="{h/2}" fill="#0038a8"/><rect x="{x}" y="{y + h/2}" width="{w}" height="{h/2}" fill="#ce1126"/>'
                                    f'<path d="M{x} {y}L{x + w*0.5} {y + h/2}L{x} {y + h}z" fill="#fff"/><circle cx="{x + w*0.14}" cy="{y + h/2}" r="{h*0.1}" fill="#fcd116"/>'
                                    f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="#6b7280" stroke-width="1"/>')
MARIA = dict(shirt='#c8102e', skin='b', hair='#222', long=True)
JONAS = dict(shirt='#e76f51', skin='a', hair='#2b2118')
ANNA = dict(shirt='#2a9d8f', skin='a', hair='#4a2f1c', long=True)
JOSE = dict(shirt='#1d4e89', skin='b', hair='#222')


def tag(x, y, text, w=76):
    """White name sign, text 15 px."""
    return f'<rect x="{x - w/2}" y="{y}" width="{w}" height="26" rx="6" fill="#fff" stroke="#34506b" stroke-width="2.5"/>' + label(x, y + 19, text, 15)


def who(x, p, bottom, s):
    """Bust of one of the recurring people, its lower edge at y = bottom."""
    return person(x, p['shirt'], p['skin'], p['hair'], y=bottom - 260, s=s, long=p.get('long', False))


# 1 amt – Jonas Huber enters the office of Anna Gruber (name signs 15 px, readable on a phone)
PICS['amt'] = '''<rect width="400" height="260" fill="#f3ead9"/><rect y="196" width="400" height="64" fill="#d9c3a3"/>
<rect x="24" y="30" width="96" height="88" rx="4" fill="#9ed8ff" stroke="#fff" stroke-width="8"/>
<circle cx="96" cy="56" r="13" fill="#ffd23f"/><path d="M28 104q22-22 44-8t44-10v28H28z" fill="#7cc36a"/>
<path d="M72 30v88M24 74h96" stroke="#fff" stroke-width="5"/>
<circle cx="206" cy="58" r="28" fill="#fff" stroke="#3a3a3a" stroke-width="4"/>
<g stroke="#3a3a3a" stroke-width="4" stroke-linecap="round"><path d="M206 58V38"/><path d="M206 58l-13-8"/></g>
<g fill="#3a3a3a"><circle cx="206" cy="35" r="1.5"/><circle cx="229" cy="58" r="1.5"/><circle cx="206" cy="81" r="1.5"/><circle cx="183" cy="58" r="1.5"/></g>
<rect x="268" y="34" width="108" height="34" rx="6" fill="#34506b"/><text x="322" y="57" font-size="18" font-weight="bold" fill="#fff" text-anchor="middle">Büro</text>
<path d="M286 150q0-30 30-30t30 30v40h-60z" fill="#2a9d8f"/>
<circle cx="316" cy="104" r="19" fill="#f1c9a5"/>
<path d="M296 106q-3-30 20-30t20 30q-4-16-20-16t-20 16z" fill="#4a2f1c"/><path d="M296 104q-4 20 2 30l6-4q-6-12-2-24zM336 104q4 20-2 30l-6-4q6-12 2-24z" fill="#4a2f1c"/>
<circle cx="309" cy="104" r="2" fill="#333"/><circle cx="323" cy="104" r="2" fill="#333"/><path d="M309 112q7 6 14 0" fill="none" stroke="#b5533c" stroke-width="2.5" stroke-linecap="round"/>
<rect x="232" y="176" width="156" height="14" rx="3" fill="#8a5a2b"/><rect x="244" y="190" width="12" height="52" fill="#734a22"/><rect x="364" y="190" width="12" height="52" fill="#734a22"/>
<rect x="350" y="152" width="32" height="24" rx="3" fill="#555"/><rect x="346" y="174" width="40" height="4" rx="2" fill="#777"/>
<rect x="232" y="146" width="112" height="30" rx="4" fill="#fff" stroke="#34506b" stroke-width="3"/><text x="288" y="167" font-size="16" font-weight="bold" fill="#1c2733" text-anchor="middle">Anna Gruber</text>
<rect x="131" y="196" width="13" height="44" rx="5" fill="#2f3e56"/><rect x="150" y="196" width="13" height="44" rx="5" fill="#2f3e56"/>
<ellipse cx="137" cy="242" rx="11" ry="5" fill="#222"/><ellipse cx="157" cy="242" rx="11" ry="5" fill="#222"/>
<path d="M122 150q0-26 25-26t25 26v52h-50z" fill="#e76f51"/>
<path d="M170 140l24-30" stroke="#e76f51" stroke-width="13" stroke-linecap="round"/><circle cx="196" cy="106" r="8" fill="#e0b08a"/>
<path d="M124 142l-8 40" stroke="#e76f51" stroke-width="13" stroke-linecap="round"/><circle cx="115" cy="186" r="7" fill="#e0b08a"/>
<circle cx="147" cy="106" r="19" fill="#e0b08a"/><path d="M128 102q2-22 19-22t19 22q-8-10-19-10t-19 10z" fill="#2b2118"/>
<circle cx="141" cy="106" r="2" fill="#333"/><circle cx="154" cy="106" r="2" fill="#333"/><path d="M141 114q6 6 13 0" fill="none" stroke="#9c4a35" stroke-width="2.5" stroke-linecap="round"/>
<path d="M140 126l8 18 8-18" fill="none" stroke="#34506b" stroke-width="2.5"/>
<rect x="92" y="146" width="112" height="30" rx="4" fill="#fff" stroke="#34506b" stroke-width="3"/><text x="148" y="167" font-size="16" font-weight="bold" fill="#1c2733" text-anchor="middle">Jonas Huber</text>'''

# 2 nacht – child's bedroom at night (unchanged except for a larger clock)
PICS['nacht'] = '''<rect width="400" height="260" fill="#27365c"/><rect y="204" width="400" height="56" fill="#1b2542"/>
<rect x="30" y="28" width="104" height="96" rx="4" fill="#0e1730" stroke="#c9d3ea" stroke-width="8"/>
<path d="M100 48a22 22 0 1 0 16 36a26 26 0 0 1-16-36z" fill="#ffe89a"/>
<g fill="#fff"><circle cx="52" cy="50" r="2.5"/><circle cx="70" cy="84" r="2"/><circle cx="48" cy="104" r="2"/><circle cx="84" cy="44" r="1.8"/><circle cx="116" cy="106" r="2"/></g>
<path d="M82 28v96M30 76h104" stroke="#c9d3ea" stroke-width="5"/>
<rect x="146" y="170" width="54" height="46" rx="4" fill="#6b4a2b"/>
<rect x="146" y="148" width="54" height="22" rx="4" fill="#111"/><text x="173" y="165" font-size="16" font-weight="bold" fill="#7dff8a" text-anchor="middle">21:00</text>
<rect x="204" y="150" width="14" height="76" rx="5" fill="#7a5230"/><rect x="204" y="186" width="176" height="30" rx="6" fill="#7a5230"/><rect x="366" y="170" width="14" height="56" rx="5" fill="#7a5230"/>
<rect x="222" y="158" width="52" height="30" rx="12" fill="#fff"/>
<circle cx="250" cy="160" r="16" fill="#f1c9a5"/><path d="M234 158q2-18 16-18t16 18q-6-8-16-8t-16 8z" fill="#6b3f1d"/>
<path d="M243 160q3 3 6 0M252 160q3 3 6 0" fill="none" stroke="#333" stroke-width="2" stroke-linecap="round"/><path d="M246 168q4 3 8 0" fill="none" stroke="#b5533c" stroke-width="2" stroke-linecap="round"/>
<path d="M262 170q60-22 116 6v22H262z" fill="#5fa8d3"/><path d="M262 170q60-22 116 6" fill="none" stroke="#3f86b3" stroke-width="3"/>
<g fill="#fff" opacity=".8"><circle cx="300" cy="180" r="3"/><circle cx="330" cy="174" r="3"/><circle cx="356" cy="184" r="3"/><circle cx="316" cy="192" r="3"/></g>
<text x="276" y="140" font-size="18" font-weight="bold" fill="#c9d3ea">z</text><text x="288" y="126" font-size="14" font-weight="bold" fill="#c9d3ea">z</text>
<rect x="64" y="200" width="12" height="40" rx="5" fill="#3b3054"/><rect x="82" y="200" width="12" height="40" rx="5" fill="#3b3054"/>
<path d="M54 156q0-26 25-26t25 26v50H54z" fill="#c2185b"/>
<path d="M102 146l26-22" stroke="#c2185b" stroke-width="12" stroke-linecap="round"/><circle cx="131" cy="121" r="7" fill="#f1c9a5"/>
<circle cx="79" cy="112" r="18" fill="#f1c9a5"/><path d="M60 114q-2-30 19-30t19 30q-4-16-19-16t-19 16z" fill="#3a2414"/><path d="M60 112q-4 22 2 34l6-4q-6-14-2-28z" fill="#3a2414"/>
<circle cx="74" cy="112" r="2" fill="#333"/><circle cx="87" cy="112" r="2" fill="#333"/><path d="M74 120q6 5 13 0" fill="none" stroke="#b5533c" stroke-width="2.5" stroke-linecap="round"/>'''


# 3 tageszeit – three times of day: sky, sun or moon, digital clock (07:00 · 14:00 · 19:00)
def day_panel(x, n, sky, sun, clock, ground):
    return (panel(x, 14, 124, 232, n)
            + f'<rect x="{x + 12}" y="44" width="100" height="92" rx="4" fill="{sky}" stroke="#c4ccd6" stroke-width="6"/>' + sun
            + f'<path d="M{x + 15} 133v-12q22-16 44-4t50-6v22z" fill="{ground}"/>'
            + f'<rect x="{x + 22}" y="150" width="80" height="34" rx="6" fill="#111"/>' + label(x + 62, 175, clock, 22, '#7dff8a')
            + who(x + 62, JONAS, 236, 0.36))


PICS['tageszeit'] = (
    day_panel(8, 1, '#ffd9a8', '<circle cx="48" cy="112" r="17" fill="#f58a1f"/><path d="M48 80v-10M22 90l-8-7M74 90l8-7" stroke="#f58a1f" stroke-width="4" stroke-linecap="round"/>', '07:00', '#5aa65a')
    + day_panel(138, 2, '#8fd0ff', '<circle cx="190" cy="68" r="15" fill="#ffd23f"/><path d="M190 44v-5M190 92v5M166 68h-5M214 68h5" stroke="#ffd23f" stroke-width="3" stroke-linecap="round"/>', '14:00', '#7cc36a')
    + day_panel(268, 3, '#1f2d52', '<path d="M338 62a15 15 0 1 0 11 24a18 18 0 0 1-11-24z" fill="#ffe89a"/><g fill="#fff"><circle cx="300" cy="66" r="2"/><circle cx="364" cy="60" r="2"/><circle cx="318" cy="100" r="2"/><circle cx="372" cy="98" r="2"/></g>', '19:00', '#2f4a45'))

# 4 formular – Maria Santos on a registration form (Frau ticked)
PICS['formular'] = ('<rect x="36" y="14" width="328" height="232" rx="8" fill="#fff" stroke="#9ca3af" stroke-width="2"/><rect x="36" y="14" width="328" height="42" rx="8" fill="#34506b"/><rect x="36" y="38" width="328" height="18" fill="#34506b"/>'
                    + label(200, 44, 'Name', 22, '#fff')
                    + '<rect x="62" y="76" width="26" height="26" fill="#fff" stroke="#1f2937" stroke-width="2.5"/>' + label(98, 97, 'Herr', 19, anchor='start', bold=False)
                    + '<rect x="186" y="76" width="26" height="26" fill="#fff" stroke="#1f2937" stroke-width="2.5"/>' + label(222, 97, 'Frau', 19, anchor='start', bold=False)
                    + '<path d="M191 81l16 16M207 81l-16 16" stroke="#c8102e" stroke-width="4.5" stroke-linecap="round"/>'
                    + label(62, 140, 'Vorname', 17, '#6b7280', 'start', False) + '<path d="M62 176h276" stroke="#9ca3af" stroke-width="2"/>'
                    + label(62, 170, 'Maria', 26, '#1d4e89', 'start')
                    + label(62, 198, 'Familienname', 17, '#6b7280', 'start', False) + '<path d="M62 234h276" stroke="#9ca3af" stroke-width="2"/>'
                    + label(62, 228, 'Santos', 26, '#1d4e89', 'start'))

# 5 dusie – two situations: a counter in the office (Grüß Gott, Frau Gruber) and two friends (Servus)
PICS['dusie'] = (panel(8, 10, 188, 240, 1) + panel(204, 10, 188, 240, 2)
                 + bubble(30, 38, 108, 'Grüß Gott!', 17, tail_x=62) + who(62, MARIA, 214, 0.62) + who(142, ANNA, 214, 0.62)
                 + '<rect x="108" y="190" width="80" height="24" fill="#8a5a2b"/>'
                 + tag(56, 220, 'Maria', 66) + tag(146, 220, 'Frau Gruber', 92)
                 + bubble(224, 38, 104, 'Servus!', 17, tail_x=256) + who(256, MARIA, 214, 0.62) + who(336, JOSE, 214, 0.62)
                 + tag(256, 220, 'Maria', 70) + tag(336, 220, 'Jose', 70))

# 6 situationen – 1: Herr Huber bumps into Frau Gruber, apples fall · 2: Jonas brings Frau Santos a coffee
APPLE = lambda x, y: f'<circle cx="{x}" cy="{y}" r="9" fill="#c8102e"/><path d="M{x} {y-9}q2-6 6-6" stroke="#4a7c2f" stroke-width="2.5" fill="none"/>'
PICS['situationen'] = (panel(8, 10, 188, 240, 1) + panel(204, 10, 188, 240, 2)
                       # 1 collision
                       + '<g transform="rotate(14 56 200)">' + who(56, JONAS, 200, 0.6) + '</g>' + who(140, ANNA, 200, 0.6)
                       + '<path d="M148 150h40v44h-40z" fill="#c9a36a" stroke="#8a6a43" stroke-width="2"/>'
                       + APPLE(160, 206) + APPLE(178, 214) + APPLE(130, 214) + APPLE(188, 202) + '<path d="M26 202h160" stroke="#c4ccd6" stroke-width="2"/>'
                       + label(98, 40, '!', 30, '#c8102e')
                       + tag(54, 226, 'Herr Huber', 84) + tag(146, 226, 'Frau Gruber', 90)
                       # 2 café: Jonas serves a cup to Frau Santos
                       + who(254, MARIA, 190, 0.6) + '<rect x="222" y="170" width="86" height="12" rx="3" fill="#8a5a2b"/><rect x="258" y="182" width="10" height="34" fill="#734a22"/>'
                       + who(346, JONAS, 190, 0.6) + '<path d="M324 148l-26 8" stroke="#e76f51" stroke-width="10" stroke-linecap="round"/><circle cx="296" cy="157" r="6" fill="#e0b08a"/>'
                       + '<path d="M284 146h20l-3 14h-14z" fill="#fff" stroke="#6b7280" stroke-width="2"/><path d="M304 148q8 0 8 6t-8 6" fill="none" stroke="#6b7280" stroke-width="2"/><path d="M290 138q-3-6 0-12M298 138q-3-6 0-12" stroke="#9ca3af" stroke-width="2" fill="none"/>'
                       + tag(254, 226, 'Frau Santos', 100) + tag(346, 226, 'Jonas', 62))

# 7 kurs – three people with name tags and their country (Maria: Philippinen · Jonas, Anna: Österreich)
PICS['kurs'] = ''.join(who(x, p, 146, 0.6) + f'<rect x="{x - 64}" y="154" width="128" height="30" rx="5" fill="#fff" stroke="#34506b" stroke-width="3"/>' + label(x, 175, n, 15)
                       + (FLAG_PH(x - 52, 202) if c == 'Philippinen' else FLAG_AT(x - 52, 202)) + label(x - 12, 219, c, 15, anchor='start', bold=False)
                       for x, p, n, c in ((70, MARIA, 'Maria Santos', 'Philippinen'), (200, JONAS, 'Jonas Huber', 'Österreich'), (330, ANNA, 'Anna Gruber', 'Österreich')))

# 8 paare – Anna and Jonas (Österreich) ask Maria and Jose (Philippinen): „Woher kommt ihr?“
PICS['paare'] = (bubble(20, 8, 186, 'Woher kommt ihr?', 17, tail_x=86)
                 + who(52, ANNA, 168, 0.55) + who(120, JONAS, 168, 0.55) + who(280, MARIA, 168, 0.55) + who(348, JOSE, 168, 0.55)
                 + tag(52, 174, 'Anna', 62) + tag(120, 174, 'Jonas', 62) + tag(280, 174, 'Maria', 62) + tag(348, 174, 'Jose', 62)
                 + FLAG_AT(56, 214, 44, 28) + label(78, 258, 'Österreich', 15, bold=False) + FLAG_PH(292, 214, 44, 28) + label(314, 258, 'Philippinen', 15, bold=False))


# ---------------------------------------------------------------- lessons (content standard v2: intro + cards + 6–8 items)
X = ''
LOOK = L('Schauen Sie das Bild an.', 'Look at the picture.', 'Tingnan ang larawan.')


def alt(name, de_, en, tl):
    return lambda: img(name, de_, en, tl)


TAGESZEIT = alt('tageszeit', 'Drei Fenster mit Himmel und Uhr. Bild 1: oranger Himmel, Uhr 07:00. Bild 2: blauer Himmel mit hoher Sonne, Uhr 14:00. Bild 3: dunkler Himmel mit Mond und Sternen, Uhr 19:00. Unter jeder Uhr steht ein Mann.',
                'Three windows with sky and clock. Picture 1: orange sky, clock 07:00. Picture 2: blue sky with a high sun, clock 14:00. Picture 3: dark sky with moon and stars, clock 19:00. A man stands under each clock.',
                'Tatlong bintana na may langit at orasan. Larawan 1: kulay-kahel na langit, orasan 07:00. Larawan 2: asul na langit at mataas na araw, orasan 14:00. Larawan 3: madilim na langit na may buwan at mga bituin, orasan 19:00. May lalaking nakatayo sa ilalim ng bawat orasan.')
AMT = alt('amt', 'Ein Büro am Vormittag. Frau Gruber sitzt am Schreibtisch, Herr Huber kommt herein und winkt. Beide haben ein Namensschild, an der Wand hängt eine Uhr.',
          'An office in the morning. Frau Gruber sits at her desk, Herr Huber comes in and waves. Both have a name sign, and there is a clock on the wall.',
          'Isang opisina sa umaga. Nakaupo si Frau Gruber sa mesa, pumapasok si Herr Huber at kumakaway. May name sign silang dalawa, at may orasan sa dingding.')
NACHT = alt('nacht', 'Nacht im Kinderzimmer: Ein Kind liegt im Bett und schläft ein, die Mutter steht am Bett und winkt. Draußen sind Mond und Sterne, die Uhr zeigt 21:00.',
            'Night in a child’s bedroom: a child lies in bed and is falling asleep, the mother stands by the bed and waves. Outside there are the moon and stars, the clock shows 21:00.',
            'Gabi sa kuwarto ng bata: nakahiga ang bata sa kama at patulog na, nakatayo ang nanay sa tabi ng kama at kumakaway. May buwan at mga bituin sa labas, 21:00 ang nasa orasan.')
FORM = alt('formular', 'Ein Formular mit der Überschrift „Name“. Bei „Herr“ und „Frau“ ist ein Kästchen angekreuzt. Darunter stehen zwei Zeilen: „Vorname“ und „Familienname“, beide ausgefüllt.',
           'A form headed “Name”. One of the boxes “Herr” and “Frau” is ticked. Below are two filled-in lines: “Vorname” and “Familienname”.',
           'Isang form na may pamagat na “Name”. May ekis ang isa sa mga kahong “Herr” at “Frau”. Sa ibaba ay may dalawang linyang may sagot: “Vorname” at “Familienname”.')
DUSIE = alt('dusie', 'Zwei Bilder. Bild 1: Maria sagt „Grüß Gott!“ zu Frau Gruber, neben Frau Gruber steht ein Tisch. Bild 2: Maria sagt „Servus!“ zu Jose.',
            'Two pictures. Picture 1: Maria says “Grüß Gott!” to Frau Gruber, who stands next to a desk. Picture 2: Maria says “Servus!” to Jose.',
            'Dalawang larawan. Larawan 1: Sinasabi ni Maria ang “Grüß Gott!” kay Frau Gruber, na nakatayo sa tabi ng mesa. Larawan 2: Sinasabi ni Maria ang “Servus!” kay Jose.')
SITUATION = alt('situationen', 'Zwei Bilder. Bild 1: Herr Huber stößt gegen Frau Gruber, ihr Papiersackerl ist offen und Äpfel fallen heraus. Bild 2: Jonas bringt Frau Santos eine Tasse Kaffee an den Tisch.',
                'Two pictures. Picture 1: Herr Huber bumps into Frau Gruber, her paper bag is open and apples fall out. Picture 2: Jonas brings Frau Santos a cup of coffee at her table.',
                'Dalawang larawan. Larawan 1: Nabangga ni Herr Huber si Frau Gruber, bukas ang paper bag niya at nalalaglag ang mga mansanas. Larawan 2: Dinadalhan ni Jonas si Frau Santos ng tasa ng kape sa mesa niya.')
KURS = alt('kurs', 'Drei Personen mit Namensschild. Maria Santos hat die Flagge der Philippinen und das Wort „Philippinen“ darunter. Jonas Huber und Anna Gruber haben die rot-weiß-rote Flagge und das Wort „Österreich“ darunter.',
           'Three people with name signs. Maria Santos has the flag of the Philippines and the word “Philippinen” under it. Jonas Huber and Anna Gruber have the red-white-red flag and the word “Österreich” under it.',
           'Tatlong taong may name sign. Si Maria Santos ay may bandila ng Pilipinas at ang salitang “Philippinen” sa ilalim. Sina Jonas Huber at Anna Gruber ay may pula-puti-pulang bandila at ang salitang “Österreich” sa ilalim.')
PAARE = alt('paare', 'Zwei Paare. Links Anna und Jonas mit der österreichischen Flagge, rechts Maria und Jose mit der Flagge der Philippinen. Über dem linken Paar steht die Sprechblase „Woher kommt ihr?“.',
            'Two pairs. On the left Anna and Jonas with the Austrian flag, on the right Maria and Jose with the flag of the Philippines. Above the left pair there is a speech bubble: “Woher kommt ihr?”.',
            'Dalawang magkapareha. Sa kaliwa sina Anna at Jonas na may bandila ng Austria, sa kanan sina Maria at Jose na may bandila ng Pilipinas. Sa itaas ng kaliwang pares ay may speech bubble: “Woher kommt ihr?”.')

# fixed option order for "Bild 1 / Bild 2 / Bild 3"
def ordered(it, options, answer):
    it['options'], it['answer'] = options, answer
    return it


# L01 ------------------------------------------------------------------ greetings
lesson(1, L('Grüß Gott und Servus', 'Hello and goodbye', 'Pagbati at pagpapaalam'),
       ['grüß Gott', 'servus', 'hallo', 'guten Morgen', 'guten Tag', 'guten Abend', 'gute Nacht', 'auf Wiedersehen', 'tschüss'], [
    PHRASE('Grüß Gott!', 'So grüßen Sie in Österreich: höflich, zu jeder Tageszeit, auch zu Menschen, die Sie nicht kennen. Die Antwort ist wieder „Grüß Gott!“.',
           'This is how you greet people in Austria: politely, at any time of day, also people you do not know. The answer is “Grüß Gott!” again.',
           'Ganito ang pagbati sa Austria: magalang, anumang oras ng araw, kahit sa mga hindi mo kilala. Ang sagot ay “Grüß Gott!” din.'),
    RULE('Guten Morgen · Guten Tag · Guten Abend', 'Der Gruß passt zur Tageszeit: früh am Tag „Guten Morgen“, untertags „Guten Tag“, am Abend „Guten Abend“. Wann genau der Abend beginnt, ist nicht fest – wenn es dunkel wird, passt „Guten Abend“ sicher.',
         'The greeting matches the time of day: early in the day “Guten Morgen”, during the day “Guten Tag”, in the evening “Guten Abend”. There is no exact time when the evening starts – when it gets dark, “Guten Abend” is always right.',
         'Ang pagbati ay ayon sa oras ng araw: maaga ang “Guten Morgen”, sa araw ang “Guten Tag”, sa gabi ang “Guten Abend”. Walang eksaktong oras kung kailan nagsisimula ang gabi – kapag dumidilim na, tama palagi ang “Guten Abend”.',
         ['Guten Morgen, Frau Gruber!', 'Guten Tag, Herr Huber!', 'Guten Abend, Frau Santos!']),
    RULE('Gute Nacht! – nur vor dem Schlafen', '„Gute Nacht“ ist kein Gruß zum Kommen. Sie sagen es, wenn jemand schlafen geht. Wer am Abend kommt, sagt „Guten Abend“. Achtung: Nacht ist „die Nacht“, darum „Gute“ – bei Morgen, Tag und Abend heißt es „Guten“.',
         '“Gute Nacht” is not a greeting for arriving. You say it when someone goes to sleep. Anyone arriving in the evening says “Guten Abend”. Careful: Nacht is “die Nacht”, so it is “Gute” – with Morgen, Tag and Abend it is “Guten”.',
         'Hindi pagbati sa pagdating ang “Gute Nacht”. Sinasabi ito kapag may matutulog na. Ang dumarating sa gabi ay nagsasabi ng “Guten Abend”. Pansin: “die Nacht” ang Nacht, kaya “Gute” – sa Morgen, Tag at Abend ay “Guten”.',
         ['Gute Nacht, Maria!', 'Guten Abend, Maria!']),
    PHRASE('Servus! · Hallo! · Tschüss!', 'Für Freunde und Familie. „Servus“ passt beim Kommen und beim Gehen. „Hallo“ sagen Sie beim Kommen, „Tschüss“ beim Gehen.',
           'For friends and family. “Servus” works when you arrive and when you leave. You say “Hallo” when you arrive and “Tschüss” when you leave.',
           'Para sa mga kaibigan at pamilya. Ang “Servus” ay para sa pagdating at pag-alis. Ang “Hallo” ay sinasabi sa pagdating, ang “Tschüss” sa pag-alis.'),
    CULTURE('Auf Wiedersehen!', 'Beim Gehen sagen Sie höflich „Auf Wiedersehen!“ – zum Beispiel im Büro, im Geschäft oder bei einer Ärztin. In Österreich hören Sie oft auch „Auf Wiederschauen!“. Unter Freunden reicht „Servus!“ oder „Tschüss!“.',
            'When you leave, you politely say “Auf Wiedersehen!” – for example in an office, a shop or at the doctor’s. In Austria you also often hear “Auf Wiederschauen!”. Among friends “Servus!” or “Tschüss!” is enough.',
            'Sa pag-alis, magalang na sinasabi ang “Auf Wiedersehen!” – halimbawa sa opisina, sa tindahan o sa doktor. Sa Austria madalas ding maririnig ang “Auf Wiederschauen!”. Sa mga kaibigan, sapat na ang “Servus!” o “Tschüss!”.'),
], [
    choice(X, 'lesen', L('Schauen Sie das Bild an.', 'Jonas Huber comes to the office three times: in the morning, in the afternoon and in the evening. Look at the sky and the clock in picture 3.',
                         'Tatlong beses na pumupunta si Jonas Huber sa opisina: sa umaga, sa hapon at sa gabi. Tingnan ang langit at ang orasan sa larawan 3.'),
           'Bild 3: Was sagt Jonas?', 'Guten Abend!', ['Guten Morgen!', 'Gute Nacht!'],
           L('Richtig: „Guten Abend!“ Bild 3 zeigt 19:00 und der Himmel ist dunkel: Es ist Abend. „Gute Nacht“ sagt man nicht beim Kommen, sondern vor dem Schlafen. „Guten Morgen“ passt zu Bild 1.',
             'Correct: “Guten Abend!” Picture 3 shows 7 p.m. and the sky is dark: it is evening. You do not say “Gute Nacht” when you arrive, but before going to sleep. “Guten Morgen” fits picture 1.',
             'Tama: “Guten Abend!” Ipinapakita ng larawan 3 ang 7:00 ng gabi at madilim ang langit: gabi na. Hindi sinasabi ang “Gute Nacht” sa pagdating kundi bago matulog. Ang “Guten Morgen” ay para sa larawan 1.'),
           [G1], R('guten Abend', 'gute Nacht', 'guten Morgen'), img=TAGESZEIT()),
    choice(X, 'lesen', L('Schauen Sie das Bild an.', 'Jonas Huber comes into the office of Frau Gruber. He does not know her well. Look at the name signs. What does he say?',
                         'Pumapasok si Jonas Huber sa opisina ni Frau Gruber. Hindi niya siya lubos na kilala. Tingnan ang mga name sign. Ano ang sinasabi niya?'),
           'Was sagt Jonas?', 'Grüß Gott, Frau Gruber!', ['Gute Nacht, Frau Gruber!', 'Tschüss, Frau Gruber!'],
           L('Richtig: „Grüß Gott, Frau Gruber!“ „Grüß Gott“ ist der höfliche Gruß beim Kommen, zu jeder Tageszeit. „Gute Nacht“ ist für das Schlafengehen, „Tschüss“ ist ein Gruß zum Gehen unter Freunden.',
             'Correct: “Grüß Gott, Frau Gruber!” “Grüß Gott” is the polite greeting when you arrive, at any time of day. “Gute Nacht” is for going to sleep, “Tschüss” is a goodbye among friends.',
             'Tama: “Grüß Gott, Frau Gruber!” Ang “Grüß Gott” ay ang magalang na pagbati sa pagdating, anumang oras. Ang “Gute Nacht” ay para sa pagtulog, ang “Tschüss” ay paalam sa mga kaibigan.'),
           [G1], R('grüß Gott', 'Frau'), img=AMT()),
    ordered(choice(X, 'hoeren', L('Hören Sie. Zu welchem Bild passt der Gruß?', 'Jonas greets Frau Gruber. Listen and look at the three pictures again: which picture fits the greeting?',
                                  'Binabati ni Jonas si Frau Gruber. Makinig at tingnan muli ang tatlong larawan: aling larawan ang tugma sa pagbati?'),
                   None, 'Bild 1', ['Bild 2', 'Bild 3'],
                   L('Sie hören: „Guten Morgen, Frau Gruber!“ „Morgen“ passt zu Bild 1: Die Sonne geht auf, die Uhr zeigt 07:00. Um 14:00 (Bild 2) und um 19:00 (Bild 3) wäre „Guten Morgen“ nicht richtig.',
                     'You hear: “Guten Morgen, Frau Gruber!” “Morgen” fits picture 1: the sun is rising and the clock shows 07:00. At 14:00 (picture 2) and at 19:00 (picture 3) “Guten Morgen” would not be right.',
                     'Naririnig mo: “Guten Morgen, Frau Gruber!” Ang “Morgen” ay para sa larawan 1: sumisikat ang araw at 07:00 ang orasan. Sa 14:00 (larawan 2) at sa 19:00 (larawan 3) hindi tama ang “Guten Morgen”.'),
                   [G1], R('guten Morgen'), audio='Guten Morgen, Frau Gruber!', img=TAGESZEIT()), ['Bild 1', 'Bild 2', 'Bild 3'], 0),
    choice(X, 'grammatikWortschatz', L('Maria sieht ihren Freund Jose auf der Straße. Was sagt sie?', 'Maria sees her friend Jose in the street. What does she say?', 'Nakita ni Maria ang kaibigan niyang si Jose sa kalye. Ano ang sinasabi niya?'),
           None, 'Servus, Jose!', ['Auf Wiedersehen, Jose!', 'Gute Nacht, Jose!'],
           L('Richtig: „Servus, Jose!“ „Servus“ ist der Gruß unter Freunden. „Auf Wiedersehen“ sagt man beim Gehen und eher höflich, nicht beim Treffen. „Gute Nacht“ ist nur für das Schlafengehen.',
             'Correct: “Servus, Jose!” “Servus” is the greeting among friends. “Auf Wiedersehen” is said when leaving, and is rather polite, not when meeting. “Gute Nacht” is only for going to sleep.',
             'Tama: “Servus, Jose!” Ang “Servus” ay pagbati ng magkakaibigan. Ang “Auf Wiedersehen” ay sinasabi sa pag-alis at medyo magalang, hindi sa pagkikita. Ang “Gute Nacht” ay para lang sa pagtulog.'),
           [G1], R('servus')),
    cloze(X, 'grammatikWortschatz', L('Ergänzen Sie die Sätze.', 'Jonas comes into the office and later leaves again. Complete what he says with the words below.', 'Pumapasok si Jonas sa opisina at pagkatapos ay umaalis. Kumpletuhin ang sinasabi niya gamit ang mga salita sa ibaba.'),
          'Jonas kommt: „{{1}} Gott, Frau Gruber!“\nJonas geht: „Auf {{2}}, Frau Gruber!“', [['Grüß'], ['Wiedersehen']],
          L('Richtig: „Grüß Gott“ beim Kommen, „Auf Wiedersehen“ beim Gehen. „Gott“ und „Wiedersehen“ schreibt man groß. „Guten Gott“ gibt es nicht, und „Tschüss“ ist ein anderes Wort: „Auf Tschüss“ ist falsch.',
            'Correct: “Grüß Gott” when arriving, “Auf Wiedersehen” when leaving. “Gott” and “Wiedersehen” are written with a capital letter. There is no “Guten Gott”, and “Tschüss” is a different word: “Auf Tschüss” is wrong.',
            'Tama: “Grüß Gott” sa pagdating, “Auf Wiedersehen” sa pag-alis. Nakasulat nang malaki ang unang titik ng “Gott” at “Wiedersehen”. Walang “Guten Gott”, at ibang salita ang “Tschüss”: mali ang “Auf Tschüss”.'),
          [G1], R('grüß Gott', 'auf Wiedersehen'), bank=['Grüß', 'Wiedersehen', 'Guten', 'Tschüss']),
    cloze(X, 'lesen', L('Schauen Sie das Bild an. Schreiben Sie die zwei Wörter.', 'Maria’s mother says goodnight to her daughter. Look at the picture and complete the greeting with the words below.', 'Binabati ng nanay ni Maria ang anak niya ng magandang gabi bago matulog. Tingnan ang larawan at kumpletuhin ang pagbati gamit ang mga salita sa ibaba.'),
          '„{{1}} {{2}}, Maria!“', [['Gute'], ['Nacht']],
          L('Richtig: „Gute Nacht, Maria!“ Das Bild zeigt die Nacht (Mond, 21:00), das Kind geht schlafen. „Guten Morgen“ wäre falsch. Und: „die Nacht“ → „Gute“, nicht „Guten“.',
            'Correct: “Gute Nacht, Maria!” The picture shows the night (moon, 21:00), the child is going to sleep. “Guten Morgen” would be wrong. And: “die Nacht” → “Gute”, not “Guten”.',
            'Tama: “Gute Nacht, Maria!” Ipinapakita ng larawan ang gabi (buwan, 21:00), matutulog na ang bata. Mali ang “Guten Morgen”. At: “die Nacht” → “Gute”, hindi “Guten”.'),
          [G1], R('gute Nacht'), img=NACHT(), bank=['Gute', 'Nacht', 'Guten', 'Morgen']),
    choice(X, 'sprechen', L('Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'You leave the office. Frau Gruber is still working. What do you say? Choose, then say it aloud.', 'Aalis ka sa opisina. Nagtatrabaho pa si Frau Gruber. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'),
           None, 'Auf Wiedersehen, Frau Gruber!', ['Guten Morgen, Frau Gruber!', 'Hallo, Frau Gruber!'],
           L('Richtig: „Auf Wiedersehen, Frau Gruber!“ Beim Gehen sagt man höflich „Auf Wiedersehen“. „Guten Morgen“ und „Hallo“ sind Grüße zum Kommen, „Hallo“ ist außerdem zu locker für Frau Gruber.',
             'Correct: “Auf Wiedersehen, Frau Gruber!” When leaving you politely say “Auf Wiedersehen”. “Guten Morgen” and “Hallo” are greetings for arriving, and “Hallo” is also too casual for Frau Gruber.',
             'Tama: “Auf Wiedersehen, Frau Gruber!” Sa pag-alis, magalang na sinasabi ang “Auf Wiedersehen”. Ang “Guten Morgen” at “Hallo” ay pagbati sa pagdating, at ang “Hallo” ay masyadong kaswal para kay Frau Gruber.'),
           [G1], R('auf Wiedersehen', 'hallo')),
    short(X, 'schreiben', L('Schreiben Sie, was Sie antworten.', 'It is morning. You come into the office, and Frau Gruber greets you. Write your answer.', 'Umaga na. Pumasok ka sa opisina at binati ka ni Frau Gruber. Isulat ang sagot mo.'),
          'Frau Gruber: „Guten Morgen!“ – Sie: „…“',
          ['Guten Morgen!', 'Guten Morgen, Frau Gruber!', 'Grüß Gott!', 'Grüß Gott, Frau Gruber!'],
          L('Richtig: „Guten Morgen!“ oder „Grüß Gott!“ Man grüßt zurück, mit demselben Gruß oder mit „Grüß Gott“. „Guten“ und „Morgen“ schreibt man groß.',
            'Correct: “Guten Morgen!” or “Grüß Gott!” You greet back, with the same greeting or with “Grüß Gott”. “Guten” and “Morgen” are written with a capital letter.',
            'Tama: “Guten Morgen!” o “Grüß Gott!” Binabati mo pabalik, gamit ang parehong pagbati o ang “Grüß Gott”. Nakasulat nang malaki ang unang titik ng “Guten” at “Morgen”.'),
          [G1], R('guten Morgen', 'grüß Gott')),
], intro=INTRO(
    L('Anna Gruber arbeitet im Büro in Wien. Jonas Huber kommt am Morgen, am Abend sagt er „Auf Wiedersehen“. Was sagt man wann?',
      'Anna Gruber works in an office in Vienna. Jonas Huber arrives in the morning and says goodbye in the evening. Which greeting is right at which moment?',
      'Nagtatrabaho si Anna Gruber sa isang opisina sa Vienna. Dumarating si Jonas Huber sa umaga at nagpapaalam sa gabi. Aling pagbati ang tama sa bawat oras?'),
    L('zu jeder Tageszeit grüßen und sich verabschieden – höflich („Grüß Gott“) und unter Freunden („Servus“).',
      'greet people at any time of day and say goodbye – politely (“Grüß Gott”) and among friends (“Servus”).',
      'bumati at magpaalam anumang oras ng araw – magalang (“Grüß Gott”) at sa mga kaibigan (“Servus”).')))

# L02 ------------------------------------------------------------------ names
lesson(2, L('Ich heiße …', 'My name is …', 'Ang pangalan ko ay …'), ['ich', 'heißen', 'Name', 'Vorname', 'Familienname', 'Herr', 'Frau', 'wie', 'Sie'], [
    PHRASE('Wie heißen Sie? – Ich heiße Jonas Huber.', 'So fragen Sie höflich nach dem Namen und so antworten Sie. Kürzer geht auch: „Ich bin Jonas Huber.“',
           'This is how you politely ask for a name and how you answer. A shorter answer is also correct: “Ich bin Jonas Huber.”',
           'Ganito magalang na itanong ang pangalan at ganito sumagot. Puwede rin ang mas maikli: “Ich bin Jonas Huber.”'),
    RULE('ich heiße · Sie heißen', 'Das Verb ändert sich mit der Person. Bei „ich“ endet es auf -e, bei „Sie“ auf -en. Darum: „Wie heißen Sie?“, aber „Ich heiße …“.',
         'The verb changes with the person. With “ich” it ends in -e, with “Sie” in -en. That is why: “Wie heißen Sie?”, but “Ich heiße …”.',
         'Nagbabago ang verb ayon sa tao. Sa “ich”, nagtatapos ito sa -e; sa “Sie”, sa -en. Kaya: “Wie heißen Sie?”, pero “Ich heiße …”.',
         ['Ich heiße Maria.', 'Wie heißen Sie?']),
    RULE('Vorname + Familienname = Name', 'Der Vorname ist der erste Teil des Namens (Maria), der Familienname der zweite (Santos). Beim Sprechen sagen Sie zuerst den Vornamen. Auf Formularen stehen beide in getrennten Feldern.',
         'The Vorname is the first part of the name (Maria), the Familienname the second (Santos). When speaking, you say the Vorname first. On forms both have their own field.',
         'Ang Vorname ang unang bahagi ng pangalan (Maria), ang Familienname ang pangalawa (Santos). Sa pagsasalita, unang sinasabi ang Vorname. Sa mga form, may sariling kahon ang bawat isa.',
         ['Maria ist der Vorname.', 'Santos ist der Familienname.', 'Maria Santos ist der Name.']),
    RULE('Herr / Frau + Familienname', 'Höflich sagen Sie „Herr“ oder „Frau“ und den Familiennamen: Herr Huber, Frau Gruber. Mit dem Vornamen („Herr Jonas“) ist es nicht die übliche höfliche Anrede.',
         'To be polite, you say “Herr” or “Frau” and the family name: Herr Huber, Frau Gruber. With the first name (“Herr Jonas”) it is not the usual polite form of address.',
         'Para maging magalang, sinasabi ang “Herr” o “Frau” at ang apelyido: Herr Huber, Frau Gruber. Kapag Vorname ang gamit (“Herr Jonas”), hindi ito ang karaniwang magalang na pagtawag.',
         ['Grüß Gott, Herr Huber!', 'Guten Tag, Frau Gruber!']),
], [
    choice(X, 'lesen', L('Schauen Sie das Bild an.', 'Maria Santos registers for a German course in Vienna. Look at the form. Which sentence is correct?', 'Nagpaparehistro si Maria Santos sa isang kursong German sa Vienna. Tingnan ang form. Aling pangungusap ang tama?'),
           None, 'Der Vorname ist Maria. Der Familienname ist Santos.', ['Der Vorname ist Santos. Der Familienname ist Maria.', 'Der Vorname ist Maria. Der Familienname ist Frau.'],
           L('Richtig: Beim Feld „Vorname“ steht Maria, beim Feld „Familienname“ steht Santos. „Frau“ gehört nicht zum Namen: Es zeigt nur, dass Maria eine Frau ist.',
             'Correct: next to “Vorname” it says Maria, next to “Familienname” it says Santos. “Frau” is not part of the name: it only shows that Maria is a woman.',
             'Tama: sa tabi ng “Vorname” ay Maria, sa tabi ng “Familienname” ay Santos. Hindi bahagi ng pangalan ang “Frau”: ipinapakita lang nito na babae si Maria.'),
           [G2], R('Vorname', 'Familienname'), img=FORM()),
    choice(X, 'lesen', L('Schauen Sie das Bild an.', 'Jonas Huber meets Maria Santos in the course. Look at the form: is she a Frau or a Herr? What does he say?', 'Nakilala ni Jonas Huber si Maria Santos sa kurso. Tingnan ang form: Frau ba siya o Herr? Ano ang sinasabi niya?'),
           'Was sagt Jonas?', 'Grüß Gott, Frau Santos!', ['Grüß Gott, Herr Santos!', 'Grüß Gott, Frau Maria!'],
           L('Richtig: „Grüß Gott, Frau Santos!“ Auf dem Formular ist „Frau“ angekreuzt, und höflich sagt man Frau + Familienname. „Herr“ ist für Männer. „Frau Maria“ nennt den Vornamen und ist nicht die übliche höfliche Anrede.',
             'Correct: “Grüß Gott, Frau Santos!” On the form “Frau” is ticked, and politely you say Frau + family name. “Herr” is for men. “Frau Maria” uses the first name and is not the usual polite form of address.',
             'Tama: “Grüß Gott, Frau Santos!” Nakaekis ang “Frau” sa form, at magalang ang Frau + apelyido. Ang “Herr” ay para sa lalaki. Ang “Frau Maria” ay gumagamit ng Vorname at hindi ito ang karaniwang magalang na pagtawag.'),
           [G2], R('Frau', 'Familienname'), img=FORM()),
    choice(X, 'hoeren', L('Hören Sie. Was ist richtig?', 'Anna Gruber introduces herself. Listen. Which sentence is correct?', 'Nagpapakilala si Anna Gruber. Makinig. Aling pangungusap ang tama?'),
           None, 'Anna ist der Vorname.', ['Gruber ist der Vorname.', 'Anna ist der Familienname.'],
           L('Sie hören: „Ich heiße Anna Gruber.“ Der Vorname kommt zuerst: Anna ist der Vorname, Gruber ist der Familienname.',
             'You hear: “Ich heiße Anna Gruber.” The Vorname comes first: Anna is the Vorname, Gruber is the Familienname.',
             'Naririnig mo: “Ich heiße Anna Gruber.” Una ang Vorname: Anna ang Vorname, Gruber ang Familienname.'),
           [G2], R('Vorname', 'Familienname', 'heißen'), audio='Ich heiße Anna Gruber.'),
    cloze(X, 'grammatikWortschatz', L('Ergänzen Sie den Dialog.', 'Frau Gruber asks Jonas Huber for his name. Complete the dialogue with the words below.', 'Tinanong ni Frau Gruber si Jonas Huber tungkol sa pangalan niya. Kumpletuhin ang dialogo gamit ang mga salita sa ibaba.'),
          'Frau Gruber: Wie {{1}} Sie?\nJonas: Ich {{2}} Jonas Huber.', [['heißen'], ['heiße', 'bin']],
          L('Richtig: „Wie heißen Sie?“ – „Ich heiße …“. Bei „Sie“ endet das Verb auf -en, bei „ich“ auf -e. „heißt“ passt zu er/sie, nicht zu „Sie“ oder „ich“.',
            'Correct: “Wie heißen Sie?” – “Ich heiße …”. With “Sie” the verb ends in -en, with “ich” in -e. “heißt” goes with er/sie, not with “Sie” or “ich”.',
            'Tama: “Wie heißen Sie?” – “Ich heiße …”. Sa “Sie”, nagtatapos sa -en ang verb; sa “ich”, sa -e. Ang “heißt” ay para sa er/sie, hindi sa “Sie” o “ich”.'),
          [G5], R('heißen', 'wie'), bank=['heißen', 'heiße', 'heißt'], hints=['(heißen)', '(heißen)']),
    cloze(X, 'grammatikWortschatz', L('Ergänzen Sie den Dialog.', 'Jonas and Anna greet each other politely. Complete the dialogue with the words below.', 'Magalang na nagbabatian sina Jonas at Anna. Kumpletuhin ang dialogo gamit ang mga salita sa ibaba.'),
          'Jonas: Grüß Gott, {{1}} Gruber!\nAnna: Grüß Gott, {{2}} Huber!', [['Frau'], ['Herr']],
          L('Richtig: Jonas spricht mit Anna, einer Frau: „Frau Gruber“. Anna spricht mit Jonas, einem Mann: „Herr Huber“. Nach „Herr“ und „Frau“ steht der Familienname.',
            'Correct: Jonas speaks to Anna, a woman: “Frau Gruber”. Anna speaks to Jonas, a man: “Herr Huber”. After “Herr” and “Frau” comes the family name.',
            'Tama: Kausap ni Jonas si Anna, isang babae: “Frau Gruber”. Kausap ni Anna si Jonas, isang lalaki: “Herr Huber”. Pagkatapos ng “Herr” at “Frau” ay ang apelyido.'),
          [G2], R('Herr', 'Frau'), bank=['Frau', 'Herr', 'Name']),
    choice(X, 'sprechen', L('Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'You are Maria Santos. Frau Gruber asks you: “Wie heißen Sie?” What do you answer? Choose, then say it aloud.', 'Ikaw si Maria Santos. Tinanong ka ni Frau Gruber: “Wie heißen Sie?” Ano ang sagot mo? Pumili, tapos sabihin nang malakas.'),
           None, 'Ich heiße Maria Santos.', ['Ich heiße Frau Santos.', 'Ich heißen Maria Santos.'],
           L('Richtig: „Ich heiße Maria Santos.“ Bei „ich“ endet das Verb auf -e. „Frau“ sagen nur andere zu Ihnen, über sich selbst sagen Sie Vor- und Familienname. „ich heißen“ ist falsch: -en gehört zu „Sie“ und „wir“.',
             'Correct: “Ich heiße Maria Santos.” With “ich” the verb ends in -e. Only other people say “Frau” to you; about yourself you say first name and family name. “ich heißen” is wrong: -en goes with “Sie” and “wir”.',
             'Tama: “Ich heiße Maria Santos.” Sa “ich”, nagtatapos sa -e ang verb. Ang “Frau” ay sinasabi lang ng ibang tao sa iyo; sa sarili mo, Vorname at Familienname ang sinasabi mo. Mali ang “ich heißen”: ang -en ay para sa “Sie” at “wir”.'),
           [G2, G5], R('ich', 'heißen')),
    short(X, 'schreiben', L('Schreiben Sie die Antwort.', 'You are Jonas Huber. Frau Gruber asks you for your name. Write your answer as a full sentence.', 'Ikaw si Jonas Huber. Tinanong ka ni Frau Gruber tungkol sa pangalan mo. Isulat ang sagot mo bilang buong pangungusap.'),
          'Frau Gruber: „Wie heißen Sie?“ – Sie: „…“', ['Ich heiße Jonas Huber.', 'Ich bin Jonas Huber.'],
          L('Richtig: „Ich heiße Jonas Huber.“ oder „Ich bin Jonas Huber.“ Bei „ich“ endet „heißen“ auf -e: ich heiße. Vorname zuerst, dann der Familienname.',
            'Correct: “Ich heiße Jonas Huber.” or “Ich bin Jonas Huber.” With “ich” the verb “heißen” ends in -e: ich heiße. First name first, then the family name.',
            'Tama: “Ich heiße Jonas Huber.” o “Ich bin Jonas Huber.” Sa “ich”, nagtatapos sa -e ang “heißen”: ich heiße. Una ang Vorname, tapos ang Familienname.'),
          [G2, G5], R('heißen', 'ich')),
], intro=INTRO(
    L('Jonas Huber kommt zu Frau Gruber. Sie fragt: „Wie heißen Sie?“ Er sagt seinen Namen.',
      'Jonas Huber comes to Frau Gruber. She asks: “Wie heißen Sie?” He tells her his name.',
      'Pumunta si Jonas Huber kay Frau Gruber. Nagtanong siya: “Wie heißen Sie?” Sinabi niya ang pangalan niya.'),
    L('sagen, wie Sie heißen – und andere höflich nach dem Namen fragen: „Wie heißen Sie?“',
      'say what your name is – and politely ask other people for theirs: “Wie heißen Sie?”',
      'sabihin ang pangalan mo – at magalang na itanong ang pangalan ng iba: “Wie heißen Sie?”')))

# L03 ------------------------------------------------------------------ du or Sie, origin
lesson(3, L('du oder Sie?', 'du or Sie?', 'du o Sie?'), ['du', 'woher', 'kommen', 'sein (Verb)', 'wer', 'Österreich', 'Philippinen'], [
    RULE('Sie = höflich · du = Freunde, Familie, Kinder', '„Sie“ sagen Sie zu Erwachsenen, die Sie nicht gut kennen: im Büro, im Amt, bei der Ärztin. „du“ sagen Sie zu Freunden, zur Familie und zu Kindern. „Sie“ (höflich) schreibt man immer groß.',
         'You say “Sie” to adults you do not know well: in an office, at an official’s desk, at the doctor’s. You say “du” to friends, family and children. The polite “Sie” is always written with a capital letter.',
         'Ang “Sie” ay sinasabi sa mga matatandang hindi mo lubos na kilala: sa opisina, sa ahensya ng gobyerno, sa doktor. Ang “du” ay sa mga kaibigan, pamilya at bata. Ang magalang na “Sie” ay laging nakasulat nang malaki ang unang titik.',
         ['Wie heißen Sie?', 'Wie heißt du?']),
    RULE('ich komme · du kommst · Sie kommen', 'Das Verb passt zur Person: bei „ich“ endet es auf -e, bei „du“ auf -st, bei „Sie“ auf -en. Darum: „Woher kommst du?“, aber „Woher kommen Sie?“.',
         'The verb matches the person: with “ich” it ends in -e, with “du” in -st, with “Sie” in -en. That is why: “Woher kommst du?”, but “Woher kommen Sie?”.',
         'Ang verb ay ayon sa tao: sa “ich”, nagtatapos sa -e; sa “du”, sa -st; sa “Sie”, sa -en. Kaya: “Woher kommst du?”, pero “Woher kommen Sie?”.',
         ['Ich komme aus Österreich.', 'Woher kommst du?', 'Woher kommen Sie?']),
    PHRASE('Woher kommen Sie? – Ich komme aus Österreich.', 'So fragen Sie nach dem Land und so antworten Sie: „Ich komme aus“ + Land. Lernen Sie den Satz jetzt als Ganzes. Das Wort „aus“ erklärt Kapitel 3.',
           'This is how you ask for the country and how you answer: “Ich komme aus” + country. Learn the sentence as a whole for now. Chapter 3 explains the word “aus”.',
           'Ganito itanong ang bansa at ganito sumagot: “Ich komme aus” + bansa. Isaulo muna ang pangungusap bilang buo. Ipapaliwanag ng Kapitel 3 ang salitang “aus”.'),
    PHRASE('Ich komme aus den Philippinen.', 'Bei den Philippinen heißt es „aus den Philippinen“ (nicht: „aus Philippinen“). Lernen Sie auch diesen Satz als Ganzes, Kapitel 3 erklärt, warum.',
           'For the Philippines you say “aus den Philippinen” (not “aus Philippinen”). Learn this sentence as a whole, too. Chapter 3 explains why.',
           'Para sa Pilipinas, sinasabi ang “aus den Philippinen” (hindi “aus Philippinen”). Isaulo rin ang pangungusap na ito bilang buo. Ipapaliwanag ng Kapitel 3 kung bakit.'),
    RULE('ich bin · du bist · Sie sind', 'Das Verb „sein“ ist besonders. Es endet nicht auf -e, -st, -en, sondern hat eigene Formen. Lernen Sie sie auswendig: ich bin – du bist – Sie sind.',
         'The verb “sein” is special. It does not follow the endings -e, -st, -en, but has its own forms. Learn them by heart: ich bin – du bist – Sie sind.',
         'Espesyal ang verb na “sein”. Hindi nito sinusunod ang mga hulaping -e, -st, -en, kundi may sarili itong anyo. Isaulo: ich bin – du bist – Sie sind.',
         ['Ich bin Maria.', 'Wer sind Sie? – Ich bin Jonas Huber.', 'Du bist Jose.']),
], [
    choice(X, 'lesen', L('Schauen Sie das Bild an.', 'Maria Santos is in the office of Frau Gruber. She does not know her well. Look at picture 1. What does Maria ask?', 'Nasa opisina ni Frau Gruber si Maria Santos. Hindi niya siya lubos na kilala. Tingnan ang larawan 1. Ano ang itatanong ni Maria?'),
           'Bild 1: Was fragt Maria?', 'Wie heißen Sie?', ['Wie heißt du?', 'Wie heiße Sie?'],
           L('Richtig: „Wie heißen Sie?“ Frau Gruber arbeitet im Büro, Maria kennt sie nicht gut: Darum „Sie“, und das Verb endet auf -en. „Wie heißt du?“ ist für Freunde. „Wie heiße Sie?“ hat die falsche Endung (-e gehört zu „ich“).',
             'Correct: “Wie heißen Sie?” Frau Gruber works in the office and Maria does not know her well: so “Sie”, and the verb ends in -en. “Wie heißt du?” is for friends. “Wie heiße Sie?” has the wrong ending (-e goes with “ich”).',
             'Tama: “Wie heißen Sie?” Nagtatrabaho si Frau Gruber sa opisina at hindi siya lubos na kilala ni Maria: kaya “Sie”, at nagtatapos sa -en ang verb. Ang “Wie heißt du?” ay para sa mga kaibigan. Mali ang hulapi ng “Wie heiße Sie?” (ang -e ay para sa “ich”).'),
           [G3], R('Sie', 'wie'), img=DUSIE()),
    choice(X, 'lesen', L('Schauen Sie das Bild an.', 'Look at picture 2. Maria and Jose are friends. Maria wants to know where Jose is from. What does she ask?', 'Tingnan ang larawan 2. Magkaibigan sina Maria at Jose. Gusto ni Maria na malaman kung taga-saan si Jose. Ano ang itatanong niya?'),
           'Bild 2: Was fragt Maria?', 'Woher kommst du?', ['Woher kommen Sie?', 'Woher kommt du?'],
           L('Richtig: „Woher kommst du?“ Maria sagt „Servus“ zu Jose, sie sind Freunde: „du“. Bei „du“ endet das Verb auf -st. „Woher kommen Sie?“ wäre zu höflich. „kommt“ gehört zu er/sie, nicht zu „du“.',
             'Correct: “Woher kommst du?” Maria says “Servus” to Jose, they are friends: “du”. With “du” the verb ends in -st. “Woher kommen Sie?” would be too polite. “kommt” goes with er/sie, not with “du”.',
             'Tama: “Woher kommst du?” Sinasabi ni Maria ang “Servus” kay Jose, magkaibigan sila: “du”. Sa “du”, nagtatapos sa -st ang verb. Masyadong magalang ang “Woher kommen Sie?”. Ang “kommt” ay para sa er/sie, hindi sa “du”.'),
           [G3, G4], R('du', 'woher', 'kommen'), img=DUSIE()),
    choice(X, 'hoeren', L('Hören Sie. Wen fragt Maria?', 'Maria asks a question. Listen: is she asking Frau Gruber from the office or her friend Jose?', 'May itinatanong si Maria. Makinig: si Frau Gruber ba sa opisina ang tinatanong niya o ang kaibigan niyang si Jose?'),
           'Maria fragt …', 'Jose', ['Frau Gruber'],
           L('Sie hören: „Servus! Woher kommst du?“ „Servus“ und „kommst du“ gehören zu Freunden: Maria fragt Jose. Zu Frau Gruber würde sie „Grüß Gott! Woher kommen Sie?“ sagen.',
             'You hear: “Servus! Woher kommst du?” “Servus” and “kommst du” belong to friends: Maria asks Jose. To Frau Gruber she would say “Grüß Gott! Woher kommen Sie?”.',
             'Naririnig mo: “Servus! Woher kommst du?” Ang “Servus” at “kommst du” ay para sa mga kaibigan: si Jose ang tinatanong ni Maria. Kay Frau Gruber, sasabihin niya ang “Grüß Gott! Woher kommen Sie?”.'),
           [G3], R('du', 'servus'), audio='Servus! Woher kommst du?'),
    cloze(X, 'grammatikWortschatz', L('Ergänzen Sie den Dialog.', 'Jose asks Maria where she is from. They are friends. Complete the dialogue with the words below.', 'Tinanong ni Jose si Maria kung taga-saan siya. Magkaibigan sila. Kumpletuhin ang dialogo gamit ang mga salita sa ibaba.'),
          'Jose: Woher {{1}} du?\nMaria: Ich {{2}} aus den Philippinen.', [['kommst'], ['komme']],
          L('Richtig: „Woher kommst du?“ – „Ich komme …“. Bei „du“ endet das Verb auf -st, bei „ich“ auf -e. „kommen“ passt zu „Sie“ und „wir“.',
            'Correct: “Woher kommst du?” – “Ich komme …”. With “du” the verb ends in -st, with “ich” in -e. “kommen” goes with “Sie” and “wir”.',
            'Tama: “Woher kommst du?” – “Ich komme …”. Sa “du”, nagtatapos sa -st ang verb; sa “ich”, sa -e. Ang “kommen” ay para sa “Sie” at “wir”.'),
          [G4, G5], R('kommen', 'woher'), bank=['kommst', 'komme', 'kommen']),
    cloze(X, 'grammatikWortschatz', L('Ergänzen Sie den Dialog.', 'Maria knocks at a door in the office. Frau Gruber asks who is there. Complete the dialogue with the words below.', 'Kumatok si Maria sa pinto ng opisina. Tinanong ni Frau Gruber kung sino iyon. Kumpletuhin ang dialogo gamit ang mga salita sa ibaba.'),
          'Frau Gruber: Wer {{1}} Sie?\nMaria: Ich {{2}} Maria Santos.', [['sind'], ['bin']],
          L('Richtig: „Wer sind Sie?“ – „Ich bin …“. Das Verb „sein“ ist besonders: ich bin, du bist, Sie sind. „bist“ gehört nur zu „du“.',
            'Correct: “Wer sind Sie?” – “Ich bin …”. The verb “sein” is special: ich bin, du bist, Sie sind. “bist” only goes with “du”.',
            'Tama: “Wer sind Sie?” – “Ich bin …”. Espesyal ang verb na “sein”: ich bin, du bist, Sie sind. Ang “bist” ay para lang sa “du”.'),
          [G5], R('sein (Verb)', 'wer'), bank=['sind', 'bin', 'bist']),
    choice(X, 'sprechen', L('Was antworten Sie? Wählen Sie, dann sagen Sie es laut.', 'You are Maria Santos and come from the Philippines. Frau Gruber asks you: “Woher kommen Sie?” What do you answer? Choose, then say it aloud.', 'Ikaw si Maria Santos at taga-Pilipinas ka. Tinanong ka ni Frau Gruber: “Woher kommen Sie?” Ano ang sagot mo? Pumili, tapos sabihin nang malakas.'),
           None, 'Ich komme aus den Philippinen.', ['Ich kommst aus den Philippinen.', 'Ich kommen aus den Philippinen.'],
           L('Richtig: „Ich komme aus den Philippinen.“ Bei „ich“ endet das Verb auf -e. „kommst“ gehört zu „du“, „kommen“ zu „Sie“ und „wir“.',
             'Correct: “Ich komme aus den Philippinen.” With “ich” the verb ends in -e. “kommst” goes with “du”, “kommen” with “Sie” and “wir”.',
             'Tama: “Ich komme aus den Philippinen.” Sa “ich”, nagtatapos sa -e ang verb. Ang “kommst” ay para sa “du”, ang “kommen” sa “Sie” at “wir”.'),
           [G4, G5], R('kommen', 'Philippinen')),
    short(X, 'schreiben', L('Schreiben Sie die Frage.', 'You are Maria. Your friend Jose is new in the course. Write your question to him with the words in the brackets.', 'Ikaw si Maria. Bago sa kurso ang kaibigan mong si Jose. Isulat ang tanong mo sa kanya gamit ang mga salita sa panaklong.'),
          'Maria: „…?“ (woher – kommen – du)', ['Woher kommst du?', 'Woher kommst du, Jose?'],
          L('Richtig: „Woher kommst du?“ Die Frage beginnt mit dem Fragewort „woher“, dann kommt das Verb mit der Endung -st: kommst, dann „du“.',
            'Correct: “Woher kommst du?” The question starts with the question word “woher”, then comes the verb with the ending -st: kommst, then “du”.',
            'Tama: “Woher kommst du?” Nagsisimula ang tanong sa salitang pananong na “woher”, kasunod ang verb na may hulaping -st: kommst, tapos “du”.'),
          [G3, G4], R('woher', 'kommen', 'du')),
], intro=INTRO(
    L('Maria Santos kommt aus den Philippinen. In Wien trifft sie Frau Gruber im Büro und ihren Freund Jose. Sagt sie „du“ oder „Sie“?',
      'Maria Santos is from the Philippines. In Vienna she meets Frau Gruber in the office and her friend Jose. Does she say “du” or “Sie”?',
      'Taga-Pilipinas si Maria Santos. Sa Vienna, nakikilala niya si Frau Gruber sa opisina at ang kaibigan niyang si Jose. “du” ba o “Sie” ang sinasabi niya?'),
    L('höflich mit „Sie“ und unter Freunden mit „du“ fragen – und sagen, woher Sie kommen.',
      'ask questions politely with “Sie” and among friends with “du” – and say where you come from.',
      'magtanong nang magalang gamit ang “Sie” at sa mga kaibigan gamit ang “du” – at sabihin kung taga-saan ka.')))

# L04 ------------------------------------------------------------------ how are you, thanks
lesson(4, L("Wie geht's?", 'How are you?', 'Kumusta?'), ["Wie geht's?", 'danke', 'bitte', 'gut', 'sehr', 'Entschuldigung', 'dir', 'und'], [
    PHRASE("Wie geht's? – Danke, gut. Und dir?", 'So fragen Sie unter Freunden, wie es jemandem geht. Antworten Sie kurz und fragen Sie zurück: „Und dir?“ „dir“ gehört zu „du“. Mit „Sie“ heißt es „Wie geht es Ihnen?“ – das lernen Sie später.',
           'This is how you ask a friend how they are. Answer briefly and ask back: “Und dir?” “dir” goes with “du”. With “Sie” it is “Wie geht es Ihnen?” – you will learn that later.',
           'Ganito itanong sa kaibigan kung kumusta siya. Sumagot nang maikli at magtanong pabalik: “Und dir?” Ang “dir” ay para sa “du”. Sa “Sie”, “Wie geht es Ihnen?” ang sinasabi – matututuhan mo iyon mamaya.'),
    RULE('sehr gut – „sehr“ steht vor „gut“', '„sehr“ macht ein Wort stärker und steht davor: gut → sehr gut. Man sagt nicht „gut sehr“.',
         '“sehr” makes a word stronger and comes before it: gut → sehr gut. You do not say “gut sehr”.',
         'Pinalalakas ng “sehr” ang salita at nasa unahan nito: gut → sehr gut. Hindi sinasabi ang “gut sehr”.',
         ['Sehr gut, danke!', 'Danke, sehr gut. Und dir?']),
    RULE('Danke! – Bitte!', 'Für etwas sagen Sie „Danke“. Die Antwort ist „Bitte“, auch „Bitte sehr“ oder „Bitte schön“. „Bitte“ heißt außerdem „please“: So bitten Sie höflich um etwas.',
         'For something you receive you say “Danke”. The answer is “Bitte”, also “Bitte sehr” or “Bitte schön”. “Bitte” also means “please”: that is how you ask politely for something.',
         'Para sa isang bagay na natanggap mo, sinasabi ang “Danke”. Ang sagot ay “Bitte”, o “Bitte sehr” o “Bitte schön”. Ang “Bitte” ay nangangahulugan ding “pakiusap”: ganito ka humihingi nang magalang.',
         ['Danke! – Bitte!', 'Danke sehr! – Bitte sehr!']),
    PHRASE('Entschuldigung!', 'Das sagen Sie bei einem kleinen Fehler, zum Beispiel wenn Sie jemanden anstoßen. Sie sagen es auch, wenn Sie jemanden etwas fragen wollen: „Entschuldigung, Frau Gruber!“',
           'You say this after a small mistake, for example when you bump into someone. You also say it when you want to ask someone something: “Entschuldigung, Frau Gruber!”',
           'Sinasabi ito pagkatapos ng maliit na pagkakamali, halimbawa kapag nabangga mo ang isang tao. Sinasabi rin ito kapag may gusto kang itanong: “Entschuldigung, Frau Gruber!”'),
], [
    choice(X, 'lesen', L('Schauen Sie das Bild an.', 'Look at picture 1. Herr Huber bumps into Frau Gruber by mistake. What does he say?', 'Tingnan ang larawan 1. Nabangga ni Herr Huber si Frau Gruber nang hindi sinasadya. Ano ang sinasabi niya?'),
           'Bild 1: Was sagt Herr Huber?', 'Entschuldigung!', ['Danke!', 'Bitte!'],
           L('Richtig: „Entschuldigung!“ Herr Huber macht einen kleinen Fehler: Er stößt gegen Frau Gruber. „Danke“ sagt man für etwas, das man bekommt. „Bitte“ ist die Antwort auf „Danke“.',
             'Correct: “Entschuldigung!” Herr Huber makes a small mistake: he bumps into Frau Gruber. You say “Danke” for something you receive. “Bitte” is the answer to “Danke”.',
             'Tama: “Entschuldigung!” Nagkamali nang kaunti si Herr Huber: nabangga niya si Frau Gruber. Ang “Danke” ay para sa isang bagay na natanggap mo. Ang “Bitte” ay sagot sa “Danke”.'),
           [G6], R('Entschuldigung'), img=SITUATION()),
    choice(X, 'lesen', L('Schauen Sie das Bild an.', 'Look at picture 2. Jonas brings Frau Santos her coffee. What does Frau Santos say?', 'Tingnan ang larawan 2. Dinadalhan ni Jonas si Frau Santos ng kape niya. Ano ang sinasabi ni Frau Santos?'),
           'Bild 2: Was sagt Frau Santos?', 'Danke!', ['Bitte!', 'Entschuldigung!'],
           L('Richtig: „Danke!“ Frau Santos bekommt etwas und bedankt sich. „Bitte“ sagt danach Jonas: Es ist die Antwort auf „Danke“. „Entschuldigung“ ist hier nicht nötig, es ist kein Fehler passiert.',
             'Correct: “Danke!” Frau Santos receives something and says thank you. After that Jonas says “Bitte”: it is the answer to “Danke”. “Entschuldigung” is not needed here, nothing went wrong.',
             'Tama: “Danke!” May natanggap si Frau Santos at nagpapasalamat siya. Pagkatapos, sinasabi ni Jonas ang “Bitte”: ito ang sagot sa “Danke”. Hindi kailangan ang “Entschuldigung” dito, walang pagkakamaling nangyari.'),
           [G6], R('danke', 'bitte'), img=SITUATION()),
    choice(X, 'hoeren', L('Hören Sie. Wie geht es Maria?', 'Jonas asks Maria how she is. Listen: how is Maria?', 'Tinanong ni Jonas si Maria kung kumusta siya. Makinig: kumusta si Maria?'),
           'Wie geht es Maria?', 'Sehr gut.', ['Gut.'],
           L('Sie hören: „Wie geht’s, Maria? – Sehr gut, danke! Und dir?“ Maria sagt „sehr gut“, das ist mehr als „gut“. Danach fragt sie zurück: „Und dir?“',
             'You hear: “Wie geht’s, Maria? – Sehr gut, danke! Und dir?” Maria says “sehr gut”, which is more than “gut”. Then she asks back: “Und dir?”',
             'Naririnig mo: “Wie geht’s, Maria? – Sehr gut, danke! Und dir?” Sinabi ni Maria ang “sehr gut”, na mas mataas kaysa sa “gut”. Pagkatapos, nagtatanong siya pabalik: “Und dir?”'),
           [G6], R("Wie geht's?", 'sehr', 'gut'), audio="Wie geht's, Maria? – Sehr gut, danke! Und dir?"),
    choice(X, 'grammatikWortschatz', L('Was antwortet Maria? Wählen Sie die richtige Antwort.', 'Maria holds the door open for Herr Huber. He says: “Danke!” What does Maria answer?', 'Hinawakan ni Maria ang pinto para kay Herr Huber. Sinabi niya: “Danke!” Ano ang sagot ni Maria?'),
           'Herr Huber: „Danke!“', 'Bitte!', ['Entschuldigung!', 'Hallo!'],
           L('Richtig: Auf „Danke“ antwortet man „Bitte“. „Entschuldigung“ sagt man bei einem Fehler. „Hallo“ ist ein Gruß und keine Antwort auf „Danke“.',
             'Correct: the answer to “Danke” is “Bitte”. You say “Entschuldigung” after a mistake. “Hallo” is a greeting and not an answer to “Danke”.',
             'Tama: ang sagot sa “Danke” ay “Bitte”. Ang “Entschuldigung” ay sinasabi pagkatapos ng pagkakamali. Ang “Hallo” ay pagbati at hindi sagot sa “Danke”.'),
           [G6], R('danke', 'bitte')),
    cloze(X, 'grammatikWortschatz', L('Ergänzen Sie den Dialog.', 'Jonas meets his friend Maria in front of the office. Complete the dialogue with the words below.', 'Nakasalubong ni Jonas ang kaibigan niyang si Maria sa harap ng opisina. Kumpletuhin ang dialogo gamit ang mga salita sa ibaba.'),
          "Jonas: Wie geht's {{1}}?\nMaria: {{2}}, sehr gut!", [['dir'], ['Danke']],
          L('Richtig: „Wie geht’s dir?“ – „Danke, sehr gut!“ „dir“ gehört zu „du“: „Wie geht’s du?“ ist falsch. Auf die Frage antwortet man mit „Danke“. „Bitte“ ist die Antwort auf „Danke“.',
            'Correct: “Wie geht’s dir?” – “Danke, sehr gut!” “dir” goes with “du”: “Wie geht’s du?” is wrong. You answer the question with “Danke”. “Bitte” is the answer to “Danke”.',
            'Tama: “Wie geht’s dir?” – “Danke, sehr gut!” Ang “dir” ay para sa “du”: mali ang “Wie geht’s du?”. Sa tanong, sumasagot ng “Danke”. Ang “Bitte” ay sagot sa “Danke”.'),
          [G6], R('dir', 'danke'), bank=['dir', 'Danke', 'du', 'Bitte']),
    choice(X, 'sprechen', L('Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'Your friend Jose asks you: “Wie geht’s?” You are doing very well. What do you say? Choose, then say it aloud.', 'Tinanong ka ng kaibigan mong si Jose: “Wie geht’s?” Napakabuti ng lagay mo. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'),
           None, 'Sehr gut, danke! Und dir?', ['Gut sehr, danke! Und dir?', 'Sehr gut, bitte! Und dir?'],
           L('Richtig: „Sehr gut, danke! Und dir?“ „sehr“ steht vor „gut“. Auf die Frage antwortet man mit „danke“, nicht mit „bitte“. Dann fragt man zurück: „Und dir?“',
             'Correct: “Sehr gut, danke! Und dir?” “sehr” comes before “gut”. You answer the question with “danke”, not with “bitte”. Then you ask back: “Und dir?”',
             'Tama: “Sehr gut, danke! Und dir?” Nasa unahan ng “gut” ang “sehr”. Sa tanong, sumasagot ng “danke”, hindi ng “bitte”. Pagkatapos, nagtatanong pabalik: “Und dir?”'),
           [G6], R('sehr', 'gut', 'und')),
    short(X, 'schreiben', L('Schreiben Sie, was Sie antworten.', 'You help Jonas. He thanks you. Write your answer.', 'Tinulungan mo si Jonas. Nagpapasalamat siya sa iyo. Isulat ang sagot mo.'),
          'Jonas: „Danke!“ – Sie: „…“', ['Bitte!', 'Bitte sehr!', 'Bitte schön!'],
          L('Richtig: „Bitte!“ – auch „Bitte sehr!“ oder „Bitte schön!“ sind möglich. Auf „Danke“ antwortet man mit „Bitte“. „Bitte“ schreibt man am Anfang groß.',
            'Correct: “Bitte!” – “Bitte sehr!” or “Bitte schön!” are also possible. The answer to “Danke” is “Bitte”. “Bitte” is written with a capital letter at the beginning.',
            'Tama: “Bitte!” – puwede rin ang “Bitte sehr!” o “Bitte schön!”. Ang sagot sa “Danke” ay “Bitte”. Nakasulat nang malaki ang unang titik ng “Bitte” sa simula.'),
          [G6], R('bitte', 'danke')),
], intro=INTRO(
    L("Jonas Huber trifft Maria Santos vor dem Büro. Sie kennen sich schon. Jonas fragt: „Wie geht's?“",
      'Jonas Huber meets Maria Santos in front of the office. They already know each other. Jonas asks: “Wie geht’s?”',
      'Nakasalubong ni Jonas Huber si Maria Santos sa harap ng opisina. Magkakilala na sila. Nagtanong si Jonas: “Wie geht’s?”'),
    L('fragen, wie es jemandem geht, kurz antworten – und „Danke“, „Bitte“ und „Entschuldigung“ richtig sagen.',
      'ask how someone is, answer briefly – and say “Danke”, “Bitte” and “Entschuldigung” correctly.',
      'magtanong kung kumusta ang isang tao, sumagot nang maikli – at sabihin nang tama ang “Danke”, “Bitte” at “Entschuldigung”.')))

# L05 ------------------------------------------------------------------ er, sie, es
lesson(5, L('Wer ist das? – er und sie', 'Who is that? – he and she', 'Sino iyan? – siya (lalaki/babae)'), ['er', 'sie', 'es'], [
    PHRASE('Wer ist das? – Das ist Herr Huber.', 'So fragen Sie nach einer anderen Person und so stellen Sie sie vor. „wer“ fragt immer nach Personen.',
           'This is how you ask about another person and how you introduce them. “wer” always asks about people.',
           'Ganito itanong ang tungkol sa ibang tao at ganito siya ipakilala. Ang “wer” ay laging para sa mga tao.'),
    RULE('er = ein Mann · sie = eine Frau', 'Sie müssen den Namen nicht wiederholen: Für einen Mann sagen Sie „er“, für eine Frau „sie“.',
         'You do not have to repeat the name: for a man you say “er”, for a woman “sie”.',
         'Hindi mo na kailangang ulitin ang pangalan: para sa lalaki, “er”; para sa babae, “sie”.',
         ['Das ist Herr Huber. Er heißt Jonas.', 'Das ist Frau Gruber. Sie heißt Anna.']),
    RULE('sie (eine Frau) ≠ Sie (höflich)', 'Klein „sie“ meint eine Frau (über die Sie sprechen). Groß „Sie“ ist die höfliche Anrede für das Gegenüber. Am Satzanfang sieht man die Größe nicht, aber das Verb hilft: „Sie heißt“ (eine Frau) – „Sie heißen“ (zu Ihnen).',
         'A small “sie” means a woman (someone you talk about). A capital “Sie” is the polite form for the person you talk to. At the start of a sentence you cannot see the capital letter, but the verb helps: “Sie heißt” (a woman) – “Sie heißen” (you, polite).',
         'Ang maliit na “sie” ay babae (pinag-uusapan mo). Ang malaking “Sie” ay magalang na pagtawag sa kausap. Sa simula ng pangungusap, hindi makikita ang laki ng titik, pero tumutulong ang verb: “Sie heißt” (babae) – “Sie heißen” (ikaw, magalang).',
         ['Sie heißt Anna Gruber.', 'Wie heißen Sie?']),
    RULE('er heißt · sie kommt · er ist', 'Bei „er“ und „sie“ endet das Verb auf -t: er heißt, sie kommt. Besonders ist „sein“: er ist, sie ist.',
         'With “er” and “sie” the verb ends in -t: er heißt, sie kommt. “sein” is special: er ist, sie ist.',
         'Sa “er” at “sie”, nagtatapos sa -t ang verb: er heißt, sie kommt. Espesyal ang “sein”: er ist, sie ist.',
         ['Er heißt Jonas. Er kommt aus Österreich.', 'Sie ist Frau Gruber.']),
    PHRASE('Wie geht es? – Es geht.', 'Auf die Frage „Wie geht es?“ antworten Sie manchmal „Es geht.“ Das heißt: nicht sehr gut, aber auch nicht schlecht. „es“ meint hier keine Person, es steht nur im Satz.',
           'You sometimes answer the question “Wie geht es?” with “Es geht.” It means: so-so, not very good, but not bad either. “es” does not mean a person here, it just stands in the sentence.',
           'Minsan, ang sagot sa tanong na “Wie geht es?” ay “Es geht.” Ibig sabihin: so-so, hindi masyadong mabuti pero hindi rin masama. Hindi tao ang tinutukoy ng “es” dito, nasa pangungusap lang ito.'),
], [
    choice(X, 'lesen', L('Schauen Sie das Bild an.', 'Maria, Jonas and Anna sit in the course in Vienna. Look at the name signs and flags. Which sentence is correct?', 'Nakaupo sina Maria, Jonas at Anna sa kurso sa Vienna. Tingnan ang mga name sign at bandila. Aling pangungusap ang tama?'),
           'Das ist Jonas Huber.', 'Er kommt aus Österreich.', ['Sie kommt aus Österreich.', 'Er kommt aus den Philippinen.'],
           L('Richtig: „Er kommt aus Österreich.“ Jonas ist ein Mann: „er“. Unter seinem Namensschild ist die österreichische Flagge. „Sie kommt …“ wäre für eine Frau, und die Flagge der Philippinen gehört zu Maria.',
             'Correct: “Er kommt aus Österreich.” Jonas is a man: “er”. Under his name sign is the Austrian flag. “Sie kommt …” would be for a woman, and the flag of the Philippines belongs to Maria.',
             'Tama: “Er kommt aus Österreich.” Lalaki si Jonas: “er”. Sa ilalim ng name sign niya ay ang bandila ng Austria. Ang “Sie kommt …” ay para sa babae, at ang bandila ng Pilipinas ay kay Maria.'),
           [G7, G4], R('er', 'Österreich'), img=KURS()),
    cloze(X, 'grammatikWortschatz', L('Schauen Sie das Bild an. Ergänzen Sie den Satz.', 'Look at the picture again. Complete the sentences about Anna Gruber with the words below.', 'Tingnan muli ang larawan. Kumpletuhin ang mga pangungusap tungkol kay Anna Gruber gamit ang mga salita sa ibaba.'),
          'Das ist Anna Gruber. {{1}} kommt aus {{2}}.', [['Sie'], ['Österreich']],
          L('Richtig: „Sie kommt aus Österreich.“ Anna ist eine Frau: „sie“, und das Verb endet auf -t. Unter ihrem Namen ist die österreichische Flagge. „Er“ ist für einen Mann; „Philippinen“ gehört zu Maria.',
            'Correct: “Sie kommt aus Österreich.” Anna is a woman: “sie”, and the verb ends in -t. Under her name is the Austrian flag. “Er” is for a man; “Philippinen” belongs to Maria.',
            'Tama: “Sie kommt aus Österreich.” Babae si Anna: “sie”, at nagtatapos sa -t ang verb. Sa ilalim ng pangalan niya ay ang bandila ng Austria. Ang “Er” ay para sa lalaki; ang “Philippinen” ay kay Maria.'),
          [G7, G4], R('sie', 'kommen'), img=KURS(), bank=['Sie', 'Er', 'Österreich', 'Philippinen']),
    choice(X, 'hoeren', L('Hören Sie. Wer ist das?', 'Maria talks about one person in the picture. Listen: who is it?', 'May pinag-uusapang tao si Maria sa larawan. Makinig: sino iyon?'),
           'Wer ist das?', 'Anna Gruber', ['Jonas Huber', 'Maria Santos'],
           L('Sie hören: „Sie kommt aus Österreich.“ „sie“ = eine Frau, und sie kommt aus Österreich: Das ist Anna Gruber. Jonas Huber ist ein Mann („er“). Maria Santos ist eine Frau, kommt aber aus den Philippinen.',
             'You hear: “Sie kommt aus Österreich.” “sie” = a woman, and she comes from Austria: that is Anna Gruber. Jonas Huber is a man (“er”). Maria Santos is a woman, but she comes from the Philippines.',
             'Naririnig mo: “Sie kommt aus Österreich.” “sie” = babae, at taga-Austria siya: si Anna Gruber iyon. Lalaki si Jonas Huber (“er”). Babae si Maria Santos, pero taga-Pilipinas siya.'),
           [G7], R('sie', 'wer'), audio='Sie kommt aus Österreich.', img=KURS()),
    cloze(X, 'grammatikWortschatz', L('Ergänzen Sie den Dialog.', 'Jose points at Frau Gruber and asks Maria. Complete the dialogue with the words below.', 'Itinuro ni Jose si Frau Gruber at nagtanong kay Maria. Kumpletuhin ang dialogo gamit ang mga salita sa ibaba.'),
          'Jose: Wer {{1}} das?\nMaria: Das {{2}} Frau Gruber.', [['ist'], ['ist']],
          L('Richtig: „Wer ist das? – Das ist Frau Gruber.“ Bei „das“ steht „ist“. „sind“ gehört zu „Sie“ und „wir“, „bin“ nur zu „ich“.',
            'Correct: “Wer ist das? – Das ist Frau Gruber.” With “das” you use “ist”. “sind” goes with “Sie” and “wir”, “bin” only with “ich”.',
            'Tama: “Wer ist das? – Das ist Frau Gruber.” Sa “das”, ang gamit ay “ist”. Ang “sind” ay para sa “Sie” at “wir”, ang “bin” ay para lang sa “ich”.'),
          [G5], R('sein (Verb)', 'wer'), bank=['ist', 'ist', 'sind', 'bin']),
    choice(X, 'grammatikWortschatz', L('Was passt? Wählen Sie die richtige Form.', 'Maria talks about Jonas. Which verb form fits?', 'Pinag-uusapan ni Maria si Jonas. Aling anyo ng verb ang tama?'),
           'Er … Jonas.', 'heißt', ['heiße', 'heißen'],
           L('Richtig: „Er heißt Jonas.“ Bei „er“ und „sie“ endet das Verb auf -t. „heiße“ gehört zu „ich“, „heißen“ zu „Sie“ und „wir“.',
             'Correct: “Er heißt Jonas.” With “er” and “sie” the verb ends in -t. “heiße” goes with “ich”, “heißen” with “Sie” and “wir”.',
             'Tama: “Er heißt Jonas.” Sa “er” at “sie”, nagtatapos sa -t ang verb. Ang “heiße” ay para sa “ich”, ang “heißen” sa “Sie” at “wir”.'),
           [G5, G7], R('er', 'heißen')),
    choice(X, 'grammatikWortschatz', L('Was antwortet Maria?', 'Jonas asks Maria: “Wie geht’s?” Maria is neither happy nor sad, it is just so-so. What does she answer?', 'Tinanong ni Jonas si Maria: “Wie geht’s?” Hindi masaya at hindi rin malungkot si Maria, so-so lang. Ano ang sagot niya?'),
           'Jonas: „Wie geht’s?“', 'Es geht.', ['Sehr gut!', 'Danke, gut.'],
           L('Richtig: „Es geht.“ Das heißt: nicht sehr gut, aber auch nicht schlecht. „Sehr gut“ und „Danke, gut“ sind klar positiv. „es“ meint hier keine Person, es steht nur im Satz.',
             'Correct: “Es geht.” It means: so-so, not very good, but not bad either. “Sehr gut” and “Danke, gut” are clearly positive. “es” does not mean a person here, it just stands in the sentence.',
             'Tama: “Es geht.” Ibig sabihin: so-so, hindi masyadong mabuti pero hindi rin masama. Malinaw na positibo ang “Sehr gut” at “Danke, gut”. Hindi tao ang tinutukoy ng “es” dito, nasa pangungusap lang ito.'),
           [G6], R('es', "Wie geht's?")),
    choice(X, 'sprechen', L('Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'Jose asks you: “Wer ist das?” You point at Frau Gruber. What do you say? Choose, then say it aloud.', 'Tinanong ka ni Jose: “Wer ist das?” Itinuro mo si Frau Gruber. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'),
           None, 'Das ist Frau Gruber. Sie heißt Anna.', ['Das ist Frau Gruber. Er heißt Anna.', 'Das ist Frau Gruber. Sie heißen Anna.'],
           L('Richtig: „Das ist Frau Gruber. Sie heißt Anna.“ Frau Gruber ist eine Frau: „sie“, Verb auf -t. „Er“ ist für einen Mann. „Sie heißen“ ist die höfliche Anrede für das Gegenüber, nicht für Frau Gruber.',
             'Correct: “Das ist Frau Gruber. Sie heißt Anna.” Frau Gruber is a woman: “sie”, verb ending in -t. “Er” is for a man. “Sie heißen” is the polite form for the person you talk to, not for Frau Gruber.',
             'Tama: “Das ist Frau Gruber. Sie heißt Anna.” Babae si Frau Gruber: “sie”, verb na nagtatapos sa -t. Ang “Er” ay para sa lalaki. Ang “Sie heißen” ay magalang na pagtawag sa kausap, hindi kay Frau Gruber.'),
           [G7, G5], R('sie', 'heißen')),
    short(X, 'schreiben', L('Schreiben Sie die Antwort.', 'Look at the picture. Maria points at the man and asks: “Wer ist das?” Write your answer.', 'Tingnan ang larawan. Itinuro ni Maria ang lalaki at nagtanong: “Wer ist das?” Isulat ang sagot mo.'),
          'Maria: „Wer ist das?“ – Sie: „…“', ['Das ist Jonas Huber.', 'Das ist Herr Huber.', 'Das ist Jonas.', 'Er heißt Jonas Huber.', 'Er heißt Jonas.', 'Er ist Jonas Huber.', 'Er ist Herr Huber.'],
          L('Richtig: z. B. „Das ist Jonas Huber.“ oder „Er heißt Jonas.“ Es ist ein Mann, darum „er“. Auf dem Namensschild steht „Jonas Huber“, höflich sagt man „Herr Huber“.',
            'Correct: for example “Das ist Jonas Huber.” or “Er heißt Jonas.” It is a man, so “er”. The name sign says “Jonas Huber”, and the polite form is “Herr Huber”.',
            'Tama: halimbawa “Das ist Jonas Huber.” o “Er heißt Jonas.” Lalaki siya, kaya “er”. Nakasulat sa name sign ang “Jonas Huber”, at ang magalang na anyo ay “Herr Huber”.'),
          [G7, G2], R('wer', 'er'), img=KURS()),
], intro=INTRO(
    L('Im Deutschkurs in Wien sitzen drei Personen. Maria fragt: „Wer ist das?“ Wie heißen sie? Woher kommen sie?',
      'Three people sit in the German course in Vienna. Maria asks: “Wer ist das?” What are their names? Where do they come from?',
      'Tatlong tao ang nakaupo sa kursong German sa Vienna. Nagtanong si Maria: “Wer ist das?” Ano ang pangalan nila? Taga-saan sila?'),
    L('über andere Personen sprechen: „Wer ist das?“ – „Das ist Herr Huber. Er heißt Jonas. Er kommt aus Österreich.“',
      'talk about other people: “Wer ist das?” – “Das ist Herr Huber. Er heißt Jonas. Er kommt aus Österreich.”',
      'pag-usapan ang ibang tao: “Wer ist das?” – “Das ist Herr Huber. Er heißt Jonas. Er kommt aus Österreich.”')))

# L06 ------------------------------------------------------------------ ja, nein, auch, was
lesson(6, L('Ja, nein, ich auch', 'Yes, no, me too', 'Oo, hindi, ako rin'), ['ja', 'nein', 'auch', 'was'], [
    RULE('Frage ohne Fragewort: Verb zuerst → ja oder nein', 'Bei „wer“, „wie“ und „woher“ steht das Fragewort vorne. Ohne Fragewort steht das Verb vorne, und Sie antworten mit „ja“ oder „nein“.',
         'With “wer”, “wie” and “woher” the question word comes first. Without a question word the verb comes first, and you answer with “ja” or “nein”.',
         'Sa “wer”, “wie” at “woher”, nasa unahan ang salitang pananong. Kung walang salitang pananong, nasa unahan ang verb, at sumasagot ka ng “ja” o “nein”.',
         ['Heißen Sie Huber? – Ja, ich heiße Huber.', 'Kommst du aus Österreich? – Ja, ich komme aus Österreich.']),
    PHRASE('Kommen Sie aus Österreich? – Nein, ich komme aus den Philippinen.', 'Nach „nein“ sagen Sie kurz, was richtig ist. So hilft Ihre Antwort mehr als nur „nein“.',
           'After “nein” you briefly say what is correct. That way your answer helps more than just “nein”.',
           'Pagkatapos ng “nein”, sabihin nang maikli kung ano ang tama. Mas nakakatulong ang sagot mo kaysa sa “nein” lang.'),
    RULE('auch – bei mir ist es gleich', '„auch“ heißt: Bei mir ist es genauso. „Ich auch!“ ist eine kurze Antwort, wenn jemand etwas sagt und es bei Ihnen gleich ist.',
         '“auch” means: it is the same for me. “Ich auch!” is a short answer when someone says something and it is the same for you.',
         'Ang “auch” ay nangangahulugang: pareho rin sa akin. Ang “Ich auch!” ay maikling sagot kapag may sinabi ang isang tao at pareho rin ito sa iyo.',
         ['Ich heiße Maria. – Ich auch!', 'Anna kommt aus Österreich. Jonas kommt auch aus Österreich.']),
    RULE('wer = Person · was = Ding', '„wer“ fragt nach Personen, „was“ fragt nach Dingen: Wer ist das? – Das ist Frau Gruber. Was ist das? – Das ist der Familienname.',
         '“wer” asks about people, “was” asks about things: Wer ist das? – Das ist Frau Gruber. Was ist das? – Das ist der Familienname.',
         'Ang “wer” ay para sa mga tao, ang “was” ay para sa mga bagay: Wer ist das? – Das ist Frau Gruber. Was ist das? – Das ist der Familienname.',
         ['Wer ist das? – Das ist Frau Gruber.', 'Was ist das? – Das ist der Familienname.']),
], [
    choice(X, 'lesen', L('Schauen Sie das Bild an. Was antwortet Anna?', 'Anna and Jonas talk about Maria. Jonas asks: “Kommt Maria aus Österreich?” Look at the picture. What does Anna answer?', 'Pinag-uusapan nina Anna at Jonas si Maria. Nagtanong si Jonas: “Kommt Maria aus Österreich?” Tingnan ang larawan. Ano ang sagot ni Anna?'),
           'Jonas: „Kommt Maria aus Österreich?“', 'Nein, sie kommt aus den Philippinen.', ['Ja, sie kommt aus Österreich.', 'Nein, sie kommt aus Österreich.'],
           L('Richtig: Maria hat die Flagge der Philippinen. Darum „Nein“ – und danach das richtige Land. „Ja, sie kommt aus Österreich“ stimmt nicht mit dem Bild überein. „Nein, sie kommt aus Österreich“ widerspricht sich: Nach „nein“ muss etwas anderes kommen.',
             'Correct: Maria has the flag of the Philippines. So “Nein” – and then the right country. “Ja, sie kommt aus Österreich” does not match the picture. “Nein, sie kommt aus Österreich” contradicts itself: after “nein” something different has to follow.',
             'Tama: Ang bandila ni Maria ay ang bandila ng Pilipinas. Kaya “Nein” – at pagkatapos ang tamang bansa. Hindi tugma sa larawan ang “Ja, sie kommt aus Österreich”. Salungat sa sarili ang “Nein, sie kommt aus Österreich”: pagkatapos ng “nein”, dapat iba ang sunod.'),
           [G6, G4], R('nein', 'ja'), img=KURS()),
    choice(X, 'lesen', L('Schauen Sie das Bild an. Wählen Sie die richtige Antwort.', 'Look at the picture of the bedroom. Someone asks: “Ist es Nacht?” What is the right answer?', 'Tingnan ang larawan ng kuwarto. May nagtanong: “Ist es Nacht?” Ano ang tamang sagot?'),
           'Ist es Nacht?', 'Ja, es ist Nacht.', ['Nein, es ist Morgen.', 'Ja, es ist Morgen.'],
           L('Richtig: „Ja, es ist Nacht.“ Das Bild zeigt Mond und Sterne, die Uhr zeigt 21:00. Die Frage hat kein Fragewort, die Antwort beginnt mit „ja“. „Nein, es ist Morgen“ stimmt nicht mit dem Bild überein. „Ja, es ist Morgen“ widerspricht sich.',
             'Correct: “Ja, es ist Nacht.” The picture shows the moon and stars, and the clock shows 21:00. The question has no question word, so the answer begins with “ja”. “Nein, es ist Morgen” does not match the picture. “Ja, es ist Morgen” contradicts itself.',
             'Tama: “Ja, es ist Nacht.” Ipinapakita ng larawan ang buwan at mga bituin, at 21:00 ang orasan. Walang salitang pananong ang tanong, kaya “ja” ang simula ng sagot. Hindi tugma sa larawan ang “Nein, es ist Morgen”. Salungat sa sarili ang “Ja, es ist Morgen”.'),
           [G6], R('ja', 'nein', 'es'), img=NACHT()),
    choice(X, 'hoeren', L('Hören Sie. Was antworten Sie?', 'Frau Gruber asks you a question. You are Maria Santos. Listen. What do you answer?', 'May tanong si Frau Gruber sa iyo. Ikaw si Maria Santos. Makinig. Ano ang sagot mo?'),
           None, 'Nein, ich heiße Santos.', ['Ja, ich heiße Huber.', 'Ich auch.'],
           L('Sie hören: „Heißen Sie Huber?“ Sie heißen Santos, darum „Nein“ – und dann der richtige Name. „Ja, ich heiße Huber“ stimmt nicht. „Ich auch“ passt nur, wenn bei Ihnen etwas gleich ist wie bei der anderen Person.',
             'You hear: “Heißen Sie Huber?” Your name is Santos, so “Nein” – and then the right name. “Ja, ich heiße Huber” is not true. “Ich auch” only fits when something is the same for you as for the other person.',
             'Naririnig mo: “Heißen Sie Huber?” Santos ang pangalan mo, kaya “Nein” – at pagkatapos ang tamang pangalan. Hindi totoo ang “Ja, ich heiße Huber”. Ang “Ich auch” ay bagay lang kapag pareho kayo ng ibang tao.'),
           [G6, G2], R('nein', 'heißen'), audio='Heißen Sie Huber?'),
    cloze(X, 'grammatikWortschatz', L('Ergänzen Sie den Dialog.', 'Jonas asks Anna a question. Anna comes from Austria. Complete the dialogue with the words below.', 'May itinanong si Jonas kay Anna. Taga-Austria si Anna. Kumpletuhin ang dialogo gamit ang mga salita sa ibaba.'),
          'Jonas: Kommst du aus Österreich?\nAnna: {{1}}, ich komme aus Österreich.', [['Ja']],
          L('Richtig: „Ja“. Anna kommt aus Österreich, also stimmt die Frage. „Nein, ich komme aus Österreich“ widerspricht sich. „Auch“ ist keine Antwort auf eine Frage mit „ja“ oder „nein“.',
            'Correct: “Ja”. Anna comes from Austria, so the question is right. “Nein, ich komme aus Österreich” contradicts itself. “Auch” is not an answer to a yes-or-no question.',
            'Tama: “Ja”. Taga-Austria si Anna, kaya totoo ang tanong. Salungat sa sarili ang “Nein, ich komme aus Österreich”. Ang “Auch” ay hindi sagot sa tanong na “ja” o “nein” ang sagot.'),
          [G6], R('ja'), bank=['Ja', 'Nein', 'Auch']),
    cloze(X, 'grammatikWortschatz', L('Ergänzen Sie den Dialog.', 'Jose and Maria both come from the Philippines. Complete the dialogue with the words below.', 'Parehong taga-Pilipinas sina Jose at Maria. Kumpletuhin ang dialogo gamit ang mga salita sa ibaba.'),
          'Jose: Ich komme aus den Philippinen.\nMaria: Ich {{1}}!', [['auch']],
          L('Richtig: „Ich auch!“ Maria kommt auch aus den Philippinen: Bei ihr ist es gleich. „Ich ja“ und „Ich nein“ gibt es nicht: „ja“ und „nein“ beantworten Fragen.',
            'Correct: “Ich auch!” Maria also comes from the Philippines: it is the same for her. “Ich ja” and “Ich nein” do not exist: “ja” and “nein” answer questions.',
            'Tama: “Ich auch!” Taga-Pilipinas din si Maria: pareho sa kanya. Walang “Ich ja” at “Ich nein”: ang “ja” at “nein” ay sagot sa mga tanong.'),
          [G6], R('auch'), bank=['auch', 'ja', 'nein']),
    cloze(X, 'grammatikWortschatz', L('Ergänzen Sie die Fragen.', 'Jose points first at Frau Gruber, then at a word on the form. Complete his two questions with the words below.', 'Una, itinuro ni Jose si Frau Gruber, tapos ang isang salita sa form. Kumpletuhin ang dalawa niyang tanong gamit ang mga salita sa ibaba.'),
          '„{{1}} ist das?“ – „Das ist Frau Gruber.“\n„{{2}} ist das?“ – „Das ist der Familienname.“', [['Wer'], ['Was']],
          L('Richtig: Frau Gruber ist eine Person: „Wer ist das?“ Der Familienname ist ein Ding: „Was ist das?“ „Wie“ passt hier nicht: Es fragt nach der Art, nicht nach Person oder Ding.',
            'Correct: Frau Gruber is a person: “Wer ist das?” The family name is a thing: “Was ist das?” “Wie” does not fit here: it asks how something is, not about a person or a thing.',
            'Tama: Tao si Frau Gruber: “Wer ist das?” Bagay ang Familienname: “Was ist das?” Hindi bagay dito ang “Wie”: nagtatanong ito kung paano, hindi tungkol sa tao o bagay.'),
          [G4], R('wer', 'was'), bank=['Wer', 'Was', 'Wie']),
    choice(X, 'sprechen', L('Was antworten Sie? Wählen Sie, dann sagen Sie es laut.', 'You are Maria Santos from the Philippines. Jonas asks you a question. What do you answer? Choose, then say it aloud.', 'Ikaw si Maria Santos mula sa Pilipinas. May tanong si Jonas sa iyo. Ano ang sagot mo? Pumili, tapos sabihin nang malakas.'),
           'Jonas: „Kommen Sie aus Österreich?“', 'Nein, ich komme aus den Philippinen.', ['Ja, ich komme aus den Philippinen.', 'Nein, ich auch.'],
           L('Richtig: „Nein, ich komme aus den Philippinen.“ Die Antwort auf die Frage ist „nein“, und danach sagen Sie, was richtig ist. „Ja, ich komme aus den Philippinen“ passt nicht zur Frage. „Nein, ich auch“ widerspricht sich.',
             'Correct: “Nein, ich komme aus den Philippinen.” The answer to the question is “nein”, and then you say what is correct. “Ja, ich komme aus den Philippinen” does not fit the question. “Nein, ich auch” contradicts itself.',
             'Tama: “Nein, ich komme aus den Philippinen.” “Nein” ang sagot sa tanong, at pagkatapos ay sasabihin mo kung ano ang tama. Hindi bagay sa tanong ang “Ja, ich komme aus den Philippinen”. Salungat sa sarili ang “Nein, ich auch”.'),
           [G6, G4], R('nein', 'Philippinen')),
    short(X, 'schreiben', L('Schreiben Sie die Antwort.', 'Anna also comes from Austria. Jonas says: “Ich komme aus Österreich.” Write what Anna answers.', 'Taga-Austria rin si Anna. Sinabi ni Jonas: “Ich komme aus Österreich.” Isulat ang sagot ni Anna.'),
          'Jonas: „Ich komme aus Österreich.“ – Anna: „…“', ['Ich auch!', 'Ich auch.'],
          L('Richtig: „Ich auch!“ Anna kommt auch aus Österreich, bei ihr ist es gleich. „auch“ steht hier nach „ich“.',
            'Correct: “Ich auch!” Anna also comes from Austria, it is the same for her. Here “auch” comes after “ich”.',
            'Tama: “Ich auch!” Taga-Austria rin si Anna, pareho sa kanya. Dito, nasa likod ng “ich” ang “auch”.'),
          [G6], R('auch')),
], intro=INTRO(
    L('Im Kurs fragen sich die Leute: „Kommen Sie aus Österreich?“ oder „Heißen Sie Huber?“ Die Antwort ist „ja“ oder „nein“.',
      'In the course people ask each other: “Kommen Sie aus Österreich?” or “Heißen Sie Huber?” The answer is “ja” or “nein”.',
      'Sa kurso, nagtatanungan ang mga tao: “Kommen Sie aus Österreich?” o “Heißen Sie Huber?” Ang sagot ay “ja” o “nein”.'),
    L('Fragen mit „ja“, „nein“ oder „ich auch“ beantworten – und mit „wer“ und „was“ fragen.',
      'answer questions with “ja”, “nein” or “ich auch” – and ask with “wer” and “was”.',
      'sagutin ang mga tanong gamit ang “ja”, “nein” o “ich auch” – at magtanong gamit ang “wer” at “was”.')))

# L07 ------------------------------------------------------------------ wir, ihr, introduce yourselves
lesson(7, L('Wir stellen uns vor', 'We introduce ourselves', 'Nagpapakilala kami'), ['wir', 'ihr', 'mir', 'vorstellen (sich)'], [
    PHRASE('Ich stelle mich vor: Ich heiße Maria Santos. Ich komme aus den Philippinen.', 'So stellen Sie sich vor: zuerst der Name, dann das Land. Das Verb heißt „sich vorstellen“.',
           'This is how you introduce yourself: first your name, then your country. The verb is “sich vorstellen”.',
           'Ganito magpakilala: unang ang pangalan, tapos ang bansa. Ang verb ay “sich vorstellen”.'),
    RULE('ich stelle mich vor · wir stellen uns vor', 'Das Verb hat zwei Teile: „stelle … vor“. Der Teil „vor“ steht am Ende des Satzes. „mich“ gehört zu „ich“, „uns“ gehört zu „wir“.',
         'The verb has two parts: “stelle … vor”. The part “vor” comes at the end of the sentence. “mich” goes with “ich”, “uns” goes with “wir”.',
         'Dalawang bahagi ang verb: “stelle … vor”. Ang bahaging “vor” ay nasa dulo ng pangungusap. Ang “mich” ay para sa “ich”, ang “uns” ay para sa “wir”.',
         ['Ich stelle mich vor.', 'Wir stellen uns vor.']),
    RULE('wir kommen · ihr kommt', '„wir“ heißt „ich und andere“: Das Verb endet auf -en (wir kommen). „ihr“ sagen Sie zu zwei oder mehr Freunden: Das Verb endet auf -t (ihr kommt).',
         '“wir” means “I and others”: the verb ends in -en (wir kommen). You say “ihr” to two or more friends: the verb ends in -t (ihr kommt).',
         'Ang “wir” ay “ako at ang iba”: nagtatapos sa -en ang verb (wir kommen). Ang “ihr” ay sinasabi sa dalawa o higit pang kaibigan: nagtatapos sa -t ang verb (ihr kommt).',
         ['Wir kommen aus Österreich.', 'Woher kommt ihr?']),
    RULE('wir sind · ihr seid', 'Auch hier ist „sein“ besonders: wir sind, ihr seid. Zu mehreren Personen, die Sie nicht gut kennen, sagen Sie weiter „Sie sind“.',
         '“sein” is special here, too: wir sind, ihr seid. To several people you do not know well you still say “Sie sind”.',
         'Espesyal din dito ang “sein”: wir sind, ihr seid. Sa maraming taong hindi mo lubos na kilala, “Sie sind” pa rin ang sinasabi mo.',
         ['Wir sind Anna und Jonas.', 'Seid ihr Maria und Jose?']),
    PHRASE("Wie geht's dir? – Mir geht's gut.", '„dir“ gehört zu „du“, „mir“ gehört zu „ich“: Wie geht’s dir? – Mir geht’s gut. Und dir?',
           '“dir” goes with “du”, “mir” goes with “ich”: Wie geht’s dir? – Mir geht’s gut. Und dir?',
           'Ang “dir” ay para sa “du”, ang “mir” ay para sa “ich”: Wie geht’s dir? – Mir geht’s gut. Und dir?'),
], [
    choice(X, 'lesen', L('Schauen Sie das Bild an. Was antworten Maria und Jose?', 'Anna and Jonas ask Maria and Jose: “Woher kommt ihr?” Look at the flags. What do Maria and Jose answer?', 'Tinanong nina Anna at Jonas sina Maria at Jose: “Woher kommt ihr?” Tingnan ang mga bandila. Ano ang sagot nina Maria at Jose?'),
           None, 'Wir kommen aus den Philippinen.', ['Wir kommen aus Österreich.', 'Ich komme aus den Philippinen.'],
           L('Richtig: „Wir kommen aus den Philippinen.“ Maria und Jose sind zu zweit: „wir“, das Verb endet auf -en. Ihre Flagge ist die der Philippinen. „aus Österreich“ gehört zu Anna und Jonas. „Ich komme …“ sagt nur eine Person.',
             'Correct: “Wir kommen aus den Philippinen.” Maria and Jose are two people: “wir”, and the verb ends in -en. Their flag is the flag of the Philippines. “aus Österreich” belongs to Anna and Jonas. “Ich komme …” is said by only one person.',
             'Tama: “Wir kommen aus den Philippinen.” Dalawa sina Maria at Jose: “wir”, at nagtatapos sa -en ang verb. Ang bandila nila ay ang bandila ng Pilipinas. Ang “aus Österreich” ay kina Anna at Jonas. Ang “Ich komme …” ay sinasabi ng iisang tao lang.'),
           [G7, G4], R('wir', 'Philippinen'), img=PAARE()),
    cloze(X, 'grammatikWortschatz', L('Schauen Sie das Bild an. Ergänzen Sie den Satz.', 'Now Maria and Jose ask the same question, and Anna and Jonas answer. Look at the flags and complete the sentence with the words below.', 'Ngayon, sina Maria at Jose naman ang nagtanong, at sina Anna at Jonas ang sumasagot. Tingnan ang mga bandila at kumpletuhin ang pangungusap gamit ang mga salita sa ibaba.'),
          'Anna und Jonas: Wir {{1}} aus {{2}}.', [['kommen'], ['Österreich']],
          L('Richtig: „Wir kommen aus Österreich.“ Bei „wir“ endet das Verb auf -en; „kommt“ gehört zu „ihr“. Anna und Jonas haben die österreichische Flagge. „Philippinen“ gehört zu Maria und Jose (und dort heißt es „aus den Philippinen“).',
            'Correct: “Wir kommen aus Österreich.” With “wir” the verb ends in -en; “kommt” goes with “ihr”. Anna and Jonas have the Austrian flag. “Philippinen” belongs to Maria and Jose (and there it is “aus den Philippinen”).',
            'Tama: “Wir kommen aus Österreich.” Sa “wir”, nagtatapos sa -en ang verb; ang “kommt” ay para sa “ihr”. Ang bandila nina Anna at Jonas ay ang bandila ng Austria. Ang “Philippinen” ay kina Maria at Jose (at doon ay “aus den Philippinen”).'),
          [G7, G5], R('wir', 'kommen'), img=PAARE(), bank=['kommen', 'kommt', 'Österreich', 'Philippinen']),
    choice(X, 'hoeren', L('Hören Sie. Wen fragt Jonas?', 'Jonas asks a question. Listen: is he asking one person or two?', 'May itinatanong si Jonas. Makinig: isang tao ba o dalawa ang tinatanong niya?'),
           'Jonas fragt …', 'Maria und Jose.', ['Maria.'],
           L('Sie hören: „Woher kommt ihr?“ „ihr“ sagt man zu zwei oder mehr Freunden, und das Verb endet auf -t. Bei nur einer Person würde Jonas sagen: „Woher kommst du?“',
             'You hear: “Woher kommt ihr?” You say “ihr” to two or more friends, and the verb ends in -t. For one person only, Jonas would say: “Woher kommst du?”',
             'Naririnig mo: “Woher kommt ihr?” Ang “ihr” ay sinasabi sa dalawa o higit pang kaibigan, at nagtatapos sa -t ang verb. Kung iisang tao lang, sasabihin ni Jonas: “Woher kommst du?”'),
           [G7, G4], R('ihr', 'woher'), audio='Woher kommt ihr?'),
    cloze(X, 'grammatikWortschatz', L('Ergänzen Sie den Text.', 'Anna and Jonas introduce themselves in the course. Complete the text with the words below.', 'Nagpapakilala sina Anna at Jonas sa kurso. Kumpletuhin ang teksto gamit ang mga salita sa ibaba.'),
          'Wir stellen uns vor: Wir {{1}} Anna und Jonas. Wir {{2}} aus Österreich.', [['heißen', 'sind'], ['kommen']],
          L('Richtig: „Wir heißen Anna und Jonas. Wir kommen aus Österreich.“ Bei „wir“ endet das Verb auf -en. „heißt“ und „kommt“ gehören zu er/sie (und „kommt“ zu „ihr“).',
            'Correct: “Wir heißen Anna und Jonas. Wir kommen aus Österreich.” With “wir” the verb ends in -en. “heißt” and “kommt” go with er/sie (and “kommt” also with “ihr”).',
            'Tama: “Wir heißen Anna und Jonas. Wir kommen aus Österreich.” Sa “wir”, nagtatapos sa -en ang verb. Ang “heißt” at “kommt” ay para sa er/sie (at ang “kommt” ay para rin sa “ihr”).'),
          [G5, G7], R('wir', 'heißen', 'kommen'), bank=['heißen', 'kommen', 'heißt', 'kommt'], hints=['(heißen)', '(kommen)']),
    cloze(X, 'grammatikWortschatz', L('Ergänzen Sie den Satz.', 'Jonas asks Maria and Jose, two friends. Complete his question with the word below.', 'Tinatanong ni Jonas sina Maria at Jose, dalawang kaibigan. Kumpletuhin ang tanong niya gamit ang salita sa ibaba.'),
          'Jonas: Woher kommt {{1}}?', [['ihr']],
          L('Richtig: „Woher kommt ihr?“ Das Verb „kommt“ mit -t gehört zu „ihr“. „du“ braucht „kommst“, und „wir“ braucht „kommen“.',
            'Correct: “Woher kommt ihr?” The verb “kommt” with -t goes with “ihr”. “du” needs “kommst”, and “wir” needs “kommen”.',
            'Tama: “Woher kommt ihr?” Ang verb na “kommt” na may -t ay para sa “ihr”. Ang “du” ay nangangailangan ng “kommst”, at ang “wir” ng “kommen”.'),
          [G7], R('ihr'), bank=['ihr', 'du', 'wir']),
    cloze(X, 'grammatikWortschatz', L('Ergänzen Sie den Dialog.', 'Jonas asks Maria how she is. Complete the dialogue with the words below.', 'Tinanong ni Jonas si Maria kung kumusta siya. Kumpletuhin ang dialogo gamit ang mga salita sa ibaba.'),
          "Jonas: Wie geht's dir?\nMaria: Danke, {{1}} geht's gut.", [['mir']],
          L('Richtig: „Mir geht’s gut.“ „mir“ gehört zu „ich“: Maria spricht über sich. „dir“ gehört zu „du“ (Jonas). „ich geht’s“ gibt es nicht.',
            'Correct: “Mir geht’s gut.” “mir” goes with “ich”: Maria talks about herself. “dir” goes with “du” (Jonas). “ich geht’s” does not exist.',
            'Tama: “Mir geht’s gut.” Ang “mir” ay para sa “ich”: si Maria ay nagsasalita tungkol sa sarili. Ang “dir” ay para sa “du” (si Jonas). Walang “ich geht’s”.'),
          [G6, G7], R('mir', 'dir'), bank=['mir', 'dir', 'ich']),
    choice(X, 'sprechen', L('Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'You are Maria Santos. It is the first day in the course and you introduce yourself. What do you say? Choose, then say it aloud.', 'Ikaw si Maria Santos. Unang araw sa kurso at nagpapakilala ka. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'),
           None, 'Ich stelle mich vor: Ich heiße Maria Santos.', ['Ich stelle mich: Ich heiße Maria Santos.', 'Ich stelle vor mich: Ich heiße Maria Santos.'],
           L('Richtig: „Ich stelle mich vor.“ Das Verb hat zwei Teile: „stelle“ und „vor“. „vor“ steht am Ende. „mich“ gehört zu „ich“. „Ich stelle mich:“ ohne „vor“ ist unvollständig, und „vor mich“ steht an der falschen Stelle.',
             'Correct: “Ich stelle mich vor.” The verb has two parts: “stelle” and “vor”. “vor” comes at the end. “mich” goes with “ich”. “Ich stelle mich:” without “vor” is incomplete, and “vor mich” is in the wrong place.',
             'Tama: “Ich stelle mich vor.” Dalawang bahagi ang verb: “stelle” at “vor”. Nasa dulo ang “vor”. Ang “mich” ay para sa “ich”. Kulang ang “Ich stelle mich:” kung walang “vor”, at mali ang puwesto ng “vor mich”.'),
           [G2, G7], R('vorstellen (sich)', 'ich')),
    short(X, 'schreiben', L('Schreiben Sie den Satz.', 'You are Maria. You and your friend Jose introduce yourselves in the course. Write the sentence with the words in the brackets.', 'Ikaw si Maria. Magkasama kayo ng kaibigan mong si Jose na nagpapakilala sa kurso. Isulat ang pangungusap gamit ang mga salita sa panaklong.'),
          '(wir – heißen – Maria und Jose)', ['Wir heißen Maria und Jose.', 'Wir sind Maria und Jose.'],
          L('Richtig: „Wir heißen Maria und Jose.“ Bei „wir“ endet das Verb auf -en. „Wir sind Maria und Jose.“ ist auch richtig.',
            'Correct: “Wir heißen Maria und Jose.” With “wir” the verb ends in -en. “Wir sind Maria und Jose.” is also correct.',
            'Tama: “Wir heißen Maria und Jose.” Sa “wir”, nagtatapos sa -en ang verb. Tama rin ang “Wir sind Maria und Jose.”'),
          [G2, G7], R('wir', 'heißen')),
], intro=INTRO(
    L('Erster Tag im Deutschkurs in Wien. Maria und Jose stellen sich vor. Anna und Jonas fragen: „Woher kommt ihr?“',
      'First day of the German course in Vienna. Maria and Jose introduce themselves. Anna and Jonas ask: “Woher kommt ihr?”',
      'Unang araw ng kursong German sa Vienna. Nagpapakilala sina Maria at Jose. Nagtanong sina Anna at Jonas: “Woher kommt ihr?”'),
    L('sich und andere vorstellen: „Ich stelle mich vor“, „Wir kommen aus …“ und „Woher kommt ihr?“',
      'introduce yourself and others: “Ich stelle mich vor”, “Wir kommen aus …” and “Woher kommt ihr?”',
      'magpakilala ng sarili at ng iba: “Ich stelle mich vor”, “Wir kommen aus …” at “Woher kommt ihr?”')))

# ---------------------------------------------------------------- checks (content standard v2 §1–§4) and output
for _l in LESSONS:
    assert _l.get('intro') and 3 <= len(_l['cards']) <= 6 and 6 <= len(_l['items']) <= 8, (_l['id'], len(_l['cards']), len(_l['items']))
    assert len({i['skill'] for i in _l['items']}) >= 2, _l['id']
    for _it in _l['items']:
        assert all(_it['instruction'][k] and _it['explanation'][k] for k in ('de', 'en', 'tl')), _it['id']
        assert _it.get('goals') and _it.get('refs'), _it['id']
        if _it.get('image'):
            assert all(_it['image']['alt'][k] for k in ('de', 'en', 'tl')), _it['id']
        if _it['type'] == 'choice':
            assert len(set(_it['options'])) == len(_it['options']) >= 2 and 0 <= _it['answer'] < len(_it['options']), _it['id']
        if _it['type'] == 'cloze':
            assert len(_it['gaps']) <= 3 and (_it.get('bank') or any(g.get('hint') for g in _it['gaps'].values())), _it['id']
            if _it.get('bank'):
                assert all(g['accept'][0] in _it['bank'] for g in _it['gaps'].values()), _it['id']
                assert len(_it['bank']) - len(_it['gaps']) in (1, 2), _it['id']
    assert not [c for c in _l['cards'] if c['kind'] == 'rule' and not c.get('examples')], _l['id']

# vocabulary exactly as in the hand-written file (same order, ids, lemma, glosses); every word is introduced by a lesson
_ids = {NEW[k]: k for k in NEW}
_vocab = [{'id': NEW[k], 'lemma': lem, 'en': en, 'tl': tl, **({'article': art} if art else {})} for k, (lem, art, en, tl) in VOCAB.items()]
assert {v['id'] for v in _vocab} == {r for l in LESSONS for r in l['introduces']}, 'every vocabulary id must be introduced exactly by the lessons'
assert sum(len(l['introduces']) for l in LESSONS) == len(_vocab)

write_svgs('/tmp/a1-01.png')
# lessons and vocab only: the pools file (a1-01-pools.json) is hand-written and stays untouched
(CONTENT / 'a1-01.json').write_text(json.dumps({'schemaVersion': 1, 'chapterId': CH, 'tlReviewStatus': 'machine', 'vocab': _vocab, 'lessons': LESSONS}, ensure_ascii=False, indent='\t'))
print(f'{CH}: {len(LESSONS)} lessons / {sum(len(l["items"]) for l in LESSONS)} tasks:', [len(l['items']) for l in LESSONS])
