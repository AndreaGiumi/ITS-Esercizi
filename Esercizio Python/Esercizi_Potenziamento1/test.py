# def mcd(x: int, y: int)-> int:
#     list_mcd = []
    
#     for i in range(1, min(x,y) + 1):
#         if x % i == 0 and y % i == 0:
#             list_mcd.append(i)
#     print(max(list_mcd))






# mcd(12, 18)

nome = "Andrea"

new = ""
for index, i in enumerate(nome):
    if index % 2 == 1:
       i =  i.upper()
    new += i
print(new)
    


    