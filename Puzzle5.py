# %%
data = open('Puzzle5_input.txt', 'r').readlines()

# %%
stacks = [list() for x in range(9)]

nums = [chr(ord('0') + x) for x in range(10)]

for x in data:
    x = x.strip('\n')
    if x == "":
        break
    for y in range(9):
        val = x[1 + (y * 4)]
        if val != " ": # and val not in nums:
            stacks[y].append(val)

start_stacks = [x[::-1] for x in stacks]

# %%
stacks = list(start_stacks)
start = False
for x in data:
    x = x.strip('\n')
    if not start:
        if x == "":
            start = True
        continue
    words = x.split(' ')
    if words[0] != "move":
        print(f"Crap, got {words[0]} not move")
        break
    move_num = int(words[1])
    stack_from = int(words[3]) - 1
    stack_to = int(words[5]) - 1

    from_data = stacks[stack_from][-move_num:]
    # Part A is reverse order
    #from_data.reverse()

    stacks[stack_from] = stacks[stack_from][:-move_num]
    stacks[stack_to] += from_data

# %%
for x in stacks:
    print(' '.join(x))

top_box = [x[-1] for x in stacks]

print(top_box)
print(''.join(top_box))

# %%
