# 求  a+aa+aaa+.......+aaaaaaaaa=?其中a为1至9之中的一个数，项数也要可以指定。
def sum_1(a,b):#输入数字和项数输出最后一位值
    sumA = 0
    valueA = 0  
    while b>0:
        valueA = 10**(b-1)*a
        sumA = valueA + sumA
        b -= 1
    return sumA
def sum_2(a,b):#输入数字和项数得出结果
    value = 0 
    while b>0:
        value += sum_1(a,b)
        b=b-1
    print("结果为",value) 
a = int(input("输入数字"))
b = int(input("输入项数"))
sum_2(a,b)




    
             
        