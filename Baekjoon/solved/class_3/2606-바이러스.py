import sys
from collections import deque

def count_BFS(start):
    count=0
    record=[]
    queue=deque([start])
    record.append(start)
    while queue:
        index=queue.popleft()
        for i in com[index]:
            if not i in record:
                record.append(i)
                count+=1
                queue.append(i)
    return count

input=sys.stdin.readline
N=int(input())
com=[[] for _ in range(N+1)]
M=int(input())
for _ in range(M):
    a, b=map(int,input().split())
    com[a].append(b)
    com[b].append(a)
print(count_BFS(1))