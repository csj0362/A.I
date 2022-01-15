#리스트에서 홀수인 데이터만 추출

num_list = [1, 5, 7, 15, 16, 22, 28, 29]

def get_odd_num(num_list):
    num_list = [data for data in num_list if data % 2 == 1]
    return num_list

print(get_odd_num(num_list))