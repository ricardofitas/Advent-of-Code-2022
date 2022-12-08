
c = open("data/input_day8.txt")
lines_stn = [list(i.split("\n")[0]) for i in c.readlines()]

fin_list = []
fin_list2 = []

for k,i in enumerate(lines_stn[1:len(lines_stn)-1]):
    for k2, j in enumerate(i[1:len(i)-1]):

        ## Part 1

        fin_list.append(int(any([all([int(j) > int(j2) for j2 in [i2[k2+1] for i2 in lines_stn[0:k+1]]]),
                                   all([int(j) > int(j2) for j2 in [i2[k2+1] for i2 in lines_stn[k+2:]]]),
                                   all([int(j) > int(j2) for j2 in lines_stn[k+1][0:k2+1]]),
                                   all([int(j) > int(j2) for j2 in lines_stn[k+1][k2+2:]])])))

        ## Part 2
        val_aux = 1
        list_aux = [[i2[k2+1] for i2 in lines_stn[0:k+1]], [i2[k2+1] for i2 in lines_stn[k+2:]],
                    lines_stn[k+1][0:k2+1], lines_stn[k+1][k2+2:]]
        k_aux = [[k + 1, -1], [1,1], [k2 + 1, -1], [1,1]]
        for k4, kk in enumerate(list_aux):
            v2_aux = min([len(kk) if int(j) > int(j2) else abs(
                                       int(int(j) > int(j2)) - 1) * (k_aux[k4][0] + k_aux[k4][1] * k3) for k3, j2 in
                                        enumerate(kk)])
            val_aux = val_aux * v2_aux
        fin_list2.append(val_aux)

print(sum(fin_list) + len(lines_stn)*2 + 2*(len(lines_stn[0])-2))
print(max(fin_list2))
