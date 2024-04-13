# 合并两个有序数组，合并后还是有序列表
def select_ls(ls= []):
    n = len(ls)
    for i in range(n):
        for j in range(n-i-1):
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1] = ls[j+1],ls[j]
    return ls
ls1 = eval(input("输入列表1"))
ls2 = eval(input("输入列表2"))

ls1.extend(ls2)
print("结果为",select_ls(ls1))