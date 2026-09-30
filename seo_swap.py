"""
SEO swap: Ramsey, MN → Twin Cities, MN in build.py and build_pages.py
Preserves physical address strings and schema addressLocality.
"""
import re

KEEP = [
    '6650 US-10, Ramsey, MN 55303',
    'q=6650+US-10,+Ramsey,+MN+55303',
    '"addressLocality": "Ramsey"',
    "'addressLocality': 'Ramsey'",
    'addressLocality": "Ramsey',
    '    "addressLocality": "Ramsey",',
]

# Ordered list of (find, replace) — most specific first
SWAPS = [
    # Page titles
    ('Ramsey, MN Since 2010',       'Twin Cities, MN Since 2010'),
    ('Ramsey, MN | ',               'Twin Cities, MN | '),
    (' \u2014 Ramsey, MN',          ' \u2014 Twin Cities, MN'),
    (', Ramsey MN"',                ', Twin Cities MN"'),
    ('| Ramsey, MN"',               '| Twin Cities, MN"'),
    # Meta descriptions / body copy
    ('in Ramsey, MN.',              'in the Twin Cities.'),
    ('in Ramsey, MN.',              'in the Twin Cities.'),
    ('in Ramsey, MN,',              'in the Twin Cities,'),
    ('in Ramsey, MN ',              'in the Twin Cities '),
    ('in Ramsey, Minnesota.',       'in the Twin Cities.'),
    ('in Ramsey, Minnesota.',       'in the Twin Cities.'),
    ('in Ramsey.',                  'in the Twin Cities.'),
    ('Ramsey Minnesota\'s trusted', "the Twin Cities' trusted"),
    ("Ramsey Minnesota's trusted",  "the Twin Cities' trusted"),
    # Nav / footer / labels
    ('Licensed FFL Dealer &middot; Ramsey, MN', 'Licensed FFL Dealer &middot; Twin Cities, MN'),
    ('Join our team in Ramsey, MN', 'Join our team in the Twin Cities'),
    # Headings / copy
    ('Buy Firearms Online &mdash; Ramsey, MN', 'Buy Firearms Online &mdash; Twin Cities, MN'),
    ('A Ramsey fixture since 2010, proudly serving the Twin Cities community.', 'A Twin Cities fixture since 2010, proudly serving the metro community.'),
    ('A Ramsey fixture since 2010',  'A Twin Cities fixture since 2010'),
    ('a Ramsey fixture since 2010',  'a Twin Cities fixture since 2010'),
    ('our Ramsey crew',              'our Twin Cities crew'),
    ('our Ramsey location on US-10', 'our Twin Cities location on US-10'),
    ('Visit our Ramsey store on US-10', 'Visit us on US-10 in the Twin Cities'),
    ('Ramsey, MN &middot; Since 2010', 'Twin Cities, MN &middot; Since 2010'),
    ('Stop by our Ramsey location on US-10', 'Stop by our Twin Cities location on US-10'),
    # Alt text patterns
    ('in Ramsey, MN"',              'in the Twin Cities"'),
    ('Ramsey MN"',                  'Twin Cities, MN"'),
    ('in Ramsey MN"',               'in the Twin Cities"'),
    # Keywords
    ('pawn shop Ramsey MN',         'pawn shop Twin Cities MN'),
    ('gun store Ramsey MN',         'gun store Twin Cities MN'),
    ('gun store Ramsey,',           'gun store Twin Cities,'),
    ('pawn loans Ramsey',           'pawn loans Twin Cities'),
    ('buy guns Ramsey',             'buy guns Twin Cities'),
    ('handguns Ramsey',             'handguns Twin Cities MN'),
    ('guns for sale Ramsey MN',     'guns for sale Twin Cities MN'),
    ('ammunition Ramsey MN',        'ammunition Twin Cities MN'),
    ('gold buyer Ramsey',           'gold buyer Twin Cities'),
    ('sell jewelry Ramsey',         'sell jewelry Twin Cities'),
    ('firearms dealer contact Minnesota', 'firearms dealer contact Twin Cities'),
    ('pawn shop directions Ramsey', 'pawn shop directions Twin Cities'),
    ('gun store Ramsey MN phone',   'gun store Twin Cities MN phone'),
    ('gun store history Ramsey MN', 'gun store history Twin Cities MN'),
    ('about Twin Cities Pawn',      'about Twin Cities Gun and Pawn'),
    # Geo meta
    ('content="Ramsey, Minnesota"', 'content="Twin Cities, Minnesota"'),
    ('in Ramsey, Minnesota"',       'in the Twin Cities, Minnesota"'),
    ('storefront in Ramsey, Minnesota"', 'storefront in the Twin Cities, Minnesota"'),
    # Misc body copy
    ('at Twin Cities Gun &amp; Pawn in Ramsey, Minnesota.', 'at Twin Cities Gun &amp; Pawn in the Twin Cities, Minnesota.'),
    ('visit us in Ramsey.)',        'visit us in the Twin Cities.)'),
    ('visit us in Ramsey.',         'visit us in the Twin Cities.'),
    ('visit us in Ramsey',          'visit us in the Twin Cities'),
    # Hidden SEO geo block
    ('Ramsey, Minnesota (MN) &middot; Twin Cities &middot; Minneapolis',
     'Twin Cities, Minnesota (MN) &middot; Minneapolis'),
    # FAQ answer - keep the address but update descriptor
    ('We\'re at 6650 US-10, Ramsey, MN 55303, conveniently serving the Minneapolis\u2013St. Paul metro area.',
     'We\'re located at 6650 US-10 in Ramsey (Twin Cities metro), conveniently serving Minneapolis\u2013St. Paul.'),
]

def safe_replace(text, find, replace, keep_list):
    """Replace all occurrences of find→replace, but skip lines that contain a keep string."""
    lines = text.split('\n')
    result = []
    for line in lines:
        if find in line:
            skip = any(k in line for k in keep_list)
            if skip:
                result.append(line)
            else:
                result.append(line.replace(find, replace))
        else:
            result.append(line)
    return '\n'.join(result)

for fname in ['build.py', 'build_pages.py']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    original = text
    for find, replace in SWAPS:
        text = safe_replace(text, find, replace, KEEP)
    if text != original:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Updated: {fname}")
    else:
        print(f"No changes: {fname}")

print("Done.")
