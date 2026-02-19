import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    mid = n // 2
    total = 0

    for i in range(n):
        dist = abs(mid - i)

        start = dist
        end = n - dist

        for j in range(start, end):
            total += arr[i][j]

    print(f'#{tc} {total}')


