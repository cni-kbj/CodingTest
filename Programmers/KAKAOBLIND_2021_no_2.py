from collections import defaultdict
import sys

sys.setrecursionlimit(300000)

def solution(sales, links):
    n = len(sales)
    
    # 1. 트리 구조 만들기
    tree = defaultdict(list)
    for a, b in links:
        tree[a].append(b)
    
    # 2. DP 배열 선언 (각 직원이 참석하는 경우와 참석하지 않는 경우를 나눔)
    dp = [[0, 0] for _ in range(n + 1)]
    
    # 3. DFS로 트리 DP 수행
    def dfs(node):
        dp[node][1] = sales[node - 1]  # node가 참석할 경우
        
        if not tree[node]:  # 리프 노드인 경우
            return
        
        extra_cost = sys.maxsize  # 팀장 불참 시 최소 추가 비용
        
        for child in tree[node]:
            dfs(child)
            if dp[child][0] < dp[child][1]:
                dp[node][0] += dp[child][0]  # 팀원이 불참하는 게 이득이면 불참
                dp[node][1] += dp[child][0]
                extra_cost = min(extra_cost, dp[child][1] - dp[child][0])
            else:
                dp[node][0] += dp[child][1]  # 한 명 이상은 참석해야 하므로 참석
                dp[node][1] += dp[child][1]
                extra_cost = 0  # 최소 한 명 참석했으므로 추가 비용 필요 없음
        
        if extra_cost > 0:  # 팀장이 불참할 경우 반드시 한 명은 참석해야 함
            dp[node][0] += extra_cost
    
    # CEO(1번 직원)부터 시작
    dfs(1)
    
    return min(dp[1][0], dp[1][1])  # CEO가 참석하는 경우와 참석하지 않는 경우 중 최소값 반환

sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
print(solution(sales, links))  # Output: 44

sales = [5, 6, 5, 3, 4]
links = [[2,3], [1,4], [2,5], [1,2]]
print(solution(sales, links))  # Output: 6

sales = [5, 6, 5, 1, 4]
links = [[2,3], [1,4], [2,5], [1,2]]
print(solution(sales, links))  # Output: 5

sales = [10, 10, 1, 1]
links = [[3,2], [4,3], [1,4]]
print(solution(sales, links))  # Output: 2
