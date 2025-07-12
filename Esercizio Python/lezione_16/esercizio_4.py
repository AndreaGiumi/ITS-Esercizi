class Specie:
    _nome: str
    _popolazione: int
    _tasso_crescita: float

    def __init__(self, nome: str, popolazione: int, tasso_crescita: float) -> None:
        self.set_nome(nome)
        self.set_popolazione(popolazione)
        self.set_tasso_crescita(tasso_crescita)



    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def nome(self) -> str:
        return self._nome
    
    def set_popolazione(self, popolazione: int) -> None:
        self._popolazione = popolazione

    def popolazione(self) -> int:
        return self._popolazione
    
    def set_tasso_crescita(self, tasso_crescita: float) -> None:
        self._tasso_crescita = tasso_crescita

    def tasso_crescita(self) -> float:
        return self._tasso_crescita
    

    def crescita(self) -> int:
        nuova_popolazione: int = self.popolazione() * (1 + self.tasso_crescita()/100)
        return nuova_popolazione
    

    def anni_per_superare(self, altra_specie: 'Specie') -> int:
        pass



class BufaloKlingon(Specie):
    _nome_specie: str

    def __init__(self, nome, popolazione, tasso_crescita):
        super().__init__(nome, popolazione, tasso_crescita)
        self._nome_specie = nome


class Elefante(Specie):
    _nome_specie: str
    def __init__(self, nome, popolazione, tasso_crescita):
        super().__init__(nome, popolazione, tasso_crescita)

        self._nome_specie = nome