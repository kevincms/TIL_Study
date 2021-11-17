'''
문제
 -There are a number of electronic circuits, such as CPU’s, ROM’s, RAM’s, to be printed in a single chip consisting of multiple layers. Due to some design restriction, there can be only two electrical wires that are horizontal segments. Your job is to find two horizontal wires that together connect as many circuits as possible so that the electric signals go through the circuits.
입력
 -Your program is to read from standard input. The first line contains a positive integer n representing the number of axis-aligned rectangles in the plane, where 3 ≤ n ≤ 100,000. It is followed by n lines, each contains four integers ux, uy, vx and vy (with ux < vx and uy > vy) representing the (x, y)-coordinates, (ux, uy), of the top-left corner and the (x, y)-coordinates, (vx, vy), of the bottom-right corner of an axisaligned rectangle, where −10,000,000 ≤ ux, uy, vx, vy ≤ 10,000,000.
출력
 -Your program is to write to standard output. Print exactly one line. The line should contain the maximum total number of rectangles that can be intersected by two horizontal lines.
예제 입력 1
 -5
0 13 4 4
2 14 11 9
7 17 12 12
3 5 16 0
5 2 13 1

예제 출력 1
 -5

예제 입력 2
 -5
0 4 4 0
1 3 3 1
5 8 9 4
0 12 4 8
1 11 3 9

예제 출력 2
 -4

https://www.acmicpc.net//problem/16357
'''