/*
문제
 -N개의 정점으로 이루어진 트리(무방향 사이클이 없는 연결 그래프)가 있다. 정점은 1번부터 N번까지 번호가 매겨져 있고, 간선은 1번부터 N-1번까지 번호가 매겨져 있다.
아래의 두 쿼리를 수행하는 프로그램을 작성하시오.

1 u v: u에서 v로 가는 경로의 비용을 출력한다.
2 u v k: u에서 v로 가는 경로에 존재하는 정점 중에서 k번째 정점을 출력한다. k는 u에서 v로 가는 경로에 포함된 정점의 수보다 작거나 같다.
입력
 -첫째 줄에 N (2 ≤ N ≤ 100,000)이 주어진다.
둘째 줄부터 N-1개의 줄에는 i번 간선이 연결하는 두 정점 번호 u와 v와 간선의 비용 w가 주어진다.
다음 줄에는 쿼리의 개수 M (1 ≤ M ≤ 100,000)이 주어진다.
다음 M개의 줄에는 쿼리가 한 줄에 하나씩 주어진다.
간선의 비용은 항상 1,000,000보다 작거나 같은 자연수이다.
출력
 -각각의 쿼리의 결과를 순서대로 한 줄에 하나씩 출력한다.
예제 입력 1
 -6
1 2 1
2 4 1
2 5 2
1 3 1
3 6 2
2
1 4 6
2 4 6 4

예제 출력 1
 -5
3

https://www.acmicpc.net//problem/13511
*/