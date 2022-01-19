#2개의 딕셔너리 객체를 합쳐서 출력

from collections import defaultdict
from itertools import chain


dict_first = {'사과' : 30, '배' : 15, '감' : 10, '포도' : 10}
dict_second = {'사과' : 5, '감' : 25, '배' : 15, '귤' : 25}
dict_third = defaultdict(list)

def merge_dict(dict_first, dict_second):
    for i, j in chain(dict_first.items(), dict_second.items()):
        dict_third[i].append(j)

    result = {i:sum(j) for i,j in sorted(dict_third.items())}
    print(result)

merge_dict(dict_first, dict_second)