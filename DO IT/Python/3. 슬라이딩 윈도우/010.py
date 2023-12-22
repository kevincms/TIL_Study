# https://www.acmicpc.net/problem/11003

import sys
from collections import deque

input=sys.stdin.readline
num_count, slide_length=map(int,input().split())
num_list=list(map(int,input().split()))

slide_deque=deque([num_list[0]])
index_deque=deque([0])
output_list=[0 for _ in range(num_count)]
output_list[0]=num_list[0]

for i in range(slide_length-1):
    index=i+1
    comp_num=num_list[index]
    if slide_deque[0]>comp_num:
        slide_deque.appendleft(comp_num)
        index_deque.appendleft(index)
    else:
        while(slide_deque[-1]>comp_num):
            slide_deque.pop()
            index_deque.pop()
        slide_deque.append(comp_num)
        index_deque.append(index)
    output_list[index]=slide_deque[0]

for i in range(num_count-slide_length):
    add_index=i+slide_length
    sub_index=i
    add_num=num_list[add_index]
    sub_num=num_list[sub_index]
    while(index_deque[0]<=sub_index):
        slide_deque.popleft()
        index_deque.popleft()
    if slide_deque[0]>add_num:
        slide_deque.appendleft(add_num)
        index_deque.appendleft(add_index)
    else:
        while(slide_deque[-1]>add_num):
            slide_deque.pop()
            index_deque.pop()
        slide_deque.append(add_num)
        index_deque.append(add_index)
    output_list[add_index]=slide_deque[0]
print(*output_list)