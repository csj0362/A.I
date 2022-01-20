while 1:
    num = input('정수를 입력하시오 : ')
    if int(num) > 0:
        num1 = (num[::-1])

        if num1 == num:
            print(f'{num}은 거꾸로 정수입니다.\n')
        else:
            print(f'{num}은 거꾸로 정수가 아닙니다.\n')
    else: 
        if num == '-99':
            print('프로그램을 종료합니다.')
            break
        else:
            print('잘못된 수입니다.\n')
