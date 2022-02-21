# python 기본내장 함수 
count=1

print("%d."%count,abs(-3)) # 1. abs 절대값
count+=1

print("%d."%count,pow(2,3)) # 2. pow 제곱
count+=1

print("%d."%count,max(3, 12, 24)) # 3. max 최대값 (max의 파라미터 숫자를 변경할 수 있음, list를 넣어도 됨)
count+=1

print("%d."%count,min([3, 12, 24])) # 4. min 최소값 (min의 파라미터 숫자를 변경할 수 있음, list를 넣어도 됨)
count+=1

print("%d."%count,round(3.14), round(3.14,1))  # 5. round 반올림
count+=1


import math 
print("%d."%count,math.floor(3.14)) # 6. floor 내림
count+=1

print("%d."%count,math.ceil(3.14))  # 7. ceil 올림
count+=1

print("%d."%count,math.sqrt(16)) # 8. sqrt 루트
count+=1


import statistics
print("%d."%count,statistics.mean([1,2,3])) # 9. 평균
count+=1

