# 让用户输入一个日期格式如“2008/08/08”，将 输入的日
# 	期格式转换为“2008年-8月-8日”。
def format_date(input_date):
    # 使用split方法将日期字符串按"/"分割成年、月、日三部分
    year, month, day = input_date.split('/')
    
    # 将年、月、日转换为整数
    year = int(year)
    month = int(month)
    day = int(day)
    
    # 格式化日期字符串
    formatted_date = "{}年-{}月-{}日".format(year, month, day)
    #formatted_date = (f.'{year}年-{month}月-{day}日')
    
    return formatted_date

# 获取用户输入的日期
input_date = input("请输入一个日期（格式如“2008/08/08”）：")

# 转换日期格式并输出结果
formatted_date = format_date(input_date)
print("转换后的日期格式为：", formatted_date)
