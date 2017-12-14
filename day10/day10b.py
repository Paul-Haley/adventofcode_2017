import sys

def reverse(cur, ss, l, values):
    for i in range(l//2):
        tmp = values[(cur + i) % len(values)]
        values[(cur + i) % len(values)] = values[((cur + l) - (i + 1)) % len(values)]
        values[((cur + l) - (i + 1)) % len(values)] = tmp

# start script
lengths = [ord(i) for i in open(sys.argv[1], 'r').read().rstrip()]
lengths.extend([17, 31, 73, 47, 23])
values = [i for i in range(256)]

cur = 0
ss = 0
for _ in range(64):
    for l in lengths:
       reverse(cur, ss, l, values)
       cur += l + ss
       cur %= 256
       ss += 1

dh = [] # dense hash
for i in range(16): # xor
    hash = 0
    for j in range(16):
        hash ^= values[i * 16 + j]
    dh.append(hash)

for i in range(16):
     if len(hex(dh[i])[2:]) == 2:
         print(hex(dh[i])[2:], end='')
     else:
         print('0' + hex(dh[i])[2:], end='')
print('')

