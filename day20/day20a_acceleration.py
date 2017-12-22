import sys
p = [None] * 1000
v = [None] * 1000
a = [None] * 1000
lowest = 0
man = lambda a: abs(a[0]) + abs(a[1]) + abs(a[2])
with open(sys.argv[1], 'r') as f:
    i = 0
    for line in f:
#        print(line.strip().replace('p=','').replace('v=','').replace('a=','').replace('<','').replace('>','').replace(' ',''))
        parts = line.strip().replace('p=','').replace('v=','').replace('a=','').replace('<','').replace('>','').replace(' ','').split(',')
        p[i] = (int(parts[0]), int(parts[1]),int(parts[2]))
        v[i] = (int(parts[3]), int(parts[4]),int(parts[5]))
        a[i] = (int(parts[6]), int(parts[7]),int(parts[8]))
        if man(a[i]) < man(a[lowest]):
            lowest = i
        i += 1
print(lowest)

