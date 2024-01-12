# https://www.acmicpc.net/problem/1427

def swap(input_num1,input_num2):
    return input_num2, input_num1

num_list=list(str(input()))
num_count=len(num_list)
for i in range(num_count-1):
    for j in range(num_count-i):
        comp_index=i+j
        comp_num=num_list[comp_index]
        if j==0:
            max_num=num_list[i]
            max_index=i
        elif max_num<comp_num: 
            max_num=comp_num
            max_index=comp_index
    num_list[i], num_list[max_index]=swap(num_list[i],num_list[max_index])

output_num="".join(num_list)
print(output_num)