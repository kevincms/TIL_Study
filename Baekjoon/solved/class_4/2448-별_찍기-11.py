# https://www.acmicpc.net/problem/2448

import math
num=int(input())
count=int(math.log(num//3,2))
prev=["  *  "," * * ","*****"]

if num==3:
    output="\n".join(prev)
else:
    for i in range(count):
        list_size=3*(2**(i+1))

        temp=(2**(i))
        prev_size=temp*5+(temp-1)
        blank_size=prev_size//2+1
        blank=" "*blank_size

        output=[""]*list_size
        for i in range(list_size):
            if i<list_size//2: output[i]=blank+prev[i]+blank
            else:
                index=i-list_size//2
                output[i]=prev[index]+" "+prev[index]
        prev=output[:]
    output="\n".join(output)
print(output)