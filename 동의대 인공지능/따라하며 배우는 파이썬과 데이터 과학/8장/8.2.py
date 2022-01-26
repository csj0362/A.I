fruits_price = {"사과":3000, "배":4500, "수박":6000, "귤":2400, "포도":3400}
name = input('구매를 원하는 과일의 이름을 입력하시오 : ')
key = fruits_price[name]
print(f'오늘의 {name} 가격은 {key} 원 입니다.')