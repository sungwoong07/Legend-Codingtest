import sys

sys.stdin = open('inport.txt', 'r')

T = int(input())

for tc in range(1, T + 1):

    n = int(input())
    arr = list(map(int, input()))

    cnt = 0
    max_cnt = 0

    for i in arr:
        if i == '1':
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
        else:
            cnt = 0
    print(max_cnt)
        
                
    

                
    
