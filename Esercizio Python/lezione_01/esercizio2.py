max: int = int(input("Inserisci numero: "))
i: int = 1

while i < 4:
    i += 1
    n: int = int(input("Inserisci numeri: "))
    if n > max:
        max = n

print(f"Questo è il numero più grande: {max}")