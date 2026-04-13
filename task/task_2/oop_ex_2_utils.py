"""Modulo fogli esercizio 2 OOP"""


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


class Vaccinazione:
    """Classe che rappresenta una vaccinazione"""

    def __init__(self, data_vaccinazione: Data, nome_vaccino: str):
        self.__data_vaccinazione = data_vaccinazione
        self.__nome_vaccino = nome_vaccino

    def get_data_vaccinazione(self):
        return self.__data_vaccinazione

    def get_nome_vaccino(self):
        return self.__nome_vaccino

    def set_nome_vaccino(self, nome_vaccino: str):
        self.__nome_vaccino = nome_vaccino

    def __str__(self):
        return f"{self.__data_vaccinazione} [{self.__nome_vaccino}]"


class Persona:
    """Classe che rappresenta una persona"""

    def __init__(
        self,
        cognome: str,
        nome: str,
        data_nascita: Data,
        sesso: str,
        codice_fiscale: str,
    ):
        self.__cognome = cognome
        self.__nome = nome
        self.__data_nascita = data_nascita
        self.__sesso = sesso
        self.__codice_fiscale = codice_fiscale
        self.__lista_vaccinazioni = []

    def get_nome(self):
        return self.__nome

    def get_cognome(self):
        return self.__cognome

    def get_data_nascita(self):
        return self.__data_nascita

    def get_sesso(self):
        return self.__sesso

    def get_codice_fiscale(self):
        return self.__codice_fiscale

    def get_lista_vaccinazioni(self):
        return self.__lista_vaccinazioni

    def aggiungi_vaccinazione(self, vaccinazione: Vaccinazione):
        self.__lista_vaccinazioni.append(vaccinazione)

    def get_numero_vaccinazioni(self):
        return len(self.__lista_vaccinazioni)

    def __str__(self):
        persona = f"{self.__cognome} {self.__nome} [{self.__data_nascita}] [{self.__sesso}] [{self.__codice_fiscale}]\n"
        for vaccinazione in self.__lista_vaccinazioni:
            persona += f"- {vaccinazione}\n"
        return persona


def read_file(file_path: str) -> list[Persona]:
    """Legge un file di testo e restituisce una lista di persone
    Formato del file:
    cognome;nome;data_nascita;sesso;codice_fiscale;vaccino1;...;vaccinoN
    dove:
    - data_nascita è nel formato gg-mm-aaaa
    - vaccino è nel formato nome_vaccino-gg-mm-aaaa
    """

    lista_persone = []
    with open(file_path) as f:
        for line in f:
            terms = line.strip().split(sep=";")
            cognome = terms[0]
            nome = terms[1]
            data = terms[2].split(sep="-")
            giorno = int(data[0])
            mese = int(data[1])
            anno = int(data[2])
            data_nascita = Data(giorno, mese, anno)
            sesso = terms[3]
            codice_fiscale = terms[4]
            persona = Persona(cognome, nome, data_nascita, sesso, codice_fiscale)
            for vaccino in terms[5:]:
                vax = vaccino.split("-")
                nome_vaccino = vax[0]
                giorno_vaccinazione = int(vax[1])
                mese_vaccinazione = int(vax[2])
                anno_vaccinazione = int(vax[3])
                data_vaccinazione = Data(
                    giorno_vaccinazione, mese_vaccinazione, anno_vaccinazione
                )
                persona.aggiungi_vaccinazione(
                    Vaccinazione(data_vaccinazione, nome_vaccino)
                )
            lista_persone.append(persona)
    return lista_persone


def write_file(path: str, lista_persone: list[Persona]):
    with open(path, "w") as f:
        for persona in lista_persone:
            f.write(str(persona) + "\n")
