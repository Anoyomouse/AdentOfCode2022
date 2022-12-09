# %%
data = [x.strip('\n').split(' ') for x in open('Puzzle9_input.txt', 'r').readlines()]

# %%

class RopeMatrix:
    def __init__(self, segments):
        self.segments = segments
        self.tail_pos_set = { '0 0' }
        self.head_pos = [0, 0]
        self.tail_pos = []
        for x in range(self.segments):
            self.tail_pos.append([0, 0])

    def cascade(self):
        for x in range(self.segments - 1):
            self.move_tail(self.tail_pos[x], x + 1)

    def move_rope(self, direction, steps):
        for x in range(steps):
            if direction == 'R':
                self.head_pos[0] += 1
            elif direction == 'L':
                self.head_pos[0] -= 1
            elif direction == 'U':
                self.head_pos[1] -= 1
            elif direction == 'D':
                self.head_pos[1] += 1

            self.move_tail(self.head_pos)
            self.cascade()
            self.draw_matrix()
        
            self.tail_pos_set.add(f"{self.tail_pos[self.segments - 1][0]} {self.tail_pos[self.segments - 1][1]}")

    def move_tail(self, top_ref, ref = 0):
        if top_ref == self.tail_pos[ref]:
            return
        x_delta = top_ref[0] - self.tail_pos[ref][0]
        y_delta = top_ref[1] - self.tail_pos[ref][1]
        if abs(x_delta) > 1 or abs(y_delta) > 1:

            if -1 <= x_delta <= 1:
                self.tail_pos[ref][0] = top_ref[0]

            if -1 <= y_delta <= 1:
                self.tail_pos[ref][1] = top_ref[1]

            if x_delta == 2:
                self.tail_pos[ref][0] = top_ref[0] - 1
            elif x_delta == -2:
                self.tail_pos[ref][0] = top_ref[0] + 1

            if y_delta == 2:
                self.tail_pos[ref][1] = top_ref[1] - 1
            elif y_delta == -2:
                self.tail_pos[ref][1] = top_ref[1] + 1

            if x_delta > 2 or x_delta < -2:
                print(f'Too much movement! X: {x_delta}')
            if y_delta > 2 or y_delta < -2:
                print(f'Too much movement! Y: {y_delta}')

    def draw_matrix(self):
        print('-' * 3 + "  " + "-" * 3)
        print(f"{self.head_pos} {self.tail_pos}")

        max_len_x = max(self.head_pos[0], max([x[0] for x in self.tail_pos]))
        max_len_y = max(self.head_pos[1], max([x[1] for x in self.tail_pos]))

        min_len_x = min(self.head_pos[0], min([x[0] for x in self.tail_pos]))
        min_len_y = min(self.head_pos[1], min([x[1] for x in self.tail_pos]))

        matrix = []
        for y in range(min_len_y, max_len_y + 1):
            line = list("." * (max_len_x - min_len_x + 1))
            for p in range(len(self.tail_pos) - 1, 0 - 1, -1):
                tp = self.tail_pos[p]
                if y == tp[1]:
                    line[tp[0] - min_len_x] = str(p + 1)
            if self.head_pos[1] == y:
                line[self.head_pos[0] - min_len_x] = "H"
            matrix.append(line)

        for y in matrix:
            print(''.join(y))


# For solution A, RopeMatrix(1)
# For solution B, RopeMatrix(9)
game_board = RopeMatrix(9)

for x in data:
    direction = x[0]
    steps = int(x[1])

    game_board.move_rope(direction, steps)

# When doing 1 tail, we get 6243
# print(f"tail positions: {len(game_board.tail_pos_set)} - (6243)")
print(f"tail positions: {len(game_board.tail_pos_set)} - (2630)")
