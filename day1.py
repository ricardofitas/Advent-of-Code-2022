
c = open("data/input_day1.txt")
lin = c.readlines()
lines_stn = [i.split("\n")[0] for i in lin]

ind = [-1] + [k for k,i in enumerate(lines_stn) if i == ""] + [len(lines_stn)]
list_calories = sorted([sum([int(kk) for kk in lines_stn[i+1:j]]) for i,j in zip(ind[0:-1],ind[1:])])

## Part 1
no_elves = 1
list = sum(list_calories[-no_elves:])
print(list)

## Part 2
no_elves = 3
list = sum(list_calories[-no_elves:])
print(list)

