from datetime import date
from tipi_dato_prog.mytypes import *


class Impiegato:
    nome: str # noto alla nascita
    cognome: str # noto alla nascita
    nascita: date # << imm >> noto alla nascita
    stipendio: FloatGEZ # noto alla nascita



    def __init__(self, nome: str, cognome: str, nascita: date, stipendio: FloatGEZ ):
        self.setNome(nome)
        self.setCognome(cognome)
        self.nascita: date = nascita
        self.setStipendio(stipendio)


    def setNome(self, nome: str) -> None:
        self.nome = nome


    def setCognome(self, cognome: str)-> None:
        self.cognome = cognome


    def setStipendio(self, stipendio: FloatGEZ) -> None:
        self.stipendio = stipendio

    def getNascita(self) -> str:
        return self.nascita

    def getNome(self)-> str:
        return self.nome
    

    def getCognome(self) -> str:
        return self.cognome
    

    def getStripendio(self) -> FloatGEZ:
        return self.stipendio 
    
    def __str__(self) -> str:
        return f"{self.nome}  {self.cognome}  nascita: {self.nascita()}  stipendio: {self.stipendio()}"