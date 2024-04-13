def sum_01(max):#求1到max之间不能被3整除的数之和
    i=1
    j=0
    while i <= max:
        if i%3 != 0:
           j=j+i
        i += 1
    return j

maxValue = int(input("请输入最大范围"))
print("结果为",sum_01(maxValue))  
