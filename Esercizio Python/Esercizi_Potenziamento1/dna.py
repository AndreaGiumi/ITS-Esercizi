import re
def isDNA(seq: str) ->bool:
    pattern = bool(re.fullmatch(r"^[AGCT]+$", seq))
    return pattern




def sequence(s1: str, s2: str) ->None:
    
    for i in s1[0:6]:
        for j in s2[-6:]:
            if i == j:



if __name__ == "__main__":


    seq: str = "ACGTGCTGCACTGA"
    seq1: str = "CGTGCTGCACTGAACGT"



    # print(isDNA(seq))
    sequence(seq, seq1)