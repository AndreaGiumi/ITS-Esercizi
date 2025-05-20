def Production(n: int):
    return (n + 2) * Production(n + 1)



print(Production(7))