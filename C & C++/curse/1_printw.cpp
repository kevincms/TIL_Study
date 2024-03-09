#include <iostream>
#include <curses.h>

using namespace std;

int main(){
    initscr(); // 시작
    
    printw("Hello World"); // 바로 출력되지 않음
    refresh(); // 새로고침을 해줘야 화면에 출력됨
    getch(); // 새로고침 후 바로 종료. 그걸 중단해야 함. 문자열 입력
    
    endwin(); // 끝
}