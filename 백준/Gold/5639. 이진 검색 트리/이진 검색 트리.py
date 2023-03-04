import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def find_subtree(n_list):
    if n_list == []:
        return

    if len(n_list) == 1:
        subtree1 = [n_list[0]]
        subtree2 = []
        subtree3 = []
    else:
        root = n_list[0]
        for i in range(1, len(n_list)):
            if n_list[i] > root:
                break

        if n_list[i] < root:
            i += 1

        subtree1 = [root]
        subtree2 = n_list[1:i]
        subtree3 = n_list[i:]

    if len(subtree2) == 1:
        print(subtree2[0])
    else:
        find_subtree(subtree2)

    if len(subtree3) == 1:
        print(subtree3[0])
    else:
        find_subtree(subtree3)

    if len(subtree1) == 1:
        print(subtree1[0])
    else:
        find_subtree(subtree1)

node_list = []
while True:
    try:
        node_list.append(int(sys.stdin.readline()))
    except:
        break

find_subtree(node_list)

