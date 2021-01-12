# 피보나치 수열이 0부터 시작한다 할 때 n번째 피보나치 수를 재귀함수를 이용해 구하시오
# 재귀함수
def fib(n) :
    # if(n == 0) :
    #     return 0
    # elif(n == 1) :
    #     return 1
    if(n <= 1) :
        return n # 위의 두 조건을 합쳐서 나타낼 수 있다
    else :
        return fib(n - 1) + fib(n - 2)

# 반복문
def fib_loop(n) :
    if(n <= 1) :
        return n
    if(n == 2) :
        return 1
    a = 0 # fib(0)
    b = 1 # fib(1)
    c = 1 # fib(2) = fib(1) + fib(0)
    for i in range(n-2):
        a = b # fib(1)
        b = c  # fib(2)
        c = a + b # fib(3) = a + b
    return c
        

print(fib(7))
print(fib(10))
print()
print(fib_loop(7))
print(fib_loop(10))
print(fib_loop(12))
print(fib_loop(3))