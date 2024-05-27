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