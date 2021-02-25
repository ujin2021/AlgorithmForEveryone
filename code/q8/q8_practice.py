# 선택정렬을 이용하여 내림차순 정렬 해보기

def sort_desc(a) :
    n = len(a)
    for i in range(0, n - 1) :
        max_idx = i
        for j in range(i + 1, n) :
            if(a[max_idx] < a[j]) :
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]

d = [2, 4, 5, 1, 3]
sort_desc(d)
print(d)