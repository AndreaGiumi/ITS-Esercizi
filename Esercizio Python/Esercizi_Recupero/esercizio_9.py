from string import ascii_lowercase, ascii_uppercase

def caesar_cypher_encrypt(s:str, key:int):
    lettere: list[str] = ascii_lowercase
    for l in s:
        if l in lettere:
            index_l = lettere.index(l) + key
            print(f"{l}, {index_l}")
        if key > index_l:
            mod = index_l % key
            print(mod)
                
caesar_cypher_encrypt("ci", 33)