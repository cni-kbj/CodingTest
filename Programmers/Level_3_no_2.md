문제 설명

루트 노드가 설정되지 않은 1개 이상의 트리가 있습니다. 즉, 포레스트가 있습니다.
모든 노드들은 서로 다른 번호를 가지고 있습니다.
각 노드는 홀수 노드, 짝수 노드, 역홀수 노드, 역짝수 노드 중 하나입니다. 각 노드의 정의는 다음과 같으며, 0은 짝수입니다.
홀수 노드
노드의 번호가 홀수이며 자식 노드의 개수가 홀수인 노드입니다.
짝수 노드
노드의 번호가 짝수이며 자식 노드의 개수가 짝수인 노드입니다.
역홀수 노드
노드의 번호가 홀수이며 자식 노드의 개수가 짝수인 노드입니다.
역짝수 노드
노드의 번호가 짝수이며 자식 노드의 개수가 홀수인 노드입니다.
당신은 각 트리에 대해 루트 노드를 설정했을 때, 홀짝 트리가 될 수 있는 트리의 개수와 역홀짝 트리가 될 수 있는 트리의 개수를 구하려고 합니다. 각 트리의 정의는 다음과 같습니다.
홀짝 트리
홀수 노드와 짝수 노드로만 이루어진 트리입니다.
역홀짝 트리
역홀수 노드와 역짝수 노드로만 이루어진 트리입니다.
다음은 트리의 루트 노드를 설정하는 예시입니다.
다음과 같은 트리가 있습니다.
무제.drawio (1).png
위 트리의 루트 노드를 3번 노드로 설정하게 되면 다음과 같은 형태가 됩니다.
무제.drawio \(7\).png
노란색 노드는 홀수 노드 혹은 짝수 노드를 나타내고, 빨간색 노드는 역홀수 노드 혹은 역짝수 노드를 나타냅니다. 이 경우, 모든 노드가 노란색이므로 홀짝 트리가 됩니다.
이 트리의 루트 노드를 6번 노드로 설정하게 되면 다음과 같은 형태가 되어 홀짝 트리 혹은 역홀짝 트리가 될 수 없습니다.
무제.drawio \(6\).png
이와 마찬가지로 다른 노드를 루트 노드로 설정하는 경우에는 홀짝 트리 혹은 역홀짝 트리가 될 수 없습니다.
3번 노드를 루트 노드로 설정하는 경우에만 홀짝 트리가 될 수 있습니다. 따라서 위 트리는 홀짝 트리가 될 수 있는 트리입니다.
다음은 어떤 노드를 루트 노드로 설정하더라도 홀짝 트리 혹은 역홀짝 트리가 될 수 없는 트리입니다.
무제.drawio \(4\).drawio \(1\).png
즉, 트리는 어떤 노드를 루트 노드로 설정하냐에 따라 홀짝 트리 혹은 역홀짝 트리가 될 수 있습니다. 경우에 따라 하나의 트리가 홀짝 트리와 역홀짝 트리 두 가지 모두 될 수 있거나 두 가지 모두 될 수 없을 수도 있습니다.
포레스트에 존재하는 노드들의 번호를 담은 1차원 정수 배열 nodes, 포레스트에 존재하는 간선들의 정보를 담은 2차원 정수 배열 edges가 매개변수로 주어집니다. 이때, 홀짝 트리가 될 수 있는 트리의 개수와 역홀짝 트리가 될 수 있는 트리의 개수를 1차원 정수 배열에 순서대로 담아 return 하도록 solution 함수를 완성해 주세요.
제한사항
1 ≤ nodes의 길이 ≤ 400,000
1 ≤ nodes의 원소 ≤ 1,000,000
nodes의 원소는 중복되지 않습니다.
1 ≤ edges의 길이 ≤ 1,000,000
edges의 원소는 [a, b] 형태의 1차원 정수 배열이며, a번 노드와 b번 노드 사이에 무방향 간선이 존재한다는 것을 의미합니다.
a, b는 nodes에 존재하는 원소이며 서로 다릅니다.
포레스트인 경우만 입력으로 주어집니다.
테스트 케이스 구성 안내
아래는 테스트 케이스 구성을 나타냅니다. 각 그룹 내의 테스트 케이스를 모두 통과하면 해당 그룹에 할당된 점수를 획득할 수 있습니다.
그룹	총점	추가 제한 사항
#1	10%	하나의 트리만 주어집니다. nodes의 길이 ≤ 1,000, edges의 길이 ≤ 1,000
#2	10%	nodes의 길이 ≤ 1,000, edges의 길이 ≤ 1,000
#3	30%	하나의 트리만 주어집니다.
#4	50%	추가 제한 사항 없음
입출력 예
nodes	edges	result
[11, 9, 3, 2, 4, 6]	[[9, 11], [2, 3], [6, 3], [3, 4]]	[1, 0]
[9, 15, 14, 7, 6, 1, 2, 4, 5, 11, 8, 10]	[[5, 14], [1, 4], [9, 11], [2, 15], [2, 5], [9, 7], [8, 1], [6, 4]]	[2, 1]
입출력 예 설명
입출력 예 #1
문제의 예시와 같습니다.
홀짝 트리가 될 수 있는 트리가 하나 존재하고, 역홀짝 트리가 될 수 있는 트리는 존재하지 않습니다.
따라서 [1, 0]을 return 해야 합니다.
입출력 예 #2
주어진 포레스트를 그림으로 나타내면 다음과 같습니다.
무제.drawio (5).png
1, 3번째 트리는 각각 10번 노드, 4번 노드를 루트 노드로 설정하면 홀짝 트리가 될 수 있고, 2번째 트리는 9번 노드를 루트 노드로 설정하면 역홀짝 트리가 될 수 있습니다.
4번째 트리는 어떤 노드를 루트 노드로 설정해도 홀짝 트리 혹은 역홀짝 트리가 될 수 없습니다.
따라서 [2, 1]을 return 해야 합니다.