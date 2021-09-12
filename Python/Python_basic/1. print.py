language=["Python","C","Java","C++","Go"]
language_number=1

# +로 구분할 때에는 모두 문자열(str)이어야 한다.
print(str(language_number)+". "+"Hello "+language[language_number-1])
language_number+=1

# +가 아닌 ,로 구분가능 (단 띄어쓰기가 됨) (혼용 가능)
print(language_number,".","Hello ",language[language_number-1])
language_number+=1

# 파이썬은 자동적으로 줄바꿈이 된다. (end를 이용하면 뒤의 출력을 바꿀 수 있다.))
print(str(language_number)+". "+"Hello ",end="")
print(language[language_number-1])
language_number+=1