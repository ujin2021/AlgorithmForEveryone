# practice1 : 재귀 함수를 사용해 1부터 n까지 합 구하기
def sum_n(n) :
    if(n == 1) :
        return 1
    return n + sum_n(n-1)

print(sum_n(4))

# practice2 : 재귀 함수를 사용해 가장 큰 숫자 찾기 - 풀이 참고
def find_max(num_list, n) :
    print(f'{num_list}, {n}') # n이 점점 작아진다
    if n == 1:
        return num_list[0]
    max_n = find_max(num_list, n - 1)
    if max_n > num_list[n - 1] :
        return max_n
    else:
        return num_list[n - 1]

print(find_max([3, 5, 10, 1, 7], 5))