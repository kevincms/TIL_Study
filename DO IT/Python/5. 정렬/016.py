# https://www.acmicpc.net/problem/1377

import sys

def swap(input_num1,input_num2):
    return input_num2, input_num1

input=sys.stdin.readline
num_count=int(input())
num_list=[0 for _ in range(num_count)]
for i in range(num_count):
    input_num=int(input())
    num_list[i]=[input_num,i]

sorted_list=sorted(num_list)
max_index_diff_num=-1
for i in range(num_count):
    index_diff_num=sorted_list[i][1]-i
    if index_diff_num>max_index_diff_num: max_index_diff_num=index_diff_num

print(max_index_diff_num+1)