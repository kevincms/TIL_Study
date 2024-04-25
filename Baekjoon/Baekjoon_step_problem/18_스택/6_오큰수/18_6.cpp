/*
문제
 -크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.
예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.
입력
 -첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.
출력
 -총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력한다.
예제 입력 1
 -4
3 5 2 7

예제 출력 1
 -5 7 7 -1

예제 입력 2
 -4
9 5 4 8

예제 출력 2
 --1 8 8 -1

https://www.acmicpc.net//problem/17298
*/
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int input_t, t_top;
    cin>>input_t;
    vector<int> num(input_t), output(input_t);
    stack<int> S;
    for (size_t t = 0; t < input_t; t++) cin>>num[t];
    for (int i = input_t-1; i >= 0; i--){
        while (1){
            if(S.empty()){
                output[i]=-1;
                break;
            }
            t_top=S.top();
            if (num[i]<t_top){
                output[i]=t_top;
                break;
            }
            S.pop();
        }
        S.push(num[i]);
    }
    for (size_t t = 0; t < input_t; t++) cout<<output[t]<<" ";
    
    return 0;
}
