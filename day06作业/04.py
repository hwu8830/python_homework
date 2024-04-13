# 【选做】某个人进入如下一个棋盘中，要求从左上角开始走，
# 	最后从右下角出来（要求只能前进，不能后退），
# 	问题：共有多少种走法？
# 0 0 0 0 0 0 0 0

# 0 0 0 0 0 0 0 0

# 0 0 0 0 0 0 0 0

# 0 0 0 0 0 0 0 0

# 0 0 0 0 0 0 0 0

def aaa(i, j, y, x):
    
    # 递归结束条件：到达右下角的格子
    if i == y - 1 and j == x - 1:
        return 1
    
    # 向右移动一步的走法数目
    right_paths = aaa(i, j + 1, y, x) if j < x - 1 else 0
    # 向下移动一步的走法数目
    down_paths = aaa(i + 1, j, y, x) if i < y - 1 else 0
    
    # 返回向右和向下移动一步的走法数目之和
    return right_paths + down_paths

y = 5
x = 8
result = aaa(0, 0, y, x)
print("共有 {} 种走法。".format(result))


