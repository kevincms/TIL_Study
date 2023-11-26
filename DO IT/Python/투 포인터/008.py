import sys

def two_point_search(input_num,input_list):
    start_index=0
    end_index=len(input_list)-1
    while(start_index!=input_num-1):
        if start_index==end_index: return False
        temp_sum=input_list[start_index]+input_list[end_index]
        if temp_sum==input_num: return True
        elif temp_sum>input_num: end_index=end_index-1
        else: start_index=start_index+1

input=sys.stdin.readline
input_count=int(input())
input_list=list(map(int,input().split()))
output_num=0

for i in range(input_count):
    temp_num=input_list[i]
    is_good_num=two_point_search(temp_num,input_list)
    if is_good_num: output_num=output_num+1
print(output_num)