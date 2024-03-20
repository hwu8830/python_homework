j = 0
g = 0
for i in range(1360,9999):
    if (i%1000)>=300 and (i%1000)<400 and (i%100)>=60 and (i%100)<70 and (i%2 == 0)and (i%3==0):
        j += 1
        g = i
        if j == 1:
            print(i)

print(g)
             
