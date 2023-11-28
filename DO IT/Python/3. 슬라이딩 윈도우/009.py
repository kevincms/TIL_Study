# https://www.acmicpc.net/problem/12891
import sys

def char_to_index(char):
    if char=="A": return 0
    elif char=="C": return 1
    elif char=="G": return 2
    elif char=="T": return 3
    else: return -1

input=sys.stdin.readline
string_length, pass_length=map(int,input().split())
string_list=list(input().strip())
include_count_list=list(map(int,input().split())) # 0 : A, 1 : C, 2 : G, 3 : T
check_count_list=[0 for _ in range(4)]
output_count=0

for i in range(pass_length):
    temp_index=char_to_index(string_list[i])
    check_count_list[temp_index]=check_count_list[temp_index]+1
if check_count_list==include_count_list: output_count=output_count+1

for i in range(string_length-pass_length):
    add_index=i+pass_length
    sub_index=i
    # count_add
    temp_index=char_to_index(string_list[add_index])
    check_count_list[temp_index]=check_count_list[temp_index]+1
    # count sub
    temp_index=char_to_index(string_list[sub_index])
    check_count_list[temp_index]=check_count_list[temp_index]-1
    if check_count_list==include_count_list: output_count=output_count+1
print(output_count)
    