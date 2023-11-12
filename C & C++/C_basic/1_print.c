#include <stdio.h>

int main(){
    int count=1;
    printf("1. test\n"); // 1. 문자열 출력
    printf("%d. 정수 : %d\n",++count,10); // 2. 정수 변수 출력
    printf("%d. 실수 : %f\n",count++,3.14); // 3. 실수 변수 출력
    printf("%d. 문자 : %c\n",count++,'c'); // 4. 문자 변수 출력
    printf("%d. 문자열 : %s\n",count++,"string"); // 5. 문자열 변수 출력


    printf("%d. 문자 : %g\n",count++,3.14); // 6. 실수 변수 출력 (자리수에 맞게)
}