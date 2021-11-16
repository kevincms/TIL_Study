'''
문제
 -(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
입력
 -첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
출력
 -첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
예제 입력 1
 -5 8 4
예제 출력 1
 -
1
1
0
0
'''

input_num_list=input().split()
num=[]
for i in input_num_list:
    num.append(int(i))
a=num[0]
b=num[1]
c=num[2]
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)