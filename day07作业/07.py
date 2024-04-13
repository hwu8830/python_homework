# 上题中两位同学输入 lol和 LOL代表同一游戏，怎么办?
def compare_games(game1, game2):
    game1_lower = game1.lower()  # 将游戏名称转换为小写形式
    game2_lower = game2.lower()  # 将游戏名称转换为小写形式

    if game1_lower == game2_lower:
        print("你们俩喜欢相同的游戏：", game1)
    else:
        print("你们俩喜欢不相同的游戏。")

# 获取学员输入的游戏名称
game1 = input("请输入第一个学员最喜欢的游戏名称：")
game2 = input("请输入第二个学员最喜欢的游戏名称：")

# 比较游戏名称并输出结果
compare_games(game1, game2)
