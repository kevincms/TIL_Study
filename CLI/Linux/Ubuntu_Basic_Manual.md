## 모든 사용자가 사용하는 프로그램 및 파일
> - /usr
>> - /usr/bin  
>> 리눅스에서 사용하는 명령어가 있는 곳.  
>> ln을 이용해 이곳에 링크파일을 생성하면 새로운 명령어를 만들 수 있다.

## 추가 프로그램
> - /opt 
>> 보통 opt 경로에 설치된다.
> - deb, rpm
>> window에서 exe와 같은 확장자. 대부분 deb이며 프로그램 설치 패키치 필요.
>> wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb


### GUI
> - sudo apt-mark hold acpid acpi-support
> - sudo apt install ubuntu-desktop
>> - 그냥 ubuntu-desktop 설치 시 오류 발생 [참고 : https://github.com/microsoft/WSL/discussions/9350]
> - sudo apt install xfce4
> - sudo apt install xrdp

> - sudo apt install xfce4
> - sudo apt install xrdp
> - sudo cp /etc/xrdp/xrdp.ini /etc/xrdp/xrdp.ini.bak
> - sudo sed -i 's/3389/3390/g' /etc/xrdp/xrdp.ini
> - sudo sed -i 's/max_bpp=32/#max_bpp=32nmax_bpp=128/g' /etc/xrdp/xrdp.ini
> - sudo sed -i 's/xserverbpp=24/#xserverbpp=24nxserverbpp=128/g' /etc/xrdp/xrdp.ini

> - echo xfce4-session > ~/.xsession

> - sudo /etc/init.d/xrdp start

https://guiyomi.tistory.com/113

[실패 참고 : https://x410.dev/cookbook/wsl/enable-systemd-in-wsl2-and-have-the-best-ubuntu-gui-desktop-experience/]

> - apt install ubuntu-desktop





### 웹검색
> - chrome
>> 실행 명령 : google-chrome
>> 설치 : sudo apt install ./google-chrome-stable_current_amd64.deb
