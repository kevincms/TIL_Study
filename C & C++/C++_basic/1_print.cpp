#include <iostream>
using namespace std;

int main(){
    int count=1;
    cout<<"1. test"<<endl; // 1. ���ڿ� ���
    cout<<++count<<". ���� : "<<10<<"\n"; // 2. ���� ���� ���
    printf("%d. �Ǽ� : %f\n",count++,3.14); // 3. �Ǽ� ���� ���
    printf("%d. ���� : %c\n",count++,'c'); // 4. ���� ���� ���
    printf("%d. ���ڿ� : %s\n",count++,"string"); // 5. ���ڿ� ���� ���
    printf("%d. ���� : %g\n",count++,3.14); // 6. �Ǽ� ���� ��� (�ڸ����� �°�)
}