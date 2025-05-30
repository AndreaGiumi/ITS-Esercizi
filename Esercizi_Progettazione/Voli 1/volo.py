from typing import Any   
from tipi_dato_prog.mytypes import *
from compagnia import Compagnia
class Volo:
    _codice: CodiceVolo # noto alla nascita
    _durata: IntGEZ # noto alla nascita
    _volo_comp: Compagnia # noto alla nascita

    def __init__(self, codice: CodiceVolo, durata: IntGEZ, volo_comp: Compagnia) -> None:
        self.set_codice(codice)
        self.set_durata(durata)
        self.set_volo_comp(volo_comp)
        

    def set_codice(self, codice: CodiceVolo) ->None:
        self._codice = codice

    def set_durata(self, durata: IntGEZ) -> None:
        self._durata = durata


    def set_volo_comp(self, volo_comp: Compagnia) -> None:
        self._volo_comp = volo_comp

    
    def codice(self) -> CodiceVolo:
        return self._codice
    

    def durata(self) -> IntGEZ:
        return self._durata
    

    def volo_comp(self) -> Compagnia:
        return self._volo_comp
    

    def __hash__(self) -> int:
        return hash(self._codice)
    
    def __eq__(self, other: Any)  -> bool:
        if other is None or \
                not isinstance(other, type(self)) or \
                hash(self) != hash(other):
            return False
        return self._codice == other._codice
        
    


    def __str__(self) -> str:
        return f"Codice volo: {self._codice} \nDurata volo: {self._durata}"
    
    def __repr__(self):
        return f"Volo(codice={self.codice()}, durata={self.durata()})"