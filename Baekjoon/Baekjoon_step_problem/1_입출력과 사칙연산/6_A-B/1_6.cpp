/*
문제
 -두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
입력
 -첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
출력
 -첫째 줄에 A-B를 출력한다.
예제 입력 1
 -3 2

예제 출력 1
 -1
https://www.acmicpc.net//problem/1001
*/

#include <iostream>

using namespace std;
int main(int argc, char const *argv[])
{
    int num1, num2;
    cin>>num1>>num2;
    cout<<num1-num2<<'\n';
    
    return 0;
}