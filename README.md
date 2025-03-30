# CodingTest
1. 필수 기본 지식
1.1 자료구조 (Data Structures)
코딩 테스트에서 효율적인 문제 해결을 위해 기본적인 자료구조에 대한 이해는 필수입니다.

리스트 (List): 순서가 있고 변경 가능한 시퀀스 타입.
그림: ["apple", "banana", "cherry"] (각 요소는 순서대로 인덱스를 가짐)
핵심 연산: 삽입(append, insert), 삭제(pop, remove, del), 접근 (인덱싱), 탐색 (in, index), 정렬 (sort)
딕셔너리 (Dictionary): 키-값 쌍으로 이루어진 변경 가능한 비순서 타입.
그림: {"name": "Alice", "age": 30, "city": "New York"} (각 키는 고유하며 값에 접근하는 데 사용)
핵심 연산: 삽입 (새로운 키-값 쌍 할당), 삭제 (del, pop), 접근 (키 사용), 탐색 (in - 키 기준), 값 접근 (values), 키 접근 (keys)
집합 (Set): 순서가 없고 중복된 요소를 허용하지 않는 변경 가능한 타입.
그림: {"apple", "banana", "cherry"} (요소의 순서는 중요하지 않고 중복은 제거됨)
핵심 연산: 삽입 (add), 삭제 (remove, discard), 탐색 (in), 합집합 (union, |), 교집합 (intersection, &), 차집합 (difference, -)
튜플 (Tuple): 순서가 있고 변경 불가능한 시퀀스 타입. (주로 여러 값을 묶어서 반환하거나 불변성을 유지하고 싶을 때 사용)
그림: ("apple", "banana", "cherry") (리스트와 유사하지만 내용 변경 불가)
큐 (Queue): FIFO (First-In, First-Out) 원칙을 따르는 자료구조.
그림: front -> [item1, item2, item3] -> rear (먼저 들어온 요소가 먼저 나감)
구현: collections.deque를 사용하여 효율적으로 구현. append (enqueue), popleft (dequeue)
스택 (Stack): LIFO (Last-In, First-Out) 원칙을 따르는 자료구조.
그림: top -> [item3, item2, item1] (가장 최근에 들어온 요소가 가장 먼저 나감)
구현: 파이썬 리스트를 사용하여 구현. append (push), pop (pop)
1.2 알고리즘 (Algorithms)
자주 출제되는 기본적인 알고리즘 패턴을 익혀야 합니다.

정렬 (Sorting): 데이터를 특정 순서대로 배열하는 알고리즘.
그림: Unsorted: [3, 1, 4, 1, 5, 9, 2, 6] -> Sorted: [1, 1, 2, 3, 4, 5, 6, 9]
핵심: sort() (리스트 내장 함수), sorted() (내장 함수), 병합 정렬, 퀵 정렬의 기본 개념 이해 (시간 복잡도 중요)
탐색 (Searching): 특정 데이터를 찾는 알고리즘.
선형 탐색: 리스트의 처음부터 끝까지 순차적으로 탐색.
그림: List: [2, 5, 8, 1, 9], Target: 8 (화살표로 순서대로 가리키는 모습)
이진 탐색: 정렬된 리스트에서 탐색 범위를 절반씩 줄여가며 탐색 (효율적).
그림: Sorted List: [1, 3, 5, 7, 9, 11], Target: 7 (탐색 범위가 절반씩 줄어드는 모습)
재귀 (Recursion): 함수가 자기 자신을 호출하는 방식.
그림: 함수 A가 자신을 다시 호출하는 화살표 그림 (종료 조건 필수)
핵심: 종료 조건 명확히 설정, 스택 오버플로우 주의
완전 탐색 (Brute Force): 가능한 모든 경우의 수를 탐색하여 해답을 찾는 방식.
그림: 모든 선택지를 나뭇가지처럼 펼쳐놓고 탐색하는 모습
핵심: 시간 복잡도 고려, 제약 조건 확인 후 적용 여부 결정
탐욕 알고리즘 (Greedy Algorithm): 각 단계에서 가장 최적인 선택을 하여 최종적으로 전체적인 최적 해답을 얻으려고 시도하는 방식.
그림: 각 단계에서 '최고'의 이익을 선택하는 손 그림
핵심: 각 단계의 최적 선택이 전체 최적을 보장하는지 증명 필요
2. 문제 유형별 풀이 전략 및 Use Case
2.1 배열 (Array)
활용 지식: 리스트, 반복문, 조건문
일반적인 유형: 배열 탐색, 조건에 맞는 요소 찾기, 배열 변형, 정렬 활용
Use Case:
문제: 주어진 배열에서 특정 값의 모든 인덱스를 찾으세요.
풀이: 반복문을 사용하여 배열의 각 요소를 확인하고, 특정 값과 일치하는 경우 해당 인덱스를 결과 리스트에 추가합니다.
Python Code:
\ python def find_all_indices(arr, target): indices = [] for i, num in enumerate(arr): if num == target: indices.append(i) return indices \
2.2 문자열 (String)
활용 지식: 문자열 메서드, 슬라이싱, 반복문
일반적인 유형: 문자열 조작, 패턴 매칭, 회문(Palindrome) 확인
Use Case:
문제: 주어진 문자열이 회문인지 확인하세요. (앞뒤로 읽어도 같은 문자열)
풀이: 문자열을 뒤집은 후 원래 문자열과 비교하거나, 양 끝에서 가운데로 이동하며 문자를 비교합니다.
Python Code:
\ python def is_palindrome(s): s = s.lower() return s == s[::-1] \
2.3 탐색 (Search)
활용 지식: 선형 탐색, 이진 탐색
일반적인 유형: 특정 값 존재 여부 확인, 특정 조건을 만족하는 값 찾기
Use Case:
문제: 정렬된 배열에서 특정 값의 존재 여부를 효율적으로 확인하세요.
풀이: 이진 탐색 알고리즘을 사용하여 탐색 범위를 절반씩 줄여나갑니다.
Python Code:
\ python def binary_search(arr, target): left, right = 0, len(arr) - 1 while left <= right: mid = (left + right) // 2 if arr(mid) == target: return True elif arr(mid) < target: left = mid + 1 else: right = mid - 1 return False \
2.4 스택/큐 (Stack/Queue)
활용 지식: collections.deque (큐), 리스트 (스택)
일반적인 유형: 괄호 검사, 작업 처리 순서 관리, 그래프 탐색 (BFS)
Use Case (스택):
문제: 주어진 문자열의 괄호 쌍이 올바르게 매칭되었는지 확인하세요.
풀이: 여는 괄호를 만나면 스택에 push, 닫는 괄호를 만나면 스택에서 pop하여 짝이 맞는지 확인합니다.
Python Code:
\ python def is_valid_parentheses(s): stack = [] mapping = {")": "(", "}": "{", "]": "["} for char in s: if char in mapping: top_element = stack.pop() if stack else '#' if mapping(char) != top_element: return False else: stack.append(char) return not stack \
Use Case (큐):
문제: 그래프에서 너비 우선 탐색(BFS)을 구현하세요.
풀이: 시작 노드를 큐에 넣고, 큐가 빌 때까지 노드를 dequeue하고 방문하지 않은 인접 노드를 enqueue합니다.
2.5 해시 (Hash)
활용 지식: 딕셔너리, 집합
일반적인 유형: 빠른 검색, 빈도수 계산, 중복 요소 제거
Use Case:
문제: 주어진 배열에서 각 숫자의 빈도수를 계산하세요.
풀이: 딕셔너리를 사용하여 각 숫자를 키로 하고, 등장 횟수를 값으로 저장합니다.
Python Code:
\ python def count_frequency(arr): frequency = {} for num in arr: frequency(num) = frequency.get(num, 0) + 1 return frequency \
2.6 재귀 (Recursion)
활용 지식: 함수 정의 및 호출, 종료 조건
일반적인 유형: 트리 순회, 팩토리얼 계산, 분할 정복
Use Case:
문제: 이진 트리의 전위 순회를 재귀적으로 구현하세요.
풀이: 현재 노드를 방문하고, 왼쪽 서브트리를 재귀적으로 순회한 다음, 오른쪽 서브트리를 재귀적으로 순회합니다.
Python Code:
\ ```python
class TreeNode:
def init(self, val=0, left=None, right=None):
self.val = val
self.left = left
self.right = right
def preorder_traversal(root):
result = []
def traverse(node):
if node:
result.append(node.val)
traverse(node.left)
traverse(node.right)
traverse(root)
return result
\ ```
2.7 정렬 (Sorting)
활용 지식: sort(), sorted()
일반적인 유형: 배열 정렬 후 특정 조건 만족하는 요소 찾기, 두 배열 병합
Use Case:
문제: 두 개의 정렬된 배열을 하나의 정렬된 배열로 합치세요.
풀이: 투 포인터 방식을 사용하여 각 배열의 요소를 비교하며 새로운 배열에 추가합니다.
Python Code:
\ python def merge_sorted_arrays(arr1, arr2): merged = [] i, j = 0, 0 while i < len(arr1) and j < len(arr2): if arr1(i) <= arr2(j): merged.append(arr1(i)) i += 1 else: merged.append(arr2(j)) j += 1 while i < len(arr1): merged.append(arr1(i)) i += 1 while j < len(arr2): merged.append(arr2(j)) j += 1 return merged \