"""Modulo task 1 OOP"""


class Data:
    """Classe che rappresenta una data"""

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

    def __str__(self):
        return f"{self.__giorno:02d}/{self.__mese:02d}/{self.__anno}"


class Attrezzatura:
    """Classe che rappresenta un'attrezzatura"""

    def __init__(
        self,
        nome_attrezzatura: str,
        codice_inventario: str,
        data_prossima_revisione: Data,
    ):
        self.__nome = nome_attrezzatura
        self.__codice_inventario = codice_inventario
        self.__data_prossima_revisione = data_prossima_revisione

    def get_nome(self):
        return self.__nome

    def get_numero_inventario(self):
        return self.__numero_inventario

    def get_data_prossima_revisione(self):
        return self.__data_prossima_revisione

    def __str__(self):
        return f"[{self.__codice_inventario}] {self.__nome} ({self.__data_prossima_revisione})"


class Aula:
    """Classe che rappresenta un'aula"""

    def __init__(self, nome_aula: str, edificio: str, capienza: int):
        self.__nome = nome_aula
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

    def aggiungi_attrezzatura(self, attrezzatura: Attrezzatura):
        self.__attrezzature.append(attrezzatura)

    def controlla_capienza(self, n: int):
        if n > self.__capienza:
            return False
        else:
            return True

    def controlla_attrezzatura_obbligatoria(self):
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
        s = f"{self.__nome} [{self.__edificio}] [{self.__capienza}] [{self.controlla_attrezzatura_obbligatoria()}]\n"
        for attrezzatura in self.get_attrezzature():
            s += f"- {attrezzatura}\n"
        return s


def read_file(file_path: str) -> list:
    """Legge un file di testo e restituisce una lista di aule
    Formato del file:
    nome_aula;edificio;capienza;attrezzatura1;...;attrezzaturaN
    dove attrezzaturaX è una stringa nel formato:
    nome_attrezzatura-codice_inventario-giorno-mese-anno
    """

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
                data_revisione = Data(giorno, mese, anno)
                attrezzatura = Attrezzatura(
                    nome_attrezzatura, numero_inventario, data_revisione
                )
                aula.aggiungi_attrezzatura(attrezzatura)
            lista_aule.append(aula)
    return lista_aule


def write_file(path: str, lista_aule: list[Aula]):
    with open(path, "w") as f:
        for aula in lista_aule:
            f.write(str(aula) + "\n")
