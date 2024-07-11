# https://www.acmicpc.net/problem/1629

import sys
import math

def get_pow_list(binary):
    output=[]
    count=0
    for i in binary[::-1]:
        if i=='1': output.append(count)
        count+=1
    return output

input=sys.stdin.readline
A, B, C=map(int, input().split())
max_len=int(math.log2(B))
remain_list=[A%C]*(max_len+1)
for i in range(max_len): remain_list[i+1]=(remain_list[i]**2)%C
pow_list=get_pow_list(bin(B)[2:])
output=1
for i in pow_list: output=(output*remain_list[i])%C
print(output)