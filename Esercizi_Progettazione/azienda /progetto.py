from tipi_dato_prog.mytypes import *
from impiegato import Impiegato
from coinvolto import *
from impiegato import *

class Progetto:
    _nome: str # noto alla nascita
    _budget: RealGEZ # noto alla nascita
    _impiegati: dict[Impiegato, coinvolto._link]


    def __init__(self, nome: str, budget: RealGEZ, impiegati: dict[Impiegato, coinvolto._link] ) -> None:
        self.setNome(nome)
        self.setBudget(budget)
        self._impiegati = dict()
        


    def getNome(self) -> str:
        return self._nome
    
    def getBudget(self) -> RealGEZ:
        return self._budget
    

    def setNome(self, nome: str) -> None:
        self._nome = nome

    def setBudget(self, budget: RealGEZ) -> None:
        self._budget = budget


    def _add_link_coinvolto(self, l: coinvolto._link) -> None:
        if l.progetto() != self:
            raise ValueError(f"Il link non coinvolge me, ma {l.progetto()}")
        if l.impiegato() in self._impiegati:
            raise KeyError(f"L'impiegato {l.impiegato}")
        self._impiegati[l.impiegato()] = l
        

    def __str__(self) -> str:
        return f"Progetto: {self.getNome()} con budget: {self.getBudget()} €"
    

    def __repr__(self) -> str:
        return f"Progetto(nome={self.getNome()}, budget={self.getBudget()})"