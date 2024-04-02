'''
문제
 -정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
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
'''

class Cir_Queue():
    def __init__(self) -> None:
        self.Front=0
        self.rear=0
        self.capacity=2000000
        self.queue=[None]*self.capacity
        self.Size=0

    def empty(self):
        return self.Front==self.rear
    
    def full(self):
        return self.Front==(self.rear+1)%self.capacity
    
    def push(self,data):
        self.queue[self.rear]=data
        self.rear=(self.rear+1)%self.capacity
        self.Size+=1

    def pop(self):
        if self.empty(): return -1
        e=self.queue[self.Front]
        self.Front=(self.Front+1)%self.capacity
        self.Size-=1
        return e
    
    def front(self):
        if self.empty(): return -1
        else: return self.queue[self.Front]

    def back(self):
        if self.empty(): return -1
        else: return self.queue[(self.rear-1+self.capacity)%self.capacity]

    def size(self):
        return self.Size
    
import sys
input=sys.stdin.readline
input_t=int(input())
Q=Cir_Queue()
for i in range(input_t):
    input_cmd=list(map(str,input().split()))
    if len(input_cmd)==1:
        cmd=input_cmd[0]
        if cmd=="pop": print(Q.pop())
        elif cmd=="size": print(Q.size())
        elif cmd=="empty": print(int(Q.empty()))
        elif cmd=="front": print(Q.front())
        else: print(Q.back())
    else:
        Q.push(input_cmd[1])


""" 연결리스트
class linklist():
    def __init__(self,data,next) -> None:
        self.data=data
        self.next=next

class Queue():
    def __init__(self) -> None:
        self.Front=None
        self.rear=None
        self.Size=0

    def empty(self):
        return self.Front==None
    
    def push(self,data):
        node=linklist(data,None)
        if self.empty():
            self.Front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node
        self.Size+=1

    def pop(self):
        if self.empty(): return -1
        e=self.Front
        if(self.Size==1):
            self.Front=None
            self.rear=None
        else:
            self.Front=self.Front.next
        self.Size-=1
        return e.data
    
    def front(self):
        if self.empty(): return -1
        else: return self.Front.data

    def back(self):
        if self.empty(): return -1
        else: return self.rear.data

    def size(self):
        return self.Size
    
import sys
input=sys.stdin.readline
input_t=int(input())
Q=Queue()
for i in range(input_t):
    input_cmd=list(map(str,input().split()))
    if len(input_cmd)==1:
        cmd=input_cmd[0]
        if cmd=="pop": print(Q.pop())
        elif cmd=="size": print(Q.size())
        elif cmd=="empty": print(int(Q.empty()))
        elif cmd=="front": print(Q.front())
        else: print(Q.back())
    else:
        Q.push(input_cmd[1])
"""