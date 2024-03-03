# https://www.acmicpc.net/problem/10989

import sys
from collections import deque

input=sys.stdin.readline
input_count=int(input())
max_num_=10000
max_digit=5
digit_queue_list=[deque([]) for _ in range(10)]
num_queue=deque([])

for i in range(input_count): num_queue.append(int(input()))
for i in range(max_digit):
    for j in range(input_count):
        temp=num_queue[0]
        digit_num=(temp//(10**i))%10
        num_queue.popleft()
        digit_queue_list[digit_num].append(temp)
    for j in range(10):
        temp_queue=digit_queue_list[j]
        while(len(temp_queue)!=0):
            temp=temp_queue[0]
            temp_queue.popleft()
            num_queue.append(temp)
print(*list(num_queue),sep="\n")