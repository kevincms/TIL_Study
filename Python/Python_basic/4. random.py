import random

count=1
print(random.random()) # 0.0~1.0 미만의 값 생성
count+=1
print(random.randrange(1,11)) # 1~10 사이의 정수 값 생성
test_list=[i for i in range(1,17,3)]
print(test_list)
count+=1
print(random.choice(test_list)) # 리스트 내의 값을 랜덤하게 추출
count+=1