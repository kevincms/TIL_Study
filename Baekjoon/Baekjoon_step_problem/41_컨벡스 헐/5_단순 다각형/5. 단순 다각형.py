'''
문제
 -평면 위의 점의 집합이 주어졌을 때, 다각형을 만드는 프로그램을 작성하시오. 집합의 모든 점은 다각형의 꼭짓점이어야 하고, 집합에 없는 점을 다각형의 꼭짓점으로 가질 수 없다. 다각형의 두 선분은 연속하는 두 선분의 교점을 제외하고는 교차할 수 없다.
입력
 -첫째 줄에 테스트 케이스의 개수 c (1 ≤ c ≤ 200)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있다. 테스트 케이스의 첫 번째 숫자는 점의 개수 n (3 ≤ n ≤ 2000) 이다. 다음 숫자는 점의 좌표 x와 y이며, 좌표는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
출력
 -각 테스트 케이스마다 0부터 n-1까지 순열중 하나를 출력해야 한다. 출력하는 순열은 입력으로 주어지는 점의 번호를 나타내며, 출력하는 순서대로 점을 이었을 때, 올바른 다각형을 만들어야 한다.
예제 입력 1
 -2
4 0 0 2 0 0 1 1 0
5 0 0 10 0 10 5 5 -1 0 5

예제 출력 1
 -0 3 1 2
3 1 2 4 0

'''