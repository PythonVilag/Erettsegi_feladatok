"""
Feladat: 2020_I Meteorologia Jelentes
Keszitette: Pecsenye Samu
E-mail: samu.pecsenye@gmail.com
"""


# print('1. feladat')
with open('tavirathu13.txt', 'r') as bemeneti_file:
    taviratok = list()
    for sor_str in bemeneti_file:
        sor_list_str = sor_str.split()
        taviratok.append(sor_list_str)


print('2. feladat')
bemeneti_varos = input('Adja meg egy telepules kodjat! Telepules:')
utolso_ido = '0000'
van_tavirat = False
for tavirat in taviratok:
    if tavirat[0] == bemeneti_varos:
        van_tavirat = True
        if utolso_ido <= tavirat[1]:  # a beturend csodaja miatt nem kell int-re valtani az idoket, de atvalthatnank siman intre, vagy rendesen percekre is, de nem szamit
            utolso_ido = tavirat[1]
if van_tavirat:
    formazott_ido = utolso_ido[:2]+':'+utolso_ido[2:]
    print(f'Az utolso meresi adat a megadott telepulesrol {formazott_ido}-kor erkezett')
else:
    print('Az adott varoskoddal nem erkezett tavirat')


print('\n3. feladat')
min_tavirat = min(taviratok, key=lambda x: x[3])
nev = min_tavirat[0]
ido = min_tavirat[1]
formazott_ido = ido[:2]+':'+ido[2:]
hom = min_tavirat[3]
print(f'A alacsonyabb homerseklet: {nev} {ido} {hom}°C.')

max_tavirat = max(taviratok, key=lambda x: x[3])
## alternativ
# max_tavirat = taviratok[0]
# for tavirat in taviratok:
#     if max_tavirat[3] < tavirat[3]:
#         max_tavirat = tavirat
nev = max_tavirat[0]
ido = max_tavirat[1]
formazott_ido = ido[:2]+':'+ido[2:]
hom = max_tavirat[3]
print(f'A legmagasabb homerseklet: {nev} {ido} {hom}°C.')

    
print('\n4. feladat')
csendes_taviratok = list()
for tavirat in taviratok:
    if tavirat[2] == '00000':
        csendes_taviratok.append(tavirat)
if len(csendes_taviratok) == 0:
    print('Nem volt szelcsent a meresek idejen')
else:
    for tavirat in csendes_taviratok:
        nev = tavirat[0]
        ido = tavirat[1]
        formazott_ido = ido[:2]+':'+ido[2:]
        print(tavirat[0], formazott_ido)


print('\n5. feladat')
"""
szoooooval. a feladat szerint ha mondjuk egy varos adatai a kovetkezok:
0100 12
0115 15

0715 21
0730 24

1300 32

1900 26

akkor a napi kozephomerseklet (12+15+21+24+32+26) / 6, nem pedig
((12+15)/2 + (21+24)/2 + 32 + 26) / 4. Ennek semmi ertelme, mert ha hajnalban
gyakrabban merunk, akkor eltorzitjuk a homersekletet, de ezt mondja a feladat,
ugyhogy ezt kell csinálni.
"""
telepulesnevek = {taviratok[0] for taviratok in taviratok}  #set, a többször elofordulo kodokat osszevonja
erteksorok = {nev:list() for nev in telepulesnevek}  #dict, gyakorlatilag lista is lehetne de igy közvetlenebbül lehet utalni rajuk
kph_flagek = {nev:[False, False, False, False] for nev in telepulesnevek}
alacsony = {nev:None for nev in telepulesnevek}
magas = {nev:None for nev in telepulesnevek}
for tavirat in taviratok:
    nev = tavirat[0]
    ora = tavirat[1][:2]
    hom = int(tavirat[3]) # mivel ezzel szamolni kell majd, ezert itt atvaltom intbe
    #5/a feladat
    if ora in {'01', '07', '13', '19'}:
        erteksorok[nev].append(hom)
        if ora == '01':
            kph_flagek[nev][0] = True
        if ora == '07':
            kph_flagek[nev][1] = True
        if ora == '13':
            kph_flagek[nev][2] = True
        if ora == '19':
            kph_flagek[nev][3] = True
    #5/b feladat
    if alacsony[nev] is None or hom < alacsony[nev]:  #az adott varos erso erteke mindenkepp beirodik minimumnak
        alacsony[nev] = hom
    if magas[nev] is None or magas[nev] < hom:  #az adott varos erso erteke mindenkepp beirodik maximumnak
        magas[nev] = hom
for nev in telepulesnevek:
    #5/a feladat
    print(nev, end=' ')
    if all(kph_flagek[nev]):
        erteksor = erteksorok[nev]
        atlag = sum(erteksor)/len(erteksor)
        print(f'Kozephomerseklet: {round(atlag)};', end=' ')
    else:
        print('NA;', end=' ')

    #5/b feladat
    ingadozas = magas[nev]-alacsony[nev]
    print(f'Homerseklet-ingadozat: {ingadozas}')
        

print('\n6. feladat')
for nev in telepulesnevek:
    kimeneti_filenev = nev+'.txt'
    with open(kimeneti_filenev, 'w') as kimeneti_file:
        print(nev, file=kimeneti_file)
        for tavirat in taviratok:
            if tavirat[0] == nev:
                ido = tavirat[1]
                formazott_ido = ido[:2]+':'+ido[2:]
                szelerosseg = int(tavirat[2][3:])
                print(formazott_ido, '#'*szelerosseg, file=kimeneti_file)