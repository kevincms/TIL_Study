# https://www.acmicpc.net/problem/10986
import sys

def Combination_2(n,r=2):
    return n*(n-1)//r
    

input=sys.stdin.readline
matrix_size, divide_num=map(int,input().split())

matrix_list=[0]+list(map(int,input().split()))
matrix_sum_list=[0 for _ in range(matrix_size+1)]
remain_count=[0 for _ in range(divide_num)]

for i in range(matrix_size):
    matrix_list[i+1]=matrix_list[i+1]%divide_num
    temp=(matrix_sum_list[i]+matrix_list[i+1])%divide_num
    matrix_sum_list[i+1]=temp
    remain_count[temp]=remain_count[temp]+1

output_num=remain_count[0]
for i in range(divide_num):
    output_num=output_num+Combination_2(remain_count[i],2)
print(output_num)