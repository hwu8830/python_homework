#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

i = int(input("请输入行数"))
for j in range(1,i+1):
    print(" "*(i-j),"*"*(2*j-1),end="")
    print("")

for j in range(i-1,0,-1):
    print(" "*(i-j),"*"*(2*j-1),end="")
    print("")