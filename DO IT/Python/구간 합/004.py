import sys

input=sys.stdin.readline
matrix_size, question_count=map(int,input().split())
matrix_list=[[] for _ in range(matrix_size+1)]
matrix_list[0]=[0 for _ in range(matrix_size+1)]
matrix_sum_list=[[0 for _ in range(matrix_size+1)] for _ in range(matrix_size+1)]

for i in range(matrix_size):
    matrix_list[i+1]=[0]+list(map(int,input().split()))
    
for i in range(matrix_size):
    for j in range(matrix_size):
        matrix_sum_list[i+1][j+1]=matrix_sum_list[i+1][j]+matrix_sum_list[i][j+1]-matrix_sum_list[i][j]+matrix_list[i+1][j+1]

for i in range(question_count):
    x1, y1, x2, y2=map(int,input().split())
    output_num=matrix_sum_list[x2][y2]-matrix_sum_list[x1-1][y2]-matrix_sum_list[x2][y1-1]+matrix_sum_list[x1-1][y1-1]
    print(output_num)