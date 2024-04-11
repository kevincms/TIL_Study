from collections import deque

count=1
# Stack
stack=[] # list로 구현한 stack

stack.append(3) # 1. Push
print(f"{count}. {stack}")
count=count+1

print(f"{count}. {stack[-1]}") # 2. Top
count=count+1

stack.pop() # 3. Pop (Pop을 출력할 경우 빼내기 전 Top에 있는 자료를 출력한다.)
print(f"{count}. {stack}")
count=count+1

# Queue
queue=[] # list로 구현한 queue

queue.append(3) # 4. Enqueue
queue.append(2)
print(f"{count}. {queue}")
count=count+1

print(f"{count}. {queue[0]}") # 5. Front
count=count+1

print(f"{count}. {queue[-1]}") # 6. Rear(Back)
count=count+1

queue.pop(0) # 7. Dequeue
print(f"{count}. {queue}")
count=count+1

# Deque
test_deque=deque([2,3])
test_deque.append(4) # 8. append
print(f"{count}. {test_deque}")
count=count+1

test_deque.appendleft(1) # 9. appendleft
print(f"{count}. {test_deque}")
count=count+1

test_deque.rotate(1) # 10. rotate [양수면 오른쪽, 음수면 왼쪽 회전]
print(f"{count}. {test_deque}")
count=count+1

test_deque.pop() # 11. pop
print(f"{count}. {test_deque}")
count=count+1

test_deque.popleft() # 12. popleft
print(f"{count}. {test_deque}")
count=count+1

print(f"{count}. {test_deque} {test_deque[0]}") # 13. 요소의 접근은 list와 동일하다.
count=count+1

# Stack
stack=deque([]) # list로 구현한 stack

stack.append(3) # 14. Push
print(f"{count}. {stack}")
count=count+1

print(f"{count}. {stack[-1]}") # 15. Top
count=count+1

stack.pop() # 16. Pop (Pop을 출력할 경우 빼내기 전 Top에 있는 자료를 출력한다.)
print(f"{count}. {stack}")
count=count+1

# Queue
queue=deque([]) # list로 구현한 queue

queue.append(3) # 17. Enqueue
queue.append(2)
print(f"{count}. {queue}")
count=count+1

print(f"{count}. {queue[0]}") # 18. Front
count=count+1

print(f"{count}. {queue[-1]}") # 19. Rear(Back)
count=count+1

queue.popleft() # 20. Dequeue
print(f"{count}. {queue}")
count=count+1

from queue import PriorityQueue
# PriorityQueue
prqueue=PriorityQueue()

print(f"{count}. {prqueue.empty()}") # 21. prqueue empty 확인
count=count+1

prqueue.put(5) # prqueue 요소 삽입
print(f"{count}. {prqueue.get()}") # 22. prqueue 요소 삭제 및 반환
count=count+1

prqueue=PriorityQueue(maxsize=2) # 만약 maxsize를 초과하여 put을 시도하면 무한대기에 걸린다.
prqueue.put(1)
prqueue.put(2)
print(f"{count}. {prqueue.full()}") # 23. prqueue full 확인
count=count+1