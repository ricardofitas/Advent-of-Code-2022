c = open("data/input_day15.txt").readlines()
lines_stn = [i.split("\n")[0] for i in c]
sensors=[[int(i.split('Sensor at x=')[1].split(',')[0]),int(i.split('Sensor at x=')[1].split(', y=')[1].split(':')[0]),
            int(i.split('is at x=')[1].split(',')[0]),int(i.split('is at x=')[1].split(', y=')[1].split(':')[0])]
           for i in lines_stn]
Ss = [i[0:2] for i in sensors]; Bc = [i[2:4] for i in sensors]
yy = 10; hh = "mapf[yy + i*1j] == '#'"; i = yy; mapf = dict()
suma = 0
for j in Ss:
    mapf[j[0] + j[1] * 1j] = 'S'
    if j[1] == yy: suma += 1
for j in Bc: mapf[j[0] + j[1] * 1j] = 'B'

mapf2 = dict(); kmax = 4000000; p2n = 4000000

for k1, k2 in zip(Ss, Bc):
    tam = abs(k1[0] - k2[0]) + abs(k1[1] - k2[1]) - abs(i-k1[1])
    kkk = range(k1[0]-tam,k1[0] + tam + 1)
    for j in kkk:
        if j+i*1j not in mapf.keys(): mapf[j+i*1j] = '#'; suma += 1

for k1, k2 in zip(Ss, Bc):
    md = abs(k1[0] - k2[0]) + abs(k1[1] - k2[1]) + 1
    for i in range(k1[1] - md, k1[1] + md + 1):
        for j in [k1[0] - md + abs(k1[1]-i), k1[0] + 1 + md - abs(k1[1]-i)]:
            if i <= kmax and j <= kmax and i >= 0 and j >= 0:
                mapf2[j + i * 1j] = (j, i)

flag2 = True; kkkk2 = 0
gg = [key for key in mapf2.keys()]; j = 0
while flag2:
    j, i = mapf2[gg[kkkk2]]
    kkkkk = 0; flag = True
    while kkkkk < len(Ss) and flag:
        k1 = Ss[kkkkk]; k2 = Bc[kkkkk]
        md = abs(k1[0] - k2[0]) + abs(k1[1] - k2[1])
        md2 = abs(k1[0] - i) + abs(k1[1] - j)
        if md >= md2: flag = not flag
        kkkkk += 1
    if flag:
        flag2 = not flag2
    kkkk2 += 1

print(suma) # 5832528
print(int(i*p2n + j))


# 13360899249595