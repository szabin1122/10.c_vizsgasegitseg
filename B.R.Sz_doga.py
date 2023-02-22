# Tessék bekérni a vett fa mennyiségét a felhasználótól
vett_fa = int(input('Adja meg a vásárolt fa mennyiségét "kg"-ban:'))
# Ha ez a mennyiség nagyobb 500-nl, akkor írjuk ki, hogy "Elég fát vettünk télire"
if vett_fa > 500:
    print('Elég fát vettünk télire.')
# Ha kissebb mint 500, akkor írjuk ki, hogy "Télire ez kevés lesz, venni kell még fát"
if vett_fa < 500:
    print('Télire ez kevés lesz, venni kell még fát!')
# Kérjük be a felhasználó nevét, és köszönjünk neki
nev = input('Mi a neved?')
print('Szia, ' + nev)
# Kérjük be a felhasználó nemét, és a megadott szöveget e szerint írja ki
nem = int(input('Mi a neme? (1=Férfi 2=Nő :'))
if nem == 1:
    print('Szerdán nem kell suliba jönnöd.')
if nem == 2:
    print('Kedden nem kell suliba jönnöd.')


# Plusz feladat az unatkozóknak
lista = ["Szabin", "Károly", "L.Levente", "Máté", "Péter", "Dominik", "Zoltán", "Lajos", "Ákos", "Krisztián", "B.Levi", "Bálint", "Patrik"]
for x in lista:
  print(x)
