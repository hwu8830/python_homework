i = int(input())
if i%2 == 0:
    print("该数是偶数")
    for j in range(1,i+1):
        if j%3==0:
            print(j)
else:
    print("该数是奇数")
    for k in range(1,i):
        if k%5==0:
            print(k)