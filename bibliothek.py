buecher = {
    "9780131101630": {"titel":"The C Programming Language","autor":"Kernighan & Ritchie","jahr":1988,"seiten":272,"preis_eur":36.99},
    "9781491957660": {"titel":"Python for Data Analysis","autor":"Wes McKinney","jahr":2017,"seiten":547,"preis_eur":42.50},
    "9780132350884": {"titel":"Clean Code","autor":"Robert C. Martin","jahr":2008,"seiten":464,"preis_eur":43.79},
    "9780262033848": {"titel":"Introduction to Algorithms","autor":"Cormen et al.","jahr":2009,"seiten":1312,"preis_eur":129.99},
    "9780201616224": {"titel":"The Pragmatic Programmer","autor":"Hunt & Thomas","jahr":1999,"seiten":352,"preis_eur":39.90},
    "9780134685991": {"titel":"Effective Java","autor":"Joshua Bloch","jahr":2018,"seiten":416,"preis_eur":54.90},
    "9781491903995": {"titel":"Fluent Python","autor":"Luciano Ramalho","jahr":2015,"seiten":792,"preis_eur":54.00},
    "9781593279929": {"titel":"Automate the Boring Stuff","autor":"Al Sweigart","jahr":2019,"seiten":504,"preis_eur":35.00},
    "9781492056355": {"titel":"Designing Data-Intensive Applications","autor":"Martin Kleppmann","jahr":2017,"seiten":616,"preis_eur":49.90},
    "9780134494166": {"titel":"Clean Architecture","autor":"Robert C. Martin","jahr":2017,"seiten":432,"preis_eur":45.00},
    "9780132354183": {"titel":"Code Complete","autor":"Steve McConnell","jahr":2004,"seiten":960,"preis_eur":55.00},
    "9780137903955": {"titel":"Patterns of Enterprise Application Architecture","autor":"Martin Fowler","jahr":2002,"seiten":533,"preis_eur":48.50},
     "9780201485677": {"titel":"Refactoring","autor":"Martin Fowler","jahr":1999,"seiten":431,"preis_eur":45.00},
    "9780137081073": {"titel":"The Clean Coder","autor":"Robert C. Martin","jahr":2011,"seiten":256,"preis_eur":38.90},
    "9781491946008": {"titel":"Learning Python","autor":"Mark Lutz","jahr":2013,"seiten":1648,"preis_eur":68.00},
    "9780262035613": {"titel":"Structure and Interpretation of Computer Programs","autor":"Sussman & Abelson","jahr":1996,"seiten":657,"preis_eur":59.99},
    "9780261103573": {"titel":"The Mythical Man-Month","autor":"Frederick P. Brooks Jr.","jahr":1995,"seiten":336,"preis_eur":32.50},
    "9780131177055": {"titel":"Design Patterns","autor":"Gamma et al.","jahr":1994,"seiten":395,"preis_eur":47.00}
}

def ausgabe_suche(isbn, buch):
    print(10 * "\n")
    print(f"ISBN                    :  {isbn}")
    print(f"Titel                   :  {buch['titel']}")
    print(f"Autor                   :  {buch['autor']}")
    print(f"Preis                   :  {buch['preis_eur']} €")
    print(f"Erscheinungsjahr        :  {buch['jahr']}")
    print(f"Seiten                  :  {buch['seiten']}")
    print(5 * "\n")

def suche_buecher(buecher):
    gesuch = int(input(
        "Womit möchtest du dein Buch suchen?: \n"
        "1. ISBN\n"
        "2. Titel\n"
        "3. Autor\n"))

    if gesuch == 1:
        isbn = input("Bitte die 13-stellige ISBN eingeben:\n").strip()
        if isbn in buecher:
            buch = buecher[isbn]
            ausgabe_suche(isbn, buch)
            return isbn, buch
        else:
            print(f"ISBN '{isbn}' nicht gefunden.\n")
            return None, None

    elif gesuch == 2:
        titel_origin = input("Bitte gib den Titel ein:\n")
        titel = titel_origin.strip().lower()
        gefunden = False

        for isbn, buch in buecher.items():
            if buch["titel"].lower() == titel:
                ausgabe_suche(isbn, buch)
                gefunden = True
                return isbn, buch
                break

        if not gefunden:
            print(f"Titel '{titel_origin}' nicht gefunden.\n")
            return None, None

    elif gesuch == 3:
        autor_origin = input("Bitte gib den Autor ein:\n")
        autor = autor_origin.strip().lower()
        gefunden = False

        for isbn, buch in buecher.items():
            if buch["autor"].lower() == autor:
                ausgabe_suche(isbn, buch)
                gefunden = True
                return isbn, buch
                break

        if not gefunden:
            print(f"Autor '{autor_origin}' nicht gefunden.\n")
            return None, None


    else:
        print("Ungültige Eingabe.")
        return None, None

isbn, buch = suche_buecher(buecher)

def buch_ausleihen(isbn, buch):
    ausleihen = input(f"\nMöchtest du das Buch mit der ISBN '{isbn}' "
                      f"'{buch['titel']}' ausleihen?\n"
                      f"'j' für 'Ja'\n"
                      f"'n' für 'Nein'\n> ").strip().lower()
    if ausleihen == "j":
        kd_nr = input(f"Bitte geben Sie Ihre Kunden-Nummer ein:\n")
        return  kd_nr
    else:
        print(f"Danke und auf wieder sehen!")
        return None

if buch:
    kundennummer = buch_ausleihen(isbn, buch)
    if kundennummer:
        print(f"\nBuch '{buch['titel']}' wird für Kundennummer {kundennummer} reserviert.")
    else:
        print("Keine gültige auswahl getroffen.")
