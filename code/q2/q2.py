# 첫째마당 - 알고리즘 기초
# 문제 02 최댓값 찾기

def findMax(num_list) :
    max_num = num_list[0]
    for i in num_list :
        if(i > max_num) :
            max_num = i
    return max_num

def findMax_idx(num_list) :
    max_num = num_list[0]
    max_idx = 0
    for i in range(len(num_list)) :
        if(num_list[i] > max_num) :
            max_idx = i
            max_num = num_list[i]
    return max_idx

print(findMax([17, 92, 18, 33, 58, 7, 33, 42]))
print(findMax_idx([17, 92, 18, 33, 58, 7, 33, 42]))