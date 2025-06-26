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
        return self._codice


    def nome(self) -> str:
        return self._nome
    


    def __str__(self) -> str:
        return f"Codice IATA: {self._codice} \nNome Aeroporto:  {self._nome}"
    
    def __repr__(self):
        return f"Aeroporto(Codice IATA={self.codice()}, nome={self.nome()})"