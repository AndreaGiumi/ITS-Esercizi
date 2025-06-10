from string import ascii_lowercase, ascii_uppercase

def caesar_cypher_encrypt(s:str, key:int):
    lettere: list[str] = ascii_lowercase
    lettere_upper: list[str] = ascii_uppercase
    for l in s:
        if l in lettere:
            index_l = (lettere.index(l) + key) % 26
            print(lettere[index_l])
        elif l in lettere_upper:
            index_l = (lettere_upper.index(l) + key) % 26
            print(lettere_upper[index_l])
                
caesar_cypher_encrypt("cIao mai", 33)