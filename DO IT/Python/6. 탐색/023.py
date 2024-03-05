# https://www.acmicpc.net/problem/11724

import sys
from collections import deque

input=sys.stdin.readline
point, arc=map(int,input().split())
check_list=[False for _ in range(point+1)]
check_list[0]=True
graph_list=[[] for i in range(point+1)]
output_list=[]
Con_Cpm_count=0

def DFS(index=1):
    if index in output_list: return
    temp=graph_list[index]
    output_list.append(index)
    check_list[index]=True
    if temp:    
        for i in range(len(temp)):
            temp_index=temp[i]
            if not check_list[temp_index]: DFS(temp_index)
    return 

for i in range(arc):
    point_1, point_2=map(int,input().split())
    graph_list[point_1].append(point_2)
    graph_list[point_2].append(point_1)

start_index=1
while(1):
    output_list=[]
    DFS(start_index)
    Con_Cpm_count+=1
    if not(False in check_list): break
    start_index=check_list.index(False)

print(Con_Cpm_count)

"""
6 5
1 2
2 5
5 1
3 4
4 6
"""