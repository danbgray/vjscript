import fontforge

# Open the source font
font = fontforge.open('DejaVuSans.ttf')

# Correct the Unicode mapping for Omega
if 'Omega' in font:
    font['Omega'].unicode = 0x2126

# Remove the 'kern' table to avoid conflicts with 'GPOS'
if 'kern' in font:
    font.removeLookup('kern')

# Ensure no 'use-my-metrics' flag issues
for glyph in font.glyphs():
    glyph.unlinkRef()  # Clear any references to other glyphs

# Define anchor points for consonants and vowels
def add_anchor_points(glyph, anchors):
    for name, x, y in anchors:
        glyph.addAnchorPoint(name, "base" if "base" in name else "mark", x, y)

# Define the consonant and vowel glyphs
consonants = {
    'K': 'K',
    'G': 'G',
    'NG': 'eng',  # Typically, 'eng' is used for 'ng' in fonts
    'CH': 'C',  # Adjusted to a common glyph, replace as necessary
    'J': 'J',
    'T': 'T',
    'TH': 'Thorn',  # 'Thorn' is the common glyph for 'th', adjust as necessary
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
    'SH': 'S',  # Adjusted to a common glyph, replace as necessary
    'ZH': 'Z'  # Adjusted to a common glyph, replace as necessary
}

vowels = {
    'IY': 'I',
    'IH': 'I',
    'EY': 'E',
    'EH': 'E',
    'AE': 'A',
    'AA': 'A',
    'AO': 'O',
    'OW': 'O',
    'UH': 'U',
    'UW': 'U',
    'AH': 'A',
    'AY': 'A',
    'AW': 'A',
    'OY': 'O'
}

# Add anchor points to consonants
consonant_anchors = [
    ("top", 300, 800),
    ("bottom", 300, 0)
]

for con in consonants.values():
    if con in font:
        glyph = font[con]
        add_anchor_points(glyph, consonant_anchors)

# Add anchor points to vowels
vowel_anchors = [
    ("top", 300, 0)
]

for vow in vowels.values():
    if vow in font:
        glyph = font[vow]
        add_anchor_points(glyph, vowel_anchors)

# Create OpenType features
font.addLookup("gpos_mark", "gpos_mark2base", None, (("mark", (("latn", ("dflt")),)),))
font.addLookupSubtable("gpos_mark", "mark2base")

for con in consonants.values():
    if con in font:
        base_glyph = font[con]
        for vow in vowels.values():
            if vow in font:
                mark_glyph = font[vow]
                base_glyph.addAnchorPoint("top", "base", 300, 800)
                mark_glyph.addAnchorPoint("top", "mark", 300, 0)

# Save the font with the applied features
font.save("VJScript.sfd")

# Generate the new font
font.generate('VJScript.otf')
font.close()
