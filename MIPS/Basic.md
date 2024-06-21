# 기본 형식
- 아래와 같은 형식을 기반으로 코드를 작성 후 spim을 이용해서 실행해야함.

```bash
.text
.globl main # global 아님 주의
main:
    wanted_code # 원하는 어셈블리어 코드 작성
```

# spim
- MIPS 프로세서의 시뮬레이터
- 최신버전은 qtspim 이라 부르는 듯
- 텍스트 편집 기능없이 실행 및 디버그 기능만 제공
- 자세한 사용법은 SPIM.md 참고

# $ : 레지스터를 가르키는 기호
- 0부터 시작이기 때문에 $2면 3번쨰 레지스터이다.
- $0은 항상 0의 값을 가지고 수정할 수 없다.
- 각 레지스터는 index 대신 별명으로 접근가능하다. ex) $8 = $t0

# label
## .text
- text segment의 시작을 알림
> - .text \<addr\>
>> - addr은 option

## .data
- data segment의 시작을 알림
> - .data \<addr\>
>> - addr은 option

- data segment 선언 후 데이터의 크기에 맟춰 명령어를 사용해 순차적으로 데이터를 저장한다.
> - .byte \<data\>
> - .word \<data\>
>> - 4byte
> - .half \<data\>
> - .float \<data\>
> - .double \<data\>

- example
```C
int w1[4] = {1,-1, 0xabcdef12, 0xffff};
```
```bash
.data 0x10020000
    .word 1
    .word -1
    .word 0xabcdef12
    .word 0xffff
```

위의 예시에서 word는 4byte기 아래와 같이 저장된다.

|주소|값|
|---|---|
|0x10020000~0x10020003|0x00000001|
|0x10020004~0x10020007|0xffffffff|
|0x10020008~0x1002000b|0xabcdef12|
|0x1002000c~0x1002000f|0x0000ffff|

여기서 한 줄을 골라 더 자세히 분석을 할 수 있다.

|주소|값|
|---|---|
|0x10020008~0x1002000b|0xabcdef12|


- data 저장 방식
> - Big endian byte order
>> - SPARC, Motorola

|주소|값|
|---|---|
|0x10020008|0xab|
|0x10020009|0xcd|
|0x1002000a|0xef|
|0x1002000b|0x12|


> - Little endian byte order
>> - intel, SPIM

|주소|값|
|---|---|
|0x10020008|0x12|
|0x10020009|0xef|
|0x1002000a|0xcd|
|0x1002000b|0xab|

- MIPS는 2개의 방식 모두 이용할 수 있고 SPIM에서는 Little endian byte order를 사용.
- 또한 word가 아닌 byte로 저장하더라도 SPIM에서는 word 단위로 끊어서 보여준다.

## .global