import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):

    n, m = list(map(int, input().split()))

    check = True
    
    for _ in range(n):
        if m % 2 == 0:
            check = False
            break
        m //= 2

    if check:
        print(f'#{tc} {'ON'}')
    else:
        print(f'#{tc} {"OFF"}')
    