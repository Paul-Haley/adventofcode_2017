import sys

maps = dict()
file = open(sys.argv[1], "r")
for line in file:
    parts = line.split()
    key = int(parts[0])
    maps[key] = set()
    for mate in parts[2:]:
        maps[key].add(int(mate.replace(",","")))
file.close()

allNodes = set(maps.keys())
remaining = allNodes
allSeen = set()
groups = 0
while(len(remaining) > 0):
    groups += 1
    origin = remaining.pop()
    seen = {origin}
    togo = maps[origin]
    while(len(togo) > 0):
        node = togo.pop()
        seen.add(node)
        togo = togo.union(maps[node]).difference(seen)
    allSeen = allSeen.union(seen)
    remaining = allNodes.difference(allSeen)
print(groups)
