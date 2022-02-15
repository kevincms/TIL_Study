# 
### 관리자 명령으로 실행
- sudo
### package index 정보를 업데이트 (apt-get의 index : /etc/apt/sources.list)
- sudo apt-get update
### 설치된 package 업데이트
- sudo apt-get upgrade

# package
### package 설치
- sudo apt-get install (package)
### package 재설치
- apt-get --reinstall install (package)
### package 삭제 (purge : 설정파일포함 삭제)
- sudo apt-get remove (package)
- sudo apt-get purge (package)
### 패키지 검색
- sudo apt-cache search (package)
### 패키지 정보
- sudo apt-cache show 패키지이름