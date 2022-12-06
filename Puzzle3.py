# Points for each character minus 1, (a is 0th position, z is 25th position, etc)
tr = [chr(x) for x in range(ord('a'), ord('z') + 1)]
# Make the list all uppercase and add it to the list, so A is 26th, and Z is last :P
tr += [x.upper() for x in tr]

data = open("Puzzle3_input.txt",'r')
points_a = 0
common_a = ""
points_b = 0
common_b = ""
bag_data = [x.strip(' \r\n') for x in data.readlines()]
for x in [x for x in zip(bag_data[::3], bag_data[1::3], bag_data[2::3])]:
    for y in x:
        mid = len(y)//2
        fp,sp = set(y[:mid]), set(y[mid:])
        v = fp.intersection(sp).pop()
        #print(f"Common: {v} - {tr.index(v) + 1}")
        points_a += (tr.index(v) + 1)
        common_a += v

    v = set.intersection(*map(set, x)).pop()
    # print(f"Common: {v} - {tr.index(v) + 1}")
    points_b += (tr.index(v) + 1)
    common_b += v

print(f"Total: {points_a} - 8039 - {common_a}")
print(f"Total: {points_b} - 2510 - {common_b}")
