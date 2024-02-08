#include <iostream>
using namespace std;

int main(){
    // 정수
    int count=1, test_int=10;
    printf("%d. %d | size: %d\n",count++,test_int,sizeof(test_int)); // 1. 정수형 변수
    
    // long = long int, long long = long long int 
    long test_long=10;
    printf("%d. %d | size: %d\n",count++,test_long,sizeof(test_long)); // 2. 이상하고 사연이 많은 정수형 변수
    // 윈도우에서는 4바이트인데 맥에서는 8바이트이다.
    // 윈도우 기존으로 int와 같은 4byte인데 따로 있는 이유는 32bit 64bit 운영체제에 불협화음으로 추정. [참고 : https://hackerpark.tistory.com/entry/C%EC%96%B8%EC%96%B4-int-%EC%99%80-long-%EC%9D%80-%EB%AC%B4%EC%97%87%EC%9D%B4-%EB%8B%A4%EB%A5%BC%EA%B9%8C-short-short-int-int-long-int-long-long-long]

    long long test_longlong=10;
    printf("%d. %d | size: %d\n",count++,test_longlong,sizeof(test_longlong)); // 3. 더 커진 정수형 변수

    unsigned int test_usint=10;
    printf("%d. %d | size: %d\n",count++,test_usint,sizeof(test_usint)); // 4. 음수가 없는 정수형 변수

    // 실수
    float test_float=3.14;
    printf("%d. %f | size: %d\n",count++,test_float,sizeof(test_float)); // 5. 실수

    double test_double=3.14;
    printf("%d. %f | size: %d\n",count++,test_double,sizeof(test_double)); // 6. 정확한 실수

    long double test_longdouble=3.14;
    printf("%d. %f | size: %d\n",count++,test_longdouble,sizeof(test_longdouble)); // 7. 더 정확한 실수
    // 컴파일러의 지원여부에 따라 long double이 16byte가 되는 것으로 추정

    // 문자
    char test_char='a';
    printf("%d. %c\n",count++,test_char); // 8. 문자
}