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
    