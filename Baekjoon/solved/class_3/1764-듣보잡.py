# https://www.acmicpc.net/problem/1764

import sys

input=sys.stdin.readline
N, M=map(int,input().split())
N_set=set()
M_set=set()
for _ in range(N): N_set.add(input().strip())
for _ in range(M): M_set.add(input().strip())

NM_list=list(N_set.intersection(M_set))
NM_list.sort()
print(len(NM_list))
for i in NM_list: print(i)