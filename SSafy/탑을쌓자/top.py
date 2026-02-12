import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    n, w1, w2 = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    # 오름차순
    arr.sort()
    # 최소비용
    min_cos = 0

    for i in range(1, n + 1):
        # w1 층이 0 보다 크면
        # 화물을 큰 값부터 뽑아서 
        # 그 층 만큼 곱한다
        if w1 > 0:
            min_cos += arr.pop() * i
            # 층을 하나 깎는다
            w1 -= 1
        if w2 > 0:
            min_cos += arr.pop() * i
            w2 -= 1
    print(f'#{tc} {min_cos}')

