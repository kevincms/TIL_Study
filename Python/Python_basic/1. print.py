language=["Python","C","Java","C++","Go","JavaScript","Swift","C#"]
language_number=1

# +로 구분할 때에는 모두 문자열(str)이어야 한다.
print(str(language_number)+". "+"Hello "+language[language_number-1]) # 1.
language_number+=1

# +가 아닌 ,로 구분가능 (단 띄어쓰기가 됨, sep으로 수정가능) (혼용 가능)
print(language_number,".","Hello ",language[language_number-1]) # 2. 
language_number+=1

# 파이썬은 자동적으로 줄바꿈이 된다. (end를 이용하면 뒤의 출력을 바꿀 수 있다.)
print(str(language_number),". ","Hello ",end="",sep="") # 3.
print(language[language_number-1])
language_number+=1

# 다음과 같이 변수를 출력할 수 있다.
print("%d. Hello %s" % (language_number, language[language_number-1])) # 4. %d int | %f, %lf float | %s str
language_number+=1

print("{}. Hello {}".format(language_number,language[language_number-1])) # 5.
language_number+=1

print("{1}. Hello {0}".format(language[language_number-1],language_number)) # 6.
language_number+=1

print("{num}. Hello {Contents}".format(num=language_number,Contents=language[language_number-1])) # 7.
language_number+=1

print(f"{language_number}. Hello {language[language_number-1]}") # 8. ver 3.6 이상만 된다.
language_number+=1

very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_long_variable="PYTHON"
print("{}. very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_very_long_variable"\
    .format(language_number)) # 9. \(역슬래쉬)로 줄을 바꿔도 한줄로 인식할수 있다.