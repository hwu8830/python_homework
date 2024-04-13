#求一个十进制的数值的二进制的0、1的个数
def get_cal(number):
    zero = 0
    one = 0
    while number>0:
        i = number%2 #余数
        j = number//2 #商
        if i == 0:
            zero +=1
        elif i==1:
            one +=1
        elif j == 1:
            one += 1
        number = j   
    return zero,one
number = int(input("请输入一个十进制数字"))
zero,one = get_cal(number)
print("0的个数为",zero)
print("1的个数为",one)


    





