
c = open("data/input_day13.txt").readlines(); c[len(c)-1] += '\n'; c += ['\n', '[[6]]\n', '[[2]]\n']
lines_stn = [i.split("\n")[0] for i in c]

def unpack_cmp(pa2, pb2):

    pa = [i for i in pa2]; pb = [i for i in pb2]; flag = True; flag2 = True
    while pa and pb and flag and flag2:
        if type(pa[0]) == list or type(pb[0]) == list:
            if type(pa[0]) != list: pa[0] = [pa[0]]
            if type(pb[0]) != list: pb[0] = [pb[0]]
            flag, flag2 = unpack_cmp(pa[0],pb[0])
        else:
            flag = (pa[0] == pb[0])
            if not flag: flag2 = not (pa[0] > pb[0])
        pa.pop(0); pb.pop(0)

    if not len(pb) and len(pa) and flag: flag2 = not flag2; flag = not flag
    if not len(pa) and len(pb) and flag: flag = not flag

    return flag, flag2

def sort_pack(pack):
    sa = []
    for i, p in enumerate(pack):
        m = 0
        for j, k in enumerate(pack):
            if j != i:
                _, flag2 = unpack_cmp(k, p)
                if flag2: m += 1
        sa.append(m)
    pack2 = [pack[[kk for kk in range(len(sa)) if sa[kk] == i][0]] for i in range(len(pack))]
    return [i+1 for i,k in enumerate(pack2) if k == [[2]]][0]*[i+1 for i,k in enumerate(pack2) if k == [[6]]][0]

kk = []; ka = kk.append
pack = []; packa = pack.append
for k,i in enumerate(range(0,len(lines_stn),3)):
    pa, pb = eval('(' + lines_stn[i] + ', ' + lines_stn[i+1] + ')')
    packa(eval( lines_stn[i]))
    packa(eval(lines_stn[i+1]))
    flag, flag2 = unpack_cmp(pa, pb)
    if flag2:
        ka(k + 1)

print(sum(kk))
print(sort_pack(pack))