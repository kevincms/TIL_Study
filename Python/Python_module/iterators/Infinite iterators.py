import itertools

# 1. count(start_num,step_num)
count=1
loop_count=0
print("%d-1."%count,end=" ")
for i in itertools.count(10):
    print(i,end=" ")
    loop_count+=1
    if loop_count==3: break

loop_count=0
print("\n%d-2."%count,end=" ")
for i in itertools.count(10,2):
    print(i,end=" ")
    loop_count+=1
    if loop_count==3: break

# 2. cycle(string)
count+=1
loop_count=0
print("\n\n%d."%count,end=" ")
for i in itertools.cycle("test"):
    print(i,end=" ")
    loop_count+=1
    if loop_count==6: break

# 3. repeat(element,num)
count+=1
loop_count=0
print("\n\n%d-1."%count,end=" ")
for i in itertools.repeat("test"):
    print(i,end=" ")
    loop_count+=1
    if loop_count==3: break

loop_count=0
print("\n%d-2."%count,end=" ")
for i in itertools.repeat([123]):
    print(i,end=" ")
    loop_count+=1
    if loop_count==3: break

print("\n{}-3. {}".format(count,itertools.repeat(2,3)))