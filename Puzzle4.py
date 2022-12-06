raw_data = open('Puzzle4_input.txt', 'r')
data = raw_data.readlines()

count = 0
overlaps = 0
for x in data:
    a,b = x.split(',')
    i,j = [int(n) for n in a.split('-')]
    set1 = {z + i for z in range(j - i + 1)}
    i,j = [int(n) for n in b.split('-')]
    set2 = {z + i for z in range(j - i + 1)}
    if set1.issuperset(set2) or set2.issuperset(set1):
        count += 1
    if not set1.isdisjoint(set2):
        overlaps += 1

print(f"Count: {count}")
print(f"Overlaps: {overlaps}")
