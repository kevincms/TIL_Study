import random
count=1

print(str(count)+".",random.random()) # 1. 0.0~1.0 미만의 임의의 값 생성
count+=1

print(str(count)+".",int(random.random()*10)) # 2. 0~10 미만의 임의의 값 생성
count+=1

print(str(count)+".",random.randrange(1,46)) # 3. 1~46 미만의 정수 값 생성
count+=1

print(str(count)+".",random.randint(1,45)) # 3. 1~45 이하의 정수 값 생성
count+=1

test_list=[i for i in range(1,17,3)]
print(str(count)+".",test_list) # 임의의 데이터 list
count+=1

print(str(count)+".",random.choice(test_list)) # 리스트 내의 값을 랜덤하게 추출
count+=1
