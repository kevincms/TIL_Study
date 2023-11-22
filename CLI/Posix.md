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

# File
### Create
- editor[vi] (filename)
> - 내용을 작성 후 파일 생성.
> - .(filename) : Hidden File
- touch (filename)
> - 빈 파일생성
### Read
- cat (filename)
> - 특정 파일내용 확인
### Update
- editor[vi] 
- mv
### Delete
- rm (filename)

# Directory
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



<span id="apt">우분투에 내장된 패키지 매니저</span>