def in_order(node):
    # 노드 번호가 전체 노드 수(N) 이하일 때만 순회
    if node <= N:
        in_order(node * 2)  # 왼쪽 자식 방문
        print(tree[node], end='')  # 현재 노드(부모) 출력
        in_order(node * 2 + 1)  # 오른쪽 자식 방문


# 총 10개의 테스트 케이스 처리
for tc in range(1, 11):
    try:
        N = int(input())
    except EOFError:
        break  # 더 이상 입력이 없으면 종료

    # 1번 인덱스부터 사용하기 위해 N+1 크기의 배열 생성
    tree = [''] * (N + 1)

    for _ in range(N):
        # 입력받은 정점 정보 분리
        node_info = input().split()
        node_idx = int(node_info[0])
        node_char = node_info[1]

        # 트리의 해당 인덱스에 문자 저장
        tree[node_idx] = node_char

    print(f'#{tc} ', end='')
    in_order(1)  # 1번 노드(루트)부터 중위 순회 시작
    print()  # 테스트 케이스 종료 후 줄바꿈

