import sys
grid = []
height = width = 0
with open(sys.argv[1], 'r') as f:
    final = False
    i = 0
    for line in f:
        grid.append([0] * (len(line) - 1))
        final = True
        for j in range(len(line) - 1): #ignore \n
            if line[j] != ' ':
                final = False
            grid[i][j] = line[j]
        i += 1
        if final:
            height = len(grid) - 1
            width = len(line) - 1
            del(grid[i - 1])
            break
# need to find start
x = y = 0
for i in range(len(grid[0])):
    if grid[0][i] == '|':
        x = i

#following path now
seen = []
d = 2 # 0 for N, 1 is E, 2 is S, 3 is W
while x >= 0 and y >= 0 and x < width and y < height:
    c = grid[y][x]
    if c == '|' or c == '-':
        if d == 0:
            y -= 1
        if d == 1:
            x += 1
        if d == 2:
            y += 1
        if d == 3:
            x -= 1
    elif c == '+': # need to find new direction
        if d % 2 != 0 and y + 1 < height and grid[y + 1][x] != ' ':
            d = 2
            y += 1
        elif d % 2 != 0 and y - 1 >= 0 and grid[y - 1][x] != ' ':
            d = 0
            y -= 1
        elif d % 2 == 0 and x + 1 < width and grid[y][x + 1] != ' ':
            d = 1
            x += 1
        elif d % 2 == 0 and x - 1 >= 0 and grid[y][x - 1] != ' ':
            d = 3
            x -= 1
    else: # letter
        seen.append(c)
        grid[y][x] = '|' # letter collected, continue path

for i in seen:
    print(i, end='')
print('')

