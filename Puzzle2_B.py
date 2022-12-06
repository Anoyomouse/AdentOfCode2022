rps = {"A": "Rock", "B": "Paper", "C": "Scissors"}
rps2 = { "X": "Lose", "Y": "Draw", "Z": "Win" }

rps_win = { "A": "Paper", "B": "Scissors", "C": "Rock" }
rps_draw = { "A": "Rock", "B": "Paper", "C": "Scissors" }
rps_lose = { "A": "Scissors", "B": "Rock", "C": "Paper" }

rps_how = { "Win": rps_win, "Draw": rps_draw, "Lose": rps_lose }

value = { "Rock": 1, "Paper": 2, "Scissors": 3 }
round_points = { "Win": 6, "Draw": 3, "Lose": 0 }

data = open("Puzzle2_input.txt",'r')
points = 0
for x in data.readlines():
    x = x.strip(' \t\n')
    a,b = x.split(' ')
    # i need to: [Win, Draw, Lose]
    i = rps2[b]
    # i need to draw a:
    draw_a = rps_how[i][a]
    points += value[draw_a] + round_points[i]

print(f"Total: {points}")

