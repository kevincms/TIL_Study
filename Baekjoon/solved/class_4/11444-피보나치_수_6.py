# https://www.acmicpc.net/problem/1764

# 풀이참고 - https://ohgym.tistory.com/1

def mutiple_matrix(a,b,mod):
    return [[(a[0][0]*b[0][0]+a[0][1]*b[1][0])%mod,(a[0][0]*b[0][1]+a[0][1]*b[1][1])%mod],
            [(a[1][0]*b[0][0]+a[1][1]*b[1][0])%mod,(a[1][0]*b[0][1]+a[1][1]*b[1][1])%mod]]

def pow_matrix(n,mod):
    if len(matrix_list)<n+1:
        temp_list=pow_matrix(n-1,mod)
        matrix_list.append(mutiple_matrix(temp_list,temp_list,mod))
    return matrix_list[n]

def get_pow_list(binary):
    output=[]
    count=0
    for i in binary[::-1]:
        if i=='1': output.append(count)
        count+=1
    return output

import sys
import math

input=sys.stdin.readline
n=int(input())
max_len=int(math.log2(n))
mod=1000000007
matrix_list=[[[1,1],[1,0]]]
output_matix=[[1,0],[0,1]]
pow_matrix(max_len,mod)
pow_list=get_pow_list(bin(n)[2:])
for i in pow_list: output_matix=(mutiple_matrix(output_matix,matrix_list[i],mod))
print(output_matix[0][1])