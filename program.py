#v1.0 dzialajacej aplikacji
wiek = input("Podaj wiek uzytkownika:")
#Sprawdzamy czy podany wiek jest liczba calkowita:
if wiek.isdigit() == False:
    exit("Wiek musi byc liczba calkowita")
wiek=int(wiek)
if wiek>=120:
    exit("wiek obsługiwanego musi być mniejszy niż 120 lat")
if wiek>=18 and wiek <=40:
    print("Witaj w naszym sklepie z alkoholem")
elif wiek > 40 and wiek <= 99:
    print("Witaj w naszym sklepie z alkoholem")
    print("Prosze korzystac z umiarem, dbaj o zdrowie")
elif wiek>=100 and wiek <=119:
    print("Ze względu na zaawansowany wiek nie powinieneś w ogóle pić alkoholu")
else:
    exit("Jestes za mlody/a na alkohol. Zapraszamy na disney.com")
