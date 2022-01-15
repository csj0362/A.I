# 문자열에서 숫자를 제거한 후 string만 남은 리스트 출력
inputs = input("inputs = ")

def find_string(inputs):
    newString = ''.join(i if not i.isdigit() else ' ' for i in inputs).split()
    return newString

string_list = find_string(inputs)
print(string_list)