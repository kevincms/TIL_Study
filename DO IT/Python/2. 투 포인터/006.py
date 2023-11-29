# https://www.acmicpc.net/problem/2018
# 입력 :15, 출력 4
input_num=int(input())

end_list_num=input_num//2 if input_num%2==0 else input_num//2+1
two_point_list=[i+1 for i in range(end_list_num)]

start_index=0
end_index=0
temp_sum=0

output_count=0
while(start_index!=end_list_num-1):
    temp_sum=sum(two_point_list[start_index:end_index+1])
    if temp_sum==input_num:
        output_count=output_count+1
        start_index=start_index+1
    elif temp_sum>input_num: start_index=start_index+1
    else:
        if end_index==end_list_num-1: break
        else: end_index=end_index+1
print(output_count+1)