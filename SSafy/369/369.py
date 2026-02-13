import sys

sys.stdin = open("input.txt", "r")

n = int(input())

num = []
cnt = 0
# i에 1 부터 10을 넣어준다
for i in range(1, n + 1):
    # str 으로 바꿔서, 3/6/9 가 포함되어 있다면
    my_str = str(i)
    cnt = 0
    if my_str in '3' or my_str in '6' or my_str in '9':
        cnt += 1
        my_str = '-' * cnt
    num.append(my_str)
    continue
print(*num)
        # for 루프 돌면서 3,6,9의 개수만큼 - 를 추가한다.
    # 포함되어 있지 않는다면 그냥 리스트에 추가 
