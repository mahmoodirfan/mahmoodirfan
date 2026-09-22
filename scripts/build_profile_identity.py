#!/usr/bin/env python3
"""Rebuild the profile's self-contained SVG identity; Python standard library only."""
from pathlib import Path
from html import escape
import math

OUT = Path(__file__).resolve().parents[1] / 'assets' / 'profile-v2'
OUT.mkdir(parents=True, exist_ok=True)
NAVY, TEAL, LIME, CORAL, CREAM = '#102A43', '#087F8C', '#CEF2A2', '#F3A785', '#F5F4EE'


def text(x, y, words, size=24, color=NAVY, weight=400, extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" {extra}>{escape(words)}</text>'


def svg(name, w, h, body, title, bg=NAVY):
    markup = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title">
<title id="title">{escape(title)}</title>
<rect width="{w}" height="{h}" rx="24" fill="{bg}"/>
<g font-family="Arial, Helvetica, sans-serif">{body}</g>
</svg>\n'''
    (OUT / name).write_text(markup, encoding='utf-8')


def globe(cx, cy, r):
    out = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#163D53" stroke="#598E95" stroke-width="1.3"/>'
    out += f'<g fill="none" stroke="#598E95" stroke-width="1" opacity=".6">'
    for d in [.3, .62]:
        out += f'<ellipse cx="{cx}" cy="{cy}" rx="{r*d}" ry="{r}"/>'
    for d in [-.65, -.32, 0, .32, .65]:
        y = cy + d*r
        a = r * math.sqrt(1-d*d)
        out += f'<path d="M {cx-a} {y} Q {cx} {y+r*.23*(1-abs(d))} {cx+a} {y}"/>'
    out += f'<path d="M{cx} {cy-r}V{cy+r}"/></g>'
    out += f'<ellipse cx="{cx}" cy="{cy}" rx="{r*1.31}" ry="{r*.36}" transform="rotate(-32 {cx} {cy})" fill="none" stroke="{LIME}" stroke-width="2"/>'
    out += f'<circle cx="{cx+r*1.08}" cy="{cy-r*.52}" r="7" fill="{LIME}"/>'
    out += f'<circle cx="{cx-r*.86}" cy="{cy+r*.69}" r="5" fill="{CORAL}"/>'
    out += f'<circle cx="{cx}" cy="{cy}" r="{r*1.45}" fill="none" stroke="#416377" stroke-dasharray="2 12"/>'
    return out


def hero(mobile=False):
    w,h = (640,740) if mobile else (1200,560)
    out = '<rect x="34" y="34" width="44" height="44" rx="12" fill="#CEF2A2"/>'
    out += text(43,64,'IM',23,NAVY,700)
    out += text(95,63,'IRFAN MAHMOOD',20,CREAM,700,'letter-spacing="2"')
    if mobile:
        out += text(36,125,'REMOTE SENSING  /  GIS  /  SOFTWARE',19,'#ACC7CE',600)
        out += text(32,213,'Earth data.',68,CREAM,700,'letter-spacing="-3"')
        out += text(32,292,'Real-world',68,LIME,700,'letter-spacing="-3"')
        out += text(32,371,'impact.',68,LIME,700,'letter-spacing="-3"')
        out += text(36,427,'From satellite observations',27,'#DBE8EA')
        out += text(36,465,'to science and useful software.',27,'#DBE8EA')
        out += globe(450,593,66)
        out += text(36,557,'OBSERVE.',24,CREAM,700)
        out += text(36,595,'UNDERSTAND.',24,CREAM,700)
        out += text(36,633,'BUILD.',24,CREAM,700)
        out += '<path d="M36 690H604" stroke="#365064"/>'
        out += text(36,722,'LAND  /  OCEAN  /  ATMOSPHERE',19,'#ACC7CE',600,'letter-spacing="1"')
    else:
        out += text(803,62,'EARTH OBSERVATION & DEVELOPMENT',16,'#ACC7CE',500,'letter-spacing="1"')
        out += text(44,143,'REMOTE SENSING  /  GIS  /  SOFTWARE',18,'#ACC7CE',600,'letter-spacing="2"')
        out += text(39,245,'Earth data.',82,CREAM,700,'letter-spacing="-4"')
        out += text(39,337,'Real-world impact.',82,LIME,700,'letter-spacing="-4"')
        out += text(44,397,'From satellite observations to science and useful software.',25,'#DBE8EA')
        out += globe(956,276,128)
        out += '<path d="M44 471H1156" stroke="#365064"/>'
        out += text(44,520,'LAND  /  OCEAN  /  ATMOSPHERE',19,'#ACC7CE',600,'letter-spacing="2"')
        out += text(785,520,'OBSERVE. UNDERSTAND. BUILD.',18,CREAM,700,'letter-spacing="1"')
    svg('hero-mobile.svg' if mobile else 'hero-wide.svg',w,h,out,'Irfan Mahmood. Earth data. Real-world impact. Remote sensing, GIS and software.')


def contact(mobile=False):
    w,h=(640,310) if mobile else (1200,220)
    out=text(36,51,'RESEARCH  /  CONSULTANCY  /  DEVELOPMENT',17,'#54706E',700,'letter-spacing="1"')
    if mobile:
        out+=text(32,121,'Let’s build',48,NAVY,700,'letter-spacing="-1.5"')
        out+=text(32,180,'something useful.',48,NAVY,700,'letter-spacing="-1.5"')
        out+=text(36,261,'GET IN TOUCH',21,TEAL,700,'letter-spacing="2"')
        out+='<path d="M530 240L552 262L530 284M504 262H552" fill="none" stroke="#087F8C" stroke-width="3"/>'
    else:
        out+=text(32,127,'Let’s build something useful.',55,NAVY,700,'letter-spacing="-2"')
        out+=text(36,183,'Geospatial ideas. Research collaborations. Working tools.',25,'#54706E')
        out+='<circle cx="1094" cy="116" r="49" fill="#087F8C"/><path d="M1077 99L1111 133M1084 133H1111V106" fill="none" stroke="white" stroke-width="3" transform="rotate(-90 1094 116)"/>'
    svg('contact-mobile.svg' if mobile else 'contact-wide.svg',w,h,out,'Let’s build something useful. Research, consultancy and geospatial development.','#E4EFDF')


if __name__ == '__main__':
    for compact in [False,True]:
        hero(compact)
        contact(compact)
    print(f'Wrote 4 profile identity assets to {OUT}')
