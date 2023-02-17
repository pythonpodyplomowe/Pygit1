#v1.0 dzialajacej aplikacji

from Reg import Reg
wiek = input("Podaj wiek uzytkownika:")

reg = input("Select region [EUR] or [USA]:")
obj_reg = Reg(reg)
print(obj_reg)

#Sprawdzamy czy podany wiek jest liczba calkowita:
if wiek.isdigit() is False:
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

#Użytkownik wybiera region.
inp = input("Wybierz swój region EUR albo USA ")

if inp == "EUR":
    print("Oferta dostępna dla regionu EUR")
elif inp == "USA":
    print("Oferta dostępna dla regionu USA")
else:
    print("Wybierz poprawny region EUR albo USA")



plec = input('Podaj plec (kobieta/mezczyzna: )')
if plec == 'kobieta' and wiek > 30:
    print('Pierwszy Aperol Spritz gratis!')
elif plec == 'mezczyzna' and wiek < 30:
    print('Jagerbomka gratis!')
else:
    exit(' ')

