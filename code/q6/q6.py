# 둘째마당 - 재귀 함수
# 문제 06 하노이의 탑 옮기기

'''
n : 원반의 갯수
from_pos : 옮길원반이 있는 출발점 기둥
to_pos : 도착점 기둥
aux_pos : 보조기둥
'''

def hanoi(n, from_pos, to_pos, aux_pos) :
    if(n == 1) :
        print(f'{from_pos} -> {to_pos}')
        return
    hanoi(n-1, from_pos, aux_pos, to_pos) # 원반 n-1개를 출발기둥에서 보조기둥으로 옮긴다
    print(f'{from_pos} -> {to_pos}') # 가장 큰 원반을 도착점 기둥으로 옮긴다
    hanoi(n-1, aux_pos, to_pos, from_pos) # 원반 n-1개를 보조기둥에서 도착점 기둥으로 옮긴다

print('n = 1')
hanoi(1, 1, 3, 2)

print('n = 2')
hanoi(2, 1, 3, 2)

print('n = 3')
hanoi(3, 1, 3, 2)