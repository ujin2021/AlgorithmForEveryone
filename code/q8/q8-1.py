# 일반적인 선택 정렬 알고리즘

def sel_sort(a) :
    n = len(a)
    for i in range(0, n - 1) :
        min_idx = i # 최소 인덱스를 i로 잡고
        for j in range(i + 1, n) : # i 이후에 i보다 작은 게 있는지 확인
            if a[j] < a[min_idx] :
                min_idx = j # 제일 작은 수의 인덱스를 찾는다
        a[i], a[min_idx] = a[min_idx], a[i] # swap

d = [2, 4, 5, 1, 3]
sel_sort(d)
print(d)