count=1

test_range=list(range(3)) # 1. 파라미터가 하나일 경우 0부터 n미만
print("%d."%count,test_range)
count+=1

test_range=list(range(3,6)) # 2. 파라미터가 2개인 경우 a부터 b미만
print("%d."%count,test_range)
count+=1

test_range=list(range(3,8,2)) # 3. 파라미터가 3개인 경우 c간격으로 a부터 b미만 
print("%d."%count,test_range)
count+=1

test_range=list(range(3,-1,-1)) # 4. slice와 비슷하게 사용가능
print("%d."%count,test_range)
count+=1

print("%d."%count,end=" ")
count+=1
for i in [1,2,3]:    # 5. for 반복문 in 뒤에 있는 자료의 요소를 i 변수에 차례로 담아 반복한다. (list가 아닌 자료형도 가능)
    print(i,end=" ")

print("\n%d."%count,end=" ") 
count+=1
for i in range(4,7): # 6. range를 이용한 반복문
    print(i,end=" ")

test_list=[i for i in range(3)] # 7. for 반복문의 또 다른 활용 예시
print("\n%d."%count,test_list)
count+=1

index=7
print("%d."%count,end=" ")
while index<=9:             # 8. while 반복문
    print(index,end=" ")
    index+=1
count+=1

print("\n%d."%count,end=" ")
while True:                 # 9. 무한 loop (break로 빠져나올 수 있고 continue로 생략할 수 있음)
    if index==13:
        break
    index+=1
    if index==12:
        continue
    print(index,end=" ")
count+=1