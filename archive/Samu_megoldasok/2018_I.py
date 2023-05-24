"""1. feladat"""
adatok = list()
with open('ajto.txt', 'r') as bemeneti_file:
    for sor in bemeneti_file:
        ora, perc, azon, irany = sor.split()
        adat = dict()
        adat['ora'] = int(ora)
        adat['perc'] = int(perc)
        adat['azon'] = int(azon)
        adat['irany'] = irany
        adatok.append(adat)

print('2. feladat')
# mivel a szoba ures 9 orakor, az első feljegyzés biztosan belépő
azon_elso = adatok[0]['azon']
print(f'Az elso belepo: {azon_elso}')
# mivel a szoba nem ures 15 orakor, az utolso feljegyzes nem feltétlenül kilepo
azon_utolso = None
for adat in adatok:
    if adat['irany'] == 'ki':
        azon_utolso = adat['azon']
# for adat in reversed(adatok):
#     if adat['irany'] == 'be': continue
#     azon_utolso = adat['azon']
#     break
print(f'Az utolso kilepo: {azon_utolso}')

"""3. feladat"""
# a szépség érdekében csak azokat az azonositokat irjuk ki, akik legalább egyszer megjelennek
emberek = dict()
for adat in adatok:
    azon = adat['azon']
    if azon not in emberek:
        emberek[azon] = 0
    emberek[azon] += 1

with open('athaladas.txt', 'w') as kimeneti_file:
    for azon, szam in sorted(emberek.items()):
        print(f'{azon} {szam}', file=kimeneti_file)

print('\n4. feladat')
bent = set()
for adat in adatok:
    azon = str(adat['azon'])
    if adat['irany'] == 'be':
        bent.add(azon)
    else:
        bent.remove(azon)
print(f'A vegen a tarsalgoban voltak: {" ".join(sorted(bent))}')

print('\n5.feladat')
szamlalo = 0
max_szamlalo = 0
max_ido = 0
for adat in adatok:
    if adat['irany'] == 'be':
        szamlalo += 1
    else:
        szamlalo -= 1
    if max_szamlalo < szamlalo:
        max_szamlalo = szamlalo
        max_ido = f'{adat["ora"]}:{adat["perc"]}'
print(f'Peldaul {max_ido}-kor voltak a legtobben a tarsalgoban.')

print('\n6. feladat')
azon = input('Adja meg a szemely azonositojat! ')
azon = int(azon)
print('\n7. feladat')
bent_van = False
for adat in adatok:
    if adat['azon'] == azon:
        if adat['irany'] == 'be':
            print(f'{adat["ora"]}:{adat["perc"]}', end='-')
            bent_van = True
        else:
            print(f'{adat["ora"]}:{adat["perc"]}')
            bent_van = False
if bent_van:
    print('')

print('\n8. feladat')
ido = 0
bent_van = False
for adat in adatok:
    if adat['azon'] == azon:
        if adat['irany'] == 'be':
            t_be = 60*int(adat['ora'])+int(adat['perc'])
            bent_van = True
        else:
            t_ki = 60*int(adat['ora'])+int(adat['perc'])
            ido += t_ki-t_be
            bent_van = False
if bent_van:
    t_ki = 60*15
    ido += t_ki-t_be
print(f'A(z) {azon}. szmeely osszesen {ido} percet volt bent, ', end='')
if bent_van:
    print('a megfigyeles vegen a tarsalgoban volt.')
else:
    print('a megfigyeles vegen nem votl a tarsalgoban')
    
    

    
    