import getpass
global global_data
global_data = {}
def login():
    while True:
        print("                 英雄联盟商城登录界面")
        print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
        print("                   1. 用户登录")
        print("                   2. 新用户注册")
        print("                   3. 退出系统")

        choice = int(input("请输入选项"))
        if choice== 1:      
            while True:
                k1 = False
                k2 = False
                userID=str(input("请输入用户名:"))
                userPW=str(getpass.getpass("请输入密码:"))
                
                for i,j in global_data.items():
                    if userID == i:
                        k1=True
                    if userID==i and userPW == j:
                        k2=True
                if k1 and k2:
                    print ("登录成功")
                    return 1
                elif k1 and not k2:
                    print("密码错误")
                elif not k1:
                    print("用户不存在")       
        elif choice==2:
            while True:
                while True:
                    k = True
                    userID1=str(input("请输入用户名:"))
                    for i,j in global_data.items():  
                        if i == userID1: 
                            print("该用户名已被注册请重新输入")
                            k = False
                            break
                    if k:
                        break 
                while True:   
                    userPW1=str(getpass.getpass("请输入密码:"))
                    userPW2=str(getpass.getpass("请再次输入密码:"))
                    if userPW1 != userPW2:
                        print("两次输入的密码不一致！")
                    elif userPW1==userPW2:
                        global_data[userID1]=userPW1
                        print("注册成功，按任意键返回首页。")
                        input("")
                        break

                break 
        elif choice == 4:   
            for i, j in global_data.items():        
                print(f"用户: {i}: 密码: {j}")
login()
print("                  英雄商城购买英雄")
print("英雄购买票据")
print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
print("       英雄名称：盲僧(史诗)")
print("       英雄属性：生命值428(+85)/能量值200(+0)/移动速度425/攻击力55.8(+3.2)")
print("                攻击速度0.651(+3.1%)/护甲值24(+1.25)/攻击距离125")
print("")
print("       英雄座右铭：一人之行可灭世，众人之勤可救世！")
print("       英雄价格：3000")
print("       活动折扣：9.5")
print("")
print("插播广告：当风云变色，当流离失所，世界不再是旧日模样")
print("你是否会为了自己的梦想战斗，直至力战身亡，直至彼岸他乡 ")
print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")


number = int(input("请输入数量："))
print(f'应付款{number*3000*0.95}')
pay = int(input("(温馨提示)请付款："))

print("                  英雄商城购买英雄")
print("英雄购买票据")
print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
print("       英雄名称：盲僧(史诗)")
print("       英雄价格：3000")
print("       活动折扣：9.5")
print("")
print(f'应付款{number*3000*0.95}')
print(f'实际付款:{pay}')
print(f'找零:{pay-(number*3000*0.95)}')
print("")
print("插入广告：当风云变色，当流离失所，世界不再是旧日模样")
print("你是否会为了自己的梦想战斗，直至力战身亡，直至彼岸他乡")
print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~")
back = str(input("(温馨提示)按任意键返回上一级菜单："))