language=["Python","C","Java","C++","Go","JavaScript","Swift","C#"]
count=1

# +로 구분할 때에는 모두 문자열(str)이어야 한다.
print(str(count)+". "+"Hello "+language[count-1]) # 1.
count+=1

# +가 아닌 ,로 구분가능 (단 띄어쓰기가 됨, sep으로 수정가능) (혼용 가능)
print(count,".","Hello ",language[count-1]) # 2. 
count+=1

# 파이썬은 자동적으로 줄바꿈이 된다. (end를 이용하면 뒤의 출력을 바꿀 수 있다.)
print(str(count),". ","Hello ",end="",sep="") # 3.
print(language[count-1])
count+=1

# 다음과 같이 변수를 출력할 수 있다.
print("%d. Hello %s" % (count, language[count-1])) # 4. %d int | %f, %lf float | %s str
count+=1

print("{}. Hello {}".format(count,language[count-1])) # 5.
count+=1

print("{1}. Hello {0}".format(language[count-1],count)) # 6.
count+=1

print("{num}. Hello {Contents}".format(num=count,Contents=language[count-1])) # 7.
count+=1

print(f"{count}. Hello {language[count-1]}") # 8. ver 3.6 이상만 된다.
count+=1

very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_long_variable="PYTHON"
print("{}. very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_long_variable"\
    .format(count)) # 9. \(역슬래쉬)로 줄을 바꿔도 한줄로 인식할수 있다.