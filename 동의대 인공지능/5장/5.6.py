import re
tank = 500

while 1:
    num = input('충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오: ')

    if num[0] == '+':
        print('현재 탱크양은 {} 입니다.'.format(tank + int(''.join(re.findall("\d+", num)))))
        tank = tank + int(''.join(re.findall("\d+", num)))
    else:
        print('현재 탱크양은 {} 입니다.'.format(tank - int(''.join(re.findall("\d+", num)))))
        tank = tank - int(''.join(re.findall("\d+", num)))
        if tank < 50:
            print('경고 : 연료가 10% 미만이니 충전하세요!')
            break