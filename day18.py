
c = open("data/input_day18.txt").readlines()
lines_stn = [[int(k) for k in i.split("\n")[0].split(',')] for i in c]; score = 6

# Part 1
for ind,k in enumerate(lines_stn[1:]):
    score += 6
    for k2 in lines_stn[0:ind+1]:
        if sum([abs(k2[x]-k[x]) for x in range(3)]) == 1: score -= 2;
score2 = score; lines_stn2 = lines_stn
print(score)

# Part 2
dic = dict()
for j in lines_stn:
    for j2 in lines_stn:
            mapi2 = [(k6 == kk) for k6, kk in zip(j, j2)]
            if sum(mapi2) == 2:
                g = []
                for kkkkk, m in enumerate(mapi2):
                    if not m:
                        for jj in range(min(j[kkkkk], j2[kkkkk]) + 1, max(j[kkkkk], j2[kkkkk])): g.append([jj,kkkkk])
                if g:
                    for indkg, k10 in enumerate([kg[0] for kg in g]):
                        h = tuple()
                        for kkkkk, m in enumerate(mapi2):
                            h = h + (k10,) if not m else h + (j[kkkkk],)
                        h2 = h + (g[indkg][1],)
                        if h not in dic.keys(): dic[h] = [0,0,0]
                        dic[h][g[indkg][1]] = 1

for key in dic.keys():
    if sum(dic[key]) == 3 and list(key) not in lines_stn:
        k1, k2, k3 = key
        lines_stn2.append([k1, k2, k3]); score2 += 6
        for k5 in lines_stn2[0:len(lines_stn2)]:
            if sum([abs(k5[x] - [k1, k2, k3][x]) for x in range(3)]) == 1: score2 -= 2

print(score2)
