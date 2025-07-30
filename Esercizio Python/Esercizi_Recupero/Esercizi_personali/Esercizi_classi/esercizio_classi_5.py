'''
Crea una classe GestoreMagazzino che gestisca un magazzino di prodotti. La classe dovrà avere i seguenti attributi:

    Un dizionario “prodotti” che mappa i nomi dei prodotti ai rispettivi oggetti “Prodotto” (che descriverai in seguito)
    Una variabile “costo_magazzinaggio” che indica il costo per magazzinare ogni prodotto per un mese

La classe dovrà avere i seguenti metodi:

    Un metodo “aggiungi_prodotto” che aggiunga un nuovo prodotto al magazzino
    Un metodo “rimuovi_prodotto” che rimuova un prodotto dal magazzino
    Un metodo “calcola_costi_magazzinaggio” che calcoli i costi di magazzinaggio per tutti i prodotti presenti nel magazzino

Crea inoltre una classe Prodotto che abbia gli attributi “nome”, “prezzo” e “scorta”.

'''



class Prodotto:
    _nome: str
    _prezzo: float
    _scorta: int

    def __init__(self, nome: str, prezzo: float, scorta: int) -> None:
        self.set_nome(nome)
        self.set_prezzo(prezzo)
        self.set_scorta(scorta)
    

    def set_nome(self, nome: int) -> None:
        self._nome = nome

    def nome(self) -> str:
        return self._nome
    
    def set_prezzo(self, prezzo: float) -> None:
        self._prezzo = prezzo

    def prezzo(self) -> float:
        return self._prezzo
    
    def set_scorta(self, scorta: int) -> None:
        self._scorta = scorta

    def scorta(self) -> int:
        return self._scorta
    

class GestoreMagazzino:
    _prodotti: dict[Prodotto,float]
    _costo_magazzinaggio: float


    def __init__(self, costo_magazzinaggio: float) -> None:
        self._prodotti: dict[Prodotto, float] = {}
        self.set_costoMagazzinaggio(costo_magazzinaggio)
    

    def set_costoMagazzinaggio(self, costo_magazzinaggio: float) -> None:
        self._costo_magazzino = costo_magazzinaggio

    def costo_magazzinaggio(self) -> float:
        return self._costo_magazzinaggio
        

    def aggiungi_prodotto(self, prodotto: str) -> dict[Prodotto, float]:
        self._prodotti[prodotto.nome] = prodotto

    def rimuovi_prodotto(self, nome: str) -> None:
        self._prodotti.pop(nome)

    def costi_magazzinaggio(self) -> None:
        costi = 0

        for nome, prodotto in self._prodotti.items():
            costi += prodotto.scorta


if __name__=="__main__":

    p: Prodotto = Prodotto("Barretta", 2.50, 10)

    d_p = GestoreMagazzino(10)


    d_p.aggiungi_prodotto(p)

    print

    


    