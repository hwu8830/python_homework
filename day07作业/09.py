# 接收用户输入的字符串，将其中的字符进行排序（升
# 序），并以逆序的顺序输出，“cabed”→"abcde"→“edcba”
def sort_and_reverse(input_string):
    # 将字符串转换为列表，并对列表进行排序
    sorted_string = ''.join(sorted(input_string))
    
    # 将排序后的字符串进行逆序输出
    reversed_string = sorted_string[::-1]
    
    return reversed_string

# 获取用户输入的字符串
input_string = input("请输入一个字符串：")

# 对字符串进行排序并逆序输出
result = sort_and_reverse(input_string)
print("排序后并逆序输出的字符串为：", result)
