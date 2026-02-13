import sys
sys.stdin = open("input.txt", 'r')

dxy1 = [[-1,0], [0,-1], [1,0], [0, 1]]
dxy2 = [[-1,-1], [1,1], [-1,1], [1,-1]]
T = int(input())

for tc in range(1, T + 1):

    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_val = 0

    for i in range(n):
        for j in range(n):
            sum_val = arr[i][j]
            sum_num1 = arr[i][j]
            sum_num2 = arr[i][j]
            for dx, dy in dxy1:
                for dist in range(1, m):
                    ni = i + dx * dist
                    nj = j + dy * dist
                    if 0 <= ni < n and 0 <= nj < n:
                        sum_num1 += arr[ni][nj]
            for dx, dy in dxy2:
                for dist in range(1, m):
                    ni = i + dx * dist
                    nj = j + dy * dist
                    if 0 <= ni < n and 0 <= nj < n:
                        sum_num2 += arr[ni][nj]
            max_val = max(max_val, sum_num1, sum_num2)
    print(f'#{tc} {max_val}')
