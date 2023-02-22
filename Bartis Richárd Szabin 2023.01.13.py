#1.) Feladat
honap = []
honap.append("j")
honap.append("a")
honap.append("n")
honap.append("u")
honap.append("á")
honap.append("r")
print(honap)
honap.remove("j")
print(honap)
honap.reverse()
print(honap)
honap.append("Szeretem a Pythont")
print(honap)

#2.) Feladat
fajf = 0
korte =[]
for i in range(1,6):
    a = int(input("Add meg az alma mennyiségét tonnában:"))
    korte.append(a)
    fajf = fajf + a

print(korte)
print(fajf)