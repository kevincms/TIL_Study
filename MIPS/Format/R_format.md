# Instruction fields

|field|op|rs|rt|rd|shamt|funct|
|---|--:|--:|--:|--:|--:|--:|
|bit|6|5|5|5|5|6|

> 1. op: operation code (opcode)
>> - opcode를 통해 format을 파악한다.
> 2. rs: first source register number
>> - register source의 약자
> 3. rt: second source register number
>> - s 다음 알파벳이 t이기 떄문에 register t사용
> 4. rd: destination register number
>> - register destination의 약자
> 5. shamt: shift amount (00000 for now)
> 6. funct: function code (extends opcode)
>> - extends opcode를 통해 어떤 command인지 파악한다.


## Example
- add $1, $2, $3

|field|op|rs|rt|rd|shamt|funct|
|---|--:|--:|--:|--:|--:|--:|
|cmd|special|$2|$3|$1|0|add|
|num|0|2|3|1|0|32|
|bit|000000|00010|00011|00001|00000|100000|
