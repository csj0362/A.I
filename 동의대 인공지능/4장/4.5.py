import random

bok1 = random.randint(0, 9)
bok2 = random.randint(0, 9)
bok3 = random.randint(0, 9)

num1, num2, num3 = map(int, input('세 복권번호를 입력하시오 : ').split())
list1 =[num1, num2, num3]

if bok1 in list1 and bok2 in list1 and bok3 in list1:
    print('상금 1억원')
elif (bok1 in list1 and bok2 in list1) or (bok1 in list1 and bok3 in list1) or (bok2 in list1 and bok3 in list1):
    print('상금 1천만원')
elif bok1 in list1 or bok2 in list1 or bok3 in list1:
    print('상금 1만원')
else:
    print('다음 기회에...')

print(bok1, bok2, bok3)