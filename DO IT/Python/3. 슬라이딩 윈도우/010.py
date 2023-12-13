# https://www.acmicpc.net/problem/11003

# 12 3
# 1 5 2 3 6 2 3 7 3 5 2 6
# 1 1 1 2 2 2 2 2 3 3 2 2

import sys

input=sys.stdin.readline
num_count, slide_length=map(int,input().split())
num_list=list(map(int,input().split()))

slide_min_num=[num_list[0] for _ in range(slide_length)]
output_list=[0 for _ in range(num_count)]

def min_num_sort(num_list,num):
    if num_list==[]: return []
    if num_list[0]>num:
        num_list[0]=num
        return num_list
    else: return num_list[:1]+min_num_sort(num_list[1:],num)

for i in range(slide_length):
    slide_min_num=min_num_sort(slide_min_num,num_list[i])
    output_list[i]=slide_min_num[0]

for i in range(num_count-slide_length):
    end_index=i+slide_length
    start_index=i+1
    slide_list=num_list[start_index:end_index+1]

    if not (slide_min_num in slide_list):
        slide_min_num=slide_min_num_2
        slide_min_num_2=1000000001
    elif not (slide_min_num_2 in slide_list): slide_min_num_2=1000000001
    for j in range(slide_length):
        if slide_min_num>=slide_list[j]: slide_min_num=slide_list[j]
        else:
            if slide_min_num_2>slide_list[j]: slide_min_num_2=slide_list[j]
    output_list[i+1]=slide_min_num
print(*output_list)
    