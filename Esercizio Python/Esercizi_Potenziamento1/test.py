# def mcd(x: int, y: int)-> int:
#     list_mcd = []
    
#     for i in range(1, min(x,y) + 1):
#         if x % i == 0 and y % i == 0:
#             list_mcd.append(i)
#     print(max(list_mcd))






# mcd(12, 18)

# nome = "Andrea"

# new = ""
# for index, i in enumerate(nome):
#     if index % 2 == 1:
#        i =  i.upper()
#     new += i
# print(new)
    




# def rimbalzo() -> None:
#     tempo: int = 0
#     altezza: float = 0.0
#     velocita: float = 100.0
#     rimbalzi: int = 0

#     while rimbalzi <= 5:
#         print(f"Tempo: {tempo} Altezza: {altezza:.2f}")

#         altezza += velocita
#         velocita -= 96

#         if altezza < 0:
#             altezza *= -0.5
#             velocita *= -0.5
#             rimbalzi += 1
#             print(f"Tempo: {tempo} Rimbalzo!")


#         tempo += 1
    

 
# rimbalzo()


def media(numbers: list[int]) -> int:
    for num in numbers:
        result = sum(numbers) / len(numbers)
    return f"{result:.2f}"



lis = [5, 4, 7, 51, 2, 0, 14, 7, 47]


print(media(lis))
