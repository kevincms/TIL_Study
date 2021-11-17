'''
문제
 -Naughty mouse Jerry and his friend mice sometimes visit a vacant house to play the famous children game ‘hide and seek’ and also to adjust the length of their teeth by gnawing furniture and chairs left there. If we look down the house from the sky the boundary of it composes an orthogonal polygon parallel to the xy-axes as shown in the figure below. In other words, every wall of the house is either horizontal or vertical.
입력
 -Your program is to read from standard input. The input starts with a line containing four integers, n, k, h, and m, where n(1 ≤ n ≤ 1,000) is the number of the corner points of a house, k(1 ≤ k ≤ 5) the maximum number of mice each hole can afford, h(1 ≤ h ≤ 50) the number of holes, m(1 ≤ m ≤ k ∙ h) the number of mice. In each of the following n lines, each coordinate of the corner points of the house is given in counter clockwise order. Each point is represented by two integers separated by a single space, which are the x- coordinate and the y-coordinate of the point, respectively. Each coordinate is given as an integer between -109 and 109, inclusively. In each of the following h lines, two integers x and y are given, which represent the coordinate (x, y) of each hole. In each of the following m lines, two integers x and y are given, which represent the coordinate (x, y) of each mouse.
출력
 -Your program is to write to standard output. Print exactly one line for the input. Print Possible if all the mice can hide into the rat’s holes holding the constraints explained above. Otherwise print Impossible.
예제 입력 1
 -6 1 3 3
0 0
100 0
100 50
40 50
40 70
0 70
0 55
55 50
80 50
15 65
90 10
92 10

예제 출력 1
 -Possible

예제 입력 2
 -6 1 3 3
0 0
100 0
100 50
40 50
40 70
0 70
0 55
55 50
80 50
15 65
90 10
30 66

예제 출력 2
 -Impossible

https://www.acmicpc.net//problem/14750
'''