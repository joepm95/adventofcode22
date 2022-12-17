lines = []
with open('./input.txt') as file:
    lines = [line.rstrip() for line in file]

max_elf = [0, 0, 0]
curr_elf = 0
for line in lines:
    if line:
        curr_elf = curr_elf + int(line)
    else:
        if curr_elf > max_elf[0]:
            max_elf[2] = max_elf[1]
            max_elf[1] = max_elf[0]
            max_elf[0] = curr_elf
        elif curr_elf > max_elf[1]:
            max_elf[2] = max_elf[1]
            max_elf[1] = curr_elf
        elif curr_elf > max_elf[2]:
            max_elf[2] = curr_elf
        
        curr_elf = 0

print(sum(max_elf))


        