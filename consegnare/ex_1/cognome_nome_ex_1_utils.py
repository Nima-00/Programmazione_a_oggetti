"""Module ex_1"""


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

    def __str__(self):
        return f"{self.__giorno:02d}/{self.__mese:02d}/{self.__anno}"


class Vaccinazione:

    def __init__(self, data: Data, nome_vaccino: str):
        self.__data = data
        self.__nome_vaccino = nome_vaccino

    def get_data(self):
        return self.__data

    def get_nome_vaccino(self):
        return self.__nome_vaccino

    def set_nome_vaccino(self, nome_vaccino: str):
        self.__nome_vaccino = nome_vaccino

    def __str__(self):
        return f"{self.__data} [{self.__nome_vaccino}]"


class Persona:

    def __init__(self, nome: str, cognome: str, data_nascita: Data, sesso: str):
        self.__nome = nome
        self.__cognome = cognome
        self.__data_nascita = data_nascita
        self.__sesso = sesso
        self.__vaccinazioni = []

    @classmethod
    def da_codice_fiscale(cls, nome: str, cognome: str, codice_fiscale: str):
        if len(codice_fiscale) != 16:
            raise ValueError("Il codice fiscale deve essere lungo 16 caratteri.")
        anno = 1900 + int(codice_fiscale[6:8])
        mese = "ABCDEHLMPRST".index(codice_fiscale[8]) + 1
        giorno = int(codice_fiscale[9:11])
        if giorno > 40:
            giorno -= 40
            sesso = "F"
        else:
            sesso = "M"
        return cls(nome, cognome, Data(giorno, mese, anno), sesso)

    def get_nome(self):
        return self.__nome

    def get_cognome(self):
        return self.__cognome

    def get_data_nascita(self):
        return self.__data_nascita

    def get_sesso(self):
        return self.__sesso

    def get_vaccinazioni(self):
        return self.__vaccinazioni

    def add_vaccinazione(self, vaccinazione: Vaccinazione):
        self.__vaccinazioni.append(vaccinazione)

    def get_numero_vaccinazioni(self):
        return len(self.__vaccinazioni)

    def ciclo_cocluso(self):
        ciclo_terminato = False
        A = 0
        M = 0
        P = 0
        for vaccinazione in self.__vaccinazioni:
            if vaccinazione.get_nome_vaccino() == "Johnson":
                ciclo_terminato = True
            elif vaccinazione.get_nome_vaccino() == "AstraZeneca":
                A += 1
            elif vaccinazione.get_nome_vaccino() == "Moderna":
                M += 1
            elif vaccinazione.get_nome_vaccino() == "Pfizer":
                P += 1
            if A == 2 or M == 2 or P == 2:
                ciclo_terminato = True
        return ciclo_terminato

    def __str__(self):
        return f"{self.__nome} {self.__cognome} {self.__data_nascita} [{self.__sesso}] [{self.ciclo_cocluso()}]"


def read_file(file_path: str) -> list[Persona]:
    lista_persone = []
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            terms = line.split(sep=";")
            nome = terms[0]
            cognome = terms[1]
            data = terms[2].split(sep="-")
            giorno = int(data[0])
            mese = int(data[1])
            anno = int(data[2])
            sesso = terms[3]
            codice_fiscale = terms[4]
            persona = Persona(nome, cognome, Data(giorno, mese, anno), sesso)
            A = 0
            for vaccino in terms[5:]:
                vax = vaccino.split("-")
                nome_vaccino = vax[0]
                giorno_vaccino = int(vax[1])
                mese_vaccino = int(vax[2])
                anno_vaccino = int(vax[3])
                persona.add_vaccinazione(
                    Vaccinazione(
                        Data(giorno_vaccino, mese_vaccino, anno_vaccino), nome_vaccino
                    )
                )
                if nome_vaccino == "AstraZeneca":
                    A += 1
            if A == 1:
                lista_vaccinazioni = persona.get_vaccinazioni()
                for vaccino in lista_vaccinazioni:
                    if vaccino.get_nome_vaccino() == "AstraZeneca":
                        vaccino.set_nome_vaccino("Johnson")
            lista_persone.append(persona)
    return lista_persone
