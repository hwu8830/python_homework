#如何将0-10随机存入列表中
import random
ls = []
for i in range(10):
	ls.append(random.randint(0, 10)) 
print(ls)