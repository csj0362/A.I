num = int(input('숫자를 입력하세요 : '))

for n in range(1, num + 1):
    print(' '*(num-n) + '*'*n)


