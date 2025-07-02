from tipi_dato_prog.mytypes import RealGEZ

class Citta:
    _nome: str
    _num_abitanti: RealGEZ

    def __init__(self, nome: str, num_abitanti: RealGEZ) -> None:
        self.set_nome(nome)
        self.num_abitanti(num_abitanti)

    def nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        self._nome = nome


    def set_abitanti(self, num_abitanti: RealGEZ) -> None:
        self._num_abitanti = num_abitanti

    def num_abitanti(self) -> RealGEZ:
        return self._num_abitanti