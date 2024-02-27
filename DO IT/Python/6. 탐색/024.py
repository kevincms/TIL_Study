# https://www.acmicpc.net/problem/2023

def is_prime(num):
    if num in prime_list: return True
    for i in prime_list:
        if num%i==0: return False
    return True

def DFS(digit):
    if digit==1: return [2,3,5,7]
    else:
        temp_list=DFS(digit-1)
        output_list=[]
        for i in temp_list:
            for j in range(10):
                num=i*10+j
                if is_prime(num): output_list.append(num)
        return output_list

num_digit=int(input())
max_num=1000000
prime_list=[True for _ in range(max_num)]

prime_list[0]=False
prime_list[1]=False
for i in range(2,max_num):
    if prime_list[i]:
        for j in range(2*i,max_num,i): prime_list[j]=False

temp_list=[]
for i in range(max_num):
    if prime_list[i]: temp_list.append(i)

prime_list.clear()
temp_list=prime_list

print(*DFS(num_digit),sep="\n")