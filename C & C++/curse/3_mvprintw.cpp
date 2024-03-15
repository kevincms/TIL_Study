#include <iostream>
#include <curses.h>

using namespace std;

int main(){
    initscr(); // 시작
    
    mvprintw(3,3,"Hello World"); // printw + move
    refresh(); // 새로고침을 해줘야 화면에 출력됨
    getch(); // 새로고침 후 바로 종료. 입력대기 시간을 통해 종료 지연.
    
    endwin(); // 끝
}