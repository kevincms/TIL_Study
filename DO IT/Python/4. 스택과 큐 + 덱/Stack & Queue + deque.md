### Stack - 스택
<img src="https://raw.githubusercontent.com/kevincms/image/main/%EC%9D%B4%EB%A1%A0/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0/stack.png" style="float: right" width="40%" height="40%"/>

- Stack의 영어 뜻은 명사로 **무더기** 동사로 **쌓이다**
- 무더기에 경우 가장 먼저 놓은 것이 가장 아래에 있어 꺼낼려면 가장 나중에 꺼낼 수 있고 가장 마지막에 놓은 것이 가장 먼저 꺼낼 수 있음.

#### 특징 및 용어
- 후입선출 LIFO(Last in First Out)
- 가장 마지막에 들어온 자료 = Top
- Top에서만 삽입과 삭제가 일어날 수 있다.
- 삽입연산 = push, 삭제연산 = pop

#### Python
> - list
>> - Top : stack[-1]
>> - push : stack.append(data)
>> - pop : stack.pop()

### Queue - 큐
<img src="https://raw.githubusercontent.com/kevincms/image/main/%EC%9D%B4%EB%A1%A0/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0/queue.png" style="float: right" width="40%" height="40%"/>

- Stack의 영어 뜻은 명사로 **줄, 대기** 동사로 **줄을 서서 기다리다**
- 줄의 경우 가장 먼저 도착한 사람이 가장 먼저 들어가고 가장 마지막에 도착한 사람이 가장 마지막에 들어갈 수 있음

#### 특징 및 용어
- 선입선출 FIFO(First in First Out)
- 가장 앞에 있는(먼저 들어온) 자료 Front. 가장 뒤에 있는(나중에 들어온) 자료 Back 혹은 Rear.
- Front에서 삭제가 이루어지고 Rear(Back)에서는 삽입이 이루어진다.
- 삽입연산 = Enqueue(append), 삭제연산 = Dequeue(popleft)

#### Python
> - list
>> - Front : queue[0]
>> - Rear(Back) : queue[-1]
>> - Enqueue(append) : queue.append(data)
>> - Dequeue(popleft) : queue.pop(0)

### Deque - 덱 or 데크
<img src="https://raw.githubusercontent.com/kevincms/image/main/%EC%9D%B4%EB%A1%A0/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0/deque.png" style="float: right" width="60%" height="60%"/>

- Deque의 영어 뜻은 따로 없다. 자료구조를 정의하기 위해서만 만들어진 단어인 것 같다.

#### 특징 및 용어
- 양방향으로 있는 큐가 합쳐진 형태이다. 어느 방향으로든 데이터를 삽입하고 삭제할 수 있다.
- 따라서 스택과 큐의 연산을 모두 수행할 수 있다.
- 오른쪽 삽입연산 = append, 왼쪽 삽입연산 = appendleft
- 오른쪽 삭제연산 = pop, 왼쪽 삭제연산 = popleft  
---
- 큐의 예시 사진에서는 왼쪽에서 삽입되어 오른쪽으로 나와있지만 기존의 list를 사용하는 방식은 그 반대이므로 반대방향으로 생각하는 것이 편하다.

#### Python
- Deque을 list를 이용해 사용할 수 있는 있지만 collections.deque 모듈이 더 처리가 빠르다
> - deque
>> - 요소 접근 : 리스트와 동일 (ex. deque[0])
>> - append : deque.append(item)
>> - appendleft : deque.appendleft(item)
>> - pop : deque.pop()
>> - popleft : deque.popleft()
>> - 오른쪽으로 deque 추가 : deque.extend(array)
>> - 왼쪽으로 deque 추가 : deque.extendleft(array)
>> - 요소 삭제 : deque.remove(element)
>> - 요소 회전 : deque.rotate(num) (양수 : 시계(오른쪽), 음수 : 반시계(왼쪽))
