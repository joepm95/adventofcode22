lines = []
with open('./input.txt') as file:
    lines = [line for line in file]

# 3 characters for a crate ([x]) or 3 whitespaces for no crate
# 1 whitespace between each stack
def parse_crates(lines):
    stacks = [[],[],[],[],[],[],[],[],[]]
    for line in lines:
        pos = 0
        while pos < len(line):
            if not line[pos+1].isspace():
                stacks[int(pos/4)].append(line[int(pos+1)])
            pos = pos + 4
    return stacks

def parse_move_one(stacks, lines):
    for line in lines:
        digits = [int(s) for s in line.split() if s.isdigit()]
        stacks = move_items_one(stacks, digits[1], digits[2], digits[0])
    return stacks

def move_items_one(stacks, source, to, amount):
    i = 0
    while i < int(amount):
        mover = stacks[(int(source)-1)].pop(0)
        stacks[(int(to)-1)].insert(0, mover)
        i = i + 1
    return stacks

def parse_move_multi(stacks, lines):
    for line in lines:
        digits = [int(s) for s in line.split() if s.isdigit()]
        stacks = move_items_multi(stacks, digits[1], digits[2], digits[0])
    return stacks

def move_items_multi(stacks, source, to, amount):
    i = 0
    mover = []
    while i < int(amount):
        mover.append(stacks[(int(source)-1)].pop(0))
        i = i + 1
    # list concatenation -> moved elements end up at the start/top of the stack
    stacks[(int(to)-1)] = mover + stacks[(int(to)-1)]
    return stacks   

# First parse the stacks, then the moves
# Initialize stacks as lists
stacks = parse_crates(lines[0:8])

# Parse and execute the moves (one crate at a time)
moved_stacks = parse_move_one(stacks, lines[10:])

top_stack = [s[0] for s in stacks]

str_top = ''.join(top_stack)

print(str_top)

# Parse and execute moves (multiple at a time)
stacks_multi = parse_crates(lines[0:8])

moved_stacks = parse_move_multi(stacks_multi, lines[10:])

top_stack_multi = [s[0] for s in stacks_multi]

str_top_multi = ''.join(top_stack_multi)

print(str_top_multi)

