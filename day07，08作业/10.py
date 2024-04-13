# 接收用户输入的一句英文，将其中的单词以反序输
#   出，“hello c java python”→“python java c hello”。
def reverse_words(input_sentence):
    # 使用split方法将句子按空格分割成单词列表
    words = input_sentence.split()
    
    # 将单词列表进行反转
    reversed_words = words[::-1]
    
    # 将反转后的单词列表转换为字符串
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

# 获取用户输入的英文句子
input_sentence = input("请输入一句英文：")

# 对单词进行反序输出
result = reverse_words(input_sentence)
print("反序输出的单词为：", result)
