def solution(n, s, a, b, fares):
    INF = float('inf')
    
    # 최단 거리 테이블 초기화
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    
    # 자기 자신까지의 거리는 0
    for i in range(1, n + 1):
        dist[i][i] = 0

    # 간선 정보 입력
    for c, d, f in fares:
        dist[c][d] = f
        dist[d][c] = f

    # 플로이드-워셜 알고리즘 실행
    for k in range(1, n + 1):  # 중간 노드
        for i in range(1, n + 1):  # 출발 노드
            for j in range(1, n + 1):  # 도착 노드
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # 최소 요금 계산
    min_cost = INF
    for k in range(1, n + 1):  # 합승 종료 지점 `k`
        cost = dist[s][k] + dist[k][a] + dist[k][b]
        min_cost = min(min_cost, cost)

    return min_cost

print(solution(6, 4, 6, 2, [
    [4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], 
    [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]
]))  # Output: 82

print(solution(7, 3, 4, 1, [
    [5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]
]))  # Output: 14

print(solution(6, 4, 5, 6, [
    [2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], 
    [5, 3, 20], [2, 4, 8], [4, 3, 9]
]))  # Output: 18
