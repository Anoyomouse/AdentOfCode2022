rps = {"A": "Rock", "B": "Paper", "C": "Scissors"}
rps2 = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}

win = 6
draw = 3
loss = 0

data_points = {
    "A X": 3 + 1, "A Y": 6 + 2, "A Z": 0 + 3,
    "B X": 0 + 1, "B Y": 3 + 2, "B Z": 6 + 3,
    "C X": 6 + 1, "C Y": 0 + 2, "C Z": 3 + 3
}

data = open("Puzzle2_input.txt",'r')
points = 0
for x in data.readlines():
    x = x.strip(' \t\n')
    points += data_points[x]

print(f"Total: {points}")

