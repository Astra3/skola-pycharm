import pandas as pd
from sqlalchemy import create_engine
import numpy as np


class Pocasi:
    def __init__(self, filename: str, source="excel"):
        """
        Načte databázi do pd.DataFrame objektu a umožňuje s ní následnou práci
        :param filename: název souboru pro přečtení včetně přípony
        :param source: buď "sql" nebo "excel" pro čtení jak z SQL tak z tradičního Excel formátu který používáme
        """
        self.data = {}  # dictionary všech výsledných dat
        self._filename = filename
        self._mesice = ["Leden", "Únor", "Březen", "Duben", "Květen", "Červen", "Červenec", "Srpen", "Září",
                        "Říjen", "Listopad", "Prosinec"]
        if source == "excel":
            self._data_source = pd.read_excel(filename, None, parse_dates=[0])  # načte data z Excelu
            strings = ["Čas", "Směr větru"]  # seznam tabulek, co jsou stringy
            for i in self._data_source:
                data = self._data_source[i].drop(strings, axis=1)  # vytvoří kopii tabulky beze strings
                data = data.astype("float")  # interpretuje novou tabulku jako float
                for i2 in strings:
                    # nahradí nan ve string na np.nan
                    data[i2] = self._data_source[i][i2].replace("nan", np.nan, regex=True)
                self.data.update({i: data})
        elif source == "sql":
            self.conn = create_engine(f"sqlite:///{filename}")  # vytvoří connection
            for i in self._mesice:
                self._tabulka = pd.read_sql_table(i, self.conn)  # načte tabulku
                self.data.update({i: self._tabulka})

    def to_sql(self):
        """
        Uloží tabulku do SQL databáze odpovídající filename z :class:`Pocasi` nebo s příponou .db
        """
        if "self._tabulka" not in locals():
            self.conn = create_engine(f"sqlite:///{self._filename}.db")
        for mes in self._mesice:
            self.data[mes].to_sql(mes, self.conn)


if __name__ == '__main__':
    pcs = Pocasi("Data/2020.xlsx.db", "sql")
    # pcs.to_sql()
    pass
    for k in ["Leden", "Únor", "Březen", "Duben", "Květen", "Červen", "Červenec", "Srpen", "Září",
              "Říjen", "Listopad", "Prosinec"]:
        print(k)
        print(pcs.data[k].dtypes)
    pass
