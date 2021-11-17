'''
문제
 -Mr. Dajuda, who is famous for a TV show program, occasionally suggests an interesting game for the audience and gives them some gifts as a prize. The game he suggested this week can be explained as follows.
입력
 -Your program is to read from standard input. The input starts with a line containing two integers, k and n (3 < k ≤ 5,000, 1 ≤ n ≤ 10,000), where k is the number of lamps and n the number of game participants. Each of the following n lines contains three pairs of (l, c), where l is the lamp number he/she selected and c is a character, either B for blue or R for red, which denotes the color he/she guessed for the lamp. There is a blank between l and c and each pair of (l, c) is separated by a blank as well as shown in following samples.
출력
 -Your program is to write to standard output. If it is possible that all the colors can be adjusted so that every participant can receive a prize, print k characters in a line. The ith character, either B for blue or R for red represents the color of the ith lamp. If impossible, print -1. If there are more than one answer, you can print out any of them.
예제 입력 1
 -7 5
3 R 5 R 6 B
1 B 2 B 3 R
4 R 5 B 6 B
5 R 6 B 7 B
1 R 2 R 4 R

예제 출력 1
 -BRRRBBB

예제 입력 2
 -5 6
1 B 3 R 4 B
2 B 3 R 4 R
1 B 2 R 3 R
3 R 4 B 5 B
3 B 4 B 5 B
1 R 2 R 4 R

예제 출력 2
 --1

https://www.acmicpc.net//problem/16367
'''