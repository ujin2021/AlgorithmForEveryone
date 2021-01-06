# 1부터 n까지 연속한 숫자의 제곱의 합을 구하는 프로그램
# 반복문 사용

def sum_square(n) :
    s = 0
    for i in range(1, n+1) :
        s += i * i
    return s

def sum_square_2(n) :
    s = 0
    return n * (n + 1) * (2 * n + 1) // 6

print(sum_square(10))
print()
print(sum_square_2(10))

'''
sum_square
    계산 복잡도 : O(n)
    입력의 갯수와 계산횟수가 비례한다

sum_square_2
    계산 복잡도 : O(1)
    게산횟수가 입력의 갯수와 무관하다
'''