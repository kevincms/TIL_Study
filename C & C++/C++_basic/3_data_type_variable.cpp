#include <iostream>
using namespace std;

int main(){
    int count=1, test_int=10;
    printf("%d. %d | size: %d\n",count++,test_int,sizeof(test_int)); // 1. ������ ����
    
    // long = long int, long long = long long int 
    long test_long=10;
    printf("%d. %d | size: %d\n",count++,test_long,sizeof(test_long)); // 2. ������ ����

    long long test_longlong=10;
    printf("%d. %d | size: %d\n",count++,test_longlong,sizeof(test_longlong)); // 2. ������ ����
}