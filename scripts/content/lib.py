"""Shared helpers for chapter generators (lessons, pools, pictures).

Usage in a chapter script (scripts/content/a1-NN.py):
    import lib; lib.init('A1-04', seed=20261119, sources=['Q36'])
    from lib import *
Then build LESSONS with lesson(...), pools with fam(...), pictures with svg helpers, and call write_all(...).
Run: python3 scripts/content/a1-NN.py  → writes src/lib/content/<ch>.json, <ch>-pools.json, static/img/<ch>-*.svg
"""
import json
import math
import random
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / 'src/lib/content'

CH = ''
rng = random.Random(0)
ID, NEW, NO_CARD, SOURCES, EARLIER = {}, {}, set(), [], {}
LESSONS, TEST, PRACTICE, PICS = [], [], [], {}


def init(ch, seed, sources):
    """Load vocabulary ids of all earlier chapters and of this chapter (03c)."""
    global CH, rng, SOURCES
    CH, rng, SOURCES = ch, random.Random(seed), sources
    for f in sorted(CONTENT.glob('a[12]-[0-9][0-9].json')):
        if f.stem.upper() < ch:
            ID.update({v['lemma']: v['id'] for v in json.loads(f.read_text())['vocab']})
    EARLIER.update({k.lower(): v for k, v in ID.items()})
    for line in (ROOT / 'docs/spec/03c-kapitel-wortschatz.tsv').read_text().splitlines():
        c = line.split('\t')
        if c[-1] == ch:
            NEW[c[1]] = c[0]
            if c[5] == 'p' or c[7]:
                NO_CARD.add(c[0])  # R-W1: passive entries no card; sets one set card (G-014)
    ID.update(NEW)


L = lambda de, en, tl: {'de': de, 'en': en, 'tl': tl}
# Explanation that is only the German answer: label it instead of pretending to translate it.
def same(de):
    for d, en, tl in (('Sie hören: ', 'You hear: ', 'Naririnig mo: '), ('Im Text: ', 'The text says: ', 'Sabi sa teksto: '), ('Im Plan: ', 'The plan says: ', 'Sabi sa plano: ')):
        if de.startswith(d):
            return L(de, en + de[len(d):], tl + de[len(d):])
    return L(de, f'Answer: {de}', f'Sagot: {de}')
R = lambda *ls: [ID[x] for x in ls]

# ---------------------------------------------------------------- numbers and letters
ONES = 'null eins zwei drei vier fünf sechs sieben acht neun zehn elf zwölf dreizehn vierzehn fünfzehn sechzehn siebzehn achtzehn neunzehn'.split()
TENS = {2: 'zwanzig', 3: 'dreißig', 4: 'vierzig', 5: 'fünfzig', 6: 'sechzig', 7: 'siebzig', 8: 'achtzig', 9: 'neunzig'}


def de(n):
    if n < 20:
        return ONES[n]
    if n < 100:
        t, o = divmod(n, 10)
        return TENS[t] if o == 0 else ('ein' if o == 1 else ONES[o]) + 'und' + TENS[t]
    h, r = divmod(n, 100)
    return ('' if h == 1 else ONES[h]) + 'hundert' + ('' if r == 0 else de(r))


NAMES = dict(zip('abcdefghijklmnopqrstuvwxyzäöü', 'A Be Ze De E Ef Ge Ha I Jot Ka El Em En O Pe Ku Er Es Te U Fau We Ix Üpsilon Zett Ä Ö Ü'.split()))
spell_audio = lambda w: ', '.join(NAMES[c] for c in w.lower().replace('ß', 'ss'))  # letter names: safe for TTS

# ---------------------------------------------------------------- items
def _base(i, kind, skill, instr, exp, goals, refs):
    it = {'id': i, 'type': kind, 'skill': skill, 'instruction': instr, 'explanation': exp}
    if goals:
        it['goals'] = goals
    if refs:
        it['refs'] = refs
    if skill == 'werte':
        it['sourceIds'] = SOURCES
    return it


def choice(i, skill, instr, prompt, correct, others, exp, goals=None, refs=None, audio=None, img=None):
    it = _base(i, 'choice', skill, instr, exp, goals, refs)
    k = rng.randrange(len(others) + 1)
    it['options'], it['answer'] = others[:k] + [correct] + others[k:], k
    if prompt:
        it['prompt'] = prompt
    if audio:
        it.update(audioText=audio, audioOnly=True)
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
    it['prompt'], it['accept'] = prompt, accept
    if audio:
        it.update(audioText=audio, audioOnly=True)
    if img:
        it['image'] = img
    return it


CHOOSE = L('Wählen Sie die richtige Antwort.', 'Choose the correct answer.', 'Piliin ang tamang sagot.')
READ = L('Lesen Sie. Wählen Sie die richtige Antwort.', 'Read. Choose the correct answer.', 'Basahin. Piliin ang tamang sagot.')
LISTEN = L('Hören Sie. Was ist richtig?', 'Listen. What is correct?', 'Makinig. Alin ang tama?')
SAY = L('Was sagen Sie? Wählen Sie, dann sagen Sie es laut.', 'What do you say? Choose, then say it aloud.', 'Ano ang sasabihin mo? Pumili, tapos sabihin nang malakas.')
GAPS = L('Schreiben Sie die fehlenden Wörter.', 'Write the missing words.', 'Isulat ang mga nawawalang salita.')
LOOK = L('Schauen Sie das Bild an. Wählen Sie die richtige Antwort.', 'Look at the picture. Choose the correct answer.', 'Tingnan ang larawan. Piliin ang tamang sagot.')
RF = ['richtig', 'falsch']  # A1-LES-T2 style (from A1-05 on)
img = lambda name, de_, en, tl: {'src': f'/img/{CH.lower()}-{name}.svg', 'alt': L(de_, en, tl)}

# ---------------------------------------------------------------- lessons
C = lambda phrase, de_, en, tl, audio=None: {'phrase': phrase, 'note': L(de_, en, tl), **({'audioText': audio} if audio else {})}
# Content standard v2 §1 (docs/content-standard.md): phrase / rule (+ speakable examples) / culture cards, lesson intro.
PHRASE = lambda phrase, de_, en, tl: {'kind': 'phrase', 'phrase': phrase, 'note': L(de_, en, tl)}
RULE = lambda phrase, de_, en, tl, examples: {'kind': 'rule', 'phrase': phrase, 'note': L(de_, en, tl), 'examples': examples}
CULTURE = lambda phrase, de_, en, tl: {'kind': 'culture', 'phrase': phrase, 'note': L(de_, en, tl)}
INTRO = lambda situation, goal: {'situation': situation, 'goal': goal}


def lesson(n, title, introduces, cards, items, intro=None):
    lid = f'{CH}-L{n:02d}'
    for k, it in enumerate(items, 1):
        it['id'] = f'{lid}-I{k}'
    assert any('image' in i for i in items), f'{lid}: every lesson needs a picture task'
    LESSONS.append({'id': lid, 'title': title, **({'intro': intro} if intro else {}), 'introduces': [r for r in R(*introduces) if r not in NO_CARD], 'cards': cards, 'items': items})


# ---------------------------------------------------------------- pools
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


def _interleave(groups):
    return [g[k] for k in range(max(map(len, groups))) for g in groups if k < len(g)]


def _group(lst, key):
    d = {}
    for x in lst:
        d.setdefault(key(x), []).append(x)
    return list(d.values())


# ---------------------------------------------------------------- pictures (flat style of A1-01…A1-03)
SKIN = {'a': '#f1c9a5', 'b': '#c68a5c', 'c': '#8d5a3b'}


def person(x, shirt, skin='a', hair='#4a2f1c', y=0, long=False, s=1.0):
    """Bust; s scales around (x, y+260)."""
    k = SKIN[skin]
    h = (f'<path d="M{x-26} {y+150}v-38q0-30 26-30t26 30v38h-10v-36q-4-12-16-12t-16 12v36z" fill="{hair}"/>' if long
         else f'<path d="M{x-24} {y+116}q-2-34 24-34t24 34q-6-16-24-16t-24 16z" fill="{hair}"/>')
    body = (f'<path d="M{x-40} {y+260}v-60q0-44 40-44t40 44v60z" fill="{shirt}"/><circle cx="{x}" cy="{y+118}" r="26" fill="{k}"/>{h}'
            f'<circle cx="{x-9}" cy="{y+118}" r="3" fill="#222"/><circle cx="{x+9}" cy="{y+118}" r="3" fill="#222"/>'
            f'<path d="M{x-8} {y+130}q8 6 16 0" stroke="#222" stroke-width="2.5" fill="none"/>')
    return body if s == 1 else f'<g transform="translate({x} {y+260}) scale({s}) translate({-x} {-(y+260)})">{body}</g>'


def label(x, y, text, size=16, color='#1f2937', anchor='middle', bold=True):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}"{" font-weight=\"bold\"" if bold else ""}>{text}</text>'


def bubble(x, y, w, text, size=15, color='#34506b', tail_x=None):
    tx = x + w / 2 if tail_x is None else tail_x
    return (f'<rect x="{x}" y="{y}" width="{w}" height="40" rx="12" fill="#fff" stroke="{color}" stroke-width="2"/>'
            f'<path d="M{tx-8} {y+38}l8 12 8-12z" fill="#fff" stroke="{color}" stroke-width="2"/><rect x="{tx-7}" y="{y+34}" width="14" height="5" fill="#fff"/>'
            + label(x + w / 2, y + 26, text, size, bold=False))


def house(x, y, w=60, color='#e8d3b0', roof='#c8102e'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{w*0.8}" fill="{color}"/><path d="M{x-6} {y}l{w/2+6} -{w*0.5} {w/2+6} {w*0.5}z" fill="{roof}"/><rect x="{x+w*0.4}" y="{y+w*0.4}" width="{w*0.22}" height="{w*0.4}" fill="#7a4e2d"/>'


def panel(x, y, w, h, n=None):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#fff"/>' + (f'<circle cx="{x+16}" cy="{y+16}" r="12" fill="#c8102e"/>' + label(x + 16, y + 21, str(n), 14, '#fff') if n else '')


HEAD = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 260" role="img" font-family="Arial, sans-serif"><rect width="400" height="260" fill="#f3ead9"/>'


def write_svgs(sheet='/tmp/sheet.png'):
    """Write PICS and render one contact sheet to look at (render and check every picture before shipping)."""
    out = []
    for name, body in PICS.items():
        f = ROOT / f'static/img/{CH.lower()}-{name}.svg'
        f.write_text(HEAD + body + '</svg>\n')
        png = f'/tmp/{CH.lower()}-{name}.png'
        subprocess.run(['rsvg-convert', '-w', '300', str(f), '-o', png], check=True)
        out.append(png)
    subprocess.run(['montage', '-geometry', '+4+4', '-tile', '4x', '-label', '%t', *out, sheet], check=True)
    print(len(PICS), 'pictures →', sheet)


# ---------------------------------------------------------------- recycling refs (Q8)
def _texts(it):
    return ' '.join([it.get('prompt', ''), it.get('text', ''), it.get('audioText', ''), *it.get('options', []), *(a for a in it.get('accept', []))]).lower()


def add_earlier_refs(items):
    """Add refs to vocabulary of earlier chapters that the German text really uses (makes recycling measurable)."""
    for it in items:
        words = set(__import__('re').findall(r"[a-zäöüß]+", _texts(it)))
        found = [i for lemma, i in EARLIER.items() if (lemma in words if ' ' not in lemma else lemma in _texts(it)) and i not in NEW.values()]
        if found:
            it['refs'] = list(dict.fromkeys([*it.get('refs', []), *found[:4]]))


# ---------------------------------------------------------------- write everything
def write_all(vocab_meta, goals, quota):
    """vocab_meta: lemma -> (article|None, en, tl). quota: test items per discipline (focus +2)."""
    add_earlier_refs([*PRACTICE, *TEST, *(i for l in LESSONS for i in l['items'])])
    vocab = []
    for lemma, wid in NEW.items():
        art, en, tl = vocab_meta[lemma]
        vocab.append({'id': wid, 'lemma': lemma, 'en': en, 'tl': tl, **({'article': art} if art else {})})
    missing = [v['lemma'] for v in vocab if v['id'] not in {r for l in LESSONS for r in l['introduces']} and v['id'] not in NO_CARD]
    assert not missing, f'not introduced: {missing}'
    (CONTENT / f'{CH.lower()}.json').write_text(json.dumps({'schemaVersion': 1, 'chapterId': CH, 'tlReviewStatus': 'machine', 'vocab': vocab, 'lessons': LESSONS}, ensure_ascii=False, indent='\t'))
    (CONTENT / f'{CH.lower()}-pools.json').write_text(json.dumps({'chapterId': CH, 'goals': goals, 'pools': {'practice': PRACTICE, 'test': TEST}}, ensure_ascii=False, indent='\t'))
    # Practice split as the app does it (G-010 A): readiness blocks need ≥ 2 × quota per discipline in the rest.
    rest = _interleave(_interleave(_group(_group(PRACTICE, lambda p: p.get('family', p['id'])), lambda f: f[0]['skill'])))[40:]
    rs = Counter(p['skill'] for p in rest)
    print(f'{CH}: {len(LESSONS)} lessons / {sum(len(l["items"]) for l in LESSONS)} tasks · test {len(TEST)} {dict(Counter(t["skill"] for t in TEST))} · practice {len(PRACTICE)}')
    for s, q in quota.items():
        if rs[s] < 2 * q:
            print(f'  ! practice rest {s}: {rs[s]} < {2 * q}')
