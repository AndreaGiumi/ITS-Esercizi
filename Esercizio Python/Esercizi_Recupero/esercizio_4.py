#  Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, e Z) è
# soddisfatta per procedere con un'azione. L'azione può procedere solo se la condizione X
# è vera e almeno una tra Y e Z è vera. La funzione deve ritornare "Azione permessa"
# oppure "Azione negata" a seconda delle condizioni che sono soddisfatte.



def verifica(x: int, y: int, z: int) -> str:
    if x >= 5 and (y + 2 > 15 or z == 10):
        return "Azione permessa"
    else:
        return "Azione negata"
    

print(verifica(5, 12, 1))