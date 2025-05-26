from typing import Self, Any
from enum import *
from datetime import datetime, date
import re

class Genere(StrEnum):
    uomo = auto()
    donna = auto()


class Continente(StrEnum):
    Asia = auto()
    Europa = auto()
    America = auto()
    Africa = auto()
    Antartide = auto()


class Voto(int):
    def __new__(cls, v:int|float|Self) -> Self:
        if v < 18 or v > 30:
            raise ValueError(f"Value v == {v} must be beetween 18 and 30")
        return int.__new__(cls, v)
    

class IntGEZ(int):
    def __new__(cls, v:int|float|Self) -> Self:
        if v < 0:
            raise ValueError(f"Value v == {v} must be greater or equal than 0")
        return int.__new__(cls, v)
    
class FloatGEZ(float):
    def __new__(cls,v: float|int|str|bool|Self) -> Self:
        n: float = super().__new__(cls, v)

        if n >=0:
            return n
        
        raise ValueError(f"Il valore {n} è negativo!")
    

class Valuta(str):
    def __new__(cls, v: str) -> Self:
        if re.fullmatch(f"^[A-Z]{3}", v):
            return super().__new__(cls, v)
        raise ValueError("Il codice {v} non è un codice valido per una valuta!")

class Telefono(str):
    def __new__(cls, v: str) -> Self:
        if re.fullmatch(f"^[0-9]{10}", v):
            return super().__new__(cls, v)
        raise ValueError("Il codice {v} non è un codice valido per una valuta!")

class Denaaro:
    # Rappresenta il tipo di dato concettuale composto
    # con i seguenti campi:
    # -importo: Reale
    # -valuta: Valuta
    _importo: float
    _valuta: Valuta

    def __init__(self, imp: float, val: Valuta) -> None:
        self._importo = imp
        self._valuta = val

    def importo(self) -> float:
        return self._importo
    

    def valuta(self)-> Valuta:
        return self._valuta
    
    def __str__(self) ->str:
        return f"{self.importo()} {self.valuta()}"
    

    def __repr__(self) ->str:
        return f"Denaro: {self.importo()} unità di valuta {self.valuta()}"
    

    def __hash__(self) ->int:
        return hash((self.importo(), self.valuta()))
    

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, type(self)) or \
            hash(self) != hash(other):
            return False
        return self.importo() == other.importo() and \
            self.valuta() == other.valuta()
        

    def __add__(self, other: Self) -> Self:
        
        """Somma self ad un'altra istanza di Denaro , ma solo se la valuta è la stessa
        Restituisce una nuova istanza di Denaro"""

        if self.valuta() != other.valuta():
            raise ValueError(f"Non posso sommare importi con due valute diverse")
        
        somma: float = self.importo() + other.importo()
        return Denaaro(somma, self.valuta())


class FloatDenaro(float):
    _valuta: Valuta
    def __new__(cls, imp: float, val: Valuta) -> Self:
        d = super().__new__(imp)
    
        d._valuta = val
        return d
    

    def importo(self) -> float:
        return self.real
    

    def valuta(self)-> Valuta:
        return self._valuta        

    def __str__(self) ->str:
        return f"{self.real} {self.valuta()}"
    

    def __repr__(self) ->str:
        return f"Denaro: {self.importo()} unità di valuta {self.valuta()}"
    

    def __hash__(self) ->int:
        return hash((self.importo(), self.valuta()))
    

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, type(self)) or \
            hash(self) != hash(other):
            return False
        return self.importo() == other.importo() and \
            self.valuta() == other.valuta()
        

    def __add__(self, other: Self) -> Self:
        
        """Somma self ad un'altra istanza di Denaro , ma solo se la valuta è la stessa
        Restituisce una nuova istanza di Denaro"""

        if self.valuta() != other.valuta():
            raise ValueError(f"Non posso sommare importi con due valute diverse")
        
        somma: float = self.importo() + other.importo()
        return FloatDenaro(somma, self.valuta())


    def __sub__(self, other: Self) ->Self:
        return self + FloatDenaro(-other, other.valuta())  



class Indirizzo:
    _via: str
    _civico: int

    def __init__(self, via: str, civico: int) -> None:
        self._via = via
        self._civico = civico

    def via(self) -> str:
        return self._via
    
    def civico(self) -> int:
        return self._civico
    

    def __hash__(self) -> int:
        return hash((self._via, self._civico))
    
    def __str__(self):
        return f"\nVia: {self._via}\nCivico: {self._civico}"
    
    def __eq__(self, other: Any) -> bool:
        if other is None or \
                not isinstance(other, type(self)) or \
                hash(self) != hash(other):
            return False
        return self._via == other._via and self._civico == other._civico
    

    

class Anno:
    def __init__(self, anno: int):
        if not isinstance(anno, int):
            raise TypeError("L'anno deve essere un numero intero.")
        if anno < 1900 or anno > 9999:
            raise ValueError(f"Anno non valido: {anno}. Deve essere >= 1900 e un numero di 4 cifre.")
        self._anno = anno


    def __hash__(self) -> int:
        return hash(self._anno)
        
    def __eq__(self, other: Any) -> bool:
        if other is None or \
                not isinstance(other, type(self)) or \
                hash(self) != hash(other):
            return False
        return self._anno == other._anno
    
    def __str__(self):
        return f"Anno: {self._anno}"


class Email:
    _re_mail: str = r"[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-z]{2,}$"
    def __init__(self, email) -> None:
        email = email.lower()
        if not re.findall(self._re_mail, email):
            raise ValueError(f"Email non valida {email}")
        self._re_mail = email
        

    def re_mail(self) -> str:
        return self._re_mail        
    


    def __hash__(self) -> int:
        return hash(self._re_mail)
        
    def __eq__(self, other: Any) -> bool:
        if other is None or \
                not isinstance(other, type(self)) or \
                hash(self) != hash(other):
            return False
        return self._re_mail == other._re_mail
    
    def __str__(self):
        return f"Email: {self._re_mail}"
    


class CodiceFiscale:
    _cf: str = r"[A-Z]{6}[0-9]{2}[A-EHLMPRST][0-9]{2}[A-Z0-9]{4}[A-Z]$"
    def __init__(self, codice) -> None:
        codice = codice.upper()
        if not re.findall(self._cf, codice):
            raise ValueError(f"Codice Fiscale non valido {codice}")
        self._cf = codice



    def cf(self) -> bool:
        return self._cf
        

    def __hash__(self) -> int:
        return hash(self._cf)
        
    def __eq__(self, other: Any) -> bool:
        if other is None or \
                not isinstance(other, type(self)) or \
                hash(self) != hash(other):
            return False
        return self._cf == other._cf


    def __str__(self):
        return f"Codice Fiscale: {self._cf}"
    


class Matricola:
    def __init__(self, matricola: str):
        if not isinstance(matricola, str):
            raise ValueError("La matricola deve essere un numero intero")
        if len(matricola) < 5 or len(matricola) > 5:
            raise TypeError(f"Matricola non valida: {matricola}. Deve essere un numero di 5 cifre.")
        self._matricola = matricola


    def __hash__(self) -> int:
        return hash(self._matricola)
        
    def __eq__(self, other: Any) -> bool:
        if other is None or \
                not isinstance(other, type(self)) or \
                hash(self) != hash(other):
            return False
        return self._matricola == other._matricola
    
    def __str__(self):
        return f"Matricola: {self._matricola}"

        
               
        