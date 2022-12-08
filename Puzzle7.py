# %%
data = open('Puzzle7_input.txt', 'r').readlines()

class Item:
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.dirs = []
        self.known_size = -1

    def get_size(self):
        if self.known_size >= 0:
            return self.known_size
        sizes = [x.get_size() for x in self.dirs]
        size = 0
        for x in sizes:
            size += x
        for x in self.files:
            size += self.files[x]
        self.known_size = size
        return size

root = Item("/")
dir_dict = {"/" : root}
dir_stack = []
current_dir = ""
state = 0
for x in data:
    x = x.strip(' \t\r\n')
    if x[0] == '$':
        state = 0
        # Command
        print(f"Got Command: {x}")
        a = x.split(' ')
        if a[1] == 'cd':
            print(f"Change directory: {a[2]}")
            if a[2] == '..':
                print(f"Go Back: {a[2]}")
                dir_stack.pop()
            else:
                print(f"Go into: {a[2]}")
                dir_stack.append(a[2])
            current_dir = '/'.join(dir_stack)
            print(f"We are in: {current_dir}")
        elif a[1] == 'ls':
            state = 1
        else:
            print(f"Unknown command: {a[0]}")
        continue
    if state != 1:
        print("We wern't followed by an 'ls'?")
    a = x.split(' ')
    if a[0] == "dir":
        new_dir = Item(a[1])
        print(f"Currently in: {current_dir}")
        dir_dict[current_dir].dirs.append(new_dir)
        new_dir_name = '/'.join(dir_stack + [a[1]])
        print ("New Directory: " + new_dir_name)
        dir_dict[new_dir_name] = new_dir
    else:
        dir_dict[current_dir].files[a[1]] = int(a[0])


# %%

l = [dir_dict[x].get_size() for x in dir_dict if dir_dict[x].get_size() <= 100000]

size = 0
for x in l:
    size += x

print(f"Total size of directories smaller than 100000: {size} - (1084134)")


# %%
total_size = 70000000
used_size = total_size - root.get_size()

needed_space = 30000000
space_to_free = needed_space - used_size

l = [dir_dict[x].get_size() for x in dir_dict if dir_dict[x].get_size() >= space_to_free]

l.sort() # key=lambda x,y: x < y)

print(f"Smallest directory to free up: {space_to_free} is {l[0]} - (6183184)")

# %%
