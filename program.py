#v1.0 dzialajacej aplikacji
wiek = input("Podaj wiek uzytkownika:")
#Sprawdzamy czy podany wiek jest liczba calkowita:
if wiek.isdigit() == False:
    exit("Wiek musi byc liczba calkowita")
wiek=int(wiek)
if wiek>=18 and wiek <=40:
    print("Witaj w naszym sklepie z alkoholem")
elif wiek>40:
    print("Witaj w naszym sklepie z alkoholem")
    print("Prosze korzystac z umiarem")
else:
    exit("Jestes za mlody/a na alkohol. Zapraszamy na disney.com")
