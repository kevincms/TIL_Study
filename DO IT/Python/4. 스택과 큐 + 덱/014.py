# https://www.acmicpc.net/problem/11286

import sys
from queue import PriorityQueue

input=sys.stdin.readline
cal_num=int(input())
heap_queue=PriorityQueue()
before_sort_check=False

for i in range(cal_num):
    input_num=int(input())
    if input_num==0:
        if heap_queue.empty(): print("0")
        else: print(heap_queue.get()[1])
    else: heap_queue.put([abs(input_num),input_num])