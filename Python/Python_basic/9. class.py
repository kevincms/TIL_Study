count=1
    
class test_class:
    def __init__(self,count): # __init__ : 생성자 (클래스가 생성될 때 실행되는 함수)
        self.count=count # self : class 내에서 정의된 변수
    def test_print(self): # class의 함수에서는 아무런 변수를 입력받지 않더라도 self를 사용해야 함
        print("%d."%self.count,end=" ")
    def test_language(self):
        print(self.language)
        

test_class_variable=test_class(count)
test_class_variable.test_print() # 1. class 변수(객체) 생성 후 출력
test_class_variable.language="python" # 외부에서 변수를 만든 후 사용할 수 있다. (변수를 만든 객체에만 생성됨. )
test_class_variable.test_language()