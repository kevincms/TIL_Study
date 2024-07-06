# https://www.acmicpc.net/problem/1620

import sys

input=sys.stdin.readline
N, M=map(int,input().split())
p_list=[""]*(N+1)
p_dict=dict()
for i in range(N): 
    key=input().strip()
    p_list[i+1]=key
    p_dict[key]=f"{i+1}"
for _ in range(M):
    key=input().strip()
    try:
        key=int(key)
        print(p_list[key])
    except:
        print(p_dict[key])