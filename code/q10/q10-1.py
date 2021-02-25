# 일반적인 병합 정렬 알고리즘

def merge_sort(a) :
    n = len(a)
    if n <= 1 : # 종료조건
        return
    
    # 그룹을 나누어 각각 병합 정렬을 호출
    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort(g1) # g1 = [3, 6, 8, 9, 10]
    merge_sort(g2) # g2 = [1, 2, 4, 5, 7]

    # print('mid : ', mid)
    # print('g1 : ', g1)
    # print('g2 : ', g2)

    # 두 그룹을 하나로 병합
    i1 = 0 # g1의 idx
    i2 = 0 # g2의 idx
    ia = 0 # a의 idx

    while i1 < len(g1) and i2 < len(g2) :
        if g1[i1] < g2[i2] :
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else :
            a[ia] = g2[i2] 
            i2 += 1
            ia += 1
        # print('a :', a)
    
    # 아직 남아있는 자료들을 결과에 추가
    while i1 < len(g1) :
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2) :
        a[ia] = g2[i2]
        i2 += 1
        ia += 1

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(d)
print(d)