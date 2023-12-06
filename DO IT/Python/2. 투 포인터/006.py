# https://www.acmicpc.net/problem/2018
# 입력 :15, 출력 4
input_num=int(input())

start_index=1
end_index=1
temp_sum=1
output_count=0

end_num=input_num//2 if input_num%2==0 else input_num//2+1
while(start_index!=end_num or end_index!=end_num):
    if temp_sum==input_num:
        output_count=output_count+1

        temp_sum=temp_sum-start_index
        start_index=start_index+1
    elif temp_sum>input_num:
        temp_sum=temp_sum-start_index
        start_index=start_index+1
    else:
        if end_index>end_num: break
        else: 
            end_index=end_index+1
            temp_sum=temp_sum+end_index
print(output_count+1)