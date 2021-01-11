# 둘째마당 - 재귀 함수
# 문제 04 팩토리얼 구하기

def fact(n) :
    f = 1 
    for i in range(1, n+1) :
        f *= i
    return f

# 재귀 함수 사용
def fact_re(n) :
    if n <= 1:
        return 1
    return n * fact_re(n-1)


print(fact(4))
print(fact(5))
print()
print(fact_re(4))
print(fact_re(5))