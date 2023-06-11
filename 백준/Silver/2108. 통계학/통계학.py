import sys
from collections import Counter

n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))

#산술평균
print(round(sum(a)/n))      #round() => 반올림 하는 함수

#중앙값
print(sorted(a)[len(a)//2]) 

#최빈값
count = Counter(a)           #collection 모듈 사용 / Counter() -> 빈도수 구해주는 함수
order = count.most_common()  #딕셔너리 형태로 수와 빈도수가 저장된 배열
max_frequency = order[0][1]  #최대 빈도수

fq = []                      #최대 빈도수를 가진 수들을 저장하는 리스트
for i in order:
    if i[1] == max_frequency: #i[1] => 각 수의 빈도수임. 이것이 최대 빈도수라면
        fq.append(i[0])       #fq 리스트에 해당 숫자를 추가
        
if len(fq) == 1:              #만약 최대빈도수를 가진 수가 1개라면
    print(fq[0])              #첫번째 숫자 출력
else:
    print(sorted(fq)[1])      #1개가 아니라면 정렬 후 두번째 인덱스 출력

#범위
print(max(a)-min(a))