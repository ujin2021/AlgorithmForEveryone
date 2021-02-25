# 삽입정렬을 사용해서 내림차순으로 정렬하기

def sort_desc(a) :
    n = len(a)
    for i in range(1, n) :
        key = a[i] # 삽입할 값
        j = i - 1
        while j >= 0 and a[j] < key :
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

d = [2, 4, 3, 1, 5]
sort_desc(d)
print(d)