
c = open("data/input_day11.txt")
lines_stn = [i.split("\n")[0] for i in c.readlines()] + ['END']

kkk = 0
for k11, k12 in zip([3,1], [20, 10000]):
    kkk += 1
    mk_items = []; mk2 = []; mk_dic = []; dic = 1
    for k, l in enumerate(lines_stn):
        if k % 7 == 1: mk_items.append([int(kk) for kk in l.split(':')[1].split(',')]);
        if k % 7 == 3: mk_dic.append(int(l.split('by ')[1]));
    for m in mk_dic:
        dic *= m
    mkop = [0 for _ in range(len(mk_items))]
    for xx in range(k12):
        for mk_n, mk in enumerate(mk_items):
            for k, l in enumerate(lines_stn):
                if k == 2 + mk_n * 7:
                    mk2 = eval(
                    '[int((' + l.split(':')[1].split('=')[1] + ')/3) if k11 == 3 else int(' + l.split(':')[1].split('=')[1] + ') for old in mk ]')
                if k == 3 + mk_n * 7:
                    for m in mk2:
                        if m % dic == 0:
                            print('w')
                    [mk_items[int(lines_stn[k + 1 + int(k3 % int(l.split('by ')[1]) != 0)].split('monkey ')[1])].append(k3 % dic) for k3 in mk2]
            mkop[mk_n] += len(mk)
            mk_items[mk_n] = []
    mkop.sort(reverse = True)
    print(mkop[0] * mkop[1])