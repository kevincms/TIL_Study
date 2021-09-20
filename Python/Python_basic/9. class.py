language=["Python","C","Java","C++","Go","JavaScript","Swift","C#"]
count=1
    
class test_language:
    def __init__(self,count): # __init__ : 생성자 (클래스가 생성될 때 실행되는 함수)
        self.count=count # self : class 내에서 정의된 변수
    def count_print(self): # class의 함수에서는 아무런 변수를 입력받지 않더라도 self를 사용해야 함
        print("%d."%self.count,end=" ")
    def language_print(self):
        print(self.language)

test_class_variable=test_language(count)
test_class_variable.count_print() # 1. class 변수(객체) 생성 후 출력
test_class_variable.language=language[count-1] # 외부에서 변수를 만든 후 사용할 수 있다. (변수를 만든 객체에만 생성됨)
test_class_variable.language_print()
count+=1

class language_characteristic:
    def __init__(self,language):
        self.language=language
    def characteristic_print(self):
        if self.language=="C":
            print("C는 절차지향 언어이다.")
        elif self.language=="Java":
            print("Java는 객체지향 언어이다.")


class test_language_C(test_language): # test_language의 내용을 상속받아 사용 (super 사용가능)
    def __init__(self, count, language):
        test_language.__init__(self,count) # 클래스를 지정하여 사용할 경우 self 사용
        language_characteristic.__init__(self,language) # 상속을 정의하지 않은 클래스도 사용가능
    def count_print(self):
        super().count_print() # 상속을 사용할 경우 self를 사용하지 않음
    def language_print(self):
        language_characteristic.characteristic_print(self)

test_class_variable=test_language_C(count,language[count-1])
test_class_variable.count_print()
test_class_variable.language_print()
count+=1

class test_language_Java(test_language,language_characteristic): # 다중상속
    def __init__(self, count, language):
        test_language.__init__(self,count) 
        language_characteristic.__init__(self,language) 
    def count_print(self):
        super().count_print() # 다중상속일 경우 가장 앞에 있는 클래스를 사용한다.
    def language_print(self):
        language_characteristic.characteristic_print(self)

test_class_variable=test_language_Java(count,language[count-1])
test_class_variable.count_print()
test_class_variable.language_print()
count+=1