import string
import time


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
match_score = 0

for line in lines:
    half_len = int(len(line)/2)
    half1 = line[:half_len]
    half2 = line[half_len:]
    for x in half1:
        for y in half2:
            if x == y:
                match = x
    match_score = match_score + scores[match]

print(match_score)

start_time = time.time()
# Find the badge type for each group
badge_score = 0
i = 0
while i < len(lines):
    line1 = lines[i]
    line2 = lines[i + 1]
    line3 = lines[i + 2]
    for x in line1:
        for y in line2:
            if x == y:
                for z in line3:
                    if y == z:
                        badge = z
    badge_score = badge_score + scores[badge]
    i = i + 3

print("My program took", time.time() - start_time, "to run")
print(badge_score)
    