import string

lines = []
with open('./input.txt') as file:
    lines = [line.rstrip() for line in file]

# Create scoring table for letters
letters = list(string.ascii_letters)
prio = []
for i in range(52):
    prio.append(i+1)

scores = {letters[i]:prio[i] for i in range(len(letters))}

# Find matching symbol between two compartments
total_score = 0

for line in lines:
    half_len = int(len(line)/2)
    half1 = line[:half_len]
    half2 = line[half_len:]
    match = 0
    for x in half1:
        for y in half2:
            if x == y:
                match = x
    if not match == 0:
        total_score = total_score + scores[match]

print(total_score)