# https://www.acmicpc.net/problem/11399

def insert(list):
    temp=list[:-1]
    list[0]=list[-1]
    list[1:]=temp
    return list

num_count=int(input())
num_list=list(map(int,input().split()))
for i in range(num_count-1):
    insert_lndex=i+1
    insert_num=num_list[i+1]
    for j in range(i+1):
        sort_index=j
        sort_num=num_list[j]
        if insert_num<sort_num:
            insert_list=num_list[sort_index:insert_lndex+1]
            num_list[sort_index:insert_lndex+1]=insert(insert_list)
            break

output_sum=0
for i in range(num_count): output_sum=output_sum+num_list[i]*(num_count-i)
print(output_sum)