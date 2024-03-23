# 验证:任意一个大于9的整数减去它的各位数字之和所得的差,一定能被9整除.
num = int(input("请输入待验证数字"))

str_num = str(num)
sum_num = 0
print("拆分为",end="")
for i in str_num:
    print(f"{i},",end="")
    sum_num = sum_num + int(i)
print("")
if (num-sum_num)%9==0:
    print(f"待验证数字{num}的各位数字之和为{sum_num},求差为{num-sum_num},除以9等于{int((num-sum_num)/9)}")
    print("验证成功")
