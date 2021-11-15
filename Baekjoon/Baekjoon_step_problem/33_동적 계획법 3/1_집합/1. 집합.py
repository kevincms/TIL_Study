'''
문제
 -비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
입력
 -첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
출력
 -check 연산이 주어질때마다, 결과를 출력한다.
예제 입력 1
 -26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1

예제 출력 1
 -1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0

'''