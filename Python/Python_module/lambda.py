# (lambda [variable[매개변수]] : [function[함수식]])(constant[상수]) 의 형태로 구성
count=1
print("{}. {}".format(count,(lambda x : x**2)(3))) # 1. 
count+=1
print("{}. {}".format(count,(lambda x,y : x+y)(1,2))) # 2.
count+=1

# (lambda [variable[매개변수]] : [function[함수식]]) = def fuction 
print("{}. {}".format(count,list(map(lambda x:x**2,range(5))))) # 3. 
count+=1