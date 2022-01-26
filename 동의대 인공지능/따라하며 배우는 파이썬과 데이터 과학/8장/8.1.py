apple, pear, watermellon, mandarin, grape = \
    map(int, input('사과, 배, 수박, 귤, 포도 가격을 공백으로 구분하여 입력: ').split())
fruits_price = {"사과":apple, "배":pear, "수박":watermellon, "귤":mandarin, "포도":grape}

print('-----------오늘의 가격-------------')
for i in fruits_price.keys():
    print('{:<6}'.format(i), ' :     ', fruits_price[i], '원')
