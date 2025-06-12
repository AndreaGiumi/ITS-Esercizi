from datetime import date
from progetto import Progetto
from impiegato import Impiegato
from __future__ import annotations
from typing import Any

class coinvolto:
    @staticmethod
    def add(cls, progetto: Progetto, impiegato: Impiegato, data: date) -> None:
        l = cls._link(progetto, impiegato, data)
        progetto._add_link_coinvolto(l)
        impiegato._add_link_coinvolto(l)


    class _link:

        _data: date # immutabile noto alla nascita
        _progetto: Progetto # noto alla nascita
        _impiegato: Impiegato # noto alla nascita

        def __init__(self, data: date, progetto: Progetto, impiegato: Impiegato) -> None:
            self._impiegato = impiegato
            self._progetto = progetto
            self._data = data

        
        def progetto(self) -> Progetto:
            return self._progetto

        def impiegato(self) -> Impiegato:
            return self._impiegato

        def data(self) -> date:
            return self._data
        

        def __hash__(self) -> int:
            return hash((self._progetto, self._impiegato))
        

        def __eq__(self, other: Any) -> bool:
            if type(self) != type(other) or hash(self) != hash(other):
                return False
            
            return self.progetto() is other.progetto() \
                and self.impiegato() is other.impiegato()

        
        


        