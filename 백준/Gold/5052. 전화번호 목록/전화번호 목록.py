import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

def insert(string):
    global flag
    current_node = root

    for char in string:
        if char not in current_node.children:
            if current_node.data:
                flag = False
            current_node.children[char] = Node(char)
        current_node = current_node.children[char]
    current_node.data = string

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = []

    root = Node("head")
    flag = True

    for i in range(n):
        num = input().rstrip()
        nums.append(num)

    nums.sort(key=lambda x: len(x))

    for num in nums:
        insert(num)

    if flag:
        print("YES")
    else:
        print("NO")
