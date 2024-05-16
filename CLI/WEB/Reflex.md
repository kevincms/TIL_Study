# Reflex
- python으로 web의 모든 것을 개발할 수 있는 Framework
- 기존이름은 Pynecone 이었느데 이름이 Reflex로 바뀜

## 기본 사용법
- https://reflex.dev/docs/getting-started/installation/#install-on-macos/linux
> 1. python과 nodejs 설치 후 환경변수 설정
>> - python, pip, node, npm 명령어가 모든 경로에서 동작하도록 환경변수 설정이 되어야 함.
> 2. 폴더(디렉토리) 만들기
>> - 자신이 만들려는 프로젝트 이름의 폴더를 생성(영어 추천)
>> - 윈도우보다 mac이나 Linux에서 하는 것을 추천.(무슨 오류가 발생할지 모르고 더 빠른 거 같음)
> 3. python 가상환경 설정
>> - 근데 난 안함
> 4. pip install reflex
---
>> - 만든 폴더 위치에서 터미널 입력
> 5. reflex init
> 6. reflex run
>> - localhost에서 실행됨
---
- https://reflex.dev/docs/hosting/deploy-quick-start/
> 7. reflex login
>> - github or google 로그인
> 8. reflex deploy
> 9. reflex deployments list
>> - url 확인

## delpoy(배포)
- https://reflex.dev/docs/hosting/hosting-cli-commands/#reflex-deployments-status-
> - reflex login
>> - 기본적으로 google or github 로그인을 해야 배포를 할 수 있음.
>> - 2024.8.11 기준으로 서버비는 reflex에서 대주는 느낌. [대신 url에 reflex 붙음]
---
> - reflex deployments --helpㅔ
> - reflex deployments list
>> - 배포된 목록 확인
> - reflex deployments status (app_name)
> - reflex deployments log (app_name)
> - reflex deployments delte (app_name)
>> - 배포한 web app 삭제
---
### reflex deploy
- 만든 web app을 배포할 때 사용
> - option
>> - 
> - update : 명령어는 동일. reflex에서 자동으로 이름이 같은 프로젝트를 찾아서 업데이트 함.
>> - Overwrite deployment [app-name] 과 같은 log가 표시되어야 함.