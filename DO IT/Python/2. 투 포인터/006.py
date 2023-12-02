# https://www.acmicpc.net/problem/2018
# 입력 :15, 출력 4
input_num=int(input())

start_index=1
end_index=1
temp_sum=0

output_count=0
while(start_index!=input_num-1):
    if start_index==end_index: temp_sum=end_index
    else: temp_sum=(start_index+end_index)*(end_index-start_index+1)//2
    if temp_sum==input_num:
        output_count=output_count+1
        start_index=start_index+1
    elif temp_sum>input_num: start_index=start_index+1
    else:
        if end_index==input_num-1: break
        else: end_index=end_index+1
print(output_count+1)