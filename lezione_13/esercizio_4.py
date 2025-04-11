def recursiveDigitCounter(n:int):
    if n < 10:
        return 1
    else:
        if n >= 10:
            return n / recursiveDigitCounter(n-1)
        
    


print(recursiveDigitCounter(25))