n = int(input('정수를 입력하시오: '))
fact = 1 
for i in range(1, n):
    fact = fact * i
print(f'{n}!은 {fact}이다.')