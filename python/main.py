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
    while val != '0':
        os.system('cls')
        match val:
            case '1':
                buy_new_car()
            case '2': 
                new_user()
            case '3':
                rent_car()
            case '4':
                list_all_cars()
            case '5':
                list_users()
            case '6':
                list_avaible_cars()
            case '7': 
                listing_kiberelt_cars()
            case '8':
                unrent_car()
            case '9':
                profit_calc()
            case '10':
                how_profit_calc()
        os.system('cls')
        val = menu()

def menu():
    print('1.\tÚj kocsi vásárlása')
    print('2.\tFelhasználó hozzáadása')
    print('3.\tAutó bérlése')
    print('4.\tÖsszes Autó listázása')
    print('5.\tFelhasználók listázása')
    print('6.\tBérelhető autók listázása')
    print('7.\tKibérelt autók listázása')
    print('8.\tKibérelt autók visszavétele')
    print('9.\tProfit kiszámítása')
    print('10.\tProfit kiszámítás képlete')
    print('0.\tKilépés')

    val = ''
    while val not in map(str, range(10)):
        val = input('\nVálasszon egy lehetőséget:  ')
    return val

def new_user():
    nev = input('Mi a neve? ')
    telefonszam = input('Mi a telefonszáma? ')
    nem = input('Mi a neme? (F/N) ')
    sor = ';'.join([nev, telefonszam, nem])
    with open('python/felhasznalok.csv', 'a', encoding='utf-8') as f:
        f.write(sor + '\n')
    felhasznalok.append(Felhasznalo(sor))
    input('Felhasználó sikeresen hozzáadva\n(ENTER)')

def find_user(szoveg) -> Felhasznalo:
        while True:
            nev = input(szoveg)
            for i in felhasznalok:
                if i.nev == nev:
                    return i

def find_car(szoveg, mylist: list[Auto] = autok) -> Auto :
        while True:
            rendszam = input(szoveg)
            for i in mylist:
                if i.rendszam == rendszam:
                    return i
        
def rent_car():
    kiberlendo_auto: Auto = find_car('Melyik autót szeretnék kibérelni? (rendszám) ')
    for i in kiadott_autok:
        if kiberlendo_auto.rendszam == i.auto.rendszam and i.lejarati_ido is None:
            input('Az autó már ki van adva. (ENTER)')
            return 
    kiberlo = find_user('Ki bérli az autót? ')
    lejarati_ido = ido_bekeres()

    sor = ';'.join([kiberlendo_auto.rendszam, kiberlo.nev, now_time(), lejarati_ido]) + ";None"
    with open('python/kiadott_autok.csv', 'a', encoding='utf-8') as f:
        f.write(sor + '\n')
    kiadott_autok.append(Kiadott_Auto(sor, autok, felhasznalok))
    input('Autó sikeresen ki lett bérelve.\n(ENTER)')

def unrent_car():
    auto: Auto = find_car('Melyik autót hozták vissza? ', mylist=[i.auto for i in kiadott_autok if i.visszahozasi_ido is None])
    for i in kiadott_autok:
        if i.auto.rendszam == auto.rendszam:
            i.visszahozasi_ido = now_time()
            break
    else:
        print('Nincs benne')
    with open('python/kiadott_autok.csv', 'w', encoding='utf-8') as f:
        f.write('Rendszám;felhasznalo_neve;berlesi_ido;lejarati_ido;visszahozasi_ido\n')
        for i in kiadott_autok:
            # print(f'{i.auto.rendszam};{i.felhasznalo.nev};{i.berlesi_ido};{i.lejarati_ido};{str(i.visszahozasi_ido)}')
            f.write(f'{i.auto.rendszam};{i.felhasznalo.nev};{i.berlesi_ido};{i.lejarati_ido};{str(i.visszahozasi_ido)}\n')
    input('Autó visszavéve\n(ENTER)')

def ido_bekeres(nagyobb = True) -> str:
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
        nowev, nowhonap,nownap = map(int, now_time().split('.'))
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

def now_time() -> str:
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
    input('Autó sikeresen megvéva\n(ENTER)')

def how_profit_calc():
    print('Ha időben hozza vissza, akkor a napok száma * az autó bérlési ára')
    print('Ha előbb hozza vissza, akkor az eltöltött napok száma * az autó bérlési ára + a maradék nap *az autó árának fele')
    input('Ha később hozza vissza, akkor a lejárati napok száma * az autó bérlési ára + 14 nap az autó árána 1.5-szerese, ezen fellül 2-szerese\n(ENTER)')

def profit_calc():
    osszprofit: int = 0
    for i in kiadott_autok:
        if i.visszahozasi_ido is not None:
            if i.visszahozasi_ido == i.lejarati_ido:
                berlesi_ido = list(map(int, i.berlesi_ido.split('.')))
                visszahozasi_ido = list(map(int, i.visszahozasi_ido.split('.')))
                profit = ( (visszahozasi_ido[0] - berlesi_ido[0])*365 + (visszahozasi_ido[1] - berlesi_ido[1])*30 + visszahozasi_ido[2] - berlesi_ido[2]) * i.auto.ar
                osszprofit += profit
                print(f'A kibérelt autó: {i.auto.rendszam}')
                print(f'\tAz autó {i.berlesi_ido}-kor adták ki')
                print(f'\tAz autót a megbeszélt időben visszahozták: {i.visszahozasi_ido}')
                print(f'\tEbből a profit: {profit} forint')
                print()
                continue
            berlesi_ido = list(map(int, i.berlesi_ido.split('.')))
            visszahozasi_ido = list(map(int, i.visszahozasi_ido.split('.')))
            lejarati_ido = list(map(int, i.lejarati_ido.split('.')))
            if kisebb_ido(visszahozasi_ido, lejarati_ido):
                profit = ((visszahozasi_ido[0] - berlesi_ido[0])*365 + (visszahozasi_ido[1] - berlesi_ido[1])*30 + visszahozasi_ido[2] - berlesi_ido[2]) * i.auto.ar
                profit += ((lejarati_ido[0] - visszahozasi_ido[0])*365 + (lejarati_ido[1] - visszahozasi_ido[1])*30 + lejarati_ido[2] - visszahozasi_ido[2]) * i.auto.ar/2
                osszprofit += profit
                print(f'A kibérelt autó: {i.auto.rendszam}')
                print(f'\tAz autó {i.berlesi_ido}-kor adták ki')
                print(f'\tAz autót a korábban hozták vissza: {i.visszahozasi_ido}')
                print(f'\tAz autót a eddig bérelték ki: {i.lejarati_ido}')
                print(f'\tEbből a profit: {profit:.0f} forint')
                print()
                continue
            profit = ((lejarati_ido[0] - berlesi_ido[0])*365 + (lejarati_ido[1] - berlesi_ido[1])*30 + lejarati_ido[2] - berlesi_ido[2]) * i.auto.ar
            hatralevo_napok = (visszahozasi_ido[0] - lejarati_ido[0])*365 + (visszahozasi_ido[1] - lejarati_ido[1])*30 + visszahozasi_ido[2] - lejarati_ido[2]
            # print(profit)
            profit += hatralevo_napok*i.auto.ar*1.5 if hatralevo_napok <= 14 else 21*i.auto.ar + (hatralevo_napok-14)*i.auto.ar*2
            # print(profit)
            osszprofit += profit
            print(f'A kibérelt autó: {i.auto.rendszam}')
            print(f'\tAz autó {i.berlesi_ido}-kor adták ki')
            print(f'\tAz autót a később hozták vissza: {i.visszahozasi_ido}')
            print(f'\tAz autót a eddig bérelték ki: {i.lejarati_ido}')
            print(f'\tEbből a profit: {profit:.0f} forint')
            print()
        
    input(f'\nAz összes profit: {osszprofit:.0f}\n\n(ENTER)')

def kisebb_ido(elso_ido: list[int], masodik_ido: list[int]) -> bool:
    if elso_ido[0] < masodik_ido[0]: 
        return True
    if elso_ido[1] < masodik_ido[1]: 
        return True
    if elso_ido[2] < masodik_ido[2]: 
        return True
    return False

def listing_kiberelt_cars():
    os.system('cls')
    for i in kiadott_autok:
        if i.visszahozasi_ido is None:
            print(f'Rendszam: {i.auto.rendszam}')
            print(f'\tFelhasználó: {i.felhasznalo.nev}')
            print(f'\tKibérlés idő: {i.berlesi_ido}')
            print(f'\tLejárati idő: {i.lejarati_ido}')
            print()
    input('(ENTER)')

def list_avaible_cars():
    os.system('cls')
    for i in autok:
        if i.rendszam not in [auto.auto.rendszam for auto in kiadott_autok]:
            print(f'Rendszam: {i.rendszam}')
            print(f'\tTipus: {i.tipus}')
            print(f'\tKm-t ment: {i.km} km')
            print(f'\tJelenlegi üzenemanyagmennyiség: {i.uzemanyag} l')
            print(f'\tÜzemanyagtartály mérete: {i.uzemanyagMax} l')
            print(f'\tFogyasztás : {i.fogyasztas} l/100 km')
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
        print(f'\tFogyasztás : {i.fogyasztas} l/100 km')
        print(f'\tÁr: {i.ar} ft/nap')
        print()
    input('ENTER')

def list_users():
    os.system('cls')
    for i in felhasznalok:
        print(f'Neve: {i.nev}')
        print(f'\ttelefonszáma: {i.telefonszam}')
        print(f'\tneme: {"Férfi" if i.nem else "Nő"}')
        print()
    input('ENTER')

if __name__ == '__main__':
    main()