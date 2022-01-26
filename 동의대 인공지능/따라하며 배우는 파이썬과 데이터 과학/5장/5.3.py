print('맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다. ')
print('1) 햄버거 \n2) 치킨 \n3) 피자')
menu = int(input('1에서 3까지의 메뉴를 선택하세요 : '))

while menu not in [1, 2, 3]:
        menu = int(input('메뉴를 다시 입력하세요: '))
        if menu == 1 or menu == 2 or menu ==3:
            break

if menu == 1 or menu == 2 or menu == 3:
    if menu == 1:
        print('햄버거를 선택하였습니다.')
    elif menu == 2:
        print('치킨을 선택하였습니다.')
    else:
        print('피자를 선택하였습니다.')
