import fontforge

# Open the source font
font = fontforge.open('DejaVuSans.ttf')

# Define anchor points for consonants and vowels
def add_anchor_points(glyph, anchors):
    for name, x, y in anchors:
        glyph.addAnchorPoint(name, "base" if "base" in name else "mark", x, y)

# Define the consonant and vowel glyphs
consonants = {
    'K': 'K',
    'G': 'G',
    'NG': 'NG',
    'CH': 'CH',
    'J': 'J',
    'T': 'T',
    'TH': 'TH',
    'D': 'D',
    'N': 'N',
    'P': 'P',
    'B': 'B',
    'F': 'F',
    'M': 'M',
    'Y': 'Y',
    'R': 'R',
    'L': 'L',
    'V': 'V',
    'S': 'S',
    'Z': 'Z',
    'SH': 'SH',
    'ZH': 'ZH'
}

vowels = {
    'IY': 'EE',
    'IH': 'I',
    'EY': 'EI',
    'EH': 'E',
    'AE': 'AE',
    'AA': 'AW',
    'AO': 'AW',
    'OW': 'OA',
    'UH': 'Ø',
    'UW': 'O',
    'AH': 'U',
    'AY': 'AI',
    'AW': 'OW',
    'OY': 'OY'
}

# Add anchor points to consonants
consonant_anchors = [
    ("base", 300, 0),
    ("top", 300, 800)
]

for con in consonants.values():
    glyph = font[con]
    add_anchor_points(glyph, consonant_anchors)

# Add anchor points to vowels
vowel_anchors = [
    ("top", 300, 0)
]

for vow in vowels.values():
    glyph = font[vow]
    add_anchor_points(glyph, vowel_anchors)

# Create OpenType features
font.addLookup("mark", "gpos_mark2base", None, (("mark", [["latn", ["dflt"]]]),))
font.addLookupSubtable("mark", "mark1")

# Position vowels above consonants
for con in consonants.values():
    for vow in vowels.values():
        font[con].addAnchorClass("mark1", "base", "top", "mark", "top")

# Generate the new font
font.generate('VJScript.otf')
font.close()

