# https://www.acmicpc.net/problem/2164
# 입력 :6, 출력 4 [※ 입력 :1, 출력 1]
from collections import deque

input_num=int(input())
card_queue=deque([i+1 for i in range(input_num)])

if input_num!=1:
    while(1):
        card_queue.popleft()
        if len(card_queue)==1: break
        temp=card_queue[0]
        card_queue.popleft()
        card_queue.append(temp)
print(card_queue[0])