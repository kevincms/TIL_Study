# https://www.acmicpc.net/problem/11724

import sys

sys.setrecursionlimit(1001)
input=sys.stdin.readline
node, edge=map(int,input().split())
check_list=[False for _ in range(node+1)]
graph_list=[[] for i in range(node+1)]
count=0

def DFS(index):
    if check_list[index]: return
    check_list[index]=True
    for i in graph_list[index]:
        if not check_list[i]: DFS(i)        

for i in range(edge):
    node1, node2=map(int,input().split())
    graph_list[node1].append(node2)
    graph_list[node2].append(node1)
for i in range(node):
    if not check_list[i+1]:
        DFS(i+1)
        count+=1

print(count)

"""
6 5
1 2
2 5
5 1
3 4
4 6
"""