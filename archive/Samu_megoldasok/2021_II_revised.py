"""
Feladat: 2021_II Sudoku
Keszitette: Pecsenye Samu
E-mail: samu.pecsenye@gmail.com
"""


print('\n1. feladat')
bemeneti_filenev_str = input('Add meg a bemeneti fájlnevet:')
bemeneti_sor_int = int(input('Add meg a sor indexét:')) - 1
bemeneti_oszlop_int = int(input('Add meg az oszlop indexét:')) - 1


print('\n2. feladat')
tablazat = list()
lepesek = list()
x = int()
with open(bemeneti_filenev_str, 'r') as forras_file:
    for sorszam, sor_str in enumerate(forras_file):
        sor_str_list = sor_str.strip().split()
        sor_int_list = list(map(int, sor_str_list))
        if sorszam < 9:
            tablazat.append(sor_int_list)
        else:
            lepesek.append(sor_int_list)


print('\n3. feladat')
cella_int = tablazat[bemeneti_sor_int][bemeneti_oszlop_int]

def resztablazat(sor, oszlop):
    """
    A resztablazat szama jobbra 1-gyel növekszik 3 cellánként,
    lefelé peding 3-mal. A bal felső pedig az 1-es szamú.
    """
    resztabla_sorszam = (sor//3)*3 + (oszlop//3) + 1
    return resztabla_sorszam

if cella_int == 0:
    print('Az adott helyet még nem töltötték ki.')
else:
    print(f'Az adott helyen szerplő szám: {cella_int}')
resztabla_sorszam = resztablazat(bemeneti_sor_int, bemeneti_oszlop_int)
print(f'A  cella az {resztabla_sorszam}. resztablazatba tartozik')


print('\n4. feladat')
nullak_szama = 0
for sor_int_list in tablazat:
    nullak_szama += sor_int_list.count(0)
print(f'Az üres helyek aránya: {100*nullak_szama/81:.1f}%')


print('\n5. feladat')
for lepes in lepesek:
    szam = lepes[0]
    sor = lepes[1] - 1
    oszlop = lepes[2] - 1
    print(f'A kiválasztott sor: {sor+1}, oszlop: {oszlop+1}, szam: {szam}')
    if tablazat[sor][oszlop] != 0:
        print('A helyet mar kitoltottek')
    elif szam in tablazat[sor]: 
        print('Az adott sorban mar szerepel a szam')
    elif szam in [sor_int_list[oszlop] for sor_int_list in tablazat]:
        print('Az adott oszlopban mar szerepel a szam')
    else:
        resztabla_flag = False
        balfelso_sor = (sor//3)*3
        balfelso_oszlop = (oszlop//3)*3
        for sorszam in range(balfelso_sor, balfelso_sor+3):
            for oszlopszam in range(balfelso_oszlop, balfelso_oszlop+3):
                if szam == tablazat[sorszam][oszlopszam]:
                    resztabla_flag = True
        if resztabla_flag:
            print('Az adott resztablazatban mar szerepel a szam')
        else:
            print('A lepes megteheto')
    print()
            
