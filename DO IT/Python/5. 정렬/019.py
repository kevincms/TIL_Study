# https://www.acmicpc.net/problem/11004


def quick_sort(input_list):
    num_count=len(input_list)
    if num_count<=1: return input_list
    else: 
        pivot_num=input_list[0]
        pivot_count=1
        front_list=[]
        back_list=[]
        for i in range(num_count-1):
            comp_num=input_list[i+1]
            if pivot_num>comp_num: front_list.append(comp_num)
            elif pivot_num<comp_num: back_list.append(comp_num)
            else: pivot_count=pivot_count+1
        return quick_sort(front_list)+[pivot_num]*pivot_count+quick_sort(back_list)

num_count, num_order=map(int,input().split())
num_list=list(map(int,input().split()))
num_list=quick_sort(num_list)
print(num_list[num_order-1])