print('1에서 100까지의 수 중에서 짝수는 ')
num = 0
for i in range(2, 101, 2):
    print(i, end = ' ')

print('\n--------------------------')
while num < 100:
    num += 2
    print(num, end = ' ')