# 쉽게 설명한 병합 정렬 알고리즘

def merge_sort(a) :
    n = len(a)
    # 종료 조건 : 정렬할 리스트의 자료 갯수가 한 개 이하이면 정렬할 필요가 없다
    if n <= 1 :
        return a
    # 그룹을 나누어 각각 병합 정렬을 호출하는 과정
    mid = n // 2
    g1 = merge_sort(a[:mid]) # 재귀호출로 첫번째 그룹을 정렬
    g2 = merge_sort(a[mid:]) # 재귀호출로 두번째 그룹을 정렬

    # 두 그룹을 하나로 병합
    result = [] # 두 그룹을 합쳐 만들 최종 결과
    while g1 and g2 : # 두 그룹에 모두 자료가 남아있는 동안 반복
        if g1[0] < g2[0] : # 각 그룹의 첫번째 값을 비교
            # g1 값이 더 작으면 그 값을 빼내어 결과에 추가
            result.append(g1.pop(0))
        else :
            # g2 값이 더 작으면 그 값을 빼내어 결과에 추가
            result.append(g2.pop(0))
    
    # 아직 남아있는 자료를 결과에 추가
    while g1 :
        result.append(g1.pop(0))
    while g2 :
        result.append(g2.pop(0))
    
    return result

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(d))