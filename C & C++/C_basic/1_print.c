#include <stdio.h>

int main(){
    int count=1;
    printf("1. test\n"); // 1. ���ڿ� ���
    printf("%d. ���� : %d\n",++count,10); // 2. ���� ���� ���
    printf("%d. �Ǽ� : %f\n",count++,3.14); // 3. �Ǽ� ���� ���
    printf("%d. ���� : %c\n",count++,'c'); // 4. ���� ���� ���
    printf("%d. ���ڿ� : %s\n",count++,"string"); // 5. ���ڿ� ���� ���


    printf("%d. ���� : %g\n",count++,3.14); // 6. �Ǽ� ���� ��� (�ڸ����� �°�)
}