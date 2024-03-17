i = float(input("第一个数："))
j = float(input("第二个数："))
g = str(input("运算符："))

if g == '+':
     print(f'{i}+{j}={i+j}')
elif g == '-':
     print(f'{i}-{j}={i-j}')
elif g == '*':
     print(f'{i}*{j}={i*j}')
elif g == '/':
     print(f'{i}/{j}={i/j}')
elif g == '%':
     print(f'{i}%{j}={i%j}')
elif g == '//':
      print(f'{i}//{j}={i//j}')
elif g == '**':
      print(f'{i}**{j}={i**j}')