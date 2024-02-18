https://midnightcow.tistory.com/entry/Git-Command-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%A0%95%EB%A6%AC


## git 초기 세팅
- git remote add  <u>path</u>: 
- git remote add  <u>name</u> <u>path</u> :
- git remote remove 

## git repository 만들기
1. git init [새로 만들기] **or** git clone [복사하기]
2. git add <u>파일 이름</u>
3. git commit 후 vim 실행 **or** git commit -m "message"

## git 자주 쓰는 명령어
> - git status
>> - 현재 git의 상태를 파악
> - git add
>> - 변경된 파일을 반영
>> - -u : 삭제된 파일을 반영하는 옵션
> - git reset (filename - option)
>> - add 된 파일을 되돌기는 용도

## git 설정 및 상태 확인
> - 기본 설정 보기
>> - git config --list  
> - github 연동
>> - git config --global user.name <u>github ID</u>
>> - git config --global user.mail <u>github Email</u>
> - 설정 초기화
>> - git config --unset <NAME>

- git status : git의 상태 파악 [현재 commit 된 파일, ]
- git log : 로그 확인

## git commit 날짜 수정
> 1. commit 날짜 지정
>> - git commit --date "1 day ago" -m "message"
>> - git commit --date "$(date)" -m "message"
>> - git commit --date "Thu 30 Mar 2023 10:00:00 KST" -m "message"

> 2. 마지막 commit 날짜 수정s
>> - git commit --amend --no-edit --date "$(date)"
>> - git commit --amend --no-edit --date "Thu 30 Mar 2023 10:00:00 KST"

> 3. 특정 commit 날짜 수정 [https://blacklobster.tistory.com/17]
>> - rebose

> date 옵션
>> - 형식 : "Thu 30 Mar 2023 10:00:00 KST"
>> - 월 : Mon, 화 : Tue, 수 : Wed, 목 : Thu, 금 : Fri, 토 : Sat, 일 : Sun
>> - 1월 : Jan, 2월 : Feb, 3월 : Mar, 4월 : Apr, 5월 : May, 6월 : Jun, 7월 : Jul, 8월 : Aug, 9월 : Sep, 10월 : Oct, 11월 : Nov, 12월 : Dec

>> - ex) git commit --date "Sat 23 Jun 2024 12:34:06 KST" -m "message" 
>> - 요일은 안맞춰도 자동으로 맞추어준다.

## mac git 설정
> ### 개행문자 설정
>> - git config --global core.autocrlf input
>> - git config --global core.eol lf
> ### 한글 설정
>> - git config --global core.quotepath false
>> - git config --global core.precomposeunicode true
> ### Vscode GUI
>> - git config --global core.filemode true
> ### author
>> - git config user.useConfigOnly true
> ### 잔디오류 [ https://it-eldorado.tistory.com/145 ]
>> - git filter-branch -f --env-filter "GIT_AUTHOR_NAME='kevincms'; GIT_AUTHOR_EMAIL='kevincms314@naver.com'; GIT_COMMITTER_NAME='kevincms'; GIT_COMMITTER_EMAIL='kevincms314@naver.com';" HEAD
>> - git push --force --set-upstream origin master