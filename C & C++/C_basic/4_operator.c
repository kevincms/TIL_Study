#include <stdio.h>
int main(){
    int count=1;
    printf("%d. %d\n",count++,1+1); // 1. 덧셈
    printf("%d. %d\n",count++,3-1); // 2. 뺄셈
    printf("%d. %d\n",count++,1*5); // 3. 곱셈
    printf("%d. %d %g\n",count++,5/2,5.0/2); // 4. 나눗셈 (연산되는 변수, 상수의 type에 따라 나오는 출력값이 달라짐)
    printf("%d. %d\n",count++,5%3); // 5. 나머지
    
}