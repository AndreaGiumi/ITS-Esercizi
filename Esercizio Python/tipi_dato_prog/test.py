from mytypes import CodiceFiscale, FloatGEZ, Continente, Voto, IntGEZ, Indirizzo, Anno, Data, Email, Genere, Matricola
from typing import Any


ciao: Indirizzo = Indirizzo("Via Valente", 6)


# print(ciao)



# if isinstance(ciao, Indirizzo):
#     print(f"\nciao è istanza della classe Indirizzo")




scorso: Anno = Anno(2077)


# print(scorso)



# if isinstance(scosrso, Anno):
#     print(f"\nscorso è istanza della classe Anno")



ieri: Data = Data("20.5.2025")
# if isinstance(ieri, Data):
#     print(f"\nieri è istanza della classe Data")
# print(ieri)


mai: Email = Email("andreagiumi97@gmail.com")

# print(mai)

# if isinstance(mai, Email):
    # print(f"\nmai è un istanza della classe Email ")



mio: CodiceFiscale = CodiceFiscale("gmindr97d15c034r")
# if isinstance(mio, CodiceFiscale):
    # print(f"\nmio è un istanza della classe CodiceFiscale ")

# print(mio)



ci: FloatGEZ = FloatGEZ(25)
# if isinstance(ci, FloatGEZ):
    # print(f"\nci è un istanza della classe FloatGEZ ")
# print(ci)




# print(list(Continente))



ita: Voto = Voto(25)
# if isinstance(ita, Voto):
    # print(f"\nita è un istanza della classe Voto ")

# print(ita)


ing: IntGEZ = IntGEZ(22.2)
# if isinstance(ing, IntGEZ):
    # print(f"\ning è un istanza della classe IntGEZ ")
# print(ing)


# print(list(Genere))


matr: Matricola = Matricola("25145")
matr2 : Matricola = Matricola("25145")
# if isinstance(matr, Matricola):
    # print(f"\nmatr è un istanza della classe Matricola ")

# print(matr)


print(matr == matr2)

my_set: set[Any] = {matr, ita, ci, mai}



print(type(matr))

print(my_set)