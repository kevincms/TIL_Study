count=1
# Stack
stack=[] # 5tack을 list로 구현

stack.append(3) # Push
print(f"{count}. {stack}")
count=count+1

print(f"{count}. {stack[-1]}") # Top
count=count+1

stack.pop() # Pop
print(f"{count}. {stack}")
count=count+1