import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**6)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    
    for s, e in (map(int, input().split()) for _ in range(E)):
        graph[s].append(e)
    
    S, G = map(int, input().split())
    visited = [0]*(V+1)
    
    def dfs(v):
        if v == G: return 1
        visited[v] = 1
        for n in graph[v]:
            if not visited[n]:
                if dfs(n): return 1
        return 0
    
    print(f"#{tc} {dfs(S)}")