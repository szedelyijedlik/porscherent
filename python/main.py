import os, sys, time
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
        case '4':
            rent_car()
        case '5':
            list_all_cars()
        case '6':
            list_avaible_cars()
        case '7': 
            listing_kiberelt_cars()

def menu():
    print('1...új kocsi vásárlása')
    print('2...kocsi eladása')
    print('3...felhasználó hozzáadása')
    print('4...Autó bérlése')
    print('5...Összes Autó listázása')
    print('6...Bérelhető autók listázása')
    print('7...Kibérelt autók listázása')

    val = ''
    while val not in map(str, range(8)):
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


def find_user(szoveg):
        while True:
            nev = input(szoveg)
            for i in felhasznalok:
                if i.nev == nev:
                    return i


def find_car(szoveg):
        while True:
            rendszam = input(szoveg)
            for i in autok:
                if i.rendszam == rendszam:
                    return i
        
def rent_car():
    kiberlendo_auto: Auto = find_car('Melyik autót szeretnék kibérelni? (rendszám) ')
    for i in kiadott_autok:
        if kiberlendo_auto.rendszam == i.auto.rendszam:
            input('Az autó már ki van adva. (ENTER)')
            return 
    kiberlo = find_user('Ki bérli az autót? ')
    lejarati_ido = ido_bekeres()

    sor = ';'.join([kiberlendo_auto.rendszam, kiberlo.nev, time_now(), lejarati_ido])
    with open('python/kiadott_autok.csv', 'a', encoding='utf-8') as f:
        f.write(sor)
    kiadott_autok.append(Kiadott_Auto(sor, autok, felhasznalok))
    
def ido_bekeres(nagyobb = True):
    lejarati_ido = ' '
    while True:
        while True:
            lejarati_ido = input('Mikor jár le a bérlés? ')
            if lejarati_ido.count('.') != 2:
                continue

            try:
                ev, honap, nap = map(int, lejarati_ido.split('.'))
                if honap > 12:
                    print('túl sok honap')
                    continue
                if nap > 31:
                    print('túl sok nap ')
                    continue
                break
            except ValueError:
                pass
        if not nagyobb: 
            break
        nowev, nowhonap,nownap = map(int, time_now().split('.'))
        if ev > nowev:
            break
        if ev < nowev: 
            print('Nem lehet kisebb, mint a mostani dátum')
            continue
        if honap > nowhonap:
            break
        if honap < nowhonap: 
            print('Nem lehet kisebb, mint a mostani dátum')
            continue
        if nap > nownap:
            break
    return lejarati_ido

def time_now() -> str:
    ido = time.localtime()
    return '.'.join(list(map(str, [ido.tm_year, ido.tm_mon, ido.tm_mday])))

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
    eladando_auto: Auto = find_car('Mi az auto rendszáma, amit szeretne eladni? ')
    for i in autok:
        if i.rendszam == eladando_auto.rendszam:
            autok.remove(i)
            break
    else:
        input('Nincs ilyen rendszámú autó\n(ENTER)')
        return 
    with open('python/autolista.csv', 'w', encoding='utf-8') as f:
        f.write('Rendszám;Kocsi típusa;Futott km;uzemanyag;uzemanyagMax;fogyasztás;ár naponta\n')
        for i in autok:
            f.write(f'{i.rendszam};{i.tipus};{i.km};{i.uzemanyag};{i.uzemanyagMax};{i.fogyasztas};{i.ar}\n')
    input('Az auto sikeren törölve lett\n(ENTER)')

def listing_kiberelt_cars():
    os.system('cls')
    for i in kiadott_autok:
        print(f'Rendszam: {i.auto.rendszam}')
        print(f'\tFelhasználó: {i.felhasznalo.nev}')
        print(f'\tKibérlés idő: {i.berlesi_ido}')
        print(f'\tLejárati idő: {i.lejarati_ido}')

def list_avaible_cars():
    os.system('cls')
    for i in autok:
        if i.rendszam not in [auto.auto.rendszam for auto in kiadott_autok]:
            print(f'Rendszam: {i.rendszam}')
            print(f'\tTipus: {i.tipus}')
            print(f'\tKm-t ment: {i.km} km')
            print(f'\tJelenlegi üzenemanyagmennyiség: {i.uzemanyag} l')
            print(f'\tÜzemanyagtartály mérete: {i.uzemanyagMax} l')
            print(f'\tFogyasztás : {i.fogyasztas} ) l/km')
            print(f'\tÁr: {i.ar} ft/nap')
            print()
    input('ENTER')

def list_all_cars():
    os.system('cls')
    for i in autok:
        print(f'Rendszam: {i.rendszam}')
        print(f'\tTipus: {i.tipus}')
        print(f'\tKm-t ment: {i.km} km')
        print(f'\tJelenlegi üzenemanyagmennyiség: {i.uzemanyag} l')
        print(f'\tÜzemanyagtartály mérete: {i.uzemanyagMax} l')
        print(f'\tFogyasztás : {i.fogyasztas} ) l/km')
        print(f'\tÁr: {i.ar} ft/nap')
        print()
    input('ENTER')

if __name__ == '__main__':
    main()