# 쉽게 설명한 선택 정렬 알고리즘

# 최소값의 위치를 돌려주는 함수
def find_min_idx(a) :
    n = len(a) 
    min_idx = 0
    for i in range(n) :
        if(a[i] < a[min_idx]) :
            min_idx = i
    return min_idx

# 정렬 함수
def sel_sort(a) :
    result = [] # 결과를 담을 새로운 list
    while a : # a에 값이 남아 있는 동안
        min_idx = find_min_idx(a) # 최소값의 인덱스를 받는다
        value = a.pop(min_idx) # 최소값을 value에 저장
        result.append(value) # 최소값을 result에 appned
    return result

d = [2, 4, 5, 1, 3]
print(sel_sort(d))