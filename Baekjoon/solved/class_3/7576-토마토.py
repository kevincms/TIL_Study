import sys
from collections import deque

input = sys.stdin.readline
M, N = map(int, input().split())
box = [[] for _ in range(N+1)]
box[0] = [-2]*(M+1)
for i in range(N): box[i+1] = [-2]+list(map(int, input().split()))
blank=0
start_tomato=deque([])

for i in range(N):
    for j in range(M):
        if box[i+1][j+1]==-1: blank+=1
        elif box[i+1][j+1]==1: start_tomato.append((i+1,j+1))

directions = [(0,1),(0,-1),(1,0),(-1,0)]
date=0
prev=len(start_tomato)
max=N*M-blank
while prev!=max:
    count=0
    temp=len(start_tomato)
    for _ in range(temp):
        i,j=start_tomato.popleft()
        for dx, dy in directions:
            ni, nj=i+dx, j+dy
            if 1<=ni<=N and 1<=nj<=M and box[ni][nj]==0:
                count+=1
                box[ni][nj]=1
                start_tomato.append((ni,nj))
    if not count: break
    prev+=count
    date+=1

if prev==max: print(date)
else: print(-1)

''' graph 리스트 따로 만들어 구현함.
import sys
from collections import deque

def num_to_index(num,M): return (num-1)//M+1,((num-1)%M)+1
def index_to_num(i,j,M): return ((i-1)*M)+j

input = sys.stdin.readline
M, N = map(int, input().split())
boxes=N*M
box = [[] for _ in range(N+1)]
box[0] = [-2]*(M+1)
for i in range(N): box[i+1] = [-2]+list(map(int, input().split()))
box_graph=[[] for _ in range(boxes+1)]
start_tomato=deque([])
count=0
date=0
blank=0
record=[]
for i in range(N):
    for j in range(M):
        if box[i+1][j+1]==-1: blank+=1
        else:
            tomato=index_to_num(i+1,j+1,M)
            if box[i+1][j+1]==1:
                start_tomato.append(tomato)
                record.append(tomato)
            if 1<=j<=M: box_graph[tomato].append(tomato-1)
            if 1<=j+2<=M: box_graph[tomato].append(tomato+1)
            if 1<=i<=N: box_graph[tomato].append(tomato-M)
            if 1<=i+2<=N: box_graph[tomato].append(tomato+M)

prev=len(record)
max=boxes-blank
while prev!=max:
    temp=len(start_tomato)
    for _ in range(temp):
        i=start_tomato.popleft()
        for j in box_graph[i]:
            ni, nj=num_to_index(j,M)
            if box[ni][nj]==0: 
                box[ni][nj]=1
                start_tomato.append(j)
                record.append(j)
    temp=len(record)
    if temp==prev: break
    prev=temp
    date+=1
if prev==max: print(date)
else: print(-1)
'''