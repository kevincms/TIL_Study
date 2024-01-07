# https://www.acmicpc.net/problem/2750

import sys

def swap(input_num1,input_num2):
    return input_num2, input_num1

input=sys.stdin.readline
num_count=int(input())
num_list=[0 for _ in range(num_count)]
for i in range(num_count): num_list[i]=int(input())
for i in range(num_count-1):
    for j in range(num_count-i-1):
        front_num=num_list[j]
        back_num=num_list[j+1]
        if front_num>back_num: num_list[j], num_list[j+1]=swap(front_num,back_num)
for i in range(num_count): print(num_list[i])