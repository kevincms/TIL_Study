import sys
from collections import deque

def count_DFS(start):
    if visited[start]: return 0
    visited[start]=True
    count=0
    for i in com[start]:
        if not visited[i]: count+=count_DFS(i)+1
    return count

input=sys.stdin.readline
N=int(input())
com=[[] for _ in range(N+1)]
visited=[False]*(N+1)
M=int(input())
for _ in range(M):
    a, b=map(int,input().split())
    com[a].append(b)
    com[b].append(a)
print(count_DFS(1))

'''
- BFS queue로 구현
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

'''