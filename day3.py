
c = open("data/input_day3.txt")
lin = c.readlines()
lines_stn = [i.split("\n")[0] for i in lin]

## Part 1
comp = [[i[0:int(len(i)/2)],i[int(len(i)/2):len(i)]] for i in lines_stn]
sum = 0
for k,i in enumerate([i[0] for i in comp]):
    flag = 0
    for j in i:
        if j in comp[k][1] and flag ==0:
            if ord(j) > 96:
                sum += ord(j) - 96
                flag = 1
            else:
                sum += ord(j) - 38
                flag = 1
print(sum)

## Part 2
comp = [lines_stn[k:k+3] for k in range(0,len(lines_stn),3)]
sum = 0
for i in comp:
    flag = 0
    for j in i[0]:
        if j in i[1] and j in i[2] and flag ==0:
            if ord(j) > 96:
                sum += ord(j) - 96
                flag = 1
            else:
                sum += ord(j) - 38
                flag = 1
print(sum)