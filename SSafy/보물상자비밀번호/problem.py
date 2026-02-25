import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = input().strip()
    
    length = N // 4
    result = set()
    
    for _ in range(length):
        for i in range(0, N, length):
            part = numbers[i:i+length]
            result.add(int(part, 16))  # 여기서 바로 10진수로 변환
        
        numbers = numbers[-1] + numbers[:-1]
    
    # 그냥 숫자 정렬 (내림차순)
    result = sorted(result, reverse=True)
    
    print(f"#{tc} {result[K-1]}")

