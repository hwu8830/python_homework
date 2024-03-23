#如果两个素数之差为2,这样的两个素数就叫作"孪生数",找出100以内的所有"孪生数"
nums=[2,3]
d={}
for j in range(4,101):
    k =True
    for i in range(2,j):
        if j%i==0 or j%2 == 0 or j%3==0:
            k = False
            break 
    if k:        
        nums.append(j)  
print(nums)
i=0
print("其中为孪生数的有")
while i < len(nums)-1:
    a = nums[i]
    b = nums[i+1]    
    if b-a == 2:    
        d[a]=b
    i+=1

for i,j in d.items():
    print(i,j)


       