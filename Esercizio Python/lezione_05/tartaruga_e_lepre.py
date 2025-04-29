import random

percorso:list[int] = ["'_'"] * 70

def tartaruga(t:int):
     r1 = random.randint(1,10)
     if 1 <= r1 <= 5:      #passo veloce
            t += 3
     if 6 <= r1 <= 7:      #scivolata
         t -= 6
         if t < 1:
              t = 1
     if 8 <= r1 <= 10:     #passo lento
         t += 1


def lepre(h:int):
     r1 = random.randint(1,10)
     if 1 <= r1 <= 2:     #riposo
          h += 0
     if 3 <= r1 <= 4:     #grande balzo
          h += 9
     if r1 == 5:          #grande scivolata
         h -= 9
         if h < 1:
              h = 1
     if 6 <= r1 <= 8:     #piccolo balzo
         h += 1
     if 9 <= r1 <= 10:    #piccola scivolata
         h -= 2
         if h < 1:
              h = 1
     

def gara():
     t = 1
     h = 1
     while True:
          percorso = ['_'] * 70
          t = tartaruga(t)
          h = lepre(h)

