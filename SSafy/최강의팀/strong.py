import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):

    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort()

    max_cnt = 0

    for i in range(n):
        cnt = 0
        for j in range(i, n):
            if abs(arr[i] - arr[j]) <= k:
                cnt += 1
        max_cnt = max(max_cnt, cnt)
    print(f'#{tc} {max_cnt}')
                