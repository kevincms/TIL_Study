import re

find_str="ab.d" # . : 하나의 문자 (ab,d) -> (abcd, abed) [\n 제외]
pattern=re.compile(find_str) 
count=1

goal_str=["abcd" ,"abccd" ,"abcdefg" ,"xxxxx abcd","abcdabed"]
print("%d. "%count,end="") # 1. match - 주어진 문자열의 처음부터 일치하는 것 하나를 string으로 반환
for i in range(len(goal_str)):
    match_str=pattern.match(goal_str[i])
    if match_str: print("%s "%match_str.group(),end="") 
    else: print("Nm ",end="") # Nm=Not match
count+=1

print("\n%d. "%count,end="") # 2. search - 주어진 문자열 중에 일치하는 것 하나를 string으로 반환
for i in range(len(goal_str)):
    search_str=pattern.search(goal_str[i])
    if search_str: print("%s "%search_str.group(),end="") 
    else: print("Ns ",end="") # Ns=Not search
count+=1

print("\n%d. "%count,end="") # 3. findall - 주어진 문자열 중에 일치하는 모든 것을 list로 반환
for i in range(len(goal_str)):
    findall_list=pattern.findall(goal_str[i])
    if findall_list: print("{} ".format(findall_list),end="") 
    else: print("Nf ",end="") # Nf=Not findall
count+=1

def print_regex(str, count):
    if str:
        print("\n%d. %s "%(count,str.group()),end="") # 일치하는 문자열
        print("%s "%str.string,end="") # 입력받은 문자열
        print("%d "%str.start(),end="") # 일치하는 문자열의 시작 index
        print("%d "%str.end(),end="") # 일치하는 문자열의 끝 index
        print("{} ".format(str.span()),end="") # 일치하는 문자열의 시작과 끝 index
    else:
        print("%d. Not regex")

goal_str="abcdabcd"
match_str=pattern.match(goal_str)
print_regex(match_str,count) # 4.
count+=1

goal_str="xxxabcdabcd"
search_str=pattern.search(goal_str)
print_regex(search_str,count) # 5.
count+=1