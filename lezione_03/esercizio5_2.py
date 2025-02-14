n: int = int(input("Inserisci numero: "))

if n % 1 == 0 and n > 0:
    sum = 0
    i = 1

    while i > n:
        print(sum)
        sum += sum + i * i
        i += 1

else:
    print("Errore! n deve essere positivo")