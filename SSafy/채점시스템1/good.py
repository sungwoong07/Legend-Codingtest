import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):

    n, m = list(map(int, input().split())) # n: 학생수 m: 문항 수
    answer = list(map(int, input().split()))
    s_answer = [list(map(int, input().split())) for _ in range(n)]

    total = 0

    max_num = 0
    min_num = float('inf')
    
    for student in s_answer:

        s_num = 0
        s_cnt = 0

        for i in range(m):
            if student[i] == answer[i]:
                s_cnt += 1
                s_num += s_cnt
            else:
                s_cnt = 0
        max_num = max(max_num, s_num)
        min_num = min(min_num, s_num)
    print(f'#{tc} {max_num - min_num}')

    

            

