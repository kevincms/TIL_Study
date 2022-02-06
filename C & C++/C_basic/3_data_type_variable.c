#include <stdio.h>

int main(){
    int count=1, test_int=10;
    printf("%d. %d | size: %d\n",count++,test_int,sizeof(test_int)); // 1. 정수형 변수

    
    printf("%d. %d",count++,test_int); // 2. 정수형 변수
}