from datetime import date
from privato import Privato
from asta import Asta
class Bid:
    __istante: date # immutable, noto alla nascita
    __privato: Privato
    __asta: Asta

    def __init__(self, istante: date, privato: Privato, asta: Asta) -> None:
        self.__istante = istante
        

    def istante(self) -> date:
        return self.__istante
    
    def add_link_bid()