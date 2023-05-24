"""
Feladat: 2021_INY Banyato
Keszitette: Pecsenye Samu
E-mail: samu.pecsenye@gmail.com
"""


#print('1. feladat')
with open('melyseg.txt', 'r') as forras_file:
    melyseg = list()
    for sorszam, sor_str in enumerate(forras_file):
        if sorszam == 0:
            sorok_szama = int(sor_str)
        elif sorszam == 1:
            oszlopok_szama = int(sor_str)
        else:
            sor_str_list = sor_str.strip().split()
            sor_int_list = list(map(int, sor_str_list))
            melyseg.append(sor_int_list)


print('2. feladat')
bemeneti_sor_int = int(input('A meres soranak azonositoja=')) - 1
bemeneti_oszlop_int = int(input('A meres oszlopanak azonositoja=')) - 1
cella_melyseg = melyseg[bemeneti_sor_int][bemeneti_oszlop_int]
print(f'A mert melyseg az adott helyen {cella_melyseg} dm')


print('\n3. feladat')
"""
a felulet a nem-nulla ertekek szama [m^2]-ben
az atlag melyseg a melysegek osszege osztva a melysegek szamaval, átváltva m-be
"""
nem_felszin = 0
melyseg_osszeg = 0
for sor_int_list in melyseg:
    nem_felszin += sor_int_list.count(0)
    melyseg_osszeg += sum(sor_int_list)
## alternativ
# nem_felszin = sum(map(lambda x: x.count(0), melyseg))
# melyseg_osszeg = sum(map(sum, melyseg))
meresek_szama = sorok_szama*oszlopok_szama
felszin = meresek_szama-nem_felszin
atlag_melyseg = melyseg_osszeg/felszin
print(f'A to felszine {felszin} m2, atlagos melysege: {atlag_melyseg/10:.2f} m')


print('\n4. feladat')
max_ertek = -1
max_helyek = list()
for sorszam, sor_int_list in enumerate(melyseg):
    for oszlopszam, ertek in enumerate(sor_int_list):
        if max_ertek < ertek:
            max_ertek = ertek
            max_helyek = [(sorszam+1, oszlopszam+1),]  #+1 hogy kesobb ne kelljen meg1x vegigmenni rajtuk egyesevel a kiirashoz
        elif max_ertek == ertek:
            max_helyek.append((sorszam, oszlopszam))
print(f'A to legnagyobb melysege: {max_ertek} dm')
print('A legmelyebb helyek sor-oszlop koordinátái:')
# print(max_helyek)
# print(*max_helyek, sep='\t')
print('\t'.join(map(str, max_helyek)))  #hasonlit a peldara, de a sima print is jo

print('\n5. feladat')
partszakasz = 0
for sorszam in range(sorok_szama):
    for oszlopszam in range(oszlopok_szama):
        if 0 < oszlopszam:
            bal = melyseg[sorszam][oszlopszam-1]
            jobb = melyseg[sorszam][oszlopszam]
            if (bal == 0) != (jobb == 0):
                partszakasz += 1
        if 0 < sorszam:
            felso = melyseg[sorszam-1][oszlopszam]
            also = melyseg[sorszam][oszlopszam]
            if (felso == 0) != (also == 0):
                partszakasz += 1
## alternativ
# partszakasz = 0
# for sor_int_list in melyseg:
#     for bal, jobb in zip(sor_int_list[:-1], sor_int_list[1:]):
#         if bool(bal) != bool(jobb):  # itt a != gyakorlatilag kizaro vagy (xor)
#             partszakasz += 1
# for oszlopszam in range(oszlopok_szama):
#     oszlop_int_list = [melyseg[k][oszlopszam] for k in range(sorok_szama)]
#     for felso, also in zip(oszlop_int_list[:-1], oszlop_int_list[1:]):
#         if bool(felso) != bool(also):
#             partszakasz += 1
print(f'A to partvonala {partszakasz} m hosszu')


print('\n6. feladat')
oszlop_azonosito_int = int(input('A vizsgalt szelveny oszlopanak azonositoja=')) - 1
with open('diagram.txt', 'w') as kimeneti_file:
    vizsgalt_oszlop = [melyseg[k][oszlop_azonosito_int] for k in range(sorok_szama)]
    for sorszam, ertek in enumerate(vizsgalt_oszlop):
        print(f'{sorszam:02d}{"*"*round(ertek/10)}', file=kimeneti_file)
        ## alternativ
        # szam = f'{sorszam:02d}'
        # csillagok = '*'*round(ertek/10)
        # print(szam+csillagok, file=kimeneti_file)

        # 02 a vezeto nullakat iratja ki 2 szamjegyig, d az intek betuje (floatoknal f)
        # masfele idezojelet hasznalunk belul mint kivul, kulonben errort dob
        # "string * int" muvelet int-szer egymas utan rakja a string-et
        # print(file=) miatt a fileba ir a konzol helyett
        # az alternativban a + pedig egymas utan fuz stringeket
    