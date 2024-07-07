# https://www.acmicpc.net/problem/11723

class SET():
    def __init__(self): self.data=[False]*21
    def add(self,x): self.data[x]=True
    def remove(self,x): self.data[x]=False
    def check(self,x):return (1 if self.data[x] else 0)
    def toggle(self,x): self.data[x]=not self.data[x]
    def all(self): self.data=[True]*21
    def empty(self): self.data=[False]*21

import sys

input=sys.stdin.readline
num=int(input())
set=SET()
for i in range(num):
    cmd_line=list(input().split())
    if len(cmd_line)==2: x=int(cmd_line[1])
    cmd=cmd_line[0]
    if cmd=="add": set.add(x)
    elif cmd=="remove": set.remove(x)
    elif cmd=="check": print(set.check(x))
    elif cmd=="toggle": set.toggle(x)
    elif cmd=="all": set.all()
    elif cmd=="empty": set.empty()