# https://www.acmicpc.net/problem/11003

import sys
from collections import deque

input=sys.stdin.readline
num_count, slide_length=map(int,input().split())
num_list=list(map(int,input().split()))

slide_deque=deque([num_list[0]])
output_list=[0 for _ in range(num_count)]
output_list[0]=num_list[0]

for i in range(slide_length-1):
    comp_num=num_list[i+1]
    if slide_deque[0]>comp_num: slide_deque.appendleft(comp_num)
    else:
        while(slide_deque[-1]>comp_num): slide_deque.pop()
        slide_deque.append(comp_num)
    output_list[i+1]=slide_deque[0]

for i in range(num_count-slide_length):
    add_index=i+slide_length
    sub_index=i
    add_num=num_list[add_index]
    sub_num=num_list[sub_index]
    try: slide_deque.remove(sub_num)
    except: pass
    if slide_deque[0]>add_num: slide_deque.appendleft(add_num)
    else:
        while(slide_deque[-1]>add_num): slide_deque.pop()
        slide_deque.append(add_num)
    output_list[add_index]=slide_deque[0]
print(*output_list)