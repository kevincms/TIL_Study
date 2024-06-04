# add : 레지스터끼리 더하는 명령어
> - add (1), (2), (3) # 주석 달수 있음
>> - (1) : destination operands
>> - (2), (3) : sorce operands
>> - (1), (2), (3) 모두 레지스터이어야 한다.

> - ex) add $2, $4, $2
>> - 5번째와 3번째 레지스터를 더해서 3번째 레지스터에 저장

# addi : 레지스터에 상수를 더하는 명령어
> - addi (1), (2), (3) 
>> - (1) : destination operands
>> - (2), (3) : sorce operands
>> - (3) = 상수, (1), (2) = 레지스터

> - ex) addi $2, $4, 32
>> - 5번째 레지스터에 32를 더한 값을 3번째 레지스터에 저장

### 레지스터 값 복사 or 할당
- $0가 항상 0인것을 이용해서 원하는 레지스터에 값을 할당할 수 있다.
- ex) addi $2, $0, 24

# sub : 레지스터끼리 빼는 명령어
- add와 문법 동일.
> - sub (1), (2), (3)
>> - (1) : destination operands
>> - (2), (3) : sorce operands
>> - (1), (2), (3) 모두 레지스터이어야 한다.

> - ex) add $2, $4, $2
>> - 5번째와 3번째 레지스터를 빼서 3번째 레지스터에 저장

# subi : 없음. addi로 대체 가능
- 음수를 더하면 subu 연산을 할 수 있기 때문에 따로 명령어가 없다

# unsigned
- 아래의 연산들은 unsigned 지만 음수인 상수 혹은 레지스터로 연산이 가능하다.
- 이유는 레지스터의 값을 부호가 없는 unsigned로 해석하여 사용하기 때문인 것으로 추정.
## addu : overflow를 무시하는 add 연산
## addiu : overflow를 무시하는 addi 연산
## subu : overflow를 무시하는 sub 연산

# mult : 레지스터끼리 곱하는 명령어
> - mult (1), (2)
>> - (1), (2) : sorce operands
> - destination operands가 정해져 있다.
>> - HI 와 LO 레지스터에 저장된다.
>> - HI : 연산결과의 최상단 32bit를 저장하는 레지스터
>> - LO : 연산결과의 최하단 32bit를 저장하는 레지스터

# mfhi, mflo : mult 연산 결과를 가져오는 명령어
- move from hi(lo)
> - mfhi (1)
>> - (1) : destination operands