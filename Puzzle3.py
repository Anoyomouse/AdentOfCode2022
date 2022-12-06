# Points for each character minus 1, (a is 0th position, z is 25th position, etc)
tr = [chr(x) for x in range(ord('a'), ord('z') + 1)]
# Make the list all uppercase and add it to the list, so A is 26th, and Z is last :P
tr += [x.upper() for x in tr]

data = open("Puzzle3_input.txt",'r')
points_a = 0
points_b = 0
bag_data = data.readlines()
for x in [x for x in zip(bag_data[::3], bag_data[1::3], bag_data[2::3])]:
    for y in x:
        y = y.strip(' \t\n')
        mid = len(y)//2
        fp,sp = set(y[:mid]), set(y[mid:])
        v = list(fp.intersection(sp))
        #print(f"Common: {v[0]} - {tr.index(v[0]) + 1}")
        points_a += (tr.index(v[0]) + 1)

    groups = [set(y.strip(' \t\n')) for y in x]
    common = groups[0].intersection(groups[1], groups[2])
    v = list(common)
    # print(f"Common: {v[0]} - {tr.index(v[0]) + 1}")
    points_b += (tr.index(v[0]) + 1)

print(f"Total: {points_a} - 8039")
print(f"Total: {points_b} - 2510")
