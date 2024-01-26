# https://www.acmicpc.net/problem/1517

num_count=int(input())
num_list=list(map(int,input().split()))
num_list=[[num_list[i], i] for i in range(num_count)]
sorted_list=sorted(num_list)

index_diff_num_sum=0
duplication_num=0
for i in range(num_count):
    if sorted_list[i][0]<num_list[i][0]: duplication_num=duplication_num+1
    index_diff_num=abs(sorted_list[i][1]-i)
    index_diff_num_sum=index_diff_num_sum+index_diff_num

print(index_diff_num_sum-duplication_num)