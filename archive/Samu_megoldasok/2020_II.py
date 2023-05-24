# 2020_II sorozatok
source = open('lista.txt', 'r')

records = list()
while True:
    row = source.readline()
    if not row: break
    record = dict()
    record['date'] = row.strip()
    record['title'] = source.readline().strip()
    record['SxEE'] = source.readline().strip()
    record['runtime'] = source.readline().strip()
    record['watched'] = source.readline().strip()
    records.append(record)

print("2. feladat")
num_of_NI = list(map(lambda rec: rec['date'], records)).count('NI')
num_of_I = len(records)-num_of_NI
print(f'{num_of_I} db ismert datum')

print("3. feladat")
num_of_watched = list(map(lambda rec: rec['watched'], records)).count('1')
if len(records) == 0:
    print('empty input file, zerodiv')
else:
    percentage = 100*num_of_watched/len(records)
    print(f'{percentage:.2f}%-at nezte meg')

print("4. feladat")
watchtime = 0
for rec in records:
    if rec['watched'] == '1':
        watchtime += int(rec['runtime'])
mins = watchtime%60
hours = watchtime//60%24
days = watchtime//(60*24)
print(f'nezessel toltott ido: {days} nap, {hours:02} ora, {mins:02} perc')

print("5. feladat")
input_date = input('Adj meg egy datumot!')
for rec in records:
    if rec['date'] <= input_date: # string compare beturend szerint, a formatum miatt mukodik
        if rec['watched'] == '0':
            print(rec['SxEE'], '\t', rec['title'])

print("6. feladat")
def Hetnapja(year, month, day):
    days = "v h k sze cs p szo".split()
    months = (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
    if month < 3:
        year -= 1
    return days[(year + (year//4) - (year//100) + (year//400) + months[month-1] + day) % 7]

print("7. feladat")
input_day = input('Válassz egy napot (h k sze cs p szo v):')
shows = set()
for rec in records:
    if rec['date'] == 'NI': continue
    year, month, day = map(int, rec['date'].split('.'))
    if Hetnapja(year, month, day) == input_day:
        shows.add(rec['title'])
if not shows:
    print('Az adott napon nem kerul adasba sorozat')
else:
    for show in shows:
        print(show)
print("8. feladat")
shows = dict()
for rec in records:
    title = rec['title']
    if title not in shows:
        shows[title] = [0, 0]
    shows[title][0] += int(rec['runtime'])
    shows[title][1] += 1

dest = open('summa.txt', 'w')
for title, (runtime, eps) in shows.items():
    print(f'{title} {runtime} {eps}', file=dest)
dest.close()
    
    
    