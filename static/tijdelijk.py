prijzen = {
    'aardbei': 3,
    'vanille': 4,
    'chocholade': 5
}



aanbieding = prijzen['aardbei'] * 8


reclame_teskt = f"vandaag in aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"

reclame_teskt2 = reclame_teskt[:62]

reclame_teskt3 = reclame_teskt2.upper()

reclame_teskt4 = reclame_teskt3.split()


for el in reclame_teskt4:
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el.lower())
        