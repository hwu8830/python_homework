# 让用户输入一句话,找出所有"呵"的位置。
def findHE(str):
    str_pos = []
    num = 0
    for i in str:
        num += 1
        if i == "呵":
            str_pos.append(num)
    return str_pos

str= input("请输入句话")
print(f"这句话的第{findHE(str)}个字符都是呵")