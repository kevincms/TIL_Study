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
> 1. sudo apt update -y && apt upgrade -y
> 2. sudo apt install openssh-server
>> - 오류 발생 시 삭제 후 설치(sudo apt remove openssh-server)
> 3. service ssh start
>> - 작동 확인 : service ssh status
>> - 정지 : service ssh stop
>> - 재시작 : service ssh restart

4. netsh interface portproxy add v4tov4 listenport=22 listenaddress=0.0.0.0 connectport=22 connectaddress=172.24.163.9

ssh kevincms@116.127.178.135

https://wikidocs.net/219898