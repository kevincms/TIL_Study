from collections import deque

node_num=6
graph_list=[[i+1] for i in range(node_num)]

graph_list[0].append(2)
graph_list[0].append(3)

graph_list[1].append(5)
graph_list[1].append(6)

graph_list[2].append(4)

graph_list[3].append(6)

check_list=[False for _ in range(6)]

def DFS(stack=deque([0]),output_list=[],check_list=check_list):
    if len(stack)==0: return output_list
    node=stack[-1]
    stack.pop()
    output_list.append(node+1)
    check_list[node]=True

    arc_list=graph_list[node]
    arc_len=len(arc_list)
    if arc_len==1: return DFS(stack,output_list)
    else:
        for i in range(1,arc_len):
            node_index=arc_list[i]-1
            if not check_list[node_index]: stack.append(node_index)
        return DFS(stack,output_list)

start_index=0
stack=deque([start_index])
print(DFS())