from tipi_dato_prog.mytypes import *
from datetime import date

class Persona:
    _nome: str # mutabile noto alla nascita
    _cognome: str # mutabile noto alla nascita
    _cf: CodiceFiscale # immutabile noto alla nascita e univoco
    _nascita: date # immtuabile noto alla nascita
    _maternità: IntGEZ # [0..1] mutabile 
    _genere: Genere # mutabile noto alla nascita

    def __init__(self, nome: str, cognome: str, cf: CodiceFiscale, nascita: date, maternità: IntGEZ, genere: Genere):
        