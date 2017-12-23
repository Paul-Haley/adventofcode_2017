import sys
MAX = 1000
grid = [None] * MAX # grid sufficiently large enough based off number of bursts
for i in range(len(grid)):
    grid[i] = [False] * MAX # everything not infected originally
with open(sys.argv[1], 'r') as f:
    size = sum(1 for _ in f)
    f.seek(0)
    j = MAX//2 - 12
    for line in f:
        i = MAX//2 - 12
        for c in line:
            grid[i][j] = c == '#'
            i += 1
        j += 1
x = y = MAX//2 # centre
d = 0 #0 is North, going cw
infects = 0
for i in range(10000): #bursts
    d = (d + (1 if grid[x][y] else -1)) % 4 # change direction if infected
    if not grid[x][y]: # not infected
        infects += 1
        grid[x][y] = True
    else:
        grid[x][y] = False
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
