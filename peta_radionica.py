# 0. GITHUB LOKACIJA RADIONICE 5

# 1. TEORIJSKO OBJASNJENJE FUNKCIJA
#     - BEZ PARAMETARA
#     - SA PARAMETRIMA


# 2. OBRADA FUNKCIJA KROZ PRAKTICNE PRIMJERE

#**********************************************************************
# 2.1. Napisati funkciju bez parametara koja ispisuje na ekran rezultat
#    zbira brojeva 100 i 400.
#**********************************************************************

# definicija funkcije
def Saberi():
    zbir = 100 + 400
    print ("Rezultat sabiranja je: " + str(zbir))


# glavni program
Saberi()



#**********************************************************************
# 2.2. Napisati funkciju koja prima 2 parametra iz glavnog programa, 
#    pomnozi ta dva broja, i vrati rezultat u glavni program. Parametri
#    se uzimaju sa tastature od korisnika.
#**********************************************************************

# definicija funkcije
def Pomnozi(prviBroj, drugiBroj):
    proizvod = prviBroj * drugiBroj
    return proizvod


# glavni program
prviBroj = int(input("Unesite prvi broj: "))
drugiBroj = int(input("Unesite drugi broj: "))
	
rezultat = Pomnozi(prviBroj, drugiBroj)
print("Rezultat mnozenja je: " + str(rezultat))








#**************************************************************************
# 3. PRAKTICNI PROJEKAT 1                                                 *
#**************************************************************************
#                                "BANKOMAT"                               *
#**************************************************************************
# Kontaktirani ste iz menadzmenta banke "Banca Intesa". Od vas je trazeno *
# da kreirate aplikaciju koja ce se koristiti u njihovih 35 bankomata.    *
# Aplikacija mora biti napisana u programskom jeziku Python, i korisnicima*
# mora omogucavati opcije: da izvrse upit stanja na svoj racun, mora      *
# omogucavati korisniku da podigne novac sa racuna ako na njemu ima       *
# sredstava, i mora omogucavati korisniku da uplati novac na svoj racun.  * 
# Ukoliko je korisnik izabrao nepostojecu opciju, mora mu se to kulturno  *
# predociti i ponovo ponuditi neka od funkcionalnosti bankomata.          *
# Za izradu ove aplikacije, Menadzment banke Vam je ponudio novcana       *
# sredstva u iznosu od 5.000 eura.                                        *
#**************************************************************************
 

# za elegantan izlazak iz programa - funkcija exit()
import sys


# inicijalizacija promjenljivih
opcija = ""
bankovniRacun = 0


# Funkcije programa
def iscrtajPocetniEkranBankomata():
    print("\n\n\n\nUnesite akciju: \n 1 - Uplata na bankovni racun" \
                          "\n 2 - Podizanje sa bankovnog racuna" \
                          "\n 3 - Stanje na bankovnom racunu" \
                          "\n q - Kraj")

def depozitNaRacun(bankovniRacun):
    uplata = int(input("Koliko novca uplacujete na svoj racun? "))
    bankovniRacun = bankovniRacun + uplata
    print("\nNakon uplate stanje na Vasem racunu je: " + str(bankovniRacun) + " eura")
    return bankovniRacun

        
def isplataSaRacuna(bankovniRacun):
    isplata = int(input("Koliko novca zelite da Vam se isplati sa racuna? "))
    if isplata <= bankovniRacun:
        bankovniRacun = bankovniRacun - isplata
        print("\nNakon isplate, stanje na Vasem racunu je: " + str(bankovniRacun) + " eura")
        return int(bankovniRacun)
    else:
        print("Nemate dovoljno sredstava na racunu za isplatu.")
        return bankovniRacun


def stanjeNaRacunu(bankovniRacun):
    print("\nStanje na Vasem racunu je: " + str(bankovniRacun) + " eura.")


# Glavni program
while opcija != 'q':
    iscrtajPocetniEkranBankomata()
    
    opcija = input()

    if opcija == '1':
        novostanje = depozitNaRacun(bankovniRacun)
        bankovniRacun = novostanje
        
    elif opcija == '2':
        novostanje = isplataSaRacuna(bankovniRacun)
        bankovniRacun = novostanje
     
    elif opcija == '3':
        stanjeNaRacunu(bankovniRacun)

    elif opcija == 'q':
        sys.exit()

    else:
        print("Unijeli ste nepostojecu opciju. Pokusajte ponovo. \n\n\n" )








#******************************************************************************
#                POTENCIJALNE NADOGRADNJE PROGRAMA 'BANKOMAT'                 *
#******************************************************************************
# 1. Korisnik unosi 4-cifreni PIN kod prije dobijanja glavnog menija. PIN-ovi *
#    korisnika banke se cuvaju u listi sa cijelim brojevima.                  *
#******************************************************************************
# 2. Bankomat dozvoljava korisniku da udje u minus do 300 eura. Preraditi.    *
#******************************************************************************
# 3. Kreirati dugmad za brzi izbor kolicine novca za uplatu/isplatu.          *
#    Na primjer: a-10 eura, b-20 eura, c-50 eura, d-100 eura                  *           *
#******************************************************************************
