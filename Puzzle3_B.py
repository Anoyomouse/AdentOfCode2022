
tr = [chr(x) for x in range(ord('a'), ord('z') + 1)]
tr += [x.upper() for x in tr]

data = open("Puzzle3_input.txt",'r')
points = 0
bag_data = data.readlines()
for x in [x for x in zip(bag_data[::3], bag_data[1::3], bag_data[2::3])]:
    groups = [set(y.strip(' \t\n')) for y in x]
    common = groups[0].intersection(groups[1], groups[2])
    v = list(common)
    print(f"Common: {v[0]} - {tr.index(v[0]) + 1}")
    points += (tr.index(v[0]) + 1)

print(f"Total: {points}")
