import sys

def progress(firewall):
    for depth in firewall.keys():
        scanner = firewall[depth]
        if scanner[2] and scanner[0] == scanner[1] - 1: # at bottom
            firewall[depth] = (scanner[0] - 1, scanner[1], False)
        elif not scanner[2] and scanner[0] == 0: # at top
            firewall[depth] = (1, scanner[1], True)
        elif scanner[2]:
            firewall[depth] = (scanner[0] + 1, scanner[1], scanner[2])
        elif not scanner[2]:
            firewall[depth] = (scanner[0] - 1, scanner[1], scanner[2])

firewall = dict()
highest = 0
with open(sys.argv[1], "r") as f:
    for line in f:
        parts = line.split(": ")
        highest = int(parts[0])
        firewall[highest] = (0, int(parts[1]), True) #tuple of index, size and isDescending
        

total = 0
pico = 0 #aka depth
for pico in range(0, highest + 1):
    scanner = firewall.get(pico)
    #print(firewall) # good visual for debugging
    if scanner != None and scanner[0] == 0: #caught
        total += pico * scanner[1]
    progress(firewall)

print(total)

