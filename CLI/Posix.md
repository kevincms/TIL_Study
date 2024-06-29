# POSIX(Portable Operating System Interface)
Unix Linux Mac

# How to use Posix 
### 현재 Directory 위치
- pwd
### Directory 목록
- ls
### Directory 이동
- cd (Directory_Location)
> - /   : Root Directory
> - ~   : Home Directory
> - ./  : Current Directory
> - ../ : Parent Directory
### Option & Explanation
- (Command) --help
- man (Command)
> - h : 도움말
> - e : 한줄 내리기
> - y : 한줄 올리기

# File CRUD (Create, read, update and delete)
### Create
- editor[vi] (filename)
> - 내용을 작성 후 파일 생성.
> - .(filename) : Hidden File
- touch (filename)
> - 빈 파일생성
### Read
- cat (filename)
> - 특정 파일내용 확인
- find (filename)
> - 특정 파일 찾기. * 를 이용해 특정 문자열 필터링 가능
### Update
- editor[vi] 
- mv
- sed
> - 
### Delete
- rm (filename)

# Directory CRUD (Create, read, update and delete)
### Create
- mkdir (Directory) 
### Read
- ls (option)
### Update
- mv (Current Directory) (Modified Directory)
### Delete
- rm -r (Directory)
### Link
- ln -s (Path) (Link Name)
> - s : 링크 옵션. 하드링크가 아닌 심볼릭 링크를 만듦. 윈도우 바로가기와 유사한 개념

# Apt<sup id="a1">[1](#apt)</sup>
> - apt update : apt 업데이트
> - apt install (package) : 패키지 설치
> - apt upgrade : 전체 패키지 업데이트
> - apt list : 패키지 목록 리스트
>> - --installed : 설치된 리스트
>> - --upgradable : 업그레이드 가능한 리스트 

# SSH
> - ssh user@ip
>> - 외부 ip에서 접속하기 위해서는 포트피워드 설정 필요
## SSH KEY
- client 컴퓨터에서 명령어 입력
> 1. ssh-keygen -t rsa -C "message"
>> - -t : 키 타입 (RSA, DSA)
>> - -C : comment
>> - id_rsa와 id_rsa.pub 키가 생성된다
> 2. scp (id_rsa.pub path) (user@ip):id_rsa.pub
> - Mac id_rsa.pub path : ~/.ssh/
> - 만들어진 키를 복사하여 전달
---
- server 컴퓨터에서 실행
> 1. ~에 id_rsa.pub 전달됨
> 2. .ssh 권한 700 확인
>> - chmod 700 .ssh
> 3. cat id_rsa.pub >> .ssh/authorized_keys
---
- ssh 접속
- ssh -i ~/.ssh/id_rsa user@ip

<span id="apt">우분투에 내장된 패키지 매니저. apt는 apt-get의 최신버전이다.</span>