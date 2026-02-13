import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):

    n = int(input())
    arr = list(map(int, input().split()))

    max_carrot = 0

    cnt = 1

    for i in range(n-1): 
        if arr[i] < arr[i + 1]:
            cnt += 1
        else:
            cnt = 1
        max_carrot = max(max_carrot, cnt)

    print(f'#{tc} {max_carrot}')
        