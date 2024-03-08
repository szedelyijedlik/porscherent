import os
try:
    f = open('python/slotar.csv', 'r', encoding='utf-8')
    slavak = [sor.strip() for sor in f]
except: 
    f = open('python/slotar.csv', 'w', encoding='utf-8')
    slavak = []
f.close()

def menu():
    print('1...Keresni')
    print('2...Új szót hozzáadni')
    print('0...kilépni')
    val = ''
    while val not in ['1', '2', '0']:
        val = input('Mit szeretne csinálni? ')
    return val

def main():
    val = menu()
    while val != '0':
        os.system('cls')    
        match val:
            case '1':
                kereses()
            case '2':
                hozzaadas()
        os.system('cls')
        val = menu()

def hozzaadas():
    hozzaadando = input('Mit szeretne hozzáadni? ')
    val = ''
    if hozzaadando in slavak: 
        input('A szó már hozzá lett adva. (ENTER)')
    if 'sl' not in hozzaadando:
        while val != '1' and val != '0':
            val = input('A szóban nincs sl. Biztos hozzá szeretné adni?(0/1) ')
    if val == '0':
        input('A  szót nem adtuk a listához. (ENTER)')
    else: 
        input('A szót sikeresen a listához adtuk. (ENTER)')
        with open('slotar.csv', 'a', encoding='utf-8') as f:
            f.write(hozzaadando + '\n')
            slavak.append(hozzaadando)   

def kereses():
    val = input('Mire szeretne keresni? ')
    kiirt_szo_db = 1
    szavak = [sor for sor in slavak if val in sor]
    for i in szavak:
        if kiirt_szo_db == 4 or i == szavak[-1]:
            print(i)
            kiirt_szo_db = 1
            continue
        else:
            print(i, end=', ')
            kiirt_szo_db += 1


    input('ENTER')

if __name__ == '__main__':
    main()