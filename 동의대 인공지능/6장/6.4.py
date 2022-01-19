def max_and_min(n1, n2, n3):
    list1 = [n1, n2, n3]
    return max(list1), min(list1)

num1, num2, num3 = map(int, input('3 수를 입력하시오 : ').split())
max_num, min_num = max_and_min(num1, num2, num3)

print(f'가장 큰 수 : {max_num} ')
print(f'가장 작은 수 : {min_num}')