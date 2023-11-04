https://midnightcow.tistory.com/entry/Git-Command-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%A0%95%EB%A6%AC


## git 초기 세팅
- git remote add  <u>path</u>: 
- git remote add  <u>name</u> <u>path</u> :
- git remote remove 

## git 설정 확인
git config --list  

git config --global user.name <u>github ID</u>
git config —global user.mail <u>github Email</u>

- git status : git의 상태 파악 [현재 commit 된 파일, ]
- git log : 로그 확인

## git repository 만들기
1. git init [새로 만들기] **or** git clone [복사하기]
2. git add <u>파일 이름</u>
3. git commit 후 vim 실행 **or** git commit -m "message"

## git commit 날짜 수정
> 1. commit 날짜 지정
>> - git commit --date "1 day ago" -m "message"
>> - git commit --date "$(date)" -m "message"
>> - git commit --date "Thu 30 Mar 2023 10:00:00 KST" -m "message"

> 2. 마지막 commit 날짜 수정
>> - git commit --amend --no-edit --date "$(date)"
>> - git commit --amend --no-edit --date "Thu 30 Mar 2023 10:00:00 KST"

## mac git 설정
> ### 개행문자 설정
>> git config --global core.autocrlf input 
>> git config --global core.eol lf 
> ### 한글 설정
>> git config --global core.quotepath false