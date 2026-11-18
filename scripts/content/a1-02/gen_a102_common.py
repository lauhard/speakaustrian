# Shared helpers for the A1-02 generator (lessons + pools). Not part of the repo.
import json
import random

ROOT = str(__import__('pathlib').Path(__file__).resolve().parents[3])
CH = 'A1-02'
rng = random.Random(20261117)

L = lambda de, en, tl: {'de': de, 'en': en, 'tl': tl}

# ---- vocabulary ids (A1-02 from 03c, A1-01 from the chapter file)
A101 = {v['lemma']: v['id'] for v in json.load(open(f'{ROOT}/src/lib/content/a1-01.json'))['vocab']}
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
        it['sourceIds'] = ['Q101']
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


def cloze(i, skill, instr, text, gaps, exp, goals=None, refs=None, audio=None, img=None, bank=None, hints=None):
    it = _base(i, 'cloze', skill, instr, exp, goals, refs)
    it['text'] = text
    it['gaps'] = {str(n): {'accept': a, **({'hint': hints[n - 1]} if hints and hints[n - 1] else {})} for n, a in enumerate(gaps, 1)}
    if bank:
        it['bank'] = bank  # content standard v2 §3: correct words + 1–2 distractors
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

IMG_KLINGEL = lambda: {'src': '/img/a1-02-klingel.svg', 'alt': L('Ein Hauseingang mit Hausnummer und Klingeln mit Namen.', 'A house entrance with a house number and doorbells with names.', 'Pasukan ng bahay na may numero ng bahay at mga doorbell na may pangalan.')}
IMG_MARKT = lambda: {'src': '/img/a1-02-markt.svg', 'alt': L('Ein Marktstand mit Äpfeln, Brot und Milch. Auf jedem Produkt steht ein Preis.', 'A market stall with apples, bread and milk. Each product has a price.', 'Isang puwesto sa palengke na may mansanas, tinapay at gatas. May presyo ang bawat produkto.')}
IMG_NOTRUF = lambda: {'src': '/img/a1-02-notruf.svg', 'alt': L('Ein Aufkleber mit vier Notrufnummern und Bildern.', 'A sticker with four emergency numbers and pictures.', 'Sticker na may apat na emergency number at mga larawan.')}

# Picture facts (must match the SVGs)
KLINGEL = {'Hausnummer': 17, 'Huber': 1, 'Santos': 2, 'Berger': 3, 'Mayer': 4}
MARKT = {'Äpfel': 240, 'Brot': 310, 'Milch': 119}
NOTRUF = {'Feuerwehr': '122', 'Polizei': '133', 'Rettung': '144'}

GOALS = {
    'A1-02-G1': L('Buchstabieren und Buchstaben verstehen', 'Spelling and understanding letters', 'Mag-spell at umintindi ng mga titik'),
    'A1-02-G2': L('Zahlen von 0 bis 100 verstehen und sagen', 'Understanding and saying numbers from 0 to 100', 'Umintindi at magsabi ng numero mula 0 hanggang 100'),
    'A1-02-G3': L('Das Alter sagen und fragen', 'Saying your age and asking about age', 'Sabihin at itanong ang edad'),
    'A1-02-G4': L('Telefonnummer, Hausnummer, Postleitzahl', 'Phone number, house number, postcode', 'Numero ng telepono, numero ng bahay, postal code'),
    'A1-02-G5': L('Preise in Euro und Cent', 'Prices in euros and cents', 'Presyo sa euro at cent'),
    'A1-02-G6': L('Die Verben sein und haben', 'The verbs sein and haben', 'Ang mga verb na sein at haben'),
    'A1-02-G7': L('Fragen mit wie, wie viel, wie viele', 'Questions with wie, wie viel, wie viele', 'Mga tanong na may wie, wie viel, wie viele'),
    'A1-02-G8': L('Notrufnummern in Österreich', 'Emergency numbers in Austria', 'Mga emergency number sa Austria'),
}
G1, G2, G3, G4, G5, G6, G7, G8 = GOALS

def img(name, de_, en, tl):
    return {'src': f'/img/a1-02-{name}.svg', 'alt': L(de_, en, tl)}
