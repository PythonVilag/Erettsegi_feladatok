"""
Feladat: 2018_II Kerites
Keszitette: Pecsenye samu
E-mail: samu.pecsenye@gmail.com
"""

# print('1. feladat')
with open('kerites.txt', 'r') as bemeneti_file:
    keritesek = list()
    for sor_str in bemeneti_file:
        sor_list_str = sor_str.split()
        sor_list_str[0] = int(sor_list_str[0])
        sor_list_str[1] = int(sor_list_str[1])
        sor_list_str[2] = str(sor_list_str[2])  # redundans, már string
        keritesek.append(sor_list_str)
# a kesobbi feladatokban külön-külön is kellenek, ezért szétválogatva is taroljuk
paratlan_keritesek = [kerites for kerites in keritesek if kerites[0]]
paros_keritesek = [kerites for kerites in keritesek if not kerites[0]]

print('2. feladat')
print(f'Az eladott telkek szama: {len(keritesek)}')

print('\n3. feladat')
if keritesek[-1] == True:  # true-> páratlan oldal
    print('A paratlan oldalon adtak el az utolso telket')
    hazszam = len(paratlan_keritesek)*2-1
else :  # false-> páros oldal
    print('A paros oldalon adtak el az utolso telket')
    hazszam = len(paros_keritesek)*2
print(f'Az utolso telek hazszama: {hazszam}')  # ez mind2 esetben ugyanaz, csak a hazszamot szamoltunk maskepp

print('\n4. feladat')
sorszam = None
for k in range(len(paratlan_keritesek)-1): # -1, hogy a jobb ne tudjon tulfutni
    bal = paratlan_keritesek[k]
    jobb = paratlan_keritesek[k+1]
    if bal[2] == jobb[2] and bal[2] not in (':', '#'):
        sorszam = k 
        # break is lehetne itt, mert csak 1 kell (break-kel az elsot kapjuk, nelkule az utolsot)
hazszam = sorszam*2 + 1
print(f'A szomsedossal egyezik a kerites szine: {hazszam}')

print('\n5. feladat')
bemenet_hazszam = int(input('Adjon meg egy hazszamot:'))
if bemenet_hazszam % 2 == 0:
    sorszam = (bemenet_hazszam//2)-1  # 2, 4, 6 -> 0, 1, 2
    oldal_keritesek = paros_keritesek
else:
    sorszam = (bemenet_hazszam//2)  # 1, 3, 5 -> 0, 1, 2
    oldal_keritesek = paratlan_keritesek
print(f'A kerites szine / allapota: {oldal_keritesek[sorszam][2]}')

foglalt_szinek = list()
foglalt_szinek.append(oldal_keritesek[sorszam][2])
if sorszam != 0:
    foglalt_szinek.append(oldal_keritesek[sorszam-1][2])
if sorszam != len(oldal_keritesek)-1:
    foglalt_szinek.append(oldal_keritesek[sorszam+1][2])

valasztott_szin = None
for szin in 'DCBA':
    # mivel a haz es legfeljebb 2 szomszedja legfeljebb 3 szinű lehet, ezért 4 
    # szin kozott biztosan van egy szabad
    if szin not in foglalt_szinek:
        valasztott_szin = szin
        # itt is lehetne break, mert csak 1 kell
print(f'Egy lehetseges festesi szin: {valasztott_szin}')

# print('6. feladat')
with open('utcakep.txt','w') as kimeneti_file:
    elso_sor = str()
    masodik_sor = str()
    for sorszam, kerites in enumerate(paratlan_keritesek):
        hazszam = 2*sorszam+1
        elso_sor += kerites[2]*kerites[1]
        # a string*int a szöveget <int>-szer egymás után rakja: pl 'ab'*3 = 'ababab'

        masodik_sor += str(hazszam) + ' '*(kerites[1]-len(str(hazszam)))
        # ahhoz, hogy egy oszlopba keruljenek a sorszamok es a szinek, a sorszamok
        # utani spacek szama a kerites szelessege minusz a hazszam felirat szelessege
        
        # egy egyszerubb megoldas, ljust--'left justify', magyarul balra zár
        # masodik_sor += str(hazszam).ljust(kerites[1]) 

        # fstring formázást is használhatunk, de ez olvasatatlan :[
        # masodik_sor += f'{str(hazszam) :{" "}<{kerites[1]}}'
    print(elso_sor, file=kimeneti_file)
    print(masodik_sor, file=kimeneti_file, end='')  # a masodik sor utan nem rakunk uj sort, mert félünk a pontozótól
        
