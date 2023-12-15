### Stack
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

### Queue
<img src="https://raw.githubusercontent.com/kevincms/image/main/%EC%9D%B4%EB%A1%A0/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0/queue.png" style="float: right" width="40%" height="40%"/>

- Stack의 영어 뜻은 명사로 **줄, 대기** 동사로 **줄을 서서 기다리다**
- 줄의 경우 가장 먼저 도착한 사람이 가장 먼저 들어가고 가장 마지막에 도착한 사람이 가장 마지막에 들어갈 수 있음

#### 특징 및 용어
- 선입선출 FIFO(First in First Out)
- 가장 앞에 있는(먼저 들어온) 자료 Front. 가장 뒤에 있는(나중에 들어온) 자료 Back 혹은 Rear.
- Front에서 삭제가 이루어지고 Rear(Back)에서는 삽입이 이루어진다.
- 삽입연산 = Enqueue, 삭제연산 = Dequeue

#### Python
> - list
>> - Front : queue[0]
>> - Rear(Back) : queue[-1]
>> - Enqueue : queue.append(data)
>> - Dequeue : queue.pop(0)