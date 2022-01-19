from os import remove


fruit_list = ['banana', 'orange', 'kiwi', 'apple', 'melon']
remove_list = []
length = 0

#가장 긴 길이 확인
for i in fruit_list:
    if length < len(i):
        length = len(i)

#가장 긴 길이의 값을 저장
for i in fruit_list:
    if length == len(i):
        remove_list.append(i)
remove_str = " ".join(remove_list)
print(f'가장 길이가 긴 문자열 : {remove_str}')

#가장 긴 길이의 값을 삭제
for i in range(len(remove_list)):
    fruit_list.remove(remove_list[i])
print(f'fruit_list = {fruit_list}')


