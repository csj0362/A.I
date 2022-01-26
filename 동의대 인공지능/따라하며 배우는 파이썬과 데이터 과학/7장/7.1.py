num_list = [100, 200, 300, 400, 500, 600, 700, 800]
high = 6
low = 3

# 1
print(num_list[high]) # 예측: 700
# 2
print(num_list[high - 2]) # 예측: 500
# 3
print(num_list[high - low]) # 예측: 400
# 4
print(num_list[low - high]) # 예측: 600
# 5
print(num_list[-1]) # 예측: 800
# 6
print(num_list[-low]) # 예측: 600
# 7
print(num_list[2 * 3]) # 예측: 700
# 8
print(num_list[2] * 3) # 예측: 900
# 9
print(num_list[5 % 4]) # 예측:200
# 10
print(len(num_list)) # 예측: 8
# 11
print(min(num_list)) # 예측: 100
# 12
print(max(num_list)) # 예측: 800
# 13
print(num_list[:3]) # 예측: [100, 200, 300]
# 14
print(num_list[1:5]) # 예측: [200, 300, 400, 500]
# 15
print(num_list[-1:-5:-1]) # 예측: [800, 700, 600, 500]
# 16
print(num_list[-5:-1:1]) # 예측: [400, 500, 600, 700]