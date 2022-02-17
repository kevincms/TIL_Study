/*
문제
 -집합 S는 크기가 N이고, 원소가 문자열인 집합이다. Q개의 문자열이 주어졌을 때, 각 문자열의 부분 문자열이 집합 S에 있는지 판별하는 프로그램을 작성하시오. 문자열의 여러 부분 문자열 중 하나라도 집합 S에 있으면 'YES'를 출력하고, 아무것도 없으면 'NO'를 출력한다.
예를 들어, 집합 S = {"www","woo","jun"} 일 때, "myungwoo"의 부분 문자열인 "woo" 가 집합 S에 있으므로 답은 'YES'이고, "hongjun"의 부분 문자열 "jun"이 집합 S에 있으므로 답은 'YES'이다. 하지만, "dooho"는 모든 부분 문자열이 집합 S에 없기 때문에 답은 'NO'이다.
입력
 -첫째 줄에 집합 S의 크기 N이 주어진다. (1 ≤ N ≤ 1000)
다음 N개 줄에 집합 S의 원소들이 주어진다. 이 문자열의 길이는 100을 넘지 않는다.
다음 줄에 답을 판별해야 하는 문자열의 개수 Q가 주어진다. (1 ≤ Q ≤ 1000)
다음 Q개 줄에 답을 판별해야 하는 문자열이 주어진다. 이 문자열의 길이는 10000을 넘지 않는다.
입력으로 주어지는 모든 문자열은 알파벳 소문자로만 이루어져 있다.
출력
 -Q개 줄에 각 문자열에 대한 답을 출력한다.
예제 입력 1
 -3
www
woo
jun
3
myungwoo
hongjun
dooho

예제 출력 1
 -YES
YES
NO

https://www.acmicpc.net//problem/9250
*/