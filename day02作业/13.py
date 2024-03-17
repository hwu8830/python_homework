a = float(input("第一条边长："))
b = float(input("第二条边长："))
c = float(input("第三条边长："))
d = a+b+c
e = (d/2)
s = (e*((e-a)*(e-b)*(e-c)))**0.5
print(f'周长是{d},面积是{s}')
