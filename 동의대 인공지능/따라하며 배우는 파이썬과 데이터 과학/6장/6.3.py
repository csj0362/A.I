def max3(n1, n2, n3):
    list1 = [n1, n2, n3]
    return max(list1)

def min3(n1, n2, n3):
    list1 = [n1, n2, n3]
    return min(list1)

num1, num2, num3 = map(int, input('3 수를 입력하시오 : ').split())

max_num = max3(num1, num2, num3)
min_num = min3(num1, num2, num3)

print(f'가장 큰 수 : {max_num} ')
print(f'가장 작은 수 : {min_num}')