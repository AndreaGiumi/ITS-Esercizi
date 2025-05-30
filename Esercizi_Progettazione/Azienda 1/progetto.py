from tipi_dato_prog.mytypes import FloatGEZ

class Progetto:
    _nome: str # noto alla nascita
    _budget: FloatGEZ # noto alla nascita


    def __init__(self, nome: str, budget: FloatGEZ) -> None:
        self.setNome(nome)
        self.setBudget(budget)
        


    def getNome(self) -> str:
        return self._nome
    
    def getBudget(self) -> FloatGEZ:
        return self._budget
    

    def setNome(self, nome: str) -> None:
        self._nome = nome

    def setBudget(self, budget: FloatGEZ) -> None:
        self._budget = budget
        

    def __str__(self) -> str:
        return f"Progetto: {self.getNome()} con budget: {self.getBudget()} €"
    

    def __repr__(self) -> str:
        return f"Progetto(nome={self.getNome()}, budget={self.getBudget()})"