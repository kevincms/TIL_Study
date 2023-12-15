count=1
# Stack
stack=[] # 5tack을 list로 구현

stack.append(3) # Push
print(f"{count}. {stack}")
count=count+1

print(f"{count}. {stack[-1]}") # Top
count=count+1

stack.pop() # Pop (Pop을 출력할 경우 빼내기 전 Top에 있는 자료를 출력한다.)
print(f"{count}. {stack}")
count=count+1