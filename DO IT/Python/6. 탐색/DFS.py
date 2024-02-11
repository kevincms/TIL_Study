from collections import deque

graph_list=[[i+1] for i in range(6)]

graph_list[0].append(2)
graph_list[0].append(3)

graph_list[1].append(5)
graph_list[1].append(6)

graph_list[2].append(4)

graph_list[3].append(6)

check_list=[False for _ in range(6)]

def DFS(graph_list, check_list):
    graph_size=len(graph_list)
    compelte_list=[]
    stack=deque()

    stack.append(graph_list[0][0])
    check_list[graph_list[0][0]-1]=True

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


print(DFS(graph_list, check_list))