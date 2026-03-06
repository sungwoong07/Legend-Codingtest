T = int(input())

def dfs(idx, sum):
    global cnt

    if sum > K:
        return

    if idx == N:
        if sum == K:
            cnt += 1
        return

    dfs(idx + 1, sum + A[idx])
    dfs(idx + 1, sum)

for tc in range(1, T + 1):

    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = 0

    dfs(0, 0)

    print(f'#{tc} {cnt}')