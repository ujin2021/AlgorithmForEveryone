# 숫자 n개를 리스트로 입력받아 최솟값을 구하는 프로그램

def find_max(num_list) :
    min_num = num_list[0]
    for i in num_list :
        if(i < min_num) :
            min_num = i
    return min_num

print(find_max([3, 5, 1, 7, 10]))