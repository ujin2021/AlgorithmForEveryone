# 첫째마당 - 알고리즘 기초
# 문제 01 1부터 n까지의 합 구하기

'''
입력 : n
출력 : 1부터 n까지의 숫자를 더한 값
'''

def sum_n(n) :
    s = 0
    for i in range(0, n+1) :
        s += i
    return s

def sum_n_generalize(n) :
    return n * (n + 1) // 2 # 정수 출력을 위해 // 사용

print(sum_n(10))
print(sum_n(100))
print()
print(sum_n_generalize(10))
print(sum_n_generalize(100))