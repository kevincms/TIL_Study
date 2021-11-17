'''
문제
 -Suffix Array란, 문자열 S가 있을 때 그 접미사들을 정렬해 놓은 배열이다. 예를 들어, 문자열 S=banana의 접미사는 아래와 같이 총 6개가 있다.
입력
 -첫째 줄에 알파벳 소문자로만 이루어진 문자열 S가 주어진다. S의 길이는 50만보다 작거나 같다.
출력
 -첫째 줄에는 Suffix Array를, 둘째 줄에는 LCP Array를 공백으로 구분하여 출력한다. LCP Array의 첫 값은 항상 'x'이다.
예제 입력 1
 -abracadabra

예제 출력 1
 -11 8 1 4 6 9 2 5 7 10 3
x 1 4 1 1 0 3 0 0 0 2

https://www.acmicpc.net//problem/9248
'''