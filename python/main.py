import os, sys
from classes import Felhasznalo, Kiadott_Auto, Auto
with open('python/autolista.csv', 'r', encoding='utf-8') as f:
    f.readline()
    autok: list[Auto] = [Auto(sor) for sor in f]
with open('python/felhasznalok.csv', 'r', encoding='utf-8') as f:
    f.readline()
    felhasznalok: list[Felhasznalo] = [Felhasznalo(sor) for sor in f]
with open('python/kiadott_autok.csv', 'r', encoding='utf-8') as f:
    f.readline()
    try: 
        kiadott_autok: list[Kiadott_Auto] = [Kiadott_Auto(sor, autok, felhasznalok) for sor in f]
    except Exception as a:
        print(a)
        sys.exit()

def main():
    val = menu()
    match val:
        case '1':
            buy_new_car()
        case '2':
            sell_car()
        case '3': 
            new_user()

def menu():
    print('1...új kocsi vásárlása')
    print('2...kocsi eladása')
    print('3...felhasználó hozzáadása')

    val = ''
    while val not in map(str, range(4)):
        val = input('Mit szeretne tenni? ')
    return val

def new_user():
    nev = input('Mi a neve? ')
    telefonszam = input('Mi a telefonszáma? ')
    nem = input('Mi a neme? (F/N) ')
    sor = ';'.join([nev, telefonszam, nem])
    with open('python/felhasznalok.csv', 'a', encoding='utf-8') as f:
        f.write(sor + '\n')
    autok.append(Felhasznalo(sor))


    val = ''
    while val not in map(str, range(3)):
        val = input('Mit szeretne tenni? ')
    return val

def buy_new_car():
    rendszam = input('Rendszam: ')
    tipus = input('tipus: ')
    futott_km = input('Hány km-t ment az autó: ')
    uzemanyag = input('Mennyi üzemanyag van benne most? ')
    uzemanyag_max = input('Mennyi az  üzemanyagtartály mérete? ')
    fogyasztas = input('Mennyi a fogyasztás? ')
    ar = input('Mennyi a napi ára? ')
    sor = ';'.join([rendszam, tipus, futott_km, uzemanyag, uzemanyag_max, fogyasztas, ar])
    with open('python/autolista.csv', 'a', encoding='utf-8') as f:
        f.write(sor + '\n')
    autok.append(Auto(sor))



def sell_car():
    eladando_auto_rendszam = input('Mi az auto rendszáma, amit szeretne eladni? ')
def sell_car():
    eladando_auto_rendszam= input('Mi az auto rendszáma, amit szeretne eladni? ')
    for i in autok:
        if i.rendszam == eladando_auto_rendszam:
            autok.remove(i)
            break
    else:
        input('Nincs ilyen rendszámú autó\n(ENTER)')
        return 
    with open('python/autolista.csv', 'w', encoding='utf-8') as f:
        f.write('Rendszám;Kocsi típusa;Futott km;uzemanyag;uzemanyagMax;fogyasztás;ár naponta\n')
        for i in autok:
            f.write(f'{i.rendszam};{i.tipus};{i.km};{i.uzemanyag};{i.uzemanyagMax};{i.fogyasztas};{i.ar}')
    input('Az auto sikeren törölve lett\n(ENTER)')

if __name__ == '__main__':
    main()