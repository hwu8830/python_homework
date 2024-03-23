# 求50~150之间的质数是那些？
nums=[]
for j in range(53,150):
    k =True
    for i in range(4,j):
        if j%i==0 or j%2 == 0 or j%3==0:
            k = False
            break 
    if k:        
        nums.append(j)  
print(nums) 
       

