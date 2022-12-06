# %%
data = open('Puzzle6_input.txt', 'r').readline()

# %%
# find the first grouping of unique chars of 4

startBlock = 0
for x in range(len(data) - 4):
    s = set(data[x:x+4])
    if len(s) == 4:
        print(x + 4)
        startBlock = x + 4
        break

# %%
# find the first grouping of unique chars of 14

startBlock = 0
for x in range(len(data) - 14):
    s = set(data[x:x+14])
    if len(s) == 14:
        print(x + 14)
        startBlock = x + 14
        break
