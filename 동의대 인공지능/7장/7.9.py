def overlap(str1, str2):
    result = ''
    for i in range(len(str1)):
        if str1[i:len(str1)] == str2[0:len(str1)-i]:
            result += str1[i:len(str1)]
            break
        else:
            result = ''

    print('일치하는 값 :', result)
    str2 = str2[len(result):len(str2)]

    if result == str2[0:len(result)]:
        return str1 + str2
    else:
        return str1 + str2



str1 = input('첫번째 문자열을 입력하세요 : ')
str2 = input('두번째 문자열을 입력하세요 : ')

new_str = overlap(str1, str2)
print('새로운 문자열 :', new_str)