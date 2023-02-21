import sys
from angajati import *
from departament import Departament
from management import Management
from tabulate import tabulate
import time


def vizualizare():
    """ Reprezinta submeniul de vizualizare, care contine urmatoarele optiuni:
    1. Vizualizare a tuturor angajatilor in functie de departament
    2. Vizualizarea angajatilor dintr-un departament
    3. Iesire la meniul principal
    """
    print(35 * "=")
    print("1. Meniu Vizualizare".center(35))
    print(35 * "=")
    print("""
    1. Vizualizare a tuturor angajatilor in functie de departament
    2. Vizualizarea angajatilor dintr-un departament
    3. Iesire la meniul principal
    4. Iesire din aplicatie
    """)
    print(35 * "=")
    df_angajati = Departament.df_angajati

    opt = input("\nIntroduceti optiunea: ").strip()
    if (opt == "1"):
        df_angajati = df_angajati.sort_values(by='Department', ascending=True).reset_index(drop=True)
        df_angajati.index = df_angajati.index + 1
        print(tabulate(df_angajati, headers='keys', tablefmt='psql'))
        time.sleep(0.5)
        input('press Enter to continue...')
        vizualizare()
    elif (opt == "2"):
        print('\nLista Departamente:')
        print(tabulate(Angajat.nr_angajati()[1], headers='keys', tablefmt='psql', showindex=False))
        while True:
            try:
                dep = input("Alegeti ID-ul departamentului: ").strip()
                if (type(int(dep)) == int) and (int(dep) in list(df_angajati['Id dep'])):
                    break
                else:
                    print('ID deparament invalid!')
            except ValueError:
                print('Valoare invalida! Introduceti un numar intreg!')
            continue
        df_angajati_dep = Angajat.df_dep(df_angajati, 'Id dep', int(dep))
        print(tabulate(df_angajati_dep, headers='keys', tablefmt='psql'))
        time.sleep(0.5)
        input('press Enter to continue...')
        vizualizare()
    elif (opt == "3"):
        time.sleep(0.25)
        main()
    elif (opt == "4"):
        sys.exit()
    else:
        print("Nu ati introdus o optiune valida!")
        time.sleep(1)
        vizualizare()


def informatii_firma():
    """ Reprezinta submeniul de informatii despre firma, care contine urmatoarele optiuni:
    1. Afisare medie salariala.
    2. Afisare nr angajati/ departament
    3. Afisare nr de angajati cu vechime mai mare de x ani.
    4. iesire la meniul principal
    """
    print(35 * "=")
    print("2. Meniu Informatii despre firma".center(35))
    print(35 * "=")
    print("""
    1. Afisare medie salariala
    2. Afisare nr angajati/ departament
    3. Afisare nr de angajati cu vechime mai mare de x ani
    4. Iesire la meniul principal
    5. Iesire din aplicatie
    """)
    print(35 * "=")
    while True:
        opt = input("\nIntroduceti optiunea: ").strip()
        if (opt == "1"):
            dep = input("Introduceti departamentul dorit [* pentru toate]: ").strip()
            print(f'Media salariilor pe departamentul {dep} este: {Angajat.avg_salary("Department", dep, "Starting Salary")}')
            time.sleep(0.5)
            input('press Enter to continue...')
            informatii_firma()
        elif (opt == "2"):
            print(tabulate(Angajat.nr_angajati()[0], headers='keys', tablefmt='psql', showindex=False))
            time.sleep(0.5)
            input('press Enter to continue...')
            informatii_firma()
        elif (opt == "3"):
            nr = int(input("Introduceti x: " ).strip())
            print(f'In firma sunt {Angajat.vechime(nr)} angajat(i) mai vechi de {nr} an(i).' )
            time.sleep(0.5)
            input('press Enter to continue...')
            informatii_firma()
        elif (opt == "4"):
            main()
        elif (opt == "5"):
            sys.exit()
        else:
            print("Nu ati introdus o optiune valida!")
            time.sleep(0.5)
            informatii_firma()


def management_angajati():
    """ Reprezinta functia de adaugare a angajatilor. Functia cere datele pentru crearea unui obiect
    nou de tip angajat, il adauga in Angajat.lista_anagajati si face update la fisierul 'angajati.csv'.
    * Nota: adaugarea se poate face si dintr-o functie dedicata din clasa de Angajat (in acest caz,
    functia asta doar va apela functia creata in clasa Angajat, [update docstring])
    """

    dict_optiuni1 = {"1": Management.adauga_angajat, "2": Management.elimina_angajat,
                     "3": Management.modifica_angajat, "4": main, "5": sys.exit}

    while True:
        print(35 * "=")
        print("3. Meniu Manangement angajati".center(35))
        print(35 * "=")
        print("""
        1. Adaugare angajati
        2. Eliminare angajati
        3. Modificare date angajat
        4. Iesire la meniul principal
        5. Iesire din aplicatie
        """)
        print(35 * "=")

        optiune = input("\nIntroduceti optiune: ")
        if optiune in dict_optiuni1:
            dict_optiuni1[optiune]()
        else:
            print("Nu ati introdus o optiune valida.")
            time.sleep(0.5)
            input('\npress Enter to continue...')


def main():
    """ Functia de main a proiectului. Reprezinta meniul principal"""
    dict_optiuni = {

        "1": vizualizare,
        "2": informatii_firma,
        "3": management_angajati,
        "4": sys.exit
    }

    # Apelarea functiei load_angajati pentru a incarca datele din fisier in baza curenta de date
    # Angajat.lista_angajati.clear()
    Angajat.load_angajati("angajati.csv")


    while True:
        print(35 * "=")
        print("Meniu".center(35))
        print(35 * "=")
        print("1. Vizualizare\n2. Informatii despre firma\n3. Manangement angajati\n4. Iesire")
        print(35 * "=")

        optiune = input("\nIntroduceti optiune: ")
        # Apelarea optiunii corespunzatoare input-ului
        if optiune in dict_optiuni:
            dict_optiuni[optiune]()
        else:
            print("Nu ati introdus o optiune valida.")
            time.sleep(0.5)
            input('\npress Enter to continue...')


if __name__ == "__main__":
    main()
