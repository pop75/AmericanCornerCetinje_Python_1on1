# 0. Upotreba Github lokacie za citanje kodova

# 1. Prihvatanje unosa od strane korisnika

broj = int(input("Unesite neki cijeli broj: "))
kvadrirani = broj * broj
print("Kvadrirani broj je: " + str(kvadrirani))

ime = input("Unesite vase ime: ")
prezime = input("Unesite vase prezime: ")
godine = input("Unesite broj godina: ")
skola = input("Unesite ime vase skole: ")

print("Vi se zovete " + ime + " " + prezime + ", imate " \
      + godine + " godina, " + "a vasa skola se zove " + skola)


# 2. Liste. Elementi liste. Indeksi(pozicije) u listi. Dodavanje u listu.
#    Brisanje elementa iz liste. Praznjenje liste.
#    Ispis prvog elementa liste. Ispis zadnjeg elementa liste.
#    Ispis opsega elemenata iz liste.

# lista stringova
imena = ["Ana", "Biljana", "Marija", "Ksenija"] 
#pozicija  0        1          2         3
print(imena)


# lista integera
desetice = [10, 20, 30, 40, 50, 60, 70]         
#pozicija    0   1   2   3   4   5   6
print(desetice)
print(len(desetice))

# lista float-ova. duzina liste.
meteo = [-1.5, 2.5, 15.0, 23.4, 33.5]           
#pozicija  0    1     2     3     4
print(meteo)
print(len(meteo))

# dodavanje elemenata u listu sa funkcijom 'append'
listaimena = []
listaimena.append("Bosko")
listaimena.append("Mihailo")
listaimena.append("Janko")
print(listaimena)

# brisanje elementa iz liste sa funkcijom 'remove'.
listadesetica = [10, 20, 30, 40, 50]
print(listadesetica)
listadesetica.remove(10)
print(listadesetica)

# brisanje sa odredjene pozicije(indeksa)
listadesetica.pop(3)
print(listadesetica)

# praznjenje liste
lista = ["marko", "janko", "bosko"]
print(lista)
lista.clear()
print(lista)

# ispis prvog elementa liste
rase = ["doberman", "haski", "terijer", "vucjak"]
print(rase)
print(rase[0])

# ispis zadnjeg elementa liste
print(rase[-1])

# ispis opsega elemenata iz liste: prva dva elementa
print(rase[0:2])

# ispis opsega elemenata iz liste: zadnja dva elementa
print(rase[-2:])

# ispis opsega elemenata iz liste: srednja dva elementa
print(rase[1:3])

# ispis opsega elemenata iz liste: od drugog do kraja
print(rase[1:])

# ispis opsega elemenata iz liste u obrnutom redosljedu
rase.reverse()
print(rase)

# sortiranje liste po abecednom redu
rase.sort()
print(rase)

# sortiranje liste u obrnutom redu
rase.sort(reverse = True)
print(rase)


# 3. Zadaci sa listama
#====================================================================================
#                                   Z A D A C I
#====================================================================================
# 1. Unijeti rucno 2 liste sa po 3 elementa koji su cijeli brojevi.
#   Napraviti trecu listu ciji su elementi zbirovi elemenata prethodne dvije
#   liste po odgovarajucim pozicijama

lista1 = [10, 20, 30]
lista2 = [40, 50, 60]
print(lista1)
print(lista2)

lista3 = [lista1[0] + lista2[0], lista1[1] + lista2[1], lista1[2] + lista2[2]]
print(lista3)


# 2. Unijeti rucno 2 liste sa po 3 elementa koji su cijeli brojevi.
#   Napraviti trecu listu ciji su elementi: zbir prvog i treceg elemenata,
#   zbir drugih pozicija, i zbir trece i prve pozicije u listama.

prvalista = [30, 20, 10]
drugalista = [40, 50, 60]
print(prvalista)
print(drugalista)

trecalista = [prvalista[0] + drugalista[2], prvalista[1] + drugalista[1], prvalista[2] + drugalista[0]]
print("Rezultujuca lista je: " + str(trecalista))


#3. Unijeti rucno dvije liste sa po 4 jednocifrena elementa. Kreirati trecu listu kao proizvod
#   odgovarajucih elemenata ove dvije liste.
prvalista = [1, 3, 5, 7]
drugalista = [2, 4, 6, 8]
print(prvalista)
print(drugalista)

rezultujucalista = [prvalista[0] * drugalista[0], prvalista[1] * drugalista[1], \
                    prvalista[2] * drugalista[2], prvalista[3] * drugalista[3]]
print("Rezultujuca lista je:" + str(rezultujucalista))


#=====================================================================================