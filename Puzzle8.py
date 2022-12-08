# %%
data = [[int(y) for y in x.strip('\n')] for x in open('Puzzle8_input.txt', 'r').readlines()]

# %%

def solution_a():
    data_trees = []

    all_x = list("O" * len(data[0]))
    data_trees.append(all_x)
    edges_x = list("O" + (" " * (len(all_x) - 2)) + "O")
    for i in range(len(all_x) - 2):
        data_trees.append(edges_x.copy())
    data_trees.append(all_x.copy())

    for y in range(1, len(data) - 1):
        min_height = data[y][0]
        # go from left to right finding the tallest tree
        # Skip first tree, that will always be tallest
        data_trees[y][0] = str(min_height)
        for x in range(1, len(data[y]) - 1):
            if data[y][x] > min_height:
                data_trees[y][x] = str(data[y][x])
                min_height = data[y][x]
                if min_height == 9:
                    break

        min_height = data[y][-1]
        data_trees[y][-1] = str(min_height)
        for x in range(len(data[y]) - 1, 1 + 1, -1):
            if data[y][x] > min_height:
                data_trees[y][x] = str(data[y][x])
                min_height = data[y][x]
                if min_height == 9:
                    break


    for x in range(1, len(data[0]) - 1):
        min_height = data[0][x]
        # go from left to right finding the tallest tree
        # Skip first tree, that will always be tallest
        data_trees[0][x] = str(min_height)
        for y in range(1, len(data) - 1):
            if data[y][x] > min_height:
                data_trees[y][x] = str(data[y][x])
                min_height = data[y][x]
                if min_height == 9:
                    break

        min_height = data[-1][x]
        data_trees[-1][x] = str(min_height)
        for y in range(len(data) - 1, 1 + 1, -1):
            if data[y][x] > min_height:
                data_trees[y][x] = str(data[y][x])
                min_height = data[y][x]
                if min_height == 9:
                    break

    for x in data_trees:
        print(''.join(x))

    all_data = ''.join([''.join(x) for x in data_trees])
    all_data = all_data.replace(' ', '')

    print(f"Visible trees: {len(all_data)} - (1789)")

# solution_a()

# %%

data_trees = []

all_x = list([0] * len(data[0]))
data_trees.append(all_x)
edges_x = list([0] + ([-1] * (len(all_x) - 2)) + [0])
for i in range(len(all_x) - 2):
    data_trees.append(edges_x.copy())
data_trees.append(all_x.copy())

# %%

for y in range(1, len(data) - 1):
    data_trees[y][0] = 0
    for x in range(1, len(data[0]) - 1):
        my_height = data[y][x]
        rldu = [-1, -1, -1, -1]
        for i in range(len(data[y]) - x - 1):
            # print(f"Looking at x + {(i + 1)} from {x},{y}, it's {data[y][x + 1 + i]} high (vs {my_height})")
            if data[y][x + (i + 1)] >= my_height:
                rldu[0] = i + 1
                break
        else:
            rldu[0] = len(data[y]) - x - 1

        for i in range(x):
            # print(f"Looking at x - {i + 1} from {x},{y}, it's {data[y][x - (i + 1)]} high (vs {my_height})")
            if data[y][x - (i + 1)] >= my_height:
                rldu[1] = i + 1
                break
        else:
            rldu[1] = x

        for i in range(len(data) - y - 1):
            # print(f"Looking at y + {(i + 1)} from {x},{y}, it's {data[y + (i + 1)][x]} high (vs {my_height})")
            if data[y + (i + 1)][x] >= my_height:
                rldu[2] = i + 1
                break
        else:
            rldu[2] = len(data) - y - 1

        for i in range(y):
            # print(f"Looking at y - {(i + 1)} from {x},{y}, it's {data[y - (i + 1)][x]} high (vs {my_height})")
            if data[y - (i + 1)][x] >= my_height:
                rldu[3] = i + 1
                break
        else:
            rldu[3] = y

        data_trees[y][x] = rldu[0] * rldu[1] * rldu[2] * rldu[3]

# %%

all_trees = []
for x in data_trees:
    all_trees.extend(x)

all_trees.sort(reverse=True)

print(f"Max Beauty: {all_trees[0]} - (314820)")
# %%