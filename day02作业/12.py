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