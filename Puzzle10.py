# %%
data = [x.strip('\n') for x in open('Puzzle10_input.txt', 'r').readlines()]

# %%

grab_cycles = [20, 60, 100, 140, 180, 220]
grab_cycle_num = 0

cycle_number = 0
register_x = 1
_20th_cycles = []
for x in data:
    if x == 'noop':
        cycle_number += 1
    elif x[:4] == 'addx':
        val = int(x.split(' ')[1])

        if (grab_cycle_num < len(grab_cycles)
           and grab_cycles[grab_cycle_num] in [cycle_number, cycle_number + 1, cycle_number + 2]):
            _20th_cycles.append(register_x)
            grab_cycle_num += 1

        cycle_number += 2
        register_x += val

    if grab_cycle_num < len(grab_cycles) and cycle_number == grab_cycles[grab_cycle_num]:
        _20th_cycles.append(register_x)
        grab_cycle_num += 1

    print(f"Cycle: {cycle_number} - {register_x}")


zipped_cycles = [x for x in zip(grab_cycles, _20th_cycles)]
print (f"We have grabbed {grab_cycle_num} cycles: {zipped_cycles}")

result = 0
for x in zipped_cycles:
    result += (x[0] * x[1])

print(f"Result - {result} - 15140")
