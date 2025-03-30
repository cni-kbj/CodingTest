from sys import setrecursionlimit
setrecursionlimit(10000)  # 깊은 재귀 처리를 위해 제한 증가

class TreeNode:
    def __init__(self, data):
        self.node_id = data[2]  # 노드 번호
        self.coordinates = data[:2]  # [x, y] 좌표
        self.left_child = None  # 왼쪽 서브트리
        self.right_child = None  # 오른쪽 서브트리

def build_binary_tree(node_data):
    # 각 노드에 번호를 추가하고 y값 내림차순, x값 오름차순으로 정렬
    for index, data in enumerate(node_data):
        data.append(index + 1)
    node_data.sort(key=lambda n: (-n[1], n[0]))
    
    # 첫 번째 노드를 루트로 설정
    root_node = TreeNode(node_data[0])
    
    # 나머지 노드를 트리에 추가
    for data in node_data[1:]:
        insert_node(root_node, data)
    
    # 전위 순회 및 후위 순회 수행
    return [preorder_traversal(root_node), postorder_traversal(root_node)]

def insert_node(parent_node, new_data):
    """ 이진트리에 새로운 노드를 추가하는 함수 """
    if parent_node.coordinates[0] > new_data[0]:  # 왼쪽 서브트리로 배치
        if parent_node.left_child:
            insert_node(parent_node.left_child, new_data)
        else:
            parent_node.left_child = TreeNode(new_data)
    else:  # 오른쪽 서브트리로 배치
        if parent_node.right_child:
            insert_node(parent_node.right_child, new_data)
        else:
            parent_node.right_child = TreeNode(new_data)

def preorder_traversal(current_node):
    """ 전위 순회: 루트 -> 왼쪽 -> 오른쪽 """
    traversal_path = []
    if current_node:
        traversal_path.append(current_node.node_id)
        traversal_path += preorder_traversal(current_node.left_child)
        traversal_path += preorder_traversal(current_node.right_child)
    return traversal_path

def postorder_traversal(current_node):
    """ 후위 순회: 왼쪽 -> 오른쪽 -> 루트 """
    traversal_path = []
    if current_node:
        traversal_path += postorder_traversal(current_node.left_child)
        traversal_path += postorder_traversal(current_node.right_child)
        traversal_path.append(current_node.node_id)
    return traversal_path

def solution(nodeinfo):
    return build_binary_tree(nodeinfo)
# main start!

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]		#TC no.1
print(solution(nodeinfo)) 
nodeinfo = [[5, 3], [3, 4], [7, 2], [2, 5], [6, 1]]		#TC no.2
print(solution(nodeinfo))  # [[4, 2, 1, 3, 5], [5, 3, 1, 2, 4]]
# main end!

