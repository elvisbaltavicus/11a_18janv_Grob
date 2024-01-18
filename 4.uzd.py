def nolasit_un_izdrukāt_faila_saturs():
    try:
        faila_nosaukums = input("Ievadiet faila nosaukumu: ")
        faila_formats = input("Ievadiet faila formātu (paplašinājumu): ")
        pilns_ceļš = f"{faila_nosaukums}.{faila_formats}"

        with open(pilns_ceļš, 'r') as fails:
            saturs = fails.read()
            print(f"Faila '{pilns_ceļš}' saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Kļūda: Fails '{pilns_ceļš}' nav atrasts.")
    except PermissionError:
        print(f"Kļūda: Nav atļaujas lasīt failu '{pilns_ceļš}'.")
    except Exception as e:
        print(f"Kļūda: Neizvēlēta kļūda - {e}")