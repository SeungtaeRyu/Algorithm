import sys
input = sys.stdin.readline
R, C =map(int,input().split())
Map=sum( [list(map(lambda x: 1<<(ord(x)-65), input()[:-1])) for i in range(R)],[])

pos=0
vis=Map[0]
stack=[(pos,vis,1)]
Max=1
while stack:
    pos,vis,ac=stack.pop()
    Max=max(Max,ac)

    if pos%C>0 and not(vis & Map[pos-1]):
        stack.append( (pos-1, vis|Map[pos-1],ac+1))

    if pos%C<C-1 and not(vis & Map[pos+1]):
        stack.append( (pos+1, vis|Map[pos+1],ac+1))

    if pos//C>0 and not(vis & Map[pos-C]):
        stack.append( (pos-C, vis|Map[pos-C],ac+1))

    if pos//C<R-1 and not(vis & Map[pos+C]):
        stack.append(( pos+C, vis|Map[pos+C],ac+1))
print(Max)
