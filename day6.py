
lin = open("data/input_day6.txt").readlines()[0]
print([[ind + kk for ind,_ in enumerate(lin[0:len(lin[0])-kk-1]) if len(list(set([ord(l) for l in lin[ind:ind+kk]]))) == len(lin[ind:ind+kk])][0] for kk in [4,14]])


