# https://www.acmicpc.net/problem/11724

import sys
from collections import deque

def DFS(graph_list, check_list, start_index):
    graph_size=len(graph_list)
    compelte_list=[]
    stack=deque()
    start_index=start_index

    temp_list=graph_list[start_index]
    stack.append(temp_list[0])
    check_list[temp_list[0]-1]=True

    while(1):
        if len(stack)==0: return compelte_list, check_list

        previous_top=stack[-1]
        temp_list=graph_list[previous_top-1]
        compelte_list.append(previous_top)
        stack.pop()

        temp_len=len(temp_list)
        if temp_len!=1:
            for i in range(1,temp_len):
                check_node=temp_list[i]
                if check_list[check_node-1]: continue
                stack.append(check_node)
                check_list[temp_list[i]-1]=True
        while(1):
            if start_index==graph_size-1: break
            if not(check_list[start_index]): break
            start_index+=1

input=sys.stdin.readline
point, link=map(int,input().split())
check_list=[False for _ in range(point)]
graph_list=[[i+1] for i in range(point)]
Con_Cpm_count=0
for i in range(link):
    point_1, point_2=map(int,input().split())
    graph_list[point_1-1].append(point_2)
    graph_list[point_2-1].append(point_1)

start_index=0
while(1):
    temp_list, check_list=DFS(graph_list,check_list,start_index)
    Con_Cpm_count+=1
    if not(False in check_list): break
    start_index=check_list.index(False)

print(Con_Cpm_count)