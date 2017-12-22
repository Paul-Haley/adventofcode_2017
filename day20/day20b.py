import sys
p = [None] * 1000
v = [None] * 1000
a = [None] * 1000
man = lambda a: abs(a[0]) + abs(a[1]) + abs(a[2])
update = lambda d1, d2: (d1[0]+d2[0], d1[1]+d2[1], d1[2]+d2[2]) 

with open(sys.argv[1], 'r') as f:
    i = 0
    for line in f:
        parts = line.strip().replace('p=','').replace('v=','').replace('a=','').replace('<','').replace('>','').replace(' ','').split(',')
        p[i] = (int(parts[0]), int(parts[1]),int(parts[2]))
        v[i] = (int(parts[3]), int(parts[4]),int(parts[5]))
        a[i] = (int(parts[6]), int(parts[7]),int(parts[8]))
        i += 1

i = 0
same = 0
collided = set()
for i in range(int(sys.argv[2])): # number of iterations to attempt
    locations = dict()
    lowest = 0
    for j in range(len(p)):
        if j in collided: # speed things up a little
            continue
        v[j] = update(v[j], a[j])
        p[j] = update(p[j], v[j])
        if locations.get(p[j]) != None: # collision
            collided.add(j)
            collided.add(locations.get(p[j]))
        else: # store location
            locations[p[j]] = j
print(len(p) - len(collided))

