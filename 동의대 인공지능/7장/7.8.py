num = int(input('n을 입력하시오 : '))
count = 0
if num > 10 or num < 1:
    while 1:
        num = int(input('n을 입력하시오 : '))
        if num >= 1 and num <= 10:
            break

numbers = list(range(1, num*num+1))

j = 0
for i in range(num):
    if i % 2 == 0:
        print('  '.join(map(str, numbers[j:j+num])), end = ' ') 
    else:
        print('  '.join(map(str, numbers[j+(num-1):j-1:-1])), end = ' ') 
    j = j + num 
    print()
