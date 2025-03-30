from collections import deque

def solution(nodes, edges):
    # 그래프 생성
    graph = {node: [] for node in nodes}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # 모든 트리 찾기
    visited = set()
    odd_even_count = 0
    reverse_odd_even_count = 0
    
    for start_node in nodes:
        if start_node in visited:
            continue
        
        # 트리 찾기
        tree_nodes = []
        queue = deque([start_node])
        visited.add(start_node)
        
        while queue:
            node = queue.popleft()
            tree_nodes.append(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        # 트리의 중심 노드를 찾고, 그 중심을 루트로 먼저 시도
        center = find_tree_center(tree_nodes, graph)[0]
        
        # 중심 노드를 루트로 했을 때 확인
        can_be_odd_even, can_be_reverse_odd_even = check_tree(center, graph)
        
        # 중심 노드에서 결과가 나오지 않으면 다른 노드들도 확인
        if not (can_be_odd_even and can_be_reverse_odd_even):
            for root in tree_nodes:
                if root == center:  # 이미 확인한 노드는 건너뛰기
                    continue
                
                is_odd_even, is_reverse = check_tree(root, graph)
                
                if is_odd_even:
                    can_be_odd_even = True
                if is_reverse:
                    can_be_reverse_odd_even = True
                    
                if can_be_odd_even and can_be_reverse_odd_even:
                    break
        
        if can_be_odd_even:
            odd_even_count += 1
        if can_be_reverse_odd_even:
            reverse_odd_even_count += 1
    
    return [odd_even_count, reverse_odd_even_count]

def find_tree_center(nodes, graph):
    """트리의 중심 노드(들) 찾기"""
    if len(nodes) <= 2:
        return nodes
    
    # 리프 노드 식별
    degree = {node: len(graph[node]) for node in nodes}
    leaves = [node for node in nodes if degree[node] == 1]
    
    remaining_nodes = set(nodes)
    
    # 리프 노드를 제거하며 중심으로 이동
    while len(remaining_nodes) > 2:
        new_leaves = []
        
        for leaf in leaves:
            remaining_nodes.remove(leaf)
            
            # 이웃 노드의 차수 감소
            for neighbor in graph[leaf]:
                if neighbor in remaining_nodes:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        new_leaves.append(neighbor)
        
        leaves = new_leaves
        
        if not leaves:
            break
    
    return list(remaining_nodes)

def check_tree(root, graph):
    """주어진 루트로 트리를 구성하고 홀짝/역홀짝 조건을 확인"""
    # 자식 노드 구성 (BFS 사용)
    children = {}
    queue = deque([root])
    visited = {root}
    
    while queue:
        node = queue.popleft()
        children[node] = []
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                children[node].append(neighbor)
                queue.append(neighbor)
    
    # 모든 노드 조건 확인
    is_odd_even = True
    is_reverse = True
    
    for node in visited:
        num_children = len(children.get(node, []))
        
        # 홀짝 트리 조건 확인
        node_odd_even_valid = ((node % 2 == 1 and num_children % 2 == 1) or 
                              (node % 2 == 0 and num_children % 2 == 0))
        
        # 역홀짝 트리 조건 확인
        node_reverse_valid = ((node % 2 == 1 and num_children % 2 == 0) or 
                             (node % 2 == 0 and num_children % 2 == 1))
        
        if not node_odd_even_valid:
            is_odd_even = False
        if not node_reverse_valid:
            is_reverse = False
            
        if not is_odd_even and not is_reverse:
            break
    
    return is_odd_even, is_reverse