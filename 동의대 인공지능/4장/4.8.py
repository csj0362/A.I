print('1)덧셈 2)뺄셈 3)곱셈 4)나눗셈')
bun = int(input('어떤 연산을 원하는지 번호를 입력하세요: '))
while 1:
    if bun in [1, 2, 3, 4]:
        break 
    else:
        print('번호를 잘못 입력하였습니다.\n')
        bun = int(input('어떤 연산을 원하는지 번호를 입력하세요: '))
        

print('연산을 원하는 숫자 두개를 입력하세요')
num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)

if bun == 1:
    sum = num1 + num2
    print(f'{num1} + {num2} = {sum}')
elif bun == 2:
    sum = num1 - num2
    print(f'{num1} - {num2} = {sum}')
elif bun == 3:
    sum = num1 * num2
    print(f'{num1} * {num2} = {sum}')
elif bun == 4:
    sum = num1 / num2
    print(f'{num1} / {num2} = {sum}')
else:
    print('다시 입력하세요')

    
