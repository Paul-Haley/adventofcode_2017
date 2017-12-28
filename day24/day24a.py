def nextPiece(previous, parts):
    weights = list()
    for part in parts:
        w = part[0] + part[1]
        for i in range(2):
            if part[i] == previous:
                reduced = parts.copy()
                reduced.discard(part)
                weights.append(w + nextPiece(part[(i+1)%2], reduced))
    if len(weights) == 0:
        weights.append(0)
    return max(weights)



import sys
coms = set()
with open(sys.argv[1], 'r') as f:
    for line in f:
        parts = line.split('/')
        coms.add((int(parts[0]),int(parts[1])))

#solving
print(nextPiece(0, coms))

