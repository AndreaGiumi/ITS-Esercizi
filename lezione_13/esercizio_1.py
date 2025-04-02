def recursivePower(a:int, b:int):
    if b == 0:
        return 1
    else:
        return int(a * recursivePower(a, b - 1))


print(recursivePower(3,4))