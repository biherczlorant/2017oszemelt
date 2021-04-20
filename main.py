# 1. feladat
data = []
with open('naplo.txt', 'r') as f:
    for line in f:
        if line.startswith('#'):
            bonto = line.strip().split()
            honap = bonto[1]
            nap = bonto[2]
        else:
            bonto = line.strip().split()
            date = {'honap': int(honap),
                    'nap': int(nap),
                    'nev': bonto[0] + " " + bonto[1],
                    'hianyzasok': bonto[2]}
            data.append(date)
# 2. feladat
print(f'2.feladat\nA naplóban {data.__len__()} bejegyzés van. ')
# 3. feladat
igazolt = 0
igazolatlan = 0
for i in data:
    for j in i['hianyzasok']:
        if j == 'I':
            igazolatlan += 1
        elif j == 'X':
            igazolt += 1
print(f'3. feladat\nAz igazolt hiányzások száma {igazolt}, az igazolatlanoké {igazolatlan} óra.')


# 4. feladat
def hetnapja(honap: int, nap: int):
    napnev = ['vasárnap', 'hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek', 'szombat']
    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam = (napszam[honap - 1] + nap) % 7
    return napnev[napsorszam]

# 5. feladat
print(f'5. feladat')
honap = int(input("A hónap sorszáma="))
nap = int(input("A nap sorszáma="))
print(f"Azon a napon {hetnapja(honap, nap)} volt.")

# 6. feladat
print('6. feladat')
napnev = input('A nap neve=')
osor = int(input('Az óra sorszáma='))
hianyszamol = 0
for i in data:
    if hetnapja(i['honap'], i['nap']) == napnev:
        if i['hianyzasok'][osor-1] == 'X' or i['hianyzasok'][osor-1] == 'I':
            hianyszamol += 1
print(f'Ekkor összesen {hianyszamol} óra hiányzás történt.')

# 7. feladat
tanulok = set()
maxhiany = 0
maxhianynev = []
for i in data:
    tanulok.add(i['nev'])
for tanulo in sorted(tanulok):
    hianyzasok = 0
    tanulohianyzas = [i['hianyzasok'] for i in data if i['nev']==tanulo]
    for j in tanulohianyzas:
        hianyzasok += j.count('X')
        hianyzasok += j.count('I')
    if hianyzasok > maxhiany:
        maxhiany = hianyzasok
    valami = {'nev': tanulo,
              'hiany': hianyzasok}
    maxhianynev.append(valami)
print('7. feladat\nA legtöbbet hiányzó tanulók:', end=" ")
for i in maxhianynev:
    if i['hiany'] == maxhiany:
        print(f'{i["nev"]}', end=" ")
