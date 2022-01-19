sum, sum1, num = 0, 0, 0
for i in range(0, 102, 2):
    sum += i

print(f'1에서 100까지의 수 중에서 짝수의 합 : {sum}')
print('---------------------')

while num < 100:
    num += 2
    sum1 += num

print(f'1에서 100까지의 수 중에서 짝수의 합 : {sum1}')
