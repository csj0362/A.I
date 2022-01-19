num = int(input('n을 입력하시오 : '))
count = 0
if num > 10 or num < 1:
    while 1:
        num = int(input('n을 입력하시오 : '))
        if num >= 1 and num <= 10:
            break

numbers = list(range(num*num))
print(numbers, 'li')

for i in range(num):
    if i == 0:
        print('0번째')    
    else:
        count += 1
        for j in range(num):
            if i % 2 == 0:
                print('짝수 : ', numbers[j]+1, end = ' ')       
            else:
                print('홀수: ', numbers[num * count + 1:num * (count+1):1], end = ' ')