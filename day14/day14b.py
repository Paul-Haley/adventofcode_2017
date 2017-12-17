import sys

def reverse(cur, ss, l, values):
    for i in range(l//2):
        tmp = values[(cur + i) % len(values)]
        values[(cur + i) % len(values)] = values[((cur + l) - (i + 1)) % len(values)]
        values[((cur + l) - (i + 1)) % len(values)] = tmp

"""16 byte long elements"""
def knot(key):
    lengths = [ord(i) for i in key.rstrip()]
    lengths.extend([17, 31, 73, 47, 23])
    values = [i for i in range(256)]

    cur = 0
    ss = 0
    for _ in range(64):
        for l in lengths:
           reverse(cur, ss, l, values)
           cur += l + ss
           cur %= len(values)
           ss += 1

    dh = [] # dense hash
    for i in range(16): # xor
        hash = 0
        for j in range(16):
            hash ^= values[i * 16 + j]
        dh.append(hash)
    return dh

# main script
seen = [None] * 128
disk = [None] * 128
for i in range(128):
    hash = knot("hxtvlmkl" + "-" + str(i))
    seen[i] = [0] * 128
    line = ""
    for b in hash:
        bits = bin(b)[2:]
        for _ in range(8 - len(bits)):
            bits = "0" + bits
        line += bits
    disk[i] = [int(i) for i in line]

# finding regions
regions = 0
for i in range(len(disk)):
    for j in range(len(disk[i])):
        if seen[i][j] == 1 or disk[i][j] == 0: #seen this element before or empty
            continue
        regions += 1 # new region found
        view = {(i,j)} # set of items to view
        while len(view) != 0: # going to check up down left right for unseen
            x, y = view.pop()
            if x - 1 >= 0 and seen[x - 1][y] == 0 and disk[x-1][y] != 0: # check left
                view.add((x-1, y))
                seen[x-1][y] = 1
            if x + 1 < len(disk[i]) and seen[x + 1][y] == 0 and disk[x+1][y] != 0: # check right
                view.add((x+1, y))
                seen[x+1][y] = 1
            if y - 1 >= 0 and seen[x][y - 1] == 0 and disk[x][y-1] != 0: # check up
                view.add((x, y-1))
                seen[x][y-1] = 1
            if y + 1 < len(disk) and seen[x][y + 1] == 0 and disk[x][y+1] != 0: # check down
                view.add((x, y+1))
                seen[x][y+1] = 1
print(regions)
