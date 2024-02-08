#include <iostream>
using namespace std;

int main(){
    int count=1, int_array[30]={1,2,3,}; // 1. {}를 통해 초기 값을 설정할 수 있다.
    printf("%d. ",count++);
    for(int i=0; i<30; i++) printf("%d ",int_array[i]);

    printf("\n%d. ",count++);
    int_array[3]=4; // 2. 배열에 값을 대입해 변경할 수 있다.
    for(int i=0; i<30; i++) printf("%d ",int_array[i]);
    
    char string[30]="Hello World!"; // 3. 문자 배열을 이용해 문자열을 출력할 수 있다.
    printf("\n%d. %s\n ",count++,string);
}