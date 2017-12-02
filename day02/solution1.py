import sys
sheet = open(sys.argv[1])
checksum = 0
for line in sheet:
    min = sys.maxsize
    max = 0
    for i in line.split():
        current = int(i)
        if current > max:
            max = current
        if current < min:
            min = current
    checksum += (max - min)
print(checksum)
sheet.close()
