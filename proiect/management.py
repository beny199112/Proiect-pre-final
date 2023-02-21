import time

from departament import Departament
from angajati import Angajat
from tabulate import tabulate
import pandas as pd
from datetime import datetime as dt

class Management(Angajat):
    # Variabila de clasa care va contine obiecte de tip Departament

    def __init__(self):
        """ Constructorul clasei Departament. """
        super().__init__(self)

    @classmethod
    def adauga_angajat(cls):
        workdep = input("Introduceti departamentul la care lucreaza angajatul:  ").strip()
        empname = input("Introduceti numele angajatului respectiv: ").strip()
        job = input("Introduceti numele jobului la care este angajat respectivul: ").strip()

        while True:
            try:
                hire_date = input("Introduceti data la care a fost angajat: ").strip()
                if Departament.is_valid_date(hire_date)[0] and Departament.is_valid_date(hire_date)[1] > 0:
                    break
                else:
                    print('Valoare invalida! Introduceti o data in formatul "aaaa-ll-zz" ')
            except ValueError:
                print('Valoare invalida! Introduceti un numar intreg!')
            continue

        while True:
            try:
                salary = int(input("Introduceti salarul angajatului: ").strip())
                if type(int(salary)) == int:
                    break
                else:
                    pass
            except ValueError:
                print('Valoare invalida! Introduceti un numar intreg!')
            continue

        a = Angajat(workdep, empname, job, hire_date, salary)

        Angajat.add_angajat(a)
        Angajat.update_fisier()
        time.sleep(0.5)
        print("Angajatul a fost adaugat cu succes! ")

    @classmethod
    def elimina_angajat(cls):
        code = input('Introduceti codul angajatului pe care doriti sa-l stergeti din baza de date: ')
        df = Angajat.database_angajati
        row = df[df['Id'] == code]
        df.drop(row.index, inplace=True)

        Angajat.update_fisier()

        df_ex_angajati = pd.read_csv('fosti_angajati.csv', sep=';')
        df_ex_angajati = pd.concat([df_ex_angajati, row])
        df_ex_angajati.to_csv('./fosti_angajati.csv', sep=';', index=False)
        time.sleep(0.5)
        print("Angajatul a fost eliminat cu succes! ")

    @classmethod
    def modifica_angajat(cls):
        code = input('Introduceti codul angajatului caruia doriti sa-i modificati datele: ')
        df = Angajat.database_angajati
        col_names = list(df.columns)
        df1 = df.rename(columns=lambda x: str(col_names.index(x)) + ' - ' + x if  col_names.index(x) > 1 else x)
        print(tabulate(df1[df1['Id'] == code], headers='keys', tablefmt='psql', showindex=False))
        col = int(input('Introduceti nr coloanei pe care doriti sa o modificati: '))
        new_val = input('Introduceti noua valoare: ')
        df.loc[df.Id == code, df.iloc[:,col].name] = new_val

        Angajat.update_fisier()
        print("Datele angajatului au fost modificate cu succes! ")

        input('press Enter to continue...')




