from collections import deque

class Node:                                     # 노드 클래스 정의
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def get_postfix(v):                             # 후위 표기식 구하기
    if tree[v].left_node != -1:                 # postorder 기법(LRV)을 사용하여 postfix 에 저장
        get_postfix(tree[v].left_node)
    if tree[v].right_node != -1:                # 자식이 있으면 재귀식으로 더 탐색
        get_postfix(tree[v].right_node)         # 자식이 있는지 없는지??
    postfix.append(tree[v].data)                # -> tree[left_node or right_node] = -1일 때

def calculator(postfix):                        # 후위 표기식 계산
    num_stack = []
    while postfix:
        x = postfix.popleft()
        if x.isdigit():
            num_stack.append(int(x))
        else:
            if x == '-':
                num_stack.append(- num_stack.pop() + num_stack.pop())
            elif x == '+':
                num_stack.append(num_stack.pop() + num_stack.pop())
            elif x == '*':
                num_stack.append(num_stack.pop() * num_stack.pop())
            elif x == '/':
                num_stack.append(1 / num_stack.pop() * num_stack.pop())
    return int(num_stack.pop())                 # 계산이 끝나면 num_stack 에 계산 결과 하나가 남아 있다


for tc in range(1, 11):
    n = int(input())

    tree = {}
    for i in range(1, n+1):                     # 트리 구조 Node Class를 사용하여 저장
        data = list(input().split())
        if data[1].isdigit():
            tree[i] = Node(data[1], -1, -1)     # 자식이 없다면 -1,-1을 할당
        else:
            tree[i] = Node(data[1], int(data[2]), int(data[3]))

    postfix = deque()       # 후위 표기식 빈 리스트로 초기화
    get_postfix(1)          # 후위 표기식 저장 완료

    print(f'#{tc} {calculator(postfix)}')