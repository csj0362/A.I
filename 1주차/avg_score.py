#학생들의 평균점수 출력

score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]

def get_avg(score):
    for num, i in enumerate(score):
        print("{0} 번, 평균 : {1}".format(num + 1, sum(i)/2))

get_avg(score)