import math,cmath
# Feladat: Programozzuk le a másodfokú egyenlet képletét
# 1) Változók bekérése, az "a" változó csekkolása, hogy 0-e
a = float(input("Adja meg az a változót: "))
while a==0:
    print("Az a változó nem lehet kisebb, mint 0")
    a = float(input("Adja meg az a változót: "))
b = float(input("Adja meg a b változót: "))
c = float(input("Adja meg a c változót: "))

# 2) Egyenlet elvégzése
def megoldokeplet():
    seged1 = (b*b)-4*a*c
    x1 = (-b+cmath.sqrt(seged1))/(2*a)
    x2 = (-b-cmath.sqrt(seged1))/(2*a)
    if seged1 <= 0:
        print("Nincs a képletnek megoldása")
    else: 
# Válasz kidobása
        print("X1 megoldása: ")
        print(x1)
        print("X2 megoldása: ")
        print(x2)
# Függvény meghívása
megoldokeplet()

# Új dolgok:
# Gyökvonás a programban: cmath.sqrt( )
# Matematika importálása: import math,cmath
# Képletek a pythonban: def --():
# Függvény meghívása: fuggvenyneve()