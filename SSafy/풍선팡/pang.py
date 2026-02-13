import sys
sys.stdin = open('pang.txt', 'r')

dxy = [[1,0], [0,1], [-1,0], [0,-1]]
T = int(input())

for tc in range(1, T + 1):

    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_val = 0

    for i in range(n):
        for j in range(m):
            sum_val = arr[i][j]
        
            for dx, dy in dxy: 
                for dist in range(1, arr[i][j] + 1):
                    ni = i + dx * dist
                    nj = j + dy * dist
                    if 0 <= ni < n and 0 <= nj < m:
                        sum_val += arr[ni][nj]
                    max_val = max(max_val, sum_val)
    print(f'#{tc} {max_val}')


        