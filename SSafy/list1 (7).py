import sys
sys.stdin = open("sample_input (6).txt", 'r')

T = int(input())

for tc in range(1, T + 1):

    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    big_num = 0
    small_num = 99999999
    for i in range(n - m + 1):
        my_sum = 0
        for j in range(m):
            my_sum += arr[i + j]
        if my_sum >= big_num:
            big_num = my_sum
        if my_sum <= small_num:
            small_num = my_sum

    print(f'#{tc} {big_num - small_num}')










