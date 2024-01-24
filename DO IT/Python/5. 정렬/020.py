# https://www.acmicpc.net/problem/2751

def merge(list1,list2):
    list1_length=len(list1)
    list2_length=len(list2)
    output_list=[0 for _ in range(list1_length+list2_length)]
    list1_index=0
    list2_index=0
    output_index=0
    while(1):
        list1_num=list1[list1_index]
        list2_num=list2[list2_index]
        if list1_num>=list2_num:
            output_list[output_index]=list2_num
            list2_index=list2_index+1
            output_index=output_index+1
            if list2_index==list2_length:
                output_list[output_index:]=list1[list1_index:]
                return output_list
        else:
            output_list[output_index]=list1_num
            list1_index=list1_index+1
            output_index=output_index+1
            if list1_index==list1_length:
                output_list[output_index:]=list2[list2_index:]
                return output_list

import sys

input=sys.stdin.readline
input_count=int(input())
sort_list=[]
temp_num=0
before_check=False

if input_count%2==0:
    for i in range(input_count):
        input_num=int(input())
        if before_check:
            before_check=False
            if input_num>=temp_num: sort_list.append([temp_num,input_num])
            else: sort_list.append([input_num,temp_num])
        else:
            temp_num=input_num
            before_check=True
else:
    for i in range(input_count-1):
        input_num=int(input())
        if before_check:
            before_check=False
            if input_num>=temp_num: sort_list.append([temp_num,input_num])
            else: sort_list.append([input_num,temp_num])
        else:
            temp_num=input_num
            before_check=True
    sort_list.append([int(input())])

output_list=[]
while(1):
    list_length=len(sort_list)
    if list_length==1: break
    for i in range(0,list_length-1,2): output_list.append(merge(sort_list[i],sort_list[i+1]))
    if list_length%2==1: output_list.append(sort_list[list_length-1])
    sort_list=output_list[:]
    output_list=[]
    
for i in range(input_count): print(sort_list[0][i])