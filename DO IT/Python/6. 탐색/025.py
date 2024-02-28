# https://www.acmicpc.net/problem/13023

import sys
from collections import deque

def DFS(graph_list, start_index):
    graph_size=len(graph_list)
    check_list=[False for _ in range(graph_size)]
    compelte_list=[]
    stack=deque()

    stack.append(graph_list[start_index][0])
    check_list[graph_list[start_index][0]-1]=True

    while(1):
        if len(stack)==0: return compelte_list

        previous_top=stack[-1]
        temp_list=graph_list[previous_top]
        compelte_list.append(previous_top)
        stack.pop()

        temp_len=len(temp_list)
        if temp_len!=1:
            for i in range(1,temp_len):
                check_node=temp_list[i]
                if check_list[check_node-1]: continue
                    # if temp_list[i] <= check_node: continue
                    # if temp_list[i] in graph_list[check_node-1][1:]: continue
                    # else: return compelte_list
                stack.append(check_node)
                check_list[temp_list[i]-1]=True
                break

input=sys.stdin.readline
people_num, friend_num=map(int,input().split())
graph_list=[[i] for i in range(people_num)]

for i in range(friend_num):
    num_1, num_2=map(int,input().split())
    graph_list[num_1].append(num_2)
    graph_list[num_2].append(num_1)

check_num=0
for i in range(people_num):
    output_list=DFS(graph_list,i)
    if len(output_list)>=4:
        check_num=1
        break
# print(output_list)
print(check_num)