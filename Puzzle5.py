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

    stacks_a[stack_to] = stacks_a[stack_to] + [x for x in reversed(stacks_a[stack_from][-move_num:])]
    # If you use the following line instead of the previous one it messes up BOTH of the outputs ...
    # stacks_a[stack_to].extend(reversed(stacks_a[stack_from][-move_num:]))
    stacks_a[stack_from] = stacks_a[stack_from][:-move_num]

    stacks_b[stack_to].extend(stacks_b[stack_from][-move_num:])
    stacks_b[stack_from] = stacks_b[stack_from][:-move_num]

# %%

def print_results(stacks, answer):
    for x in range(len(stacks)):
        print(f'{x + 1}) ' + ' '.join(stacks[x]))

    top_box = [x[-1] for x in stacks]
    print(''.join(top_box) + f" - {answer}")

print(" === A ===")
print_results(stacks_a, "TDCHVHJTG")

print(" === B ===")
print_results(stacks_b, "NGCMPJLHV")

# %%
