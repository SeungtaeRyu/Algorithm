import sys, heapq
input = sys.stdin.readline

start_list = []
end_list = []
for _ in range(int(input())):
    start, end = map(int, input().split())
    start_list.append(start)
    end_list.append(end)
heapq.heapify(start_list)                           # [2, 6, 3, 6, 15, 7, 12, 20]
heapq.heapify(end_list)                             # [8, 14, 13, 20, 27, 21, 18, 25]

count = 0
max_count = 0
while start_list:
    x = start_list[0]                               # 우선순위 큐인 heapq 는 [0]번째 인덱스에 최소값이 오더라
    y = end_list[0]
    if x < y:                                       # start[0]이 end[0]보다 작다? 수업이 끝나기 전에 열린다는 뜻 => 즉 강의시간이 겹침
        count += 1                                  # 현재 사용중인 강의실 count 증가시키고 start[0]을 pop
        max_count = max(count, max_count)
        heapq.heappop(start_list)
    else:                                           # start[0]이 end[0]보다 크다? 수업이 한 개 닫혔다는 뜻
        count -= 1                                  # 현재 사용중인 강의실 count 감소시키고 end[0]을 pop
        heapq.heappop(end_list)
print(max_count)                                    # count 가 증감하면서 제일 높았던 때를 출력