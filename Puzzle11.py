# %%
from typing import List, Dict

class Monkey:
    def __init__(self, _6_lines : List[str]):
        self.name = int
        self.items = List[int]
        self.test_results = Dict[bool, int]
        self.activity = 0

        self.test_results = {}
        for x in _6_lines:
            x = x.strip('\r\n')
            if x.startswith("Monkey"):
                self.number = x.split(' ')[1].strip(':')
            if x.startswith('  Starting items:'):
                self.items = eval("[" + x.split(':')[1].strip(' ') + "]")
            if x.startswith('  Operation:'):
                self.operation = x.split(':')[1].strip(' ')
            if x.startswith('  Test:'):
                self.test = x.split(':')[1].strip(' ')
                divisor = self.test.split(' ')[-1]
                self.test_func = lambda x: x % divisor
            if x.startswith('    If true'):
                self.test_results[True] = int(x.split(':')[1].strip(' ').split(' ')[-1])
            if x.startswith('    If false'):
                self.test_results[False] = int(x.split(':')[1].strip(' ').split(' ')[-1])

    def recieve_item(self, item):
        self.items.append(item)

    def do_turn(self, monkeys: List["Monkey"]):
        new = 0
        for old in self.items:
            self.activity += 1
            exec(self.operation)
            print(f'Worry level is now: {new}')
            new = new // 3
            monkeys[self.test_results[self.test_func(new)]].recieve_item(old)

# %%
data = [x.strip('\n') for x in open('Puzzle11_input.txt', 'r').readlines()]

monkeys = []
start = 0
while True:
    monkeys.append(Monkey(data[start:start + 6]))
    start += 1
    if start >= len(data):
        break

for round in range(1):
    for x in monkeys:
        x.do_turn(monkeys)

# %%
