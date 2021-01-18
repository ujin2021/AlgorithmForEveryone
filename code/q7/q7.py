# 셋째마당 - 탐색과 정렬
# 문제 07 순차 탐색

# 주어진 리스트에서 특정값을 찾아 해당 위치 번호를 돌려주는 프로그램
# 찾으면 idx, 없으면 -1 return

def find_idx(a, n) :
    len_a = len(a)
    for i in range(len_a) :
        if(a[i] == n) :
            return i
    return -1

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_idx(v, 18))
print(find_idx(v, 33))
print(find_idx(v, 900))