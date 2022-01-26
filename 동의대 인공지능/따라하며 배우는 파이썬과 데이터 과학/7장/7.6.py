my_str = input('문자열을 입력하세요 : ')

# for i in range((len(my_str)*2 +1)):
#     print(my_str[:i])
#     if my_str[:i] == my_str:
#         break

# for i in range((len(my_str)*2 +1)):
#     print(my_str[:(len(my_str)*2 +1)-i])

for i in range((len(my_str))):
    print(my_str[:i])

for i in range((len(my_str))):
    print(my_str[:(len(my_str))-i])
