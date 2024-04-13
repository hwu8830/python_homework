#给定一个正整数N,找出1到N（含）之间所有质数的总和
# def sum_02(max):
#     j=0
#     i=1
#     sum = 0
#     for i in range(i,max+1):
#         k=False
#         for j in range(2,i):
#             if i==2 or i==3:
#                k=True
#             elif i%j==0 or i%2 == 0 or i%3==0:
#                 break
#             elif j == (i-1):
#                 k=True
#         if k:
#             sum+=i
#     return sum
# max_num =int(input("输入最大值"))
# print("结果为",sum_02(max_num))

def sum_02(max_val):
    total = 0
    for i in range(2, max_val + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            total += i
    return total

max_num = int(input("输入最大值: "))
print("结果为", sum_02(max_num))

