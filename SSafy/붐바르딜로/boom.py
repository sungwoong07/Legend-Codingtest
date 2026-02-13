import sys
sys.stdin = open('input.txt', 'r')

dxy = [[0,1], [1,0], [0,-1], [-1,0]]

T = int(input())

for tc in range(1, T + 1):

    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_cnt = 0

    for i in range(n):
        for j in range(m):
            # 자기자신
            boom = arr[i][j]
            
            for dx, dy in dxy:
                # 해당 지역 범위 만큼 추가로 1개씩 터트린다
                for dist in range(1, arr[i][j]+1):
                    ni = i + dx * dist 
                    nj = j + dy * dist
                    if 0 <= ni < n and 0 <= nj < m:
                        boom += arr[ni][nj]
                max_cnt = max(max_cnt, boom)
    print(f'#{tc} {max_cnt}')



