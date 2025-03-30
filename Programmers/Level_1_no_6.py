from sys import setrecursionlimit

# 재귀 깊이 제한 설정
setrecursionlimit(10000)

class Node:
    def __init__(self, info):
        self.num = info[2]  # 노드 번호
        self.pos = info[:2]  # [x, y] 좌표
        self.left = None     # 왼쪽 자식
        self.right = None    # 오른쪽 자식

def solution(nodeinfo):
    # 각 노드에 번호를 추가하고, y 값을 기준으로 내림차순 정렬
    for idx, info in enumerate(nodeinfo):
        info.append(idx + 1)
    
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))  # y 내림차순, x 오름차순
    
    # 첫 번째 노드를 루트로 설정
    tree = Node(nodeinfo[0])
    
    # 나머지 노드들을 트리에 추가
    for info in nodeinfo[1:]:
        add_node(tree, info)
    
    # 전위 순회와 후위 순회 결과 반환
    return [pre_order(tree), post_order(tree)]

def pre_order(node):
    """전위 순회: 루트 -> 왼쪽 서브트리 -> 오른쪽 서브트리"""
    path = [node.num]
    if node.left:
        path.extend(pre_order(node.left))
    if node.right:
        path.extend(pre_order(node.right))
    return path

def post_order(node):
    """후위 순회: 왼쪽 서브트리 -> 오른쪽 서브트리 -> 루트"""
    path = []
    if node.left:
        path.extend(post_order(node.left))
    if node.right:
        path.extend(post_order(node.right))
    path.append(node.num)
    return path

def add_node(parent, info):
    """트리에 노드를 추가하는 함수"""
    if parent.pos[0] > info[0]:  # 왼쪽 서브트리
        if parent.left:
            add_node(parent.left, info)
        else:
            parent.left = Node(info)
    else:  # 오른쪽 서브트리
        if parent.right:
            add_node(parent.right, info)
        else:
            parent.right = Node(info)


# main start!

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]		#TC no.1
print(solution(nodeinfo)) 
nodeinfo = [[5, 3], [3, 4], [7, 2], [2, 5], [6, 1]]		#TC no.2
print(solution(nodeinfo))  # [[4, 2, 1, 3, 5], [5, 3, 1, 2, 4]]
# main end!

