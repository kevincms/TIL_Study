# https://www.acmicpc.net/problem/17298

import sys
from collections import deque

input=sys.stdin.readline
input_count=int(input())
num_list=list(map(int,input().split()))
num_stack=deque(num_list)

bigger_stack=deque([])
ouput_list=[-1 for _ in range(input_count)]

for i in range(input_count):
    output_index=input_count-1-i
    if len(bigger_stack)==0: ouput_list[output_index]=-1
    elif num_stack[-1]<bigger_stack[-1]: ouput_list[output_index]=bigger_stack[-1]
    else:
        while(num_stack[-1]>bigger_stack[-1]):
            bigger_stack.pop()
            if len(bigger_stack)==0: break
        if len(bigger_stack)==0: ouput_list[output_index]=-1
        else: ouput_list[output_index]=bigger_stack[-1]

    temp=num_stack.pop()
    if len(bigger_stack)==0: bigger_stack.append(temp)
    else:
        while(temp>bigger_stack[-1]):
            bigger_stack.pop()
            if len(bigger_stack)==0: break
        bigger_stack.append(temp)
print(*ouput_list)