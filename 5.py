list=[1, 2, 3, 4, 5, 6]
a=int(input("Které  číslo vyhledat?"))
if a in list:
    print(a, "Je v listu")
else:
    print(a, "Není v listu")