num1, num2, num3 = map(int, input('세 정수를 입력하시오: ').split())

if num1 > num2:
  if num1 > num3:
    if num2 > num3:
      print(f'{num1} {num2} {num3}')
    else:
      print(f'{num1} {num3} {num2}')
  else: 
    print(f'{num3} {num1} {num2}')
else:
  if num2 > num3:
    if num1 > num3:
      print(f'{num2} {num1} {num3}')
    else:
      print(f'{num2} {num3} {num1}')
  else:
    print(f'{num3} {num2} {num1}')
