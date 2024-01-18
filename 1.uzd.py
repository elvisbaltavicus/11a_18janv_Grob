def lasit_failu(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r') as fails:
            saturs = fails.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Kļūda: Fails '{faila_nosaukums}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: Neizvēlēta kļūda - {e}")
lasit_failu('jusu_faila_nosaukums.txt')