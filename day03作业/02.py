# 判断一个数是否是质数（素数）

i=int(input("请输入一个数"))

for j in range(4,i):

    if i==2 or i==3:
        print("这是一个质数")

    elif i%j==0 or i%2 == 0 or i%3==0:
        print("这不是一个质数")
        
       
    elif j == (i+1):
        print("这是一个质数")
    

 

    
       
       
