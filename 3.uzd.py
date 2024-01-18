faila_ceļš = 'jūsu_fails.txt'
try:
    with open(faila_ceļš, 'r') as fails:
        rindas = fails.readlines()
        if len(rindas) >= 3:
            print("Trešā rinda:", rindas[2])
        else:
            print("Failā nav pietiekami daudz rindu.")
except FileNotFoundError:
    print(f"Faila '{faila_ceļš}' nav atrasts.")
except Exception as e:
    print(f"Kļūda lasot failu '{faila_ceļš}': {e}")