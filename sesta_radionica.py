# 0. Github lokacija Radionice 6

# 1. PRAKTIČNI ZADACI SA FUNKCIJAMA

#********************************************************************************
# 1.1. Napisati funkcije koja izracunavaju kvadraturu placa za izgradnju kuce   *
#      i njegovu cijenu. Prva funkcija prima dva parametra iz glavnog programa, *
#      to su duzina i sirina placa u metrima, izracunava povrsinu te parcele,   *
#      i vraca izracunatu povrsinu glavnom programu. Druga funkcija izracunava  *
#      cijenu tog placa na osnovu unesene kvadrature. Kvadrat placa racunati    *
#      po cijeni od 1000 eura.                                                  *
#********************************************************************************

# funkcije
def KvadraturaPlaca(duzina, sirina):
    povrsina = duzina * sirina
    return povrsina
	
def CijenaPlaca(povrsina):
    cijena_po_kvm = 1000		
    cijenaplaca = povrsina * cijena_po_kvm
    return cijenaplaca

# glavni program	
duzinaplaca = input("Unesite duzinu parcele placa: ")
sirinaplaca = input("Unesite sirinu parcele placa: ")

povrsina = KvadraturaPlaca(int(duzinaplaca),int(sirinaplaca))
print("Kvadratura placa je: " + str(povrsina) + "mkv.")

cijenaPlaca = CijenaPlaca(povrsina)
print("Cijena placa je: " + str(cijenaPlaca) + " eura.")



#********************************************************************************
# 1.2. Napisati funkciju koja izracunava proizvod svih elemenata liste. Lista   *
#      ima 3 elementa koji se ucitavaju sa tastature.                           *                      *
#********************************************************************************

# funkcija
def proizvodElemenataListe(listaBrojeva):
    proizvod = 1

    for broj in listaBrojeva:
        proizvod = proizvod * broj
    
    return proizvod

# glavni program
lista_brojeva = []

for i in range(0, 3):
    ulaz = int(input("Unesite %d broj: " %(i+1) ))
    lista_brojeva.append(ulaz)

rezultat = proizvodElemenataListe(lista_brojeva)
print("Proizvod elemenata ove liste je: " + str(rezultat))



#********************************************************************************
# 1.3. Napisati funkciju koja pronalazi najveci element liste. Lista ima 5      *
#      elementa koji se ucitavaju sa tastature.                                 *
#********************************************************************************

# funkcija
def najveciElementListe(listaBrojeva):
    najveci = listaBrojeva[0]

    for i in range(1, len(listaBrojeva)):
        if najveci < listaBrojeva[i]:
            najveci = listaBrojeva[i] 
           
    return najveci

# glavni program
brojevi = []

for i in range(0, 5):
    ulaz = int(input("Unesite %d broj: " %(i+1) ))
    brojevi.append(ulaz)

rezultat = najveciElementListe(brojevi)

print("Unesena lista: " + str(brojevi))
print("Najveci element ove liste je: " + str(rezultat))






#*******************************************************************************
#                               2. PRAKTICNI PROJEKAT 2                        *
#*******************************************************************************
#                        M J E NJ A C N I C A    V A L U T A                   *
#*******************************************************************************
# Info sa: https://www.bankar.me/kursna-lista-crna-gora-centralna-banka/

# Datum kursne liste: 26feb2021

import sys, os

usdolarKupovniKurs = 1.1961
usDolarProdajniKurs = 1.2325
ausDolarKupovniKurs = 1.5379
ausDolarProdajniKurs = 1.5847
canDolarKupovniKurs = 1.5135
canDolarProdajniKurs = 1.5595
funtaKupovniKurs = 0.8602
funtaProdajniKurs = 1.8864
chfKupovniKurs = 1.0638
chfProdajniKurs = 1.0962
jpnKupovniKurs = 126.2376
jpnProdajniKurs =  130.0823

# Funkcije
def IscrtajEkranMjenjacnice():
    print ("==================================================================================*")
    print ("*                             E     U     R     O                                 *")
    print ("*      M     J     E     N     J     A     C     N     I     C     A              *")      
    print ("==================================================================================*")
    print ("*                                                                                 *")
    print ("*     Valuta:             Oznaka:   Kupujemo 1 euro po:   Prodajemo 1 euro po:    *")
    print ("*                                                                                 *")
    print ("*     Americki Dolar        USD            1.1961                1.2325           *")
    print ("*     Australijski Dolar    AUD            1.5379                1.5847           *")
    print ("*     Kanadski Dolar        CAD            1.5135                1.5595           *")
    print ("*     Britanska Funta       GBP            0.8602                0.8864           *")
    print ("*     Svajcarski Franak     USD            1.0638                1.0962           *")
    print ("*     Japanski Jen          JPY          126.2376              130.0823           *")
    print ("*                                                                                 *")
    print ("==================================================================================*")
    print("")


def IzracunajOtkupEura(kolicina_prodaje, valuta_za_isplatu):
    if valuta_za_isplatu == '1':
        isplata = float(kolicina_prodaje) * usdolarKupovniKurs
        print("\n Za isplatu: " + str(isplata) + " americkih dolara")
        
    if valuta_za_isplatu == '2':
        isplata = float(kolicina_prodaje) * ausDolarKupovniKurs
        print("\n Za isplatu: " + str(isplata) + " australijskih dolara")

    if valuta_za_isplatu == '3':
        isplata = float(kolicina_prodaje) * canDolarKupovniKurs
        print("\n Za isplatu: " + str(isplata) + " kanadskih dolara")

    if valuta_za_isplatu == '4':
        isplata = float(kolicina_prodaje) * funtaKupovniKurs
        print("\n Za isplatu: " + str(isplata) + " britanskih funti")

    if valuta_za_isplatu == '5':
        isplata = float(kolicina_prodaje) * chfKupovniKurs
        print("\n Za isplatu: " + str(isplata) + " svajcarskih franaka")

    if valuta_za_isplatu == '6':
        isplata = float(kolicina_prodaje) * jpnKupovniKurs
        print("\n Za isplatu: " + str(isplata) + " japanskih jena")
        

def IzracunajIsplatuEura(kolicina_kupuje, valuta_kojom_kupuje):
    if valuta_kojom_kupuje == '1':
        isplata = float(kolicina_kupuje) * usDolarProdajniKurs
        print("\n Za uplatu: " + str(isplata) + " eura")
        
    if valuta_kojom_kupuje == '2':
        isplata = float(kolicina_kupuje) * ausDolarProdajniKurs
        print("\n Za uplatu: " + str(isplata) + " eura")

    if valuta_kojom_kupuje == '3':
        isplata = float(kolicina_kupuje) * canDolarProdajniKurs
        print("\n Za uplatu: " + str(isplata) + " eura")

    if valuta_kojom_kupuje == '4':
        isplata = float(kolicina_kupuje) * funtaProdajniKurs
        print("\n Za uplatu: " + str(isplata) + " britanskih funti")

    if valuta_kojom_kupuje == '5':
        isplata = float(kolicina_kupuje) * chfProdajniKurs
        print("\n Za uplatu: " + str(isplata) + " eura")

    if valuta_kojom_kupuje == '6':
        isplata = float(kolicina_kupuje) * jpnProdajniKurs
        print("\n Za uplatu: " + str(isplata) + " eura")


# Glavni program
akcija = ""
while akcija != 'q':
    IscrtajEkranMjenjacnice()
    
    akcija = input("Unesi: \n 'p' da prodate vase eure, \
                           \n 'k' za kupite eure, \
                           \n 'q' za kraj programa: ")
    
    if akcija == "p":
        kolicina_prodaje = input("\n Izabrali ste prodaju eura. Unesite kolicinu eura koje prodajete: ")
        valuta_za_isplatu = input("\n Valuta u kojoj zelite isplatu: \n 1 - americki dolar, \n 2 - australijski dolar: " \
                                       " \n 3 - Kanadski dolar \n 4 - Britanska funta " \
                                       " \n 5 - Svajcarski franak \n 6 - Japanski jen ")
        IzracunajOtkupEura(kolicina_prodaje, valuta_za_isplatu)
        
    elif akcija == 'k':
        kolicina_kupuje = input ("\n Izabrali ste kupovinu eura. Unesite kolicinu koju kupujete: ")
        valuta_kojom_kupuje = input("\n Valuta kojom kupujete: \n 1 - americki dolar, \n 2 - australijski dolar: " \
                                       " \n 3 - Kanadski dolar \n 4 - Britanska funta " \
                                       " \n 5 - Svajcarski franak \n 6 - Japanski jen ")        
        IzracunajIsplatuEura(kolicina_kupuje, valuta_kojom_kupuje)

    elif akcija == 'q':
        print ("\n\n Posjetite nas ponovo. Do vidjenja.")
        sys.exit()

    else:
        print("")
        print ("Dozvoljene opcije programa: 'k' ili 'p' ili 'q': ")








