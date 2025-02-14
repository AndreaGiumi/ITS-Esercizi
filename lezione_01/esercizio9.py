

nome: str = input("Inserisci nome: ")
vendite: int = int(input("Inserisci vendite: "))

max_nome: str = nome
max_vendite: int = vendite
min_nome: str = nome
min_vendite: int = vendite

i = 1

while i != 5:
        new_nome = input("Inserisci nuovo nome: ")
        new_vendite = (input("Inserisci nuovo valore: "))

        if new_nome > max_nome:
            max_nome = new_nome
            max_vendite = new_vendite
        else:
            if new_vendite < max_vendite:
                min_nome = new_nome
                min_vendite = new_vendite

        i += 1

print(max_nome, max_vendite)
print(min_nome, min_vendite)