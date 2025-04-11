def vowelsCounter(s:str):
    if len(s) > 0:
        if s not in ["a", "e", "i", "o", "u"]:
            s[0].lower = 0 + vowelsCounter(s[1:])
        else:
            s[0].lower = 1 + vowelsCounter(s[1:])
vowelsCounter("Ciao")