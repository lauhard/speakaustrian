# Shared helpers for the A1-02 generator (lessons + pools). Not part of the repo.
import json
import random

ROOT = str(__import__('pathlib').Path(__file__).resolve().parents[3])
CH = 'A1-03'
rng = random.Random(20261118)

L = lambda de, en, tl: {'de': de, 'en': en, 'tl': tl}

# ---- vocabulary ids (A1-02 from 03c, A1-01 from the chapter file)
A101 = {v['lemma']: v['id'] for f in ('a1-01', 'a1-02') for v in json.load(open(f'{ROOT}/src/lib/content/{f}.json'))['vocab']}
A102 = {}
NO_CARD = set()  # R-W1: passive entries get no card; sets get one set card (not built yet, spec-gaps G-014)
for line in open(f'{ROOT}/docs/spec/03c-kapitel-wortschatz.tsv'):
    f = line.rstrip('\n').split('\t')
    if f[-1] == CH:
        A102[f[1]] = f[0]
        if f[5] == 'p' or f[7]:
            NO_CARD.add(f[0])
ID = {**A101, **A102}
R = lambda *ls: [ID[l] for l in ls]

# ---- numbers
ONES = 'null eins zwei drei vier fünf sechs sieben acht neun zehn elf zwölf dreizehn vierzehn fünfzehn sechzehn siebzehn achtzehn neunzehn'.split()
TENS = {2: 'zwanzig', 3: 'dreißig', 4: 'vierzig', 5: 'fünfzig', 6: 'sechzig', 7: 'siebzig', 8: 'achtzig', 9: 'neunzig'}


def de(n):
    """German number word, 0–9999."""
    if n < 20:
        return ONES[n]
    if n < 100:
        t, o = divmod(n, 10)
        return TENS[t] if o == 0 else ('ein' if o == 1 else ONES[o]) + 'und' + TENS[t]
    if n < 1000:
        h, r = divmod(n, 100)
        return ('' if h == 1 else ONES[h]) + 'hundert' + ('' if r == 0 else de(r))
    t, r = divmod(n, 1000)
    return ('' if t == 1 else de(t)) + 'tausend' + ('' if r == 0 else de(r))


assert de(21) == 'einundzwanzig' and de(47) == 'siebenundvierzig' and de(16) == 'sechzehn' and de(100) == 'hundert' and de(1010) == 'tausendzehn'


def euro(c):
    """Price in cents -> ('3,50 €', 'drei Euro fünfzig')."""
    e, ct = divmod(c, 100)
    shown = f'{e},{ct:02d} €'
    if e == 0:
        return shown, f'{de(ct)} Cent'
    word = 'ein' if e == 1 else de(e)
    return shown, f'{word} Euro' + ('' if ct == 0 else f' {de(ct)}')


def digits(s):
    """'0664 12' -> 'null, sechs, sechs, vier, eins, zwei' (phone numbers digit by digit)."""
    return ', '.join(ONES[int(d)] for d in s if d.isdigit())


def spell(word):
    """Letters as shown: 'B, A, U, E, R.'"""
    return ', '.join(word.upper()) + '.'


def spell_audio(word):
    """Letters for the speech port: lower case, no full stop (upper case 'I.' / 'V.' is read as a Roman numeral)."""
    return ', '.join(word.lower())


NAMES = dict(zip('abcdefghijklmnopqrstuvwxyzäöü', 'A Be Ze De E Ef Ge Ha I Jot Ka El Em En O Pe Ku Er Es Te U Fau We Ix Üpsilon Zett Ä Ö Ü'.split()))
letter_names = lambda word: ' – '.join(NAMES[c] for c in word.lower())


# ---- items
def _base(i, kind, skill, instr, exp, goals, refs):
    it = {'id': i, 'type': kind, 'skill': skill, 'instruction': instr, 'explanation': exp}
    if goals is not None:
        it['goals'] = goals
    if refs:
        it['refs'] = refs
    if skill == 'werte':
        it['sourceIds'] = ['Q36']
    return it


def choice(i, skill, instr, prompt, correct, others, exp, goals=None, refs=None, audio=None, only=True, img=None):
    it = _base(i, 'choice', skill, instr, exp, goals, refs)
    k = rng.randrange(len(others) + 1)
    it['options'] = others[:k] + [correct] + others[k:]
    it['answer'] = k
    if prompt:
        it['prompt'] = prompt
    if audio:
        it['audioText'] = audio
        if only:
            it['audioOnly'] = True
    if img:
        it['image'] = img
    return it


def cloze(i, skill, instr, text, gaps, exp, goals=None, refs=None, audio=None, img=None):
    it = _base(i, 'cloze', skill, instr, exp, goals, refs)
    it['text'] = text
    it['gaps'] = {str(n): {'accept': a} for n, a in enumerate(gaps, 1)}
    if audio:
        it.update(audioText=audio, audioOnly=True)
    if img:
        it['image'] = img
    return it


def short(i, skill, instr, prompt, accept, exp, goals=None, refs=None, audio=None, img=None):
    it = _base(i, 'short', skill, instr, exp, goals, refs)
    it['prompt'] = prompt
    it['accept'] = accept
    if audio:
        it.update(audioText=audio, audioOnly=True)
    if img:
        it['image'] = img
    return it


# ---- common instructions
CHOOSE = L('Wählen Sie die richtige Antwort.', 'Choose the correct answer.', 'Piliin ang tamang sagot.')
READ = L('Lesen Sie. Wählen Sie die richtige Antwort.', 'Read. Choose the correct answer.', 'Basahin. Piliin ang tamang sagot.')
LISTEN = L('Hören Sie. Was ist richtig?', 'Listen. What is correct?', 'Makinig. Alin ang tama?')
SAY = L('Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'What do you say? Choose, then say it aloud.', 'Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.')
GAPS = L('Schreiben Sie die fehlenden Wörter.', 'Write the missing words.', 'Isulat ang mga nawawalang salita.')
DIGITS = L('Hören Sie. Schreiben Sie die Zahl in Ziffern (z. B. 25).', 'Listen. Write the number in digits (e.g. 25).', 'Makinig. Isulat ang numero gamit ang digits (hal. 25).')
WORD = L('Schreiben Sie die Zahl in Worten.', 'Write the number in words.', 'Isulat ang numero sa salita.')
SPELLED = L('Hören Sie. Jemand buchstabiert. Schreiben Sie das Wort.', 'Listen. Someone spells a word. Write the word.', 'Makinig. May nag-i-spell. Isulat ang salita.')
# The question is in the German prompt; the translated instruction must not hand it over (V5), so it stays generic.
LOOK = lambda en=None, tl=None: L('Schauen Sie das Bild an. Wählen Sie die richtige Antwort.', 'Look at the picture. Choose the correct answer.', 'Tingnan ang larawan. Piliin ang tamang sagot.')

GOALS = {
    'A1-03-G1': L('Sagen, woher man kommt (Land, Heimat)', 'Saying where you come from (country, home)', 'Sabihin kung taga-saan ka (bansa, pinagmulan)'),
    'A1-03-G2': L('Sagen, wo man wohnt (Stadt, Dorf, Adresse)', 'Saying where you live (town, village, address)', 'Sabihin kung saan ka nakatira (lungsod, baryo, address)'),
    'A1-03-G3': L('Über Sprachen sprechen', 'Talking about languages', 'Pag-usapan ang mga wika'),
    'A1-03-G4': L('Nicht verstehen: um Wiederholung und langsames Sprechen bitten', 'Not understanding: asking to repeat and to speak slowly', 'Hindi naintindihan: humiling na ulitin at bagalan'),
    'A1-03-G5': L('Ja/Nein-Fragen stellen und mit ja, nein, doch antworten', 'Asking yes/no questions and answering with ja, nein, doch', 'Magtanong ng oo/hindi at sumagot ng ja, nein, doch'),
    'A1-03-G6': L('Nomen mit Artikel: der, die, das, ein, eine', 'Nouns with articles: der, die, das, ein, eine', 'Noun na may article: der, die, das, ein, eine'),
    'A1-03-G7': L('Verben: sprechen, geben, nehmen, finden, suchen, wohnen', 'Verbs: sprechen, geben, nehmen, finden, suchen, wohnen', 'Mga verb: sprechen, geben, nehmen, finden, suchen, wohnen'),
    'A1-03-G8': L('Österreich: Hauptstadt, Währung, Sprache, EU', 'Austria: capital, currency, language, EU', 'Austria: kabisera, pera, wika, EU'),
}
G1, G2, G3, G4, G5, G6, G7, G8 = GOALS
SPELLED = L('Hören Sie. Jemand buchstabiert. Schreiben Sie das Wort.', 'Listen. Someone spells a word. Write the word.', 'Makinig. May nag-i-spell. Isulat ang salita.')

def img(name, de_, en, tl):
    return {'src': f'/img/a1-03-{name}.svg', 'alt': L(de_, en, tl)}
