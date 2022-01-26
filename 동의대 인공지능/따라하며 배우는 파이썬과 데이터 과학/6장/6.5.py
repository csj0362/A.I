def cel_to_fa(cel):
    fa = (9/5) * cel + 32
    return fa

for i in range(0, 51, 10):
    cel_to_fa(i)
    print(f'섭씨온도 : {i} -> 화씨온도 : {cel_to_fa(i)}')