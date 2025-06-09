from string import ascii_lowercase

def caesar_cypher_encrypt(s: str, key:int):
    lettere: list[str] = ascii_lowercase

    for i in lettere:
        for l in s:
            if i == l:
                print(i, l)

caesar_cypher_encrypt()