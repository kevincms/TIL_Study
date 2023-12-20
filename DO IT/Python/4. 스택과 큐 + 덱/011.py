# https://www.acmicpc.net/problem/1874

import sys
from collections import deque

input=sys.stdin.readline
input_count=int(input())
stack=deque([1])
push_count=0
sequence_check=True
output_queue=deque([])
 
for i in range(input_count):
    input_num=int(input())
    while(input_num>stack[-1]):
        stack.append(stack[-1]+1)
        push_count=push_count+1
        output_queue.append("+")
    if input_num==stack[-1]:
        stack.pop()
        output_queue.append("-")
    if push_count>input_count:
        sequence_check=False
        break

if sequence_check: print(*output_queue,sep="\n")
else: print("NO")
