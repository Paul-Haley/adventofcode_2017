import sys
sheet = open(sys.argv[1])
checksum = 0
for line in sheet:
    sline = line.split()
    for i in sline:
        for j in sline:
            if i == j:
                continue
            nom = int(i)
            div = int(j)
            if nom/div == nom//div and nom//div != 0:
                checksum += nom//div

print(checksum)
sheet.close()
