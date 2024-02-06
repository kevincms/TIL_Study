# https://www.acmicpc.net/problem/10989
import sys

input=sys.stdin.readline
input_count=int(input())
num_list=[0 for _ in range(input_count+1)]

for i in range(input_count):
    input_num=int(input())
    num_list[input_num]=num_list[input_num]+1
for i in range(input_count):
    num=i+1
    temp_num=num_list[num]
    if temp_num: 
        for _ in range(temp_num): print(num)
