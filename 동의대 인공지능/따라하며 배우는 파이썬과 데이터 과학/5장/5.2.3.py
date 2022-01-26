start_num = int(input('시작 정수를 입력하세요 : '))
end_num = int(input('끝 정수를 입력하세요 : '))
sum = 0

for i in range(start_num, end_num + 1, 1):
    sum += i

print('{} 에서 {} 까지 정수의 합 : {}'.format(start_num, end_num, sum ))