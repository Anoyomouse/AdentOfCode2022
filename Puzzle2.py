
# Puzzle 1
from collections import defaultdict

# Define rules of RPS
# What wins
rps_win = { "Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock" }
# What draws
rps_draw = { "Rock": "Rock", "Paper": "Paper", "Scissors": "Scissors" }
# What loses
rps_lose = { "Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper" }

# Put them all into a single Dict
rps_how = { "Win": rps_win, "Draw": rps_draw, "Lose": rps_lose }

# Turn them around, make a dict of pairs (Hop-timization)
data_points = {}
for x in rps_how:
    for y in rps_how[x]:
        data_points[f"{y} {rps_how[x][y]}"] = x

# What are points even?
value = { "Rock": 1, "Paper": 2, "Scissors": 3 }
round_points = { "Win": 6, "Draw": 3, "Lose": 0 }

# Define the inputs, what means what?
rps = {"A": "Rock", "B": "Paper", "C": "Scissors"}
rps2_a = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}
rps2_b = { "X": "Lose", "Y": "Draw", "Z": "Win" }

# Process everything together
data = open("Puzzle2_input.txt",'r')
points_a = 0
points_b = 0
for x in data.readlines():
    x = x.strip(' \t\n')
    a,b = x.split(' ')
    points_a += round_points[data_points[f'{rps[a]} {rps2_a[b]}']] + value[rps2_a[b]]

    # i need to: [Win, Draw, Lose]
    i = rps2_b[b]
    # i need to draw a:
    draw_a = rps_how[i][rps[a]]
    points_b += value[draw_a] + round_points[i]

print(f"Total: {points_a} -- 9759")
print(f"Total: {points_b} -- 12429")

