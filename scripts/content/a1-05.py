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
PICS['kursraum'] = ('<rect x="40" y="20" width="230" height="110" rx="6" fill="#2f5d50" stroke="#7a4e2d" stroke-width="6"/>' + label(155, 70, 'Willkommen!', 26, '#fff') + label(155, 104, 'Deutschkurs A1', 16, '#e5e7eb', bold=False)
                    + person(330, '#c8102e', 'a', '#7a4e2d', long=True) + label(330, 244, 'Lehrerin', 13, '#fff')
                    + person(90, '#1d4e89', 'b', '#222', y=40, s=0.55) + person(200, '#2a9d8f', 'c', '#222', y=40, s=0.55, long=True) + '<rect x="40" y="236" width="230" height="24" fill="#a8743f"/>')
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
PICS['seite'] = ('<rect x="70" y="16" width="260" height="228" rx="4" fill="#fff" stroke="#9ca3af" stroke-width="2"/>' + label(200, 46, 'Aufgabe 3', 20, '#c8102e')
                 + ''.join(f'<path d="M95 {y}h{w}" stroke="#9ca3af" stroke-width="6" stroke-linecap="round"/>' for y, w in ((80, 210), (100, 190), (120, 200), (140, 150), (170, 210), (190, 170)))
                 + label(200, 232, 'Seite 12', 16, '#1f2937'))
PICS['anweisungen'] = (panel(10, 20, 88, 220, 1) + panel(108, 20, 88, 220, 2) + panel(206, 20, 88, 220, 3) + panel(304, 20, 88, 220, 4)
                       + '<rect x="38" y="110" width="30" height="30" fill="#fff" stroke="#1f2937" stroke-width="3"/><path d="M42 114l22 22M64 114l-22 22" stroke="#c8102e" stroke-width="4"/>'
                       + label(152, 135, 'Ich ___', 16, bold=False) + '<path d="M150 150h36" stroke="#c8102e" stroke-width="3"/>'
                       + ''.join(f'<circle cx="{x}" cy="{y}" r="6" fill="#1d4e89"/>' for x, y in ((225, 100), (225, 140), (275, 100), (275, 140))) + '<path d="M225 100L275 140M225 140L275 100" stroke="#1d4e89" stroke-width="3"/>'
                       + '<rect x="318" y="118" width="60" height="22" fill="#ffd23f" opacity=".8"/>' + label(348, 135, 'Wort', 16))
PICS['test'] = ('<rect x="60" y="16" width="280" height="228" rx="6" fill="#fff" stroke="#9ca3af" stroke-width="2"/>' + label(200, 46, 'Test', 22)
                + ''.join(label(90, y, f'Frage {n}', 18, anchor='start', bold=False) + label(300, y, m, 26, c) for n, y, m, c in ((1, 100, '✓', '#2a9d8f'), (2, 150, '✗', '#c8102e'), (3, 200, '✓', '#2a9d8f'))))
PICS['sessel'] = ('<rect y="200" width="400" height="60" fill="#d9c3a3"/>'
                  + ''.join(f'<rect x="{x}" y="150" width="70" height="12" fill="#7a4e2d"/><rect x="{x+6}" y="162" width="6" height="40" fill="#7a4e2d"/><rect x="{x+58}" y="162" width="6" height="40" fill="#7a4e2d"/>' for x in (30, 165, 300))
                  + person(65, '#1d4e89', 'b', '#222', y=-20, s=0.55) + person(200, '#2a9d8f', 'a', '#7a4e2d', y=-20, s=0.55, long=True)
                  + label(65, 230, 'Jose', 14) + label(200, 230, 'Anna', 14) + label(335, 230, 'Ali', 14) + label(335, 130, '?', 36, '#f77f00'))
PICS['tische'] = ('<rect x="10" y="160" width="180" height="20" fill="#a8743f"/><rect x="210" y="160" width="180" height="20" fill="#a8743f"/>'
                  + BOOK(28, 92, 58, 66) + HEFT(112, 104, 46, 56) + HEFT(276, 104, 46, 56)
                  + label(100, 210, 'Maria', 18) + label(300, 210, 'Tom', 18))
PICS['verben'] = (panel(10, 20, 88, 220, 1) + panel(108, 20, 88, 220, 2) + panel(206, 20, 88, 220, 3) + panel(304, 20, 88, 220, 4)
                  + '<path d="M24 110l30 8 30-8v52l-30 8-30-8z" fill="#fff" stroke="#1d4e89" stroke-width="3"/><path d="M54 118v52" stroke="#1d4e89" stroke-width="2"/>'
                  + '<rect x="118" y="80" width="68" height="44" fill="#2f5d50"/><path d="M130 170l26-30" stroke="#f1c9a5" stroke-width="10" stroke-linecap="round"/>'
                  + '<circle cx="250" cy="120" r="26" fill="#fff" stroke="#1f2937" stroke-width="3"/><path d="M250 120v-16M250 120l12 6" stroke="#1f2937" stroke-width="3"/>'
                  + '<path d="M332 104q24-10 30 20t-14 36q-8-4-4-12" stroke="#1f2937" stroke-width="4" fill="#f1c9a5"/>')
PICS['plan'] = ('<rect x="50" y="16" width="300" height="228" rx="8" fill="#fff" stroke="#1d4e89" stroke-width="3"/>' + label(200, 46, 'Deutschkurs A1', 20, '#1d4e89')
                + label(80, 90, 'Unterricht: 9:00', 17, anchor='start', bold=False) + label(80, 125, 'Pause: 10:30', 17, anchor='start', bold=False)
                + label(80, 160, 'Ende: 12:00', 17, anchor='start', bold=False) + label(80, 205, 'Hausübung: Seite 20', 17, anchor='start'))
PICS['frage'] = (person(110, '#1d4e89', 'b', '#222') + '<path d="M150 150l20-70" stroke="#c68a5c" stroke-width="14" stroke-linecap="round"/>' + label(110, 244, 'Ali', 13, '#fff')
                 + bubble(170, 30, 210, 'Was bedeutet „Thema“?', 15, tail_x=200) + person(330, '#c8102e', 'a', '#7a4e2d', y=0, s=0.75, long=True))
PICS['berufe'] = (panel(10, 20, 185, 220, 1) + panel(205, 20, 185, 220, 2)
                  + person(80, '#1d4e89', 'a', '#7a4e2d', y=-30, s=0.7, long=True) + '<path d="M120 150l40-30m-6-10 16 4-4 16" stroke="#6b7280" stroke-width="8" stroke-linecap="round" fill="none"/>'
                  + '<rect x="120" y="190" width="60" height="30" rx="6" fill="#c8102e"/><circle cx="133" cy="222" r="7" fill="#222"/><circle cx="167" cy="222" r="7" fill="#222"/>'
                  + person(270, '#9ed8ff', 'b', '#222', y=-30, s=0.7) + '<rect x="262" y="180" width="16" height="16" fill="#c8102e"/><rect x="267" y="175" width="6" height="26" fill="#c8102e"/><rect x="257" y="185" width="26" height="6" fill="#c8102e"/>'
                  + '<rect x="320" y="150" width="56" height="70" rx="4" fill="#e0ebf8"/>' + label(348, 192, '+', 30, '#c8102e'))

SACHEN = lambda: img('sachen', 'Ein Tisch mit vier Dingen mit Nummern: Buch, Heft, Kugelschreiber, Bleistift.', 'A desk with four numbered things: book, exercise book, ballpoint pen, pencil.', 'Mesa na may apat na bagay na may numero: libro, kuwaderno, ballpen, lapis.')
PLAN = lambda: img('plan', 'Ein Plan für den Deutschkurs mit Uhrzeiten und der Hausübung.', 'A plan for the German course with times and the homework.', 'Plano ng kursong German na may oras at takdang-aralin.')
TEST_P = lambda: img('test', 'Ein Test mit drei Fragen. Bei zwei Fragen ist ein Häkchen, bei einer ein Kreuz.', 'A test with three questions: two have a tick, one has a cross.', 'Test na may tatlong tanong: dalawa may tsek, isa may ekis.')
BERUFE = lambda: img('berufe', 'Bild 1: eine Frau repariert ein Auto. Bild 2: ein Mann arbeitet als Krankenpfleger.', 'Picture 1: a woman repairs a car. Picture 2: a man works as a nurse.', 'Larawan 1: babaeng nag-aayos ng kotse. Larawan 2: lalaking nars.')

# ---------------------------------------------------------------- lessons (11, A1-05 spec)
X = ''
lesson(1, L('Willkommen im Deutschkurs!', 'Welcome to the German course!', 'Maligayang pagdating sa kursong German!'), ['Kurs', 'Deutschkurs', 'Lehrer, Lehrerin', 'willkommen', 'Tafel', 'Unterricht', 'herein'], [
    C('Willkommen im Deutschkurs!', 'So begrüßt die Lehrerin die Leute im Kurs.', 'This is how the teacher welcomes people in the course.', 'Ganito bumabati ang guro sa klase.'),
    C('der Lehrer – die Lehrerin', 'Mann: Lehrer, Frau: Lehrerin.', 'Man: Lehrer, woman: Lehrerin.', 'Lalaki: Lehrer, babae: Lehrerin.'),
    C('Herein!', 'Jemand klopft an die Tür: „Herein!“', 'Someone knocks at the door: “Herein!” (come in)', 'May kumakatok: “Herein!” (pasok)'),
    C('der Kursraum – die Kursteilnehmer', 'Im Kursraum sind die Kursteilnehmer und die Lehrerin.', 'In the classroom (Kursraum) are the learners (Kursteilnehmer) and the teacher.', 'Nasa silid-aralan (Kursraum) ang mga estudyante (Kursteilnehmer) at ang guro.'),
    C('der Unterricht – die Tafel', 'Der Unterricht beginnt um 9 Uhr. Die Lehrerin schreibt an die Tafel.', 'Class (Unterricht) starts at 9. The teacher writes on the board (Tafel).', 'Nagsisimula ang klase (Unterricht) ng 9. Sumusulat ang guro sa pisara (Tafel).'),
], [
    choice(X, 'lesen', LOOK, 'Was steht an der Tafel?', 'Willkommen!', ['Herein!', 'Pause!'], same('An der Tafel steht „Willkommen!“.'), [G1], R('willkommen', 'Tafel'),
           img=img('kursraum', 'Ein Kursraum mit Tafel, einer Lehrerin und zwei Personen im Kurs.', 'A classroom with a board, a teacher and two learners.', 'Silid-aralan na may pisara, guro at dalawang estudyante.')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Eine Frau unterrichtet Deutsch. Sie ist …', 'Lehrerin', ['Lehrer', 'Kurs'], L('Frau → Lehrerin (mit -in).', 'Woman → Lehrerin (with -in).', 'Babae → Lehrerin (may -in).'), [G1], R('Lehrer, Lehrerin')),
    choice(X, 'hoeren', LISTEN, None, 'Der Unterricht beginnt um neun.', ['Der Unterricht beginnt um zehn.'], same('Sie hören: „Der Unterricht beginnt um neun Uhr.“'), [G1], R('Unterricht'), audio='Guten Morgen! Der Unterricht beginnt um neun Uhr.'),
])
lesson(2, L('Buch, Heft, Stift', 'Book, exercise book, pen', 'Libro, kuwaderno, panulat'), ['Buch', 'Heft', 'Kugelschreiber', 'Bleistift', 'Stift', 'Papier', 'Blatt'], [
    C('das Buch – das Heft', 'Im Buch lesen Sie, ins Heft schreiben Sie.', 'You read in the book (Buch) and write in the exercise book (Heft).', 'Nagbabasa sa libro (Buch), sumusulat sa kuwaderno (Heft).'),
    C('der Kugelschreiber – der Bleistift – der Stift', 'Kugelschreiber kurz: Kuli. Stift = Bleistift oder Kugelschreiber.', 'Kugelschreiber, short: Kuli. Stift = pencil or pen.', 'Kugelschreiber, maikli: Kuli. Stift = lapis o ballpen.'),
    C('das Papier – das Blatt', 'Ein Blatt Papier, bitte.', 'A sheet (Blatt) of paper, please.', 'Isang pirasong papel, please.'),
], [
    choice(X, 'grammatikWortschatz', LOOK, 'Nummer 3 ist …', 'der Kugelschreiber', ['der Bleistift', 'das Heft'], same('1 Buch, 2 Heft, 3 Kugelschreiber, 4 Bleistift.'), [G1], R('Kugelschreiber'), img=SACHEN()),
    choice(X, 'grammatikWortschatz', LOOK, 'Nummer 1 ist …', 'das Buch', ['das Heft', 'das Papier'], same('Nummer 1 ist das Buch.'), [G1], R('Buch'), img=SACHEN()),
    cloze(X, 'grammatikWortschatz', GAPS, '{{1}} Heft · {{2}} Bleistift · {{3}} Buch', [['das'], ['der'], ['das']], L('das Heft, der Bleistift, das Buch.', 'das Heft, der Bleistift, das Buch (articles).', 'das Heft, der Bleistift, das Buch (mga article).'), [G1], R('Heft', 'Bleistift', 'Buch')),
])
lesson(3, L('Wort, Satz, Text, Seite', 'Word, sentence, text, page', 'Salita, pangungusap, teksto, pahina'), ['Wort', 'Satz', 'Text', 'Seite', 'Aufgabe', 'Beispiel', 'Thema'], [
    C('das Wort – der Satz – der Text', 'Wörter bilden einen Satz. Sätze bilden einen Text.', 'Words make a sentence. Sentences make a text.', 'Ang mga salita ay bumubuo ng pangungusap. Ang mga pangungusap ay bumubuo ng teksto.'),
    C('Seite 12, Aufgabe 3', 'Öffnen Sie das Buch auf Seite 12. Machen Sie Aufgabe 3.', 'Open the book at page 12. Do exercise 3.', 'Buksan ang libro sa pahina 12. Gawin ang gawain 3.'),
    C('das Beispiel – das Thema', 'Zuerst kommt ein Beispiel. Das Thema heute: Familie.', 'First comes an example. Today’s topic: family.', 'Una ang halimbawa. Paksa ngayon: pamilya.'),
], [
    choice(X, 'lesen', LOOK, 'Auf welcher Seite ist Aufgabe 3?', 'auf Seite 12', ['auf Seite 3', 'auf Seite 21'], same('Unten steht: Seite 12.'), [G1], R('Seite', 'Aufgabe'),
           img=img('seite', 'Eine Buchseite mit „Aufgabe 3“ und einer Seitenzahl.', 'A book page with “Aufgabe 3” and a page number.', 'Pahina ng libro na may “Aufgabe 3” at numero ng pahina.')),
    choice(X, 'grammatikWortschatz', CHOOSE, '„Ich lerne Deutsch.“ ist …', 'ein Satz', ['ein Wort', 'eine Seite'], L('Mehrere Wörter mit Verb = ein Satz.', 'Several words with a verb = a sentence (Satz).', 'Ilang salita na may verb = pangungusap (Satz).'), [G1], R('Satz')),
    choice(X, 'hoeren', LISTEN, None, 'Seite 15', ['Seite 50'], same('Sie hören: „Öffnen Sie das Buch auf Seite fünfzehn.“'), [G2], R('Seite', 'öffnen'), audio='Öffnen Sie das Buch auf Seite fünfzehn.'),
])
lesson(4, L('Kreuzen Sie an! – Anweisungen', 'Tick! – instructions', 'Markahan! – mga instruction'), ['ankreuzen', 'ergänzen', 'zuordnen', 'markieren'], [
    C('Kreuzen Sie an.', 'ankreuzen = ein Kreuz (x) machen. „Kreuzen Sie die richtige Antwort an.“', 'ankreuzen = make a cross (x). “Tick the right answer.”', 'ankreuzen = lagyan ng ekis (x).'),
    C('Ergänzen Sie.', 'ergänzen = die Lücke füllen: „Ich ___ Anna.“ → heiße.', 'ergänzen = fill the gap.', 'ergänzen = punan ang patlang.'),
    C('Ordnen Sie zu.', 'zuordnen = Paare verbinden: 1 – b, 2 – a.', 'zuordnen = match pairs: 1 – b, 2 – a.', 'zuordnen = itugma: 1 – b, 2 – a.'),
    C('Markieren Sie.', 'markieren = ein Wort farbig machen.', 'markieren = highlight a word.', 'markieren = kulayan ang salita.'),
    C('Diese Wörter kommen in der Prüfung!', 'In der Integrationsprüfung stehen die Anweisungen auf Deutsch.', 'In the integration exam the instructions are in German.', 'Sa integration exam, nasa German ang instructions.'),
], [
    choice(X, 'lesen', LOOK, 'Bild 1: Was macht man?', 'ankreuzen', ['ergänzen', 'zuordnen'], same('Bild 1 zeigt ein Kreuz: ankreuzen. 2 = ergänzen, 3 = zuordnen, 4 = markieren.'), [G2], R('ankreuzen'),
           img=img('anweisungen', 'Vier Bilder: ein Kreuz im Kästchen, eine Lücke, Linien zwischen Punkten, ein farbiges Wort.', 'Four pictures: a cross in a box, a gap, lines between dots, a highlighted word.', 'Apat na larawan: ekis sa kahon, patlang, linya sa pagitan ng tuldok, kulay na salita.')),
    choice(X, 'lesen', READ, 'Anweisung: „Ergänzen Sie die Wörter.“ Was machen Sie?', 'Ich schreibe die Wörter in die Lücken.', ['Ich mache ein Kreuz.', 'Ich lese laut.'], L('ergänzen = in die Lücke schreiben.', 'ergänzen = write into the gap.', 'ergänzen = isulat sa patlang.'), [G2], R('ergänzen')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Ein x in einem Kästchen machen heißt …', 'ankreuzen', ['ergänzen', 'markieren'], L('ankreuzen = ein Kreuz machen.', 'ankreuzen = make a cross.', 'ankreuzen = lagyan ng ekis.'), [G2], R('ankreuzen')),
])
lesson(5, L('Richtig oder falsch?', 'Right or wrong?', 'Tama o mali?'), ['richtig', 'falsch', 'Frage', 'Antwort', 'Lösung', 'Fehler', 'Aussage', 'Prüfung', 'Test'], [
    C('richtig – falsch', 'In der Prüfung: „Ist die Aussage richtig oder falsch?“', 'In the exam: “Is the statement right or wrong?”', 'Sa exam: “Tama o mali ang pahayag?”'),
    C('die Frage – die Antwort – die Lösung', 'Auf eine Frage gibt man eine Antwort. Die Lösung = die richtige Antwort.', 'You give an answer to a question. Lösung = the correct answer.', 'Sumasagot sa tanong. Lösung = tamang sagot.'),
    C('der Fehler', 'Ein Fehler ist nicht schlimm – man lernt daraus.', 'A mistake is not bad – you learn from it.', 'Hindi masama ang mali – natututo ka rito.'),
    C('die Prüfung – der Test', 'Am Ende vom Kurs gibt es eine Prüfung.', 'At the end of the course there is an exam.', 'Sa dulo ng kurso may exam.'),
], [
    choice(X, 'lesen', LOOK, 'Welche Antwort ist falsch?', 'Frage 2', ['Frage 1', 'Frage 3'], same('Bei Frage 2 ist ein Kreuz (✗): falsch.'), [G5], R('falsch', 'Frage'), img=TEST_P()),
    choice(X, 'lesen', READ, 'Aussage: „Ein Heft ist ein Buch.“', 'falsch', ['richtig'], L('Ein Heft ist kein Buch: falsch.', 'An exercise book is not a book: wrong.', 'Hindi libro ang kuwaderno: mali.'), [G5], R('falsch', 'Heft')),
    choice(X, 'lesen', READ, 'Aussage: „Ein Satz hat Wörter.“', 'richtig', ['falsch'], L('Ein Satz hat Wörter: richtig.', 'A sentence has words: right.', 'May mga salita ang pangungusap: tama.'), [G5], R('richtig', 'Satz')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Die richtige Antwort heißt auch …', 'die Lösung', ['der Fehler', 'die Frage'], L('Lösung = richtige Antwort.', 'Lösung = the correct answer.', 'Lösung = tamang sagot.'), [G5], R('Lösung')),
])
lesson(6, L('nicht', 'not', 'hindi'), ['nicht'], [
    C('Ali ist nicht im Kurs.', '„nicht“ verneint ein Verb, ein Adjektiv oder einen Ort.', '“nicht” negates a verb, an adjective or a place.', 'Ang “nicht” ay pantanggi sa verb, adjective o lugar.'),
    C('Ich verstehe das nicht.', '„nicht“ steht oft am Satzende.', '“nicht” often comes at the end of the sentence.', 'Madalas nasa dulo ng pangungusap ang “nicht”.'),
    C('Das ist nicht richtig.', 'nicht + Adjektiv: nicht richtig = falsch.', 'nicht + adjective: nicht richtig = wrong.', 'nicht + adjective: nicht richtig = mali.'),
], [
    choice(X, 'lesen', LOOK, 'Ist Ali im Kurs?', 'Nein, Ali ist nicht im Kurs.', ['Ja, Ali ist im Kurs.', 'Nein, Ali ist kein im Kurs.'], L('Der Sessel von Ali ist leer: Ali ist nicht im Kurs.', 'Ali’s chair is empty: he is not in class.', 'Bakante ang upuan ni Ali: wala siya sa klase.'), [G4], R('nicht', 'Kurs'),
           img=img('sessel', 'Drei Sessel: Jose und Anna sitzen, der Sessel von Ali ist leer.', 'Three chairs: Jose and Anna sit, Ali’s chair is empty.', 'Tatlong upuan: nakaupo sina Jose at Anna, bakante ang kay Ali.')),
    cloze(X, 'grammatikWortschatz', GAPS, 'Ich verstehe das {{1}}.', [['nicht']], L('Verb verneinen → nicht.', 'Negating a verb → nicht.', 'Pantanggi sa verb → nicht.'), [G4], R('nicht', 'verstehen')),
    choice(X, 'hoeren', LISTEN, None, 'Tom kommt heute nicht.', ['Tom kommt heute.'], same('Sie hören: „Tom kommt heute nicht. Er ist krank.“'), [G4], R('nicht'), audio='Tom kommt heute nicht. Er ist krank.'),
])
lesson(7, L('kein, keine', 'no, not a', 'wala, hindi'), ['kein'], [
    C('Ich habe kein Buch.', '„kein“ verneint ein Nomen ohne Artikel oder mit ein/eine: ein Buch → kein Buch.', '“kein” negates a noun with ein/eine or no article: ein Buch → kein Buch.', 'Ang “kein” ay pantanggi sa noun na may ein/eine: ein Buch → kein Buch.'),
    C('eine Frage → keine Frage', 'die → keine. Plural: keine Bücher.', 'die → keine. Plural: keine Bücher (no books).', 'die → keine. Plural: keine Bücher (walang libro).'),
    C('nicht oder kein?', 'Nomen mit ein/eine oder ohne Artikel → kein. Sonst → nicht.', 'Noun with ein/eine or no article → kein. Otherwise → nicht.', 'Noun na may ein/eine o walang article → kein. Kung hindi → nicht.'),
], [
    choice(X, 'lesen', LOOK, 'Hat Tom ein Buch?', 'Nein, er hat kein Buch.', ['Nein, er hat nicht Buch.', 'Ja, er hat ein Buch.'], L('Auf dem Tisch von Tom ist nur ein Heft: kein Buch.', 'On Tom’s desk there is only an exercise book: no book.', 'Kuwaderno lang ang nasa mesa ni Tom: walang libro.'), [G4], R('kein', 'Buch'),
           img=img('tische', 'Zwei Tische: Maria hat Buch und Heft, Tom hat nur ein Heft.', 'Two desks: Maria has a book and an exercise book, Tom only an exercise book.', 'Dalawang mesa: may libro at kuwaderno si Maria, kuwaderno lang si Tom.')),
    cloze(X, 'grammatikWortschatz', GAPS, 'Ich habe {{1}} Frage. Ich habe {{2}} Heft.', [['keine'], ['kein']], L('die Frage → keine Frage; das Heft → kein Heft.', 'die Frage → keine Frage (no question); das Heft → kein Heft (no exercise book).', 'die Frage → keine Frage (walang tanong); das Heft → kein Heft (walang kuwaderno).'), [G4], R('kein')),
    choice(X, 'grammatikWortschatz', CHOOSE, 'Das ist … Fehler.', 'kein', ['nicht', 'keine'], L('der Fehler → kein Fehler.', 'der Fehler → kein Fehler (no mistake).', 'der Fehler → kein Fehler (walang mali).'), [G4], R('kein', 'Fehler')),
])
lesson(8, L('Verben im Kurs', 'Verbs in class', 'Mga verb sa klase'), ['öffnen', 'zeigen', 'warten', 'zuhören', 'lernen', 'üben', 'erklären', 'bringen', 'holen'], [
    C('Öffnen Sie das Buch.', '„öffnen“: ich öffne, du öffnest, er öffnet.', '“öffnen” (open): ich öffne, du öffnest, er öffnet.', '“öffnen” (buksan): ich öffne, du öffnest, er öffnet.'),
    C('Die Lehrerin zeigt auf die Tafel und erklärt.', '„zeigen“, „erklären“ – regelmäßig.', '“zeigen” (show), “erklären” (explain) – regular.', '“zeigen” (ipakita), “erklären” (ipaliwanag) – regular.'),
    C('Hören Sie zu! – Warten Sie, bitte.', '„zuhören“: Ich höre zu (trennbar). „warten“: er wartet.', '“zuhören” (listen): Ich höre zu (separable). “warten” (wait): er wartet.', '“zuhören”: Ich höre zu (nahahati). “warten”: er wartet.'),
    C('Wir lernen und üben. Bringen Sie das Heft mit. Holen Sie ein Blatt.', 'lernen, üben, bringen, holen.', 'learn, practise, bring, fetch.', 'mag-aral, magsanay, magdala, kumuha.'),
], [
    choice(X, 'grammatikWortschatz', LOOK, 'Bild 3: Was macht man?', 'warten', ['öffnen', 'zuhören'], same('Bild 3 zeigt eine Uhr: warten. 1 = öffnen, 2 = zeigen, 4 = zuhören.'), [G2], R('warten'),
           img=img('verben', 'Vier Bilder: ein offenes Buch, eine Hand zeigt auf die Tafel, eine Uhr, ein Ohr.', 'Four pictures: an open book, a hand pointing at the board, a clock, an ear.', 'Apat na larawan: bukas na libro, kamay na nakaturo sa pisara, orasan, tainga.')),
    cloze(X, 'grammatikWortschatz', GAPS, 'Die Lehrerin {{1}} (erklären) die Aufgabe. Er {{2}} (warten).', [['erklärt'], ['wartet']], L('sie erklärt, er wartet (mit -et).', 'sie erklärt, er wartet (with -et).', 'sie erklärt, er wartet (may -et).'), [G2], R('erklären', 'warten')),
    choice(X, 'hoeren', LISTEN, None, 'Wir sollen zuhören.', ['Wir sollen schreiben.'], same('Sie hören: „Bitte hören Sie gut zu.“'), [G2], R('zuhören'), audio='Bitte hören Sie gut zu.'),
])
lesson(9, L('Hausübung und Pause', 'Homework and break', 'Takdang-aralin at pahinga'), ['Hausübung', 'Hausaufgabe', 'Pause'], [
    C('die Hausübung', 'In Österreich sagt man „Hausübung“. (in Deutschland: „Hausaufgabe“)', 'In Austria you say “Hausübung” (in Germany: “Hausaufgabe”).', 'Sa Austria: “Hausübung” (sa Germany: “Hausaufgabe”).'),
    C('die Pause', 'Um 10:30 Uhr ist Pause.', 'At 10:30 there is a break.', 'Pahinga ng 10:30.'),
], [
    choice(X, 'lesen', LOOK, 'Was ist die Hausübung?', 'Seite 20', ['Seite 12', 'Aufgabe 3'], same('Im Plan: „Hausübung: Seite 20“.'), [G5], R('Hausübung', 'Seite'), img=PLAN()),
    choice(X, 'lesen', LOOK, 'Wann ist Pause?', 'um 10:30 Uhr', ['um 9:00 Uhr', 'um 12:00 Uhr'], same('Im Plan: „Pause: 10:30“.'), [G5], R('Pause'), img=PLAN()),
    choice(X, 'grammatikWortschatz', CHOOSE, '… Hausübung', 'die', ['der', 'das'], L('die Übung → die Hausübung.', 'die Übung (exercise) → die Hausübung (homework).', 'die Übung → die Hausübung (takdang-aralin).'), [G1], R('Hausübung')),
])
lesson(10, L('Was bedeutet das?', 'What does that mean?', 'Ano ang ibig sabihin niyan?'), ['bedeuten'], [
    C('Was bedeutet „Thema“?', 'Sie kennen ein Wort nicht? Fragen Sie!', 'You don’t know a word? Ask!', 'Hindi mo alam ang salita? Magtanong!'),
    C('Wie sagt man „book“ auf Deutsch?', 'Antwort: „das Buch“.', 'Answer: “das Buch”.', 'Sagot: “das Buch”.'),
    C('Können Sie das bitte erklären?', 'Höfliche Bitte an die Lehrerin.', 'A polite request to the teacher.', 'Magalang na pakiusap sa guro.'),
], [
    choice(X, 'lesen', LOOK, 'Was möchte Ali wissen?', 'was „Thema“ bedeutet', ['wie man „Thema“ schreibt', 'wo die Lehrerin wohnt'], same('Ali fragt: „Was bedeutet „Thema“?“'), [G3], R('bedeuten', 'Thema'),
           img=img('frage', 'Ali zeigt auf und fragt die Lehrerin etwas.', 'Ali raises his hand and asks the teacher something.', 'Nagtaas ng kamay si Ali at may tinatanong sa guro.')),
    choice(X, 'sprechen', SAY, 'Sie verstehen das Wort „Heft“ nicht.', 'Was bedeutet „Heft“?', ['Wo ist „Heft“?', 'Ich heiße „Heft“.'], L('Nach der Bedeutung fragen: „Was bedeutet …?“', 'Ask for the meaning: “Was bedeutet …?”', 'Itanong ang kahulugan: “Was bedeutet …?”'), [G3], R('bedeuten')),
    choice(X, 'sprechen', SAY, 'Sie wissen das deutsche Wort für „pen“ nicht.', 'Wie sagt man „pen“ auf Deutsch?', ['Was bedeutet Deutsch?', 'Wie schreibt man „pen“?'], L('„Wie sagt man … auf Deutsch?“', '“Wie sagt man … auf Deutsch?”', '“Wie sagt man … auf Deutsch?”'), [G3], R('sagen', 'Deutsch')),
])
WOW = L('In Österreich können Frauen und Männer alle Berufe lernen und ausüben. Deutsch lernen hilft bei der Arbeit, im Alltag und bei der Prüfung.',
        'In Austria women and men can learn and work in all professions. Learning German helps at work, in everyday life and in the exam.',
        'Sa Austria, puwedeng mag-aral at magtrabaho ang babae at lalaki sa lahat ng propesyon. Nakakatulong ang German sa trabaho, araw-araw at sa exam.')
lesson(11, L('Lernen für alle', 'Learning for everyone', 'Pag-aaral para sa lahat'), [], [
    C('Frauen und Männer können alle Berufe lernen.', 'Eine Frau kann Mechanikerin sein, ein Mann Krankenpfleger.', 'A woman can be a mechanic, a man a nurse.', 'Puwedeng mekaniko ang babae, nars ang lalaki.'),
    C('der Beruf – die Berufe', 'Lehrerin, Lehrer – und alle anderen Berufe: für Frauen und für Männer.', 'Teacher (woman, man) – and all other jobs: for women and for men.', 'Guro (babae, lalaki) – at lahat ng ibang trabaho: para sa babae at lalaki.'),
    C('Deutsch lernen hilft.', 'Mit Deutsch verstehen Sie Briefe, Ärztinnen, Lehrer und Kolleginnen.', 'With German you understand letters, doctors, teachers and colleagues.', 'Sa German, maiintindihan mo ang mga sulat, doktor, guro at katrabaho.'),
], [
    choice(X, 'werte', LOOK, 'Bild 1: Wer arbeitet hier?', 'eine Frau', ['ein Mann'], WOW, [G6], R('Frau'), img=BERUFE()),
    choice(X, 'werte', LOOK, 'Was zeigen Bild 1 und Bild 2?', 'Frauen und Männer arbeiten in allen Berufen.', ['Berufe sind nur für Männer.'], WOW, [G6], R('Mann'), img=BERUFE()),
    choice(X, 'werte', CHOOSE, 'Warum ist Deutsch lernen in Österreich wichtig?', 'Es hilft bei der Arbeit und im Alltag.', ['Man braucht es nur im Kurs.'], WOW, [G6], R('Deutsch', 'lernen')),
])

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
