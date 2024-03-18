#include <iostream>
#include <string>
#include <curses.h>

using namespace std;

int main(){
    initscr(); // 시작

    // newwin(height, width, y, x); x y 좌표에 window 생성
    WINDOW *win=newwin(5,30,0,0); // 윈도우 생성

    // print처럼 순자적인 출력외에 특정 좌표를 출력 할 수 있음.
    string test="Hello by wprintw";
    // wprintw의 경우 char 배열의 값을 argument로 전달해야 함.
    mvwprintw(win, 1, 0, test.c_str()); // string의 경우 char 배열로 변환 필요.
    mvwprintw(win, 0, 0, "long string by wprintw"); // 윈도우 height 범위를 벗어나면 자동 줄바꿈


    refresh(); // 일반 새로고침 후 
    wrefresh(win); // 윈도우 새로고침
    getch();
    
    endwin(); // 끝
}