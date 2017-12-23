import sys
MAX = 1000
grid = [None] * MAX # grid sufficiently large enough based off number of bursts
for i in range(len(grid)):
    grid[i] = [0] * MAX # everything not infected originally
with open(sys.argv[1], 'r') as f:
    size = sum(1 for _ in f)
    f.seek(0)
    j = MAX//2 - 12
    for line in f:
        i = MAX//2 - 12
        for c in line:
            grid[i][j] = 2 if c == '#' else 0
            i += 1
        j += 1
x = y = MAX//2 # centre
d = 0 #0 is North, going cw
infects = 0
for i in range(10000000): #bursts
    #direction changes
    if grid[x][y] == 0:
        d = (d-1) % 4
    elif grid[x][y] == 2:
        d = (d+1) % 4
    elif grid[x][y] == 3:
        d = (d+2) % 4
        
    grid[x][y] = (grid[x][y] + 1) % 4
    if grid[x][y] == 2:
        infects += 1

    #moving
    if d==0:
        y-=1
    elif d==1:
        x+=1
    elif d==2:
        y+=1
    else:
        x-=1
print(infects)
