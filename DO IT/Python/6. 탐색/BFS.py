from collections import deque

graph_list=[[i+1] for i in range(6)]

graph_list[0].append(2)
graph_list[0].append(3)

graph_list[1].append(5)
graph_list[1].append(6)

graph_list[2].append(4)

graph_list[3].append(6)

check_list=[False for _ in range(6)]

def BFS(graph_list, check_list):
    graph_size=len(graph_list)
    compelte_list=[]
    queue=deque()

    queue.append(graph_list[0][0])
    check_list[graph_list[0][0]-1]=True

    while(1):
        if len(queue)==0: return compelte_list, check_list

        previous_front=queue[0]
        temp_list=graph_list[previous_front-1]
        compelte_list.append(previous_front)
        queue.popleft()

        temp_len=len(temp_list)
        if temp_len!=1:
            for i in range(1,temp_len):
                check_node=temp_list[i]
                if check_list[check_node-1]: continue
                queue.append(check_node)
                check_list[temp_list[i]-1]=True


print(BFS(graph_list, check_list))
# 1 2 3 5 6 4