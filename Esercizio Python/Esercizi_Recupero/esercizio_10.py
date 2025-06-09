def binary_search(n: int,v: int, p: int,  lista:list[int] = []):
    if v < lista[v] or v > lista[p]:
        return -1
    while v <= p:
        q = (v + p)/2
        if lista[q] == n:
            return q
        if lista[q] > n:
            r = q - 1
        return -1