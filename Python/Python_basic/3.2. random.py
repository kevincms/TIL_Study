import random
count=1

print("%d."%count,random.random()) # 1. 0.0~1.0 미만의 임의의 값 생성
count+=1

print("%d."%count,int(random.random()*10)) # 2. 0~10 미만의 임의의 값 생성
count+=1

print("%d."%count,random.randrange(1,46)) # 3. 1~46 미만의 정수 값 생성
count+=1

print("%d."%count,random.randint(1,45)) # 4. 1~45 이하의 정수 값 생성
count+=1

test_list=[i for i in range(1,17,3)]
print("%d."%count,test_list) # 5. 임의의 데이터 list
count+=1

random.shuffle(test_list)
print("%d."%count,test_list) # 6. list를 무작위로 섞음.
count+=1

print("%d."%count,random.choice(test_list)) # 7. 리스트 내의 값을 랜덤하게 1개 추출
count+=1

print("%d."%count,random.sample(test_list,3)) # 8. 리스트 내의 값을 랜덤하게 n개 추출
count+=1