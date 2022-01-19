def is_prime(n):
    for i in range(2, n, 1):
        if n % i == 0:
            return False
    
    return True

while 1:
    num = int(input('소수 검사를 할 정수를 입력하시오: '))
    if num == 1:
        print(f'종료합니다.')
        break
    result = is_prime(num)
    print(f'소수인가요? : {result}')
    print()