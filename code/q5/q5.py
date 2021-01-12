# 둘째마당 - 재귀 함수
# 문제 05 최대공약수 구하기

def gcd(a, b) :
    i = min(a, b) # 둘 중 작은 수 구하기
    while True:
        if a % i == 0 and b % i == 0 :
            return i
        i = i - 1

def euclid_gcd(a, b) :
    if(b == 0) :
        return a
    return euclid_gcd(b, a % b) # 처음엔 a > b일 수 있어도, (b, a%b)를 하면 다시 큰게 앞으로 가기때문에 상관없다

print(gcd(1, 5))
print(gcd(3, 6))
print(gcd(60, 24))
print(gcd(81, 27))
print()
print(euclid_gcd(1, 5))
print(euclid_gcd(3, 6))
print(euclid_gcd(60, 24))
print(euclid_gcd(81, 27))