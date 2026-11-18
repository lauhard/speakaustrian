# A1-05 "Im Deutschkurs" – lessons, pools, pictures. Run: python3 scripts/content/a1-05.py
import lib
lib.init('A1-05', seed=20261120, sources=['Q36'])
from lib import *  # noqa: E402,F403

GOALS = {
    'A1-05-G1': L('Dinge im Kurs benennen', 'Naming things in the course', 'Pangalanan ang mga gamit sa kurso'),
    'A1-05-G2': L('Arbeitsanweisungen verstehen (ankreuzen, ergänzen, zuordnen)', 'Understanding task instructions (tick, complete, match)', 'Umintindi ng instructions (markahan, kumpletuhin, itugma)'),
    'A1-05-G3': L('Im Kurs nachfragen: Was bedeutet …? Wie sagt man …?', 'Asking in class: what does … mean? how do you say …?', 'Magtanong sa klase: Ano ang ibig sabihin ng …?'),
    'A1-05-G4': L('Verneinung mit nicht und kein', 'Negation with nicht and kein', 'Pagtanggi gamit ang nicht at kein'),
    'A1-05-G5': L('Kurze Texte lesen: richtig oder falsch?', 'Reading short texts: true or false?', 'Magbasa ng maikling teksto: tama o mali?'),
    'A1-05-G6': L('Lernen in Österreich: Frauen und Männer, Deutsch lernen', 'Learning in Austria: women and men, learning German', 'Pag-aaral sa Austria: babae at lalaki, pag-aaral ng German'),
}
G1, G2, G3, G4, G5, G6 = GOALS

V = {
    'kein': (None, 'no, not a (before nouns)', 'wala / hindi (bago ng noun)'), 'nicht': (None, 'not', 'hindi'), 'lernen': (None, 'to learn', 'mag-aral'), 'warten': (None, 'to wait', 'maghintay'),
    'bringen': (None, 'to bring', 'magdala'), 'holen': (None, 'to fetch, get', 'kunin'), 'zeigen': (None, 'to show', 'ipakita'), 'öffnen': (None, 'to open', 'buksan'),
    'richtig': (None, 'right, correct', 'tama'), 'falsch': (None, 'wrong', 'mali'), 'Zigarette': ('die', 'cigarette', 'sigarilyo'), 'willkommen': (None, 'welcome', 'maligayang pagdating'),
    'Kurs': ('der', 'course', 'kurso'), 'Deutschkurs': ('der', 'German course', 'kursong German'), 'Lehrer, Lehrerin': ('der', 'teacher (man, woman)', 'guro'), 'Buch': ('das', 'book', 'libro'),
    'Heft': ('das', 'exercise book', 'kuwaderno'), 'Kugelschreiber': ('der', 'ballpoint pen', 'ballpen'), 'Bleistift': ('der', 'pencil', 'lapis'), 'Papier': ('das', 'paper', 'papel'),
    'Seite': ('die', 'page', 'pahina'), 'Wort': ('das', 'word', 'salita'), 'Satz': ('der', 'sentence', 'pangungusap'), 'Text': ('der', 'text', 'teksto'), 'Frage': ('die', 'question', 'tanong'),
    'Antwort': ('die', 'answer', 'sagot'), 'Beispiel': ('das', 'example', 'halimbawa'), 'Aufgabe': ('die', 'task, exercise', 'gawain'), 'Prüfung': ('die', 'exam', 'pagsusulit / exam'), 'Test': ('der', 'test', 'test'),
    'ankreuzen': (None, 'to tick, mark with a cross', 'markahan ng ekis'), 'ergänzen': (None, 'to complete, fill in', 'kumpletuhin'), 'zuordnen': (None, 'to match', 'itugma'), 'markieren': (None, 'to mark, highlight', 'markahan'),
    'erklären': (None, 'to explain', 'ipaliwanag'), 'üben': (None, 'to practise', 'magsanay'), 'bedeuten': (None, 'to mean', 'ibig sabihin'), 'Hausübung': ('die', 'homework (in Germany: Hausaufgabe)', 'takdang-aralin (sa Germany: Hausaufgabe)'),
    'Tafel': ('die', 'board', 'pisara'), 'Pause': ('die', 'break', 'pahinga'), 'Fehler': ('der', 'mistake', 'mali'), 'Lösung': ('die', 'solution', 'sagot / solusyon'), 'Unterricht': ('der', 'lessons, class', 'klase'),
    'Thema': ('das', 'topic', 'paksa'), 'Aussage': ('die', 'statement', 'pahayag'), 'Blatt': ('das', 'sheet', 'pahina / papel'), 'Bogen': ('der', 'sheet, form', 'form'), 'herein': (None, 'come in', 'pasok'),
    'Stift': ('der', 'pen', 'panulat'), 'zuhören': (None, 'to listen', 'makinig'), 'Hausaufgabe': ('die', 'homework (German form)', 'takdang-aralin (German)'),
}

# ---------------------------------------------------------------- pictures
# Content standard v2 §5: Buch and Heft differ by shape, not by colour.
# Buch = hard cover, thick page block (visible page edges right and below), spine with bands, title plate.
# Heft = thin soft cover, spiral binding on the left, name label with lines, no page block.
def BOOK(x, y, w=80, h=100):
    t = 10
    edges = ''.join(f'<path d="M{x + w + k} {y + 3 + k}V{y + h + k}" stroke="#b9ad95" stroke-width="1"/>' for k in (2, 4, 6, 8))
    edges += ''.join(f'<path d="M{x + 3 + k} {y + h + k}H{x + w + k}" stroke="#b9ad95" stroke-width="1"/>' for k in (2, 4, 6, 8))
    return (f'<rect x="{x + t}" y="{y + t}" width="{w}" height="{h}" rx="2" fill="#fbf7ee" stroke="#8a7a5a" stroke-width="1.2"/>' + edges
            + f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="#1d4e89" stroke="#12345e" stroke-width="1.5"/>'
            + f'<rect x="{x}" y="{y}" width="12" height="{h}" rx="3" fill="#163d6b"/>'
            + f'<path d="M{x} {y + 14}h12M{x} {y + h - 14}h12" stroke="#e0b44a" stroke-width="2.5"/>'
            + f'<rect x="{x + 20}" y="{y + 16}" width="{w - 30}" height="26" rx="2" fill="#f3ead9"/>'
            + (label(x + 5 + w / 2, y + 34, 'DEUTSCH', 10, '#1d4e89') if w >= 75 else label(x + 5 + w / 2, y + 34, 'A1', 12, '#1d4e89'))
            + f'<path d="M{x + 26} {y + h - 22}h{w - 42}" stroke="#e0b44a" stroke-width="2"/>')


def HEFT(x, y, w=68, h=92):
    rings = ''.join(f'<ellipse cx="{x + 2}" cy="{y + 8 + 10 * k}" rx="5" ry="2.6" fill="none" stroke="#6b7280" stroke-width="1.8"/>' for k in range(int((h - 10) / 10) + 1))
    return (f'<rect x="{x + 2}" y="{y + 2}" width="{w}" height="{h}" rx="2" fill="#00000014"/>'
            + f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="#f6c94c" stroke="#b8901f" stroke-width="1.2"/>'
            + f'<rect x="{x + 14}" y="{y + 18}" width="{w - 24}" height="28" rx="2" fill="#fff" stroke="#b8901f" stroke-width="1"/>'
            + f'<path d="M{x + 18} {y + 28}h{w - 32}M{x + 18} {y + 38}h{w - 32}" stroke="#9ca3af" stroke-width="1.2"/>' + rings)


DESK = lambda: ('<rect x="10" y="168" width="380" height="92" fill="#a8743f"/>'
                + BOOK(26, 66) + HEFT(140, 78)
                + '<path d="M230 200l70-70 8 8-70 70-12 4z" fill="#1d4e89"/><path d="M300 130l8 8 6-6-8-8z" fill="#111"/><path d="M226 204l12-4-8-8z" fill="#e5e7eb"/>'
                + '<path d="M320 205l60-60 6 6-60 60-9 3z" fill="#f2c14e" stroke="#7a4e2d" stroke-width="1"/><path d="M380 145l6 6 4-10z" fill="#f1c9a5"/><path d="M388 143l2 4 1-3z" fill="#333"/>')
PICS['sachen'] = DESK() + ''.join(f'<circle cx="{x}" cy="{y}" r="14" fill="#c8102e"/>' + label(x, y + 6, str(n), 15, '#fff') for n, x, y in ((1, 70, 48), (2, 174, 60), (3, 270, 112), (4, 355, 128)))
PICS['test'] = ('<rect x="60" y="16" width="280" height="228" rx="6" fill="#fff" stroke="#9ca3af" stroke-width="2"/>' + label(200, 46, 'Test', 22)
                + ''.join(label(90, y, f'Frage {n}', 18, anchor='start', bold=False) + label(300, y, m, 26, c) for n, y, m, c in ((1, 100, '✓', '#2a9d8f'), (2, 150, '✗', '#c8102e'), (3, 200, '✓', '#2a9d8f'))))
PICS['tische'] = ('<rect x="10" y="160" width="180" height="20" fill="#a8743f"/><rect x="210" y="160" width="180" height="20" fill="#a8743f"/>'
                  + BOOK(28, 92, 58, 66) + HEFT(112, 104, 46, 56) + HEFT(276, 104, 46, 56)
                  + label(100, 210, 'Maria', 18) + label(300, 210, 'Tom', 18))
PICS['plan'] = ('<rect x="50" y="16" width="300" height="228" rx="8" fill="#fff" stroke="#1d4e89" stroke-width="3"/>' + label(200, 46, 'Deutschkurs A1', 20, '#1d4e89')
                + label(80, 90, 'Unterricht: 9:00', 17, anchor='start', bold=False) + label(80, 125, 'Pause: 10:30', 17, anchor='start', bold=False)
                + label(80, 160, 'Ende: 12:00', 17, anchor='start', bold=False) + label(80, 205, 'Hausübung: Seite 20', 17, anchor='start'))

# ---- redrawn pictures (content standard v2 §5): people with name signs, panels with real scenes
def CARD(cx, y, text, w=70, size=15):
    return (f'<rect x="{cx - w / 2}" y="{y}" width="{w}" height="24" rx="3" fill="#fff" stroke="#6b7280" stroke-width="1.5"/>' + label(cx, y + 17, text, size))


def DESKFRONT(cx, w=88, y=196):
    return f'<rect x="{cx - w / 2}" y="{y}" width="{w}" height="{260 - y}" fill="#a8743f"/><rect x="{cx - w / 2 - 3}" y="{y}" width="{w + 6}" height="7" fill="#c28b52"/>'


PICS['kursraum'] = (
    '<rect x="20" y="12" width="232" height="106" rx="5" fill="#2f5d50" stroke="#7a4e2d" stroke-width="6"/><rect x="20" y="118" width="232" height="6" fill="#7a4e2d"/>'
    + label(136, 60, 'Willkommen!', 26, '#fff') + label(136, 92, 'Deutschkurs A1', 16, '#e5e7eb', bold=False)
    + person(335, '#c8102e', 'a', '#7a4e2d', y=0, s=0.9, long=True) + CARD(335, 200, 'Frau Huber', 94)
    + ''.join(person(x, c, sk, hr, y=-26, s=0.6, long=lg) + DESKFRONT(x) + CARD(x, 214, nm)
              for x, c, sk, hr, nm, lg in ((50, '#1d4e89', 'b', '#222', 'Jose', False), (140, '#2a9d8f', 'a', '#7a4e2d', 'Anna', True), (230, '#f2c14e', 'a', '#b8860b', 'Tom', False))))
PICS['seite'] = ('<rect x="70" y="10" width="260" height="240" rx="4" fill="#fff" stroke="#9ca3af" stroke-width="2"/>' + label(200, 40, 'Aufgabe 3', 20, '#c8102e')
                 + '<rect x="92" y="54" width="216" height="50" rx="4" fill="#fdf3d0" stroke="#e0b44a" stroke-width="1.5"/>'
                 + label(102, 72, 'Beispiel', 14, '#7a5d12', anchor='start') + label(102, 94, 'Ich heiße Anna.', 17, anchor='start', bold=False)
                 + label(92, 134, 'Ich ____ Jose.', 17, anchor='start', bold=False) + label(92, 166, 'Er ____ Tom.', 17, anchor='start', bold=False)
                 + ''.join(f'<path d="M92 {y}h{w}" stroke="#d1d5db" stroke-width="5" stroke-linecap="round"/>' for y, w in ((190, 200), (208, 150)))
                 + label(200, 240, 'Seite 12', 16))
PICS['anweisungen'] = (
    panel(10, 20, 88, 220, 1) + ''.join(f'<rect x="22" y="{y}" width="24" height="24" fill="#fff" stroke="#1f2937" stroke-width="2.5"/>' + label(70, y + 19, t, 17, bold=False) for y, t in ((76, 'a'), (116, 'b'), (156, 'c')))
    + '<path d="M26 122l16 16M42 122l-16 16" stroke="#c8102e" stroke-width="4"/>'
    + panel(108, 20, 88, 220, 2) + label(152, 125, 'Ich ___', 18, bold=False) + '<path d="M128 133h48" stroke="#c8102e" stroke-width="3"/>'
    + '<path d="M156 170l22-22 6 6-22 22-9 3z" fill="#f2c14e" stroke="#7a4e2d" stroke-width="1"/>'
    + panel(206, 20, 88, 220, 3) + ''.join(f'<circle cx="{x}" cy="{y}" r="11" fill="#1d4e89"/>' + label(x, y + 5, t, 14, '#fff') for x, y, t in ((228, 100, '1'), (228, 160, '2'), (272, 100, 'a'), (272, 160, 'b')))
    + '<path d="M239 100L261 160M239 160L261 100" stroke="#1d4e89" stroke-width="3"/>'
    + panel(304, 20, 88, 220, 4) + label(348, 105, 'Ich bin', 16, bold=False) + '<rect x="318" y="122" width="60" height="26" fill="#ffd23f" opacity=".85"/>' + label(348, 141, 'Anna', 18))
PICS['sessel'] = ('<rect y="206" width="400" height="54" fill="#d9c3a3"/>'
                  + '<rect x="316" y="118" width="48" height="80" rx="8" fill="#7a4e2d"/><rect x="324" y="126" width="32" height="64" rx="5" fill="#94643a"/>'
                  + person(60, '#1d4e89', 'b', '#222', y=-24, s=0.7) + person(200, '#2a9d8f', 'a', '#7a4e2d', y=-24, s=0.7, long=True)
                  + ''.join(DESKFRONT(x, 104, 190) + CARD(x, 210, nm) for x, nm in ((60, 'Jose'), (200, 'Anna'), (340, 'Ali'))))
_CLOCK = '<circle cx="{x}" cy="{y}" r="30" fill="#fff" stroke="#1f2937" stroke-width="3"/><path d="M{x} {y}v-20M{x} {y}l14 8" stroke="#1f2937" stroke-width="3.5" stroke-linecap="round"/>'
PICS['verben'] = (
    panel(10, 12, 185, 112, 1) + BOOK(24, 38, 44, 58) + '<path d="M80 70h24m-8-7l8 7-8 7" stroke="#1f2937" stroke-width="3.5" fill="none" stroke-linecap="round"/>'
    + '<path d="M114 52l32 8 32-8v50l-32 8-32-8z" fill="#fbf7ee" stroke="#8a7a5a" stroke-width="2"/><path d="M146 60v50" stroke="#8a7a5a" stroke-width="2"/>'
    + '<path d="M122 70l16 4M122 82l16 4M154 74l16-4M154 86l16-4" stroke="#9ca3af" stroke-width="2"/>'
    + panel(205, 12, 185, 112, 2) + '<rect x="214" y="32" width="104" height="62" fill="#2f5d50" stroke="#7a4e2d" stroke-width="4"/>' + label(266, 72, 'A B C', 20, '#fff')
    + person(362, '#c8102e', 'a', '#7a4e2d', y=-136, s=0.5, long=True) + '<path d="M350 84L326 62" stroke="#f1c9a5" stroke-width="7" stroke-linecap="round"/>'
    + panel(10, 134, 185, 112, 3) + person(60, '#1d4e89', 'b', '#222', y=-14, s=0.5) + _CLOCK.format(x=140, y=190) + label(100, 168, '...', 22)
    + panel(205, 134, 185, 112, 4) + person(250, '#1d4e89', 'b', '#222', y=-14, s=0.5) + '<ellipse cx="236" cy="180" rx="4" ry="8" fill="#e8a64f"/>'
    + '<path d="M286 178q6 10 0 20M298 170q12 18 0 36" stroke="#1d4e89" stroke-width="3" fill="none" stroke-linecap="round"/>'
    + person(362, '#c8102e', 'a', '#7a4e2d', y=-14, s=0.5, long=True) + bubble(300, 142, 54, 'A, B', 14, tail_x=336))
PICS['frage'] = (person(110, '#1d4e89', 'b', '#222') + '<path d="M146 176l16-72" stroke="#1d4e89" stroke-width="16" stroke-linecap="round"/><path d="M162 104l4-22" stroke="#c68a5c" stroke-width="12" stroke-linecap="round"/>'
                 + '<circle cx="167" cy="76" r="12" fill="#c68a5c"/>' + ''.join(f'<path d="M{x} 70l{dx} -10" stroke="#c68a5c" stroke-width="5" stroke-linecap="round"/>' for x, dx in ((161, -3), (167, 0), (173, 3)))
                 + label(110, 246, 'Ali', 15, '#fff') + bubble(190, 24, 200, 'Was bedeutet „Thema“?', 15, tail_x=215)
                 + person(335, '#c8102e', 'a', '#7a4e2d', y=0, s=0.75, long=True))
_CAR = ('<path d="M100 204q0-26 16-30l14-20h38l16 20q14 4 14 30z" fill="#c8102e"/><path d="M134 160h22v14h-32zM162 160h14l10 14h-24z" fill="#cfe8f7"/>'
        '<circle cx="124" cy="206" r="10" fill="#222"/><circle cx="176" cy="206" r="10" fill="#222"/><circle cx="124" cy="206" r="4" fill="#d1d5db"/><circle cx="176" cy="206" r="4" fill="#d1d5db"/>')
PICS['berufe'] = (panel(10, 20, 185, 220, 1) + panel(205, 20, 185, 220, 2)
                  + person(58, '#2a6fb0', 'a', '#7a4e2d', y=-30, s=0.7, long=True) + '<path d="M78 180l34 -10" stroke="#f1c9a5" stroke-width="8" stroke-linecap="round"/><path d="M110 162l14 8-6 12-14-8z" fill="#9ca3af" stroke="#6b7280" stroke-width="2"/>' + _CAR
                  + person(268, '#2a9d8f', 'b', '#222', y=-30, s=0.7) + '<rect x="256" y="172" width="24" height="24" rx="3" fill="#fff"/><path d="M268 175v18M259 184h18" stroke="#c8102e" stroke-width="5"/>'
                  + '<rect x="318" y="140" width="56" height="78" rx="5" fill="#fff" stroke="#6b7280" stroke-width="2.5"/><rect x="336" y="134" width="20" height="10" rx="3" fill="#6b7280"/>'
                  + ''.join(f'<path d="M326 {y}h40" stroke="#9ca3af" stroke-width="3"/>' for y in (160, 174, 188)) + '<path d="M346 196v14M339 203h14" stroke="#c8102e" stroke-width="4"/>')

SACHEN = lambda: img('sachen', 'Ein Tisch mit vier Dingen mit Nummern: Buch, Heft, Kugelschreiber, Bleistift.', 'A desk with four numbered things: book, exercise book, ballpoint pen, pencil.', 'Mesa na may apat na bagay na may numero: libro, kuwaderno, ballpen, lapis.')
PLAN = lambda: img('plan', 'Ein Plan für den Deutschkurs mit Uhrzeiten und der Hausübung.', 'A plan for the German course with times and the homework.', 'Plano ng kursong German na may oras at takdang-aralin.')
TEST_P = lambda: img('test', 'Ein Test mit drei Fragen. Bei zwei Fragen ist ein Häkchen, bei einer ein Kreuz.', 'A test with three questions: two have a tick, one has a cross.', 'Test na may tatlong tanong: dalawa may tsek, isa may ekis.')
BERUFE = lambda: img('berufe', 'Bild 1: eine Frau repariert ein Auto. Bild 2: ein Mann arbeitet als Krankenpfleger.', 'Picture 1: a woman repairs a car. Picture 2: a man works as a nurse.', 'Larawan 1: babaeng nag-aayos ng kotse. Larawan 2: lalaking nars.')

# ---------------------------------------------------------------- lessons (11, A1-05 spec) – content standard v2
X = ''
# Standard v2 asserts (local: lib.py is shared); richtig/falsch items (exam format) have exactly 2 options, all other choices ≥ 3.
def check_lessons():
    for l in LESSONS:
        its = l['items']
        assert l.get('intro') and 3 <= len(l['cards']) <= 6 and 6 <= len(its) <= 8, (l['id'], len(l['cards']), len(its))
        assert any('image' in i for i in its) and any(i['type'] == 'cloze' and (i.get('bank') or any(g.get('hint') for g in i['gaps'].values())) for i in its), l['id']
        assert len({i['skill'] for i in its}) >= 2, l['id']
        for i in its:
            assert all(i['instruction'][k] for k in ('de', 'en', 'tl')) and all(i['explanation'][k] for k in ('de', 'en', 'tl')), i['id']
            if i['type'] == 'choice':
                assert len(set(i['options'])) == len(i['options']) >= (2 if sorted(i['options']) == sorted(RF) else 3), i['id']
            if i['type'] == 'cloze':
                assert len(i['gaps']) <= 3 and ('bank' in i or any('hint' in g for g in i['gaps'].values())), i['id']
                if 'bank' in i:
                    assert all(g['accept'][0] in i['bank'] for g in i['gaps'].values()), i['id']
                    assert len(i['bank']) - len(i['gaps']) in (1, 2), i['id']


RFI = L('Hören Sie. Ist die Aussage richtig oder falsch?', 'Listen. Is the statement right or wrong?', 'Makinig. Tama o mali ang pahayag?')
RFR = L('Lesen Sie. Ist die Aussage richtig oder falsch?', 'Read. Is the statement right or wrong?', 'Basahin. Tama o mali ang pahayag?')
KURS = img('kursraum', 'Ein Kursraum mit Tafel. Drei Leute sitzen an Tischen mit Namensschildern, die Lehrerin steht rechts.', 'A classroom with a board. Three people sit at desks with name signs, the teacher stands on the right.', 'Silid-aralan na may pisara. Tatlong tao ang nakaupo sa mesa na may pangalan, nakatayo ang guro sa kanan.')
SEITE = img('seite', 'Eine Buchseite mit „Aufgabe 3“, einem Beispiel im Kasten und einer Seitenzahl.', 'A book page with “Aufgabe 3”, an example in a box and a page number.', 'Pahina ng libro na may “Aufgabe 3”, halimbawa sa kahon at numero ng pahina.')
ANW = img('anweisungen', 'Vier Bilder: Kästchen mit einem Kreuz, ein Satz mit Lücke und Stift, Linien zwischen Zahlen und Buchstaben, ein farbig markiertes Wort.', 'Four pictures: boxes with one cross, a sentence with a gap and a pencil, lines between numbers and letters, a highlighted word.', 'Apat na larawan: kahon na may ekis, pangungusap na may patlang at lapis, linya sa pagitan ng numero at titik, kulay na salita.')
SESSEL = img('sessel', 'Drei Plätze mit Namensschildern: Jose und Anna sitzen, der Platz von Ali ist leer.', 'Three places with name signs: Jose and Anna are sitting, Ali’s seat is empty.', 'Tatlong upuan na may pangalan: nakaupo sina Jose at Anna, bakante ang upuan ni Ali.')
TISCHE = img('tische', 'Zwei Tische: Maria hat ein Buch und ein Heft, Tom hat nur ein Heft.', 'Two desks: Maria has a book and an exercise book, Tom only an exercise book.', 'Dalawang mesa: may libro at kuwaderno si Maria, kuwaderno lang si Tom.')
VERBEN = img('verben', 'Vier Bilder: ein Buch wird geöffnet, eine Lehrerin zeigt auf die Tafel, ein Mensch und eine Uhr, ein Mensch hört eine Person sprechen.', 'Four pictures: a book is opened, a teacher points at the board, a person and a clock, a person hears someone speak.', 'Apat na larawan: binubuksan ang libro, itinuturo ng guro ang pisara, tao at orasan, tao na nakikinig sa nagsasalita.')
FRAGE = img('frage', 'Ali hebt die Hand und fragt die Lehrerin etwas.', 'Ali raises his hand and asks the teacher something.', 'Itinaas ni Ali ang kamay at may tinatanong sa guro.')

# L01 ------------------------------------------------------------------
lesson(1, L('Willkommen im Deutschkurs!', 'Welcome to the German course!', 'Maligayang pagdating sa kursong German!'), ['Kurs', 'Deutschkurs', 'Lehrer, Lehrerin', 'willkommen', 'Tafel', 'Unterricht', 'herein'], [
    PHRASE('Willkommen im Deutschkurs! – Danke!', 'So begrüßt die Lehrerin die Leute am ersten Tag. Sie antworten: „Danke!“ oder „Grüß Gott!“',
           'This is how the teacher welcomes people on the first day. You answer: “Danke!” or “Grüß Gott!”', 'Ganito binabati ng guro ang mga tao sa unang araw. Sasagot ka ng: “Danke!” o “Grüß Gott!”'),
    RULE('der Lehrer – die Lehrerin', 'Mit -in wird aus dem Mann eine Frau: der Lehrer (Mann), die Lehrerin (Frau). So ist es bei vielen Wörtern für Menschen.',
         'With -in a man becomes a woman: der Lehrer (man), die Lehrerin (woman). Many words for people work like this.',
         'Sa -in, ang lalaki ay nagiging babae: der Lehrer (lalaki), die Lehrerin (babae). Ganito rin ang maraming salita para sa tao.',
         ['Frau Huber ist die Lehrerin.', 'Herr Bauer ist der Lehrer.']),
    PHRASE('Herein! – Bitte, herein!', 'Jemand will in den Kursraum. Sie sagen: „Herein!“ So ist es höflich: „Bitte, herein!“',
           'Someone wants to come into the classroom. You say: “Herein!” (come in). Polite: “Bitte, herein!”', 'May gustong pumasok sa silid-aralan. Sabihin: “Herein!” (pasok). Magalang: “Bitte, herein!”'),
    PHRASE('der Kurs – der Deutschkurs – der Kursraum', 'Im Deutschkurs lernen Leute Deutsch. Der Kursraum ist der Raum für den Kurs. Die Leute im Kurs sind die Kursteilnehmer.',
           'In the German course (Deutschkurs) people learn German. The Kursraum is the classroom. The people in the course are the Kursteilnehmer (learners).', 'Sa Deutschkurs, nag-aaral ng German ang mga tao. Ang Kursraum ay ang silid-aralan. Ang mga tao sa kurso ay ang Kursteilnehmer (mga estudyante).'),
    PHRASE('der Unterricht – die Tafel', 'Der Unterricht ist die Zeit im Kurs, mit der Lehrerin. Die Lehrerin schreibt an die Tafel.',
           'Unterricht means class, the lesson with the teacher. The teacher writes on the board (Tafel).', 'Ang Unterricht ay ang klase kasama ang guro. Sumusulat ang guro sa pisara (Tafel).'),
], [
    choice(X, 'lesen', L('Erster Tag im Deutschkurs. Sie schauen an die Tafel.', 'First day in the German course. You look at the board.', 'Unang araw sa Deutschkurs. Tumingin ka sa pisara.'),
           'Was steht an der Tafel?', 'Willkommen!', ['Herein!', 'Danke!'],
           L('Richtig: „Willkommen!“ Die Lehrerin begrüßt die Leute im Kurs. „Herein!“ sagt man an der Tür, „Danke!“ sagt man als Antwort.',
             'Correct: “Willkommen!” The teacher welcomes the people in the course. “Herein!” is said at the door, “Danke!” is an answer.',
             'Tama: “Willkommen!” Binabati ng guro ang mga tao sa kurso. Ang “Herein!” ay sinasabi sa pinto, ang “Danke!” ay sagot.'),
           [G1], R('willkommen', 'Tafel'), img=KURS),
    choice(X, 'lesen', L('Sie sind neu im Kurs. Wer ist die Lehrerin? Lesen Sie die Namensschilder.', 'You are new in the course. Who is the teacher? Read the name signs.', 'Bago ka sa kurso. Sino ang guro? Basahin ang mga pangalan.'),
           'Wie heißt die Lehrerin?', 'Frau Huber', ['Herr Huber', 'Anna'],
           L('Richtig: Frau Huber. Sie steht an der Tafel und hat das Namensschild „Frau Huber“. Anna sitzt im Kurs. „Herr Huber“ wäre ein Mann.',
             'Correct: Frau Huber. She stands at the board and wears the name sign “Frau Huber”. Anna sits in the course. “Herr Huber” would be a man.',
             'Tama: Frau Huber. Nakatayo siya sa pisara at may pangalang “Frau Huber”. Nakaupo si Anna sa kurso. Ang “Herr Huber” ay lalaki.'),
           [G1], R('Lehrer, Lehrerin', 'Kurs'), img=KURS),
    choice(X, 'grammatikWortschatz', L('Frau Huber stellt sich vor. Wählen Sie das richtige Wort.', 'Frau Huber introduces herself. Choose the correct word.', 'Nagpapakilala si Frau Huber. Piliin ang tamang salita.'),
           'Frau Huber ist …', 'die Lehrerin', ['der Lehrer', 'die Lehrer'],
           L('Richtig: die Lehrerin. Frau Huber ist eine Frau, darum -in. „der Lehrer“ ist ein Mann, „die Lehrer“ sind mehrere Lehrer.',
             'Correct: die Lehrerin. Frau Huber is a woman, so -in. “der Lehrer” is a man, “die Lehrer” are several teachers.',
             'Tama: die Lehrerin. Babae si Frau Huber, kaya -in. Ang “der Lehrer” ay lalaki, ang “die Lehrer” ay maraming guro.'),
           [G1], R('Lehrer, Lehrerin')),
    choice(X, 'hoeren', L('Die Lehrerin spricht zu Ihnen. Hören Sie.', 'The teacher speaks to you. Listen.', 'Nagsasalita ang guro sa iyo. Makinig.'),
           None, 'Frau Huber ist die Lehrerin.', ['Frau Huber ist Annas Tochter.', 'Herr Huber ist der Lehrer.'],
           L('Sie hören: „Willkommen im Deutschkurs! Ich heiße Huber. Ich bin Ihre Lehrerin.“ Eine Frau, die Lehrerin ist: Frau Huber. Von Anna oder von einem Herrn hören Sie nichts.',
             'You hear: “Willkommen im Deutschkurs! Ich heiße Huber. Ich bin Ihre Lehrerin.” A woman who is the teacher: Frau Huber. You hear nothing about Anna or a man.',
             'Naririnig mo: “Willkommen im Deutschkurs! Ich heiße Huber. Ich bin Ihre Lehrerin.” Babaeng guro: si Frau Huber. Walang sinasabi tungkol kay Anna o sa lalaki.'),
           [G1], R('Lehrer, Lehrerin', 'willkommen'), audio='Willkommen im Deutschkurs! Ich heiße Huber. Ich bin Ihre Lehrerin.'),
    cloze(X, 'grammatikWortschatz', L('Jose kommt zum ersten Mal in den Kursraum. Ergänzen Sie den Dialog.', 'Jose enters the classroom for the first time. Complete the dialogue with the words below.', 'Unang beses na pumasok si Jose sa silid-aralan. Kumpletuhin ang dialogo gamit ang mga salita sa ibaba.'),
          'Frau Huber: „{{1}} im Deutschkurs!“ – Jose: „Danke! Grüß Gott.“ – Frau Huber: „Bitte, {{2}}!“', [['Willkommen'], ['herein', 'Herein']],
          L('Richtig: „Willkommen im Deutschkurs!“ und „Bitte, herein!“ Mit „Willkommen“ begrüßen Sie jemanden, mit „herein“ bitten Sie jemanden in den Raum. „Tafel“ ist ein Ding im Kursraum und passt in keine Lücke.',
            'Correct: “Willkommen im Deutschkurs!” and “Bitte, herein!” With “Willkommen” you welcome someone, with “herein” you ask someone to come in. “Tafel” is a thing in the classroom and fits neither gap.',
            'Tama: “Willkommen im Deutschkurs!” at “Bitte, herein!” Ang “Willkommen” ay pagbati, ang “herein” ay pag-anyaya na pumasok. Ang “Tafel” ay bagay sa silid at hindi angkop sa alinmang patlang.'),
          [G1], R('willkommen', 'herein'), bank=['Willkommen', 'herein', 'Tafel']),
    choice(X, 'lesen', L('Anna schreibt eine Nachricht an Tom. Lesen Sie.', 'Anna writes a message to Tom. Read it.', 'Nagsulat si Anna ng mensahe kay Tom. Basahin.'),
           'Anna: „Hallo Tom! Ich bin im Deutschkurs in Wien. Die Lehrerin heißt Frau Huber. Der Unterricht ist sehr gut.“\n\nWas ist richtig?', 'Anna findet den Unterricht sehr gut.', ['Anna ist die Lehrerin.', 'Die Lehrerin heißt Tom.'],
           L('Richtig: „Der Unterricht ist sehr gut.“ Anna ist im Kurs, die Lehrerin ist Frau Huber. Von Tom steht nur: Anna schreibt ihm.',
             'Correct: “Der Unterricht ist sehr gut.” Anna is in the course, the teacher is Frau Huber. About Tom, the text only says that Anna writes to him.',
             'Tama: “Der Unterricht ist sehr gut.” Nasa kurso si Anna, ang guro ay si Frau Huber. Tungkol kay Tom, sinabi lang na sinusulatan siya ni Anna.'),
           [G1], R('Unterricht', 'Lehrer, Lehrerin', 'Deutschkurs')),
    choice(X, 'sprechen', L('Sie sind Frau Huber. Jemand will in den Kursraum. Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'You are Frau Huber. Someone wants to come into the classroom. What do you say? Choose, then say it aloud.', 'Ikaw si Frau Huber. May gustong pumasok sa silid-aralan. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'),
           None, 'Bitte, herein!', ['Auf Wiedersehen!', 'Gute Nacht!'],
           L('Richtig: „Bitte, herein!“ So laden Sie jemanden ein. „Auf Wiedersehen“ und „Gute Nacht“ sagt man beim Gehen.',
             'Correct: “Bitte, herein!” This is how you invite someone in. “Auf Wiedersehen” and “Gute Nacht” are said when leaving.',
             'Tama: “Bitte, herein!” Ganito inaanyayahan ang tao. Ang “Auf Wiedersehen” at “Gute Nacht” ay sinasabi kapag aalis.'),
           [G1], R('herein')),
], intro=INTRO(
    L('Erster Tag im Deutschkurs in Wien. Die Lehrerin heißt Frau Huber. Sie sagt: „Willkommen im Deutschkurs!“',
      'First day of the German course in Vienna. The teacher is called Frau Huber. She says: “Willkommen im Deutschkurs!”',
      'Unang araw ng kursong German sa Vienna. Frau Huber ang pangalan ng guro. Sabi niya: “Willkommen im Deutschkurs!”'),
    L('im Kurs „Willkommen!“ und „Herein!“ sagen und die Lehrerin und den Kursraum benennen',
      'say “Willkommen!” and “Herein!” in the course and name the teacher and the classroom',
      'sabihin ang “Willkommen!” at “Herein!” sa kurso at pangalanan ang guro at ang silid-aralan')))

# L02 ------------------------------------------------------------------
lesson(2, L('Buch, Heft, Stift', 'Book, exercise book, pen', 'Libro, kuwaderno, panulat'), ['Buch', 'Heft', 'Kugelschreiber', 'Bleistift', 'Stift', 'Papier', 'Blatt'], [
    PHRASE('Das ist ein Buch. Das ist ein Heft.', 'Im Buch lesen Sie. Ins Heft schreiben Sie.',
           'You read in the book (Buch: thick, hard cover). You write in the exercise book (Heft: thin, soft cover, here with a spiral).',
           'Nagbabasa ka sa libro (Buch: makapal, matigas na takip). Sumusulat ka sa kuwaderno (Heft: manipis, malambot na takip, may spiral).'),
    RULE('das Buch · das Heft · das Papier · das Blatt', 'Diese vier Wörter haben den Artikel „das“. Ein Blatt ist ein Stück Papier.',
         'These four words take “das”. A Blatt is one sheet of Papier.', 'Ang apat na salitang ito ay “das”. Ang Blatt ay isang pirasong Papier.',
         ['Das Buch ist hier.', 'Ich habe ein Heft.']),
    RULE('der Kugelschreiber · der Bleistift · der Stift', 'Diese drei Wörter haben den Artikel „der“. „Stift“ ist das große Wort: Ein Bleistift ist ein Stift, ein Kugelschreiber auch. Kurz sagt man „Kuli“.',
         'These three words take “der”. “Stift” is the general word: a Bleistift is a Stift, and so is a Kugelschreiber (ballpoint pen; short: Kuli).',
         'Ang tatlong salitang ito ay “der”. Ang “Stift” ay pangkalahatang salita: Stift ang Bleistift at Stift din ang Kugelschreiber (ballpen; maikli: Kuli).',
         ['Der Bleistift ist hier.', 'Das ist ein Stift.']),
    PHRASE('Ein Blatt Papier, bitte. – Hier, bitte.', 'So bitten Sie jemanden im Kurs um Papier. Die Antwort: „Hier, bitte.“',
           'This is how you ask someone in class for paper. The answer: “Hier, bitte.”', 'Ganito ka hihingi ng papel sa kurso. Ang sagot: “Hier, bitte.”'),
], [
    choice(X, 'grammatikWortschatz', L('Frau Huber zeigt vier Dinge. Schauen Sie das Bild an.', 'Frau Huber shows four things. Look at the picture.', 'Nagpapakita si Frau Huber ng apat na bagay. Tingnan ang larawan.'),
           'Nummer 1 ist …', 'das Buch', ['das Heft', 'der Bleistift'],
           L('Richtig: das Buch. Nummer 1 hat einen harten Einband und einen dicken Block aus Seiten. Nummer 2 ist das Heft: dünn, mit Spirale.',
             'Correct: das Buch. Number 1 has a hard cover and a thick block of pages. Number 2 is the Heft: thin, with a spiral.',
             'Tama: das Buch. Ang Nummer 1 ay may matigas na takip at makapal na mga pahina. Ang Nummer 2 ay ang Heft: manipis, may spiral.'),
           [G1], R('Buch'), img=SACHEN()),
    choice(X, 'grammatikWortschatz', L('Frau Huber zeigt vier Dinge. Welches Ding ist ein Heft?', 'Frau Huber shows four things. Which thing is a Heft?', 'Nagpapakita si Frau Huber ng apat na bagay. Alin ang Heft?'),
           'Das Heft ist …', 'Nummer 2', ['Nummer 1', 'Nummer 3'],
           L('Richtig: Nummer 2. Das Heft ist dünn und hat eine Spirale. Nummer 1 ist ein Buch, Nummer 3 ist ein Stift.',
             'Correct: number 2. The Heft is thin and has a spiral. Number 1 is a book, number 3 is a pen.',
             'Tama: Nummer 2. Manipis ang Heft at may spiral. Ang Nummer 1 ay libro, ang Nummer 3 ay panulat.'),
           [G1], R('Heft'), img=SACHEN()),
    choice(X, 'grammatikWortschatz', L('Maria sucht einen Stift zum Schreiben. Schauen Sie das Bild an.', 'Maria needs a pen to write. Look at the picture.', 'Kailangan ni Maria ng pansulat. Tingnan ang larawan.'),
           'Welche Nummer ist der Kugelschreiber?', 'Nummer 3', ['Nummer 4', 'Nummer 2'],
           L('Richtig: Nummer 3 ist der Kugelschreiber (blau, mit schwarzer Spitze). Nummer 4 ist der Bleistift (gelb, mit Holzspitze). Nummer 2 ist ein Heft.',
             'Correct: number 3 is the ballpoint pen (blue, black tip). Number 4 is the pencil (yellow, wooden tip). Number 2 is an exercise book.',
             'Tama: Nummer 3 ang Kugelschreiber (asul, itim ang dulo). Ang Nummer 4 ay Bleistift (dilaw, kahoy ang dulo). Ang Nummer 2 ay Heft.'),
           [G1], R('Kugelschreiber', 'Bleistift'), img=SACHEN()),
    choice(X, 'hoeren', L('Jose fragt Anna im Kurs. Hören Sie.', 'Jose asks Anna in class. Listen.', 'Nagtanong si Jose kay Anna sa kurso. Makinig.'),
           'Was hat Anna?', 'einen Bleistift', ['einen Kugelschreiber', 'ein Heft'],
           L('Sie hören: „Hast du einen Stift? – Ja, hier ist ein Bleistift.“ Anna gibt Jose einen Bleistift, keinen Kugelschreiber und kein Heft.',
             'You hear: “Hast du einen Stift? – Ja, hier ist ein Bleistift.” Anna gives Jose a pencil, not a pen and not an exercise book.',
             'Naririnig mo: “Hast du einen Stift? – Ja, hier ist ein Bleistift.” Bleistift ang ibinigay ni Anna kay Jose, hindi ballpen at hindi kuwaderno.'),
           [G1], R('Bleistift', 'Stift'), audio='Jose: Hast du einen Stift? – Anna: Ja, hier ist ein Bleistift.'),
    cloze(X, 'grammatikWortschatz', L('Maria und Tom suchen Dinge im Kurs. Ergänzen Sie den Artikel.', 'Maria and Tom look for things in class. Complete the article with the words below.', 'Naghahanap sina Maria at Tom ng mga gamit sa kurso. Kumpletuhin ang article gamit ang mga salita sa ibaba.'),
          'Maria: „Wo ist {{1}} Kugelschreiber?“ – Tom: „Hier! Und hier ist {{2}} Heft.“', [['der'], ['das']],
          L('Richtig: der Kugelschreiber, das Heft. Kugelschreiber ist „der“, Heft ist „das“. „die“ passt zu keinem der beiden Wörter.',
            'Correct: der Kugelschreiber, das Heft. Kugelschreiber takes “der”, Heft takes “das”. “die” fits neither word.',
            'Tama: der Kugelschreiber, das Heft. Ang Kugelschreiber ay “der”, ang Heft ay “das”. Ang “die” ay hindi angkop sa alinman.'),
          [G1], R('Kugelschreiber', 'Heft'), bank=['der', 'das', 'die']),
    choice(X, 'grammatikWortschatz', L('Anna fragt Jose: „Hast du einen Stift?“ Jose gibt ihr einen Stift. Was gibt er ihr?', 'Anna asks Jose: “Hast du einen Stift?” Jose gives her a Stift. What does he give her?', 'Tinanong ni Anna si Jose: “Hast du einen Stift?” Binigyan siya ni Jose ng Stift. Ano ang ibinigay niya?'),
           'Jose: „Hier, ein …“', 'Kugelschreiber', ['Heft', 'Buch'],
           L('Richtig: ein Kugelschreiber. Ein Stift ist ein Kugelschreiber oder ein Bleistift. Ein Heft oder ein Buch ist kein Stift.',
             'Correct: ein Kugelschreiber. A Stift is a ballpoint pen or a pencil. An exercise book or a book is not a Stift.',
             'Tama: ein Kugelschreiber. Ang Stift ay ballpen o lapis. Ang Heft o Buch ay hindi Stift.'),
           [G1], R('Stift', 'Kugelschreiber')),
    cloze(X, 'grammatikWortschatz', L('Tom sucht Papier. Ergänzen Sie den Dialog.', 'Tom needs paper. Complete the dialogue with the words below.', 'Kailangan ni Tom ng papel. Kumpletuhin ang dialogo gamit ang mga salita sa ibaba.'),
          'Tom: „Ein {{1}} Papier, bitte.“ – Maria: „Hier, bitte.“', [['Blatt']],
          L('Richtig: „Ein Blatt Papier, bitte.“ Man sagt „ein Blatt Papier“ für ein Stück Papier. „Ein Buch Papier“ und „ein Kugelschreiber Papier“ sagt man nicht.',
            'Correct: “Ein Blatt Papier, bitte.” You say “ein Blatt Papier” for one sheet of paper. “Ein Buch Papier” and “ein Kugelschreiber Papier” are not said.',
            'Tama: “Ein Blatt Papier, bitte.” Sinasabi ang “ein Blatt Papier” para sa isang pirasong papel. Hindi sinasabi ang “ein Buch Papier” at “ein Kugelschreiber Papier”.'),
          [G1], R('Blatt', 'Papier'), bank=['Blatt', 'Buch', 'Kugelschreiber']),
], intro=INTRO(
    L('Anna und Jose sitzen im Deutschkurs. Frau Huber sagt: „Nehmen Sie ein Heft und einen Kugelschreiber.“',
      'Anna and Jose sit in the German course. Frau Huber says: “Take an exercise book and a pen.”',
      'Nakaupo sina Anna at Jose sa Deutschkurs. Sabi ni Frau Huber: “Kunin ninyo ang isang kuwaderno at ballpen.”'),
    L('die Dinge im Kurs benennen: Buch, Heft, Kugelschreiber, Bleistift und ein Blatt Papier',
      'name the things in class: book, exercise book, ballpoint pen, pencil and a sheet of paper',
      'pangalanan ang mga gamit sa kurso: libro, kuwaderno, ballpen, lapis at isang pirasong papel')))

# L03 ------------------------------------------------------------------
lesson(3, L('Wort, Satz, Text, Seite', 'Word, sentence, text, page', 'Salita, pangungusap, teksto, pahina'), ['Wort', 'Satz', 'Text', 'Seite', 'Aufgabe', 'Beispiel', 'Thema'], [
    PHRASE('Seite 12, Aufgabe 3', 'Frau Huber sagt: „Öffnen Sie das Buch auf Seite 12. Machen Sie Aufgabe 3.“',
           'Frau Huber says: “Open the book at page 12. Do exercise 3.”', 'Sabi ni Frau Huber: “Buksan ang libro sa pahina 12. Gawin ang gawain 3.”'),
    RULE('Wort → Satz → Text', 'Ein Wort allein: „Heft“. Mehrere Wörter mit einem Verb sind ein Satz. Mehrere Sätze zusammen sind ein Text.',
         'One word alone: “Heft”. Several words with a verb make a sentence (Satz). Several sentences together make a text.',
         'Isang salita: “Heft”. Ilang salita na may verb ay pangungusap (Satz). Ilang pangungusap ay teksto (Text).',
         ['„Heft“ ist ein Wort.', '„Ich habe ein Heft.“ ist ein Satz.', 'Zwei oder drei Sätze sind ein Text.']),
    PHRASE('das Beispiel', 'Zuerst steht in der Aufgabe ein Beispiel. Dann machen Sie die Aufgabe.',
           'First the exercise has an example (Beispiel). Then you do the exercise.', 'Una, may halimbawa (Beispiel) sa gawain. Pagkatapos, gagawin mo ang gawain.'),
    PHRASE('das Thema', 'Jeder Text hat ein Thema. Das Thema sagt: Worüber ist der Text? Zum Beispiel: Familie.',
           'Every text has a topic (Thema). It says what the text is about. For example: Familie.', 'May paksa (Thema) ang bawat teksto. Ito ang pinag-uusapan ng teksto. Halimbawa: Familie.'),
    RULE('auf Seite 12', 'Bei der Seite sagen Sie „auf Seite …“ und dann die Zahl.',
         'For the page you say “auf Seite …” and then the number.', 'Sa pahina, sasabihin mo ang “auf Seite …” at ang numero.',
         ['Öffnen Sie das Buch auf Seite 20.', 'Wir sind auf Seite 12.']),
], [
    choice(X, 'lesen', L('Anna öffnet das Buch. Schauen Sie die Seite an.', 'Anna opens the book. Look at the page.', 'Binuksan ni Anna ang libro. Tingnan ang pahina.'),
           'Auf welcher Seite ist Aufgabe 3?', 'auf Seite 12', ['auf Seite 3', 'auf Seite 21'],
           L('Richtig: auf Seite 12. Unten auf der Seite steht „Seite 12“. Die 3 ist die Nummer der Aufgabe, nicht der Seite. Bei 21 sind die Ziffern vertauscht.',
             'Correct: auf Seite 12. At the bottom of the page it says “Seite 12”. The 3 is the number of the exercise, not of the page. In 21 the digits are swapped.',
             'Tama: auf Seite 12. Sa ibaba ng pahina nakasulat ang “Seite 12”. Ang 3 ay numero ng gawain, hindi ng pahina. Sa 21, nagpalit ang mga digit.'),
           [G1], R('Seite', 'Aufgabe'), img=SEITE),
    choice(X, 'lesen', L('Tom liest die Aufgabe. Das Beispiel steht im gelben Kasten. Schauen Sie das Bild an.', 'Tom reads the exercise. The example is in the yellow box. Look at the picture.', 'Binabasa ni Tom ang gawain. Nasa dilaw na kahon ang halimbawa. Tingnan ang larawan.'),
           '„Ich heiße Anna.“ ist …', 'ein Satz', ['ein Wort', 'eine Seite'],
           L('Richtig: ein Satz. „Ich heiße Anna.“ hat mehrere Wörter und ein Verb (heiße). Ein Wort wäre nur „Anna“ oder „heiße“. Eine Seite ist ein Blatt im Buch.',
             'Correct: ein Satz. “Ich heiße Anna.” has several words and a verb (heiße). A single word would be only “Anna” or “heiße”. A page is a sheet in the book.',
             'Tama: ein Satz. Ang “Ich heiße Anna.” ay may ilang salita at verb (heiße). Isang salita lang ang “Anna” o “heiße”. Ang pahina ay piraso ng libro.'),
           [G1], R('Satz', 'Beispiel'), img=SEITE),
    choice(X, 'grammatikWortschatz', L('Frau Huber schreibt ein Wort an die Tafel: „Heft“. Was ist das?', 'Frau Huber writes one word on the board: “Heft”. What is it?', 'Nagsulat si Frau Huber ng isang salita sa pisara: “Heft”. Ano ito?'),
           '„Heft“ ist …', 'ein Wort', ['ein Satz', 'eine Aufgabe'],
           L('Richtig: ein Wort. „Heft“ ist ein einzelnes Wort ohne Verb. Ein Satz hat mehrere Wörter und ein Verb. Eine Aufgabe sagt, was Sie machen sollen.',
             'Correct: ein Wort. “Heft” is a single word without a verb. A sentence has several words and a verb. An exercise tells you what to do.',
             'Tama: ein Wort. Ang “Heft” ay iisang salita na walang verb. Ang pangungusap ay maraming salita at may verb. Ang gawain ay nagsasabi kung ano ang gagawin.'),
           [G1], R('Wort')),
    choice(X, 'lesen', L('Lesen Sie den Text von Jose. Frau Huber fragt: „Wie viele Sätze hat der Text?“', 'Read Jose’s text. Frau Huber asks: “How many sentences does the text have?”', 'Basahin ang teksto ni Jose. Tanong ni Frau Huber: “Ilang pangungusap ang teksto?”'),
           'Ich heiße Jose. Ich komme aus den Philippinen. Ich wohne in Wien. Ich lerne Deutsch.\n\nDer Text hat …', 'vier Sätze', ['drei Sätze', 'fünf Sätze'],
           L('Richtig: vier Sätze. Jeder Punkt beendet einen Satz: Ich heiße Jose. / Ich komme … / Ich wohne … / Ich lerne … Das sind vier.',
             'Correct: vier Sätze. Each full stop ends a sentence: Ich heiße Jose. / Ich komme … / Ich wohne … / Ich lerne … That makes four.',
             'Tama: vier Sätze. Ang bawat tuldok ay tapos ng pangungusap: Ich heiße Jose. / Ich komme … / Ich wohne … / Ich lerne … Apat iyon.'),
           [G1], R('Text', 'Satz')),
    choice(X, 'hoeren', L('Frau Huber spricht im Kurs. Hören Sie.', 'Frau Huber speaks in class. Listen.', 'Nagsasalita si Frau Huber sa kurso. Makinig.'),
           'Was sollen Sie machen?', 'Seite 15, Aufgabe 4', ['Seite 50, Aufgabe 4', 'Seite 15, Aufgabe 14'],
           L('Sie hören: „Öffnen Sie das Buch auf Seite fünfzehn. Machen Sie Aufgabe vier.“ fünfzehn = 15, nicht fünfzig (50); vier = 4, nicht vierzehn (14).',
             'You hear: “Öffnen Sie das Buch auf Seite fünfzehn. Machen Sie Aufgabe vier.” fünfzehn = 15, not fünfzig (50); vier = 4, not vierzehn (14).',
             'Naririnig mo: “Öffnen Sie das Buch auf Seite fünfzehn. Machen Sie Aufgabe vier.” fünfzehn = 15, hindi fünfzig (50); vier = 4, hindi vierzehn (14).'),
           [G2], R('Seite', 'Aufgabe', 'öffnen'), audio='Öffnen Sie das Buch auf Seite fünfzehn. Machen Sie Aufgabe vier.'),
    cloze(X, 'grammatikWortschatz', L('Frau Huber gibt eine Anweisung. Ergänzen Sie den Satz mit den Wörtern unten.', 'Frau Huber gives an instruction. Complete the sentence with the words below.', 'May instruction si Frau Huber. Kumpletuhin ang pangungusap gamit ang mga salita sa ibaba.'),
          'Frau Huber: „Öffnen Sie das Buch auf {{1}} 12. Machen Sie {{2}} 3.“', [['Seite'], ['Aufgabe']],
          L('Richtig: „auf Seite 12“ und „Aufgabe 3“. Das Buch hat Seiten, in der Seite stehen Aufgaben. „Satz 12“ und „auf Aufgabe“ passen nicht zu „öffnen“ und „machen“.',
            'Correct: “auf Seite 12” and “Aufgabe 3”. The book has pages, and on a page there are exercises. “Satz” does not fit “auf … 12” and “machen”.',
            'Tama: “auf Seite 12” at “Aufgabe 3”. May mga pahina ang libro, at nasa pahina ang mga gawain. Ang “Satz” ay hindi angkop sa “auf … 12” at “machen”.'),
          [G1, G2], R('Seite', 'Aufgabe'), bank=['Seite', 'Aufgabe', 'Satz']),
    choice(X, 'lesen', L('Lesen Sie den Text. Frau Huber fragt: „Was ist das Thema?“', 'Read the text. Frau Huber asks: “What is the topic?”', 'Basahin ang teksto. Tanong ni Frau Huber: “Ano ang paksa?”'),
           'Meine Mutter heißt Maria. Mein Vater heißt Jose. Ich habe einen Bruder und eine Schwester.\n\nDas Thema ist …', 'die Familie', ['der Deutschkurs', 'die Hausübung'],
           L('Richtig: die Familie. Im Text stehen Mutter, Vater, Bruder und Schwester. Vom Deutschkurs oder von der Hausübung steht nichts im Text.',
             'Correct: die Familie. The text mentions mother, father, brother and sister. It says nothing about the German course or homework.',
             'Tama: die Familie. Nasa teksto ang nanay, tatay, kapatid na lalaki at babae. Walang sinabi tungkol sa Deutschkurs o takdang-aralin.'),
           [G1], R('Thema', 'Text')),
], intro=INTRO(
    L('Frau Huber sagt im Deutschkurs: „Öffnen Sie das Buch auf Seite 12. Machen Sie Aufgabe 3.“ Anna und Jose suchen die Seite.',
      'In the German course Frau Huber says: “Open the book at page 12. Do exercise 3.” Anna and Jose look for the page.',
      'Sa Deutschkurs sabi ni Frau Huber: “Buksan ang libro sa pahina 12. Gawin ang gawain 3.” Hinahanap nina Anna at Jose ang pahina.'),
    L('im Buch die Seite und die Aufgabe finden und Wort, Satz und Text unterscheiden',
      'find the page and the exercise in the book and tell word, sentence and text apart',
      'mahanap ang pahina at ang gawain sa libro at makilala ang salita, pangungusap at teksto')))

# L04 ------------------------------------------------------------------
lesson(4, L('Kreuzen Sie an! – Anweisungen', 'Tick! – instructions', 'Markahan! – mga instruction'), ['ankreuzen', 'ergänzen', 'zuordnen', 'markieren'], [
    PHRASE('Kreuzen Sie die richtige Antwort an.', 'ankreuzen = ein Kreuz (x) machen. So steht es oft in Tests.',
           'ankreuzen = make a cross (x). This is how it often reads in tests.', 'ankreuzen = lagyan ng ekis (x). Ganito ito madalas sa mga test.'),
    PHRASE('Ergänzen Sie die Sätze.', 'ergänzen = ein Wort in die Lücke schreiben. Zum Beispiel: Ich ___ Anna. → Ich heiße Anna.',
           'ergänzen = write a word into the gap. For example: Ich ___ Anna. → Ich heiße Anna.', 'ergänzen = isulat ang salita sa patlang. Halimbawa: Ich ___ Anna. → Ich heiße Anna.'),
    RULE('Ordnen Sie zu. – Kreuzen Sie an.', 'zuordnen und ankreuzen sind trennbare Verben: Die kleine Silbe (zu, an) steht am Ende vom Satz.',
         'zuordnen and ankreuzen are separable verbs: the small part (zu, an) goes to the end of the sentence.',
         'Ang zuordnen at ankreuzen ay mga verb na nahahati: ang maliit na bahagi (zu, an) ay nasa dulo ng pangungusap.',
         ['Ordnen Sie die Wörter zu.', 'Kreuzen Sie die Antwort an.']),
    PHRASE('Markieren Sie das Wort.', 'markieren = ein Wort farbig machen, zum Beispiel gelb. So finden Sie es wieder.',
           'markieren = highlight a word, for example in yellow. This way you find it again.', 'markieren = kulayan ang salita, halimbawa ng dilaw. Para madali mo itong makita ulit.'),
    CULTURE('Anweisungen in der Prüfung', 'In der Prüfung stehen die Anweisungen nur auf Deutsch. Lernen Sie diese vier Wörter gut!',
            'In the exam the instructions are in German only. Learn these four words well!', 'Sa exam, German lang ang nakasulat sa instructions. Aralin nang mabuti ang apat na salitang ito!'),
], [
    choice(X, 'lesen', L('Frau Huber zeigt vier Aufgaben. Schauen Sie das Bild an.', 'Frau Huber shows four exercises. Look at the picture.', 'Nagpapakita si Frau Huber ng apat na gawain. Tingnan ang larawan.'),
           'Bild 1: Was macht man?', 'ankreuzen', ['ergänzen', 'zuordnen'],
           L('Richtig: ankreuzen. In Bild 1 steht ein Kreuz in einem Kästchen. Bild 2 = ergänzen (Wort in die Lücke), Bild 3 = zuordnen (Linien), Bild 4 = markieren.',
             'Correct: ankreuzen. In picture 1 there is a cross in a box. Picture 2 = ergänzen (word in the gap), picture 3 = zuordnen (lines), picture 4 = markieren.',
             'Tama: ankreuzen. Sa Bild 1 may ekis sa kahon. Bild 2 = ergänzen (salita sa patlang), Bild 3 = zuordnen (mga linya), Bild 4 = markieren.'),
           [G2], R('ankreuzen'), img=ANW),
    choice(X, 'lesen', L('Frau Huber zeigt vier Aufgaben. Schauen Sie das Bild an.', 'Frau Huber shows four exercises. Look at the picture.', 'Nagpapakita si Frau Huber ng apat na gawain. Tingnan ang larawan.'),
           'Bild 4: Was macht man?', 'markieren', ['zuordnen', 'ergänzen'],
           L('Richtig: markieren. In Bild 4 ist das Wort „Anna“ gelb. Bei „zuordnen“ verbindet man Paare mit Linien (Bild 3), bei „ergänzen“ schreibt man ein Wort in eine Lücke (Bild 2).',
             'Correct: markieren. In picture 4 the word “Anna” is yellow. With “zuordnen” you connect pairs with lines (picture 3), with “ergänzen” you write a word into a gap (picture 2).',
             'Tama: markieren. Sa Bild 4, dilaw ang salitang “Anna”. Sa “zuordnen”, ikinokonekta ang mga pares ng linya (Bild 3), sa “ergänzen” may isusulat na salita sa patlang (Bild 2).'),
           [G2], R('markieren'), img=ANW),
    choice(X, 'lesen', L('Sie sind im Deutschkurs. Auf dem Blatt steht die Anweisung. Lesen Sie.', 'You are in the German course. The instruction is on the sheet. Read it.', 'Nasa Deutschkurs ka. Nasa papel ang instruction. Basahin.'),
           'Anweisung: „Ergänzen Sie die Wörter.“\n\nWas machen Sie?', 'Ich schreibe die Wörter in die Lücken.', ['Ich mache ein Kreuz.', 'Ich lese den Text.'],
           L('Richtig: Ich schreibe die Wörter in die Lücken. „ergänzen“ heißt: fehlende Wörter schreiben. Ein Kreuz machen Sie bei „ankreuzen“.',
             'Correct: Ich schreibe die Wörter in die Lücken. “ergänzen” means: write the missing words. You make a cross with “ankreuzen”.',
             'Tama: Ich schreibe die Wörter in die Lücken. Ang “ergänzen” ay: isulat ang kulang na salita. Ang ekis ay para sa “ankreuzen”.'),
           [G2], R('ergänzen')),
    choice(X, 'lesen', L('Auf dem Blatt von Frau Huber stehen zwei Anweisungen. Lesen Sie.', 'Frau Huber’s note has two instructions. Read it.', 'May dalawang instruction sa papel ni Frau Huber. Basahin.'),
           '1. Lesen Sie den Text.\n2. Kreuzen Sie an: richtig oder falsch.\n\nWas machen Sie bei 2?', 'Ich mache ein Kreuz bei „richtig“ oder „falsch“.', ['Ich schreibe ein Wort in die Lücke.', 'Ich mache ein Wort gelb.'],
           L('Richtig: ein Kreuz bei „richtig“ oder „falsch“. „ankreuzen“ = ein Kreuz machen. Ein Wort in die Lücke schreiben Sie bei „ergänzen“, ein Wort gelb machen Sie bei „markieren“.',
             'Correct: a cross at “richtig” or “falsch”. “ankreuzen” = make a cross. You write a word in a gap with “ergänzen” and make a word yellow with “markieren”.',
             'Tama: ekis sa “richtig” o “falsch”. “ankreuzen” = lagyan ng ekis. Ang pagsulat ng salita sa patlang ay “ergänzen”, ang pagkulay ng salita ay “markieren”.'),
           [G2, G5], R('ankreuzen', 'lesen', 'richtig', 'falsch')),
    choice(X, 'hoeren', L('Frau Huber gibt eine Anweisung. Hören Sie.', 'Frau Huber gives an instruction. Listen.', 'May instruction si Frau Huber. Makinig.'),
           'Was sollen Sie machen?', 'zuordnen', ['ankreuzen', 'ergänzen'],
           L('Sie hören: „Ordnen Sie die Wörter zu.“ Das Verb ist „zuordnen“. Die Silbe „zu“ steht am Ende. „ankreuzen“ hört man mit „an“, „ergänzen“ hat kein „zu“.',
             'You hear: “Ordnen Sie die Wörter zu.” The verb is “zuordnen”. The syllable “zu” is at the end. “ankreuzen” would end in “an”, “ergänzen” has no “zu”.',
             'Naririnig mo: “Ordnen Sie die Wörter zu.” Ang verb ay “zuordnen”. Nasa dulo ang “zu”. Ang “ankreuzen” ay may “an”, ang “ergänzen” ay walang “zu”.'),
           [G2], R('zuordnen'), audio='Ordnen Sie die Wörter zu.'),
    cloze(X, 'grammatikWortschatz', L('Frau Huber gibt zwei Anweisungen. Ergänzen Sie die kleinen Wörter.', 'Frau Huber gives two instructions. Complete the small words with the words below.', 'May dalawang instruction si Frau Huber. Kumpletuhin ang maliliit na salita gamit ang mga salita sa ibaba.'),
          'Kreuzen Sie die richtige Antwort {{1}}. Ordnen Sie die Wörter {{2}}.', [['an'], ['zu']],
          L('Richtig: „Kreuzen Sie … an.“ und „Ordnen Sie … zu.“ Die kleine Silbe gehört zum Verb: an-kreuzen, zu-ordnen. „auf“ passt zu keinem der beiden Verben.',
            'Correct: “Kreuzen Sie … an.” and “Ordnen Sie … zu.” The small syllable belongs to the verb: an-kreuzen, zu-ordnen. “auf” fits neither verb.',
            'Tama: “Kreuzen Sie … an.” at “Ordnen Sie … zu.” Ang maliit na pantig ay bahagi ng verb: an-kreuzen, zu-ordnen. Ang “auf” ay hindi angkop sa alinman.'),
          [G2], R('ankreuzen', 'zuordnen'), bank=['an', 'zu', 'auf'], hints=['ankreuzen', 'zuordnen']),
], intro=INTRO(
    L('Anna macht einen Test im Deutschkurs. Auf dem Blatt steht: „Kreuzen Sie an.“ Anna kennt das Wort nicht.',
      'Anna takes a test in the German course. The sheet says: “Kreuzen Sie an.” Anna does not know the word.',
      'Nagte-test si Anna sa Deutschkurs. Nakasulat sa papel: “Kreuzen Sie an.” Hindi niya alam ang salita.'),
    L('die vier wichtigsten Anweisungen verstehen: ankreuzen, ergänzen, zuordnen, markieren',
      'understand the four most important instructions: ankreuzen, ergänzen, zuordnen, markieren',
      'maintindihan ang apat na pinakamahalagang instruction: ankreuzen, ergänzen, zuordnen, markieren')))

# L05 ------------------------------------------------------------------
lesson(5, L('Richtig oder falsch?', 'Right or wrong?', 'Tama o mali?'), ['richtig', 'falsch', 'Frage', 'Antwort', 'Lösung', 'Fehler', 'Aussage', 'Prüfung', 'Test'], [
    PHRASE('Ist die Aussage richtig oder falsch?', 'So fragt der Test. Eine Aussage ist ein Satz. Sie lesen den Text und kreuzen an: richtig oder falsch.',
           'This is how the test asks. A statement (Aussage) is a sentence. You read the text and tick: right or wrong.', 'Ganito magtanong ang test. Ang Aussage ay isang pangungusap. Babasahin mo ang teksto at markahan: tama o mali.'),
    RULE('Erst den Text, dann die Aussage', 'Suchen Sie die Stelle im Text. Steht dort dasselbe, ist die Aussage richtig. Steht dort etwas anderes, ist sie falsch.',
         'Find the place in the text. If it says the same, the statement is right. If it says something else, it is wrong.',
         'Hanapin ang bahagi sa teksto. Kung pareho ang nakasulat, tama ang pahayag. Kung iba, mali.',
         ['Der Text sagt: Tom hat ein Heft. Die Aussage „Tom hat ein Heft.“ ist richtig.', 'Die Aussage „Tom hat ein Buch.“ ist falsch.']),
    RULE('die Frage – die Antwort – die Lösung', 'Eine Frage hat eine Antwort. Die Lösung ist die richtige Antwort.',
         'A question (Frage) has an answer (Antwort). The Lösung is the correct answer.', 'May sagot (Antwort) ang tanong (Frage). Ang Lösung ay ang tamang sagot.',
         ['Das ist meine Frage.', 'Die Lösung ist Nummer 3.']),
    PHRASE('der Fehler', 'Ein Fehler ist eine falsche Antwort. Fehler sind im Kurs normal – man lernt daraus.',
           'A mistake (Fehler) is a wrong answer. Mistakes are normal in a course – you learn from them.', 'Ang Fehler ay maling sagot. Normal ang mali sa kurso – natututo ka rito.'),
    PHRASE('die Prüfung – der Test', 'Am Ende vom Kurs gibt es eine Prüfung, in Österreich zum Beispiel die Integrationsprüfung. Im Kurs machen Sie auch Tests.',
           'At the end of the course there is an exam (Prüfung), in Austria for example the Integrationsprüfung (integration exam). In the course you also take tests.', 'Sa dulo ng kurso may exam (Prüfung), sa Austria halimbawa ang Integrationsprüfung. Sa kurso may mga test (Test) din.'),
], [
    choice(X, 'lesen', L('Frau Huber gibt den Test zurück. Schauen Sie das Bild an.', 'Frau Huber hands back the test. Look at the picture.', 'Ibinabalik ni Frau Huber ang test. Tingnan ang larawan.'),
           'Welche Antwort ist falsch?', 'Frage 2', ['Frage 1', 'Frage 3'],
           L('Richtig: Frage 2. Bei Frage 2 steht ein Kreuz (✗): Die Antwort ist falsch. Bei Frage 1 und 3 steht ein Häkchen (✓): richtig.',
             'Correct: Frage 2. Question 2 has a cross (✗): the answer is wrong. Questions 1 and 3 have a tick (✓): right.',
             'Tama: Frage 2. Sa Frage 2 may ekis (✗): mali ang sagot. Sa Frage 1 at 3 may tsek (✓): tama.'),
           [G5], R('falsch', 'Frage', 'Test'), img=TEST_P()),
    choice(X, 'lesen', RFR,
           'Anna schreibt: „Ich bin im Deutschkurs. Meine Lehrerin heißt Frau Huber. Ich habe ein Heft und einen Kugelschreiber.“\n\nAussage: Anna hat einen Kugelschreiber.', 'richtig', ['falsch'],
           L('Richtig. Im Text steht: „Ich habe ein Heft und einen Kugelschreiber.“ Der Satz sagt genau das – darum ist die Aussage richtig.',
             'Right. The text says: “Ich habe ein Heft und einen Kugelschreiber.” That is exactly what the statement says – so it is right.',
             'Tama. Sabi sa teksto: “Ich habe ein Heft und einen Kugelschreiber.” Iyon mismo ang sinasabi ng pahayag – kaya tama.'),
           [G5], R('richtig', 'Aussage')),
    choice(X, 'lesen', RFR,
           'Anna schreibt: „Ich bin im Deutschkurs. Meine Lehrerin heißt Frau Huber. Ich habe ein Heft und einen Kugelschreiber.“\n\nAussage: Anna hat nur einen Kugelschreiber.', 'falsch', ['richtig'],
           L('Falsch. Anna hat einen Kugelschreiber und ein Heft. „nur einen Kugelschreiber“ heißt: sonst nichts. Das stimmt nicht.',
             'Wrong. Anna has a pen and an exercise book. “nur einen Kugelschreiber” means: nothing else. That is not true.',
             'Mali. May ballpen at kuwaderno si Anna. Ang “nur einen Kugelschreiber” ay: wala nang iba. Hindi iyon totoo.'),
           [G5], R('falsch', 'Aussage')),
    choice(X, 'grammatikWortschatz', L('Frau Huber fragt: „Wie heißen Sie?“ Anna sagt: „Ich heiße Anna.“ Wie heißt „Ich heiße Anna.“?', 'Frau Huber asks: “Wie heißen Sie?” Anna says: “Ich heiße Anna.” What is “Ich heiße Anna.”?', 'Tinanong ni Frau Huber: “Wie heißen Sie?” Sabi ni Anna: “Ich heiße Anna.” Ano ang “Ich heiße Anna.”?'),
           '„Ich heiße Anna.“ ist die …', 'Antwort', ['Frage', 'Prüfung'],
           L('Richtig: die Antwort. Frau Huber stellt die Frage, Anna gibt die Antwort. Eine Prüfung ist ein großer Test am Ende vom Kurs.',
             'Correct: die Antwort. Frau Huber asks the question, Anna gives the answer. A Prüfung is a big test at the end of the course.',
             'Tama: die Antwort. Si Frau Huber ang nagtatanong (Frage), si Anna ang sumasagot (Antwort). Ang Prüfung ay malaking test sa dulo ng kurso.'),
           [G5], R('Antwort', 'Frage')),
    cloze(X, 'grammatikWortschatz', L('Tom schreibt „Ich bin Frau Anna.“ Das ist nicht gut. Frau Huber hilft. Ergänzen Sie.', 'Tom writes “Ich bin Frau Anna.” That is not right. Frau Huber helps. Complete with the words below.', 'Sumulat si Tom ng “Ich bin Frau Anna.” Hindi iyon tama. Tumutulong si Frau Huber. Kumpletuhin gamit ang mga salita sa ibaba.'),
          'Frau Huber: „Das ist ein {{1}}. Die richtige {{2}} ist: Ich bin Anna.“', [['Fehler'], ['Lösung', 'Antwort']],
          L('Richtig: „ein Fehler“ und „die richtige Lösung“. Ein Fehler ist falsch geschrieben oder falsch gesagt. Die Lösung ist die richtige Antwort. Eine „Frage“ ist es nicht: Tom hat nichts gefragt.',
            'Correct: “ein Fehler” and “die richtige Lösung”. A Fehler is something written or said wrongly. The Lösung is the correct answer. It is not a “Frage”: Tom did not ask anything.',
            'Tama: “ein Fehler” at “die richtige Lösung”. Ang Fehler ay maling nasulat o nasabi. Ang Lösung ay ang tamang sagot. Hindi ito “Frage”: wala namang tinanong si Tom.'),
          [G5], R('Fehler', 'Lösung'), bank=['Fehler', 'Lösung', 'Frage']),
    choice(X, 'lesen', RFR,
           'Frau Huber sagt: „Wir machen einen Test. Der Test hat zehn Fragen. Sie lesen die Aussage und kreuzen an: richtig oder falsch.“\n\nAussage: Der Test hat zwölf Fragen.', 'falsch', ['richtig'],
           L('Falsch. Im Text steht „zehn Fragen“, nicht „zwölf“. zehn = 10, zwölf = 12.',
             'Wrong. The text says “zehn Fragen”, not “zwölf”. zehn = 10, zwölf = 12.',
             'Mali. Sabi sa teksto “zehn Fragen”, hindi “zwölf”. zehn = 10, zwölf = 12.'),
           [G5], R('falsch', 'Test', 'Frage')),
    choice(X, 'hoeren', RFI,
           'Aussage: Frage drei ist richtig.', 'richtig', ['falsch'],
           L('Sie hören: „Frage zwei ist falsch. Frage drei ist richtig.“ Die Aussage sagt dasselbe wie der zweite Satz: richtig.',
             'You hear: “Frage zwei ist falsch. Frage drei ist richtig.” The statement says the same as the second sentence: right.',
             'Naririnig mo: “Frage zwei ist falsch. Frage drei ist richtig.” Pareho ang sinasabi ng pahayag at ng ikalawang pangungusap: tama.'),
           [G5], R('richtig', 'falsch', 'Frage'), audio='Frau Huber: Frage zwei ist falsch. Frage drei ist richtig.'),
], intro=INTRO(
    L('Frau Huber gibt einen Test. Anna liest: „Ist die Aussage richtig oder falsch?“ So ist es auch in der Prüfung.',
      'Frau Huber gives a test. Anna reads: “Ist die Aussage richtig oder falsch?” This is how it is in the exam too.',
      'May test si Frau Huber. Binasa ni Anna: “Ist die Aussage richtig oder falsch?” Ganito rin sa exam.'),
    L('einen kurzen Text lesen und sagen: Ist die Aussage richtig oder falsch?',
      'read a short text and say: is the statement right or wrong?',
      'magbasa ng maikling teksto at sabihin: tama o mali ang pahayag?')))

# L06 ------------------------------------------------------------------
lesson(6, L('nicht', 'not', 'hindi'), ['nicht'], [
    PHRASE('Ali ist nicht im Kurs.', '„nicht“ sagt: Das stimmt nicht. Bei „sein“ steht „nicht“ vor dem Ort oder vor dem Wort: nicht im Kurs, nicht richtig.',
           '“nicht” says: that is not so. With “sein”, “nicht” goes before the place or the word: nicht im Kurs, nicht richtig.', 'Ang “nicht” ay nagsasabing: hindi totoo iyon. Sa “sein”, ang “nicht” ay bago ang lugar o salita: nicht im Kurs, nicht richtig.'),
    RULE('Verb + … + nicht', 'Bei den meisten Verben steht „nicht“ am Ende vom Satz.',
         'With most verbs, “nicht” comes at the end of the sentence.', 'Sa karamihan ng verb, ang “nicht” ay nasa dulo ng pangungusap.',
         ['Ich verstehe das nicht.', 'Sofia wohnt nicht in Graz.']),
    RULE('Ja oder nein?', 'Auf eine Frage mit Verb am Anfang antworten Sie mit „Ja“ oder „Nein“. Bei „Nein“ steht danach oft „nicht“.',
         'You answer a question that starts with a verb with “Ja” or “Nein”. After “Nein” there is often a “nicht”.',
         'Sa tanong na nagsisimula sa verb, sasagot ka ng “Ja” o “Nein”. Pagkatapos ng “Nein”, madalas may “nicht”.',
         ['Kommt Ali? – Nein, er kommt nicht.', 'Ist das richtig? – Nein, das ist nicht richtig.']),
    PHRASE('Ich verstehe das nicht. – Langsam, bitte.', 'Im Kurs sagen Sie das, wenn Sie etwas nicht verstehen. Dann hilft die Lehrerin.',
           'In class you say this when you do not understand something. Then the teacher helps.', 'Sa kurso sasabihin mo ito kapag hindi mo naiintindihan ang isang bagay. Tutulungan ka ng guro.'),
], [
    choice(X, 'lesen', L('Frau Huber schaut in den Kursraum. Sie fragt: „Ist Ali im Kurs?“ Schauen Sie das Bild an.', 'Frau Huber looks around the classroom. She asks: “Ist Ali im Kurs?” Look at the picture.', 'Tumingin si Frau Huber sa silid-aralan. Tanong niya: “Ist Ali im Kurs?” Tingnan ang larawan.'),
           'Was antworten Sie?', 'Nein, Ali ist nicht im Kurs.', ['Ja, Ali ist im Kurs.', 'Nein, Ali ist kein im Kurs.'],
           L('Richtig: „Nein, Ali ist nicht im Kurs.“ Der Platz von Ali ist leer. Bei „ist im Kurs“ steht „nicht“ vor dem Ort. „kein“ steht nur vor einem Nomen.',
             'Correct: “Nein, Ali ist nicht im Kurs.” Ali’s seat is empty. With “ist im Kurs”, “nicht” goes before the place. “kein” only stands before a noun.',
             'Tama: “Nein, Ali ist nicht im Kurs.” Bakante ang upuan ni Ali. Sa “ist im Kurs”, ang “nicht” ay bago ang lugar. Ang “kein” ay nasa harap lang ng noun.'),
           [G4], R('nicht', 'Kurs'), img=SESSEL),
    choice(X, 'lesen', L('Frau Huber schaut in den Kursraum. Sie fragt: „Wer ist nicht da?“ Schauen Sie das Bild an.', 'Frau Huber looks around the classroom. She asks: “Wer ist nicht da?” Look at the picture.', 'Tumingin si Frau Huber sa silid-aralan. Tanong niya: “Wer ist nicht da?” Tingnan ang larawan.'),
           'Wer ist nicht im Kurs?', 'Ali', ['Jose', 'Anna'],
           L('Richtig: Ali. Jose und Anna sitzen an ihren Plätzen. Der Platz mit dem Namensschild „Ali“ ist leer.',
             'Correct: Ali. Jose and Anna sit at their places. The seat with the name sign “Ali” is empty.',
             'Tama: Ali. Nakaupo sina Jose at Anna sa upuan nila. Bakante ang upuan na may pangalang “Ali”.'),
           [G4], R('nicht', 'Kurs'), img=SESSEL),
    cloze(X, 'grammatikWortschatz', L('Anna versteht die Aufgabe nicht. Ergänzen Sie den Dialog.', 'Anna does not understand the exercise. Complete the dialogue with the words below.', 'Hindi naiintindihan ni Anna ang gawain. Kumpletuhin ang dialogo gamit ang mga salita sa ibaba.'),
          'Frau Huber: „Verstehen Sie das?“ – Anna: „Nein, ich verstehe das {{1}}.“', [['nicht']],
          L('Richtig: „ich verstehe das nicht“. Das Verb „verstehen“ verneinen Sie mit „nicht“ am Ende. „kein“ und „keine“ stehen vor einem Nomen, nicht nach einem Verb.',
            'Correct: “ich verstehe das nicht”. You negate the verb “verstehen” with “nicht” at the end. “kein” and “keine” stand before a noun, not after a verb.',
            'Tama: “ich verstehe das nicht”. Ang verb na “verstehen” ay tinatanggihan ng “nicht” sa dulo. Ang “kein” at “keine” ay nasa harap ng noun, hindi pagkatapos ng verb.'),
          [G4], R('nicht', 'verstehen'), bank=['nicht', 'kein', 'keine']),
    choice(X, 'grammatikWortschatz', L('Frau Huber fragt: „Wohnt Sofia in Graz?“ Sofia wohnt in Linz. Was sagt Anna?', 'Frau Huber asks: “Wohnt Sofia in Graz?” Sofia lives in Linz. What does Anna say?', 'Tanong ni Frau Huber: “Wohnt Sofia in Graz?” Nakatira si Sofia sa Linz. Ano ang sinabi ni Anna?'),
           None, 'Nein, Sofia wohnt nicht in Graz.', ['Nein, Sofia nicht wohnt in Graz.', 'Ja, Sofia wohnt nicht in Graz.'],
           L('Richtig: „Nein, Sofia wohnt nicht in Graz.“ Das Verb „wohnt“ steht an zweiter Stelle, „nicht“ kommt danach. „Ja“ passt nicht, weil Sofia in Linz wohnt.',
             'Correct: “Nein, Sofia wohnt nicht in Graz.” The verb “wohnt” is in second position, “nicht” follows. “Ja” does not fit because Sofia lives in Linz.',
             'Tama: “Nein, Sofia wohnt nicht in Graz.” Nasa ikalawang posisyon ang verb na “wohnt”, kasunod ang “nicht”. Hindi angkop ang “Ja” dahil sa Linz nakatira si Sofia.'),
           [G4], R('nicht', 'wohnen')),
    choice(X, 'hoeren', L('Frau Huber spricht über Anna. Hören Sie.', 'Frau Huber talks about Anna. Listen.', 'Nagsasalita si Frau Huber tungkol kay Anna. Makinig.'),
           None, 'Anna ist nicht im Kurs.', ['Anna ist im Kurs.', 'Anna ist nicht in Graz.'],
           L('Sie hören: „Anna ist nicht im Kurs. Sie ist in Graz.“ Anna ist also in Graz, nicht im Kurs. „nicht in Graz“ wäre das Gegenteil.',
             'You hear: “Anna ist nicht im Kurs. Sie ist in Graz.” So Anna is in Graz, not in the course. “nicht in Graz” would be the opposite.',
             'Naririnig mo: “Anna ist nicht im Kurs. Sie ist in Graz.” Nasa Graz si Anna, wala sa kurso. Ang “nicht in Graz” ay kabaligtaran.'),
           [G4], R('nicht', 'Kurs'), audio='Frau Huber: Anna ist nicht im Kurs. Sie ist in Graz.'),
    choice(X, 'lesen', RFR,
           'Ali schreibt: „Hallo Frau Huber! Ich komme nicht in den Kurs. Ich bin in Linz.“\n\nAussage: Ali ist im Kurs.', 'falsch', ['richtig'],
           L('Falsch. Ali schreibt: „Ich komme nicht in den Kurs. Ich bin in Linz.“ Er ist nicht im Kurs, er ist in Linz.',
             'Wrong. Ali writes: “Ich komme nicht in den Kurs. Ich bin in Linz.” He is not in the course, he is in Linz.',
             'Mali. Sulat ni Ali: “Ich komme nicht in den Kurs. Ich bin in Linz.” Wala siya sa kurso, nasa Linz siya.'),
           [G4, G5], R('nicht', 'Kurs')),
    choice(X, 'sprechen', L('Frau Huber zeigt ein Wort an der Tafel: „Heft“ und fragt Sie: „Ist das Wort richtig?“ Es ist falsch. Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'Frau Huber shows a word on the board and asks you: “Ist das Wort richtig?” It is wrong. What do you say? Choose, then say it aloud.', 'Nagpakita si Frau Huber ng salita sa pisara at tinanong ka: “Ist das Wort richtig?” Mali ito. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'),
           None, 'Nein, das ist nicht richtig.', ['Ja, das ist nicht richtig.', 'Nein, das ist kein richtig.'],
           L('Richtig: „Nein, das ist nicht richtig.“ „Nein“ und „nicht“ passen zusammen. „Ja, … nicht richtig“ widerspricht sich. „richtig“ ist ein Adjektiv, davor steht „nicht“, nicht „kein“.',
             'Correct: “Nein, das ist nicht richtig.” “Nein” and “nicht” go together. “Ja, … nicht richtig” contradicts itself. “richtig” is an adjective, so “nicht” comes before it, not “kein”.',
             'Tama: “Nein, das ist nicht richtig.” Magkasama ang “Nein” at “nicht”. Ang “Ja, … nicht richtig” ay magkasalungat. Ang “richtig” ay adjective, kaya “nicht” ang nasa unahan, hindi “kein”.'),
           [G4], R('nicht', 'richtig')),
], intro=INTRO(
    L('Frau Huber schaut in den Kursraum. Ein Platz ist leer. Sie fragt: „Ist Ali im Kurs?“ Die Antwort ist „Nein“.',
      'Frau Huber looks around the classroom. One seat is empty. She asks: “Ist Ali im Kurs?” The answer is “Nein”.',
      'Tumingin si Frau Huber sa silid-aralan. May bakanteng upuan. Tanong niya: “Ist Ali im Kurs?” Ang sagot ay “Nein”.'),
    L('„nicht“ richtig benutzen: „Ali ist nicht im Kurs.“ „Ich verstehe das nicht.“',
      'use “nicht” correctly: “Ali ist nicht im Kurs.” “Ich verstehe das nicht.”',
      'gamitin nang tama ang “nicht”: “Ali ist nicht im Kurs.” “Ich verstehe das nicht.”')))

# L07 ------------------------------------------------------------------
lesson(7, L('kein, keine', 'no, not a', 'wala, hindi'), ['kein'], [
    PHRASE('Ich habe kein Buch.', '„kein“ sagt: Ich habe nichts davon. Aus „ein Buch“ wird „kein Buch“, aus „ein Heft“ wird „kein Heft“.',
           '“kein” says: I have none of it. “ein Buch” becomes “kein Buch”, “ein Heft” becomes “kein Heft”.', 'Ang “kein” ay nagsasabing: wala akong ganoon. Ang “ein Buch” ay nagiging “kein Buch”, ang “ein Heft” ay “kein Heft”.'),
    RULE('ein → kein · eine → keine', 'Vor einem Nomen mit „ein“ oder „eine“ steht bei „Nein“ das Wort „kein“ oder „keine“. Bei „die“-Wörtern: keine.',
         'Before a noun that has “ein” or “eine”, the negative is “kein” or “keine”. With “die”-words: keine.',
         'Sa noun na may “ein” o “eine”, ang pagtanggi ay “kein” o “keine”. Sa mga salitang “die”: keine.',
         ['Das ist kein Fehler.', 'Ich habe keine Frage.']),
    RULE('Ich habe einen Stift → keinen Stift', 'Bei „der“-Wörtern nach „haben“ wird aus „einen“ das Wort „keinen“. Nach „sein“ bleibt es „kein“: Das ist kein Stift.',
         'With “der”-words after “haben”, “einen” becomes “keinen”. After “sein” it stays “kein”: Das ist kein Stift.',
         'Sa mga salitang “der” pagkatapos ng “haben”, ang “einen” ay nagiging “keinen”. Pagkatapos ng “sein”, “kein” pa rin: Das ist kein Stift.',
         ['Ich habe keinen Kugelschreiber.', 'Das ist kein Bleistift.']),
    RULE('Mehrzahl: keine Bücher', 'Bei der Mehrzahl (Plural) gibt es kein „ein“. Dann heißt die Verneinung immer „keine“: ein Buch → keine Bücher.',
         'In the plural there is no “ein”. The negative is then always “keine”: ein Buch → keine Bücher.', 'Sa plural walang “ein”. Ang pagtanggi ay laging “keine”: ein Buch → keine Bücher.',
         ['Ich habe keine Bücher.', 'Wir haben keine Hefte.']),
    RULE('nicht oder kein?', '„kein“ verneint ein Nomen: Ich habe kein Heft. „nicht“ verneint alles andere: Ich verstehe das nicht. Das ist nicht richtig.',
         '“kein” negates a noun: Ich habe kein Heft. “nicht” negates everything else: Ich verstehe das nicht. Das ist nicht richtig.',
         'Ang “kein” ay para sa noun: Ich habe kein Heft. Ang “nicht” ay para sa lahat ng iba: Ich verstehe das nicht. Das ist nicht richtig.',
         ['Ich habe kein Heft.', 'Ich habe das Heft nicht.']),
], [
    choice(X, 'lesen', L('Maria und Tom machen eine Aufgabe. Frau Huber fragt: „Hat Tom ein Buch?“ Schauen Sie das Bild an.', 'Maria and Tom do an exercise. Frau Huber asks: “Hat Tom ein Buch?” Look at the picture.', 'Gumagawa ng gawain sina Maria at Tom. Tanong ni Frau Huber: “Hat Tom ein Buch?” Tingnan ang larawan.'),
           'Was antworten Sie?', 'Nein, Tom hat kein Buch.', ['Nein, Tom hat nicht Buch.', 'Ja, Tom hat ein Buch.'],
           L('Richtig: „Nein, Tom hat kein Buch.“ Auf dem Tisch von Tom liegt nur ein Heft. „Buch“ ist ein Nomen (ein Buch), darum „kein Buch“. „nicht Buch“ sagt man nicht.',
             'Correct: “Nein, Tom hat kein Buch.” On Tom’s desk there is only an exercise book. “Buch” is a noun (ein Buch), so “kein Buch”. “nicht Buch” is not said.',
             'Tama: “Nein, Tom hat kein Buch.” Kuwaderno lang ang nasa mesa ni Tom. Ang “Buch” ay noun (ein Buch), kaya “kein Buch”. Hindi sinasabi ang “nicht Buch”.'),
           [G4], R('kein', 'Buch'), img=TISCHE),
    choice(X, 'lesen', L('Maria und Tom machen eine Aufgabe. Frau Huber fragt: „Hat Maria ein Heft?“ Schauen Sie das Bild an.', 'Maria and Tom do an exercise. Frau Huber asks: “Hat Maria ein Heft?” Look at the picture.', 'Gumagawa ng gawain sina Maria at Tom. Tanong ni Frau Huber: “Hat Maria ein Heft?” Tingnan ang larawan.'),
           'Was antworten Sie?', 'Ja, Maria hat ein Heft.', ['Nein, Maria hat kein Heft.', 'Ja, Maria hat kein Heft.'],
           L('Richtig: „Ja, Maria hat ein Heft.“ Auf dem Tisch von Maria liegt ein Heft (und ein Buch). Wer „Ja“ sagt, sagt dann „ein Heft“, nicht „kein Heft“.',
             'Correct: “Ja, Maria hat ein Heft.” On Maria’s desk there is an exercise book (and a book). Whoever says “Ja” then says “ein Heft”, not “kein Heft”.',
             'Tama: “Ja, Maria hat ein Heft.” May kuwaderno (at libro) sa mesa ni Maria. Kapag “Ja” ang sagot, “ein Heft” ang kasunod, hindi “kein Heft”.'),
           [G4], R('kein', 'Heft'), img=TISCHE),
    cloze(X, 'grammatikWortschatz', L('Frau Huber fragt Anna. Ergänzen Sie den Dialog mit den Wörtern unten.', 'Frau Huber asks Anna. Complete the dialogue with the words below.', 'Nagtanong si Frau Huber kay Anna. Kumpletuhin ang dialogo gamit ang mga salita sa ibaba.'),
          'Frau Huber: „Haben Sie eine Frage?“ – Anna: „Nein, ich habe {{1}} Frage.“', [['keine']],
          L('Richtig: „keine Frage“. „die Frage“ ist ein „die“-Wort: eine Frage → keine Frage. „kein“ passt zu „der“- und „das“-Wörtern, „nicht“ steht nicht vor einem Nomen mit „eine“.',
            'Correct: “keine Frage”. “die Frage” is a “die”-word: eine Frage → keine Frage. “kein” fits “der”- and “das”-words, “nicht” does not stand before a noun with “eine”.',
            'Tama: “keine Frage”. Ang “die Frage” ay salitang “die”: eine Frage → keine Frage. Ang “kein” ay para sa “der” at “das”, ang “nicht” ay hindi nasa harap ng noun na may “eine”.'),
          [G4], R('kein', 'Frage'), bank=['keine', 'kein', 'nicht']),
    cloze(X, 'grammatikWortschatz', L('Frau Huber zeigt ein Heft. Anna sagt, was es nicht ist. Ergänzen Sie.', 'Frau Huber shows an exercise book. Anna says what it is not. Complete with the words below.', 'Nagpapakita si Frau Huber ng kuwaderno. Sinasabi ni Anna kung ano ito hindi. Kumpletuhin gamit ang mga salita sa ibaba.'),
          'Anna: „Das ist {{1}} Buch. Das ist ein Heft.“', [['kein']],
          L('Richtig: „kein Buch“. „das Buch“ ist ein „das“-Wort: ein Buch → kein Buch. „keine“ gehört zu „die“-Wörtern, „nicht Buch“ gibt es nicht.',
            'Correct: “kein Buch”. “das Buch” is a “das”-word: ein Buch → kein Buch. “keine” belongs to “die”-words, “nicht Buch” does not exist.',
            'Tama: “kein Buch”. Ang “das Buch” ay salitang “das”: ein Buch → kein Buch. Ang “keine” ay para sa “die”, hindi umiiral ang “nicht Buch”.'),
          [G4], R('kein', 'Buch', 'Heft'), bank=['kein', 'keine', 'nicht']),
    choice(X, 'grammatikWortschatz', L('Frau Huber sagt: „Das ist ein Fehler.“ Tom sagt „Nein“. Was sagt Tom?', 'Frau Huber says: “Das ist ein Fehler.” Tom disagrees. What does Tom say?', 'Sabi ni Frau Huber: “Das ist ein Fehler.” Hindi sang-ayon si Tom. Ano ang sasabihin ni Tom?'),
           'Tom: „Nein, das ist … Fehler.“', 'kein', ['keine', 'nicht'],
           L('Richtig: „kein Fehler“. „der Fehler“ ist ein „der“-Wort, nach „sein“ heißt es „kein“. „keine“ ist für „die“-Wörter. „nicht“ steht nicht vor einem Nomen.',
             'Correct: “kein Fehler”. “der Fehler” is a “der”-word, after “sein” it is “kein”. “keine” is for “die”-words. “nicht” does not stand before a noun.',
             'Tama: “kein Fehler”. Ang “der Fehler” ay salitang “der”, pagkatapos ng “sein” ay “kein”. Ang “keine” ay para sa “die”. Ang “nicht” ay hindi nasa harap ng noun.'),
           [G4], R('kein', 'Fehler')),
    choice(X, 'lesen', RFR,
           'Jose schreibt: „Hallo Frau Huber! Ich habe kein Heft und keinen Kugelschreiber. Ich habe nur ein Buch.“\n\nAussage: Jose hat ein Heft.', 'falsch', ['richtig'],
           L('Falsch. Jose schreibt: „Ich habe kein Heft.“ Er hat nur ein Buch. „kein Heft“ heißt: nicht ein einziges Heft.',
             'Wrong. Jose writes: “Ich habe kein Heft.” He only has a book. “kein Heft” means: not a single exercise book.',
             'Mali. Sulat ni Jose: “Ich habe kein Heft.” Libro lang ang mayroon siya. Ang “kein Heft” ay: walang kahit isang kuwaderno.'),
           [G4, G5], R('kein', 'Heft')),
    choice(X, 'sprechen', L('Frau Huber fragt Sie: „Haben Sie einen Kugelschreiber?“ Sie haben keinen. Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'Frau Huber asks you: “Haben Sie einen Kugelschreiber?” You have none. What do you say? Choose, then say it aloud.', 'Tinanong ka ni Frau Huber: “Haben Sie einen Kugelschreiber?” Wala kang ballpen. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'),
           None, 'Nein, ich habe keinen Kugelschreiber.', ['Nein, ich habe nicht Kugelschreiber.', 'Ja, ich habe keinen Kugelschreiber.'],
           L('Richtig: „Nein, ich habe keinen Kugelschreiber.“ Der Kugelschreiber ist ein „der“-Wort, nach „haben“ heißt es „keinen“. „Ja“ und „keinen“ passen nicht zusammen.',
             'Correct: “Nein, ich habe keinen Kugelschreiber.” The Kugelschreiber is a “der”-word, after “haben” it is “keinen”. “Ja” and “keinen” do not go together.',
             'Tama: “Nein, ich habe keinen Kugelschreiber.” Ang Kugelschreiber ay salitang “der”, pagkatapos ng “haben” ay “keinen”. Hindi magkasama ang “Ja” at “keinen”.'),
           [G4], R('kein', 'Kugelschreiber')),
], intro=INTRO(
    L('Maria und Tom machen eine Aufgabe. Maria hat ein Buch und ein Heft. Tom hat nur ein Heft. Frau Huber fragt: „Hat Tom ein Buch?“',
      'Maria and Tom do an exercise. Maria has a book and an exercise book. Tom has only an exercise book. Frau Huber asks: “Hat Tom ein Buch?”',
      'Gumagawa ng gawain sina Maria at Tom. May libro at kuwaderno si Maria. Kuwaderno lang ang kay Tom. Tanong ni Frau Huber: “Hat Tom ein Buch?”'),
    L('sagen, was Sie nicht haben: „Ich habe kein Buch.“ – und „kein“ und „nicht“ unterscheiden',
      'say what you do not have: “Ich habe kein Buch.” – and tell “kein” and “nicht” apart',
      'sabihin kung ano ang wala ka: “Ich habe kein Buch.” – at makilala ang “kein” at “nicht”')))

# L08 ------------------------------------------------------------------
lesson(8, L('Verben im Kurs', 'Verbs in class', 'Mga verb sa klase'), ['öffnen', 'zeigen', 'warten', 'zuhören', 'lernen', 'üben', 'erklären', 'bringen', 'holen'], [
    PHRASE('Öffnen Sie das Buch. – Zeigen Sie das Heft.', 'Frau Huber sagt „Sie“. Das Verb steht am Anfang: Öffnen Sie …, Zeigen Sie …, Bringen Sie …, Holen Sie …',
           'Frau Huber says “Sie”. The verb comes first: Öffnen Sie …, Zeigen Sie …, Bringen Sie …, Holen Sie …', 'Sinasabi ni Frau Huber ang “Sie”. Nasa unahan ang verb: Öffnen Sie …, Zeigen Sie …, Bringen Sie …, Holen Sie …'),
    RULE('warten → er wartet · öffnen → du öffnest', 'Bei „warten“ und „öffnen“ kommt bei er/sie und du ein „e“ dazu. So kann man es besser sprechen.',
         'With “warten” and “öffnen” an “e” is added for er/sie and du. This makes it easier to say.',
         'Sa “warten” at “öffnen”, may idinagdag na “e” sa er/sie at du. Mas madaling bigkasin.',
         ['Tom wartet hier.', 'Du öffnest das Buch.']),
    RULE('zuhören: Ich höre zu.', 'zuhören ist ein trennbares Verb. Die kleine Silbe „zu“ steht am Ende vom Satz.',
         'zuhören is a separable verb. The small syllable “zu” goes to the end of the sentence.', 'Ang zuhören ay verb na nahahati. Ang maliit na pantig na “zu” ay nasa dulo ng pangungusap.',
         ['Ich höre zu.', 'Hören Sie bitte gut zu.', 'Anna hört gut zu.']),
    PHRASE('lernen · üben · erklären', 'Wir lernen Deutsch. Wir üben die Wörter. Frau Huber erklärt die Aufgabe.',
           'We learn German. We practise the words. Frau Huber explains the exercise.', 'Nag-aaral tayo ng German. Nagsasanay tayo ng mga salita. Ipinapaliwanag ni Frau Huber ang gawain.'),
    PHRASE('bringen · holen', 'Bringen Sie das Buch. Holen Sie ein Blatt Papier.',
           'Bringen = take something to a place. Holen = go and get something from a place.', 'Bringen = dalhin sa isang lugar. Holen = kunin mula sa isang lugar.'),
], [
    choice(X, 'grammatikWortschatz', L('Frau Huber zeigt vier Bilder. Schauen Sie das Bild an.', 'Frau Huber shows four pictures. Look at the picture.', 'Nagpapakita si Frau Huber ng apat na larawan. Tingnan ang larawan.'),
           'Bild 3: Was macht der Mensch?', 'warten', ['öffnen', 'zuhören'],
           L('Richtig: warten. In Bild 3 sitzt ein Mensch neben einer Uhr und wartet. Bild 1 = öffnen (Buch), Bild 2 = zeigen, Bild 4 = zuhören.',
             'Correct: warten. In picture 3 a person sits next to a clock and waits. Picture 1 = öffnen (book), picture 2 = zeigen, picture 4 = zuhören.',
             'Tama: warten. Sa Bild 3, may taong nakaupo sa tabi ng orasan at naghihintay. Bild 1 = öffnen (libro), Bild 2 = zeigen, Bild 4 = zuhören.'),
           [G2], R('warten'), img=VERBEN),
    choice(X, 'grammatikWortschatz', L('Frau Huber zeigt vier Bilder. Schauen Sie das Bild an.', 'Frau Huber shows four pictures. Look at the picture.', 'Nagpapakita si Frau Huber ng apat na larawan. Tingnan ang larawan.'),
           'Bild 2: Was macht Frau Huber?', 'Sie zeigt auf die Tafel.', ['Sie öffnet das Buch.', 'Sie wartet.'],
           L('Richtig: Sie zeigt auf die Tafel. In Bild 2 geht ihre Hand zur Tafel mit „A B C“. Das Buch öffnen (Bild 1) und warten (Bild 3) sind andere Bilder.',
             'Correct: Sie zeigt auf die Tafel. In picture 2 her hand points to the board with “A B C”. Opening the book (picture 1) and waiting (picture 3) are other pictures.',
             'Tama: Sie zeigt auf die Tafel. Sa Bild 2, nakaturo ang kamay niya sa pisara na may “A B C”. Ang pagbukas ng libro (Bild 1) at paghihintay (Bild 3) ay ibang larawan.'),
           [G2], R('zeigen', 'Tafel'), img=VERBEN),
    cloze(X, 'grammatikWortschatz', L('Frau Huber und Anna im Kurs. Ergänzen Sie das richtige Verb.', 'Frau Huber and Anna in class. Complete with the correct verb.', 'Sina Frau Huber at Anna sa kurso. Kumpletuhin ang tamang verb.'),
          'Frau Huber {{1}} die Aufgabe. Anna {{2}} gut zu.', [['erklärt'], ['hört']],
          L('Richtig: „Frau Huber erklärt die Aufgabe. Anna hört gut zu.“ Die Lehrerin erklärt, Anna hört zu. „zuhören“ ist trennbar: hört … zu. „wartet“ passt zu keiner Lücke.',
            'Correct: “Frau Huber erklärt die Aufgabe. Anna hört gut zu.” The teacher explains, Anna listens. “zuhören” is separable: hört … zu. “wartet” fits neither gap.',
            'Tama: “Frau Huber erklärt die Aufgabe. Anna hört gut zu.” Ang guro ay nagpapaliwanag, nakikinig si Anna. Ang “zuhören” ay nahahati: hört … zu. Ang “wartet” ay hindi angkop sa alinmang patlang.'),
          [G2], R('erklären', 'zuhören'), bank=['erklärt', 'hört', 'wartet'], hints=['erklären', 'zuhören']),
    cloze(X, 'grammatikWortschatz', L('Tom und Jose im Kurs. Ergänzen Sie die Verbformen mit den Wörtern unten.', 'Tom and Jose in class. Complete the verb forms with the words below.', 'Sina Tom at Jose sa kurso. Kumpletuhin ang mga anyo ng verb gamit ang mga salita sa ibaba.'),
          'Tom {{1}} hier. Jose, du {{2}} das Buch.', [['wartet'], ['öffnest']],
          L('Richtig: „Tom wartet hier. Jose, du öffnest das Buch.“ Bei „Tom“ (er) endet das Verb auf -et, bei „du“ auf -est. „wartest“ und „öffnet“ gehören zu den anderen Personen.',
            'Correct: “Tom wartet hier. Jose, du öffnest das Buch.” With “Tom” (er) the verb ends in -et, with “du” in -est. “wartest” and “öffnet” belong to the other persons.',
            'Tama: “Tom wartet hier. Jose, du öffnest das Buch.” Sa “Tom” (er), nagtatapos sa -et ang verb, sa “du” sa -est. Ang “wartest” at “öffnet” ay para sa ibang tao.'),
          [G2], R('warten', 'öffnen'), bank=['wartet', 'öffnest', 'wartest', 'öffnet']),
    choice(X, 'hoeren', L('Frau Huber gibt eine Anweisung. Hören Sie.', 'Frau Huber gives an instruction. Listen.', 'May instruction si Frau Huber. Makinig.'),
           'Was sollen Sie machen?', 'das Buch öffnen', ['das Buch holen', 'das Buch zeigen'],
           L('Sie hören: „Öffnen Sie bitte das Buch.“ Das Verb ist „öffnen“. Bei „holen“ geht man das Buch suchen, bei „zeigen“ hält man es hoch.',
             'You hear: “Öffnen Sie bitte das Buch.” The verb is “öffnen”. With “holen” you go and get the book, with “zeigen” you hold it up.',
             'Naririnig mo: “Öffnen Sie bitte das Buch.” Ang verb ay “öffnen”. Sa “holen”, kukunin mo ang libro, sa “zeigen”, itataas mo ito.'),
           [G2], R('öffnen'), audio='Öffnen Sie bitte das Buch.'),
    choice(X, 'grammatikWortschatz', L('Anna sagt über sich: Sie lernt Deutsch. Wählen Sie das richtige Verb.', 'Anna says about herself: she learns German. Choose the correct verb.', 'Sinasabi ni Anna ang tungkol sa sarili: nag-aaral siya ng German. Piliin ang tamang verb.'),
           'Anna: „Ich … Deutsch.“', 'lerne', ['lernen', 'lernt'],
           L('Richtig: „Ich lerne Deutsch.“ Bei „ich“ endet das Verb auf -e. „lernen“ passt zu wir/Sie, „lernt“ zu er/sie/ihr.',
             'Correct: “Ich lerne Deutsch.” With “ich” the verb ends in -e. “lernen” goes with wir/Sie, “lernt” with er/sie/ihr.',
             'Tama: “Ich lerne Deutsch.” Sa “ich”, nagtatapos sa -e ang verb. Ang “lernen” ay para sa wir/Sie, ang “lernt” sa er/sie/ihr.'),
           [G2], R('lernen')),
    choice(X, 'lesen', L('Frau Huber gibt Ihnen ein Blatt. Lesen Sie.', 'Frau Huber puts a note on the desk. Read it.', 'Nag-iwan si Frau Huber ng papel sa mesa. Basahin.'),
           'Blatt von Frau Huber: „Holen Sie bitte ein Blatt Papier. Bringen Sie das Buch.“\n\nWas holen Sie?', 'ein Blatt Papier', ['das Buch', 'das Heft'],
           L('Richtig: ein Blatt Papier. „Holen Sie“ steht bei „ein Blatt Papier“. Das Buch bringen Sie (Sie haben es schon). Vom Heft steht nichts auf dem Zettel.',
             'Correct: ein Blatt Papier. “Holen Sie” goes with “ein Blatt Papier”. You bring the book (you already have it). The note says nothing about the exercise book.',
             'Tama: ein Blatt Papier. Ang “Holen Sie” ay para sa “ein Blatt Papier”. Dadalhin mo ang libro (mayroon ka na nito). Walang sinabi ang papel tungkol sa kuwaderno.'),
           [G2], R('holen', 'bringen')),
    choice(X, 'sprechen', L('Frau Huber sagt: „Warten Sie hier, bitte.“ Sie antworten höflich. Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'Frau Huber says: “Warten Sie hier, bitte.” You answer politely. What do you say? Choose, then say it aloud.', 'Sabi ni Frau Huber: “Warten Sie hier, bitte.” Sumagot ka nang magalang. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'),
           None, 'Danke, ich warte hier.', ['Danke, ich wartet hier.', 'Danke, ich warten hier.'],
           L('Richtig: „ich warte“. Bei „ich“ endet das Verb auf -e. „wartet“ ist für er/sie/ihr, „warten“ für wir/Sie.',
             'Correct: “ich warte”. With “ich” the verb ends in -e. “wartet” is for er/sie/ihr, “warten” for wir/Sie.',
             'Tama: “ich warte”. Sa “ich”, nagtatapos sa -e ang verb. Ang “wartet” ay para sa er/sie/ihr, ang “warten” ay para sa wir/Sie.'),
           [G2], R('warten')),
], intro=INTRO(
    L('Frau Huber sagt oft: „Öffnen Sie das Buch.“ „Hören Sie zu.“ „Holen Sie ein Blatt Papier.“ Anna und Jose lernen diese Verben.',
      'Frau Huber often says: “Öffnen Sie das Buch.” “Hören Sie zu.” “Holen Sie ein Blatt Papier.” Anna and Jose learn these verbs.',
      'Madalas sabihin ni Frau Huber: “Öffnen Sie das Buch.” “Hören Sie zu.” “Holen Sie ein Blatt Papier.” Pinag-aaralan nina Anna at Jose ang mga verb na ito.'),
    L('Anweisungen im Kurs verstehen und die Verbformen sagen: ich lerne, er wartet, du öffnest',
      'understand instructions in class and say the verb forms: ich lerne, er wartet, du öffnest',
      'maintindihan ang instructions sa kurso at sabihin ang mga anyo ng verb: ich lerne, er wartet, du öffnest')))

# L09 ------------------------------------------------------------------
lesson(9, L('Hausübung und Pause', 'Homework and break', 'Takdang-aralin at pahinga'), ['Hausübung', 'Hausaufgabe', 'Pause'], [
    PHRASE('die Hausübung', 'Die Hausübung machen Sie zu Hause, nicht im Unterricht. Frau Huber sagt: „Die Hausübung ist Seite 20.“',
           'You do the Hausübung (homework) at home, not in class. Frau Huber says: “Die Hausübung ist Seite 20.”', 'Ginagawa mo ang Hausübung (takdang-aralin) sa bahay, hindi sa klase. Sabi ni Frau Huber: “Die Hausübung ist Seite 20.”'),
    CULTURE('Hausübung (in Deutschland: Hausaufgabe)', 'In Österreich sagt man „die Hausübung“. In Deutschland sagt man „die Hausaufgabe“. Beide Wörter sind „die“-Wörter.',
            'In Austria people say “die Hausübung”. In Germany they say “die Hausaufgabe”. Both words take “die”.', 'Sa Austria, “die Hausübung” ang sinasabi. Sa Germany, “die Hausaufgabe”. Parehong “die” ang dalawang salita.'),
    RULE('die Übung → die Hausübung', 'Bei langen Wörtern gilt der Artikel vom letzten Teil: Haus + die Übung = die Hausübung.',
         'In long words the article comes from the last part: Haus + die Übung = die Hausübung.', 'Sa mahahabang salita, ang article ay mula sa huling bahagi: Haus + die Übung = die Hausübung.',
         ['Die Hausübung ist Seite 20.', 'Ich mache die Hausübung.']),
    PHRASE('die Pause', 'In der Pause machen alle Pause. Dann lernen Sie nicht. Nach der Pause ist wieder Unterricht.',
           'In the break (Pause) everybody takes a break. You do not study. After the break class starts again.', 'Sa Pause, nagpapahinga ang lahat. Hindi ka nag-aaral. Pagkatapos ng Pause, may klase ulit.'),
    PHRASE('Wann ist Pause? – Um 10:30 Uhr.', 'Ein Kurs hat einen Plan mit Zeiten wie 9:00 oder 10:30. Mit „Wann?“ fragen Sie nach der Zeit. Die Antwort: „Um 10:30 Uhr.“',
           'A course has a plan with times like 9:00 or 10:30. With “Wann?” you ask for the time. The answer: “Um 10:30 Uhr.” (at 10:30)', 'May plano ang kurso na may oras tulad ng 9:00 o 10:30. Sa “Wann?” itinatanong ang oras. Ang sagot: “Um 10:30 Uhr.” (ng 10:30)'),
], [
    choice(X, 'lesen', L('Anna liest den Plan im Kursraum. Schauen Sie das Bild an.', 'Anna reads the plan in the classroom. Look at the picture.', 'Binabasa ni Anna ang plano sa silid-aralan. Tingnan ang larawan.'),
           'Was ist die Hausübung?', 'Seite 20', ['Seite 12', 'Aufgabe 3'],
           L('Richtig: Seite 20. Im Plan steht: „Hausübung: Seite 20“. Seite 12 und Aufgabe 3 stehen nicht im Plan.',
             'Correct: Seite 20. The plan says: “Hausübung: Seite 20”. Seite 12 and Aufgabe 3 are not in the plan.',
             'Tama: Seite 20. Sabi sa plano: “Hausübung: Seite 20”. Wala sa plano ang Seite 12 at Aufgabe 3.'),
           [G5], R('Hausübung', 'Seite'), img=PLAN()),
    choice(X, 'lesen', L('Anna liest den Plan im Kursraum. Schauen Sie das Bild an.', 'Anna reads the plan in the classroom. Look at the picture.', 'Binabasa ni Anna ang plano sa silid-aralan. Tingnan ang larawan.'),
           'Wann ist Pause?', 'um 10:30 Uhr', ['um 9:00 Uhr', 'um 12:00 Uhr'],
           L('Richtig: um 10:30 Uhr. Im Plan steht: „Pause: 10:30“. 9:00 steht neben „Unterricht“, 12:00 neben „Ende“.',
             'Correct: um 10:30 Uhr. The plan says: “Pause: 10:30”. 9:00 is next to “Unterricht”, 12:00 next to “Ende”.',
             'Tama: um 10:30 Uhr. Sabi sa plano: “Pause: 10:30”. Ang 9:00 ay katabi ng “Unterricht”, ang 12:00 ay katabi ng “Ende”.'),
           [G5], R('Pause'), img=PLAN()),
    choice(X, 'lesen', L('Anna liest den Plan im Kursraum. Schauen Sie das Bild an.', 'Anna reads the plan in the classroom. Look at the picture.', 'Binabasa ni Anna ang plano sa silid-aralan. Tingnan ang larawan.'),
           'Neben „Unterricht“ steht …', '9:00', ['10:30', '12:00'],
           L('Richtig: 9:00. Im Plan steht: „Unterricht: 9:00“. 10:30 ist bei „Pause“, 12:00 bei „Ende“.',
             'Correct: 9:00. The plan says: “Unterricht: 9:00”. 10:30 is at “Pause”, 12:00 at “Ende”.',
             'Tama: 9:00. Sabi sa plano: “Unterricht: 9:00”. Ang 10:30 ay sa “Pause”, ang 12:00 sa “Ende”.'),
           [G5], R('Unterricht'), img=PLAN()),
    choice(X, 'grammatikWortschatz', L('Anna sagt zu Frau Huber, was sie macht. Wählen Sie den richtigen Artikel.', 'Anna tells Frau Huber what she does. Choose the correct article.', 'Sinasabi ni Anna kay Frau Huber ang ginagawa niya. Piliin ang tamang article.'),
           'Anna: „Ich mache … Hausübung.“', 'die', ['der', 'das'],
           L('Richtig: die Hausübung. Das Wort endet mit „Übung“, und „die Übung“ ist ein „die“-Wort. Darum auch „die Hausübung“.',
             'Correct: die Hausübung. The word ends in “Übung”, and “die Übung” is a “die”-word. So “die Hausübung” too.',
             'Tama: die Hausübung. Nagtatapos ang salita sa “Übung”, at ang “die Übung” ay salitang “die”. Kaya “die Hausübung” din.'),
           [G1], R('Hausübung')),
    cloze(X, 'grammatikWortschatz', L('Frau Huber sagt Anna, was sie machen soll. Ergänzen Sie das Wort mit den Wörtern unten.', 'Frau Huber tells Anna what to do. Complete the word with the words below.', 'Sinasabi ni Frau Huber kay Anna ang gagawin. Kumpletuhin ang salita gamit ang mga salita sa ibaba.'),
          'Frau Huber: „Die {{1}} ist Seite 20.“ – Anna: „Danke, Frau Huber.“', [['Hausübung']],
          L('Richtig: „die Hausübung“. In Österreich sagt man „Hausübung“ für die Aufgabe nach dem Kurs. Eine „Pause“ hat keine Seite, und eine „Prüfung“ ist nicht „Seite 20“.',
            'Correct: “die Hausübung”. In Austria people say “Hausübung” for the work after the course. A “Pause” has no page, and a “Prüfung” is not “Seite 20”.',
            'Tama: “die Hausübung”. Sa Austria, “Hausübung” ang sinasabi para sa gawain pagkatapos ng kurso. Ang “Pause” ay walang pahina, at ang “Prüfung” ay hindi “Seite 20”.'),
          [G1], R('Hausübung'), bank=['Hausübung', 'Pause', 'Prüfung']),
    choice(X, 'hoeren', L('Frau Huber sagt am Ende vom Unterricht etwas. Hören Sie.', 'Frau Huber says something at the end of class. Listen.', 'May sinabi si Frau Huber sa dulo ng klase. Makinig.'),
           'Was ist die Hausübung?', 'Seite 20', ['Seite 12', 'Seite 22'],
           L('Sie hören: „Die Hausübung ist Seite zwanzig. Danke und auf Wiedersehen!“ zwanzig = 20. zwölf (12) und zweiundzwanzig (22) hören Sie nicht.',
             'You hear: “Die Hausübung ist Seite zwanzig. Danke und auf Wiedersehen!” zwanzig = 20. You do not hear zwölf (12) or zweiundzwanzig (22).',
             'Naririnig mo: “Die Hausübung ist Seite zwanzig. Danke und auf Wiedersehen!” zwanzig = 20. Hindi mo naririnig ang zwölf (12) o zweiundzwanzig (22).'),
           [G5], R('Hausübung', 'Seite'), audio='Frau Huber: Die Hausübung ist Seite zwanzig. Danke und auf Wiedersehen!'),
    choice(X, 'lesen', RFR,
           'Tom schreibt: „Die Hausübung ist Seite 20. Ich habe das Heft hier. Ich mache die Aufgabe in der Pause.“\n\nAussage: Tom macht die Aufgabe in der Pause.', 'richtig', ['falsch'],
           L('Richtig. Im Text steht: „Ich mache die Aufgabe in der Pause.“ Die Aussage sagt dasselbe.',
             'Right. The text says: “Ich mache die Aufgabe in der Pause.” The statement says the same.',
             'Tama. Sabi sa teksto: “Ich mache die Aufgabe in der Pause.” Pareho ang sinasabi ng pahayag.'),
           [G5], R('Pause', 'Hausübung')),
], intro=INTRO(
    L('Im Kursraum ist ein Plan. Anna liest: Unterricht, Pause, Hausübung. Sie fragt: Was ist die Hausübung?',
      'There is a plan in the classroom. Anna reads: Unterricht, Pause, Hausübung. She wants to know: what is the homework?',
      'May plano sa silid-aralan. Binasa ni Anna: Unterricht, Pause, Hausübung. Gusto niyang malaman: ano ang takdang-aralin?'),
    L('einen Kursplan lesen und Unterricht, Pause und Hausübung darin finden',
      'read a course plan and find class, break and homework in it',
      'basahin ang plano ng kurso at hanapin ang klase, pahinga at takdang-aralin')))

# L10 ------------------------------------------------------------------
lesson(10, L('Was bedeutet das?', 'What does that mean?', 'Ano ang ibig sabihin niyan?'), ['bedeuten'], [
    PHRASE('Was bedeutet „Thema“?', 'So fragen Sie nach der Bedeutung. Frau Huber erklärt das Wort. Sie fragen mit „Was bedeutet …?“',
           'This is how you ask for the meaning. Frau Huber explains the word. You ask with “Was bedeutet …?”', 'Ganito magtanong ng kahulugan. Ipapaliwanag ni Frau Huber ang salita. Magtatanong ka ng “Was bedeutet …?”'),
    RULE('Was bedeutet …? · Wie sagt man …? · Wie schreibt man …?', 'Mit „Was bedeutet …?“ fragen Sie nach der Bedeutung. Mit „Wie sagt man …?“ fragen Sie nach dem deutschen Wort. Mit „Wie schreibt man …?“ fragen Sie nach den Buchstaben.',
         'With “Was bedeutet …?” you ask for the meaning. With “Wie sagt man …?” you ask for the German word. With “Wie schreibt man …?” you ask for the letters.',
         'Sa “Was bedeutet …?” itinatanong ang kahulugan. Sa “Wie sagt man …?” itinatanong ang salitang German. Sa “Wie schreibt man …?” itinatanong ang mga titik.',
         ['Was bedeutet „Heft“?', 'Wie sagt man „book“ auf Deutsch?', 'Wie schreibt man „Kugelschreiber“?']),
    PHRASE('Wie sagt man „book“ auf Deutsch? – Das Buch.', 'Sie kennen das Wort auf Englisch oder Tagalog, aber nicht auf Deutsch? Dann fragen Sie so. Die Antwort: „Das Buch.“',
           'You know the word in English or Tagalog but not in German? Then ask like this. The answer: “Das Buch.”', 'Alam mo ang salita sa English o Tagalog pero hindi sa German? Ganito ang tanong. Ang sagot: “Das Buch.”'),
    PHRASE('Wiederholen Sie bitte. – Langsam, bitte.', 'Frau Huber spricht schnell? Dann bitten Sie: „Wiederholen Sie bitte.“ oder „Langsam, bitte.“',
           'Frau Huber speaks fast? Then ask: “Wiederholen Sie bitte.” (please repeat) or “Langsam, bitte.” (slowly, please)', 'Mabilis magsalita si Frau Huber? Sabihin: “Wiederholen Sie bitte.” (pakiulit) o “Langsam, bitte.” (dahan-dahan, please)'),
], [
    choice(X, 'lesen', L('Ali hat eine Frage an Frau Huber. Schauen Sie das Bild an.', 'Ali has a question for Frau Huber. Look at the picture.', 'May tanong si Ali kay Frau Huber. Tingnan ang larawan.'),
           'Was möchte Ali wissen?', 'was „Thema“ bedeutet', ['wie man „Thema“ schreibt', 'wo Frau Huber wohnt'],
           L('Richtig: was „Thema“ bedeutet. In der Sprechblase steht: „Was bedeutet „Thema“?“ Nach der Schreibweise würde Ali mit „Wie schreibt man …?“ fragen.',
             'Correct: was “Thema” bedeutet. The speech bubble says: “Was bedeutet “Thema”?” For the spelling Ali would ask “Wie schreibt man …?”',
             'Tama: was “Thema” bedeutet. Nakasulat sa bubble: “Was bedeutet “Thema”?” Para sa baybay, magtatanong si Ali ng “Wie schreibt man …?”'),
           [G3], R('bedeuten', 'Thema'), img=FRAGE),
    choice(X, 'sprechen', L('Sie verstehen das Wort „Heft“ nicht. Sie fragen Frau Huber. Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'You do not understand the word “Heft”. You ask Frau Huber. What do you say? Choose, then say it aloud.', 'Hindi mo naiintindihan ang salitang “Heft”. Tinanong mo si Frau Huber. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'),
           None, 'Was bedeutet „Heft“?', ['Wie schreibt man „Heft“?', 'Wo ist „Heft“?'],
           L('Richtig: „Was bedeutet „Heft“?“ Sie wollen die Bedeutung wissen. „Wie schreibt man …?“ fragt nach den Buchstaben, „Wo ist …?“ fragt nach dem Ort.',
             'Correct: “Was bedeutet “Heft”?” You want to know the meaning. “Wie schreibt man …?” asks for the letters, “Wo ist …?” asks for the place.',
             'Tama: “Was bedeutet “Heft”?” Gusto mong malaman ang kahulugan. Ang “Wie schreibt man …?” ay tungkol sa mga titik, ang “Wo ist …?” ay tungkol sa lugar.'),
           [G3], R('bedeuten')),
    choice(X, 'sprechen', L('Sie wissen das deutsche Wort für „pen“ nicht. Sie fragen Anna. Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'You do not know the German word for “pen”. You ask Anna. What do you say? Choose, then say it aloud.', 'Hindi mo alam ang salitang German para sa “pen”. Tinanong mo si Anna. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'),
           None, 'Wie sagt man „pen“ auf Deutsch?', ['Wie schreibt man „pen“?', 'Wo ist „pen“?'],
           L('Richtig: „Wie sagt man „pen“ auf Deutsch?“ Sie suchen das deutsche Wort. „Wie schreibt man …?“ fragt nach den Buchstaben von einem Wort, das Sie schon kennen.',
             'Correct: “Wie sagt man “pen” auf Deutsch?” You are looking for the German word. “Wie schreibt man …?” asks for the letters of a word you already know.',
             'Tama: “Wie sagt man “pen” auf Deutsch?” Hinahanap mo ang salitang German. Ang “Wie schreibt man …?” ay tungkol sa mga titik ng salitang alam mo na.'),
           [G3], R('sagen', 'Deutsch')),
    choice(X, 'hoeren', L('Anna fragt Frau Huber etwas. Hören Sie.', 'Anna asks Frau Huber something. Listen.', 'May tinanong si Anna kay Frau Huber. Makinig.'),
           'Was fragt Anna?', 'Was „Aufgabe“ bedeutet.', ['Wie man „Aufgabe“ schreibt.', 'Wo die Aufgabe ist.'],
           L('Sie hören: „Frau Huber, was bedeutet „Aufgabe“?“ Anna fragt nach der Bedeutung. Von Buchstaben und vom Ort sagt sie nichts.',
             'You hear: “Frau Huber, was bedeutet “Aufgabe”?” Anna asks for the meaning. She says nothing about letters or place.',
             'Naririnig mo: “Frau Huber, was bedeutet “Aufgabe”?” Kahulugan ang tinatanong ni Anna. Walang sinabi tungkol sa titik o lugar.'),
           [G3], R('bedeuten', 'Aufgabe'), audio='Anna: Frau Huber, was bedeutet „Aufgabe“?'),
    cloze(X, 'grammatikWortschatz', L('Ali und Anna fragen im Kurs. Ergänzen Sie die Fragen mit den Wörtern unten.', 'Ali and Anna ask questions in class. Complete the questions with the words below.', 'Nagtatanong sina Ali at Anna sa kurso. Kumpletuhin ang mga tanong gamit ang mga salita sa ibaba.'),
          'Ali: „Entschuldigung, was {{1}} „Pause“?“ – Anna: „Wie {{2}} man „book“ auf Deutsch?“', [['bedeutet'], ['sagt']],
          L('Richtig: „Was bedeutet …?“ und „Wie sagt man …?“ Zu „was“ passt „bedeutet“ (er/sie/es), zu „man“ passt „sagt“. „bedeuten“ und „sagen“ sind die Formen für wir/Sie.',
            'Correct: “Was bedeutet …?” and “Wie sagt man …?” “was” goes with “bedeutet” (er/sie/es), “man” goes with “sagt”. “bedeuten” and “sagen” are the forms for wir/Sie.',
            'Tama: “Was bedeutet …?” at “Wie sagt man …?” Ang “was” ay sinasamahan ng “bedeutet” (er/sie/es), ang “man” ng “sagt”. Ang “bedeuten” at “sagen” ay mga anyo para sa wir/Sie.'),
          [G3], R('bedeuten', 'sagen'), bank=['bedeutet', 'sagt', 'bedeuten', 'sagen']),
    choice(X, 'lesen', L('Tom und Maria sprechen im Kurs. Lesen Sie.', 'Tom and Maria talk in class. Read it.', 'Nag-uusap sina Tom at Maria sa kurso. Basahin.'),
           'Tom: Entschuldigung, wie schreibt man „Kugelschreiber“?\nMaria: K-U-G-E-L-S-C-H-R-E-I-B-E-R.\n\nWas fragt Tom?', 'wie man „Kugelschreiber“ schreibt', ['was „Kugelschreiber“ bedeutet', 'wo der Kugelschreiber ist'],
           L('Richtig: wie man „Kugelschreiber“ schreibt. Tom fragt „Wie schreibt man …?“ und Maria sagt die Buchstaben. Nach der Bedeutung fragt man mit „Was bedeutet …?“.',
             'Correct: how “Kugelschreiber” is written. Tom asks “Wie schreibt man …?” and Maria says the letters. For the meaning you ask “Was bedeutet …?”.',
             'Tama: kung paano isulat ang “Kugelschreiber”. Nagtanong si Tom ng “Wie schreibt man …?” at sinabi ni Maria ang mga titik. Para sa kahulugan, “Was bedeutet …?” ang tanong.'),
           [G3], R('schreiben', 'Kugelschreiber', 'Buchstabe')),
    choice(X, 'sprechen', L('Frau Huber spricht sehr schnell. Sie verstehen nichts. Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'Frau Huber speaks very fast. You understand nothing. What do you say? Choose, then say it aloud.', 'Napakabilis magsalita ni Frau Huber. Wala kang maintindihan. Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'),
           None, 'Langsam, bitte. Wiederholen Sie bitte.', ['Danke, auf Wiedersehen.', 'Ich habe keine Hausübung.'],
           L('Richtig: „Langsam, bitte. Wiederholen Sie bitte.“ So bitten Sie um langsames Sprechen und um Wiederholung. „Auf Wiedersehen“ sagt man beim Gehen, „keine Hausübung“ passt nicht zur Situation.',
             'Correct: “Langsam, bitte. Wiederholen Sie bitte.” This is how you ask for slower speech and a repeat. “Auf Wiedersehen” is said when leaving, “keine Hausübung” does not fit the situation.',
             'Tama: “Langsam, bitte. Wiederholen Sie bitte.” Ganito humiling ng mas mabagal na pagsasalita at pag-ulit. Ang “Auf Wiedersehen” ay sinasabi kapag aalis, ang “keine Hausübung” ay hindi angkop sa sitwasyon.'),
           [G3], R('wiederholen', 'langsam')),
], intro=INTRO(
    L('Ali versteht ein Wort nicht. Er hebt die Hand und fragt Frau Huber: „Was bedeutet „Thema“?“',
      'Ali does not understand a word. He raises his hand and asks Frau Huber: “Was bedeutet “Thema”?”',
      'Hindi naiintindihan ni Ali ang isang salita. Itinaas niya ang kamay at tinanong si Frau Huber: “Was bedeutet “Thema”?”'),
    L('im Kurs nachfragen: „Was bedeutet …?“, „Wie sagt man … auf Deutsch?“ und „Wiederholen Sie bitte.“',
      'ask in class: “Was bedeutet …?”, “Wie sagt man … auf Deutsch?” and “Wiederholen Sie bitte.”',
      'magtanong sa kurso: “Was bedeutet …?”, “Wie sagt man … auf Deutsch?” at “Wiederholen Sie bitte.”')))

# L11 ------------------------------------------------------------------
WOW = L('In Österreich sind Frauen und Männer gleichberechtigt. Frauen und Männer können alle Berufe lernen.',
        'In Austria women and men have equal rights. Women and men can learn all professions.',
        'Sa Austria, pantay ang karapatan ng babae at lalaki. Puwedeng mag-aral ng lahat ng propesyon ang babae at lalaki.')
lesson(11, L('Lernen für alle', 'Learning for everyone', 'Pag-aaral para sa lahat'), [], [
    PHRASE('Frauen und Männer lernen zusammen.', 'Im Deutschkurs sitzen Frauen und Männer zusammen. Eine Frau und ein Mann können beide Deutsch lernen.',
           'In the German course women and men sit together. A woman and a man can both learn German.', 'Sa Deutschkurs, magkasamang nakaupo ang mga babae at lalaki. Parehong puwedeng mag-aral ng German ang babae at lalaki.'),
    RULE('die Frau – die Frauen · der Mann – die Männer', 'Die Mehrzahl (Plural) von „Frau“ ist „Frauen“, von „Mann“ ist „Männer“. Beide Wörter haben bei der Mehrzahl „die“.',
         'The plural of “Frau” is “Frauen”, of “Mann” it is “Männer”. Both take “die” in the plural.', 'Ang plural ng “Frau” ay “Frauen”, ng “Mann” ay “Männer”. Parehong “die” sa plural.',
         ['Im Kurs sind Frauen und Männer.', 'Die Männer und die Frauen lernen Deutsch.']),
    PHRASE('der Beruf – die Berufe', 'Lehrerin ist ein Beruf. Lehrer ist auch ein Beruf. Ein Beruf ist die Arbeit, die man gelernt hat.',
           'Lehrerin is a profession (Beruf). Lehrer is a profession too. A Beruf is the work you have learned.', 'Ang Lehrerin ay isang Beruf (propesyon). Ang Lehrer ay Beruf din. Ang Beruf ay trabahong pinag-aralan mo.'),
    PHRASE('Deutsch lernen hilft.', 'Mit Deutsch verstehen Sie die Leute in Österreich. Sie verstehen auch Briefe und E-Mails.',
           'With German you understand the people in Austria. You also understand letters and e-mails.', 'Sa German, maiintindihan mo ang mga tao sa Austria. Maiintindihan mo rin ang mga sulat (Briefe) at e-mail.'),
    CULTURE('Frauen und Männer in Österreich', 'In Österreich sind Frauen und Männer gleichberechtigt. Frauen und Männer können alle Berufe lernen. Eine Frau kann Lehrerin sein, ein Mann kann Lehrer sein – und alle anderen Berufe auch.',
            'In Austria women and men have equal rights. Women and men can learn all professions. A woman can be a teacher, a man can be a teacher – and every other profession too.',
            'Sa Austria, pantay ang karapatan ng babae at lalaki. Puwedeng matutunan ng babae at lalaki ang lahat ng propesyon. Puwedeng guro ang babae at guro rin ang lalaki – at lahat ng ibang propesyon din.'),
], [
    choice(X, 'werte', L('Zwei Bilder zeigen zwei Menschen bei der Arbeit. Schauen Sie das Bild an.', 'Two pictures show two people at work. Look at the picture.', 'Dalawang larawan ang nagpapakita ng dalawang taong nagtatrabaho. Tingnan ang larawan.'),
           'Bild 1: Wer ist das?', 'eine Frau', ['ein Mann', 'ein Kind'],
           L('Richtig: eine Frau. In Bild 1 steht eine Frau mit langen Haaren bei einem Auto. Sie repariert das Auto – das ist ihr Beruf.', 'Correct: eine Frau. In picture 1 a woman with long hair stands at a car. She repairs the car – that is her job.',
             'Tama: eine Frau. Sa Bild 1, may babaeng mahaba ang buhok sa tabi ng kotse. Inaayos niya ang kotse – iyon ang trabaho niya.'),
           [G6], R('Frau'), img=BERUFE()),
    choice(X, 'werte', L('Zwei Bilder zeigen zwei Menschen bei der Arbeit. Schauen Sie das Bild an.', 'Two pictures show two people at work. Look at the picture.', 'Dalawang larawan ang nagpapakita ng dalawang taong nagtatrabaho. Tingnan ang larawan.'),
           'Bild 2: Wer ist das?', 'ein Mann', ['eine Frau', 'ein Kind'],
           L('Richtig: ein Mann. In Bild 2 steht ein Mann im Krankenhaus mit einem roten Kreuz auf der Kleidung. Er arbeitet als Krankenpfleger – auch das ist ein Beruf für Männer.',
             'Correct: ein Mann. In picture 2 a man stands in a hospital with a red cross on his clothes. He works as a nurse – that is also a job for men.',
             'Tama: ein Mann. Sa Bild 2, may lalaking nasa ospital na may pulang krus sa damit. Nars siya – trabaho rin ito para sa lalaki.'),
           [G6], R('Mann'), img=BERUFE()),
    choice(X, 'werte', L('Zwei Bilder zeigen zwei Menschen bei der Arbeit. Schauen Sie das Bild an.', 'Two pictures show two people at work. Look at the picture.', 'Dalawang larawan ang nagpapakita ng dalawang taong nagtatrabaho. Tingnan ang larawan.'),
           'Was zeigen Bild 1 und Bild 2 zusammen?', 'Frauen und Männer können alle Berufe lernen.', ['Berufe sind nur für Männer.', 'Berufe sind nur für Frauen.'],
           WOW, [G6], R('Frau', 'Mann'), img=BERUFE()),
    choice(X, 'werte', L('Anna und Tom sind im Deutschkurs. Frau Huber fragt: „Wer lernt in Österreich Deutsch?“ Was ist richtig?', 'Anna and Tom are in the German course. Frau Huber asks: “Who learns German in Austria?” What is correct?', 'Nasa Deutschkurs sina Anna at Tom. Tanong ni Frau Huber: “Wer lernt in Österreich Deutsch?” Ano ang tama?'),
           None, 'Frauen und Männer lernen zusammen Deutsch.', ['Nur Männer lernen Deutsch.', 'Nur Frauen lernen Deutsch.'],
           L('Richtig: Frauen und Männer lernen zusammen Deutsch. In Österreich sind Frauen und Männer gleichberechtigt – das gilt auch im Kurs. „Nur Männer“ oder „nur Frauen“ stimmt nicht.',
             'Correct: women and men learn German together. In Austria women and men have equal rights – this is true in the course too. “Only men” or “only women” is not true.',
             'Tama: sabay na nag-aaral ng German ang babae at lalaki. Sa Austria, pantay ang karapatan ng babae at lalaki – totoo rin ito sa kurso. Hindi totoo ang “nur Männer” o “nur Frauen”.'),
           [G6], R('Frau', 'Mann', 'Deutsch')),
    cloze(X, 'werte', L('Im Kurs: Frau Huber beschreibt die Leute. Ergänzen Sie mit den Wörtern unten.', 'In the course: Frau Huber describes the people. Complete with the words below.', 'Sa kurso: inilalarawan ni Frau Huber ang mga tao. Kumpletuhin gamit ang mga salita sa ibaba.'),
          'Im Kurs sind eine {{1}} und ein {{2}}. Beide lernen Deutsch.', [['Frau'], ['Mann']],
          L('Richtig: eine Frau und ein Mann. „Frau“ ist ein „die“-Wort (eine Frau), „Mann“ ist ein „der“-Wort (ein Mann). „Kind“ ist ein „das“-Wort: Es heißt „ein Kind“, nicht „eine Kind“. Außerdem ist ein Kind keine Frau und kein Mann.',
            'Correct: eine Frau and ein Mann. “Frau” is a “die”-word (eine Frau), “Mann” is a “der”-word (ein Mann). “Kind” is a “das”-word: “ein Kind”, not “eine Kind”. Also a child is neither a woman nor a man.',
            'Tama: eine Frau at ein Mann. Ang “Frau” ay salitang “die” (eine Frau), ang “Mann” ay “der” (ein Mann). Ang “Kind” ay salitang “das”: “ein Kind”, hindi “eine Kind”. At ang bata ay hindi babae o lalaki.'),
          [G6], R('Frau', 'Mann'), bank=['Frau', 'Mann', 'Kind']),
    choice(X, 'hoeren', L('Frau Huber sagt im Kurs etwas über Lehrer. Hören Sie.', 'Frau Huber says something about teachers in class. Listen.', 'May sinabi si Frau Huber tungkol sa mga guro sa kurso. Makinig.'),
           'Was ist richtig?', 'Es gibt Lehrerinnen und Lehrer.', ['Nur Männer sind Lehrer.', 'Nur Frauen sind Lehrerinnen und Lehrer.'],
           L('Sie hören: „Ich bin Lehrerin. Herr Bauer ist auch Lehrer. In Österreich gibt es Lehrerinnen und Lehrer.“ Beide Berufe gibt es für Frauen und für Männer.',
             'You hear: “Ich bin Lehrerin. Herr Bauer ist auch Lehrer. In Österreich gibt es Lehrerinnen und Lehrer.” Teaching is a job for women and for men.',
             'Naririnig mo: “Ich bin Lehrerin. Herr Bauer ist auch Lehrer. In Österreich gibt es Lehrerinnen und Lehrer.” Trabaho ito para sa babae at para sa lalaki.'),
           [G6], R('Lehrer, Lehrerin', 'Frau', 'Mann'), audio='Frau Huber: Ich bin Lehrerin. Herr Bauer ist auch Lehrer. In Österreich gibt es Lehrerinnen und Lehrer.'),
    choice(X, 'werte', L('Anna lebt in Wien. Sie lernt im Kurs Deutsch. Was ist richtig?', 'Anna lives in Vienna. She learns German in the course. What is correct?', 'Nakatira si Anna sa Vienna. Nag-aaral siya ng German sa kurso. Ano ang tama?'),
           'Mit Deutsch versteht Anna …', 'die Leute in Wien', ['nur die Lehrerin', 'nur das Buch'],
           L('Richtig: die Leute in Wien. In Österreich sprechen die Leute Deutsch. Wer Deutsch lernt, versteht die Leute – nicht nur die Lehrerin oder das Buch.',
             'Correct: die Leute in Wien. In Austria people speak German. Anyone who learns German understands the people – not only the teacher or the book.',
             'Tama: die Leute in Wien. Sa Austria, German ang sinasalita ng mga tao. Ang nag-aaral ng German ay nakakaintindi sa mga tao – hindi lang sa guro o sa libro.'),
           [G6], R('Leute', 'Deutsch', 'lernen')),
], intro=INTRO(
    L('Im Deutschkurs in Wien sitzen Frauen und Männer zusammen. Anna und Tom lernen beide Deutsch. Frau Huber ist die Lehrerin, Herr Bauer ist auch Lehrer.',
      'In the German course in Vienna women and men sit together. Anna and Tom both learn German. Frau Huber is a teacher, Herr Bauer is a teacher too.',
      'Sa Deutschkurs sa Vienna, magkasamang nakaupo ang mga babae at lalaki. Parehong nag-aaral ng German sina Anna at Tom. Si Frau Huber ay guro, si Herr Bauer ay guro rin.'),
    L('sagen, dass Frauen und Männer in Österreich gleiche Rechte haben und alle Berufe lernen können',
      'say that women and men in Austria have equal rights and can learn all professions',
      'sabihin na pantay ang karapatan ng babae at lalaki sa Austria at puwede silang mag-aral ng lahat ng propesyon')))
for _i in LESSONS[-1]['items']:
    _i.setdefault('sourceIds', SOURCES)  # Q36: every item of the Werte lesson carries its source (Q11)
check_lessons()

# ---------------------------------------------------------------- pools (focus Lesen: A1-LES-T2 richtig/falsch, Aushänge, Anweisungen)
RFQ = lambda v, i: choice(i, 'lesen', L('Lesen Sie. Ist die Aussage richtig oder falsch?', 'Read. Is the statement right or wrong?', 'Basahin. Tama o mali ang pahayag?'), f'{v[0]}\n\nAussage: {v[1]}', v[2], [x for x in RF if x != v[2]], same(v[3]), [G5], R('richtig', 'falsch'))
MAIL1 = 'Liebe Leute!\nMorgen ist kein Unterricht. Die Lehrerin ist krank. Die Hausübung: Seite 30, Aufgabe 2.\nViele Grüße, Anna Huber'
MAIL2 = 'Hallo Maria!\nIch komme heute nicht in den Deutschkurs. Ich habe einen Test in der Arbeit. Bitte bring mir morgen die Hausübung.\nDanke! Tom'
MAIL3 = 'Liebe Leute!\nDie Prüfung ist am 12. Mai um 9 Uhr. Bringen Sie bitte einen Kugelschreiber. Schreiben Sie nicht mit Bleistift.\nIhr Lehrer, Herr Bauer'
fam('LE1', RFQ, [(MAIL1, 'Morgen ist Unterricht.', 'falsch', 'Im Text: „Morgen ist kein Unterricht.“'), (MAIL2, 'Tom kommt heute nicht in den Kurs.', 'richtig', '„Ich komme heute nicht in den Deutschkurs.“'), (MAIL3, 'In der Prüfung schreibt man mit Bleistift.', 'falsch', '„Schreiben Sie nicht mit Bleistift.“')],
    [(MAIL1, 'Die Hausübung ist auf Seite 30.', 'richtig', '„Seite 30, Aufgabe 2“.'), (MAIL2, 'Tom hat heute einen Test in der Arbeit.', 'richtig', '„Ich habe einen Test in der Arbeit.“'), (MAIL3, 'Die Prüfung beginnt um 9 Uhr.', 'richtig', '„um 9 Uhr“.'),
     (MAIL1, 'Die Lehrerin ist krank.', 'richtig', '„Die Lehrerin ist krank.“'), (MAIL2, 'Maria gibt Tom die Prüfung.', 'falsch', 'Tom möchte die Hausübung, nicht die Prüfung.'), (MAIL3, 'Für die Prüfung bringt man einen Kugelschreiber.', 'richtig', '„Bringen Sie bitte einen Kugelschreiber.“')])

SIGN = lambda v, i: choice(i, 'lesen', READ, f'Im Kursraum steht:\n„{v[0]}“\n\n{v[1]}', v[2], v[3], same(v[4]), [G5], R('Kurs'))
fam('LE2', SIGN, [('Deutschkurs A1: 9:00–12:00. Pause: 10:30.', 'Wann ist Pause?', 'um 10:30', ['um 9:00', 'um 12:00'], 'Pause: 10:30.'), ('Heute kein Kurs! Der Kurs ist morgen.', 'Ist heute Kurs?', 'Nein.', ['Ja.', 'Ja, um 9 Uhr.'], '„Heute kein Kurs!“'), ('Bitte keine Zigaretten im Haus!', 'Zigaretten im Haus – ja oder nein?', 'Nein.', ['Ja.', 'Ja, in der Pause.'], '„keine Zigaretten im Haus“.')],
    [('Prüfung A1: Bitte einen Kugelschreiber bringen.', 'Was bringt man zur Prüfung?', 'einen Kugelschreiber', ['ein Heft', 'einen Bleistift'], 'einen Kugelschreiber.'),
     ('Die Bücher bleiben hier. Die Hefte nehmen Sie mit.', 'Was nehmen Sie mit?', 'das Heft', ['das Buch', 'nichts'], '„Die Hefte nehmen Sie mit.“'), ('Kurs A1: Frau Huber · Kurs A2: Herr Bauer', 'Wer ist der Lehrer im Kurs A2?', 'Herr Bauer', ['Frau Huber', 'Herr Huber'], 'Kurs A2: Herr Bauer.'),
     ('Neu im Kurs? Bitte die Lehrerin fragen.', 'Was machen neue Leute im Kurs?', 'Sie fragen die Lehrerin.', ['Sie warten allein.', 'Sie machen Pause.'], '„Bitte die Lehrerin fragen.“')])

INSTR = lambda v, i: choice(i, 'lesen', READ, f'Anweisung: „{v[0]}“\nWas machen Sie?', v[1], v[2], L(v[3], v[4], v[5]), [G2], R(v[6]))
fam('LE3', INSTR, [('Kreuzen Sie die richtige Antwort an.', 'Ich mache ein Kreuz bei der richtigen Antwort.', ['Ich schreibe einen Text.', 'Ich lese den Text.'], 'ankreuzen = ein Kreuz machen.', 'ankreuzen = make a cross.', 'ankreuzen = lagyan ng ekis.', 'ankreuzen'),
                   ('Ergänzen Sie die Sätze.', 'Ich schreibe die fehlenden Wörter in die Sätze.', ['Ich mache ein Kreuz.', 'Ich lese laut.'], 'ergänzen = Lücken füllen.', 'ergänzen = fill the gaps.', 'ergänzen = punan ang patlang.', 'ergänzen'),
                   ('Ordnen Sie die Wörter zu.', 'Ich mache Paare: 1 – b, 2 – a.', ['Ich schreibe einen Text.', 'Ich mache ein Kreuz.'], 'zuordnen = verbinden.', 'zuordnen = match.', 'zuordnen = itugma.', 'zuordnen')],
    [('Markieren Sie die Verben im Text.', 'Ich mache die Verben farbig.', ['Ich schreibe neue Verben.', 'Ich lese die Verben nicht.'], 'markieren = farbig machen.', 'markieren = highlight.', 'markieren = kulayan.', 'markieren'),
     ('Hören Sie zu und kreuzen Sie an.', 'Ich höre und mache dann ein Kreuz.', ['Ich lese und schreibe.', 'Ich spreche laut.'], 'zuhören + ankreuzen.', 'listen + tick.', 'makinig + markahan.', 'zuhören'),
     ('Lesen Sie den Text. Antworten Sie auf die Fragen.', 'Ich lese und schreibe Antworten.', ['Ich höre und warte.', 'Ich mache Pause.'], 'lesen + Antworten schreiben.', 'read + write answers.', 'magbasa + sumulat ng sagot.', 'lesen'),
     ('Üben Sie mit einem Partner.', 'Ich übe mit einer Person zusammen.', ['Ich übe allein.', 'Ich mache Pause.'], 'mit einem Partner = zu zweit.', 'with a partner = in pairs.', 'kasama ang partner = dalawahan.', 'üben')])

fam('LE4', lambda v, i: choice(i, 'lesen', LOOK, v[0], v[1], v[2], same(v[3]), [G5, G1], R('Kurs'), img=v[4]()),
    [('Wann endet der Unterricht?', 'um 12:00 Uhr', ['um 10:30 Uhr', 'um 9:00 Uhr'], 'Im Plan: „Ende: 12:00“.', PLAN), ('Nummer 2 ist …', 'das Heft', ['das Buch', 'der Bleistift'], '2 = das Heft.', SACHEN), ('Wie viele Fragen sind richtig?', 'zwei', ['drei', 'eine'], 'Frage 1 und 3: ✓ – zwei richtig.', TEST_P)],
    [('Wann beginnt der Unterricht?', 'um 9:00 Uhr', ['um 10:30 Uhr', 'um 12:00 Uhr'], 'Unterricht: 9:00.', PLAN), ('Nummer 4 ist …', 'der Bleistift', ['der Kugelschreiber', 'das Buch'], '4 = der Bleistift.', SACHEN),
     ('Ist Frage 1 richtig?', 'Ja.', ['Nein.'], 'Bei Frage 1 ist ein ✓.', TEST_P), ('Wie heißt der Kurs im Plan?', 'Deutschkurs A1', ['Prüfung A2', 'Hausübung'], 'Im Plan: Deutschkurs A1.', PLAN)])

fam('LE5', RFQ, [('Ich heiße Jose. Ich lerne seit zwei Jahren Deutsch. Mein Kurs ist am Abend. Die Lehrerin erklärt sehr gut.', 'Jose lernt am Morgen Deutsch.', 'falsch', 'Der Kurs ist am Abend.'),
                 ('Im Deutschkurs sind zwölf Leute. Sie sprechen viele Sprachen. Im Kurs sprechen alle Deutsch.', 'Im Kurs sind zwölf Personen.', 'richtig', '„Im Deutschkurs sind zwölf Leute.“'),
                 ('Heute schreiben wir einen Test. Ich habe kein Heft, aber Maria gibt mir ein Blatt.', 'Die Person hat ein Blatt von Maria.', 'richtig', '„Maria gibt mir ein Blatt.“')],
    [('Die Hausübung ist nicht schwer. Ich mache sie in der Pause.', 'Die Hausübung ist schwer.', 'falsch', '„nicht schwer“.'), ('Sofia lernt zwanzig neue Wörter.', 'Sofia lernt neue Wörter.', 'richtig', '„zwanzig neue Wörter“.'),
     ('Der Kurs hat heute keine Pause.', 'Heute ist eine Pause.', 'falsch', '„keine Pause“.'), ('Tom hat einen Fehler im Test. Die Lehrerin erklärt die Lösung.', 'Die Lehrerin erklärt die Lösung.', 'richtig', '„Die Lehrerin erklärt die Lösung.“')])

fam('HO1', lambda v, i: choice(i, 'hoeren', L('Hören Sie. Was sollen Sie machen?', 'Listen. What should you do?', 'Makinig. Ano ang dapat mong gawin?'), None, v[1], [v[2]], same(f'Sie hören: „{v[0]}“'), [G2], R('Seite'), audio=v[0]),
    [('Öffnen Sie das Buch auf Seite vierundzwanzig.', 'Seite 24', 'Seite 42'), ('Machen Sie bitte Aufgabe sieben.', 'Aufgabe 7', 'Aufgabe 17'), ('Schreiben Sie die Wörter ins Heft.', 'ins Heft schreiben', 'ins Buch schreiben')],
    [('Lesen Sie den Text auf Seite dreizehn.', 'Seite 13', 'Seite 30'), ('Kreuzen Sie die richtige Antwort an.', 'ankreuzen', 'ergänzen'), ('Hören Sie gut zu.', 'zuhören', 'schreiben'), ('Holen Sie bitte ein Blatt Papier.', 'Papier holen', 'Papier bringen')])

KR = {'bed': ('Was bedeutet „Pause“?', 'Pause bedeutet: nicht lernen.'), 'wo': ('Wo ist Kursraum drei?', 'Dort, bitte.'), 'haus': ('Haben Sie die Hausübung?', 'Ja, hier ist sie.'), 'stift': ('Hast du einen Kugelschreiber für mich?', 'Ja, hier, bitte.'),
      'seite': ('Auf welcher Seite sind wir?', 'Auf Seite zwölf.'), 'verst': ('Verstehen Sie die Aufgabe?', 'Nein, bitte erklären Sie das noch einmal.'), 'herein': ('Klopf, klopf!', 'Herein!')}
fam('HO2', lambda v, i: choice(i, 'hoeren', L('Hören Sie. Welche Antwort passt?', 'Listen. Which answer fits?', 'Makinig. Aling sagot ang angkop?'), None, KR[v[0]][1], [KR[k][1] for k in v[1]], same(f'„{KR[v[0]][0]}“ – „{KR[v[0]][1]}“'), [G3], R('Kurs'), audio=KR[v[0]][0]),
    [('bed', ['wo', 'haus', 'seite']), ('haus', ['bed', 'wo', 'stift']), ('seite', ['haus', 'bed', 'herein'])], [('wo', ['seite', 'haus', 'verst']), ('stift', ['wo', 'seite', 'bed']), ('verst', ['wo', 'stift', 'seite']), ('herein', ['bed', 'seite', 'stift'])])

fam('HO3', lambda v, i: choice(i, 'hoeren', L('Hören Sie. Ist die Aussage richtig oder falsch?', 'Listen. Is the statement right or wrong?', 'Makinig. Tama o mali ang pahayag?'), f'Aussage: {v[1]}', v[2], [x for x in RF if x != v[2]], same(f'Sie hören: „{v[0]}“'), [G5], R('richtig', 'falsch'), audio=v[0]),
    [('Liebe Kursteilnehmer, heute ist der Unterricht schon um elf Uhr zu Ende.', 'Der Unterricht endet heute um elf.', 'richtig'), ('Die Prüfung ist nicht heute, sie ist morgen.', 'Die Prüfung ist heute.', 'falsch'), ('Bitte bringen Sie morgen Ihr Buch und Ihr Heft mit.', 'Morgen braucht man kein Heft.', 'falsch')],
    [('Die Pause ist heute kurz.', 'Die Pause ist heute nicht kurz.', 'falsch'), ('Herr Bauer ist krank. Frau Huber macht heute den Unterricht.', 'Herr Bauer unterrichtet heute.', 'falsch'), ('Der Test ist nicht schwer. Es gibt nur zehn Fragen.', 'Der Test hat zehn Fragen.', 'richtig'), ('Heute sind wir nicht in Kursraum zwei. Wir sind in Kursraum vier.', 'Der Kurs ist heute in Kursraum zwei.', 'falsch')])

ANS = lambda v, i: cloze(i, 'schreiben', L('Ergänzen Sie.', 'Complete.', 'Kumpletuhin.'), v[0], v[1], same(v[2]), [G2, G1], R('ergänzen'))
fam('SC1', ANS, [('Im {{1}} lese ich, ins {{2}} schreibe ich.', [['Buch'], ['Heft']], 'Im Buch lese ich, ins Heft schreibe ich.'), ('Auf eine {{1}} gibt man eine {{2}}.', [['Frage'], ['Antwort']], 'Auf eine Frage gibt man eine Antwort.'), ('Die richtige Antwort ist die {{1}}. Eine falsche Antwort ist ein {{2}}.', [['Lösung'], ['Fehler']], 'Lösung – Fehler.')],
    [('Ein {{1}} hat viele Wörter.', [['Satz', 'Text']], 'Ein Satz/Text hat viele Wörter.'), ('Ich schreibe mit dem {{1}}.', [['Kugelschreiber', 'Bleistift', 'Stift', 'Kuli']], 'mit dem Kugelschreiber / Bleistift / Stift.'), ('Um 10:30 ist {{1}}.', [['Pause']], 'Um 10:30 ist Pause.'), ('Die Aufgabe für morgen ist die {{1}}.', [['Hausübung']], 'die Hausübung.')])

def langs(a):
    # Every order and separator of two languages counts (review G-017: "Englisch, Tagalog", "Tagalog Englisch" …).
    if ' und ' not in a:
        return [a]
    x, y = a.split(' und ')
    return [f'{p}{sep}{q}' for p, q in ((x, y), (y, x)) for sep in (' und ', ', ', ' ')]


REG = lambda v, i: cloze(i, 'schreiben', L('Lesen Sie. Ergänzen Sie das Anmeldeformular.', 'Read. Complete the registration form.', 'Basahin. Kumpletuhin ang registration form.'), f'{v[0]}\nKurs: {{{{1}}}} · Sprachen: {{{{2}}}}', [[v[1]], langs(v[2][0])], same(f'Kurs: {v[1]}, Sprachen: {v[2][0]}.'), [G1], R('Kurs'))
fam('SC2', REG, [('Ich bin Maria. Ich möchte den Kurs A1. Ich spreche Tagalog und Englisch.', 'A1', ['Tagalog und Englisch', 'Tagalog, Englisch', 'Englisch und Tagalog']), ('Ich heiße Ali. Ich mache den Kurs A2. Ich spreche Deutsch und Englisch.', 'A2', ['Deutsch und Englisch', 'Deutsch, Englisch', 'Englisch und Deutsch']), ('Mein Name ist Sofia. Kurs: A1. Ich spreche nur Englisch.', 'A1', ['Englisch'])],
    [('Ich bin Jose. Ich bin im Kurs A1. Ich spreche Tagalog.', 'A1', ['Tagalog']), ('Ich heiße Tom. Ich möchte den Kurs A2. Ich spreche Deutsch.', 'A2', ['Deutsch']), ('Ich bin Anna, Kurs A1, ich spreche Englisch und Tagalog.', 'A1', ['Englisch und Tagalog', 'Englisch, Tagalog', 'Tagalog und Englisch']), ('Ich heiße Lukas. Kurs: A2. Sprachen: Deutsch und Englisch.', 'A2', ['Deutsch und Englisch', 'Deutsch, Englisch', 'Englisch und Deutsch'])])

NOTE = lambda v, i: cloze(i, 'schreiben', L('Ergänzen Sie die Nachricht an die Lehrerin.', 'Complete the message to the teacher.', 'Kumpletuhin ang mensahe sa guro.'), f'Liebe Frau Huber,\nich komme heute {{{{1}}}} in den Kurs. Ich bin {v[0]}. Ich mache die {{{{2}}}} morgen.\nViele Grüße, {v[1]}',
                          [['nicht'], ['Hausübung']], same('nicht (Verb verneinen), die Hausübung.'), [G4], R('nicht', 'kein', 'Hausübung'))
fam('SC3', NOTE, [('krank', 'Maria'), ('in der Arbeit', 'Jose'), ('in Graz', 'Sofia')], [('krank', 'Tom'), ('bei meiner Tochter', 'Anna'), ('in Linz', 'Ali'), ('bei meiner Oma', 'Lukas')])

META = {'bed': ('Sie kennen das Wort „Blatt“ nicht.', 'You don’t know the word “Blatt”.', 'Hindi mo alam ang salitang “Blatt”.', 'Was bedeutet „Blatt“?'),
        'sagen': ('Sie wissen das deutsche Wort für „question“ nicht.', 'You don’t know the German word for “question”.', 'Hindi mo alam ang salitang German para sa “question”.', 'Wie sagt man „question“ auf Deutsch?'),
        'schreib': ('Sie wissen nicht, wie man „Kugelschreiber“ schreibt.', 'You don’t know how to write “Kugelschreiber”.', 'Hindi mo alam isulat ang “Kugelschreiber”.', 'Wie schreibt man „Kugelschreiber“?'),
        'erkl': ('Sie verstehen die Aufgabe nicht.', 'You don’t understand the task.', 'Hindi mo naintindihan ang gawain.', 'Können Sie die Aufgabe bitte erklären?'),
        'nochmal': ('Die Lehrerin spricht zu schnell.', 'The teacher speaks too fast.', 'Masyadong mabilis ang guro.', 'Langsam, bitte. Noch einmal, bitte.'),
        'seite': ('Sie wissen die Seite nicht.', 'You don’t know the page.', 'Hindi mo alam ang pahina.', 'Auf welcher Seite sind wir?')}
fam('SP1', lambda v, i: choice(i, 'sprechen', L(META[v[0]][0] + ' Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', META[v[0]][1] + ' What do you say? Choose, then say it aloud.', META[v[0]][2] + ' Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'), None, META[v[0]][3], [META[k][3] for k in v[1]],
    same(f'Passend: „{META[v[0]][3]}“'), [G3], R('bedeuten')),
    [('bed', ['sagen', 'seite']), ('sagen', ['bed', 'schreib']), ('erkl', ['seite', 'sagen'])], [('schreib', ['bed', 'seite']), ('nochmal', ['schreib', 'bed']), ('seite', ['schreib', 'nochmal']), ('bed', ['nochmal', 'schreib'])])

TEACH = lambda v, i: choice(i, 'sprechen', L(f'{v[0]} Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', f'{v[1]} What do you say? Choose, then say it aloud.', f'{v[2]} Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.'), v[3], v[4], v[5], same(f'Passend: „{v[4]}“'), [G4], R('nicht', 'kein'))
fam('SP2', TEACH, [('Sie haben die Hausübung nicht.', 'You don’t have the homework.', 'Wala sa iyo ang takdang-aralin.', 'Haben Sie die Hausübung?', 'Nein, die habe ich nicht.', ['Ja, die habe ich nicht.', 'Nein, ich bin Hausübung.']),
                   ('Sie haben kein Buch dabei.', 'You don’t have a book with you.', 'Wala kang dalang libro.', 'Wo ist Ihr Buch?', 'Ich habe heute kein Buch.', ['Ich habe heute nicht Buch.', 'Mein Buch ist kein.']),
                   ('Sie verstehen die Frage nicht.', 'You don’t understand the question.', 'Hindi mo naintindihan ang tanong.', 'Verstehen Sie die Frage?', 'Nein, ich verstehe sie nicht.', ['Nein, ich verstehe kein.', 'Doch, ich verstehe sie nicht.'])],
    [('Sie haben keinen Stift.', 'You have no pen.', 'Wala kang panulat.', 'Schreiben Sie bitte.', 'Entschuldigung, ich habe keinen Stift.', ['Entschuldigung, ich habe nicht Stift.', 'Ich schreibe kein.']), ('Sie verstehen das Beispiel nicht.', 'You don’t understand the example.', 'Hindi mo naintindihan ang halimbawa.', 'Verstehen Sie das Beispiel?', 'Nein, das verstehe ich nicht.', ['Nein, das verstehe ich kein.', 'Ja, nicht.']),
     ('Sie haben keine Frage.', 'You have no question.', 'Wala kang tanong.', 'Haben Sie eine Frage?', 'Nein, ich habe keine Frage.', ['Nein, ich habe nicht Frage.', 'Ja, keine Frage.']), ('Sie kommen morgen nicht.', 'You are not coming tomorrow.', 'Hindi ka darating bukas.', 'Kommen Sie morgen?', 'Nein, morgen komme ich nicht.', ['Nein, morgen komme ich kein.', 'Ja, morgen komme ich nicht.'])])

NEG = lambda v, i: choice(i, 'sprechen', L(f'Verneinen Sie: „{v[0]}“ Wählen Sie, dann sagen Sie es laut.', f'Make it negative: “{v[0]}” Choose, then say it aloud.', f'Gawing negatibo: “{v[0]}” Pumili, tapos sabihin nang malakas.'), None, v[1], v[2], same(v[3]), [G4], R('nicht', 'kein'))
fam('SP3', NEG, [('Ich habe ein Heft.', 'Ich habe kein Heft.', ['Ich habe nicht ein Heft.', 'Ich nicht habe Heft.'], 'ein Heft → kein Heft.'), ('Ich komme heute.', 'Ich komme heute nicht.', ['Ich komme kein heute.', 'Ich nicht komme heute.'], 'Verb → nicht (am Ende).'), ('Das ist richtig.', 'Das ist nicht richtig.', ['Das ist kein richtig.', 'Das nicht ist richtig.'], 'Adjektiv → nicht.')],
    [('Ich habe eine Frage.', 'Ich habe keine Frage.', ['Ich habe nicht eine Frage.', 'Ich habe kein Frage.'], 'eine Frage → keine Frage.'), ('Wir lernen heute.', 'Wir lernen heute nicht.', ['Wir lernen kein heute.', 'Wir nicht lernen heute.'], 'Verb → nicht.'),
     ('Das ist ein Fehler.', 'Das ist kein Fehler.', ['Das ist nicht ein Fehler.', 'Das nicht ist Fehler.'], 'ein Fehler → kein Fehler.'), ('Der Test ist schwer.', 'Der Test ist nicht schwer.', ['Der Test ist kein schwer.', 'Der Test nicht ist schwer.'], 'Adjektiv → nicht.')])

NK = lambda v, i: choice(i, 'grammatikWortschatz', CHOOSE, v[0], v[1], [x for x in ('nicht', 'kein', 'keine') if x != v[1]], L(v[2], v[2], v[2]) if False else same(v[2]), [G4], R('nicht', 'kein'))
fam('GW1', NK, [('Ich verstehe das …', 'nicht', 'Verb → nicht.'), ('Das ist … Buch.', 'kein', 'ein Buch → kein Buch.'), ('Ich habe … Frage.', 'keine', 'eine Frage → keine Frage.')],
    [('Er kommt heute …', 'nicht', 'Verb → nicht.'), ('Wir haben … Pause.', 'keine', 'die Pause → keine Pause.'), ('Das ist … richtig.', 'nicht', 'Adjektiv → nicht.'), ('Das ist … Heft.', 'kein', 'das Heft → kein Heft.')])

SB = lambda v, i: choice(i, 'grammatikWortschatz', L('Lesen Sie die Nachricht. Was passt in die Lücke?', 'Read the message. What fits the gap?', 'Basahin ang mensahe. Ano ang angkop sa patlang?'), v[0], v[1], [v[2]], same(v[3]), [G4, G1], R('Kurs'))
fam('GW2', SB, [('Hallo Anna! Ich komme heute ___ in den Kurs. Bis morgen! Tom', 'nicht', 'kein', 'Verb verneinen → nicht.'), ('Liebe Kursteilnehmer, morgen ist ___ Unterricht. Frau Huber', 'kein', 'nicht', 'Unterricht (Nomen ohne Artikel) → kein.'), ('Liebe Frau Huber, ich verstehe das Beispiel ___. Ali', 'nicht', 'kein', 'Verb verneinen → nicht.')],
    [('Liebe Maria, ich habe ___ Buch. Bringst du deins? Jose', 'kein', 'nicht', 'ein Buch → kein Buch.'), ('Hallo Herr Bauer, ich ___ die Aufgabe nicht. Sofia', 'verstehe', 'verstehen', 'ich verstehe.'), ('Hallo! Die Hausübung ist ___ Seite 20. Lukas', 'auf', 'in', 'auf Seite 20.'), ('Liebe Leute, heute haben wir ___ Pause. Ihre Lehrerin', 'keine', 'nicht', 'die Pause → keine Pause.')])

PLK = lambda v, i: choice(i, 'grammatikWortschatz', CHOOSE, v[0], v[1], v[2], same(f'Plural: die {v[1]}.'), [G1], R(v[3]))
fam('GW3', PLK, [('das Buch → die …', 'Bücher', ['Buchs', 'Buchen'], 'Buch'), ('das Heft → die …', 'Hefte', ['Hefts', 'Heften'], 'Heft'), ('die Frage → die …', 'Fragen', ['Frages', 'Frage'], 'Frage')],
    [('das Wort → die …', 'Wörter', ['Worts', 'Worte'], 'Wort'), ('der Satz → die …', 'Sätze', ['Satzen', 'Satzs'], 'Satz'), ('die Aufgabe → die …', 'Aufgaben', ['Aufgabes', 'Aufgabe'], 'Aufgabe'), ('der Fehler → die …', 'Fehler', ['Fehlers', 'Fehlern'], 'Fehler')])

VB = lambda v, i: cloze(i, 'grammatikWortschatz', GAPS, v[0], [v[1]], same(v[2]), [G2], R(v[3]))
fam('GW4', VB, [('Die Lehrerin {{1}} (zeigen) das Bild.', ['zeigt'], 'sie zeigt.', 'zeigen'), ('Du {{1}} (öffnen) das Buch.', ['öffnest'], 'du öffnest (mit -est).', 'öffnen'), ('Wir {{1}} (üben) zusammen.', ['üben'], 'wir üben.', 'üben')],
    [('Er {{1}} (warten) auf die Lehrerin.', ['wartet'], 'er wartet (mit -et).', 'warten'), ('Ich {{1}} (lernen) Deutsch.', ['lerne'], 'ich lerne.', 'lernen'), ('Sie {{1}} (bringen) das Buch.', ['bringt', 'bringen'], 'sie bringt / Sie bringen.', 'bringen'), ('Was {{1}} (bedeuten) das?', ['bedeutet'], 'das bedeutet.', 'bedeuten')])

WQ = lambda v, i: choice(i, 'werte', CHOOSE, v[0], v[1], [v[2]], WOW, [G6], R('lernen'))
fam('WE1', WQ, [('Kann eine Frau in Österreich alle Berufe lernen?', 'Ja.', 'Nein.'), ('Kann ein Mann in Österreich alle Berufe lernen?', 'Ja.', 'Nein.'), ('Welche Berufe können Frauen in Österreich lernen?', 'alle Berufe', 'nur wenige Berufe')],
    [('Gibt es in Österreich Berufe nur für Männer?', 'Nein.', 'Ja.'), ('Gibt es in Österreich Berufe nur für Frauen?', 'Nein.', 'Ja.')])
fam('WE2', WQ, [('Wo hilft Deutsch?', 'bei der Arbeit, beim Amt und im Alltag', 'nur im Deutschkurs'), ('Was hilft bei der Integrationsprüfung?', 'Deutsch lernen und üben', 'nichts machen'), ('Ist Deutsch lernen in Österreich wichtig?', 'Ja, sehr.', 'Nein.')],
    [('Mit Deutsch versteht man …', 'Briefe vom Amt und die Lehrerin vom Kind', 'nichts'), ('Wer lernt in Österreich Deutsch?', 'Frauen und Männer', 'nur Männer')])
fam('WE3', lambda v, i: choice(i, 'werte', LOOK, v[0], v[1], [v[2]], WOW, [G6], R('Mann', 'Frau'), img=BERUFE()),
    [('Bild 1: Ist das eine Frau oder ein Mann?', 'eine Frau', 'ein Mann'), ('Bild 2: Ist das eine Frau oder ein Mann?', 'ein Mann', 'eine Frau'), ('Was zeigen Bild 1 und Bild 2 zusammen?', 'Frauen und Männer können alle Berufe lernen.', 'Berufe sind nur für Frauen.')],
    [('Bild 1: Ist das ein Beruf nur für Männer?', 'Nein, auch für Frauen.', 'Ja.'), ('Bild 2: Ist das ein Beruf nur für Frauen?', 'Nein, auch für Männer.', 'Ja.')])
fam('WE4', WQ, [], [('Ist ein Beruf nur für Männer?', 'Nein.', 'Ja.'), ('Ist ein Beruf nur für Frauen?', 'Nein.', 'Ja.'), ('Kann eine Frau Lehrerin werden?', 'Ja.', 'Nein.'), ('Kann ein Mann Lehrer werden?', 'Ja.', 'Nein.'), ('Lernen Frauen und Männer Berufe?', 'Ja, alle Berufe.', 'Nein, nur Männer.'), ('Lernen Frauen und Männer im Deutschkurs zusammen?', 'Ja.', 'Nein.')])

write_svgs('/tmp/a1-05.png')
write_all(V, GOALS, {'lesen': 5, 'hoeren': 3, 'schreiben': 3, 'sprechen': 3, 'grammatikWortschatz': 3, 'werte': 3})
