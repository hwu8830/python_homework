# 打印输出标准水仙花数，输出这些水仙花数
nums = []
for num in range(100, 1000):
    num_str = str(num)
    sum_num = sum(int(i) ** 3 for i in num_str)
    if sum_num == num:
        nums.append(num)
print(nums)