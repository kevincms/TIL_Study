# https://www.acmicpc.net/problem/11004

def pivot_divide(input_list):
    pivot_num=input_list[0]
    num_count=len(input_list)
    front_list=[]
    back_list=[]
    pivot_count=1
    for i in range(num_count-1):
        comp_num=input_list[i+1]
        if pivot_num>comp_num: front_list.append(comp_num)
        elif pivot_num<comp_num: back_list.append(comp_num)
        else: pivot_count=pivot_count+1
    return front_list, back_list, pivot_count


num_count, num_order=map(int,input().split())
num_list=list(map(int,input().split()))
pivot_index=num_order-1
front_count=0
back_count=0
sort_list=num_list
while(1):
    front_list, back_list, pivot_count=pivot_divide(sort_list)
    front_list_size=len(front_list)
    back_list_size=len(back_list)

    before_front_count=front_count
    before_back_count=back_count

    front_count=front_count+front_list_size
    back_count=back_count+back_list_size
    front_pivot_sum=front_count+pivot_count
    if front_count>=num_order:
        if front_list_size==1 and num_order==front_count:
            output_num=front_list[0]
            break
        front_count=before_front_count
        back_count=back_count+pivot_count
        sort_list=front_list
    elif front_pivot_sum>=num_order:
        output_num=sort_list[0]
        break
    else:
        if back_list_size==1 and num_order==front_pivot_sum+1:
            output_num=back_list[0]
            break
        back_count=before_back_count
        front_count=front_count+pivot_count
        sort_list=back_list

print(output_num)

# num_count, num_order=map(int,input().split())
# num_list=list(map(int,input().split()))
# num_list.sort()
# print(num_list[num_order-1])