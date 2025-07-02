from __future__ import annotations
from datetime import date
from tipi_dato_prog.mytypes import *





    

class Persona:
    _nome: str # mutabile noto alla nascita
    _cognome: str # mutabile noto alla nascita
    _cf: CodiceFiscale # immutabile noto alla nascita e univoco
    _nascita: date # immtuabile noto alla nascita
    _maternità: IntGEZ|None # [0..1] mutabile possibilmente non noto alla nascita
    _genere: Genere # mutabile noto alla nascita
    _pos_mili: PosizioneMilitare|None # certamente non noto alla nascita

    def __init__(self,*, nome: str, cognome: str, cf: CodiceFiscale, nascita: date, maternità: IntGEZ|None, genere: Genere, pos_mili: PosizioneMilitare|None):
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self._cf = cf
        self.set_genere(genere)
        self.set_pos_mili(pos_mili)
 

    def set_genere(self, genere: Genere, maternità: IntGEZ|None, pos_mili: PosizioneMilitare|None) -> None:
        self._genere = genere


    
    def dimentica_uomo(self) -> None:
        self._pos_mili = None

    def dimentica_donna(self) -> None:
        self._maternità = None

    def set_pos_mili(self, pos_mili: PosizioneMilitare|None) -> None:
        if self._genere == Genere.donna:
            if pos_mili is not None:
                raise ValueError("Errore! Una donna non può avere una posizione militare!")
        if self._genere == Genere.uomo and pos_mili is None:
            raise ValueError("Errore! Un uomo deve avere una posizione militare!")

    def posizione_militare(self) -> PosizioneMilitare:
        return self._pos_mili
    
    def set_maternità(self, maternità: IntGEZ|None) -> None:
        if self._genere == Genere.uomo:
            if maternità is not None:
                raise ValueError("Errore! Un uomo non può avere la maternità!")
        if self._genere == Genere.donna and maternità is None:
            raise ValueError("Errore! Una donna deve avere la maternità")

    def maternità(self) -> RealGEZ:
        return self._maternità
    
    def set_nome(self, nome: str) -> None:
        if nome is None:
            raise ValueError("Errore! Il nome non può essere None")
        self._nome = nome

    
    def nome(self) -> str:
        return self._nome
    

    def set_cognome(self, cognome: str) -> None:
        if cognome is None:
            raise ValueError("Errore! Il cognome non può essere None")
        self._cognome = cognome

    def cognome(self) -> str:
        return self._cognome


    def nascita(self) -> date:
        return self._nascita
    

    def cf(self) -> CodiceFiscale:
        return self._cf
    


class PosizioneMilitare:
    _nome: str # mutabile noto alla nascita

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    
    def nome(self) -> str:
        return self._nome
    
class Impiegato:
    _stipendio: RealGEZ # mutabile noto alla nascita
    _ruolo: Ruolo # mutabile noto alla nascita
    _is_responsabile: bool # [0..1]

    def __init__(self,*, stipendio: RealGEZ, ruolo: Ruolo, is_responsabile: bool| None) -> None:
        self.set_stipendio(stipendio)
        self.set_ruolo(ruolo)
        self._is_responsabile = is_responsabile



    
    def set_stipendio(self, stipendio: RealGEZ) -> None:
        self._stipendio = stipendio


    def set_ruolo(self, ruolo: Ruolo) -> None:
        self._ruolo = ruolo

    
    def stipendio(self) -> RealGEZ:
        return self._stipendio
    

    def ruolo(self) -> Ruolo:
        return self._ruolo
    

    def is_responsabile(self) -> bool|None:
        return self._is_responsabile

class Studente:
    _matricola: Matricola

    def __init__(self,*, matricola: Matricola) -> None:
        self.set_matricola(matricola)



    def set_matricola(self, matricola: Matricola) -> None:
        self._matricola = matricola


    def matricola(self) -> Matricola:
        return self._matricola

class Progetto:
    _nome: str

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)

    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def nome(self) -> str:
        return self._nome
    
class resp_progetto:
    @staticmethod
    def add(cls, impiegato: Impiegato, progetto: Progetto) -> None:
        r = cls._link(impiegato, progetto)




if __name__== "__main__":
    
    Pers1: Persona = Persona(nome="Andrea", cognome="Giumi",cf="GMINDR97D15C034R", nascita=15/4/1997,genere=Genere.uomo)
    
    Pers1.set_maternità(2)

    print(Pers1)