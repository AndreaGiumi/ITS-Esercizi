from tipi_dato_prog.mytypes import *

class Compagnia:
    _nome: str # noto alla nascita
    _fondazione: Anno # noto alla nascita


    def __init__(self, nome: str, fondazione: Anno) -> None:
        self.set_nome(nome)
        self.set_fondazione(fondazione)
        

    def set_nome(self,nome: str) -> None:
        self._nome = nome

    def set_fondazione(self, fondazione: Anno) -> None:
        self._fondazione = fondazione


    def nome(self) ->str:
        return self._nome
    
    def fondazione(self) ->Anno:
        return self._fondazione
    

    def __str__(self) -> str:
        return f"Nome compagnia: {self.nome()} Anno fondazione: {self.fondazione()}"
    

    def __repr__(self) -> str:
        return f"Compagnia(nome={self.nome()}, fondazione={self.fondazione()})"
    