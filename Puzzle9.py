# %%
data = [x.strip('\n').split(' ') for x in open('Puzzle9_input.txt', 'r').readlines()]

# %%

class RopeMatrix:
    def __init__(self):
        self.tail_pos_set = { '0 0' }
        self.head_pos = [0, 0]
        self.tail_pos = [0, 0]

    def move_tail(self):
        if self.head_pos == self.tail_pos:
            return
        x_delta = self.head_pos[0] - self.tail_pos[0]
        y_delta = self.head_pos[1] - self.tail_pos[1]
        if abs(x_delta) <= 1 and abs(y_delta) <= 1:
            self.draw_matrix("No Move")
            return

        if x_delta == 2 and -1 <= y_delta <= 1:
            # T...
            # TXH.
            # T...
            self.tail_pos = [self.head_pos[0] - 1, self.head_pos[1]]

        if x_delta == -2 and -1 <= y_delta <= 1:
            # ...T
            # .HXT
            # ...T
            self.tail_pos = [self.head_pos[0] + 1, self.head_pos[1]]

        if y_delta == 2 and -1 <= x_delta <= 1:
            # TTT
            # .X.
            # .H.
            # ...
            self.tail_pos = [self.head_pos[0], self.head_pos[1] - 1]

        if y_delta == -2 and -1 <= x_delta <= 1:
            # ...
            # .H.
            # .X.
            # TTT
            self.tail_pos = [self.head_pos[0], self.head_pos[1] + 1]

        self.tail_pos_set.add(f"{self.tail_pos[0]} {self.tail_pos[1]}")

        self.draw_matrix("Drag Tail")

    def draw_matrix(self, operation):
        print('-' * 3 + operation + "-" * 3)
        board = [['.','.','.'], ['.','H','.'], ['.','.','.']]
        delta_y = self.tail_pos[1] - self.head_pos[1]
        delta_x = self.tail_pos[0] - self.head_pos[0]
        board[delta_y + 1][delta_x + 1] = "T"
        for x in board:
            print(''.join(x))


game_board = RopeMatrix()

for x in data:
    direction = x[0]
    steps = int(x[1])

    match direction:
        case 'R':
            for x in range(steps):
                game_board.head_pos[0] += 1
                game_board.move_tail()
        case 'L':
            for x in range(steps):
                game_board.head_pos[0] -= 1
                game_board.move_tail()
        case 'U':
            for x in range(steps):
                game_board.head_pos[1] -= 1
                game_board.move_tail()
        case 'D':
            for x in range(steps):
                game_board.head_pos[1] += 1
                game_board.move_tail()
        case x:
            print(f" ====> {x}")
            break

print(f"tail positions: {len(game_board.tail_pos_set)} - (6243)")
