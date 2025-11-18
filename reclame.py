# reclame.py
from algemene_functies import mijn_functie_2

def _format_money(m):
    """Helper: toon m netjes: zonder decimalen als het een geheel getal is, anders met 2 decimalen.
       Gebruik komma als decimaalscheiding omdat voorbeelden Nederlands gebruiken."""
    if isinstance(m, (int,)) or (isinstance(m, float) and m.is_integer()):
        return str(int(m))
    else:
        # twee decimalen, en vervang . door ,
        return f"{m:.2f}".replace('.', ',')


def aanbieding_1(smaak, prijs, korting):
    """
    Params: smaak (str), prijs (float of int), korting (float, bv 0.1 voor 10%)
    Return: precies de gevraagde zin, bijvoorbeeld:
    "Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak aardbei, van 4 euro voor 3,60 euro."
    """
    nieuw_prijs = prijs * (1 - korting)
    # prijs origineel: toon als geheel wanneer mogelijk
    origineel = _format_money(prijs)
    nieuw = _format_money(round(nieuw_prijs, 2))
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {origineel} euro voor {nieuw} euro."


def inkomsten_totaal(inkomsten, btw=0.0):
    """
    inkomsten: lijst met 7 getallen (inkomsten per dag)
    btw: float zoals 0.09 (9%)
    Geeft string terug:
      "Het totaal van alle inkomsten van deze week is <totaal> euro, waarover <bedrag> euro btw betaald dient te worden."
    """
    totaal = sum(inkomsten)
    btw_bedrag = round(totaal * btw, 2)

    # nette weergave: geen decimalen als geheel getal, anders 2 decimalen met komma
    def _fmt(x):
        if isinstance(x, (int,)) or (isinstance(x, float) and float(x).is_integer()):
            return str(int(x))
        return f"{x:.2f}".replace('.', ',')

    return (f"Het totaal van alle inkomsten van deze week is {_fmt(totaal)} euro, "
            f"waarover {_fmt(btw_bedrag)} euro btw betaald dient te worden.")


def laag_en_hoog(mijn_lijst):
    """
    Geeft lijst [hoogste, laagste] terug.
    Gebruik makend van max() en min().
    """
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return [hoogste, laagste]


def gemiddelde(mijn_lijst):
    """
    Geeft string terug:
      "De gemiddelde inkomsten deze week zijn <bedrag> euro."
    """
    total = sum(mijn_lijst)
    avg = total / len(mijn_lijst)
    # toon netjes: twee decimalen als nodig, anders geen decimalen
    if float(avg).is_integer():
        avg_str = str(int(avg))
    else:
        avg_str = f"{avg:.2f}".replace('.', ',')
    return f"De gemiddelde inkomsten deze week zijn {avg_str} euro."


def meervoudig(invoer_lijst):
    """
    Verwacht een lijst van 5-10 integers. Gebruikt laag_en_hoog() en retourneert die lijst.
    """
    return laag_en_hoog(invoer_lijst)


def combinatie(invoer_lijst_2):
    """
    Roept laag_en_hoog() aan en gebruikt de retourwaarde als argument voor mijn_functie_2.
    Volgens instructie: korte_lijst = laag_en_hoog(...); resultaat = mijn_functie_2(korte_lijst)
    """
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    # mijn_functie_2 verwacht een iterable met twee getallen of losse arguments.
    return mijn_functie_2(korte_lijst)
