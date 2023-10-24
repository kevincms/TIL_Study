
환경변수는 사용자 변수와 시스템 변수가 있다.
> # 환경변수  
>> ### 사용자 변수  
>> 사용자 변수는 현재 로그인한 사용자에게만 적용
>> ### 시스템 변수  
>> 현재 사용자뿐만 아니라 모든 사용자에게 적용

환경변수의 Path값을 수정하면 재부팅 해야 적용된다.  [이거 불확실함]
cmd에 path라고 입력하면 시스템 변수의 path 출력 후 사용자 변수의 path가 출력된다.  
- 재부팅을 하지 않고 적용하는 방법  
taskkill /f /im explorer.exe  
explorer.exe  
- 환경변수 특이점


각 프로그램 별 환경변수 [컴파일러 어셈블리어 같은 경우 기본 설치경로가 아님]
BASIC="C:\Users\cho_min_seok\Melon_Reeve_Musk\"
> ### Git  
>> C:\Program Files\Git\cmd
> ### Anaconda
>> C:\Users\cho_min_seok\Melon_Reeve_Musk\Anaconda3\Scripts  
>> <u>%BASIC%Anaconda3</u> 은 anaconda Python, <u>%BASIC%Anaconda3\Scripts</u> 는 conda 실행
> ### Python
>> C:\Users\cho_min_seok\Melon_Reeve_Musk\Python 3.12.0  
>> C:\Users\cho_min_seok\Melon_Reeve_Musk\Python 3.12.0\Scripts  
>> <u>%BASIC%Python 3.12.0</u> 은 anaconda Python, <u>%BASIC%Python 3.12.0\Scripts</u> 는 pip 실행
> ### Nodejs
>> C:\Users\cho_min_seok\Melon_Reeve_Musk\nodejs 18.18.2