count=1

test_str="Hello World"
print(str(count)+".",test_str,len(test_str)) # 1. 문자열 길이 반환
count+=1

print(str(count)+".",test_str.upper()) # 2. 대문자로 변경
count+=1

print(str(count)+".",test_str.lower()) # 3. 소문자로 변경
count+=1

print(str(count)+".",test_str[0].isupper()) # 4. 대문자 확인
count+=1

print(str(count)+".",test_str[0].islower()) # 5. 소문자 확인
count+=1

print(str(count)+".",test_str.replace("World","Python")) # 6. 문자열 변경
count+=1

print(str(count)+".",test_str.index("l")) # 7. index 반환
count+=1

index=test_str.find("l") # 8. 문자뿐만 아니라 문자열도 찾아서 index 반환 (index와 동일)
print(str(count)+".",index,end=" ") 
count+=1
while index>0:
    index=test_str.find("l",index+1) # 8. index 위치를 추가하면 그 위치부터 시작하는 문자를 찾아준다. (index와 동일)
    print(index,end=" ") # find의 경우 찾는 문자열이 없으면 -1 반환하지만 index는 오류가 난다.

print("\n"+str(count)+".",test_str.count("l")) # 9. 해당 문자열의 개수를 count해서 반환
count+=1