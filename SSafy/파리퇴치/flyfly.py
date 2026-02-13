import sys

sys.stdin = open('input2.txt', 'r')

T = int(input())

for tc in range(1, T + 1):

    n, m = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_num = 0
    for l in range(n - m + 1):
        for k in range(n - m + 1):
            sum_num = 0
            for i in range(m):
                for j in range(m):
                    sum_num += arr[i + l][j + k]
                max_num = max(max_num, sum_num)
    print(f'#{tc} {max_num}')
        