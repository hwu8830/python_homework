i = float(input("请输入身高(m)"))
j = int(input("请输入体重(kg)"))
bmi =  j/(i*i)
if bmi< 18.5:
    print("过轻")
elif bmi >= 18.5 and bmi < 24:
    print("正常")
elif bmi >=24 and bmi <27:
    print("过重")
elif bmi >=27 and bmi < 30:
    print("轻度肥胖")
elif bmi >=30 and bmi < 35:
    print("中度肥胖")
elif bmi >= 35:
    print("重度肥胖")