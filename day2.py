
c = open("data/input_day2.txt")
lin = c.readlines()
lines_stn = [i.split("\n")[0] for i in lin]

## Part 1
wins_poss = ['A Y', 'B Z', 'C X']
draws_poss = ['A X', 'B Y', 'C Z']
dici = {'X': 1, 'Y': 2, 'Z': 3}
list_pts_win = sum([6 for k in lines_stn if k in wins_poss])
list_pts_draw = sum([3 for k in lines_stn if k in draws_poss])
list_shapes = sum([dici.get(k.split(' ')[1]) for k in lines_stn])
print(sum([list_pts_win, list_pts_draw, list_shapes]))

## Part 2
rock_poss = ['A Y', 'B X', 'C Z']
paper_poss = ['A Z', 'B Y', 'C X']
dici = {'X': 0, 'Y': 3, 'Z': 6}
list_pts_rock = sum([1 for k in lines_stn if k in rock_poss])
list_pts_paper = sum([2 for k in lines_stn if k in paper_poss])
list_pts_scissors = sum([3 for k in lines_stn if k not in rock_poss + paper_poss])
list_fin = sum([dici.get(k.split(' ')[1]) for k in lines_stn])
print(sum([list_pts_rock, list_pts_paper, list_pts_scissors, list_fin]))
