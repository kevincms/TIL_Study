# # test_package 에 있는 package 다양한 방법으로 사용할 수 있다.
import test_package.Python
count=1

python=test_package.Python.language_Python()
print(count,".",end=" ",sep="")
python.characteristic()
count+=1

from test_package.C import language_C
c=language_C()
print(count,".",end=" ",sep="")
c.characteristic() 
count+=1

from test_package import Java
java=Java.language_Java()
print(count,".",end=" ",sep="")
java.characteristic() 
count+=1

# 아래와 같이 전부 가져올 경우 __ini__에 __all__을 정의하여야 한다. (기본제공함수는 건들지 않아도 된다.)
from test_package import * # 이때 Go 모듈이 한번 실행된다. 
go=Go.language_Go()
print(count,".",end=" ",sep="")
go.characteristic()
count+=1