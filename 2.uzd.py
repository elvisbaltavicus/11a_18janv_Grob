import csv

def lasit_otro_kolonnu(csv_fails):
    try:
        with open(csv_fails, 'r', newline='') as fails:
            lasitajs = csv.reader(fails)
            print("Otrās kolonnas dati:")
            for rinda in lasitajs:
                if len(rinda) >= 2:
                    print(rinda[1])
    except FileNotFoundError:
        print(f"Kļūda: Fails '{csv_fails}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: Neizvēlēta kļūda - {e}")
lasit_otro_kolonnu('jusu_csv_fails.csv')