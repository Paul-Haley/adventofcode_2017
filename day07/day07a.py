import sys
file = open(sys.argv[1])
bottom = ""
seen = set()
above = set()
for line in file:
    parts = line.split()
    seen.add(parts[0])
    for i in parts[3:]:
        if (i.endswith(",")):
            above.add(i[0:-1])
        else:
            above.add(i[0:])
file.close()
print(seen.difference(above).pop())
