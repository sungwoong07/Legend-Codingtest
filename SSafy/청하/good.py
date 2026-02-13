import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):

    n = int(input())
    arr = list(map(int, input().split()))

    max_num = 0

    cnt = 1
    cnt2 = 1

    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            cnt += 1
        else:
            cnt = 1
        if arr[i] > arr[i + 1]:
            cnt2 += 1
        else:
            cnt2 = 1
        max_num = max(max_num, cnt, cnt2)
    print(f'#{tc} {max_num}')
