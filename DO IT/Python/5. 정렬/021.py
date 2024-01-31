# https://www.acmicpc.net/problem/1517

num_count=int(input())
num_list=list(map(int,input().split()))

output_count=0
for i in range(num_count-1):
    for j in range(num_count-1-i):
        if num_list[i]>num_list[j+i+1]: output_count=output_count+1

print(output_count)