test_list=["%d"%(i) for i in range(1,4)]
count=1

print("%d."%count,test_list) # 1. 
count+=1

# list의 원하는 index에 삽입
test_list.insert(0,"0") 
print("%d."%count,test_list) # 2.
count+=1

# list의 마지막에 삽입
test_list.append("4") 
print("%d."%count,test_list) # 3.
count+=1

temp_list=["%d"%(i) for i in range(5,9)]
print("%d."%count,test_list) # 4. 
count+=1
print("%d."%count,temp_list) # 5. 
count+=1

# list 합체
test_list.extend(temp_list)
print("%d."%count,test_list) # 6. 
count+=1

# list 마지막, index를 통한 제거
print("%d."%count,test_list.pop()) # 7. 리스트 마지막 요소 제거
count+=1
del test_list[0] # 리스트의 원하는 index의 요소 제거
print("%d."%count,test_list) # 8.
count+=1

# str애서 사용한 index와 같음. 하지만 find는 사용할 수 없음
print("%d."%count,test_list.index("2")) # 9.
count+=1

# list 요소를 통한 제거
test_list.remove("2") # del test_list[test_list.index("2")] 와 동일
print("%d."%count,test_list) # 11.
count+=1

# str애서 사용한 count와 같음
print("%d."%count,test_list.count("2")) # 11.
count+=1

test_list=["%d"%(i) for i in range(4,0,-1)]

print("%d."%count,test_list) # 12.
count+=1

# list 요소 type 변경
test_list=list(map(int,test_list))
print("%d."%count,test_list) # 13.
count+=1

# list 정렬
test_list.sort() # sorted : 사본생성
print("%d."%count,test_list) # 14.
count+=1

# list 역정렬
test_list.sort(reverse=True) # sorted : 사본생성
print("%d."%count,test_list) # 15.
count+=1

# list 순서 뒤집기
test_list.reverse() # reversed : 사본생성
print("%d."%count,test_list) # 16.
count+=1

# list 정리
test_list.clear()
print("%d."%count,test_list) # 17.
count+=1