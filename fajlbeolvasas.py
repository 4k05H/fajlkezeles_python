nevek = []
nemek = []
korok = []
def beolvas(fajlnev):
    f = open(fajlnev, "r", encoding="utf-8")
    print(f.readline().strip())
    sorok = f.readlines()
    print(sorok)
    feldolgoz(sorok)
    adatszam()
    atlag_eletkor()
    nok()
    legfiatalabb_no()
    f.close()
def feldolgoz(sorok):
    i = 0
    while i < len(sorok):
        print(sorok[i].strip())
        sor = sorok[i].strip().split(", ")
        print(sor)
        nevek.append(sor[0])
        nemek.append(sor[1])
        korok.append(sor[2])
        i += 1

def adatszam():
    print(len(nevek))

def atlag_eletkor():
    eletkor = 0
    for elem in korok:
        eletkor += int(elem)

    aeletkor = eletkor/len(korok)
    print(f"az átlag életkor: {aeletkor}")

def nok():
    no = 0
    for elem in nemek:
        if elem == "nő":
            no += 1

    print(f"a nők száma: {no}")
    return no

def legfiatalabb_no():
    fiatal = 100
    i = 0
    while i < len(korok):
        if (int(korok[i]) < fiatal) and (nemek[i] == "nő"):
            fiatal = korok[i]
        i += 1
    print(f"a legfiatalabb nő: {fiatal}")