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

# 비교연산(관계연산)
print("%d."%count,10>5,5>=5,10<5,10<=5,5==5,5!=5) # 8. 비교연산(관계연산)
count+=1

# 논리연산
print("%d."%count,not True) # 9. not
count+=1

print("%d."%count,True and False,1 & 0) # 10. and
count+=1

print("%d."%count,True or False,1 | 0) # 11. or
count+=1

# 비트연산
print("%d."%count,7 & 4) # 12. and gate
count+=1

print("%d."%count,7 | 4) # 13. or gate
count+=1

print("%d."%count,7 ^ 4) # 14. xor gate
count+=1

print("%d."%count,~3) # 15. not gate (보수)
count+=1

print("%d."%count,4<<1,4>>1) # 16. shift
count+=1