# 0. Github lokacija za predavanja i domace zadatke.
# https://github.com/pop75/AmericanCornerCetinje_Python_1on1



# 1. Download Python 3.6.0
# Lokacija: https://www.python.org/downloads/release/python-360/
# Provjera instalacije iz cmd linije Windowsa 10.



# 2. Objasnjenje okruzenja, Python shell i Python Editor IDLE.



# 3. Pisanje i pokretanje prvog Python programa 'Zdravo svijete'.
print("Zdravo svijete")
print("Zdravo, ja sam Marko Markovic")
print("Zdravo, " + "ja se zovem: " + "Nikola Nikolic")



# 4. Osnovni tipovi podataka: int, string, float. Ispis na ekran. Promjenljive.
# Cijeli broj je 3, "sunce" je string, 4.56 je decimalni broj tj. float.
broj = 3
rijec = "sunce"
temperatura = 4.56

print(broj)
print(rijec)
print(temperatura)



# 5. Konverzija izmedju tipova. Tumacenje gresaka interpretera kod izvrsenja programa.
broj = 10
print("U promjenljivoj broj je: " + broj)              #  => greska!!!
# ne radi, jer je promjenljiva 'broj' tipa INTEGER!
# potrebna konverzija u tip STRING
print("U promjenljivoj broj je: " + str(broj))         # => OK!

# identicno je sa tipom float
temperatura = 45.5
print("Trenutna temperatura je: " + temperatura)       #  => greska!!!
print("Trenutna temperatura je: " + str(temperatura))  #  => OK!



# 6. Prihvatanje ulaza od korisnika sa tastature.
ime = input("Unesite vase ime: ")
print("Vase ime je: " + ime)
prezime = input("Unesite vase prezime: ")
print("Vase prezime je: " + prezime)
godine = input("Koliko imate godina: ")
print("Vi se zovete " + ime + " " + prezime + " i imate " + godine + " godina")



# 7. Pregled radionice 1. Pitanja i odgovori.





