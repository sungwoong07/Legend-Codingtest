import sys

sys.stdin = open("input2.txt", "r")

T = int(input())

for tc in range(1, T + 1):

    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = 0
    
    for i in range(n):
        if A[i] == B[i]:
            continue
        cnt += 1
        for j in range(i, n):
            if A[j] == 0:
                A[j] = 1
            else:
                A[j] = 0
    print(f'#{tc} {cnt}')