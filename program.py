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
if wiek>=18 and wiek <=40:
    print("Witaj w naszym sklepie z alkoholem")
elif wiek>40:
    print("Witaj w naszym sklepie z alkoholem")
    print("Prosze korzystac z umiarem")
else:
    exit("Jestes za mlody/a na alkohol. Zapraszamy na disney.com")

gender = input("Prosze podac swoja plec K/M: ")
if "M" == gender:
    print("Dzien dobry Panu :)")
elif "K" == gender:
    print("Dzien dobry Pani :)")
else:
    print("Prosze wpisac Litere: K - 'Kobieta' lub M - 'Mezczyzna'")
    