# 用户登录注册案例
import getpass
global global_data
global_data = {}
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
                break
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


