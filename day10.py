
c = open("data/input_day10.txt")
lines_stn = [i.split("\n")[0] for i in c.readlines()]

## Part 1
k = [20, 60, 100, 140, 180, 220]; aux = 1; cy = [1]; cya = cy.append
for l in lines_stn:
    aux += [int(l.split(' ')[1]) if l.split(' ')[0] == 'addx' else 0][0]
    for kk in range(1 + int(l.split(' ')[0] == 'addx')):
        cya(aux) if kk == 1 else cya(cy[len(cy)-1])

print(sum([k1*cy[k1-1] for k1 in k]))

## Part 2
for k in range(6):
    print(''.join(['#' if ((i-1) % 40) + 1 in range(cy[i-1],cy[i-1]+3) else '.' for i in range(1+k*40, 41+k*40)]))
