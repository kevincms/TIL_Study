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