# 一个五位数,若在它的后面写上一个7,得到一个六位数A,若在它前面写上一个7,得到一个六位数B,B是A的五倍,求此五位数.

for num in range(10000, 100000):
    A = num * 10 + 7
    B = 7 * 100000 + num
    if B == 5 * A:
        print("满足条件的五位数为:", num)
        break


