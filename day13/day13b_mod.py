import sys

firewall = dict()
highest = 0
with open(sys.argv[1], "r") as f:
    for line in f:
        parts = line.split(": ")
        highest = int(parts[0])
        firewall[highest] = int(parts[1])
        
offset = 0
while True:
    pico = 0 #aka depth
    for pico in range(0, highest + 2):
        if pico > highest: # reached end
            print(offset)
            exit()
        i = offset + pico
        l = firewall.get(pico)
        if l != None and i % (2 * (l - 1)) == 0: #caught
            break
    offset += 1
print(offset)

