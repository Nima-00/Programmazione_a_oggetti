"""Module ex_2"""

from datetime import datetime


class Data:

    def __init__(self, giorno: int, mese: int, anno: int):
        self.__giorno = giorno
        self.__mese = mese
        self.__anno = anno

    def get_giorno(self):
        return self.__giorno

    def get_mese(self):
        return self.__mese

    def get_anno(self):
        return self.__anno

    def check_data_passata(self) -> bool:
        giorno_corrente = datetime.now().day
        mese_corrente = datetime.now().month
        anno_corrente = datetime.now().year
        if (
            self.__anno < anno_corrente
            and self.__mese < mese_corrente
            and self.__giorno < giorno_corrente
        ):
            return False
        else:
            return True

    def __str__(self):
        return f"{self.__giorno:02d}-{self.__mese:02d}-{self.__anno}"


class Attrezzatura:

    def __init__(
        self, nome: str, numero_inventario: str, data_prossima_revisione: Data
    ):
        self.__nome = nome
        self.__numero_inventario = numero_inventario
        self.__data_prossima_revisione = data_prossima_revisione

    def get_nome(self):
        return self.__nome

    def get_numero_inventario(self):
        return self.__numero_inventario

    def get_data_prossima_revisione(self):
        return self.__data_prossima_revisione

    def cambia_data_prossima_revisione(self, nuova_data: Data):
        self.__data_prossima_revisione = nuova_data

    def __str__(self):
        return f"[{self.__numero_inventario}] {self.__nome} ({self.__data_prossima_revisione})"


class Aula:

    def __init__(self, nome: str, edificio: str, capienza: int):
        self.__nome = nome
        self.__edificio = edificio
        self.__capienza = capienza
        self.__attrezzature = []

    def get_nome(self):
        return self.__nome

    def get_edificio(self):
        return self.__edificio

    def get_capienza(self):
        return self.__capienza

    def get_attrezzature(self):
        return self.__attrezzature

    def add_attrezzature(self, attrezzatura: Attrezzatura):
        self.__attrezzature.append(attrezzatura)

    def check_capienza(self, n: int):
        if n > self.__capienza:
            return False
        else:
            return True

    def check_attrezzatura_obbligatoria(self):
        E = False
        L = False
        S = False
        for attrezzatura in self.get_attrezzature():
            match attrezzatura.get_nome():
                case "Estintore":
                    E = True
                case "LuceEmergenza":
                    L = True
                case "Sirena":
                    S = True
        if E and L and S:
            return True
        else:
            return False
    
    def __str__(self):
        return f"{self.__nome} [{self.__edificio}] [{self.__capienza}] [{self.check_attrezzatura_obbligatoria()}]"


def reaf_file(file_path: str) -> list:
    lista_aule = []
    with open("input.txt") as f:
        for line in f:
            terms = line.strip().split(sep=";")
            nome_aula = terms[0]
            nome_edificio = terms[1]
            capienza = terms[2]
            aula = Aula(nome_aula, nome_edificio, capienza)
            for attrezzatura in terms[3:]:
                att = attrezzatura.split(sep="-")
                nome_attrezzatura = att[0]
                numero_inventario = att[1]
                giorno = int(att[2])
                mese = int(att[3])
                anno = int(att[4])
                aula.add_attrezzature(
                    Attrezzatura(
                        nome_attrezzatura,
                        numero_inventario,
                        Data(giorno, mese, anno),
                    )
                )
            lista_aule.append(aula)
    return lista_aule
