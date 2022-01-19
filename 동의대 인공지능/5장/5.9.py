count, max_num = 0, 0
list1 = []
while 1:
    num = int(input('정수를 입력하시오 : '))

    if num == -99:
        break
    
    list1.append(num)
    count += 1
    
print(f'{count}개의 유효한 정수중 가장 큰 정수는 {max(list1)} 이고, \
    가장 작은 정수는 {min(list1)} 입니다.')

    
