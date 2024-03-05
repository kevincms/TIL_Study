from collections import deque

node_num=6
graph_list=[[] for i in range(node_num+1)]

graph_list[1].append(2)
graph_list[1].append(3)

graph_list[2].append(5)
graph_list[2].append(6)

graph_list[3].append(4)

graph_list[4].append(6)

check_list=[False for _ in range(node_num+1)]
output_list=[]

def DFS(index=1):
    temp=graph_list[index]
    output_list.append(index)
    check_list[index]=True
    if temp:    
        for i in range(len(temp)):
            temp_index=temp[i]
            if not check_list[temp_index]: DFS(temp_index)
                
    

DFS()
print(output_list)