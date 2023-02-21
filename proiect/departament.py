import pandas as pd
from datetime import datetime as dt

class Departament:
    # Variabila de clasa care va contine obiecte de tip Departament
    df_angajati = pd.read_csv('angajati.csv', sep=';')

    def __init__(self, workdep):
        """ Constructorul clasei Departament. """
        self.workdep = workdep

    @staticmethod
    def id_angajat(df):
        return 'emp-' + str(df.shape[0] + 1)

    @staticmethod
    def id_dep(df, col_id_name, col_name, dep_name):
        dep_lst = list(df[col_name].unique())
        if dep_name not in dep_lst:
            id = len(dep_lst) + 1
        else:
            dff = df.loc[df[col_name] == dep_name]
            id = dff[col_id_name].iloc[0]
        return id

    @staticmethod
    def is_valid_date(hire_date):
        result = True
        # now = dt.date.now()
        dif = 1
        try:
            date = dt.strptime(hire_date, '%Y-%m-%d').date()
            # dif = now - date
        except ValueError:
            result = False
        return result, dif
