import sys

input=sys.stdin.readline
data_count, question_count=map(int,input().split())
data=[0 for _ in range(data_count+1)]
data_sum=[0 for _ in range(data_count+1)]
for i in range(data_count):
    data[i+1]=int(input())
    data_sum[i+1]=data[i+1]+data_sum[i]

for i in range(question_count):
    start_num, end_num=map(int,input().split())
    print(data_sum[end_num]-data_sum[start_num-1])