from itertools import combinations

T = int(input())

for tc in range(1, T + 1):

    n, k = list(map(int, input().split()))

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    cnt = 0

    for i in combinations(a, n):
        if sum(i) == k:
            cnt += 1
    print(f'#{tc} {cnt}')

        
            
        


