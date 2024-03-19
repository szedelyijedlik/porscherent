class Auto:
    def __init__(self, sor: str) -> None:
        data = sor.strip().split(';')
        self.rendszam = data[0]
        self.tipus = data[1]
        self.km = int(data[2])
        self.uzemanyag = float(data[3])
        self.uzemanyagMax = int(data[4])
        self.fogyasztas = float(data[5])
        self.ar = int(data[6])

    def __str__(self) -> str:
        return self.rendszam

class Felhasznalo: 
    def __init__(self, sor: str) -> None:
        data = sor.strip().split(';')
        self.nev = data[0]
        self.telefonszam = data[1]
        self.nem = data[2] == 'F'

    def __str__(self) -> str:
        return self.nev

class Kiadott_Auto:
    def __init__(self, sor: str, autok: list[Auto], felhasznalok: list[Felhasznalo]) -> None:
        data = sor.strip().split(';')
        for i in autok:
            if i.rendszam == data[0]:
                self.auto = i
                break
        else:
            if data[4] == 'None':
                raise Exception(f'Nincs {data[0]} rendszámú autó', data[4])
        for i in felhasznalok:
            if i.nev == data[1]:
                self.felhasznalo = i
                break
        else:
            raise Exception(f'Nincs {data[1]} nevű felhasználó')
        self.berlesi_ido = data[2]
        self.lejarati_ido = data[3]
        self.visszahozasi_ido = data[4] if data[4] != 'None' else None

    def __str__(self) -> str:
        return self.auto.rendszam