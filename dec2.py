# 1. Feladat
# Osztható e a szám 17-el?
szam = int(input("Kérem a számot: "))

if szam<0:
    print("A szám rossz!")
elif (szam % 17 == 0):
    print("A szám osztható 17-el!")
else:
    print("A szám nem osztható 17-el!")
#----------------------------------------------------------------------------------------------------------
# 2. Feladat
# Kérd be Ákos, Lili, Anita fizetését, és nagyság sorrendben írattatsd ki a programmal!
fiz_a = int(input("Ákos fizetése:"))
fiz_l = int(input("Lili fizetése:"))
fiz_a = int(input("Anita fizetése:"))

if fiz_a < fiz_l:
    if fiz_a < fiz_l:
        print("Lili keres a legtöbbet",fiz_l)
        if fiz_a < fiz_a:
            print("Ákos keres a legkevesebbet,",fiz_a)
            print("Lili, Anita, Ákos")
        else:
            print("Anita keres a legkevesebbet",fiz_a)
            print("Lili, Ákos, Anita")
    else:
            