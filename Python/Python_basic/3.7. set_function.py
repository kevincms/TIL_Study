test_set={1,2,3,4,3,2,1}
count=1

print("%d."%count,test_set) # 1.
count+=1

temp_set={3,4,5,6,6,5,4,3}
print("%d."%count,temp_set) # 2.
count+=1

print("%d."%count,test_set&temp_set,test_set.intersection(temp_set)) # 3. set의 교집합
count+=1

print("%d."%count,test_set|temp_set,test_set.union(temp_set)) # 4. set의 합집합
count+=1

print("%d."%count,test_set-temp_set,test_set.difference(temp_set)) # 5. set의 차집합
count+=1

test_set.add(5)
print("%d."%count,test_set) # 6. set 데이터 추가
count+=1

test_set.remove(5)
print("%d."%count,test_set) # 6. set 데이터 제거
count+=1