Seoul = 9765
Busan = 3441
Incheon = 2954
Daejeon = 1531
max_num = 0
min_num = 99999
sum = 0
city_pop = [Seoul, Busan, Incheon]
city_pop.append(Daejeon)

for i in city_pop:
    if i > max_num:
        max_num = i
    if i < min_num:
        min_num = i
    sum += i

print(f'최대 인구 : {max_num}')
print(f'최소 인구 : {min_num}')
print(f'평균 인구 : {sum / len(city_pop)}')
