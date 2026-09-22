#!/usr/bin/env python3
"""Build GitHub-safe, responsive project panels using only Python's stdlib.

Run from any working directory:
    python scripts/build_project_panels.py

The scientific/geospatial motifs are illustrative, not measured results.
Every panel is a standalone SVG with text and geometry only: no scripts,
foreignObject, fonts, linked images, or other external dependencies.
"""

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "assets" / "profile-v2"

COLORS = {
    "cream": "#F5F4EE",
    "navy": "#102A43",
    "teal": "#087F8C",
    "lime": "#CEF2A2",
    "coral": "#F3A785",
    "lavender": "#DBDAF0",
    "muted": "#496173",
    "border": "#DEE3DC",
}

PROJECTS = [
    {
        "slug": "opengeoenrich",
        "title": "OpenGeoEnrich",
        "kind": "QGIS TOOL",
        "stack": "Python · QGIS Processing",
        "wide": [
            "Add population, land cover and infrastructure",
            "context to your QGIS layers.",
        ],
        "mobile": [
            "Population, land and infrastructure",
            "indicators inside QGIS.",
        ],
        "accent": "teal",
    },
    {
        "slug": "mapevidence",
        "title": "MapEvidence",
        "kind": "RESEARCH LIBRARY",
        "stack": "Python · NumPy · SciPy",
        "wide": [
            "Validate maps with area estimates, uncertainty",
            "and spatial cross-validation.",
        ],
        "mobile": [
            "Map validation, uncertainty",
            "and spatial cross-validation.",
        ],
        "accent": "lavender",
    },
    {
        "slug": "spatialdrought",
        "title": "spatialdrought",
        "kind": "CLIMATE ANALYTICS",
        "stack": "Python · NumPy · xarray",
        "wide": [
            "Calculate six drought indicators across",
            "gridded satellite and climate time series.",
        ],
        "mobile": [
            "Six drought indicators for gridded",
            "climate and satellite time series.",
        ],
        "accent": "coral",
    },
    {
        "slug": "rastertrend",
        "title": "RasterTrend",
        "kind": "QGIS TOOL",
        "stack": "Python · QGIS Processing",
        "wide": [
            "Map gradual change through time with",
            "Mann–Kendall tests and Sen’s slope.",
        ],
        "mobile": [
            "Mann–Kendall trend tests and",
            "Sen’s slope for raster stacks.",
        ],
        "accent": "lime",
    },
    {
        "slug": "trendshift",
        "title": "TrendShift",
        "kind": "QGIS TOOL",
        "stack": "Python · QGIS Processing",
        "wide": [
            "Find a candidate abrupt shift in raster time series.",
            "Map its timing, magnitude and direction.",
        ],
        "mobile": [
            "Find a candidate change point",
            "in every raster pixel.",
        ],
        "accent": "lavender",
    },
    {
        "slug": "alive",
        "title": "ALIVE",
        "kind": "DEMO MILESTONE",
        "stack": "TypeScript · React · MSW",
        "wide": [
            "Rewind a demo, branch its timeline and",
            "compare alternative simulated futures.",
        ],
        "mobile": [
            "Rewind, branch and compare",
            "alternative simulated futures.",
        ],
        "accent": "coral",
    },
]


def text(x, y, value, size, fill="navy", weight=400, **attrs):
    """Escape text and attributes, keeping SVG text accessible and selectable."""
    extra = " ".join(
        f'{key.replace("_", "-")}="{escape(str(value), quote=True)}"'
        for key, value in attrs.items()
    )
    return (
        f'<text x="{x}" y="{y}" font-size="{size}" '
        f'font-weight="{weight}" fill="{COLORS.get(fill, fill)}" {extra}>'
        f'{escape(value)}</text>'
    )


def motif(slug):
    """Return hand-drawn abstract geometry in a 280 × 220 coordinate frame."""
    n, t = COLORS["navy"], COLORS["teal"]
    lime, coral, lav = COLORS["lime"], COLORS["coral"], COLORS["lavender"]
    if slug == "opengeoenrich":
        return f'''
<path d="M21 63 101 28 184 48 264 15V164L184 200 100 180 21 214Z" fill="#E4EBE4"/>
<path d="M101 28V180M184 48V200" fill="none" stroke="{n}" stroke-opacity=".12" stroke-width="2"/>
<path d="M25 164C72 129 60 103 111 111S185 160 261 77" fill="none" stroke="{t}" stroke-opacity=".24" stroke-width="18"/>
<path d="M30 100 99 73 169 105 237 53M65 185 99 73M169 105 205 166M99 73 205 166" fill="none" stroke="{n}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="99" cy="73" r="15" fill="{t}"/><circle cx="99" cy="73" r="5" fill="{lime}"/>
<circle cx="169" cy="105" r="11" fill="{n}"/><circle cx="237" cy="53" r="9" fill="{coral}"/>
<circle cx="65" cy="185" r="9" fill="{t}"/><circle cx="205" cy="166" r="12" fill="{lime}" stroke="{n}" stroke-width="2.5"/>
'''
    if slug == "mapevidence":
        cells = []
        for row in range(4):
            for col in range(5):
                color = [lav, "#E6E9E6", "#E6E9E6", lime][(row + col * 2) % 4]
                cells.append(
                    f'<rect x="{18 + col * 46}" y="{19 + row * 46}" '
                    f'width="40" height="40" rx="7" fill="{color}"/>'
                )
        return "".join(cells) + f'''
<path d="M41 89 87 135 179 43" fill="none" stroke="{n}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="41" cy="89" r="7" fill="{t}"/><circle cx="87" cy="135" r="7" fill="{t}"/><circle cx="179" cy="43" r="7" fill="{t}"/>
<circle cx="207" cy="159" r="39" fill="{n}"/>
<path d="M189 158 202 171 226 145" fill="none" stroke="{lime}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
'''
    if slug == "spatialdrought":
        return f'''
<rect x="18" y="20" width="244" height="180" rx="20" fill="#E7EAD7"/>
<path d="M18 112C58 50 89 119 130 73S211 74 262 35V200H18Z" fill="{lime}"/>
<path d="M18 143C63 87 87 150 135 108S204 97 262 66V200H18Z" fill="#BACFC0"/>
<path d="M18 176C58 113 100 183 140 137S215 130 262 100V200H18Z" fill="{coral}"/>
<path d="M40 174C83 126 106 194 148 156S214 153 241 128" fill="none" stroke="{n}" stroke-width="2.5" stroke-linecap="round"/>
<path d="M45 65C85 40 103 72 135 49M49 96C86 64 102 102 142 75M163 105C185 94 203 102 229 87" fill="none" stroke="{n}" stroke-opacity=".25" stroke-width="2" stroke-linecap="round"/>
<circle cx="223" cy="41" r="24" fill="{n}"/>
<path d="M223 26C218 33 213 38 213 44A10 10 0 0 0 233 44C233 38 228 33 223 26Z" fill="{coral}"/>
'''
    if slug == "rastertrend":
        return f'''
<rect x="18" y="20" width="244" height="180" rx="20" fill="#E7EBDD"/>
<path d="M42 62H239M42 105H239M42 148H239" stroke="{n}" stroke-opacity=".1" stroke-width="1.5"/>
<path d="M43 178 68 150 94 159 118 120 144 130 169 91 194 102 238 51V182H43Z" fill="{lime}"/>
<path d="M43 178 68 150 94 159 118 120 144 130 169 91 194 102 238 51" fill="none" stroke="{t}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M44 169 238 55" fill="none" stroke="{n}" stroke-width="2" stroke-dasharray="5 7"/>
<circle cx="118" cy="120" r="6" fill="{n}"/><circle cx="238" cy="51" r="9" fill="{n}"/>
<circle cx="49" cy="47" r="21" fill="{n}"/>
<path d="M41 53 56 39M44 39H56V51" fill="none" stroke="{lime}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
'''
    if slug == "trendshift":
        return f'''
<rect x="18" y="20" width="244" height="180" rx="20" fill="#E8E7EC"/>
<path d="M142 20H242Q262 20 262 40V180Q262 200 242 200H142Z" fill="{lav}"/>
<path d="M41 62H238M41 106H238M41 150H238" stroke="{n}" stroke-opacity=".1" stroke-width="1.5"/>
<path d="M142 35V185" stroke="{n}" stroke-opacity=".45" stroke-width="2" stroke-dasharray="5 7"/>
<path d="M41 154 65 145 92 156 119 146 139 151 147 75 169 63 191 73 215 61 239 67" fill="none" stroke="{t}" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M40 169H128V90H238" fill="none" stroke="{n}" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
<circle cx="146" cy="75" r="10" fill="{n}"/><circle cx="146" cy="75" r="4" fill="{lime}"/>
'''
    if slug == "alive":
        return f'''
<rect x="18" y="20" width="244" height="180" rx="20" fill="#ECE7E0"/>
<path d="M40 111H104C140 111 134 55 178 55H237M104 111C148 111 137 165 181 165H237" fill="none" stroke="{n}" stroke-width="3.5" stroke-linecap="round"/>
<path d="M104 111H237" fill="none" stroke="{t}" stroke-width="2.5" stroke-dasharray="5 8" stroke-linecap="round"/>
<circle cx="40" cy="111" r="8" fill="{n}"/>
<circle cx="104" cy="111" r="17" fill="{n}"/><circle cx="104" cy="111" r="6" fill="{lime}"/>
<circle cx="235" cy="55" r="17" fill="{t}"/>
<circle cx="235" cy="111" r="9" fill="{lav}" stroke="{n}" stroke-width="2"/>
<circle cx="235" cy="165" r="17" fill="{coral}"/>
<path d="M63 49A21 21 0 1 1 49 84M51 38 63 49 50 58" fill="none" stroke="{n}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
'''
    raise ValueError(f"Unknown motif: {slug}")


def render(project, number, mobile=False):
    width, height = (640, 440) if mobile else (1200, 300)
    title_size, body_size = (46, 27) if mobile else (48, 26)
    title_y, body_y = (110, 158) if mobile else (111, 160)
    content = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
        f'height="{height}" viewBox="0 0 {width} {height}" role="img" '
        'aria-labelledby="title desc">',
        f'<title id="title">{escape(project["title"])}</title>',
        '<desc id="desc">'
        + escape(f'{project["kind"]}. {" ".join(project["wide"])} '
                 'Decorative motif is illustrative, not measured data.')
        + '</desc>',
        f'<rect x="1" y="1" width="{width - 2}" height="{height - 2}" '
        f'rx="22" fill="{COLORS["cream"]}" stroke="{COLORS["border"]}"/>',
        '<g font-family="Arial, Helvetica, sans-serif">',
        text(42, 47, f'{number:02d}  /  {project["kind"]}', 18,
             fill="teal", weight=700, letter_spacing="2"),
        text(40, title_y, project["title"], title_size,
             weight=700, letter_spacing="-1.5"),
    ]
    for i, line in enumerate(project["mobile" if mobile else "wide"]):
        content.append(text(42, body_y + i * 34, line, body_size, fill="muted"))

    if mobile:
        content += [
            text(42, 252, project["stack"], 20, fill="muted"),
            f'<path d="M42 287H113" stroke="{COLORS[project["accent"]]}" '
            'stroke-width="5" stroke-linecap="round"/>',
            '<g transform="translate(383 238) scale(.79)">',
            motif(project["slug"]),
            '</g>',
            text(42, 379, "Explore repository", 23, weight=700),
            f'<path d="M43 402H86M78 394 86 402 78 410" '
            f'fill="none" stroke="{COLORS["teal"]}" stroke-width="2.5" '
            'stroke-linecap="round" stroke-linejoin="round"/>',
        ]
    else:
        content += [
            text(42, 258, project["stack"], 19, fill="muted"),
            text(577, 258, "Explore repository", 21, weight=700),
            f'<path d="M773 251H809M801 243 809 251 801 259" '
            f'fill="none" stroke="{COLORS["teal"]}" stroke-width="2.5" '
            'stroke-linecap="round" stroke-linejoin="round"/>',
            '<g transform="translate(866 40)">',
            motif(project["slug"]),
            '</g>',
        ]
    content += ['</g>', '</svg>']
    return "\n".join(content) + "\n"


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for number, project in enumerate(PROJECTS, start=1):
        for variant, mobile in (("wide", False), ("mobile", True)):
            path = OUTPUT / f'{project["slug"]}-{variant}.svg'
            path.write_text(render(project, number, mobile), encoding="utf-8")
            print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
