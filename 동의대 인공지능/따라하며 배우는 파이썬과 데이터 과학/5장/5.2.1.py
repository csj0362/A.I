sum, sum1, num = 0, 0, -1
for i in range(1, 100, 2):
    sum += i

print(f'1에서 100까지의 수 중에서 홀수의 합 : {sum}')
print('---------------------')

while num < 99:
    num += 2
    sum1 += num

print(f'1에서 100까지의 수 중에서 홀수의 합 : {sum1}')
