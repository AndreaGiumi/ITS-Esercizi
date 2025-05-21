from mytypes import CodiceFiscale, FloatGEZ, Continente, Voto, IntGEZ, Indirizzo, Anno, Data, Email, Genere


ciao: Indirizzo = Indirizzo("Via Valente", 6)


print(ciao)



if isinstance(ciao, Indirizzo):
    print(f"\nciao è istanza della classe Indirizzo")




scorso: Anno = Anno(2077)


print(scorso)



if isinstance(scorso, Anno):
    print(f"\nscorso è istanza della classe Anno")



ieri: Data = Data("20.5.2025")

print(ieri)


mai: Email = Email("andreagiumi97@gmail.com")

print(mai)

if isinstance(mai, Email):
    print("ciao")



mio: CodiceFiscale = CodiceFiscale("gmindr97d15c034r")

print(mio)



ci: FloatGEZ = FloatGEZ(25)

print(ci)




print(list(Continente))



ita: Voto = Voto(25)


print(ita)


ing: IntGEZ = IntGEZ(22.2)

print(ing)


print(list(Genere))