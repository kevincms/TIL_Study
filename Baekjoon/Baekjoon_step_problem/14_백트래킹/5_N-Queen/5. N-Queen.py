'''
문제
 -N-Queen 문제는 크기가 N * N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
입력
 -첫째 줄에 N이 주어진다. (1 ≤ N < 15)
출력
 -첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
예제 입력 1
 -8
예제 출력 1
 -92
https://www.acmicpc.net//problem/9663
'''

def N_Queen(count,case,check=0):
    if count==input_num: case+=1
    else:
        for i in range(input_num):
            location_list[count]=[count,i]
            for j in range(count):
                if location_list[j][1]==i or abs(count-location_list[j][0])==abs(i-location_list[j][1]): 
                    check=1
                    break
            if check==1: 
                check=0
                continue
            else:
                case=N_Queen(count+1,case)
    return case

input_num=int(input())
location_list=[[0, 0] for i in range(input_num)]
print(N_Queen(0,0))