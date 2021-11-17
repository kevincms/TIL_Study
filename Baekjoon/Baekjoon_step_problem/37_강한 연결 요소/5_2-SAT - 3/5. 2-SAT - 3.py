'''
문제
 -2-SAT은 N개의 불리언 변수 \(x_1, x_2, ..., x_n\)가 있을 때, 2-CNF 식을 true로 만들기위해 \(x_i\)를 어떤 값으로 정해야하는지를 구하는 문제이다.
입력
 -첫째 줄에 변수의 개수 N (1 ≤ N ≤ 10,000)과 절의 개수 M (1 ≤ M ≤ 100,000)이 주어진다. 둘째 줄부터 M개의 줄에는 절이 주어진다. 절은 두 정수 i와 j (1 ≤ |i|, |j| ≤ N)로 이루어져 있으며, i와 j가 양수인 경우에는 각각 \(x_i\), \(x_j\)를 나타내고, 음수인 경우에는 \(\lnot x_{-i}\), \(\lnot x_{-j}\)를 나타낸다.
출력
 -첫째 줄에 식 \(f\)를 true로 만들 수 있으면 1을, 없으면 0을 출력한다.
예제 입력 1
 -3 4
-1 2
-2 3
1 3
3 2

예제 출력 1
 -1

예제 입력 2
 -1 2
1 1
-1 -1

예제 출력 2
 -0

https://www.acmicpc.net//problem/11280
'''