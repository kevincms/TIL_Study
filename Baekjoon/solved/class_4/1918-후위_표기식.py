# https://www.acmicpc.net/problem/1918
import sys
from collections import deque

def is_op(op):
    if op=="+" or op=="-" or op=="/" or op=="*": return True
    return False

def priority(op):
    if op=="+" or op=="-": return 1
    elif op=="*" or op=="/": return 2
    return 0

input=sys.stdin.readline
calc=input().strip()
stack=deque([])
output=""
for i in calc:
    if i=="(":
        stack.append(i)
    elif i==")":
        while stack[-1]!="(":
            output+=stack.pop()
        stack.pop()
    elif is_op(i):
        if not stack: stack.append(i)
        else:
            while stack and priority(i)<=priority(stack[-1]): output+=stack.pop()
            stack.append(i)
    else: output+=i
while stack: output+=stack.pop()
print(output)