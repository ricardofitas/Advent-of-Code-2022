
c = open("data/input_day9.txt")
lines_stn = [i.split("\n")[0] for i in c.readlines()]; tm = [[[0,0]] for _ in range(10)]
coord = {'R': [0, 1], 'L': [0, -1], 'U': [-1, 0], 'D': [1, 0]}

for k, i in enumerate(lines_stn):
    for i2 in range(int(i.split(' ')[1])):
        h2 = tm[0]; ha = h2.append
        ha([h2[len(h2) - 1][k2] + coord.get(i.split(' ')[0])[k2] for k2 in range(2)])
        for h, t in zip(tm[0:len(tm)-1],tm[1:len(tm)]):
            ta = t.append
            if any([(h[len(h)-1][k2]-t[len(t)-1][k2])**2 == 4 for k2 in range(2)]):
                aux2 = [0,0]
                if any([(h[len(h)-1][k2]-t[len(t)-1][k2])**2 == 1 for k2 in range(2)]):
                    aux2 = [aux2[k2] + (h[len(h) - 1][k2] - t[len(t) - 1][k2]) * int((h[len(h) - 1][k2] - t[len(t) - 1][k2]) ** 2 == 1)
                        for k2 in range(2)]
                aux3 = [h[len(h) - 1][k2] - t[len(t) - 1][k2] for k2 in range(2)]
                aux4 = [1 if h[len(h) - 1][k2] - t[len(t) - 1][k2] > 0 else -1 for k2 in range(2)]
                aux2 = [aux2[k2] + (aux3[k2] - aux4[k2])*int((h[len(h) - 1][k2] - t[len(t) - 1][k2]) ** 2 == 4) for k2 in range(2)]
                ta([aux2[k2] +t[len(t) - 1][k2] for k2 in range(2)])
            else:
                ta([t[len(t) - 1][k2] for k2 in range(2)])

print(len([list(x) for x in set(tuple(x) for x in tm[9])]))