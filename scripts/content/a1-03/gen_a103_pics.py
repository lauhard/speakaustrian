# A1-03 pictures -> static/img/a1-03-*.svg (flat style like A1-01/A1-02). Facts here must match the tasks.
OUT = str(__import__('pathlib').Path(__file__).resolve().parents[3]) + '/static/img/a1-03-'
HEAD = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 260" role="img" font-family="Arial, sans-serif"><rect width="400" height="260" fill="#f3ead9"/>'
SKIN = {'a': '#f1c9a5', 'b': '#c68a5c', 'c': '#8d5a3b'}


def person(x, shirt, skin='a', hair='#4a2f1c', y=0, long=False, mood='smile'):
    """Simple bust: body at y+150..260, head at y+112."""
    s = SKIN[skin]
    h = f'<path d="M{x-24} {y+116}q-2-34 24-34t24 34q-6-16-24-16t-24 16z" fill="{hair}"/>'
    if long:
        h = f'<path d="M{x-26} {y+150}v-38q0-30 26-30t26 30v38h-10v-36q-4-12-16-12t-16 12v36z" fill="{hair}"/>'
    return (f'<path d="M{x-40} {y+260}v-60q0-44 40-44t40 44v60z" fill="{shirt}"/>'
            f'<circle cx="{x}" cy="{y+118}" r="26" fill="{s}"/>{h}'
            f'<circle cx="{x-9}" cy="{y+118}" r="3" fill="#222"/><circle cx="{x+9}" cy="{y+118}" r="3" fill="#222"/>'
            + {'smile': f'<path d="M{x-8} {y+130}q8 6 16 0" stroke="#222" stroke-width="2.5" fill="none"/>',
               'frown': f'<path d="M{x-8} {y+134}q8 -6 16 0" stroke="#222" stroke-width="2.5" fill="none"/>',
               'open': f'<ellipse cx="{x}" cy="{y+132}" rx="6" ry="5" fill="#7a2d2d"/>'}[mood])


def bubble(x, y, w, text, size=15, color='#34506b', tail='down'):
    tx = x + w / 2
    t = f'<path d="M{tx-8} {y+38}l8 12 8-12z" fill="#fff" stroke="{color}" stroke-width="2"/>' if tail == 'down' else ''
    return (f'<rect x="{x}" y="{y}" width="{w}" height="40" rx="12" fill="#fff" stroke="{color}" stroke-width="2"/>{t}'
            f'<rect x="{tx-7}" y="{y+34}" width="14" height="5" fill="#fff"/>' * (tail == 'down') +
            f'<text x="{tx}" y="{y+26}" font-size="{size}" fill="#1f2937" text-anchor="middle">{text}</text>')


def flag(x, y, kind, w=36):
    h = w * 2 / 3
    if kind == 'AT':
        return f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#c8102e"/><rect x="{x}" y="{y+h/3}" width="{w}" height="{h/3}" fill="#fff"/><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="#999"/></g>'
    if kind == 'DE':
        return f'<g><rect x="{x}" y="{y}" width="{w}" height="{h/3}" fill="#111"/><rect x="{x}" y="{y+h/3}" width="{w}" height="{h/3}" fill="#dd0000"/><rect x="{x}" y="{y+2*h/3}" width="{w}" height="{h/3}" fill="#ffce00"/></g>'
    if kind == 'PH':
        return (f'<g><rect x="{x}" y="{y}" width="{w}" height="{h/2}" fill="#0038a8"/><rect x="{x}" y="{y+h/2}" width="{w}" height="{h/2}" fill="#ce1126"/>'
                f'<path d="M{x} {y}l{h*0.86} {h/2}-{h*0.86} {h/2}z" fill="#fff"/><circle cx="{x+h*0.3}" cy="{y+h/2}" r="{h/8}" fill="#fcd116"/></g>')
    if kind == 'EU':
        stars = ''.join(f'<circle cx="{x+w/2+h*0.3*__import__("math").cos(k*0.5236)}" cy="{y+h/2+h*0.3*__import__("math").sin(k*0.5236)}" r="1.6" fill="#ffcc00"/>' for k in range(12))
        return f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#003399"/>{stars}</g>'


def label(x, y, text, size=16, color='#1f2937', anchor='middle', bold=True):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}"{" font-weight=\"bold\"" if bold else ""}>{text}</text>'


def house(x, y, w=60, color='#e8d3b0', roof='#c8102e'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{w*0.8}" fill="{color}"/><path d="M{x-6} {y}l{w/2+6} -{w*0.5} {w/2+6} {w*0.5}z" fill="{roof}"/><rect x="{x+w*0.4}" y="{y+w*0.4}" width="{w*0.22}" height="{w*0.4}" fill="#7a4e2d"/>'


PICS = {}
# L01: three people with flag pins and name tags
PICS['herkunft'] = ''.join(person(x, c, sk, hr, long=lg) + flag(x - 18, 196, f) + label(x, 236, n, 15, '#fff')
                           for x, c, sk, hr, f, n, lg in ((70, '#2a9d8f', 'a', '#7a4e2d', 'AT', 'Anna', True), (200, '#1d4e89', 'b', '#222', 'PH', 'Jose', False), (330, '#f77f00', 'a', '#d9a066', 'DE', 'Tom', False))) \
    + ''.join(label(x, 76, c, 14) for x, c in ((70, 'Österreich'), (200, 'Philippinen'), (330, 'Deutschland')))
# L02: map – Austria with Vienna, Germany and Switzerland
# Real outlines (Natural Earth 1:50m via scripts/content/geo.mjs, content standard v2 §5): Germany, Austria, Switzerland
# in their true position with quiet neighbours; one dot = Vienna. Tasks ask which countries are shown and where Vienna is.
GEO = __import__('json').load(open(str(__import__('pathlib').Path(__file__).resolve().parents[1]) + '/geo.json'))
FILL = {'Germany': ('#f2e2b8', '#8a7a5a'), 'Austria': ('#fbd3d3', '#c8102e'), 'Switzerland': ('#e3edc8', '#6d8a3a')}


def halo(x, y, text, size, color):
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="bold" fill="{color}" text-anchor="middle" '
            f'stroke="#fff" stroke-width="3.5" stroke-linejoin="round" paint-order="stroke">{text}</text>')


def geo_map(v, labels, dots, clip):
    w, h = v['w'], v['h']
    out = f'<defs><clipPath id="{clip}"><rect width="{w}" height="{h}" rx="10"/></clipPath></defs><g clip-path="url(#{clip})">'
    out += f'<rect width="{w}" height="{h}" fill="#d6ebf5"/>'
    out += ''.join(f'<path d="{d}" fill="#efe9de" stroke="#c9bfae" stroke-width="0.8"/>' for n, d in v['shapes'].items() if n not in v['main'])
    out += ''.join(f'<path d="{v["shapes"][n]}" fill="{FILL[n][0]}" stroke="{FILL[n][1]}" stroke-width="{2.2 if n == "Austria" else 1.6}" stroke-linejoin="round"/>' for n in v['main'])
    out += '</g>'
    for city in dots:
        x, y = v['cities'][city]
        out += f'<circle cx="{x}" cy="{y}" r="5.5" fill="#1f2937" stroke="#fff" stroke-width="2"/>' + halo(x, y - 11, city, 14, '#1f2937')
    return out + ''.join(halo(x, y, t, size, color) for x, y, t, size, color in labels)


D = GEO['dach']
cx = lambda n, dx=0, dy=0: (D['centroids'][n][0] + dx, D['centroids'][n][1] + dy)
PICS['karte'] = geo_map(D, [(*cx('Germany', 0, 10), 'Deutschland', 18, '#5b4a1c'), (*cx('Austria', 4, 6), 'Österreich', 15, '#c8102e'), (*cx('Switzerland', 0, 5), 'Schweiz', 13, '#3f5a1c')], ['Wien'], 'clip-dach')
# L03: city Graz (left) vs village St. Georgen (right) – two panels, Maria and Lukas in front of their place
def panel(x, w, fill, body, clip):
    return (f'<defs><clipPath id="{clip}"><rect x="{x}" y="8" width="{w}" height="244" rx="12"/></clipPath></defs>'
            f'<g clip-path="url(#{clip})"><rect x="{x}" y="8" width="{w}" height="244" fill="{fill}"/><g transform="translate({x} 0)">{body}</g></g>'
            f'<rect x="{x}" y="8" width="{w}" height="244" rx="12" fill="none" stroke="#c9b18e" stroke-width="2"/>')


def bust(cx, s, shirt, skin, hair, long=False, mood='smile'):
    """Bust scaled by s, centred at cx, bottom edge at y=252 (panel bottom)."""
    return f'<g transform="translate({cx - 60 * s} {252 - 260 * s}) scale({s})">{person(60, shirt, skin, hair, long=long, mood=mood)}</g>'


def windows(x, y, cols, rows, dx=14, dy=26):
    return ''.join(f'<rect x="{x + c * dx}" y="{y + r * dy}" width="8" height="13" fill="#9ed8ff" stroke="#6b8fa8" stroke-width="0.8"/>' for c in range(cols) for r in range(rows))


city = ('<rect x="0" y="206" width="210" height="50" fill="#a9a9a9"/><path d="M0 226h210" stroke="#fff" stroke-width="3" stroke-dasharray="16 12"/>'
        '<rect x="14" y="78" width="54" height="128" fill="#b8bec6"/><rect x="72" y="52" width="58" height="154" fill="#9aa3ad"/><rect x="134" y="92" width="56" height="114" fill="#c7cdd4"/>'
        + windows(22, 88, 3, 4) + windows(80, 62, 3, 5) + windows(142, 102, 3, 3))
PICS['wohnort'] = (panel(8, 188, '#dfeaf3', city + bust(102, 0.62, '#c8102e', 'b', '#222', long=True), 'clip-city')
                   + '<rect x="52" y="18" width="116" height="30" rx="5" fill="#fff" stroke="#1d4e89" stroke-width="3"/>' + label(110, 40, 'Graz', 20, '#1d4e89')
                   + label(110, 238, 'Maria', 14, '#fff')
                   + panel(204, 188, '#e6f1d8',
                           '<path d="M0 180q90-34 188-8v80H0z" fill="#8fc66b"/><rect y="214" width="188" height="40" fill="#b99f78"/>'
                           + house(8, 150, 44) + house(56, 146, 38, '#f2e2b8', '#7a4e2d')
                           + '<rect x="104" y="112" width="22" height="48" fill="#e8d3b0"/><path d="M100 112l15-26 15 26z" fill="#7a4e2d"/><path d="M115 70v16M109 77h12" stroke="#1f2937" stroke-width="2.5"/>'
                           + bust(148, 0.62, '#1d4e89', 'a', '#7a4e2d'), 'clip-dorf')
                   + '<rect x="216" y="18" width="164" height="30" rx="5" fill="#ffd23f" stroke="#1f2937" stroke-width="2.5"/>' + label(298, 40, 'St. Georgen', 18)
                   + label(352, 238, 'Lukas', 14, '#fff'))
# L04: envelope with address and a card with the e-mail address (all text >= 17 px)
PICS['adresse'] = ('<rect x="16" y="14" width="260" height="168" rx="8" fill="#fff" stroke="#9ca3af" stroke-width="2.5"/>'
                   '<path d="M16 22l130 84 130-84" fill="none" stroke="#e1e4e8" stroke-width="2"/>'
                   '<rect x="222" y="26" width="42" height="50" rx="2" fill="#fff" stroke="#c8102e" stroke-width="2" stroke-dasharray="4 3"/>' + flag(228, 38, 'AT', 30)
                   + label(34, 118, 'Maria Santos', 19, anchor='start') + label(34, 144, 'Hauptstraße 12', 19, anchor='start', bold=False)
                   + label(34, 170, '8010 Graz', 19, anchor='start', bold=False)
                   + '<rect x="16" y="198" width="368" height="50" rx="10" fill="#e0ebf8" stroke="#1d4e89" stroke-width="2.5"/>'
                   + '<rect x="30" y="212" width="30" height="22" rx="3" fill="#fff" stroke="#1d4e89" stroke-width="2"/><path d="M30 214l15 11 15-11" fill="none" stroke="#1d4e89" stroke-width="2"/>'
                   + label(72, 231, 'maria.santos@gmx.at', 19, '#1f2937', anchor='start'))
# L05: course list – who speaks which language (Anna: Deutsch, Englisch · Jose: Tagalog, Englisch, Deutsch · Tom: Deutsch)
CHIP = {'Deutsch': ('#fbd3d3', '#8a1c2b'), 'Englisch': ('#d6e4f5', '#1d4e89'), 'Tagalog': ('#fbe8b0', '#7a5b00')}


def column(cx, name, shirt, skin, hair, langs, long=False):
    out = f'<g transform="translate({cx - 60 * 0.42} 10) scale(0.42)">{person(60, shirt, skin, hair, long=long)}</g>' + label(cx, 150, name, 17)
    for k, lg in enumerate(langs):
        f, t = CHIP[lg]
        out += f'<rect x="{cx - 48}" y="{162 + k * 30}" width="96" height="25" rx="12" fill="{f}" stroke="{t}" stroke-width="1.5"/>' + label(cx, 180 + k * 30, lg, 15, t)
    return out


PICS['sprachen'] = ('<rect x="8" y="8" width="384" height="244" rx="12" fill="#fff"/><path d="M142 20v222M270 20v222" stroke="#e5e7eb" stroke-width="2"/>'
                    + column(75, 'Anna', '#2a9d8f', 'a', '#7a4e2d', ['Deutsch', 'Englisch'], True)
                    + column(206, 'Jose', '#1d4e89', 'b', '#222', ['Tagalog', 'Englisch', 'Deutsch'])
                    + column(335, 'Tom', '#f77f00', 'a', '#d9a066', ['Deutsch']))
# L06: a man talks very fast (open mouth, motion lines), Ali does not understand (frown, question marks)
PICS['langsam'] = (person(95, '#34506b', 'a', '#7a4e2d', mood='open') + person(305, '#c8102e', 'c', '#222', mood='frown') + label(305, 236, 'Ali', 16, '#fff')
                   + bubble(18, 14, 200, 'Blablablablabla…', 16) + '<path d="M226 22h34M230 36h44M226 50h34" stroke="#f77f00" stroke-width="5" stroke-linecap="round"/>'
                   + ''.join(f'<text x="{x}" y="{y}" font-size="{s}" font-weight="bold" fill="#f77f00" text-anchor="middle">?</text>' for x, y, s in ((262, 96, 34), (350, 80, 44), (332, 52, 28))))
# L07: course card Anna (facts: Österreich, Wien, Deutsch)
def kurskarte(name, land, ort, sprache, fl, shirt, skin, hair, long=False):
    return ('<rect x="30" y="24" width="340" height="212" rx="14" fill="#fff" stroke="#9ca3af" stroke-width="2.5"/>'
            '<path d="M30 38q0-14 14-14h312q14 0 14 14v26H30z" fill="#1d4e89"/>' + label(200, 53, 'Kurskarte', 18, '#fff')
            + '<rect x="48" y="82" width="104" height="134" rx="8" fill="#e8eef5" stroke="#9ca3af"/>'
            + f'<g transform="translate({100 - 60 * 0.62} {216 - 260 * 0.62}) scale(0.62)" >{person(60, shirt, skin, hair, long=long)}</g>'
            + label(170, 100, f'{name}', 22, anchor='start') + flag(318, 76, fl, 44)
            + label(170, 140, f'Land: {land}', 18, anchor='start', bold=False) + label(170, 170, f'Wohnort: {ort}', 18, anchor='start', bold=False)
            + label(170, 200, f'Sprache: {sprache}', 18, anchor='start', bold=False))


PICS['anna'] = kurskarte('Anna Huber', 'Österreich', 'Wien', 'Deutsch', 'AT', '#2a9d8f', 'a', '#7a4e2d', True)
# L08: course card Jose (facts: Philippinen, Wien, Tagalog)
PICS['jose'] = kurskarte('Jose Cruz', 'Philippinen', 'Wien', 'Tagalog', 'PH', '#1d4e89', 'b', '#222')
# L09: three unlabelled pictures: 1 country (real outline of Austria), 2 street, 3 person
import re
_nums = [float(n) for n in re.findall(r'-?\d+\.?\d*', GEO['austria']['shapes']['Austria'])]
_xs, _ys = _nums[0::2], _nums[1::2]
_bx0, _bx1, _by0, _by1 = min(_xs), max(_xs), min(_ys), max(_ys)
_sc = 100 / (_bx1 - _bx0)
PICS['nomen'] = (''.join(f'<rect x="{x}" y="40" width="118" height="186" rx="12" fill="#fff" stroke="#c9b18e" stroke-width="2"/>' for x in (12, 141, 270))
                 + f'<g transform="translate({21 - _bx0 * _sc} {133 - (_by0 + _by1) / 2 * _sc}) scale({_sc})"><path d="{GEO["austria"]["shapes"]["Austria"]}" fill="#fbd3d3" stroke="#c8102e" stroke-width="{2.2 / _sc}" stroke-linejoin="round"/></g>'
                 + '<rect x="150" y="150" width="100" height="76" fill="#a9a9a9"/><path d="M200 150v76" stroke="#fff" stroke-width="3" stroke-dasharray="10 8"/>'
                 + '<rect x="150" y="100" width="30" height="50" fill="#e8d3b0"/><rect x="214" y="112" width="34" height="38" fill="#f2e2b8"/><path d="M146 100l19-24 19 24zM210 112l21-22 21 22z" fill="#c8102e"/>'
                 + '<rect x="148" y="146" width="102" height="6" fill="#7cc36a"/>'
                 + f'<g transform="translate({270 + 59 - 60 * 0.75} {226 - 260 * 0.75}) scale(0.75)"><g clip-path="url(#none)">{person(60, "#f77f00", "a", "#4a2f1c")}</g></g>'
                 + ''.join(f'<circle cx="{c}" cy="40" r="16" fill="#c8102e" stroke="#fff" stroke-width="2"/>' + label(c, 46, str(k), 17, '#fff') for k, c in ((1, 40), (2, 169), (3, 298))))
# L10: village Moosbach – town sign, houses, church, fields
PICS['moosbach'] = ('<rect width="400" height="260" fill="#dff0fa"/><path d="M0 170q100-34 200-10t200-14v114H0z" fill="#8fc66b"/><path d="M0 214q200-26 400 0v46H0z" fill="#8a8f98"/><path d="M0 236h400" stroke="#fff" stroke-width="3" stroke-dasharray="18 14"/>'
                    + house(196, 144, 46) + house(250, 152, 40, '#f2e2b8', '#7a4e2d') + house(300, 148, 44, '#e8d3b0', '#c8102e')
                    + '<rect x="350" y="110" width="26" height="70" fill="#e8d3b0"/><path d="M346 110l17-32 17 32z" fill="#7a4e2d"/><path d="M363 58v20M356 66h14" stroke="#1f2937" stroke-width="3"/>'
                    + '<circle cx="182" cy="150" r="14" fill="#4f9a45"/><rect x="180" y="158" width="4" height="22" fill="#6b4a2d"/>'
                    + '<rect x="58" y="136" width="9" height="82" fill="#6b7280"/><rect x="16" y="56" width="176" height="84" rx="6" fill="#fff" stroke="#1f2937" stroke-width="6"/>'
                    + label(104, 108, 'Moosbach', 29))
# L11: Maria with a map asks for the Bahnhofstraße; the street sign says Hauptstraße
PICS['suchen'] = (person(110, '#c8102e', 'b', '#222', long=True) + label(110, 236, 'Maria', 16, '#fff')
                  + '<rect x="56" y="168" width="108" height="76" rx="3" fill="#fff" stroke="#9ca3af" stroke-width="2"/><path d="M66 190h88M66 214h60M96 172v68M130 172v68" stroke="#7cc36a" stroke-width="4"/><circle cx="98" cy="192" r="5" fill="#c8102e"/>'
                  + bubble(14, 14, 250, 'Wo ist die Bahnhofstraße?', 16)
                  + '<rect x="318" y="124" width="9" height="124" fill="#6b7280"/><rect x="232" y="84" width="160" height="40" rx="5" fill="#1d4e89" stroke="#fff" stroke-width="3"/>' + label(312, 111, 'Hauptstraße', 19, '#fff'))
# L12: panel 1 – a man phones; panel 2 – two people say goodbye in the street
PICS['abschied'] = (panel(8, 188, '#fff', bust(100, 0.82, '#1d4e89', 'a', '#4a2f1c')
                          + '<g transform="rotate(-12 58 130)"><rect x="42" y="96" width="26" height="52" rx="6" fill="#1f2937"/><rect x="46" y="102" width="18" height="34" rx="2" fill="#9ed8ff"/></g>'
                          + '<circle cx="74" cy="150" r="9" fill="#f1c9a5"/><path d="M26 98q-12 20 0 44M14 90q-22 30 0 60" stroke="#34506b" stroke-width="4" fill="none" stroke-linecap="round"/>', 'clip-tel')
                    + panel(204, 188, '#e8f1f8', '<rect y="206" width="188" height="50" fill="#a9a9a9"/><path d="M0 230h188" stroke="#fff" stroke-width="3" stroke-dasharray="14 10"/>' + house(8, 130, 44) + house(130, 124, 48, '#f2e2b8', '#7a4e2d')
                           + f'<g transform="translate(0 -6)">{bust(46, 0.6, "#2a9d8f", "a", "#7a4e2d", long=True)}</g>' + f'<g transform="translate(0 -6)">{bust(142, 0.6, "#1d4e89", "b", "#222")}</g>'
                           + '<path d="M70 186q16-14 16-36" stroke="#2a9d8f" stroke-width="8" stroke-linecap="round" fill="none"/><circle cx="86" cy="146" r="7" fill="#f1c9a5"/>'
                           + '<path d="M118 186q-16-14-16-36" stroke="#1d4e89" stroke-width="8" stroke-linecap="round" fill="none"/><circle cx="102" cy="146" r="7" fill="#c68a5c"/>', 'clip-str')
                    + ''.join(f'<circle cx="{c}" cy="30" r="15" fill="#c8102e" stroke="#fff" stroke-width="2"/>' + label(c, 36, str(k), 17, '#fff') for k, c in ((1, 32), (2, 228))))
# L13: Austria – Vienna, euro, EU flag
A = GEO['austria']
_wx, _wy = A['cities']['Wien']
PICS['oesterreich'] = ('<circle cx="80" cy="46" r="30" fill="#d9a441" stroke="#9aa0a6" stroke-width="8"/>' + label(80, 55, '€', 26, '#5b4a1c')
                       + flag(170, 18, 'EU', 60) + label(200, 72, 'EU', 13) + flag(290, 18, 'AT', 60)
                       + '<g transform="translate(10 90)">' + geo_map(A, [], [], 'clip-at')
                       + f'<path transform="translate({_wx} {_wy})" d="M0-11l3.2 6.6 7.3.9-5.3 5 1.4 7.2L0 5.2l-6.5 3.5 1.4-7.2-5.3-5 7.3-.9z" fill="#c8102e" stroke="#fff" stroke-width="1"/>'
                       + halo(_wx - 6, _wy + 25, 'Wien', 14, '#1f2937') + halo(A['centroids']['Austria'][0], A['centroids']['Austria'][1] + 6, 'Österreich', 18, '#c8102e') + '</g>')

for name, body in PICS.items():
    open(f'{OUT}{name}.svg', 'w').write(HEAD + body + '</svg>\n')
print(len(PICS), 'pictures')
