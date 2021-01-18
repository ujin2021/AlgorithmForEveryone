# 연습문제 1) q7.py 와 달리 중복된 값이 존재하는 리스트가 있을 때, 해당 인덱스를 모두 반환하도록
def find_idx(a, n) :
    idx = []
    len_a = len(a)
    for i in range(len_a) :
        if(a[i] == n) :
            idx.append(i)
    return idx

v = [17, 92, 18, 33, 58, 7, 33, 42, 33, 33, 17, 18]
print(find_idx(v, 18))
print(find_idx(v, 33))
print(find_idx(v, 900))

# 연습문제 2) 학생번호와 이름이 리스트로 주어졌을때, 학생번호를 입력하면 학생번호에 해당하는 이름을 순차 탐색으로 돌려주는 함수
# 해당 학생번호가 없다면 물음표를 돌려준다
def find_std(n) :
    std_no = [39, 14, 67, 105]
    std_name = ['Justin', 'John', 'Mike', 'Summer']
    length = len(std_no)
    for i in range(length) :
        if(std_no[i] == n) :
            return std_name[i]
    return '?'
    
print()
print(find_std(39))
print(find_std(14))
    
