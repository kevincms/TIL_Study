### WSL
> - wsl --install
>> - wsl 설치
> - wsl --update
>> - wsl 업데이트
> - wsl --status
>> - wsl 기본 버전. 윈도우 10 = 1, 윈도우 11 = 2
> - wsl --version
>> - WSL 및 해당 구성 요소에 대한 버전 정보
> - wsl --help
>> - 명령어 확인

### Linux
> - wsl --list --online
>> - 설치 가능한 Linux 배포판 리스트
> - wsl --install -d [배포판 이름]
>> - 배포판 설치
> - wsl --unregister [배포판 이름]
> - 배포판 삭제
> - wsl --list --verbose
>> - 설치된 Linux 배포판 리스트
> - wsl --user root
>> - wsl 루트접속 [초기 비밀번호 모를 떄 접속 후 비번변경]
> - wsl -t [배포판 이름]
>> - 특정 머신 종료
> - wsl --distribution [배포판 이름]
>> - 특정 머신 시작
> - wsl --shutdown
>> - 모든 머신 일괄 종료

> - sudo reboot
>> - WSL 머신내에서 입력. 머신 재부팅

### Option 단축
- --list = -l
- --verbose = -v
- --distribution = -d

### Window file 접근
> - /mnt
>> - mnt 아래 경로에 각 드라이브에 있는 파일에 접근할 수 있다.
>> - 심볼릭 링크를 이용하면 파일을 공유해서 사용 가능하다.

### wsl ssh 설정
- 링크 참조 [https://wikidocs.net/219898]
> 1. sudo apt update -y && apt upgrade -y
> 2. sudo apt install openssh-server
>> - 오류 발생 시 삭제 후 설치(sudo apt remove openssh-server)
> 3. service ssh start
>> - 작동 확인 : service ssh status
>> - 정지 : service ssh stop
>> - 재시작 : service ssh restart
4. netsh interface portproxy add v4tov4 listenport=22 listenaddress=0.0.0.0 connectport=22 connectaddress=172.24.163.9
> - 윈도우 pc의 ip와 wsl의 ip가 다르기 때문에 포트포워드로 연결해주어야 함
>> - listenaddress는 0.0.0.0 알 때 자신의 ip를 가르키는 것 같음
> - netsh interface portproxy show all
>> - 위에서 설정한 portproxy 설정 보기
> - netsh interface portproxy delete v4tov4 listenport=22 listenaddress=(IP)
>> - 설정한 portproxy 삭제
5. ssh kevincms@(IP)로 ssh 연결 확인
> - 연결이 되지 않으면 wsl 컴퓨터에서 ssh kevincms@localhost로 test
>> - 연결이 된다면 portproxy 설정 및 공유기 포드포워드 확인
>> - 연결이 되지 않느다면 wsl linux ssh 확인
---
#### 오류 발생
1. WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
> - 링크 참조 [https://visu4l.tistory.com/entry/ssh-%EC%9B%90%EA%B2%A9-%EC%A0%91%EC%86%8D-%EC%97%90%EB%9F%ACWARNING-REMOTE-HOST-IDENTIFICATION-HAS-CHANGED]
> - ssh-keygen -R (IP)