import sys

x = 0
y = 0
with open(sys.argv[1]) as f:
    instruct = f.read().strip().split(",")
    for c in instruct:
        if c == 'n':
            y += 2
        elif c == 's':
            y -= 2
        elif c == 'ne':
            x += 1
            y += 1
        elif c == 'nw':
            x -= 1
            y += 1
        elif c == 'se':
            x += 1
            y -= 1
        elif c == 'sw':
            x -= 1
            y -= 1
x = abs(x)
y = abs(y)
d = abs(x + y)//2
print(d)


