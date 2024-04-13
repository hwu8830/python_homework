# 给定一个非负整数数组A，将该数组中的所有偶数都放在奇数元素之前
def select_ls(ls= []):
    n = len(ls)
    for i in range(n):
            for j in range(n-i-1):
                if ls[j] % 2 != 0 and ls[j+1] % 2 == 0: 
                    ls[j+1], ls[j] = ls[j], ls[j+1] 
    return ls
ls1 = eval(input("输入列表"))
print("结果为",select_ls(ls1))