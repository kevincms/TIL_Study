# Stable-Diffusion-Webui 세팅과정
- 참고 사이트 : https://quasarzone.com/bbs/qc_plan/views/33594
> 1. git, python 설치 및 환경변수 설정.
>> - 환경변수 설정에서 cmd 창에서 pip, python, git 명령어가 어떤 경로에서든 잘 작동해야 됨.
> 2. git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
> 3. model 설치 후 파일 stable-diffusion-webui > models > Stable-diffusion 로 이동
>> #### 사이트 목록
>> - https://civitai.com/
> 4. webui-user.bat 수정
>> 상단 git pull 추가, COMMANDLINE_ARGS==--precision full --no-half --no-half-vae --xformers --autolaunch 옵션 추가
> 5. 그 후 webui-user.bat 를 실행하거나 바로가기 만들기