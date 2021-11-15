'''
문제
 -The “needle” is a legendary assassin who lives in the North Kingdom. As you know, the needle is very thin and long. More than anything, it is deadly sharp. The king of the North Kingdom is obsessed with the idea that the needle might kill him by stabbing countless times. The king issued an emergency order to arrest the needle. So, the needle decided to escape to the South Kingdom.
입력
 -Your program is to read from standard input. The input consists of six lines. The first line contains a positive integer nu representing the number of holes of the upper barrier. The second line contains nu integers separated by a space that represent the x-coordinates of the holes. The third and fourth lines are for the middle barrier, each containing nm, the number of holes of the middle barrier, and nm x-coodinates of the holes. The fifth and sixth lines are for the lower barrier, each containing nl, the number of holes of the lower barrier, and nl x-coodinates of the holes. 1 ≤ nu, nm, nl ≤ 50,000 and all x-coordinates of the holes are integers between −30,000 and 30,000. Holes of each barrier have all distinct x-coordinates.
출력
 -Your program is to write to standard output. Print exactly one line. The line should contain a nonnegative integer representing the number of all possible passages from the north to the south.
예제 입력 1
 -1
1
1
2
1
1

예제 출력 1
 -0

예제 입력 2
 -3
4 -3 2
2
4 1
3
-3 4 0

예제 출력 2
 -2

예제 입력 3
 -3
-1 1 0
3
0 1 -1
3
0 -1 1

예제 출력 3
 -5

'''