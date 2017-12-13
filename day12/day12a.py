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

seen = {0}
togo = maps[0]
while(len(togo) > 0):
    node = togo.pop()
    seen.add(node)
    togo = togo.union(maps[node]).difference(seen)
print(len(seen))
