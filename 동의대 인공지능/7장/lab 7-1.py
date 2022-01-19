fruit_list = []
for i in range(3):
    name = input('좋아하는 과일 이름을 입력하시오: ')
    fruit_list.append(name)

fruit_name = input('과일의 이름을 입력하세요: ')

if fruit_name in fruit_list:
    print('이 과일은 당신이 좋아하는 과일입니다.')
else:
    print('이 과일은 당신이 좋아하는 과일이 아닙니다.')
    
print(fruit_list)