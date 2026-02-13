import sys

sys.stdin = open('input.txt', 'r')

dxy1 = [[1,0], [0,1], [0,-1], [-1,0]]
dxy2 = [[-1,-1], [1,-1], [-1,1], [1,1]]
T = int(input())

for tc in range(1, T + 1):

    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_boom = 0

    for i in range(n):
        for j in range(m):
            sum_boom = arr[i][j]
            sum_boom1 = arr[i][j]

            for dx, dy in dxy1:
                for dist in range(1, arr[i][j]+1):
                    ni = i + dx * dist
                    nj = j + dy * dist
                    if 0 <= ni < n and 0 <= nj < m:
                        sum_boom += arr[ni][nj]
            for dx, dy in dxy2:
                for dist in range(1, arr[i][j]+1):
                    ni = i + dx * dist
                    nj = j + dy * dist
                    if 0 <= ni < n and 0 <= nj < m:
                        sum_boom1 += arr[ni][nj]
            max_boom = max(max_boom, sum_boom, sum_boom1)
    print(f'#{tc} {max_boom}')
            


