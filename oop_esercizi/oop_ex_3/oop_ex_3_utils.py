"""Modulo task 3 OOP"""


class Atleta:

    def __init__(self, nome: str, cognome: str, medaglia: str = "N"):
        self.__nome = nome
        self.__cognome = cognome
        self.__medaglia = medaglia

    def get_nome(self):
        return self.__nome

    def get_cognome(self):
        return self.__cognome

    def get_medaglia(self):
        return self.__medaglia

    def cambia_medaglia(self, medaglia: str):
        self.__medaglia = medaglia

    def __str__(self):
        return f"{self.__cognome} {self.__nome} [{self.__medaglia}]"


class Disciplina:

    def __init__(self, nome: str, tipologia: str):
        self.__nome = nome
        self.__tipologia = tipologia
        self.__atleti = []

    def get_nome(self):
        return self.__nome

    def get_tipologia(self):
        return self.__tipologia

    def get_atleti(self):
        return self.__atleti

    def add_atleta(self, atleta: Atleta):
        self.__atleti.append(atleta)

    def __str__(self):
        s = f"{self.__nome} ({self.__tipologia})"
        for atleta in self.__atleti:
            s += f"\n-- {atleta}"
        return s


class Medagliere:

    def __init__(
        self, numero_ori: int = 0, numero_argenti: int = 0, numero_bronzi: int = 0
    ):
        self.__numero_ori = numero_ori
        self.__numero_argenti = numero_argenti
        self.__numero_bronzi = numero_bronzi

    def get_numero_ori(self):
        return self.__numero_ori

    def get_numero_argenti(self):
        return self.__numero_argenti

    def get_numero_bronzi(self):
        return self.__numero_bronzi

    def set_numero_ori(self, n_ori: int):
        self.__numero_ori = n_ori

    def set_numero_argenti(self, n_argenti: int):
        self.__numero_argenti = n_argenti

    def set_numero_bronzi(self, n_bronzi: int):
        self.__numero_bronzi = n_bronzi

    def get_numero_medaglie(self):
        return self.__numero_ori + self.__numero_argenti + self.__numero_bronzi

    def azzera_medagliere(self):
        self.__numero_bronzi = 0
        self.__numero_argenti = 0
        self.__numero_bronzi = 0

    def __str__(self):
        return f"{self.__numero_ori} {self.__numero_argenti} {self.__numero_bronzi} | {self.get_numero_medaglie()}"


class Nazione:

    def __init__(self, nome: str, sigla: str):
        self.__nome = nome
        self.__sigla = sigla
        self.__discipline = []
        self.__medagliere = Medagliere()

    def get_nome(self):
        return self.__nome

    def get_sigla(self):
        return self.__sigla

    def get_discipline(self):
        return self.__discipline

    def get_medagliere(self):
        return self.__medagliere

    def add_disciplina(self, disciplina: Disciplina):
        self.__discipline.append(disciplina)

    def calcola_medagliere(self, n_ori: int, n_argenti: int, n_bronzi: int):
        self.__medagliere.set_numero_ori(self.__medagliere.get_numero_ori() + n_ori)
        self.__medagliere.set_numero_argenti(
            self.__medagliere.get_numero_argenti() + n_argenti
        )
        self.__medagliere.set_numero_bronzi(
            self.__medagliere.get_numero_bronzi() + n_bronzi
        )

    def __str__(self):
        s = f"{self.__nome} ({self.__sigla}) | {self.__medagliere}\n"
        for disciplina in self.__discipline:
            s += f"- {disciplina}\n"
        return s


def read_file(input_path: str):
    nazioni = []
    with open(input_path, "r") as f:
        n_righe = int(f.readline().strip())
        for i in range(n_righe):
            riga = f.readline()
            termini = riga.strip().split(sep="!")
            nome_nazione = termini[0]
            sigla_nazione = termini[1]
            nazione = Nazione(nome_nazione, sigla_nazione)
            for d in termini[2:]:
                d_termini = d.split(sep=";")
                nome_disciplina = d_termini[0]
                tipologia_disciplina = d_termini[1]
                disciplina = Disciplina(nome_disciplina, tipologia_disciplina)
                n_ori = 0
                n_argenti = 0
                n_bronzi = 0
                for a in d_termini[2:]:
                    a_termini = a.split(sep="-")
                    nome_atleta = a_termini[0]
                    cognome_atleta = a_termini[1]
                    medaglia = a_termini[2]
                    atleta = Atleta(nome_atleta, cognome_atleta, medaglia)
                    disciplina.add_atleta(atleta)
                    match medaglia:
                        case "O":
                            if n_ori > 0 and tipologia_disciplina == "S":
                                continue
                            n_ori += 1
                        case "A":
                            if n_argenti > 0 and tipologia_disciplina == "S":
                                continue
                            n_argenti += 1
                        case "B":
                            if n_bronzi > 0 and tipologia_disciplina == "S":
                                continue
                            n_bronzi += 1
                nazione.add_disciplina(disciplina)
                nazione.calcola_medagliere(n_ori, n_argenti, n_bronzi)
            nazioni.append(nazione)
    return nazioni


def write_file(output_path: str, nazioni: list[Nazione]):
    with open(output_path, "w") as f:
        for nazione in nazioni:
            f.write(str(nazione) + "\n")
