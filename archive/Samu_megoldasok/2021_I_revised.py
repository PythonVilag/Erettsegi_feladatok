"""
Feladat: 2021_INY Banyato
Keszitette: Pecsenye Samu
E-mail: samu.pecsenye@gmail.com
"""

print('1. feladat')
with open('melyseg.txt', 'r') as forras_file:
    melysegek = list(map(int, forras_file))
sorok_szama = len(melysegek)
print(f'A file adatainak szama: {sorok_szama}')


print('\n2. feladat', end='')
bemeneti_sorszam = int(input('Adjon meg egy tavolsagerteket:'))-1
print(f'Ezen a helyen a felszin {melysegek[bemeneti_sorszam]}')


print('\n3. feladat')
nullak_szama = melysegek.count(0)
nullak_aranya = nullak_szama/len(melysegek)
print(f'Az erintetlen terulet aranya {100*nullak_aranya:.2f}%')


#print('\n4. feladat')
print('\n5. feladat')
godrok_szama = 0
with open('godrok.txt', 'w') as kimeneti_file:
    godor_list = list()
    for ertek in melysegek:
        if ertek == 0:
            if 0 < len(godor_list):
                print(''.join(godor_list), file=kimeneti_file)  # az utolso godrot nem írná ki, ha a melysegek nem 0-val vegzodne, de a feladat szerint az elso es utolso ertek mindig 0.
                godor_list = list()
                godrok_szama += 1
        else:
            godor_list.append(str(ertek))
print(f'A godrok szama: {godrok_szama}')


print('\n6. feladat')
if melysegek[bemeneti_sorszam] == 0:
    print('Az adott helyen nincs godor')
else:
    print('a,')
    # for bal_lepesek, ertek in enumerate(melysegek[bementi_sorszam::-1]):
    #     if ertek == 0: break
    # for jobb_lepesek, ertek in enumerate(melysegek[bemeneti_sorszam:]):
    #     if ertek == 0: break
    kezdet = bemeneti_sorszam
    while melysegek[kezdet] != 0:
        kezdet -= 1
    veg = bemeneti_sorszam
    while melysegek[veg] != 0:
        veg += 1   
    # kezdet es veg az elso nullakra mutat, ezért eltoljuk egyel
    kezdet += 1
    veg -= 1
    print(f'A godor kezdete: {kezdet+1} meter, a godor vege: {veg+1} meter')
    
    
    print('b,')
    max_ertek = melysegek[kezdet]
    max_hely = 0
    for sorszam, ertek in enumerate(melysegek[kezdet:veg+1]):
        if max_ertek < ertek:
            max_ertek = ertek
            max_hely = sorszam
    folyton_melyul = True
    for sorszam, ertek in enumerate(melysegek[kezdet:veg+1]):
        if sorszam < max_hely and ertek > max_ertek:
            folyton_melyul = False
        if max_hely < sorszam and max_ertek < ertek:
            folyton_melyul = False
    if folyton_melyul:
        print('Folyamatosan melyul')
    else:
        print('Nem melyul folyamatosan')
    
    
    print('c,')
    print(f'A legnyagyobb melysege {max_ertek} meter')
    
    
    print('d,')
    melyseg_osszeg = sum(melysegek[kezdet:veg+1])
    print(f'A terfogata {melyseg_osszeg*10} m^3')
    
    
    print('e,')
    viz_osszeg = melyseg_osszeg - (veg-kezdet+1)
    print(f'A vizmennyiseg {10*viz_osszeg} m^3')
