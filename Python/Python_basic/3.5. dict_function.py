test_dict={0:"영",1:"일",2:"이"}
count=1

print("%d."%count,test_dict[1],test_dict.get(2)) # 1. key 값을 통해 value를 가져올 수 있음
count+=1

print("%d."%count,test_dict.get(5),test_dict.get(5,"해당 값 없음")) # 2. key 값이 없는 경우 None(변경가능)
count+=1

print("%d."%count,2 in test_dict,5 in test_dict) # 3. key 값이 있는지 확인
count+=1

test_dict[1]="하나"
print("%d."%count,test_dict) # 4. dictionary는 value 값 변경가능
count+=1

del test_dict[2]
print("%d."%count,test_dict) # 5. key와 value 모두 삭제
count+=1

print("%d."%count,test_dict.keys(),test_dict.values(),test_dict.items()) # 6. key 값만 출력, value 값만 출력, 동시출력
count+=1