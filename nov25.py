# Tömb létrehozása
nev = ["Budapesti","Gépészeti","Szakképzési","Centrum"]
print(nev)
# Tömbhöz való hozzáadás
nev.append("Szily")
nev.append("Kálmán")
nev.append("Technikum")
nev.append("és Kollégium")
print(nev)
# Elemek szortírozása
nev.sort()
print(nev)
# A változó visszafele kiírása
nev.reverse()
print(nev)
# Outputból Kitöröl egy megadott dolgot 
nev.remove("Technikum")
print(nev)
# Ugyan az mint a .remove 
nev.pop(2)
print(nev)
# Adatok tagjainak megszámolása
k = nev.count("Kálmán")
print(k)
e = "Ákos"

# -- Adatok keresése, és sorszámának kiírása --
try:
    i = nev.index(e)
    print("A keresett adat sorszáma: ",i)
except ValueError:
    print(A keresett adat nem található!)
# Kivételkezelés
# Mindíg try - catch szerkezet, Pytonban exept szerepel catch helyett.
# try: az itt szereplő utasítást a program megpróbálja végrehajtani. 
# Ha sikerült, akkor ezen az ágon szerepel a hozzá tartozó parancs.
# Ha nem sikerül, akkor az except után szereplő utasítások lesznek végrehajtva
# Az itt szereplő kódrészletben egy "nev" nevű tömbben keressük az "e" változó tartalmát
# Ha megvan, akkor olyan üzenetet ír ki, amiben szerepel a sorszáma is
# Ha nincs, akkor csak ezt a tényt közöljük.
