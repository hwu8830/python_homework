# 将list中的重复数据去重，至少使用两种方案

# 1

a=[1,3,5,7,9,11,13,15,16,18,19,3,5,7,9]
j = []
for i in a:
	if i not in j:
		j.append(i)
print(j)
# 2

k = list(set(a))
print(k)