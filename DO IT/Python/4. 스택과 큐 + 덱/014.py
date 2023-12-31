# https://www.acmicpc.net/problem/11286

import sys

input=sys.stdin.readline
cal_num=int(input())
heap_list=[]
before_sort_check=False

for i in range(cal_num):
    input_num=int(input())
    if input_num==0:
        if heap_list:
            heap_list.sort(reverse=True)
            print(heap_list.pop()[1])
        else: print("0")
    else: heap_list.append([abs(input_num),input_num])