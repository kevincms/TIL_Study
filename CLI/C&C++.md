### GCC & G++
- GCC와 G++ 모두 C와 C++을 컴파일할 수 있는 컴파일러이다.  

|<center>GCC</center>|<center>G++</center>|  
|---|---|  
|.c .cpp를 각각 C와 C++로 컴파일|.c .cpp를 모두 C++로 컴파일|  

### 버전확인
- g++ -v
- g++ --version

### 동작과정
- https://seamless.tistory.com/2
- 사진 참고

### Command
> - 전처리
>> - g++ -E "source.cpp" -o "source.i"
> - 컴파일
>> - g++ -S "source.cpp" -o "source.s"

<!-- - g++ "source.c"
- gcc -E "source.c"

- gcc -o "output" "source.c" -->
