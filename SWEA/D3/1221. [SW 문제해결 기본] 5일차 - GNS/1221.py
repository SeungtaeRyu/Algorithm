import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    t, length = input().split()
    text_list = list(input().split())
    num_list = [0] * 10
    str_to_int_dict = {
        "ZRO": 0,
        "ONE": 1,
        "TWO": 2,
        "THR": 3,
        "FOR": 4,
        "FIV": 5,
        "SIX": 6,
        "SVN": 7,
        "EGT": 8,
        "NIN": 9,
    }
    int_to_str_dict = {
        0: "ZRO",
        1: "ONE",
        2: "TWO",
        3: "THR",
        4: "FOR",
        5: "FIV",
        6: "SIX",
        7: "SVN",
        8: "EGT",
        9: "NIN",
    }
    for i in range(int(length)):
        num_list[str_to_int_dict[text_list[i]]] += 1

    print(f'{t}')
    for i in range(10):
        for _ in range(num_list[i]):
            print(int_to_str_dict[i],end=" ")
    print()
