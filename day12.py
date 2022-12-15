
c = open("data/input_day12.txt")
lines_stn = [i.split("\n")[0] for i in c.readlines()]

g = {i+j*1j:c for i,row in enumerate(lines_stn) for j,c in enumerate(row)}
start ,= (z for z,c in g.items() if c == 'S')
end ,= (z for z,c in g.items() if c == 'E')
g[start] = 'a'; g[end] = 'z'; qm = [[(start,0)],[(end,0)]]

for kq, q in enumerate(qm):
    dists = {start: 0} if kq == 0 else {end: 0}
    while q:
        z,d = q.pop(0); lll = []; c = g[z]
        for i in range(4):
            nz = z + 1j ** i
            if nz in g:
                nc = g[nz]
                fl = ord(nc) <= ord(c) + 1 if kq == 0 else ord(c) <= ord(nc) + 1
                if fl: lll.append(nz)
        for w in lll:
            if w not in dists:
                dists[w]=d+1; q.append((w,d+1))
    if kq == 1:
        p2 = 9 ** 9
        for start in (z for z, c in g.items() if c == 'a'):
            if start in dists and dists[start] < p2: p2 = dists[start]
        print(p2)
    else:
        print(dists[end])

