# https://www.acmicpc.net/problem/13023

import sys
from collections import deque

input=sys.stdin.readline
people_num, friend_num=map(int,input().split())
graph_list=[[i] for i in range(people_num)]
check_list=[False for _ in range(people_num)]

def DFS(stack,output_list,check_list):
    if len(stack)==0: return output_list
    node=stack[-1]
    stack.pop()
    output_list.append(node)

    arc_list=graph_list[node]
    arc_len=len(arc_list)
    if arc_len==1: return DFS(stack.copy(),output_list[:],check_list[:])
    else:
        max_list=[]
        for i in range(1,arc_len):
            node_index=arc_list[i]
            max_len=0
            
            if not check_list[node_index]:
                stack.append(node_index)
                check_list[node_index]=True
                temp_list=DFS(stack.copy(),output_list[:],check_list[:])
                temp_len=len(temp_list)

                if temp_len>max_len:
                    max_len=temp_len
                    max_list=temp_list
                
                stack.pop()
                check_list[node_index]=False
                
        if len(stack)==0: return output_list
        return max_list

for i in range(friend_num):
    num_1, num_2=map(int,input().split())
    graph_list[num_1].append(num_2)
    graph_list[num_2].append(num_1)

check_num=0
for i in range(people_num):
    stack=deque([i])
    check_list[i]=True
    temp_list=DFS(stack.copy(),[],check_list[:])
    check_list[i]=False
    print(temp_list)
    if len(temp_list)>=5:
        check_num=1
        break
# print(temp_list)
print(check_num)

"""
6 5
0 1
0 2
0 3
0 4
0 5

5 4
0 1
1 2
2 3
3 4

5 5
0 1
1 3
1 4
4 3
3 2
"""

'''
0 1 3 4
2 3 4 1 0
'''