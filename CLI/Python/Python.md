# python & pip

### python 버전 확인
- python --version

### pip 버전 확인
- pip --version

### pip 업데이트/다운그래이드
- python -m pip install --upgrade pip
- python -m pip install pip==(Version)

### package 목록
- pip list
- pip list --outdated **업데이트 가능**

### package 설치/제거/업데이트/다운그래이드
#### 설치
- pip install (package)
- pip install (package)==version
#### 제거
- pip uninstall (package)
#### 모든 package 제거
- 
#### 업데이트
- pip install --upgrade (package)
#### 다운그래이드
- pip install (package)==(Version)
#### 모든 package 업데이트
- pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}

### package 세부사항
- pip show (package)

### package 검색
- pip search (package)