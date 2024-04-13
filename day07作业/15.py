# 判断一个字符是否是回文字符串
#    	"1234567654321"
#    	"上海自来水来自海上"

def is_palindrome(string):
    # 将字符串与其逆序字符串进行比较
    return string == string[::-1]

# 测试字符串是否是回文字符串
string1 = "1234567654321"
string2 = "上海自来水来自海上"

if is_palindrome(string1):
    print(string1, "是回文字符串")
else:
    print(string1, "不是回文字符串")

if is_palindrome(string2):
    print(string2, "是回文字符串")
else:
    print(string2, "不是回文字符串")
