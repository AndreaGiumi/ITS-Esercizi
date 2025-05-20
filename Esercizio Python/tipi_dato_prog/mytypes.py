from typing import Self, Any
from enum import *
from datetime import datetime, date
import re

class Genere(StrEnum):
    uomo = auto()
    donna = auto()


class Continente(StrEnum):
    asia = auto()
    europa = auto()
    america = auto()
    africa = auto()
    antartide = auto()


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
    def __new__(cls, v:float|Self) -> Self:
        if v < 0.00:
            raise ValueError(f"Value v == {v} must be greater or equal than 0.00")
        return float.__new__(cls, v)



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
    


    def __eq__(self, other: Any) -> bool:
        if other is None or \
                not isinstance(other, type(self)) or \
                hash(self) != hash(other):
            return False
        return self._via == other._via and self._civico == other._civico
    



class Data:
    _data:str

    def __init__(self, data:str) -> None:
        self._data:date = datetime.strptime(data,"%d.%m.%Y").date()

    def data(self) -> str:
        return self._data
    

    def __hash__(self) -> int:
        return hash(self._data)
    

    def __eq__(self, other: Any) -> bool:
        if other is None or \
                not isinstance(other, type(self)) or \
                hash(self) != hash(other):
            return False
        return self._data == other._data
    

class Anno:
    _anno: int
    def __init__(self, anno: int):
        self.anno(anno)

    def anno(self, anno: int):
        if anno < 1900:
            print("Inserire anno compreso tra 1900 ad oggi")
        else:
            self._anno = anno


    def get_anno(self) -> int:
        return self._anno
    
    def __hash__(self) -> int:
        return hash(self._anno)
        
    def __eq__(self, other: Any) -> bool:
        if other is None or \
                not isinstance(other, type(self)) or \
                hash(self) != hash(other):
            return False
        return self._anno == other._anno


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
    


    class CodiceFiscale:
        _cf: str = r"[A-Z]{6}[0-9]{2}[A-EHLMPRST][0-9]{2}[A-Z0-9]{4}[A-Z]$"
        def __init__(self, codice) -> None:
            codice = codice.upper()
            if not re.findall(self.cf, codice):
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
               
        