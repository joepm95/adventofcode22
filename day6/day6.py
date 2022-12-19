lines = []
with open('./input.txt') as file:
    lines = [line for line in file]

four = False
i = 0
signal = lines[0]

while not four:
    set_four = set(signal[i:i+4])
    if len(set_four) == 4:
        four = True
        print(i+4)
    i = i + 1

fourteen = False
i = 0

while not fourteen:
    set_fourteen = set(signal[i:i+14])
    if len(set_fourteen) == 14:
        fourteen = True
        print(i+14)
    i = i + 1