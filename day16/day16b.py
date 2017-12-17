import sys
programs = [chr(i) for i in range(ord('a'), ord('p') + 1)]
with open(sys.argv[1], 'r') as f:
    for line in f:
        dance = line.strip().split(',')
        break
for _ in range(1000000000):
    for move in dance:
        if move[0] == 's': # spin
            for i in range(len(programs) - int(move[1:])):
                programs.append(programs.pop(0))
        if move[0] == 'x': # exchange
            ex = move[1:].split('/')
            tmp = programs[int(ex[0])]
            programs[int(ex[0])] = programs[int(ex[1])]
            programs[int(ex[1])] = tmp
            continue
        if move[0] == 'p': # partner
            partners = move[1:].split('/')
            for i in range(len(programs)):
                if programs[i] == partners[0]:
                    x = i
                if programs[i] == partners[1]:
                    y = i
            programs[x] = partners[1]
            programs[y] = partners[0]
            continue
print(str(programs).replace(', ','').replace('\'','')[1:-1])
