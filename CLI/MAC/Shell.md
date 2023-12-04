### Shell
> - 현재 shell 확인
>> - echo $SHELL
> - 기본 shell 변경
>> - zsh : chsh -s /bin/zsh
>> - bash : chsh -s /bin/bash
> - tab 자동완성 대소문자 무시
>> - bash shell로 기본 shell 변경. 이후 1 경로 파일에 2 추가. 1 경로 파일이 없으면 생성
>> 1. ~/.inputrc
>> 2. set completion-ignore-case on

### Bash
- 유닉스 게열에서 주로 사용되는 기본 shell
- 이전에 사용된 shell의 개선 사항 중 주요점은 스크립팅 기능 추가[자동화 가능]

### Zsh
- Bash 등작 직후 학생이 만든 shell
- Mac의 shell을 bash 대신 zsh로 채택을 2019년에 발표[왜 그런지는 몰루?]

### 공통점
1. z- 명령 [검색해도 뭔 기능인지 모르겠음]
2. 자동완성 [tab 눌렀을 때 자동으로 디렉토리 또는 파일 찾는 기능]
3. 자동보정 [몰루?]
4. 색상 사용자 [터미널 꾸미기 기능인듯]

### 차이점
|Bash|Zsh|
|---|---|
|문법 : 그냥 간단함|문법 : 복잡한거 하기 쉬움|
|tab : 자동완성 간단|tab : 자동완성 더 좋음|
|부팅 시간 : 빠름|부팅 시간 : 느림|
|작업 제어 : processID|작업 제어 : job|
|커마 : 어려움|커마 : 쉬움|