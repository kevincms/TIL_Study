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
>> - 문제 발생 : 16비트 상수값으로 32비트 레지스터와 연산을 해야됨. ([3.extensio.md 참조](../Basic_Operations/3.%20extension.md))




## I-format instructions
> - addi, addiu, subi, subiu
> - ori, andi
>> - cmd $1, $2, 100
|op|rs|rt|constant or address|
|---|--:|--:|--:|
|cmd|$2|$1|100|

## Example
### 어셈블리어 -> 기계어
- ori $1, $2, 0x8000

|field|op|rs|rt|constant or address|
|---|--:|--:|--:|--:|
|cmd|ori|$2|$1|0x8000|
|num|13|2|1|0x8000|
|bit|001101|00010|00001|1000 0000 0000 0000|

> - 2진수
>> - 001101 00010 00001 1000 0000 0000 0000
>> - 0011 0100 0100 0001 1000 0000 0000 0000

- 기계어 : 0x34418000

### 기계어 -> 어셈블리어
