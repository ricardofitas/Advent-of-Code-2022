from copy import deepcopy

c = open("data/input_day16.txt").readlines()
lines_stn = [i.split("\n")[0] for i in c]

listconv = {i.split('Valve ')[1].split(' has')[0]: [False, int(i.split('rate=')[1].split(';')[0]),
             [k.split(' ')[1] for k in i.split('valve')[1].split(',')]] for i in lines_stn}

def find_best_way(key1,key2, list_aux):

    best_way = []; new_best_way = []
    new_list = [k for k in listconv[key1][2] if not k in list_aux]
    for keyind in new_list:
        if keyind == key2:
            new_best_way = [key1, keyind]
            return new_best_way
        else:
            new_list_aux = list_aux + [keyind]
            best_way.append(find_best_way(keyind, key2, new_list_aux))
    best_way = [k for k in best_way if not k == []]
    if best_way:
        new_best_way.append(key1)
        [new_best_way.append(k) for k in min(best_way, key=len)]
    else: new_best_way = []

    return new_best_way

dic_ways = dict()
for key1 in listconv.keys():
    for key2 in listconv.keys():
        if not key1 == key2: dic_ways[(key1,key2)] = find_best_way(key1,key2, [])

print(dic_ways)

minmax = 30
scoremax = 0

def score_max(score, path):
    global scoremax
    scoremax = max(score, scoremax)

def find_mov(list_ac, ominu, pres, score, curr_valve, path, move, lv):
    lec = deepcopy(list_ac)
    minu = ominu
    global scoremax
    listvalv = [k for k in lec[curr_valve][2]]
    listvalv2 = [k for k in listvalv if k not in lv]
    listvalv3 = [key for key in lec.keys() if not lec[key][0] and not lec[key][1] == 0]
    if ominu >= 0:
        for move2 in [True, False]:
            if move2:
                if listvalv2 and listvalv3:
                    score_aux = {}
                    ref = len(listvalv3)
                    for valve in listvalv3:
                        ref -= 1
                        if path == 'AAT/': print(ref, valve)
                        minu = ominu
                        score_aux[valve] = listconv[valve][1] * (minu - len(dic_ways[(curr_valve,valve)]))
                        new_path = path
                        new_lv = lv + listvalv2
                        new_score = score + pres
                        for l in dic_ways[(curr_valve, valve)][1:]:
                            new_path = new_path + l + "T/"
                            listvalv = [k for k in lec[l][2]]
                            listvalv2 = [k for k in listvalv if k not in lv]
                            new_lv = lv + listvalv2
                            minu = minu - 1
                            new_score = new_score + pres
                            if minu == 0: score_max(new_score - pres, new_path)
                        new_pres = pres
                        new_score = new_score - pres
                        find_mov(lec, minu, new_pres, new_score, valve, new_path, True, new_lv)
                else:
                        new_score = score + pres * minu
                        score_max(new_score, path)

            if listvalv3 and len(set(lv)) == len(lv) and not move2 and move and listvalv and not \
                    lec[curr_valve][1] == 0 and not lec[curr_valve][0]:
                new_pres = pres + lec[curr_valve][1]
                new_score = score + pres
                new_path = path + curr_valve + "F/"
                lec[curr_valve][0] = True
                if minu == 1:  score_max(new_score, new_path)
                find_mov(lec, minu - 1, new_pres, new_score, curr_valve, new_path, not move, [curr_valve])


scores_dict = dict()
list_ac = deepcopy(listconv)
find_mov(list_ac, minmax,0,0, 'AA', "AAT/", True, ['AA'])

print(scoremax) # 1754