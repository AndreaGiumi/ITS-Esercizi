def HarmonicProgression(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = 1/n * HarmonicProgression(n - 1)
        result_formatted = f"{result:.6f}"
        return float(result_formatted)
    
print(HarmonicProgression(9))