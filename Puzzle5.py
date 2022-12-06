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
        if val != " " and val not in nums:
            stacks[y].append(val)

start_stacks = [x[::-1] for x in stacks]

del stacks
# %%
stacks_a = [x for x in start_stacks]
stacks_b = [x for x in start_stacks]
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

    from_data = stacks_a[stack_from][-move_num:]
    from_data.reverse()
    stacks_a[stack_from] = stacks_a[stack_from][:-move_num]
    stacks_a[stack_to] = stacks_a[stack_to] + from_data

    from_data = stacks_b[stack_from][-move_num:]
    stacks_b[stack_from] = stacks_b[stack_from][:-move_num]
    stacks_b[stack_to] = stacks_b[stack_to] + from_data

# %%
print(" === A ===")
for x in stacks_a:
    print(' '.join(x))

top_box_a = [x[-1] for x in stacks_a]

print(top_box_a)
print(''.join(top_box_a) + " - TDCHVHJTG")

print(" === B ===")
for x in stacks_b:
    print(' '.join(x))

top_box_b = [x[-1] for x in stacks_b]

print(top_box_b)
print(''.join(top_box_b) + " - NGCMPJLHV")

# %%
