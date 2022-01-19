import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

print(f'{num1} + {num2} = ', end = ' ')
result = int(input())

if num1 + num2 == result:
    print('참 잘했어요!!')
else:
    print('정답은', num1 + num2, '입니다.')