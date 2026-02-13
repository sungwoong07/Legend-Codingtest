import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):

    n = int(input())
    A = list(map(int, input().split())) # 바뀌기전 스위치
    B = list(map(int, input().split())) # 기준 스위치

    cnt = 0

    for i in range(n):
        
        if A[i] == B[i]:
            continue
        # 다르면 한번 카운트 받고 
        else:
            cnt += 1
            # i부터 n 까지 0이면 1로, 1이면 0으로 바꿔준다
            for a in range(i, n):
                if A[a] == 0: 
                    A[a] = 1
                elif A[a] == 1:
                    A[a] = 0
        

    print(f"#{tc} {cnt}")
