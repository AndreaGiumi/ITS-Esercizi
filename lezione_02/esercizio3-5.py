# (3-5)

invitati: list = ["Franccesco Totti", "J-Ax", "Bryan Cranston"]

print(f"Caro {invitati[0]}! Sei invitato alla cena di Natale presso la mia abitazione! Daje vedi di venire!")
print(f"Caro {invitati[1]}! Sei invitato alla cena di Natale presso la mia abitazione! Preparati qualche bella canzone delle tue!")
print(f"Dear {invitati[2]}! You are invited to the Christmas dinner at my home!")

print(f"{invitati[0]} non potrà essere presente alla cena! Recupereremo!")

invitati[0] = "Claudio Ranieri"

print(invitati)

print(f"Caro {invitati[0]}! Sei invitato alla cena di Natale presso la mia abitazione! Daje vedi di venire!")
print(f"Caro {invitati[1]}! Sei invitato alla cena di Natale presso la mia abitazione! Preparati qualche bella canzone delle tue!")
print(f"Dear {invitati[2]}! You are invited to the Christmas dinner at my home!")
