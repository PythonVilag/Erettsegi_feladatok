# 2021_II sudoku
print('1. feladat')
input_filename = input('fájlnév:')
input_row = int(input('sor index:'))-1  # -1 to convert to 0-indexed
input_col = int(input('oszlop index:'))-1  # -1 to convert to 0-indexed
print('2. feladat')
source = open(input_filename, 'r')
array = [0 for _ in range(9)]  # 9 empty rows for the grid
for row_index in range(9):
    row_str = source.readline()
    row_list_str = row_str.split()  # default separator -> any whitespace
    row_list_int = list(map(int, row_list_str))
    ### alternative to map
    # row_list_int = list()
    # for element_str in row_list_str:
    #     element_int = int(element_str)
    #     row_list_int.append(element_int)
    array[row_index] = row_list_int
print('3. feladat')
element = array[input_row][input_col]
if element == 0:  # ~~ if not element, but thats ugly
    print('Az adott helyet meg nem toltottek ki.')
else:
    print(element)
row = (input_row)//3  # 0..8 -> (0, 0, 0, 1, 1, 1, 2, 2, 2)
col = (input_col)//3
region = row*3+col+1  # +1 because of 0-indexing
# pelda 4. sor 9. oszlop -> input_row=3, input_col=8 -> row=1, col=2 ->
# region=1*3+2+1=6, es valoban, (4,9) a jobb kozepso regio, ami a 6. szamu
print(f'A beolvasott cella a(z) {region}. resztablazathoz tartozik')
print('4. feladat')
num_of_zeros = 0
for row in array:
    num_of_zeros += row.count(0)
percentage = 100 * num_of_zeros / 81
print(f'A tablazat {percentage:.1f}%-a nincs kitoltve.')
print('5. feladat')
for row_str in source:  # iterates over lines, ends at EOF
    row_list_str = row_str.split()
    row_list_int = map(int, row_list_str)
    n, y, x = row_list_int
    ### alternative to map
    # n = int(row_list[0])
    # y = int(row_list[1])
    # x = int(row_list[2])
    print(f'valasztott sor: {y}, oszlop: {x}, szam: {n}')  # print before -1
    y -= 1  # 0-indexing
    x -= 1  # 0-indexing
    if array[y][x] != 0:
        print(f'Mar ki van toltve.')
    else:
        row = array[y]
        column = map(lambda row: row[x], array)  # extract the x-th element from every row in array
        ### alternative to map
        # column = [row[x] for row in array]
        top = y - y%3
        left = x - x%3
        region = set()
        for y in range(top, top+3):
            for x in range(left, left+3):
                region.add(array[y][x])
        if n in row:
            print('Mar szerepel a sorban')
        elif n in column:
            print('Mar szerepel az oszlopban')
        elif n in region:
            print('Mar szerepel a resztablazatban')
        else:
            print('A lepes megteheto')
