
c = open("data/input_day4.txt")
lin = c.readlines()
lines_stn = [i.split("\n")[0] for i in lin]

sum1 = 0
sum2 = 0
for k1,k in enumerate([[j[0].split("-"), j[1].split("-")] for j in [i.split(",") for i in lines_stn]]):
    r = [int(k[0][0]), int(k[1][0]), int(k[0][1]), int(k[1][1])]

    ## Part 1
    if (r[0] <= r[1] and r[2] >= r[3]) or (r[0] >= r[1] and r[2] <= r[3]):
        sum1 += 1

    ## Part 2
    if (r[2] >= r[1] and r[0] <= r[3]) or (r[2] <= r[1] and r[0] >= r[3]):
        sum2 += 1

print(sum1)
print(sum2)