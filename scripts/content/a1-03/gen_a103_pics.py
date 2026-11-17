# A1-03 pictures -> static/img/a1-03-*.svg (flat style like A1-01/A1-02). Facts here must match the tasks.
OUT = str(__import__('pathlib').Path(__file__).resolve().parents[3]) + '/static/img/a1-03-'
HEAD = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 260" role="img" font-family="Arial, sans-serif"><rect width="400" height="260" fill="#f3ead9"/>'
SKIN = {'a': '#f1c9a5', 'b': '#c68a5c', 'c': '#8d5a3b'}


def person(x, shirt, skin='a', hair='#4a2f1c', y=0, long=False):
    """Simple bust: body at y+150..260, head at y+112."""
    s = SKIN[skin]
    h = f'<path d="M{x-24} {y+116}q-2-34 24-34t24 34q-6-16-24-16t-24 16z" fill="{hair}"/>'
    if long:
        h = f'<path d="M{x-26} {y+150}v-38q0-30 26-30t26 30v38h-10v-36q-4-12-16-12t-16 12v36z" fill="{hair}"/>'
    return (f'<path d="M{x-40} {y+260}v-60q0-44 40-44t40 44v60z" fill="{shirt}"/>'
            f'<circle cx="{x}" cy="{y+118}" r="26" fill="{s}"/>{h}'
            f'<circle cx="{x-9}" cy="{y+118}" r="3" fill="#222"/><circle cx="{x+9}" cy="{y+118}" r="3" fill="#222"/>'
            f'<path d="M{x-8} {y+130}q8 6 16 0" stroke="#222" stroke-width="2.5" fill="none"/>')


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
PICS['karte'] = ('<rect width="400" height="260" fill="#cfe8f3"/>'
                 '<path d="M30 20h210l10 70-60 20-70-10-90 20z" fill="#f2e2b8" stroke="#8a7a5a" stroke-width="2"/>'
                 '<path d="M30 120l90-20 70 10 60-20 130 10v80l-120 20-140-10-90 0z" fill="#fbd3d3" stroke="#c8102e" stroke-width="3"/>'
                 '<path d="M10 150l60-10 40 30-30 50-70-10z" fill="#e3edc8" stroke="#6d8a3a" stroke-width="2"/>'
                 + label(140, 60, 'Deutschland', 18) + label(250, 160, 'Österreich', 20, '#c8102e') + label(50, 200, 'Schweiz', 14)
                 + '<circle cx="345" cy="132" r="7" fill="#1f2937"/>' + label(345, 120, 'Wien', 15) + flag(300, 175, 'AT', 30))
# L03: city Graz (left) vs village St. Georgen (right), Maria and Lukas
PICS['wohnort'] = ('<rect x="0" y="210" width="400" height="50" fill="#c9b18e"/>'
                   '<g fill="#b8bec6"><rect x="20" y="90" width="40" height="120"/><rect x="66" y="60" width="44" height="150"/><rect x="116" y="110" width="40" height="100"/></g>'
                   '<g fill="#9ed8ff">' + ''.join(f'<rect x="{x}" y="{y}" width="10" height="12"/>' for x in (28, 44, 74, 92, 124, 140) for y in (120, 150, 180)) + '</g>'
                   + '<rect x="40" y="20" width="96" height="30" rx="4" fill="#fff" stroke="#1d4e89" stroke-width="3"/>' + label(88, 42, 'Graz', 18, '#1d4e89')
                   + house(230, 150, 50) + house(310, 160, 44, '#f2e2b8', '#7a4e2d')
                   + '<rect x="244" y="20" width="132" height="30" rx="4" fill="#ffd23f" stroke="#1f2937" stroke-width="2"/>' + label(310, 42, 'St. Georgen', 16)
                   + '<g transform="translate(64 116) scale(0.4)">' + person(60, '#c8102e', 'b', '#222', long=True) + '</g>'
                   + '<g transform="translate(350 120) scale(0.38)">' + person(60, '#1d4e89', 'a', '#7a4e2d') + '</g>'
                   + label(88, 236, 'Maria', 15, '#1f2937') + label(372, 236, 'Lukas', 15, '#1f2937'))
# L04: envelope with an address and an e-mail card
PICS['adresse'] = ('<rect x="30" y="40" width="250" height="160" rx="6" fill="#fff" stroke="#9ca3af" stroke-width="2"/>'
                   '<path d="M30 40l125 80 125-80" fill="none" stroke="#d1d5db" stroke-width="2"/>'
                   '<rect x="226" y="54" width="40" height="46" fill="#fde2e2" stroke="#c8102e" stroke-dasharray="3 2"/>'
                   + label(60, 140, 'Maria Santos', 16, anchor='start') + label(60, 162, 'Hauptstraße 12', 16, anchor='start', bold=False)
                   + label(60, 184, '8010 Graz', 16, anchor='start', bold=False)
                   + '<rect x="250" y="168" width="140" height="70" rx="8" fill="#e0ebf8" stroke="#1d4e89" stroke-width="2"/>'
                   + label(320, 192, 'E-Mail:', 13, '#1d4e89') + label(320, 214, 'maria.santos@gmx.at', 11, '#1f2937', bold=False))
# L05: three people say hello in their languages
PICS['sprachen'] = ''.join(person(x, c, sk, hr, y=20, long=lg) + label(x, 256, n, 14, '#fff') for x, c, sk, hr, n, lg in ((70, '#2a9d8f', 'a', '#7a4e2d', 'Anna', True), (200, '#1d4e89', 'b', '#222', 'Jose', False), (330, '#f77f00', 'a', '#4a2f1c', 'Emma', True))) \
    + bubble(14, 16, 112, 'Grüß Gott!', 16) + bubble(140, 16, 120, 'Kumusta!', 16) + bubble(276, 16, 112, 'Hello!', 16)
# L06: man talks fast, Ali does not understand
PICS['langsam'] = (person(100, '#34506b', 'a', '#7a4e2d') + person(300, '#c8102e', 'c', '#222')
                   + bubble(20, 20, 170, 'blablablablabla…', 15) + '<path d="M196 30h30M200 42h40M196 54h30" stroke="#f77f00" stroke-width="4" stroke-linecap="round"/>' + '<text x="300" y="70" font-size="44" font-weight="bold" fill="#f77f00" text-anchor="middle">?</text>'
                   + label(300, 236, 'Ali', 15, '#fff'))
# L07: Anna with an Austrian flag and a sign "Wien"
PICS['anna'] = (person(130, '#2a9d8f', 'a', '#7a4e2d', long=True) + label(130, 236, 'Anna', 15, '#fff') + flag(240, 60, 'AT', 90)
                + '<rect x="230" y="150" width="110" height="40" rx="6" fill="#1d4e89"/>' + label(285, 177, 'Wien', 22, '#fff'))
# L08: Jose says he speaks German and Tagalog
PICS['jose'] = person(110, '#1d4e89', 'b', '#222') + label(110, 236, 'Jose', 15, '#fff') + bubble(20, 22, 190, 'Ich wohne in Wien.', 16) + '<rect x="230" y="130" width="110" height="40" rx="6" fill="#1d4e89"/>' + label(285, 157, 'Wien', 22, '#fff')
# L09: three numbered pictures: 1 a country (map shape), 2 a street sign, 3 a person
PICS['nomen'] = ('<rect x="14" y="40" width="116" height="160" rx="10" fill="#fff"/><rect x="142" y="40" width="116" height="160" rx="10" fill="#fff"/><rect x="270" y="40" width="116" height="160" rx="10" fill="#fff"/>'
                 '<path d="M30 110l30-8 26 4 20-8 14 4v30l-40 8-50-4z" fill="#fbd3d3" stroke="#c8102e" stroke-width="2"/>' + label(72, 172, 'Österreich', 14)
                 + '<rect x="166" y="96" width="68" height="26" rx="3" fill="#1d4e89" stroke="#fff" stroke-width="2"/>' + label(200, 114, 'Hauptstraße', 10, '#fff') + '<rect x="197" y="122" width="6" height="50" fill="#6b7280"/>'
                 + '<g transform="translate(270 66) scale(0.55)">' + person(105, '#f77f00', 'a', '#4a2f1c') + '</g>'
                 + '<rect x="270" y="200" width="116" height="24" fill="#f3ead9"/>'
                 + ''.join(f'<circle cx="{cx}" cy="58" r="14" fill="#c8102e"/>' + label(cx, 64, str(k), 15, '#fff') for k, cx in ((1, 34), (2, 162), (3, 290))))
# L10: yellow town sign "Seedorf" with a few houses
PICS['moosbach'] = ('<rect y="200" width="400" height="60" fill="#8a8f98"/><path d="M0 200q100-30 200-12t200 0v12H0z" fill="#7cc36a"/>'
                   + house(220, 140, 50) + house(290, 150, 44, '#f2e2b8', '#7a4e2d') + house(345, 156, 38)
                   + '<rect x="96" y="140" width="8" height="64" fill="#6b7280"/><rect x="30" y="60" width="140" height="84" rx="4" fill="#fff" stroke="#1f2937" stroke-width="5"/>'
                   + label(100, 112, 'Moosbach', 26))
# L11: Maria with a map is looking for a street; sign shows another street
PICS['suchen'] = (person(110, '#c8102e', 'b', '#222', long=True) + label(110, 236, 'Maria', 15, '#fff')
                  + '<rect x="70" y="170" width="80" height="54" fill="#fff" stroke="#9ca3af"/><path d="M80 186h60M80 200h40M100 176v44" stroke="#7cc36a" stroke-width="3"/>'
                  + bubble(20, 20, 210, 'Wo ist die Bahnhofstraße?', 14)
                  + '<rect x="300" y="110" width="8" height="110" fill="#6b7280"/><rect x="250" y="80" width="120" height="32" rx="3" fill="#1d4e89" stroke="#fff" stroke-width="2"/>' + label(310, 102, 'Hauptstraße', 14, '#fff'))
# L12: panel 1 phone call ends, panel 2 two people part in the street
PICS['abschied'] = ('<rect x="10" y="10" width="185" height="240" rx="10" fill="#fff"/><rect x="205" y="10" width="185" height="240" rx="10" fill="#fff"/>'
                    + label(30, 40, '1', 22, '#c8102e') + label(225, 40, '2', 22, '#c8102e')
                    + '<rect x="80" y="70" width="46" height="84" rx="8" fill="#1f2937"/><rect x="86" y="80" width="34" height="60" rx="3" fill="#9ed8ff"/>'
                    + '<path d="M60 90q-12 20 0 40M48 82q-20 28 0 56" stroke="#34506b" stroke-width="3" fill="none"/>' + label(102, 190, '📞', 30)
                    + '<g transform="translate(215 40) scale(0.5)">' + person(100, '#2a9d8f', 'a', '#7a4e2d', long=True) + person(240, '#1d4e89', 'b', '#222') + '</g>'
)
# L13: Austria – Vienna, euro, EU flag
PICS['oesterreich'] = ('<path d="M20 110l90-20 70 10 60-20 130 10v80l-120 20-140-10-90 0z" fill="#fbd3d3" stroke="#c8102e" stroke-width="3"/>'
                       '<path d="M318 112l6 12 13 1-10 8 3 13-12-7-12 7 3-13-10-8 13-1z" fill="#c8102e"/>' + label(328, 168, 'Wien', 16)
                       + '<circle cx="80" cy="50" r="30" fill="#d9a441" stroke="#9aa0a6" stroke-width="8"/>' + label(80, 59, '€', 26, '#5b4a1c')
                       + flag(170, 26, 'EU', 60) + label(200, 82, 'EU', 13) + flag(290, 26, 'AT', 60) + label(170, 230, 'Österreich', 22, '#c8102e'))

for name, body in PICS.items():
    open(f'{OUT}{name}.svg', 'w').write(HEAD + body + '</svg>\n')
print(len(PICS), 'pictures')
