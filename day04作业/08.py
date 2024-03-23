##给定一个列表，求最大值（不能使用系统api），求最小值，求平均值、求和
list = [1,3,5,7,2,9,5,2,3,3,7]
print("列表",list)
num_max = list[0]
num_min = list[0]
num_and = 0
for i in range(1,len(list)):
	if num_max < list[i]:
		num_max = list[i]
	elif num_min > list[i]:
		num_min = list[i]
	else:
		pass
print("最大值:",num_max)
print("最小值:",num_min)
for i in list:
	num_and += i
print("和:",num_and)
num_average = num_and/len(list)
print("平均值:",num_average)