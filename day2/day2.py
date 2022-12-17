lines = []
with open('./input.txt') as file:
    lines = [line.rstrip() for line in file]

score = 0
for line in lines:
    strat = line.split()
    if strat[1] == 'X':
        score = score + 1
        if strat[0] == 'A':
            score = score + 3
        elif strat[0] == 'C':
            score = score + 6
    elif strat[1] == 'Y':
        score = score + 2
        if strat[0] == 'A':
            score = score + 6
        elif strat[0] == 'B':
            score = score + 3
    elif strat[1] == 'Z':
        score = score + 3
        if strat[0] == 'B':
            score = score + 6
        elif strat[0] == 'C':
            score = score + 3

print(score)

score2 = 0
for line in lines:
    strat = line.split()
    if strat[1] == 'X':
        if strat[0] == 'A':
            score2 = score2 + 3
        elif strat[0] == 'B':
            score2 = score2 + 1
        elif strat[0] == 'C':
            score2 = score2 + 2
    elif strat[1] == 'Y':
        score2 = score2 + 3
        if strat[0] == 'A':
            score2 = score2 + 1
        elif strat[0] == 'B':
            score2 = score2 + 2
        elif strat[0] == 'C':
            score2 = score2 + 3
    elif strat[1] == 'Z':
        score2 = score2 + 6
        if strat[0] == 'A':
            score2 = score2 + 2
        elif strat[0] == 'B':
            score2 = score2 + 3
        elif strat[0] == 'C':
            score2 = score2 + 1

print(score2)


