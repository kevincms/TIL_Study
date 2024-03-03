# https://www.acmicpc.net/problem/2023

def is_prime(num):
    for i in range(2,(num//2)+1):
        if num%i==0: return False
    return True

def DFS(digit):
    if digit==1: return [2,3,5,7]
    else:
        temp_list=DFS(digit-1)
        output_list=[]
        for i in temp_list:
            for j in [1,3,7,9]: # 마지막 자리수까 짝수면 2의 배수 5면 5의 배수이기 때문에 소수는 마지막 수는 4자리 중 하나이다.
                num=i*10+j
                if is_prime(num): output_list.append(num)
        return output_list

num_digit=int(input())

print(*DFS(num_digit),sep="\n")