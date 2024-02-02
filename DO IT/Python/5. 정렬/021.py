# https://www.acmicpc.net/problem/1517

def merge_list(list1,list2):
    list1_length=len(list1)
    list2_length=len(list2)
    output_list=[0 for _ in range(list1_length+list2_length)]
    list1_index=0
    list2_index=0
    output_index=0
    swap_count=0
    while(1):
        list1_num=list1[list1_index]
        list2_num=list2[list2_index]
        if list1_num>list2_num:
            swap_count=swap_count+len(list1[list1_index:])
            output_list[output_index]=list2_num
            list2_index=list2_index+1
            output_index=output_index+1
            if list2_index==list2_length:
                output_list[output_index:]=list1[list1_index:]
                return output_list, swap_count
        else:
            output_list[output_index]=list1_num
            list1_index=list1_index+1
            output_index=output_index+1
            if list1_index==list1_length:
                output_list[output_index:]=list2[list2_index:]
                return output_list, swap_count
            
def bubble_sort_count(input_list):
    output_list=[]
    swap_count=0
    while(1):
        list_length=len(input_list)
        if list_length==1: return swap_count
        for i in range(0,list_length-1,2):
            temp_list, temp_count=merge_list(input_list[i],input_list[i+1])
            output_list.append(temp_list)
            swap_count=swap_count+temp_count
        if list_length%2==1: output_list.append(input_list[list_length-1])
        input_list=output_list[:]
        output_list=[]

input_count=int(input())
temp_list=list(map(list,input().split()))
input_list=[0 for _ in range(input_count)]
for i in range(input_count): input_list[i]=[temp_list[i]]

output_count=bubble_sort_count(input_list)
print(output_count)