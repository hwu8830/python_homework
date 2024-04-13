def hanoi(n, A, B, C):
    if n == 1:
        print("Move disk {} from {} to {}".format(n, A, C))
    else:
        hanoi(n-1, A, C, B)  # 将上部圆盘从A针移动到B针（借助C针）
        print("Move disk {} from {} to {}".format(n, A, C))  # 将下部圆盘从A针直接移动到C针
        hanoi(n-1, B, A, C)  # 将上部圆盘从B针移动到C针（借助A针）

# 测试
n = 3  # 圆盘的数量
A, B, C = 'A', 'B', 'C'  # 三根针的标识
hanoi(n, A, B, C)
