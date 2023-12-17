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
queue=[]

queue.append(3) # 4. Enqueue
queue.append(2)
print(f"{count}. {queue}")
count=count+1

print(f"{count}. {queue[0]}") # 5. Front
count=count+1

print(f"{count}. {queue[-1]}") # 6. Rear(Back)
count=count+1

queue.pop(0) # 4. Dequeue
print(f"{count}. {queue}") # 7. Dequeue
count=count+1