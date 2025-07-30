from datetime import date
from tipi_dato_prog.mytypes import *

class Asta:
    __prezzo_bid: RealGEZ # mutabile, noto alla nascita
    __scadenza: date # immutabile, noto alla nascita

    def __init__(self, prezzo_bid: RealGEZ, scadenza: date) -> None:
        self.set_prezzoBid(prezzo_bid)
        self.__scadenza = scadenza

    def set_prezzoBid(self, prezzo_bid: RealGEZ) -> None:
        self.__prezzo_bid = prezzo_bid

    def prezzo_bid(self) -> RealGEZ:
        return self.__prezzo_bid
    
    def scadenza(self) -> date:
        return self.__scadenza