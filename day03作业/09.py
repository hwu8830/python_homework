head =int(input("头的数量"))
foot= int(input("脚的数量"))
for chiken in range(1,head):
    for rabit in range(1,head):
        if(chiken + rabit == head)and(chiken*2+rabit*4==foot):
            print(f"鸡有{chiken}只，兔有{rabit}只")