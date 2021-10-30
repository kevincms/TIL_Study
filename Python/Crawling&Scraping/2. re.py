import re
count=1

def print_maatch(str, count):
    if str:
        print("%d. %s"%(count,str.group()))
    else:
        print("%d. 매칭되지 않음"%count)

# . : 하나의 문자 (ab,d) -> (abcd, abed)
# ^ : 문자열의 시작 (^un) -> (unit, undo)
# $ : 문자열의 끝 (ly$) -> (fly, only)
find_str="ab.d"
pattern=re.compile(find_str) 

# match - 주어진 문자열의 처음부터 일치하는 지 확인
goal_str="abcd"
match_str=pattern.match(goal_str) 
print("%d. %s"%(count,match_str.group())) # 1. match가 되지 않으면 오류 발생
count+=1

goal_str="abccd"
match_str=pattern.match(goal_str)
print_maatch(match_str,count) # 2.
count+=1

goal_str="abcdefg"
match_str=pattern.match(goal_str)
print_maatch(match_str,count) # 3. 
count+=1

goal_str="xxxxx abcd"
match_str=pattern.match(goal_str)
print_maatch(match_str,count) # 4. 
count+=1

def print_search(str, count):
    if str:
        print("%d. %s"%(count,str.group()))
    else:
        print("%d. 매칭되지 않음"%count)

# search - 주어진 문자열 중에 일치하는 것 확인
goal_str="xxxxx abcd"
search_str=pattern.search(goal_str)
print_search(search_str,count) # 5. 
count+=1