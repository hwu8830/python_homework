# 根据标点符号对字符串进行分行
def split_by_punctuation(text):
    punctuation = [',', '.', ';', ':', '!', '?']  # 定义标点符号列表
    result = ''  # 初始化结果字符串
    for char in text:
        result += char  # 将当前字符添加到结果字符串中
        if char in punctuation:  # 如果当前字符是标点符号
            result += '\n'  # 在当前字符后添加换行符
    return result

input_text = input("请输入需要分行的字符串：")
result_text = split_by_punctuation(input_text)
print("分行后的结果：\n", result_text)
