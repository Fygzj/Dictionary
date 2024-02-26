from animals import Kon,Mysz,Zolwie

kon_bengalski = Kon("bengalski", 10, 23)
kon_arabski = Kon("Arabski", 12, 32)
myszoskoczek = Mysz("myszkoskoczek", 1, 3)
mysz_polna = Mysz("Polna", 2, 2)
mysz_gorska = Mysz("gorska", 1, 4)
zolw_wodny = Zolwie("Wodny", 0.2, 25)
zolw_ladowy = Zolwie("ladowy", 0.4, 76)
test = Kon("test", 10, 10)


zwierzaki = {
    1.1 : kon_bengalski,
    2.2 : myszoskoczek,
    1.2: kon_arabski,
    2.3: mysz_polna,
    2.4 : mysz_gorska,
    3.1 : zolw_wodny,
    3.2 : zolw_ladowy,
    1.4 : test

}

def wys_all():
    for id, name in zwierzaki.items():
        print(type(name).__name__, name.race, id)
def wysz(x):
    for op, nazwa in zwierzaki.items():
        if x == nazwa.race:
            print(type(nazwa).__name__, nazwa.race)


def wys(x):
    k = 0


    for id, race in zwierzaki.items():
        if str(id).startswith(x):
            k=k+1



            print(f"{k}:",race.race, "wiek:", race.age,"szybkosc:", race.speed)







#def dane():




odp = int(input("1: wybranie grupy\n2: wyszukanie konkretnego\n3: wyswietlic wszyskie\nopd: "))
if odp == 1:
    kop = input("konie = 1\nmyszy = 2\nzolwie = 3\nco znalezc: ")
    wys(kop)
elif odp == 2:
    pop = input("podaj nazwe: ")
    wysz(pop)
elif odp == 3:
    wys_all()

