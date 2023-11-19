import sys

input=sys.stdin.readline
data_count, question_count=map(int,input().split())
data_sum=[0 for _ in range(data_count+1)]

data_list=[0]+list(map(int,input().split()))
for i in range(data_count):
    data_sum[i+1]=data_list[i+1]+data_sum[i]

for i in range(question_count):
    start_num, end_num=map(int,input().split())
    print(data_sum[end_num]-data_sum[start_num-1])