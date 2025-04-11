import re
def is_integer(s:str):
   string = bool(re.fullmatch(f"\d+", s))
   return int(string)

    


print(is_integer("-544"))