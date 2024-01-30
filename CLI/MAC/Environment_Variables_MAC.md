### MAC 기본 환경설정
> - mac에서는 shell에 따라 환경변수 설정이 달라진다.
> - 하지만 파일만 달라진뿐 대부분의 과정은 동일하다.
> - 사용하는 ${shell}+rc 또는 ${shell}+_profile 의 이름으로 파일을 홈디렉토리에 생성 혹은 편집한다.
>> - ex) zsh : ~/.zshrc ~/.z_profile, bash : ~/.bashrc ~/.bash_profile
> - 그 후 해당 파일에 환경변수를 입력후
> - source ~/.${shell}rc or ~/.${shell} 로 변경사항 적용

### rc vs _profile
> - shell
>> - 대화형 : 터미널과 연결됨
>>> - 로그인형 : 로그인 후 처음 보이는 터미널
>>> - 비로그인형 : 새 터미널을 여는 경우 로그인 셸에서 비로그인 셸이 호출됨.
>> - 비대화형 : 터미널과 연결되지 않음

- rc는 대화형 로그인형 쉘로 호출될때 실행
- _profile은 대화형 비로그인형 쉘

- 환경변수 지정처럼 한번만 실행해도 되는 경우 _profile이 추천됨.
- ~/.${shell}_profile의 경우 특정 shell에서만 실행됨.
- ~/.profile의 경우 모든 shell에서 실행됨

### 환경변수 설정
> - alias new_command = 'old_command'
>> - 기본의 명령어를 새로운 명령어로 교체
> - export var_name = var_value
>> - 입력되어 있는 환경변수 생성 및 교체

### Python
> - ~/.bash_profile 생성 혹은 편집 후 아래 명령어 입력
>> - alias python='python3'
>> - PATH="/Library/Frameworks/Python.framework/Versions/3.11/bin:${PATH}"
>> - export PATH
> - source ~/.bash_profile
>> - source 명령어를 이용해서 변경된 내용 적용하기

### Homebrew
> - ~/.bash_profile 생성 혹은 편집 후 아래 명령어 입력
>> - PATH="/opt/homebrew/bin:${PATH}"
>> - export PATH
> - source ~/.bash_profile
>> - source 명령어를 이용해서 변경된 내용 적용하기