
c = open("data/input_day14.txt").readlines()
lines_stn = [i.split("\n")[0] for i in c]

lil = []; la = lil.append
mina, maxa = tuple([500] * 2)
minb, maxb = tuple([1] * 2)

for j in lines_stn:
    h = j.split('->')
    for h1, h2 in zip(h[0:len(h)-1],h[1:len(h)]):
        h1a = int(h1.split(',')[0]); h2a = int(h2.split(',')[0]); mina, maxa = (min(mina, h1a, h2a), max(maxa, h1a, h2a))
        h1b = int(h1.split(',')[1]); h2b = int(h2.split(',')[1]); minb, maxb = (min(minb, h1b, h2b), max(maxb, h1b, h2b))

        [la((h1a, a)) for a in range(min(h1b,h2b),max(h1b,h2b)+1)] if h1a == h2a else [la((a, h1b)) for a in range(min(h1a,h2a),max(h1a,h2a)+1)]
map = {i+j*1j:'#' if (i,j) in lil else '.' for i in range(mina - 2,maxa + 3) for j in range(minb - 1, maxb + 2)}
for j in range(mina - 2,maxa + 3): map[j+(maxb+2)*1j] = '#'
px = 1; iter = 0; py = 500

for i2, k2 in enumerate(['px < maxb + 1', "not map[500+0*1j] == 'o'"]):
    while eval(k2):

        try:
            if not any([map[(py + k) + (px + 1) * 1j] == '.' for k in [-1, 0, 1]]): map[py+px*1j] = 'o'; iter += 1; px, py = (0, 500)
            elif any([map[py + (px + 1) * 1j] == k for k in ['o', '#']]):
                if map[(py-1) + (px + 1) * 1j] == '.': px += 1; py -= 1
                else:
                    if map[(py + 1) + (px + 1) * 1j] == '.': px += 1; py += 1
                    else: map[py+px*1j] = 'o'; iter += 1; px, py = (0, 500)
            else: px += 1
        except:
            mina -= 1; maxa += 1
            for j in range(minb - 1, maxb + 3): map[(mina - 2) + j * 1j] = '.'; map[(maxa + 2) + j * 1j] = '.'
            map[mina - 2 + (maxb+2) * 1j] = '#'; map[maxa + 2 + (maxb+2) * 1j] = '#'

    #for j in range(minb - 1, maxb + 3): print(''.join([map[i + j * 1j] for i in range(mina - 2, maxa + 3)]))
    print(iter)

