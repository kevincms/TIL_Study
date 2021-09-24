language=["Python","C","Java","C++","Go","JavaScript","Swift","C#"]
count=1

# 줄 맞추기
print(str(count).ljust(2),language[count-1].rjust(8),sep=". ") # 1. ljust = 왼쪽, rjust = 오른쪽 
count+=1

print("{:<2}. {:>8}".format(count,language[count-1])) # 2. {:<n} = 왼쪽, {:>n} = 왼쪽 = 오른쪽
count+=1

# 빈공간 채우기
print(str(count).zfill(2),language[count-1].rjust(8),sep=". ") # 3. zfill = 0으로 채우기
count+=1

print("{:0>2}. {:_>8}".format(count,language[count-1])) # 4. {:[]<n} [] 안의 문자로 빈공간을 채울 수 있음
count+=1

# 숫자
print("{:<2}. {:>+8,}{:>+8,}".format(count,1000,-1000)) # 양수 음수 자리수 표시
count+=1

print("{:<2}. {:f} {:.2f}".format(count,2/3,2/3)) # 소수점 자리수 정하기 (반올림 됨)
count+=1