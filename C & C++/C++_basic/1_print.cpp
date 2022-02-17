#include <iostream>
using namespace std;

int main(){
    int count=1;
    cout<<"1. test"<<endl; // 1. 문자열 출력
    cout<<++count<<". 정수 : "<<10<<"\n"; // 2. 정수 변수 출력
    printf("%d. 실수 : %f\n",count++,3.14); // 3. 실수 변수 출력
    printf("%d. 문자 : %c\n",count++,'c'); // 4. 문자 변수 출력
    printf("%d. 문자열 : %s\n",count++,"string"); // 5. 문자열 변수 출력
    printf("%d. 문자 : %g\n",count++,3.14); // 6. 실수 변수 출력 (자리수에 맞게)
}