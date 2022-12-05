
c = open("data/input_day5.txt")
lin = c.readlines()
lines_stn = [i.split("\n")[0] for i in lin]
ind = [k for k, i in enumerate(lines_stn) if i == ''][0]

list_layers = [[] for _ in range(int((len(lines_stn[0])+1)/4))]
list_layers2 = [[] for _ in range(int((len(lines_stn[0])+1)/4))]
for i in lines_stn[0:ind-1]:
    for indx, k in enumerate(i):
        if k not in '[' and k not in ']' and k not in ' ':
            list_layers[int((indx-1)/4)].append(k)
            list_layers2[int((indx-1)/4)].append(k)

for i in lines_stn[ind+1:len(lines_stn)]:
    n1 = int(i.split('move')[1].split(' from ')[0])
    n2 = int(i.split(' from ')[1].split(' to ')[0]) - 1
    n3 = int(i.split(' to ')[1]) - 1

    for k0 in range(n1):

        # Part 1
        list_layers[n3].insert(0, list_layers[n2][0])
        list_layers[n2].pop(0)

        # Part 2
        list_layers2[n3].insert(0, list_layers2[n2][n1-1-k0])
        list_layers2[n2].pop(n1-1-k0)


fin_list = []
fin_list2 = []
for k1, k2 in zip(list_layers, list_layers2):
    fin_list.append(k1[0])
    fin_list2.append(k2[0])

print(''.join(fin_list))
print(''.join(fin_list2))