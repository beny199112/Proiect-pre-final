from departament import Departament
import pandas as pd
import numpy as np
import datetime as dt

class Angajat(Departament):
    # Variabila de clasa care va contine obiecte de tip Angajat
    database_angajati = None

    def __init__(self, workdep, empname, job, hiredate, salary):
        """ Constructorul clasei Angajat. """
        super().__init__(workdep)
        self.empname = empname
        self.job = job
        self.hiredate = hiredate
        self.__salary = salary

    @classmethod
    def load_angajati(cls,nume_fisier):
        """ Creeaza obiecte de tip Angajat si le adauga in lista_angajati, bazate
        pe informatiile din fisierul nume_fisier. """
        df_angajati1 = Departament.df_angajati
        cls.database_angajati = df_angajati1

    @classmethod
    def update_fisier(cls):
        """ Updateaza fisierul 'angajati.csv' cu informatiile actuale din lista_angajati. """
        Departament.df_angajati.to_csv('./angajati.csv', sep=';', index=False)

    def add_angajat(self):
        angajat = [Departament.id_angajat(self.database_angajati),
                   Departament.id_dep(self.database_angajati, 'Id dep', 'Department', self.workdep),
                   self.workdep, self.empname, self.job,
                   self.hiredate, self.__salary]
        Departament.df_angajati.loc[Departament.df_angajati.shape[0]] = angajat

    @staticmethod
    def df_dep(df, col_name, val='*'):
        ''' A static method that takes as input a data frame (df), a column form that dataframe (col_name)
        and a value (val) from that column in order to return a sub-dataframe only with the rows that are = val'''
        df_dep = df if val == '*' else df.loc[df[col_name] == val].reset_index(drop=True)
        df_dep.index = df_dep.index + 1
        return df_dep

    @classmethod
    def avg_salary(cls, dep_col_name, dep, col_name_for_avg):
        res = cls.df_dep(cls.database_angajati, dep_col_name, dep)
        res = res[[col_name_for_avg]].mean(axis=0)
        return np.round(res[0],2)

    @classmethod
    def nr_angajati(cls):
        dff = cls.database_angajati.groupby(['Id dep', "Department"], as_index=False)["Employee Name"].count()
        dff.columns = ['ID', 'Nume Departament', 'Nr. Angajati']
        dff = dff.sort_values(by='Nr. Angajati', ascending=False).reset_index(drop=True)
        dff.index = dff.index + 1
        return dff, dff.iloc[:, 0:2].sort_values(by='ID')

    @staticmethod
    def col_vechime_ani(val):
        now = dt.datetime.now()
        dif = now - val
        return int(np.floor(dif.days/365.25))

    @classmethod
    def vechime(cls, nr_ani):
        dff = cls.database_angajati
        dff['Hiring Date'] = pd.to_datetime(dff['Hiring Date'])
        dff.insert(dff.shape[1], 'years', dff.apply(lambda row: cls.col_vechime_ani(row['Hiring Date']), axis=1) )
        years_col = list(dff['years'])
        return years_col.count(nr_ani)





