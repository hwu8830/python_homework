import random as r
number = r.randint(0,100)
i=0
while True:
    i+=1
    my = float(input("请输入一个数"))
    if my == number:
        anser =str(input(f"正确，你猜了{i}次，是否继续？Y/N"))
        if anser == 'Y' or anser == 'y':
            number = r.randint(0,100)
        else:
            print("结束")
            break
    elif my < number:
        print("小了") 
    elif my > number:
        print("大了")