# 打印课堂上的图案
# *
# **
# ***
# ****
# *****
# ******
# *******

i = int(input("请输入行数"))
for j in range(1,i+1):
    print("*"*j,end="")
    print("")