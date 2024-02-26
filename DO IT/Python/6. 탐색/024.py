# https://www.acmicpc.net/problem/2023

def DFS(digit):
    if digit==1:
        output_list=[]
        for i in range(10):
            if prime_list[i]: output_list.append(i)
        return output_list
    else:
        temp_list=DFS(digit-1)
        output_list=[]
        for i in temp_list:
            for j in range(10):
                num=i*10+j
                if prime_list[num]: output_list.append(num)
        return output_list

num_digit=int(input())
max_num=10**num_digit+1
prime_list=[True for _ in range(max_num)]

prime_list[0]=False
prime_list[1]=False
for i in range(2,max_num):
    if prime_list[i]:
        for j in range(2*i,max_num,i): prime_list[j]=False

print(*DFS(num_digit),sep="\n")