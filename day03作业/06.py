for i in range(0, 10):
    a = float(input("请输入第一个数a:"))
    b = float(input("请输入第二个数b:"))
    if b % a == 0 or (a + b) > 1000:
        print(a)
    else:
        print(b)
    i = input("是否继续?  回复1继续")
    if i == '1': 
        continue
    else:
        break




