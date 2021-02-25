# 일반적인 삽입 정렬 알고리즘

def ins_sort(a) :
    n = len(a)
    for i in range(1, n) :
        key = a[i]
        j = i - 1 
        # j인덱스의 값과 key를 비교해 key가 들어갈 인덱스를 찾는다
        while j >= 0 and a[j] > key : # 삽입할 값보다 현재 인덱스의 값이 크면
            a[j + 1] = a[j] # 삽입할 공간이 생기도록 값을 오른쪽으로 한칸 이동시킨다
            j -= 1
        a[j + 1] = key # 찾은 위치에 key 삽입

d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)