sl = [-1] * 50000001 #initialisation
sl[0] = 0
index = 0
step = 328
for i in range(1,50000001):
    index = (index + step)%i
    sl[index + 1] = i
    index += 1
    
    
for i in range(len(sl)):
    if sl[i] == 0:
        print(sl[i+1])
