import sys

sys.stdin = open('inport.txt', 'r')

dxy = [[1,0], [0,1], [0,-1], [-1,0]]

T = int(input())

for tc in range(1, T + 1):

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 안전한 거리?
    max_cnt = 0
    # 괴물에서 1 을 만나기 전까지 빈칸에 횟수를 세주는 것
    cnt = 0
    # 전체 0 
    cnt2 = 0
    for i in range(n):
        for j in range(n):
            # 괴물 자리
            if arr[i][j] == 2:
                for dx, dy in dxy:
                    # 쭉쭉 뻗어준다(자기 자신을 빼고)
                    for dist in range(1, n):
                        ni = i + dx * dist
                        nj = j + dy * dist
                        # n*n의 제한
                        if 0 <= ni < n and 0 <= nj < n:
                            # 1이라는 벽을 만나면 멈춘다
                            if arr[ni][nj] == 1:
                                break
                            # 위 조건을 반복 못하면 광선이 쏘는 안전하지 못한 빈칸
                            cnt += 1
            # 전체 0에 갯수를 세준다
            if arr[i][j] == 0:
                cnt2 += 1

    print(f'#{tc} {cnt2 - cnt}')
            



            
