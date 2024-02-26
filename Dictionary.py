import random
stacja = {
    "tvp" : 10,
    "polsat": 11,
    "netflix" : 12,
    "tvn" : 13,
    "hbo" : 14


}
def wys_all():
    for kor, por in stacja.items():
        print(kor,"numer stacji:", por)
def wys(lol):
    flaga = 0
    for program, id in stacja.items():
        if lol == program:
            print(program, ":", id)
            flaga = 1
            break
    if flaga == 0:
        print("nie ma podanej stacji!")

def dod(x, y):
    stacja.update({x : y})

def los():

    x = random.randint(10,15)
    for i,j in stacja.items():
        if x == j:
            print("wylosowales:", i, "o numerze:",j)




dior = int(input("1: wyswietlic wszystkich \n2: wyswietlic wybrane \n3: dodac element\n4: losowy\nwpisz numer: "))




if dior == 1:
    wys_all()
elif dior == 2:
    lol = input("podaj stacje: ")

    wys(lol)
if dior == 3:
    pl = input("podaj nazwe stacji: ")
    kl = int(input("podaj numer stacji: "))
    dod(pl, kl)
    wys_all()
if dior == 4:
    los()
