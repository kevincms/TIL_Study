import re
count=1

# 1. [] : 문자열의 포함 ([abc]=[a-c]) -> (aqqq, bbqqq, qqqc), [^]=reverse [^0-9]=[a-zA-Z]
#    [\d]=[0-9] [\D]=[^0-9] [\s]=[ \t\n\r\f\v] [\S]=[^ \t\n\r\f\v] [\w]=[a-zA-Z0-9_] [\W]=[^a-zA-Z0-9_]
find_str="[ab]"
pattern=re.compile(find_str) 
goal_str=["ferwr","ababb","asadf","adsfwe"]
print("%d. "%count,end="")
for i in range(len(goal_str)):
    search_str=pattern.search(goal_str[i])
    if search_str: print("%s "%search_str.group(),end="") 
    else: print("Ns ",end="") # Ns=Not search
count+=1

# 2. . : 하나의 문자 (ab,d) -> (abcd, abed) [\n 제외]
find_str="ab.d"
pattern=re.compile(find_str)
goal_str=["abcd","abccd","abcdefg","xxxxx abcd","abcdabed"]
print("\n%d. "%count,end="")
for i in range(len(goal_str)):
    search_str=pattern.search(goal_str[i])
    if search_str: print("%s "%search_str.group(),end="") 
    else: print("Ns ",end="") # Ns=Not search
count+=1

# 3. * : 문자열의 반복 (ab*c) -> (ac, abbc, abbbbbc), + : 최소 1회의 문자열의 반복 (ab*c) -> (abc, abbc, abbbbbc)
#    {n} : n회의 문자열의 반복 (ab{3}c) -> (abbbc), {n,m} n~m회의 문자열의 반복 (ab{2,4}c) -> (abbc, abbbc, abbbbc) ?={0,1}
find_str="ab*c"
pattern=re.compile(find_str)
goal_str=["ac","aac","abc","abbc"]
print("\n%d. "%count,end="")
for i in range(len(goal_str)):
    search_str=pattern.search(goal_str[i])
    if search_str: print("%s "%search_str.group(),end="") 
    else: print("Ns ",end="") # Ns=Not search
count+=1

# 4. ^ : 문자열의 시작 (^un) -> (unit, undo)
find_str="^ab"
pattern=re.compile(find_str)
goal_str=["ac","abc","abcd","abbc"]
print("\n%d. "%count,end="")
for i in range(len(goal_str)):
    search_str=pattern.search(goal_str[i])
    if search_str: print("%s "%search_str.group(),end="") 
    else: print("Ns ",end="") # Ns=Not search
count+=1

# 5. $ : 문자열의 끝 (ly$) -> (fly, only)
find_str="cd$"
pattern=re.compile(find_str)
goal_str=["acd","abc","abcd","abbcd"]
print("\n%d. "%count,end="")
for i in range(len(goal_str)):
    search_str=pattern.search(goal_str[i])
    if search_str: print("%s "%search_str.group(),end="") 
    else: print("Ns ",end="") # Ns=Not search
count+=1