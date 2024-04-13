# 去掉字符串数组中每个字符串的空格
# def remove_spaces_from_strings(str_array):
#     result = []  # 初始化结果数组
#     for string in str_array:
#         # 去掉字符串两端的空格，并添加到结果数组中
#         result.append(string.strip())
#     return result

# # 测试
# input_array = ["  hello ", "  world  ", "  python  "]
# result_array = remove_spaces_from_strings(input_array)
# print("去掉空格后的数组:", result_array)

def remove_spaces_from_strings(str_array):
    result = []  # 初始化结果数组
    for string in str_array:
        resultValue = ''#清空临时字符串      
        for i in string:          
            if i != ' ':
                resultValue += i              
        result.append(resultValue)
    return result

# 测试
input_array = ["  hello ", "  world  ", "  python  "]
result_array = remove_spaces_from_strings(input_array)
print("去掉空格后的数组:", result_array)
