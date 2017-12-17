sl = [0]
index = 0
step = 328
for i in range(1,2018):
    index = (index + step)%len(sl)
    sl.insert(index + 1, i)
    index += 1
    
    
for i in range(len(sl)):
    if sl[i] == 2017:
        print(sl[i+1])
