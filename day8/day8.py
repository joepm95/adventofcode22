lines = []
with open('./input.txt') as file:
    lines = [line.rstrip() for line in file]

i = 0
matrix = []
for line in lines:
    matrix.append([int(c) for c in line])

# Check how many trees aren't visible
not_visible = 0
for i in range(1, len(lines)-1):
    for j in range(1, len(lines[0])-1):
        if max(list(map(int,matrix[i][0:j]))) >= int(matrix[i][j]) and max(list(map(int,matrix[i][j+1:]))) >= int(matrix[i][j]):
            check_up = False
            check_down = False
            for k in range(0, i):
                if matrix[k][j] >= matrix[i][j]:
                    check_up = True
                    break
            for k in range(i+1, len(lines)):
                if matrix[k][j] >= matrix[i][j]:
                    check_down = True
                    break
            if check_down and check_up:
                not_visible = not_visible + 1

# Calculate how many ARE visible
visible = 99*99 - not_visible

print(visible)

# Find highest viewing score
max_score = 0
for i in range(1, len(lines)-1):
    for j in range(1, len(lines[0])-1):
        up, down, left, right = 0,0,0,0
        more_up, more_down, more_left, more_right = True,True,True,True
        while more_up or more_down or more_left or more_right:
            if more_up:
                if i-1-up < 0:
                    more_up = False
                elif matrix[i-1-up][j] < matrix[i][j]:
                    up = up + 1
                else:
                    up = up + 1
                    more_up = False
            if more_down:
                if i+1+down > len(lines) - 1:
                    more_down = False
                elif matrix[i+1+down][j] < matrix[i][j]:
                    down = down + 1
                else:
                    down = down + 1
                    more_down = False
            if more_left:
                if j-1-left < 0:
                    more_left = False
                elif matrix[i][j-1-left] < matrix[i][j]:
                    left = left + 1
                else:
                    left = left + 1
                    more_left = False
            if more_right:
                if j+1+right > len(lines[0]) - 1:
                    more_right = False
                elif matrix[i][j+1+right] < matrix[i][j]:
                    right = right + 1
                else:
                    right = right + 1
                    more_right = False
        curr_score = up * down * left * right
        print("UP: " + str(up) + " Down: " + str(down) + " Left: " + str(left) + " Right: " + str(right))
        if curr_score > max_score:
            max_score = curr_score

print(max_score)



