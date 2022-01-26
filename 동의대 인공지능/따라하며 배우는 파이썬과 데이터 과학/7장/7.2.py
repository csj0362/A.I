list1 = [3, 5, 7]
list2 = [2, 3, 4, 5, 6]

for i in list1:
    print('----------')
    for j in list2:
        sum = i * j
        print(f'{i} * {j} = {sum}')