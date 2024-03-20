Ts = int(input("T恤的数量："))
Kz = int(input("裤子的数量："))
i=0
j=0
if Ts == 1:
   i=35 
elif Ts==2:
   i=35*2*0.9
elif Ts>2:
   i=35*Ts*0.8

if Kz<=2:
   j=120
elif Kz>2:
   j=120*Kz*0.9


print(i+j)
