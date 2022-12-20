
c = open("data/input_day20.txt").readlines()

for part, rounds in enumerate([1,10]):
    lines_stn = [int(i.split("\n")[0]) for i in c]; h = []
    listn = [k for k in range(len(lines_stn))]
    if part == 1: lines_stn = [k*811589153 for k in lines_stn]
    for _ in range(rounds):
        for ind in range(len(lines_stn)):
            ind2 = listn.index(ind)
            listn.remove(ind)
            nind = (ind2 + lines_stn[ind] - 1) % (len(lines_stn)-1) + 1 if not lines_stn[ind] == 0 else ind2
            listn.insert(nind, ind)

    for k in [1000, 2000, 3000]:
        ind2 = [lines_stn[kk] for kk in listn].index(0)
        h.append( lines_stn[listn[(ind2 + k) % len(lines_stn)]] )
    print(sum(h))