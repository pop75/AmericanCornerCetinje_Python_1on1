# 0. GITHUB LOKACIJA RADIONICE 4



# 1. TEORIJSKA OBRADA FOR PETLJE



# 2. OBRADA FOR PETLJE KROZ PRAKTICNE PRIMJERE
#**************************************************************************
# 2.1. Napisati program koji ispisuje sve clanove liste sa stringovima.
#**************************************************************************
voce = ["jabuka", "banana", "kruska"]
for vocka in voce:
	print(vocka)


#**************************************************************************
# 2.2. Napisati program koji ispisue sva slova rijeci "banana" na ekran
#**************************************************************************
for slovo in "banana":
    print(slovo)


#**************************************************************************
# 2.3. Napisati program koji ispisuje sve clanove liste sa brojevima.
#**************************************************************************
lista_brojeva = [1, 3, 4, 6, 8, 9]
for broj in lista_brojeva:
	print (broj)


#**************************************************************************
# 2.4. Napisati program koji ispisuje prvih 10 cijelih brojeva.
#**************************************************************************
for i in range(1, 11):
	print (i)


#**************************************************************************
# 2.5. Napisati program koji ispisuje unazad brojeve od 10 do 1.
#**************************************************************************
for i in range(10, 0, -1):
	print (i)


#**************************************************************************
# 2.6. Napisati program koji ispisuje sve parne brojeve prve desetice.
#**************************************************************************
for i in range(1, 11, 2):
	print (i)


#**************************************************************************
# 2.7. Napisati program koji ispisuje sve neparne brojeve prve desetice unazad.
#**************************************************************************
for i in range(9, 0, -2):
	print (i)








# 3. ZADACI ZA SAMOSTALAN RAD POLAZNIKA KURSA
#**************************************************************************
# 3.1. Napisati program koji za unijeti broj od korisnika racuna i ispisuje
#      zbir svih cifara do tog broja.
#**************************************************************************
n = int(input("UNesite jedan cijeli broj: "))

suma = 0

for broj in range(1, n+1):
    suma = suma + broj
    
print("Zbir prvih " + str(broj) + " brojeva je: " + str(suma))


#**************************************************************************
# 3.2. Napisati program koji broji koliko ima samglasnike u zadatoj rijeci 
#      koju sa tastature unosi korisnik.
#**************************************************************************
rijec = input("Unesite neku rijec: ")
samoglasnici = "aeiou"
brojac = 0

for slovo in rijec:
    if slovo in samoglasnici:
        brojac = brojac + 1

print("Broj samoglasnika u ovoj rijeci je: " + str(brojac))


#**************************************************************************
# 3.3. Napisati program koji za unijeti broj sa tastature ispisuje sve 
#      parne brojeve do njega.
#**************************************************************************
n = int(input("UNesite jedan cijeli broj"))

for broj in range(1, n+1):
    if broj % 2 == 0:
        print(broj)
    




