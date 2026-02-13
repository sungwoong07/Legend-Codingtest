# import sys

# sys.stdin = open("input1.txt", "r")


T = int(input())

for tc in range(1, T + 1):

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_room = 0

