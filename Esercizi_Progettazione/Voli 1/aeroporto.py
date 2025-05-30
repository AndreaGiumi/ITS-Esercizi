from tipi_dato_prog.mytypes import *
from typing import Any


class Aeroporto:
    _codice: CodiceIATA # noto alla nascita
    _nome: str  # noto alla nascita


    def __init__(self, codice: CodiceIATA, nome: str) -> None:
        self._codice = codice
        self.set_nome(nome)


    def set_nome(self, nome: str) -> None:
        self._nome = nome


    def codice(self) -> CodiceIATA:
        return self._nome


    def nome(self) -> str:
        return self._nome
    

    def __hash__(self) -> int:
        return hash(self._codice)

    def __eq__(self, other: Any)  -> bool:
        if other is None or \
                not isinstance(other, type(self)) or \
                hash(self) != hash(other):
            return False
        return self._codice == other._codice
    



    def __str__(self) -> str:
        return f"Codice IATA: {self._codice} \nNome Aeroporto:  {self._nome}"
    
    def __repr__(self):
        return f"Aeroporto(Codice IATA={self.codice()}, nome={self.nome()})"