#2021_I godor godrok vagy valami ilyesmi
print('1. feladat')
source = open('melyseg.txt', 'r')  # or open with, but not important
depths = list(map(int, source))
# depths = list()
# for string in source:
#     num = int(string)
#     depths.append(num)
print('2. feladat')
input_dist = int(input('tavolsag: '))-1  # nem egyertelmu, de szerintem itt is 1-indexelt az input, szoval konvertáltam
print(f'{input_dist+1} méternél a mélység: {depths[input_dist]}')
print('3. feladat')
num_of_zeros = depths.count(0)
percentage = num_of_zeros/len(depths)*100
print(f'A felszin {percentage:.2f}%-a maradt erintetlen')
print('4.+5. feladat')
dest = open('godrox.txt', 'w')
hole = list()
num_of_holes = 0
for d in depths:
    if d == 0:
        if 0 < len(hole):  # if hole, but thats harder to read
            print(''.join(hole), file=dest)
            hole = list()
            num_of_holes += 1
    else:
        hole.append(str(d))
# utolso hole-t nem irja ki ha nem 0-val van vege a depths-nek, de a feladat
# szerint mindig 0 az elso es az utolso ertek, szoval nem kell lekezelni
dest.close()  # always close files opened for writing
print('godrok szama:', num_of_holes)
print('6. feladat')
if depths[input_dist] == 0:
    print('nincs godor')
else:
    print('6a feladat')
    for right, d in enumerate(depths[input_dist:]):
        if d == 0: break
    # right: steps from input_dist to find a zero
    right = input_dist + right -1  # index of last non-zero element of hole
    for left, d in enumerate(depths[input_dist::-1]):
        if d == 0: break
    # left: steps from input_dist to find a zero
    left = input_dist - left +1  # index of first non-zero element of hole
    print(f'kezdet:{left+1}, veg:{right+1}')  # back to 1-indexed numbers
    
    print('6b+6c feladat')
    dmax = depths[left]
    monotone = True
    for k, d in enumerate(depths[left:right+1], start=left):
        if d < dmax: break
    for d in depths[k:right+1]:
        if dmax < d:
            monotone = False
            dmax = d
    if monotone:
        print('folyamatosan melyul')
    else:
        print('nem melyul folyamatosan')
    print(f'max melyseg: {dmax}')
    print('6d feladat')
    volume = sum(depths[left:right+1])*10
    print(f'terfogat: {volume}')
    print('6e feladat')
    water = volume-10*(right-left+1)
    print(f'vizmennyiseg: {water}')
    
    


        