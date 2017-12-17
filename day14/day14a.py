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
used = 0
for i in range(128):
    hash = knot("hxtvlmkl" + "-" + str(i))
    for b in hash:
        used += bin(b).count('1')
print(used)