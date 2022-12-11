# %%

class Logic:
    def __init__(self):
        self.grab_cycles = [20, 60, 100, 140, 180, 220]

        self.cycle_number = 0
        self.register_x = 1

        self.draw_sprite(0)
        self.screen = ""

    def draw_sprite(self, position):
        self.sprite_image = list(" " * 42)
        if position <= 0:
            for x in range(2 + position): # if pos in [-1, 0]
                self.sprite_image[x] = "#"
        # elif position >= 39:
        #     for x in range(40 - position):
        #         self.sprite_image[x] = "#"
        else:
            for x in range(3):
                self.sprite_image[x + position - 1] = "#"

    def run_cycle(self, cycles: int):
        for x in range(cycles):
            self.screen += self.sprite_image[self.cycle_number % 40]
            self.cycle_number += 1
            self.draw_result()

    def draw_result(self):
        if self.cycle_number > 0 and self.cycle_number % 40 == 0:
            print(self.screen)
            self.screen = ""

    def run_logic(self, data: str):
        grab_cycle_num = 0
        _20th_cycles = []
        for x in data:
            # I am on cycle: cycle_number
            if x == 'noop':
                self.run_cycle(1)
            elif x[:4] == 'addx':
                if (grab_cycle_num < len(self.grab_cycles)
                    and self.grab_cycles[grab_cycle_num] in [self.cycle_number, self.cycle_number + 1, self.cycle_number + 2]):
                    _20th_cycles.append(self.register_x)
                    grab_cycle_num += 1

                self.run_cycle(2)
                self.register_x += int(x.split(' ')[1])
                self.draw_sprite(self.register_x)

            if grab_cycle_num < len(self.grab_cycles) and self.cycle_number == self.grab_cycles[grab_cycle_num]:
                _20th_cycles.append(self.register_x)
                grab_cycle_num += 1

            # print(f"Cycle: {self.cycle_number} - {self.register_x}")
        return _20th_cycles

puzzle = Logic()

# %%
data = [x.strip('\n') for x in open('Puzzle10_input.txt', 'r').readlines()]
_20th_cycles = puzzle.run_logic(data)

zipped_cycles = [x for x in zip(puzzle.grab_cycles, _20th_cycles)]
print (f"We have grabbed cycles: {zipped_cycles}")

result = 0
for x in zipped_cycles:
    result += (x[0] * x[1])

print(f"Result - {result} - 15140")

print ("Text - BPJAZGAP")
