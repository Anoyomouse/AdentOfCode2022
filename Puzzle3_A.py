
tr = [chr(x) for x in range(ord('a'), ord('z') + 1)]
tr += [x.upper() for x in tr]

data = open("Puzzle3_input.txt",'r')
points = 0
for x in data.readlines():
    x = x.strip(' \t\n')
    mid = int(len(x)/2)
    fp,sp = set(x[:mid]), set(x[mid:])
    v = list(fp.intersection(sp))
    #print(f"Common: {v[0]} - {tr.index(v[0]) + 1}")
    points += (tr.index(v[0]) + 1)

print(f"Total: {points}")
