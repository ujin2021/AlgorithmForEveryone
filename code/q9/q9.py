# 쉽게 설멍한 삽입 정렬 알고리즘

# 리스트 r에서 v가 들어가야 할 위치를 돌려주는 함수
# r : 이미 정렬되어있는 리스트
def find_ins_idx(r, v) :
    for i in range(0, len(r)) :
        if v < r[i] : # i자리 학생보다 작으면
            return i # 거기가 v의 자리
    return len(r) # 모든 친구보다 v가 키가 크다면 마지막 자리

def ins_sort(a) :
    result = [] # 정렬된 값을 저장할 새로운 리스트
    while a : 
        value = a.pop(0) # 기존 리스트에서 하나를 꺼낸다
        ins_idx = find_ins_idx(result, value) # 정렬된 list result에 들어갈 value의 위치 구하기
        result.insert(ins_idx, value)
    return result

d = [2, 4, 5, 1, 3]
print(ins_sort(d))