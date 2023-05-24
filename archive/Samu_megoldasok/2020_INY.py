"""
Feladat: 2020_INY Menetrendek
Keszitette: Pecsenye Samu
E-mail: samu.pecsenye@gmail.com
"""

#print('1. feladat')
with open('vonat.txt', 'r') as bemeneti_file:
    bejegyzesek = list()
    for bejegyzes_str in bemeneti_file:
        bejegyzes_list_str = bejegyzes_str.split()
        bejegyzesek.append(bejegyzes_list_str)


print('2. feladat')
vonatok = set()
allomasok = set()
for bejegyzes in bejegyzesek:
    vonatok.add(bejegyzes[0])
    allomasok.add(bejegyzes[1])
print(f'Allomasok szama: {len(allomasok)}')
print(f'Vonatok szama: {len(vonatok)}')


# szedszedjuk vonatonkent menetrendekre. mivel a vonatok nevei egesz szamok,
# dict helyett listat hasznalok, de mivel 1-gyel kezdodnek, ezert el kell tolni
menetrendek = [list() for _ in vonatok]
for bejegyzes in bejegyzesek:
    vonat_int = int(bejegyzes[0])-1
    allomas_str = bejegyzes[1]
    ido_int = 60*int(bejegyzes[2])+int(bejegyzes[3])  # 60*ora+perc
    tipus_str = bejegyzes[4]
    menetrendek[vonat_int].append((allomas_str, ido_int, tipus_str))


print('\n3. feladat')
max_allas = -1
max_vonat = None
max_allomas = None
erkezesi_ido = 0
for vonat, menetrend in enumerate(menetrendek):
    for bejegyzes in menetrend:
        if bejegyzes[2] == 'E':
            allas = bejegyzes[1]-erkezesi_ido
            if max_allas < allas:
                max_allas = allas
                max_vonat = vonat
                max_allomas = bejegyzes[0]
        else:
            erkezesi_ido = bejegyzes[1]
print(f'A(z) {max_vonat+1}. vonat a(z) {max_allomas} allomason {max_allas} percet allt')


print('\n4. feladat')
bemeneti_vonat_int = int(input('Adja meg egy vonat aonositojat! ')) - 1
bemeneti_ora_perc_str = input('Adjon meg egy idopontot (ora perc)! ')
ora_str, perc_str = bemeneti_ora_perc_str.split()
bemeneti_perc_int = 60*int(ora_str, ) + int(perc_str)


print('\n5. feladat')
indulas = menetrendek[bemeneti_vonat_int][0][1]  # menetrendek[x][0][1] -- x. vonat elso bejegyzesenek ideje
erkezes = menetrendek[bemeneti_vonat_int][-1][1]
menetido = erkezes-indulas
keses = menetido-(2*60+22)
if 0 < keses:
    print(f'A(z) {bemeneti_vonat_int+1}. vonat utja {keses} perccel hosszabb volt az eloirtnal.')
elif 0 == keses:
    print(f'A(z) {bemeneti_vonat_int+1}. vonat utja pontosan az eloirt ideig tartott.')
else:
    print(f'A(z) {bemeneti_vonat_int+1}. vonat utja {-keses} perccel rovidebb volt az eloirtnal.')  #{-keses}


print('\n6. feladat')
kimeneti_filenev = 'halad'+str(bemeneti_vonat_int+1)+'.txt'
with open(kimeneti_filenev, 'w') as kimeneti_file:
    for bejegyzes in menetrendek[bemeneti_vonat_int]:
        if bejegyzes[2] == 'E':
            ora_int = bejegyzes[1] // 60
            perc_int = bejegyzes[1] % 60
            ido_str = str(ora_int)+':'+str(perc_int)
            print(f'{bejegyzes[0]}. allomas: {ido_str}', file=kimeneti_file)


print('\n7. feladat')
for vonat, menetrend in enumerate(menetrendek):
    if menetrend[0][1] <= bemeneti_perc_int < menetrend[-1][1]:  # kihagyjuk azokat a vonatokat, amikor a bekert ido elott beertek a vegallomasra, vagy a bekert ido utan indulnak
        for bejegyzes in menetrend:
            if bemeneti_perc_int < bejegyzes[1]:
                if bejegyzes[2] == 'I':
                    print(f'A(z) {vonat+1}. vonat a(z) {bejegyzes[0]}. allomason allt.')
                else:
                    print(f'A(z) {vonat+1}. vonat a(z) {int(bejegyzes[0])-1}. es a(z) {bejegyzes[0]}. allomasok kozott jart.')
                break
