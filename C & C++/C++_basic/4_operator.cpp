#include <iostream>
using namespace std;

int main(){
    int count=1;
    // 사칙연산 and 특수연산
    printf("%d. %d\n",count++,1+1); // 1. 덧셈
    printf("%d. %d\n",count++,3-1); // 2. 뺄셈
    printf("%d. %d\n",count++,1*5); // 3. 곱셈
    printf("%d. %d %g\n",count++,5/2,5.0/2); // 4. 나눗셈 (연산되는 변수, 상수의 type에 따라 나오는 출력값이 달라짐)
    printf("%d. %d\n",count++,5%3); // 5. 나머지
    
    // 비교연산(관계연산)
    printf("%d. %d %d\n",count++,1>1,1>=1); // 6. 부등호
    printf("%d. %d %d\n",count++,1==1,1!=1); // 7. 등호

    // 논리연산
    printf("%d. %d\n",count++,!0); // 8. not
    printf("%d. %d\n",count++,1 && 1); // 9. and
    printf("%d. %d\n",count++,1 || 0); // 10. or

    // 비트연산
    printf("%d. %d\n",count++,~3); // 11. not gate
    printf("%d. %d\n",count++,7 & 4); // 12. not gate
    printf("%d. %d\n",count++,7 | 4); // 13. and gate
    printf("%d. %d\n",count++,7 ^ 4); // 14. or gate
    printf("%d. %d %d\n",count++,4<<1,4>>1); // 15. shift
    
}