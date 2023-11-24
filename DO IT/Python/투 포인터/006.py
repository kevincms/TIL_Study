# 입력 :15, 출력 4
input_num=int(input())

two_point_list=[i+1 for i in range(input_num)]

start_index=0
end_index=0
temp_sum=0

output_count=0
while(start_index!=input_num-1):
    temp_sum=0
    for i in range(start_index,end_index+1):
        temp_sum=temp_sum+two_point_list[i]
    if temp_sum==input_num:
        output_count=output_count+1
        start_index=start_index+1
    elif temp_sum>input_num: start_index=start_index+1
    else: end_index=end_index+1
print(output_count+1)