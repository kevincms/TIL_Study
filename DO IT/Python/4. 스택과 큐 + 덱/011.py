# https://www.acmicpc.net/problem/1874

import sys
from collections import deque

input=sys.stdin.readline
input_count=int(input())
stack=deque([])
queue=deque([i+1 for i in range(input_count)])
sequence_check=True
output_queue=deque([])
 
for i in range(input_count):
    input_num=int(input())
    if len(stack)==0:
        stack.append(queue[0])
        queue.popleft()
        output_queue.append("+")
    while(input_num>stack[-1]):
        if len(queue)==0:
            sequence_check=False
            break
        else:
            stack.append(queue[0])
            queue.popleft()
            output_queue.append("+")
    if not(sequence_check): break
    elif input_num==stack[-1]:
        stack.pop()
        output_queue.append("-")
    elif input_num<stack[-1]:
        sequence_check=False
        break

if sequence_check: print(*output_queue,sep="\n")
else: print("NO")
