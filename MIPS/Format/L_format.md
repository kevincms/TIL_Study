# Instruction fields

|field|op|rs|rt|constant or address|
|---|--:|--:|--:|--:|
|bit|6|5|5|16|

> 1. op: operation code (opcode)
>> - opcode를 통해 format을 파악한다.
> 2. rs: first source register number
>> - register source의 약자
> 3. rt: second source register number
>> - R-format과 달리 destination register로도 사용할 수 있음.
>> - 기본적으로 source register로도 사용가능.
> 4. constant or address
>> - 상수 혹은 주소값


## L-format instructions
> - addi, addiu, subi, subiu
> - ori, andi
>> - cmd $1, $2, 100
|op|rs|rt|constant or address|
|---|--:|--:|--:|
|cmd|$2|$1|100|

