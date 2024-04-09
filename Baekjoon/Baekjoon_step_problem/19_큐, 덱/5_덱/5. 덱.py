'''
문제
 -정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
명령은 총 여덟 가지이다.

push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
 -첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
출력
 -출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
예제 입력 1
 -15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front

예제 출력 1
 -2
1
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
 -22
front
back
pop_front
pop_back
push_front 1
front
pop_back
push_back 2
back
pop_front
push_front 10
push_front 333
front
back
pop_back
pop_back
push_back 20
push_back 1234
front
back
pop_back
pop_back

예제 출력 2
 --1
-1
-1
-1
1
1
2
2
333
10
10
333
20
1234
1234
20

https://www.acmicpc.net//problem/10866
'''
class Deque():
    def __init__(self) -> None:
        self.capacity=10000
        self.deque=[None]*self.capacity
        self.front=0
        self.rear=0
        self.size=0

    def push_front(self,data):
        self.front=(self.front-1+self.capacity)%self.capacity
        self.deque[self.front]=data
        self.size+=1

    def push_back(self,data):
        self.deque[self.rear]=data
        self.rear=(self.rear+1)%self.capacity
        self.size+=1

    def pop_front(self):
        if self.empty(): return -1
        temp=self.deque[self.front]
        self.front=(self.front+1)%self.capacity
        self.size-=1
        return temp
    
    def pop_back(self):
        if self.empty(): return -1
        self.rear=(self.rear-1+self.capacity)%self.capacity
        temp=self.deque[self.rear]
        self.size-=1
        return temp
    
    def Size(self): return self.size
    def empty(self): return self.front==self.rear
    def Front(self):
        if self.empty(): return -1
        else: return self.deque[self.front]
    def back(self):
        if self.empty(): return -1
        else: return self.deque[(self.rear-1+self.capacity)%self.capacity]

import sys
input=sys.stdin.readline
input_t=int(input())
D=Deque()
for i in range(input_t):
    input_cmd=list(map(str,input().split()))
    if len(input_cmd)==1:
        cmd=input_cmd[0]
        if cmd=="pop_front": print(D.pop_front())
        elif cmd=="pop_back": print(D.pop_back())
        elif cmd=="size": print(D.Size())
        elif cmd=="empty": print(int(D.empty()))
        elif cmd=="front": print(D.Front())
        else: print(D.back())
    else:
        cmd=input_cmd[0]
        if cmd=="push_front": D.push_front(input_cmd[1])
        else: D.push_back(input_cmd[1])