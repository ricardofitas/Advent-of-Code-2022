
c = open("data/input_day7.txt")
lines_stn = [i.split("\n")[0] for i in c.readlines()] + ['$ ']
path = ''
dic = {'//_1': []}; dic_sum = {'//_1': 0}; maximo = 1; level = 0; dic_levels = {'//_1': level + 1}
last_level = ' '
valtot = 0
for k, i in enumerate(lines_stn):
    if '..' not in i and '$ cd' in i:
        level += 1
        last_level = i.split("cd ")[1]
        path = path + '/' + last_level + '_' + str(level)
    if '$ cd ..' in i:
        last_level = path.split('_' + str(level))[0].split('/')[-1]
        path = path.split('/' + last_level + '_' + str(level))[0]
        level -= 1
    if i == '$ ls':
        k0 = k + 1
        var = path
        while "$ " not in lines_stn[k0]:
            if "dir " in lines_stn[k0]:
                var2 = path + '/' + lines_stn[k0].split('dir ')[1] + '_' + str(level + 1)
                dic[var].append(var2)
                dic_levels[var2] = level + 1
                dic_sum[var2] = 0
                dic[var2] = []
                if maximo < dic_levels[var2]: maximo = dic_levels[var2]
            else:
                dic_sum[var] += int(lines_stn[k0].split(' ')[0])
                valtot += int(lines_stn[k0].split(' ')[0])

            k0 += 1

for i in range(maximo,0,-1):
    for key in dic:
        if dic_levels.get(key) == i:
            for j in dic.get(key):
                dic_sum[key] = dic_sum.get(key) + dic_sum.get(j)

print(sum([dic_sum.get(key) for key in dic_sum if dic_sum.get(key) < 100000]))

val = 30_000_000 - 70_000_000 + valtot
print(min([dic_sum.get(key) for key in dic_sum if dic_sum.get(key) > val]))