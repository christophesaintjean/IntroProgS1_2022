annee = int(input("annee ?"))

div4 = annee % 4 == 0
div100 = annee % 100 == 0
C1 = div4 and not div100
C2 = annee % 400 == 0

bissextile = (C1 and not C2) or (not C1 and C2)

if bissextile:
    print("B")
else:
    print("not B")