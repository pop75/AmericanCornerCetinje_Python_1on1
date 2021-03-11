# 0. Github lokacija danasnjeg predavanja i pripadajucih kodova



# 1. Teorijsko objasnjenje if, if-else, if-elsif-else iskaza 



# 2. Uvjezbavanje na prakticnim primjerima


#*******************************************************************************
# 1. Napisati program koji ispituje da li prvi broj veci od drugog.
#*******************************************************************************

a = 5
b  = 4
if a > b:
    print("a je vece od b")



#*******************************************************************************
# 2. Napisati program kojim se sa tastature unose 2 broja, ispituje koji je od
#    dva unijeta broja veci, i ispisuje na ekran rezultat poredjenja.
#*******************************************************************************

a = int(input("Unesite prvi broj: "))
b  = int(input("Unesite drugi broj: "))
if a > b:
    print("Prvi broj veci od drugog")
else:
    print("Drugi broj je veci od porvog")



#******************************************************************************
# 3. Napisati program koji ispituje koje svijetlo na semaforu je upaljeno.
#    Korisnik unosi sa tastature slovo z, ili n ili c. Zavisno od unosa, na
#    ekran se ispisuje koje svijetlo je upaljeno. Ako nije uneseno nijedno od
#    navedenh slova, na ekran se ispisuje da je semafor pokvaren.
#******************************************************************************

svijetlo = input("Unesite 'z' ili 'n' ili 'c': ")
if (svijetlo == 'z'):
    "Na semaforu je upaljeno zeleno svijetlo."
elif (svijetlo == 'n'): 	
    "Na semaforu je upaljeno narandzasto svijetlo."
elif (svijetlo == 'c'):
    "Na semaforu je upaljeno crveno svijetlo."
else:
    "Semafor je pokvaren."



#******************************************************************************
# 4. Data je lista sa elementima 3, 6, 7, i 4. Ispitati da li je zbir prva dva
#    elementa liste veci od zbira druga dva elementa liste. Ispisati na ekran
#    rezultat poredjenja.
#******************************************************************************

brojevi = [3, 6, 7, 4]

if brojevi[0] + brojevi[1] > brojevi[2] + brojevi[3]:
    print("Veci zbir je kod prva dva elementa.")
else:
    print("Veci zbir je kod druga dva elementa.")



#******************************************************************************
# 5. Lista sadrzi 6 elemenata. To su 1, 3, 5, 2, 4, 3. Ispitati da li je zbir
#    elemenata na parnim pozicijama liste veci od zbira neparnih elemenata liste, i ispitati
#    rezultat na ekran. Ako su isti, onda to ispisati da su zbirovi jednaki.
#******************************************************************************

breskvice = [1, 2, 6, 3, 2, 4]

zbirparnih = breskvice[0] + breskvice[2] + breskvice[4]
zbirneparnih = breskvice[1] + breskvice[3] + breskvice[5]

if zbirparnih > zbirneparnih:
    print("Zbir parnih elemenata liste je veci.")    
elif zbirparnih < zbirneparnih:
    print("Zbir neparnih elemenata liste je veci.")
else:
    print("Zbirovi su jednaki.")






# 3. Prakticni / samostalni rad za polaznike kursa

#******************************************************************************
# 1. Korisnik unosi 2 liste cijelih brojeva s po 5 elemenata. Program ispituje 
#    koja od lista ima veci element na poziciji 2, i u zavisnosti od toga 
#    ispisuje cijelu listu na ekran.
#******************************************************************************
lista1 = [1, 3, 5, 7, 9]
lista2 = [2, 4, 6, 8, 0]
print("Sadrzaj u listi 1: " + str(lista1))
print("Sadrzaj u listi 2: " + str(lista2))

if lista1[2] > lista2[2]:
    print("Broj na poziciji 2 je veci u prvoj listi, to je broj " + str(lista1[2]))
else:
    print("Broj na poziciji 2 je veci u drugoj listi, to je broj " + str(lista2[2]))



#******************************************************************************
# 2. Korisnik unosi 2 liste cijelih brojeva s po 5 elemenata. Program ispituje 
#    koja od lista ima veci element na poslednjoj poziciji, i u zavisnosti 
#    od toga ispisuje cijelu listu unazad na ekran.
#******************************************************************************
lista1 = [154, 223, 543, 243, 922]
lista2 = [776, 439, 648, 832, 933]
print(lista1)
print(lista2)

if lista1[-1] > lista2[-1]:
    print("Lista1 ima veci element na poslednjoj poziciji: " + str(lista1[-1]))
    lista1.reverse()
    print("Ispisana unazad ova lista ima sledeci raspored: " + str(lista1))
else:
    print("Lista2 ima veci element na poslednjoj poziciji: " + str(lista2[-1]))
    lista2.reverse()
    print("Ispisana unazad ova lista ima sledeci raspored: " + str(lista2))



#******************************************************************************
# 3. Korisnik unosi 3 razlicita broja sa tastature. Napisati program koji ispituje koji 
#    je broj najveci i ispisuje ga na ekran korinsiku.
#******************************************************************************
prvibroj = int(input("Unesi prvi broj: "))
drugibroj = int(input("Unesi drugi broj: "))
trecibroj = int(input("Unesi treci broj: "))

if prvibroj > drugibroj and prvibroj > trecibroj:
    print("Najveci broj je: " + str(prvibroj))
elif drugibroj > prvibroj and drugibroj > trecibroj:
    print("Najveci broj je: " + str(drugibroj))
elif trecibroj > prvibroj and trecibroj > drugibroj:
    print("Najveci broj je: " + str(trecibroj))

