"""
Feladat: 2021_INY Banyato
Keszitette: Pecsenye Samu
E-mail: samu.pecsenye@gmail.com
"""

print('1. feladat')
with open('lista.txt', 'r') as forras_file:
    reszek = list()
    for sorszam, forras_sor_str in enumerate(forras_file):
        if sorszam % 5 == 0:
            resz = dict()
            resz['datum'] = forras_sor_str.strip()
        elif sorszam % 5 == 1:
            resz['cim'] = forras_sor_str.strip()
        elif sorszam % 5 == 2:
            resz['epizod'] = forras_sor_str.strip()
        elif sorszam % 5 == 3:
            resz['hossz'] = forras_sor_str.strip()
        elif sorszam % 5 == 4:
            resz['nezve'] = forras_sor_str.strip()
            reszek.append(resz)


print('\n2. feladat')
datumok_szama = 0
for resz in reszek:
    if resz['datum'] != 'NI':
        datumok_szama += 1
print(f'A listaban {datumok_szama} db vetitesi datummal rendelkezo epizod van')


print('\n3. feladat')
db_nezve = 0
for resz in reszek:
    if resz['nezve'] == '1':
        db_nezve += 1
nezve_arany = db_nezve/len(reszek)
print(f'A listaban levo epizodok {100*nezve_arany:.2f}%-at latta')


print('\n4. feladat')
eltoltott_ido = 0
for resz in reszek:
    if resz['nezve'] == '1':
        eltoltott_ido += int(resz['hossz'])
percek = eltoltott_ido % 60
orak = (eltoltott_ido // 60) % 24
napok = eltoltott_ido // (60*24)
print('Sorozatnezessel', end=' ')
if 0 < napok:
    print(f'{napok} napot', end=' ')
if 0 < napok or 0 < orak:
    print(f'{orak} orat', end=' ')
print(f'{percek} percet toltott')


print('\n5. feldat')
bemeneti_datum_str = input('Adjon meg egy datumot! Datum=')
for resz in reszek:
    if resz['datum'] != 'NI':
        if resz['datum'] <= bemeneti_datum_str:  # string osszehasonlitas beturend szerint toretnik, ami it mukodik, mivel a vezeto nullakat is kiirjak a datumban
            if resz['nezve'] == '0':
                print(f'{resz["epizod"]}\t{resz["cim"]}')  # a belso idezojelek masok kell hogy legyenek mint a kulsők


# print('\n6. feladat')
def hetnapja(ev:int, ho:int, nap:int) -> int:
    napok = "v h k sze cs p szo".split()
    honapok = (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
    if ho < 3: ev -= 1
    return napok[(ev+ev//4-ev//100+ev//400+honapok[ho-1] + nap) % 7]


print('\n7. feladat')
bemeneti_nap = input('Adja meg a het egy napjat (pl.: cs) ! Nap=')
sorozatok = set()
for resz in reszek:
    if resz['datum'] != 'NI':
        ev_str, ho_str, nap_str = resz['datum'].split('.')
        ev_int = int(ev_str)
        ho_int = int(ho_str)
        nap_int = int(nap_str)
        if hetnapja(ev_int, ho_int, nap_int) == bemeneti_nap:
            sorozatok.add(resz['cim'])
for sorozat in sorozatok:
    print(sorozat)


# print('\n8. feladat')
sorozatok = dict()
for resz in reszek:
    cim = resz['cim']
    hossz = resz['hossz']
    if cim not in sorozatok:
        sorozatok[cim] = {'hossz' : 0, 'darab' : 0}
        
    sorozatok[cim]['hossz'] += int(hossz)
    sorozatok[cim]['darab'] += 1

with open('summa.txt', 'w') as kimeneti_file:
    for cim in sorozatok:
        hossz = sorozatok[cim]['hossz']  # itt a cim egy str valtozo, a hossz pedig egy szoveg konstans
        darab = sorozatok[cim]['darab']
        print(f'{cim} {hossz} {darab}', file=kimeneti_file)
    

    