# https://www.acmicpc.net/problem/16953

import sys

input=sys.stdin.readline
A, B=map(int,input().split())
isable=True
count=1
while(1):
    if A>=B:
        if A!=B: isable=False
        break
    end_num=B%10
    if(end_num==1): B=B//10
    elif end_num%2==0: B=B//2
    else:
        isable=False
        break
    count+=1
if isable: print(count)
else: print(-1)