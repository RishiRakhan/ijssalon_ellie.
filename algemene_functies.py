# algemene_functies.py

def mijn_functie_1(x):
    """
    Verwacht één getal x en geeft x goed verwerkt terug.
    Volgens de tabel is de bewerking: teruggeven van x**2.
    Voorbeelden:
      2 -> 4, 4 -> 16, 10 -> 100, 12 -> 144
    """
    return x * x


def mijn_functie_2(a_b):
    """
    Verwacht twee argumenten (of een iterabele met twee getallen).
    Volgens de tabel moeten we van (a, b) een lijst teruggeven:
      [a + b, a - b, a * b, a / b]
    We geven de deling als geheel getal terug wanneer dat kan (zoals in de voorbeelden).
    a_b kan een tuple/list of twee afzonderlijke arguments zijn; we ondersteunen beide.
    """
    # toestaan dat de gebruiker twee losse arguments geeft of één iterable
    if isinstance(a_b, (list, tuple)) and len(a_b) == 2:
        a, b = a_b
    else:
        # als men per ongeluk twee losse arguments stuurt (niet verwacht volgens opdracht),
        # proberen we daar ook mee om te gaan:
        try:
            a, b = a_b
        except Exception:
            raise TypeError("mijn_functie_2 verwacht twee getallen (a, b) of een lijst/tuple van twee getallen.")

    # basisbewerkingen
    plus = a + b
    min_ = a - b
    maal = a * b

    # gebruik integer deling als het exact deelbaar is, anders floatafhandeling
    if b == 0:
        raise ZeroDivisionError("Deling door nul is niet toegestaan.")
    if a % b == 0:
        deel = a // b
    else:
        deel = a / b

    return [plus, min_, maal, deel]
