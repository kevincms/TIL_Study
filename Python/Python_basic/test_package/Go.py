class language_Go:
    def characteristic(self):
        print("Go는 함수형 언어이다.",end="")

if __name__=="__main__":
    print("모듈을 직접 실행하였습니다.")
    Go=language_Go()
    Go.characteristic()
else:
    print("외부에서 모듈을 호출하였습니다.")