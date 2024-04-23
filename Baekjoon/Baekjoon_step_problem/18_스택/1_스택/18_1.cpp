/*
문제
 -정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
 -첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
출력
 -출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
예제 입력 1
 -14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top

예제 출력 1
 -2
2
0
2
1
-1
0
1
-1
0
3

예제 입력 2
 -7
pop
top
push 123
top
pop
top
pop

예제 출력 2
 --1
-1
123
123
-1
-1

https://www.acmicpc.net//problem/10828
*/

#include <iostream>
#include <string>
using namespace std;

class linked_list{
    friend class Stack;
private:
    int data;
    linked_list *next;
public:
    linked_list(int data){this->data=data;next=NULL;}
};

class Stack{
private:
    int size;
    linked_list *Top;
public:
    Stack(){size=0;Top=NULL;}
    ~Stack(){while(!empty()) pop();}
    void push(linked_list *node);
    int pop();
    int Size(){return size;}
    bool empty(){return Top==NULL;}
    int top();
};

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int input_t;
    string input_str;
    Stack stack;
    cin>>input_t;
    for (size_t t = 0; t < input_t; t++){
        cin>>input_str;
        if(input_str=="push"){
            cin>>input_str;
            stack.push(new linked_list(stoi(input_str)));
        }
        else if(input_str=="pop") cout<<stack.pop()<<"\n";
        else if(input_str=="size") cout<<stack.Size()<<"\n";
        else if(input_str=="empty") cout<<stack.empty()<<"\n";
        else cout<<stack.top()<<"\n";
    }
    
    return 0;
}

void Stack::push(linked_list *node){
    node->next=Top;
    Top=node;
    size++;
}

int Stack::pop(){
    if(empty()) return -1;
    int temp=Top->data;
    Top=Top->next;
    size--;
    return temp;
}

int Stack::top(){
    if(empty()) return -1;
    return Top->data;
}