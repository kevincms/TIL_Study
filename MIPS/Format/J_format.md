# Instruction fields

|field|op|label(address)|
|---|--:|--:|
|bit|6|26|

> 1. op: operation code (opcode)
>> - opcode를 통해 format을 파악한다.
> 2. address : 이동할 명령어의 주소이다. 보통 Label로 작성한다.
>> - 명령어의 주소는 32비트지만 할당된 비트는 26비트이다.
>> - 위의 문제를 해결하기 위해 명령어의 주소가 4의 배수라는 것을 이용해 뒤의 00를 생략한다. (2비트 절약)
>> - 32-26-2=4 남은 4비트는 PC(Program counter)의 앞의 4비트를 가져온다.

## J-format instructions
> - j
>> - j L1

|op|label(address)|
|---|---|
|cmd|L1|