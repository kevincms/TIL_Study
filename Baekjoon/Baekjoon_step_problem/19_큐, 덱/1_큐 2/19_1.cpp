/*
문제
 -정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
 -첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 2,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
출력
 -출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
예제 입력 1
 -15
push 1
push 2
front
back
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
front

예제 출력 1
 -1
2
2
0
1
2
-1
0
1
-1
0
3

https://www.acmicpc.net//problem/18258
*/
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Queue{
private:
    int size, capacity=2000000;
    int front, rear;
    vector<int> queue;
public:
    Queue();
    ~Queue(){while(!empty()) pop();}
    void push(int data);
    int pop();
    int Size(){return size;}
    bool empty(){return rear==front;}
    int Front();
    int back();
};

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int input_t;
    string input_str;
    Queue queue;
    cin>>input_t;
    for (size_t t = 0; t < input_t; t++){
        cin>>input_str;
        if(input_str=="push"){
            cin>>input_str;
            queue.push(stoi(input_str));
        }
        else if(input_str=="pop") cout<<queue.pop()<<"\n";
        else if(input_str=="size") cout<<queue.Size()<<"\n";
        else if(input_str=="empty") cout<<queue.empty()<<"\n";
        else if(input_str=="front") cout<<queue.Front()<<"\n";
        else cout<<queue.back()<<"\n";
    }
    
    return 0;
}

Queue::Queue(){
    queue.resize(capacity);
    front=0;
    rear=0;
    size=0;
}

void Queue::push(int data){
    queue[rear++]=data;
    rear=rear%capacity;
    size++;
}

int Queue::pop(){
    if(empty()) return -1;
    int temp=queue[front++];
    front=front%capacity;
    size--;
    return temp;
}

int Queue::Front(){
    if(empty()) return -1;
    return queue[front];
}

int Queue::back(){
    if(empty()) return -1;
    return queue[(rear-1+capacity)%capacity];
}