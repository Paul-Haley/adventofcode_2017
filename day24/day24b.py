def nextPiece(previous, parts):
    weights = list()
    lengths = list()
    for part in parts:
        w = part[0] + part[1]
        for i in range(2):
            if part[i] == previous:
                reduced = parts.copy()
                reduced.discard(part)
                pair = nextPiece(part[(i+1)%2], reduced)
                weights.append(w + pair[1])
                lengths.append(pair[0] + 1)
    if len(weights) == 0:
        return (len(parts), 0)
    #find longest and heaviest
    best = (0, 0)
    for i in range(len(lengths)):
        if lengths[i]>best[0] or (lengths[i] >= best[0] and weights[i] > best[1]):
            best = (lengths[i], weights[i])
    return best





import sys
coms = set()
with open(sys.argv[1], 'r') as f:
    for line in f:
        parts = line.split('/')
        coms.add((int(parts[0]),int(parts[1])))

#solving
print(nextPiece(0, coms))

