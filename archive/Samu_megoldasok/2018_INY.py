"""1. feladat"""
adatok = list()
with open('fogado.txt', 'r') as bementi_file:
    for sor in bementi_file:
        vezetek, kereszt, idopont, foglalas = sor.split()
        adat = dict()
        adat['nev'] = vezetek+' '+kereszt
        adat['idopont'] = idopont
        adat['foglalas'] = foglalas
        adatok.append(adat)

print('2. feladat')
print(f'Foglalasok szama: {len(adatok)}')

print('\n3. feladat')
nev = input('Adjon meg egy nevet: ')
szamlalo = 0
for adat in adatok:
        if adat['nev'] == nev:
            szamlalo += 1
if 0 < szamlalo:
    print(f'{nev} neven {szamlalo} idopontfoglalas van.')
else:
    print('A megadott neven nincs idopontfoglalas.')

print('\n4. feladat')
idopont = input('Adjon meg egy ervenyes idopontot (pl. 17:10): ')
nevek = set()
for adat in adatok:
    if adat['idopont'] == idopont:
        nevek.add(adat['nev'])

filenev = idopont[0:2]+idopont[3:5]+'.txt'
with open(filenev, 'w') as kimeneti_file:
    for nev in sorted(nevek):
        print(nev)
        print(nev, file=kimeneti_file)

print('\n5. feladat')
elso = adatok[0]
for adat in adatok:
    if adat['foglalas'] < elso['foglalas']:
        elso = adat
print(f'Tanar neve: {elso["nev"]}')
print(f'Foglalt idopont: {elso["idopont"]}')
print(f'Foglalas ideje: {elso["foglalas"]}')

print('\n6. feladat')
nev = 'Barna Eszter'
idopontok = set()
for ora in range(16, 18):
    for perc in range(0, 60, 10):
        s = str(ora) + ':' + str(perc).zfill(2)
        idopontok.add(s)
# idopontok = {'16:00', '16:10', '16:20', '16:30', '16:40', '16:50',
#              '17:00', '17:10', '17:20', '17:30', '17:40', '17:50'}

foglalt = set()
for adat in adatok:
    if adat['nev'] == nev:
        foglalt.add(adat['idopont'])

elozo_foglalt = False
kimenet = None
for idopont in sorted(idopontok):    
    if idopont not in foglalt:
        print(idopont)
        if elozo_foglalt:
            kimenet = idopont
        elozo_foglalt = False
    else:
        elozo_foglalt = True
if elozo_foglalt:
    kimenet = '18:00'
print(f'{nev} legkorabban tavozhat: {kimenet}')



