/*
문제
 -n행 n열의 격자로 나뉜 운동장이 있다. 이 위에 k개의 돌멩이가 있는데, 하나의 돌멩이는 격자 한 칸에 정확히 들어가 있으며, 두 개 이상의 돌멩이가 한 칸에 들어가 있는 경우는 없다.
사고의 위험을 없애기 위해 이 돌멩이를 모두 제거하고 깨끗한 운동장을 만들려고 한다. 돌멩이를 제거할 때에는, 한 행이나 한 열을 따라 직선으로 달려가면서 그 행이나 열에 놓인 돌멩이를 모두 줍는 방식을 쓴다.
여러분이 할 일은 운동장의 상태가 주어졌을 때 최소 몇 번이나 달려가야 돌멩이 줍기를 끝낼 수 있는지 계산하는 것이다.
입력
 -첫째 줄에 n과 k가 주어진다. (1 ≤ n ≤ 500, 1 ≤ k ≤ 10,000) 이후 k개의 줄에는 돌멩이의 위치가 한 줄에 하나씩 주어진다. 줄마다 첫 번째 숫자는 행 번호, 두 번째 숫자는 열 번호를 나타낸다. 입력으로 주어지는 돌멩이의 위치는 중복되지 않는다.
출력
 -첫 줄에 몇 번의 달리기를 통해 돌멩이를 주울 수 있는지 출력한다.
예제 입력 1
 -3 4
1 1
1 3
2 2
3 2

예제 출력 1
 -2
https://www.acmicpc.net//problem/1867
*/