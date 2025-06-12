from datetime import date
from tipi_dato_prog.mytypes import *
from progetto import Progetto
from coinvolto import coinvolto


class Impiegato:
    nome: str # noto alla nascita
    cognome: str # noto alla nascita
    nascita: date # << imm >> noto alla nascita
    stipendio: RealGEZ # noto alla nascita
    _progetti: dict[Progetto, coinvolto._link]
    



    def __init__(self, nome: str, cognome: str, nascita: date, stipendio: RealGEZ ):
        self.setNome(nome)
        self.setCognome(cognome)
        self.nascita: date = nascita
        self.setStipendio(stipendio)
        self._progetti = dict(Progetto, coinvolto._link)


    def setNome(self, nome: str) -> None:
        self.nome = nome


    def setCognome(self, cognome: str)-> None:
        self.cognome = cognome


    def setStipendio(self, stipendio: RealGEZ) -> None:
        self.stipendio = stipendio

    def getNascita(self) -> str:
        return self.nascita

    def getNome(self)-> str:
        return self.nome
    

    def getCognome(self) -> str:
        return self.cognome
    

    def getStripendio(self) -> RealGEZ:
        return self.stipendio 
    

    def _add_link_coinvolto(self, l: coinvolto._link) -> None:
        if l.impiegato() != self:
            raise ValueError(f"Il link non coinvolge me, ma {l.impiegato()}")
        if l.progetto() in self._progetti:
            raise KeyError(f"L'impiegato è già coinvolto nel progetto: {l.progetto()}")
        self._progetti[l.progetto()] = l

    
    
    def __str__(self) -> str:
        return f"{self.nome}  {self.cognome}  nascita: {self.nascita()}  stipendio: {self.stipendio()}"