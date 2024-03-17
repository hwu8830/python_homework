#    *
#   ***
#  * * *
# *******
#  * * *
#   ***
#    *

i = int(input("请输入行数"))
for j in range(1,i):
    print(" "*(i-j),end="")#
    for n in range(0,2*j-1):
        if n == 0 or n == (2*j-2) or n == j-1:
           print("*",end="")
        else:
            print(" ",end="")
            
    print("")
# 下半部分
for j in range(i,0,-1):# 
    print(" "*(i-j),end="")
    for n in range(0,2*j-1):
        if n == 0 or n == (2*j-2) or n == j-1 or (j == i):
           print("*",end="")
        else:
            print(" ",end="")
    print("")
          