
c = open("data/input_day17.txt").readlines()
lines_stn = [i.split("\n")[0] for i in c]

obj = {0:[[0,0,0,0],[0,1,2,3]], 1: [[-2,-1,-1,-1,0],[1,0,1,2,1]], 2: [[-2,-2,-2,-1,0],[0,1,2,2,2]],
       3:[[0,-1,-2,-3],[0,0,0,0]], 4: [[-1,0,-1,0],[0,0,1,1]]}

per = 7*5*49
for kk1, kkkk in enumerate([2022, 40*per + 1_000_000_000_000 % per]):
    smapo = [['#' for _ in range(9)]] + [['#'] + ['.' for _ in range(7)] + ['#'] for _ in range(4)]
    l = len(smapo) - 1; tall = 0; kjj = 0
    kk2 = 0; kk = 0; my = len(smapo) - 1; mx = 3; mys = 0; mys2=0; kk2s =0; kk22=0; ct = 0; flag = False
    while kk < kkkk:
        ct += 1
        if ct > 15: flag = True
        if kk % per == 0 and flag:
            flag = False; ct = 0;  mys2 = my - mys;  kk22 = kk2 - kk2s; kk2s = kk2; mys = my; kjj += 1
        k = lines_stn[0][kk2 % len(lines_stn[0])]; j = 0
        mx = mx + 1 if k == '>' else mx - 1
        for l, m in zip(obj[kk % 5][0],obj[kk % 5][1]):
            if smapo[l + my][m + mx] == '#': j += 1
        if j > 0:
            mx = mx - 1 if k == '>' else mx + 1
        j = 0; my = my - 1
        for l, m in zip(obj[kk % 5][0],obj[kk % 5][1]):
            if smapo[l + my][m + mx] == '#': j += 1
        if j > 0:
            my = my + 1
            for l, m in zip(obj[kk % 5][0],obj[kk % 5][1]): smapo[l + my][m + mx] = '#'
            tall = max(tall, my);   my = tall + 4 - min(obj[(kk+1) % 5][0]);  g = my - len(smapo) + 1
            smapo += [['#'] + ['.' for _ in range(7)] + ['#'] for _ in range(g)]; kk += 1; mx = 3
        kk2 += 1
    if kk1 == 0: print(tall)
    if kk1 == 1: print(tall + (int((1_000_000_000_000 - kk) / per)) * mys2)
