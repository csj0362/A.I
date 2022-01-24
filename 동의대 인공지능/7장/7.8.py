num = int(input('n을 입력하시오 : '))
count = 0
if num > 10 or num < 1:
    while 1:
        num = int(input('n을 입력하시오 : '))
        if num >= 1 and num <= 10:
            break
numbers = list(range(1, num*num+1))

result_list = []
j = 0
for i in range(num):
    if i % 2 == 0:
        result_list.append(numbers[j:j+num])
        #print(k)
    else:
        result_list.append(numbers[j+(num-1):j-1:-1])
        #print(f'{" ".join(map(str, numbers[j+(num-1):j-1:-1])):<13}')
    j = j + num 

for i in result_list:
    for j in i:
        if j < 10:
            print(' {:<2}'.format(j), end = ' ')
        else:
            print('{:<3}'.format(j), end = ' ')
    print()

# j = 0
# for i in range(num):
#     if i % 2 == 0:
#         print('  '.join(map(str, numbers[j:j+num])), end = ' ') 
#     else:
#         print('  '.join(map(str, numbers[j+(num-1):j-1:-1])), end = ' ') 
#     j = j + num 
#     print()

# for i in range(num):
#     if i == 0:
#         print('0번째')    
#     else:
#         count += 1
#         for j in range(num):
#             if i % 2 == 0:
#                 print('짝수 : ', numbers[num * count + 1:num * (count+1)+2:1], end = ' ')       
#             else:
#                 print('홀수: ', numbers[num * count + 1:num * (count+1)+1:1], end = ' ')