def baricentro(v: list[int]):
    for i in range(len(v)):
        if sum(v[:i+1]) == sum(v[i+1:]):
            return i
        else:
            return None
        

if __name__=="__main__":
    v = [1,2,3,3,2,1]

    print(baricentro(v))