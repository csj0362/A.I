depth = int(input('우물의 깊이를 입력하세요 : '))
meter = 7
num = 0

while 1:
    num += 1
    print('day : {} 달팽이의 위치 : {} 미터'.format(num, meter))

    meter += 2
    if meter > depth + 1:
        print('축하합니다. 우물을 탈출하였습니다.')
        print('우물을 탈출하는 데 걸린 날은 {}일 입니다. '.format(num))
        break
