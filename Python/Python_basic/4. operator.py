count=1

# 사칙연산
print("%d."%count,1+1) # 1. 더하기
count+=1

print("%d."%count,4-2) # 2. 뺴기
count+=1

print("%d."%count,4*2) # 3. 곱하기
count+=1

print("%d."%count,5/2) # 4. 나누기
count+=1

# 특수연산
print("%d."%count,2**3) # 5. n제곱
count+=1

print("%d."%count,5//3) # 6. 몫
count+=1

print("%d."%count,5%3) # 7. 나머지
count+=1

# 비교연산
print("%d."%count,10>5,5>=5,10<5,10<=5,5==5,5!=5) # 8. 비교연산
count+=1

# 논리연산
print("%d."%count,not True) # 9. not
count+=1

print("%d."%count,True and False,1 & 0) # 10. and
count+=1

print("%d."%count,True or False,1 | 0) # 11. or
count+=1