# https://www.acmicpc.net/problem/1517

from collections import deque

num_count=int(input())
num_queue=deque(map(int,input().split()))
count_stack=deque([])

output_count=0
for i in range(num_count):
    if len(count_stack)==0:
        count_stack.append(num_queue[0])
        num_queue.popleft()
    else:
        while(count_stack[-1]<num_queue[0]):
            count_stack.pop()
            if len(count_stack)==0: break
        output_count=output_count+len(count_stack)
        count_stack.append(num_queue[0])
        num_queue.popleft()
        
print(output_count)