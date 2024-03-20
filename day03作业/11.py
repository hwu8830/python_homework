import random
import json




data = {}
while True:
    print("****************************")
    print("  ☆ ☆ ☆ 猜拳小游戏 ☆ ☆ ☆")
    print("****************************")
    print("      1.开始游戏")
    print("      2.查看积分排名")
    print("      3.退出")
    print("****************************")
    choice = int(input("请输入选项："))
    if choice == 1:#开局选择
        i=0#回合数
        hp = 3#血量
        rank = 0#积分
        computer_choice_range = ['石头','剪刀','布']
        computer_choice = random.choice(computer_choice_range)
        name = str(input("请输入你的名字："))
        while True:#游戏主体
            
            if hp == 0:
                print("game over")
                print("")
                print("")
                print("")
                data[name] = rank
                break
            else:
                i+=1
                print("")
                print(f"第{i}回合")
                my_choice = str(input("你选择出："))
                if my_choice == computer_choice:
                    print("电脑出：",computer_choice)
                    print(f"平局,HP：{hp}，积分：{rank}")
                    computer_choice = random.choice(computer_choice_range)
                elif (my_choice == '石头' and computer_choice == '剪刀') or\
                    (my_choice == '剪刀' and computer_choice == '布')or\
                    (my_choice == '布' and computer_choice == '石头'):
                    rank += 1
                    print("电脑出：",computer_choice)
                    print(f"你赢了！HP:{hp}，积分：{rank}")
                    computer_choice = random.choice(computer_choice_range)
                else:
                    hp -= 1
                    print("电脑出：",computer_choice)
                    print(f"你输了，HP:{hp}，积分{rank}")
                    computer_choice = random.choice(computer_choice_range)
    elif choice == 2:
        print("")
        print("")
        print("$$$$$$$$$$$$$$$$$$$$")
        print("      积分榜")
        for user, score in data.items():
            print(f"用户: {user}: 积分: {score}")
        print("$$$$$$$$$$$$$$$$$$$$")
        print("")
        print("")
    else:
        break        


